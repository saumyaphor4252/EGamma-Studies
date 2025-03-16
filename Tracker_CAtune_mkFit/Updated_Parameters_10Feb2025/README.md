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

## Target set-up
```
cmsrel CMSSW_15_0_0; cd CMSSW_15_0_0/src; cmsenv
git cms-addpkg HLTrigger/Configuration
git remote add ElusianTempRepo git@github.com:elusian/cmssw.git
git fetch ElusianTempRepo 1500p3_newCAtuning
git cherry-pick d73d7272d66e7c702a615557bc4ced4ba8766019
git cherry-pick 622039de51b5cac83fa72fa901990e1eeeb9b8d0
ls HLTrigger/Configuration/python/
scram b -j 10
```

### Run the HLT step locally
```
# hltGetConfiguration
hltGetConfiguration /dev/CMSSW_14_2_0/GRun/V12 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v11,HLT_Ele32_WPTight_Gsf_v25,HLT_Ele115_CaloIdVT_GsfTrkIdT_v25,HLT_Ele135_CaloIdVT_GsfTrkIdT_v18,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v29,HLT_DoubleEle33_CaloIdL_MW_v28,HLTriggerFinalPath --output minimal --data --process MYHLT --type GRun --globaltag 141X_dataRun3_HLT_v2 --max-events 100 --unprescale --eras Run3 --customise HLTrigger/Configuration/customize_CAPixelOnlyRetune.customize_CAPixelOnlyRetuneSameEff,RecoTracker/MkFit/customizeHLTIter0ToMkFit.customizeHLTIter0ToMkFit --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_cff.py

# Re-run HLT step
cmsDriver.py --conditions 141X_dataRun3_HLT_v2 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2024I

# Now run the configuration file for local testing
cmsRun hlt_ReRun_Config.py
```

### For condor submission
```
# Use the dasFileQuery script to control the dataset or number of files/events you want to run on; Update the dataset you are using in dasFileQuery.oy manually
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.

## Create condor jobs for HLT step : cmsCondor.py ##
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration or GRun menu
## L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CA_Tuning/Updated_Parameters/CMSSW_15_0_0/src/ /eos/cms/store/group/phys_egamma/ssaumya/CATuning_mkFit/Updated_Version/HLTstep_RECO_RootFiles_Target/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u1<9999>
# python3 cmsCondor.py <python_config_to_run> <CMSSW_Area_path> <Output_Files_Area> -n <Number_of_files_per_job> -q <condor_flavor> -p <path_to_proxy>

# Submit jobs
./sub_total.jobb
```
 
## Reference set-up
```
cmsrel CMSSW_15_0_0; cd CMSSW_15_0_0/src; cmsenv
git cms-addpkg HLTrigger/Configuration
scram b -j 10

#### Run the HLT step ####

# hltGetConfiguration
hltGetConfiguration /dev/CMSSW_14_2_0/GRun/V12 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v11,HLT_Ele32_WPTight_Gsf_v25,HLT_Ele115_CaloIdVT_GsfTrkIdT_v25,HLT_Ele135_CaloIdVT_GsfTrkIdT_v18,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v29,HLT_DoubleEle33_CaloIdL_MW_v28,HLTriggerFinalPath --output minimal --data --process MYHLT --type GRun --globaltag 141X_dataRun3_HLT_v2 --max-events 100 --unprescale --eras Run3 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_cff.py

# Re-run HLT step
cmsDriver.py --conditions 141X_dataRun3_HLT_v2 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2024I

# Now run the configuration file for local testing
cmsRun hlt_ReRun_Config.py
```

### For condor submission
```
# Use the dasFileQuery script to control the dataset or number of files/events you want to run on; Update the dataset you are using in dasFileQuery.oy manually
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.

## Create condor jobs for HLT step : cmsCondor.py ##
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration or GRun menu
## L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CA_Tuning/Updated_Parameters/Reference/CMSSW_15_0_0/src/ /eos/cms/store/group/phys_egamma/ssaumya/CATuning_mkFit/Updated_Version/HLTstep_RECO_RootFiles_CorrectReference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<9999>
# python3 cmsCondor.py <python_config_to_run> <CMSSW_Area_path> <Output_Files_Area> -n <Number_of_files_per_job> -q <condor_flavor> -p <path_to_proxy>

# Submit jobs
./sub_total.jobb
```
 
## Run the PAT step to create miniAODs (Common for Target and Reference)
### Test locally
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

### Condor Submission
```
## Create condor jobs for PAT step : cmsCondor.py ##

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration or GRun menu
# L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CA_Tuning/Updated_Parameters/CMSSW_15_0_0/src/ /eos/cms/store/group/phys_egamma/ssaumya/PATstep_MINIAOD_RootFiles_Target/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

## Sumit jobs ##
./sub_total.jobb
```

### Make the ntuples
Set up inside `CMSSW_15_0_0/src`
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
# Notebook Templates: Winter24Checks.ipynb, Wniter24_DataMC_Checks.ipynb
```
