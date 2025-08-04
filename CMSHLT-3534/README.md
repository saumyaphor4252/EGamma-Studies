
## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3534
- Request for validation in: https://its.cern.ch/jira/browse/CMSHLT-3534?focusedId=7049846&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-7049846
- Menu used: 
	- Reference: /dev/CMSSW_15_0_0/GRun/V103
	- Target: /users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3534/Test21/GRun/V3
- Run used : 393276, 393331, 393346
- CMSSW: CMSSW_15_0_10_patch3
- GTs
	- HLT: 150X_dataRun3_HLT_v1
	- Prompt: 150X_dataRun3_Prompt_v1

### Blocks used
```
/EGamma0/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#4c88add9-27f5-4dca-9bd8-8f726f805049
/EGamma1/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#49df50de-dfb4-4f90-be37-c2b3da4a49e6
/EGamma2/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#836b224a-121a-4f28-9619-49f58dbb60c1
/EGamma3/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#73202192-8584-485e-af18-374c030746d4
```

### Rucio rules for dataset not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/EGamma0/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#4c88add9-27f5-4dca-9bd8-8f726f805049  1 T2_CH_CERN  --lifetime 8640    00 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma1/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#49df50de-dfb4-4f90-be37-c2b3da4a49e6  1 T2_CH_CERN  --lifetime 8640    00 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma2/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#836b224a-121a-4f28-9619-49f58dbb60c1  1 T2_CH_CERN  --lifetime 8640    00 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma3/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#73202192-8584-485e-af18-374c030746d4 1 T2_CH_CERN  --lifetime 86400    0 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio rule-info f826cda862964bd2bad0395397f63f78
rucio rule-info 795ab1f2f1f34c4fa14b3f287e06de09
rucio rule-info a9c1fb3ee6ae406b9a8355311f3fed6b
rucio rule-info fa130a6d042e4290890193b715d47640
```

### CMSSW set-up
```
cmsrel CMSSW_15_0_10_patch3; cd CMSSW_15_0_10_patch3/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V103 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v2/000/393/346/00000/ff8a9f22-21e4-47fc-9f45-b350389d8468.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025C_Reference
```

Repeat the same steps for Target menu

```
### hltGetConfiguration
hltGetConfiguration /users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3534/Test21/GRun/V3 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Target_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v2/000/393/346/00000/ff8a9f22-21e4-47fc-9f45-b350389d8468.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2025C_Target
```

### Run the PAT step to create miniAOD (Common for Reference and Target)
```
# Run locally
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2025 --filein file:../HLT_Reference/hltOutput_RECO_Reference.root --fileout file:stepMINI.root --hltProcess MYHLT
```

This step will be same for both Reference and Target.
 
### Condor Submission Tools
```
##### Input setup #####

# Use the dasFileQuery script to control the number of files/events in the dataset you want to run on
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

##### For HLT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration
## L49-L63 for configuration modification of the HLT step, L53-L58 for input source, L73 for events, L76-77 and L125-128 for output file name
# -n 10 --> 10 files per job
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3534/CMSSW_15_0_10_patch3/src/HLT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3534/HLTstep_RECO_RootFiles_Reference/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3534/CMSSW_15_0_10_patch3/src/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3534/PATstep_MINIAOD_RootFiles_Reference -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
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
source /cvmfs/cms.cern.ch/common/crab-setup.sh
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
