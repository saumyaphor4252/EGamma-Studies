import sys
import json
import subprocess
import os
import os.path
import itertools

def get_total_events(file_list):
    """
    Calculate the total number of events in List_cff.py which has the list of root files to be used

    Parameters:
        file_list (list): List of file names (CMS DAS paths).

    Returns:
        int: Total number of events in all files.
    """
    total_events = 0

    for file in file_list:
    #for file in ["/store/data/Run2024I/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/386/553/00000/8d0adf6e-43ef-4995-a57c-3c8cd4197786.root"]:
        try:
            # Use dasgoclient to fetch the number of events

            cmd = f"dasgoclient --query='file={file} | grep file.nevents'"
            result = subprocess.check_output(cmd, shell=True, text=True)
            #print(type(result))

            total_events += int(result)
        except Exception as e:
            print(f"Error processing {file}: {e}")

    return total_events

if __name__ == "__main__":
    from List_cff import inputFiles
    #total_Events = get_total_events(["/store/data/Run2024I/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/386/553/00000/8d0adf6e-43ef-4995-a57c-3c8cd4197786.root"])
    total_Events = get_total_events(inputFiles)
    print(total_Events)
