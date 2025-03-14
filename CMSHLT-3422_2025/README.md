### Set up the rucio rules for the files/blocks as per required minimally for the testing
```
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#4a2f0c6d-e420-4818-9bef-7d6d05b5fe1a 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
e2bb2474f15c4c789fca9b5d76f104bb
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#a49af9ca-d948-46ba-b2e6-f772da0a83fe 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
28a376b1e3f245de83dbf4f242a32741
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#35ff20a6-563a-4de9-a62a-5ae603bc9098 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
aeaaf79f76b14335a47f82693205ecf0
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#dce53cd5-669d-4c00-afa5-2625c1470d99 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
356645b6456647f6b8412a96f6ac4b8f
```

## CMSSW set-up
```
mkdir L1_min_Cluster_Charge
cd L1_min_Cluster_Charge/
cmsrel CMSSW_14_2_2
cd CMSSW_14_2_2/src
cmsenv
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```
### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_14_2_0/GRun/V12 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v11,HLT_Ele32_WPTight_Gsf_v25,HLT_Ele115_CaloIdVT_GsfTrkIdT_v25,HLT_Ele135_CaloIdVT_GsfTrkIdT_v18,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v29,HLT_DoubleEle33_CaloIdL_MW_v28,HLTriggerFinalPath --output minimal --data --process MYHLT --type GRun --globaltag 141X_dataRun3_HLT_v2 --max-events 100 --unprescale --eras Run3 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_cff.py

### Re-run HLT step
cmsDriver.py --conditions 141X_dataRun3_HLT_v2 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2024I

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config.py

### Create list of Files to be used for running the jobs using DAS query file
python3 dasFileQuery.py # Update the dataset manually used here if not already; /EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO in this case
# This will generate List_cff.py with files list

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/L1_min_Cluster_Charge/CMSSW_14_2_2/src /eos/cms/store/group/phys_egamma/ssaumya/L1_min_Cluster_Charge/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
# Format for above command: python3 cmsCondor.py <config_file> <CMSSW_Area> <Output_Files_Area> -n <number_of_files_per_job> -q <flavour> -p <voms_proxy_area>
```
 
### Run the PAT step to create miniAOD
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

### Make the ntuples
Set up inside `CMSSW_14_0_15/src`
```
git clone -b Private_MINIAOD_2024_Data git@github.com:saumyaphor4252/EgammaAnalysis-TnPTreeProducer.git EgammaAnalysis/TnPTreeProducer
scram b -j8
cd EgammaAnalysis/TnPTreeProducer/crab/

vi tnpCrabSubmit_PrivateMINIAOD.py
# Update the file tnpCrabSubmit_PrivateMINIAOD.py as per needs for input, output files and storage folder
python3 tnpCrabSubmit_PrivateMINIAOD.py # This will create a file crab_submit_Private_MINIAOD.py
crab submit crab_submit_Private_MINIAOD.py # This will submit the jobs
```

### Run Iason's tool for plotting
```
ssh -o ServerAliveInterval=10 ssaumya@lxplus9.cern.ch -L8777:localhost:8777
cd /afs/cern.ch/user/s/ssaumya/Egamma/egamma-tnp/
source egmtnpenv/bin/activate
jupyter lab --no-browser --port 8777

# Code used: https://github.com/saumyaphor4252/egamma-tnp/tree/2024_Studies
# Notebook used: Winter24Checks.ipynb, Wniter24_DataMC_Checks.ipynb
```
