
# Set the folder path (change if needed)
#FOLDER="./"  # current directory
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/HLTstep_RECO_RootFiles_12_26_Laurent"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/PATstep_MINIAOD_RootFiles_12_26_Laurent/"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/HLTstep_RECO_RootFiles_16_22/"
#FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/TnPTuples/2025-05-11/2024/data/CRAB_UserFiles/crab_data_Reference/250518_182358/0000/"
FOLDER="/eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/TnPTuples/2025-05-11/2024/data/CRAB_UserFiles/crab_data_12_26_Laurent/250521_101235/0000/"

# Range of expected files
START=0
END=148

# Loop through expected range
for ((i=START; i<=END; i++)); do
#    FILE="$FOLDER/stepPAT_MINIAOD_${i}.root"
#    FILE="$FOLDER/stepHLT_RECO_${i}.root"
    FILE="$FOLDER/TnPTree_data_${i}.root"
    if [ ! -f "$FILE" ]; then
#        echo "Missing: stepPAT_MINIAOD_${i}.root"
        echo "${i} "
    fi
done
