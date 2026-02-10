#!/usr/bin/env python3

"""
HTCondor submission script for distributed processing of E/gamma efficiency analysis
This script splits your 200 files across multiple condor jobs to avoid memory issues
"""

import os
import glob
import argparse
import subprocess
import math
from pathlib import Path

def create_condor_executable():
    """Create the condor executable script."""
    
    executable_content = '''#!/bin/bash

# Condor job executable for E/gamma efficiency analysis  
# Arguments: $1 = input_file, $2 = output_filename, $3 = max_events

echo "🚀 Starting Condor job on $(hostname)"
echo "📁 Working directory: $(pwd)"
echo "📊 Input file: $1"
echo "📤 Output filename: $2"
echo "⚡ Max events: $3"

# Setup CMSSW Base (following working example)
export SCRAM_ARCH=el9_amd64_gcc12
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/Efficiencies/CMSSW_16_0_0_pre4/src/
eval `scramv1 runtime -sh`

cmsenv

# Copy the python script to local directory
#cp /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/Distributions/UpgradeRoundTable_Sept2025/CMSSW_15_1_0_pre4/src/Efficiencies/lastFilterEfficiency_Upgrade.py .

# Run the analysis directly (create local file)
echo "🔄 Running analysis..."
echo "📋 Command: python3 lastFilterEfficiency_Upgrade.py --input-file \"$1\" -o \"$2\" -n \"$3\""
echo "📁 Current directory: $(pwd)"
echo "📂 Directory contents before analysis: $(ls -la)"

python3 lastFilterEfficiency_Upgrade.py --input-file "$1" -o "$2" -n "$3"
PYTHON_EXIT_CODE=$?

echo "🔍 Python exit code: $PYTHON_EXIT_CODE"
echo "📂 Directory contents after analysis: $(ls -la *.root 2>/dev/null || echo 'No .root files found')"
echo "🎯 Looking for specific file: $2"

cp *.root /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/Efficiencies/CMSSW_16_0_0_pre4/src/OutputNtuples_Reference/
rm -rf *.root

echo "🎉 Job completed successfully!"
'''
    
    # Get current paths
    cmssw_path = os.environ.get('CMSSW_BASE', '/afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/Efficiencies/CMSSW_16_0_0_pre4/')
    script_path = os.path.abspath('lastFilterEfficiency_Upgrade.py')
    
    executable_content = executable_content.format(
        CMSSW_PATH=cmssw_path,
        SCRIPT_PATH=script_path
    )
    
    with open('condor_job.sh', 'w') as f:
        f.write(executable_content)
    
    os.chmod('condor_job.sh', 0o755)
    print("📝 Created condor_job.sh")

def create_condor_submit_file(input_files, files_per_job=5, max_events=-1, output_dir="OutputNtuples_Reference", job_flavor="workday"):
    """Create the condor submit file."""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 Output directory ready: {output_dir}")
    
    submit_content = f'''Universe   = vanilla

Executable = condor_job.sh

Log        = condor_logs/job_$(Cluster)_$(Process).log
Output     = condor_logs/job_$(Cluster)_$(Process).out
Error      = condor_logs/job_$(Cluster)_$(Process).err

should_transfer_files = YES
when_to_transfer_output = ON_EXIT

+JobFlavour = "{job_flavor}"

'''

    # Create logs directory
    os.makedirs('condor_logs', exist_ok=True)
    
    # Group files into batches
    num_jobs = math.ceil(len(input_files) / files_per_job)
    
    print(f"📊 Creating {num_jobs} jobs for {len(input_files)} files ({files_per_job} files per job)")
    
    # Create a single queue command for all files (like your working example)
    with open('input_files.txt', 'w') as f:
        for i, input_file in enumerate(input_files):
            input_basename = os.path.splitext(os.path.basename(input_file))[0]
            output_filename = f"job{i:03d}_{input_basename}.root"
            f.write(f"{input_file} {output_filename} {max_events}\n")
    
    submit_content += f'''
Arguments = $(input_file) $(output_file) $(max_events)

Queue input_file,output_file,max_events from input_files.txt
'''
    
    with open('condor_submit.sub', 'w') as f:
        f.write(submit_content)
    
    print("📝 Created condor_submit.sub")
    return num_jobs

def create_merge_script(output_dir, final_output):
    """Create script to merge all condor outputs."""
    
    merge_content = f'''#!/bin/bash

# Auto-generated merge script for condor outputs

echo "🔗 Merging condor job outputs..."
echo "📁 Looking for files in: {output_dir}/"

# Count output files
NUM_FILES=$(ls {output_dir}/*.root 2>/dev/null | wc -l)

if [ $NUM_FILES -eq 0 ]; then
    echo "❌ No output files found in {output_dir}/"
    exit 1
fi

echo "📊 Found $NUM_FILES output files to merge"

# Merge all files
echo "🚀 Running hadd..."
hadd -f {final_output} {output_dir}/*.root

if [ $? -eq 0 ]; then
    echo "✅ Successfully merged $NUM_FILES files into {final_output}"
    echo "📦 Final output size: $(ls -lh {final_output} | awk '{{print $5}}')"
else
    echo "❌ Error during merging"
    exit 1
fi

echo "🎉 Merge completed successfully!"
'''
    
    with open('merge_condor_outputs.sh', 'w') as f:
        f.write(merge_content)
    
    os.chmod('merge_condor_outputs.sh', 0o755)
    print("📝 Created merge_condor_outputs.sh")

