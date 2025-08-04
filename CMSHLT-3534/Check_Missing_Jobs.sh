# Set the folder path (change if needed)
#FOLDER="./"  # current directory
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/HLTstep_RECO_RootFiles_12_26_Laurent"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/PATstep_MINIAOD_RootFiles_12_26_Laurent/"
FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3534/HLTstep_RECO_RootFiles_Reference/"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/dz_Checks/TnPTuples/2025-07-28/2025/data/CRAB_UserFiles/crab_data_Reduced_Threshold_Target_80/250728_060933/0000/"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/dz_Checks/Reduced_Threshold/HLTstep_RECO_RootFiles_Target_85/"

# Range of expected files
START=0
END=212

# Loop through expected range
for ((i=START; i<=END; i++)); do
#    FILE="$FOLDER/stepPAT_MINIAOD_${i}.root"
    FILE="$FOLDER/stepHLT_RECO_${i}.root"
#    FILE="$FOLDER/TnPTree_data_${i}.root"
    if [ ! -f "$FILE" ]; then
#        echo "Missing: stepPAT_MINIAOD_${i}.root"
        echo "${i} "
    fi
done
