## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3565
- Reference menu : /cdaq/physics/Run2025/2e34/v1.1.2/HLT/V6
- Target menu: /cdaq/physics/Run2025/2e34/v1.1.3/HLT/V1 
- Run used : Run392925 from 2025C

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
git cms-init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
##### Target
```
### hltGetConfiguration
hltGetConfiguration adg:/cdaq/physics/Run2025/2e34/v1.1.3/HLT/V1 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Target_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/392/925/00000/f58a4205-664d-4edb-972d-e1bfc3d95300.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2025C_Run392925_Reference

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Target.py

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Target.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3565/CMSSW_15_0_7/src/HLT_Target /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3565/HLTstep_RECO_RootFiles_Target/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb
```

##### Reference

```
### hltGetConfiguration
hltGetConfiguration adg:/cdaq/physics/Run2025/2e34/v1.1.2/HLT/V6 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Run392925_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/392/925/00000/f58a4205-664d-4edb-972d-e1bfc3d95300.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025C_Run392925_Reference

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Reference.py

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3565/CMSSW_15_0_7/src/HLT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3565/HLTstep_RECO_RootFiles_Reference/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb
```
 
### Run the PAT step to create miniAOD (Common for target and Reference)
```
# Local
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2025 --filein file:../HLT_Reference/hltOutput_RECO_Reference.root --fileout file:stepMINI.root --hltProcess MYHLT

# Submit on condor
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3565/CMSSW_15_0_7/src/PAT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3565/PATstep_MINIAOD_RootFiles_Reference/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb
```
 
### Make the ntuples
Set up inside `CMSSW_X_Y_Z/src`
```
git clone -b 150X_2025_Studies git@github.com:saumyaphor4252/EgammaAnalysis-TnPTreeProducer.git EgammaAnalysis/TnPTreeProducer
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
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/IasonTool/egamma-tnp/
source egmtnpenv/bin/activate
jupyter lab --no-browser --port 8777

# Code template: https://github.com/saumyaphor4252/egamma-tnp/tree/2025_Studies
# Notebook template: STEAM_23ndMay2025.ipynb
```
