import os
import yaml
import subprocess
import argparse
import math
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Prepare Condor jobs for HLT rerun")
parser.add_argument("--jobFlavour", type=str, default="tomorrow",
                    help="Condor jobflavor (e.g., espresso, longlunch, workday, tomorrow)")
parser.add_argument("--n", type=int, default=10, 
                    help="Number of DAS files per shell script")
parser.add_argument("--farm", type=str, default="Farm",
                    help="Farm directory")
parser.add_argument("--nEvent", type=int, default=100, 
                    help="Number of events per job", required=True)
parser.add_argument("--config", type=str)
parser.add_argument("--proxy", type=str, default=None)
args = parser.parse_args()
jobflavor = args.jobFlavour

# Load YAML config
with open(args.config) as f:
    cfg = yaml.safe_load(f)

cmssw_dir = cfg['cmssw-dir']
eos_dir = cfg['eos-dir']

shell_scripts = []


# -------------------------------
# DAS QUERY WITH EVENT COUNTS
# -------------------------------
def get_das_files_with_events(dataset):
    print(f"Querying DAS for dataset: {dataset}")

    query = f'file dataset={dataset} | grep file.name,file.nevents'
    das_command = f'dasgoclient -query="{query}" -json'

    output = subprocess.check_output(das_command, shell=True)
    data = json.loads(output)

    files = []

    for entry in data:
        file_info = entry['file'][0]
        name = file_info['name']
        nevents = file_info['nevents']

        file_path = f"/eos/cms/{name}"

        if os.path.exists(file_path):
            files.append((f"file:{file_path}", nevents))

    print(f"  → Found {len(files)} accessible files")
    return files


#def get_das_files(dataset):
#  das_command = f'dasgoclient -query="file dataset={dataset}"'
#  files = os.popen(das_command).read().strip().split("\n")
#  accessible = []
#
#  for file in files:
#    file_path = f"/eos/cms/{file}"
#
#    if os.path.exists(file_path):
#        accessible.append(f"file:{file_path}")
#    
#  return accessible

# -------------------------------
# MAIN LOOP
# -------------------------------


for project_name, project_cfg in cfg['project'].items():
    project_eos_dir = os.path.join(eos_dir, project_name)
    os.makedirs(project_eos_dir, exist_ok=True)

    farm_dir = os.path.join(args.farm, project_name)
    os.makedirs(farm_dir, exist_ok=True)
    
    all_input_files = []
    for ds in project_cfg['dataset']:
        all_input_files.extend(get_das_files_with_events(ds))
    
    job_idx = 0

    for file_idx, (infile, events_per_file) in enumerate(all_input_files):

        jobs_per_file = math.ceil(events_per_file / args.nEvent)

        for j in range(jobs_per_file):

            skip_events = j * args.nEvent
            if skip_events >= events_per_file:
                continue

            script_name = os.path.join(farm_dir, f"run_{project_name}_{job_idx}.sh")
            workspace = f"$TMPDIR/Job_{project_name}_{job_idx}"

            print(f"Creating {script_name}")

            with open(script_name, "w") as f:

                f.write("#!/bin/bash\n")
                f.write("set -e\n\n")

                f.write("export X509_USER_PROXY=$1\n")

                f.write(f"WORKDIR={workspace}\n")
                f.write("mkdir -p $WORKDIR\n")
                f.write("echo 'Using TMPDIR=' $WORKDIR\n\n")

                f.write(f"cd {cmssw_dir}\n")
                f.write("eval `scramv1 runtime -sh`\n\n")

                f.write("cd $WORKDIR\n\n")

                for i, cmd in enumerate(project_cfg['process']):

                    cmd_tmp = cmd.replace("file:", "file:$WORKDIR/")

                    if "TnPTreeProducer" in cmd_tmp:
                        cmd_tmp = cmd_tmp.replace('outputFile=file:', 'outputFile=')

                    if "python3" in cmd_tmp:
                        cmd_tmp = cmd_tmp.replace('output_Phase2_HLT.root', '$WORKDIR/output_Phase2_HLT.root')
                        cmd_tmp = cmd_tmp.replace('tnpNtupler.root', '$WORKDIR/tnpNtupler.root')

                    if i == 0:
                        cmd_tmp += f" --filein {infile} "

                    if 'cmsDriver' in cmd_tmp:
                        if i == 0:
                            # First step → apply skipEvents
                            cmd_tmp += (
                               f" --customise_commands "
                                f"'process.maxEvents.input=cms.untracked.int32({args.nEvent});"
                                f"process.source.skipEvents=cms.untracked.uint32({skip_events})'"
                            )
                        else:
                            # Later steps → NO skipEvents
                            cmd_tmp += (
                                f" --customise_commands "
                                f"'process.maxEvents.input=cms.untracked.int32({args.nEvent})'"
                            )

                    f.write(f"echo 'Running step {i+1}'\n")
                    f.write(f"{cmd_tmp}\n\n")

                for storefile in project_cfg.get('storefile', []):

                    eos_path = os.path.join(
                        project_eos_dir,
                        storefile.replace(".root", f"_{job_idx}.root")
                    )

                    f.write(
                        f"xrdcp $WORKDIR/{storefile} root://eosuser.cern.ch/{eos_path}\n"
                    )

                f.write("rm -f $WORKDIR/*.root\n")

            os.chmod(script_name, 0o755)
            shell_scripts.append(script_name)

            job_idx += 1

# -------------------------------
# CONDOR SUBMIT FILE
# -------------------------------
sub_file = f"{args.farm}/condor_jobs.sub"

condor_str = ""
condor_str += "executable = $(filename)\n"

if args.proxy is not None:
    condor_str += f"Proxy_path = {args.proxy}\n"
    condor_str += "arguments = $(Proxy_path)\n"

condor_str += "output = $Fp(filename)$(filename)_hlt.stdout\n"
condor_str += "error = $Fp(filename)$(filename)_hlt.stderr\n"
condor_str += "log = $Fp(filename)$(filename)_hlt.log\n"

condor_str += f'+JobFlavour = "{args.jobFlavour}"\n'

# Request enough resources
condor_str += "request_disk = 25 GB\n"
condor_str += "request_memory = 8000\n"

condor_str += f"queue filename matching ({args.farm}/*/*.sh)"

with open(sub_file, "w") as condor_file:
    condor_file.write(condor_str)

print("\n✅ Condor submission file created:", sub_file)
print(f"✅ Total jobs created: {len(shell_scripts)}")
