## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3512
- From Tracking: the latest recipe for `15_0_X` cycle
	- https://docs.google.com/document/d/1bX-ckRcYcMqfykcWAbIPfkCCwkpheywtNW981OP-r80/edit?tab=t.0#heading=h.j303vu7f1fcc
	- Under the paragraph "CA pixel-only (patatrack) re-tuning starting from a 2025 menu"

### Set up the rucio rules for the files/blocks as per required minimally for the testing
```
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#4a2f0c6d-e420-4818-9bef-7d6d05b5fe1a 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
e3ec0c1514264f7a9c35945f6b5c1199
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#a49af9ca-d948-46ba-b2e6-f772da0a83fe 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
4b8a36fe43dd4f48945ca99ef01e9d52
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#35ff20a6-563a-4de9-a62a-5ae603bc9098 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
c677f2289d2b4b84b5bcb13ed44189a6
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#dce53cd5-669d-4c00-afa5-2625c1470d99 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
dce6129136304cc19b0b975be42ddc35
```

### CMSSW set-up
```
cmsrel CMSSW_15_0_5; cd CMSSW_15_0_5/src; cmsenv
git cms-merge-topic cms-tsg-storm:devel_customizeHLTfor2025Studies_from_CMSSW_15_0_3
git cms-merge-topic elusian:1501_newCAtuning
scram b -j 10
```

### Run the HLT step
##### Reference
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V60 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2024  --customise HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu,HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2024I_Reference

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Reference.py

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CA_Tuning/28thApril/CMSSW_15_0_5/src/HLT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/CATuning_mkFit/OnlyCA_6thMay2025/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u999999
```

##### Target

```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V60 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2024  --customise HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu,HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu,RecoTracker/MkFit/customizeHLTIter0ToMkFit.customizeHLTforTrackingIter0CKF --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_Target_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2024I_Target

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Target.py

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Target.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CA_Tuning/28thApril/CMSSW_15_0_5/src/HLT_Target/ /eos/cms/store/group/phys_egamma/ssaumya/CATuning_mkFit/OnlyCA_6thMay2025/HLTstep_RECO_RootFiles_Target/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u999999
```
 
### Run the PAT step to create miniAOD
```
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```
 
### Make the ntuples
Set up inside `CMSSW_X_Y_Z/src`
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
# Notebook Template: Winter24Checks.ipynb, Wniter24_DataMC_Checks.ipynb
```

