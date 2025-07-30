#!/bin/bash

# Directory containing the files
directory="/afs/cern.ch/work/s/ssaumya/private/Egamma/dz_Checks/Rates/CMSSW_15_0_10/src/SteamRatesEdmWorkflow/Rates/Results/Data/Raw/Global/"
#directory="/afs/cern.ch/work/s/ssaumya/private/Egamma/dz_Checks/Rates/CMSSW_15_0_10/src/SteamRatesEdmWorkflow/Rates/Results/Data/Raw/PathMisc/"
# Expected filename pattern
#prefix="output.path.misc."
prefix="output.global."
suffix=".csv"

# Range of expected numbers
start=0
end=232

# Check for each expected file
for ((i=start; i<=end; i++)); do
    filename="${prefix}${i}${suffix}"
    filepath="${directory}/${filename}"
    
    if [ ! -f "$filepath" ]; then
        echo "Missing: $filename"
    fi
done
