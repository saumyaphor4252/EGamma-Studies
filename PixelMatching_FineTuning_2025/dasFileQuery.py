import sys
import json
import subprocess
import os
import os.path
import itertools

def dasFileQuery(dataset):
    """Return files for given DAS query via dasgoclient"""

    def run_dasgoclient(query):
        result = subprocess.run(
             ['dasgoclient', '--query', query, '--format', 'json'],# , '--limit', '400'],
             stdout=subprocess.PIPE, 
             stderr=subprocess.PIPE,
             text=True
             )
#        print("Return code:", result.returncode)
#        print("Output:", result.stdout)
#        print("Error:", result.stderr)

        if result.returncode != 0:
            sys.stderr.write(f"Error executing dasgoclient: {result.stderr}\n")
            sys.exit(1)
        return json.loads(result.stdout)

    files = []
    query_file = f'file dataset={dataset}'
    print("Print f query...")
    jsondict = run_dasgoclient(query_file)

    for data in jsondict['data']:
        for file in data['file']:
            files.append(file['name'])

    dir = "/eos/cms/store/data/Run2025G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/"

    li2 = []
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dir)):
        for x in filenames:
            dirpath = dirpath.replace("/eos/cms","")
            li2.append(os.path.join(dirpath,x))

    #Unaccessible = set(files)-set(li2)
    accessible = list(set(files).intersection(set(li2)))
    print(len(accessible))
    #return accessible

    # Convert the output to a list
    cff_content = "inputFiles = ["

    #limited = accessible[0:1450]
    for file in accessible:
        cff_content += f"'{file}',\n"

    # Close the list and the script
    cff_content += "]\n"

    with open('List_cff.py', 'w') as file:
        file.write(cff_content)

dasFileQuery("/EGamma0/Run2025G-ZElectron-PromptReco-v1/RAW-RECO")
# dasgoclient --query "file dataset=/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO | grep file.name,file.nevents" --limit 1425 | awk '{sum += $2} END {print sum}'
