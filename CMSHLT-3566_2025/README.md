## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3566
- Recipe : https://its.cern.ch/jira/browse/CMSHLT-3566?focusedId=6815019&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-6815019

### Set up the rucio rules for the files/blocks as per required minimally for the testing
```
[ssaumya@lxplus946 src]$ rucio add-rule cms:/EGamma0/Run2025C-ZElectron-PromptReco-v1/RAW-RECO#d6ce82b9-c7eb-4794-8563-60ff6ca57f92 1 T2_CH_CERN  --lifetime 604800 --comment "EGM TSG 2025 validations"
3a874155c31246588e3047e5c0d1268c
[ssaumya@lxplus946 src]$ rucio add-rule cms:/EGamma1/Run2025C-ZElectron-PromptReco-v1/RAW-RECO#1c85d086-819c-42c2-a147-4263c3af6250 1 T2_CH_CERN  --lifetime 604800 --comment "EGM TSG 2025 validations"
8e18b6a8f26a4d7d82e6d672957e34bd
[ssaumya@lxplus946 src]$ rucio add-rule cms:/EGamma2/Run2025C-ZElectron-PromptReco-v1/RAW-RECO#04fce9ff-28a3-48d7-bf68-896f2c381fe9 1 T2_CH_CERN  --lifetime 604800 --comment "EGM TSG 2025 validations"
17b16467804b49a8973566ea3423b648
[ssaumya@lxplus946 src]$ rucio add-rule cms:/EGamma3/Run2025C-ZElectron-PromptReco-v1/RAW-RECO#c06305bb-a1a6-46ee-b2ed-511460a39a1b 1 T2_CH_CERN  --lifetime 604800 --comment "EGM TSG 2025 validations"
7fb33a5e149441379b40b43d99c916a1
```

### CMSSW set-up
```
cmsrel CMSSW_15_0_7; cd CMSSW_15_0_7/src; cmsenv
git cms-addpkg  RecoTracker/MkFit
git remote add mmasciov git@github.com:mmasciov/cmssw.git
git fetch mmasciov
git cherry-pick 6576f0697571c8affa4aa2b57b14cda089ab2af4
scram b -j 10
```

### Run the HLT step
##### Target
```
### hltGetConfiguration
hltGetConfiguration /cdaq/physics/Run2025/2e34/v1.1.2/HLT/V6 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025  --customise RecoTracker.MkFit.customizeHLTALLMkFit.customizeHLTDoubletRecoveryToMkFit --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Run392925_Target_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/392/925/00000/f58a4205-664d-4edb-972d-e1bfc3d95300.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2025C_Run392925_Target

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Target.py

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Target.py /afs/cern.ch/work/s/ssaumya/private/Egamma/2025_CMSHLT-3566/CMSSW_15_0_7/src/HLT_Target/ /eos/cms/store/group/phys_egamma/ssaumya/2025_CMSHLT-3566/HLTstep_RECO_RootFiles_Target/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
```

##### Reference

```
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