def main():
    parser = argparse.ArgumentParser(description='Submit E/gamma efficiency analysis to HTCondor 🚀')
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--input-dir', help='Directory containing ROOT files')
    input_group.add_argument('--input-pattern', help='File pattern (e.g., /eos/cms/store/user/*/*.root)')
    input_group.add_argument('--input-list', help='Text file with list of input files (one per line)')
    
    parser.add_argument('-o', '--output', required=True, help='Final merged output file name')
    parser.add_argument('--output-dir', default='OutputNtuples_Reference', help='Directory for individual job outputs')
    parser.add_argument('--files-per-job', type=int, default=1, help='Number of files to process per condor job (default: 1)')
    parser.add_argument('-n', '--max-events', type=int, default=-1, help='Maximum events per file (-1 for all)')
    parser.add_argument('--job-flavor', default='longlunch', 
                       choices=['espresso', 'microcentury', 'longlunch', 'workday', 'tomorrow', 'testmatch', 'nextweek'],
                       help='HTCondor job flavor (default: longlunch=2h)')
    parser.add_argument('--submit', action='store_true', help='Automatically submit jobs after creating scripts')
    parser.add_argument('--dry-run', action='store_true', help='Create scripts but don\'t submit')
    
    args = parser.parse_args()
    
    # Get input files
    input_files = []
    if args.input_dir:
        if "eos" in args.input_dir:
            # For EOS paths, use ls command and handle potential issues
            try:
                # Make sure path ends with /
                eos_dir = args.input_dir.rstrip('/') + '/'
                result = subprocess.run(f"ls {eos_dir}*.root", capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    input_files = [f for f in result.stdout.strip().split('\n') if f.strip() and f.endswith('.root')]
                    print(f"🔍 EOS ls found {len(input_files)} files")
                else:
                    print(f"❌ Error listing EOS directory: {result.stderr}")
                    # Fallback to glob
                    input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
            except Exception as e:
                print(f"❌ Exception with EOS listing: {e}")
                input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
        else:
            input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
    elif args.input_pattern:
        if "eos" in args.input_pattern:
            try:
                result = subprocess.run(f"ls {args.input_pattern}", capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    input_files = [f for f in result.stdout.strip().split('\n') if f.strip() and f.endswith('.root')]
                else:
                    print(f"❌ Error with pattern: {result.stderr}")
                    input_files = glob.glob(args.input_pattern)
            except Exception as e:
                print(f"❌ Exception with pattern: {e}")
                input_files = glob.glob(args.input_pattern)
        else:
            input_files = glob.glob(args.input_pattern)
    elif args.input_list:
        with open(args.input_list, 'r') as f:
            input_files = [line.strip() for line in f if line.strip()]
    
    if not input_files:
        print("❌ No input files found!")
        return
    
    print(f"🎯 Found {len(input_files)} input files")
    print(f"⚙️  Configuration:")
    print(f"   📁 Files per job: {args.files_per_job}")
    print(f"   📊 Max events per file: {args.max_events}")
    print(f"   ⏰ Job flavor: {args.job_flavor}")
    print(f"   📤 Output directory: {args.output_dir}")
    print(f"   🎯 Final output: {args.output}")
    
    if args.dry_run:
        print("🔍 DRY RUN - scripts will be created but not submitted")
    
    # Create condor scripts
    create_condor_executable()
    num_jobs = create_condor_submit_file(input_files, args.files_per_job, args.max_events, args.output_dir, args.job_flavor)
    create_merge_script(args.output_dir, args.output)
    
    print(f"\\n📋 Summary:")
    print(f"   🎯 Total jobs: {num_jobs}")
    print(f"   📊 Total files: {len(input_files)}")
    print(f"   ⚡ Files per job: {args.files_per_job}")
    
    if args.submit and not args.dry_run:
        print("\\n🚀 Submitting jobs to condor...")
        result = subprocess.run(['condor_submit', 'condor_submit.sub'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Jobs submitted successfully!")
            print(result.stdout)
            print("\\n📊 Monitor with: condor_q")
            print("🔗 Merge outputs when done: ./merge_condor_outputs.sh")
        else:
            print("❌ Error submitting jobs:")
            print(result.stderr)
    else:
        print("\\n📝 Scripts created! To submit:")
        print("   condor_submit condor_submit.sub")
        print("\\n📊 Monitor with:")
        print("   condor_q")
        print("\\n🔗 Merge when done:")
        print("   ./merge_condor_outputs.sh")

if __name__ == "__main__":
    main()
