## Relevant Links and information
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3719
- CMSSW: `CMSSW_16_0_2_patch1`
- Menu used: `/dev/CMSSW_16_0_0/GRun/V30`
- Dataset used: `/EGamma1/Run2025G-ZElectron-PromptReco-v1/RAW-RECO`
- Difference between target and reference: Customization for `hltGetConfiguration` (See below)
```
--customise HLTrigger/Configuration/customizeHLTfor49800.customise_case1
```

- GTs
	- HLT: `160X_dataRun3_HLT_v1`
	- Prompt: `160X_dataRun3_Prompt_v1`

### Rucio rules for dataset if not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/EGamma1/Run2025G-ZElectron-PromptReco-v1/RAW-RECO#2fa1e982-079d-4e7c-936a-0d6eca9f1127 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2025G EGM-HLT studies"
rucio rule-info be54b28bccde4c17923afeefb7403642 
```

### CMSSW set-up
```
cmsrel CMSSW_16_0_2_patch1; cd CMSSW_16_0_2_patch1/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
- Reference
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_16_0_0/GRun/V30 --output minimal --data --process MYHLT --type GRun --globaltag 160X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2026 --l1-emulator uGT --l1 L1Menu_Collisions2026_v1_0_0_xml --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v*,HLT_Ele32_WPTight_Gsf_v*,HLT_Ele115_CaloIdVT_GsfTrkIdT_v*,HLT_Ele135_CaloIdVT_GsfTrkIdT_v*,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*,HLT_DoubleEle33_CaloIdL_MW_v*,HLTriggerFinalPath --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025G_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 160X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2026 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/398/859/00000/e37530b2-90d8-434c-9eeb-9267f66d5d2b.root --fileout file:hltOutput_RECO_Reference.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025G_Reference

cmsRun hlt_ReRun_Config_Reference.py
```
- Target
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_16_0_0/GRun/V30 --output minimal --data --process MYHLT --type GRun --globaltag 160X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2026 --l1-emulator uGT --l1 L1Menu_Collisions2026_v1_0_0_xml --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v*,HLT_Ele32_WPTight_Gsf_v*,HLT_Ele115_CaloIdVT_GsfTrkIdT_v*,HLT_Ele135_CaloIdVT_GsfTrkIdT_v*,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*,HLT_DoubleEle33_CaloIdL_MW_v*,HLTriggerFinalPath --customise HLTrigger/Configuration/customizeHLTfor49800.customise_case1 --cff "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025G_Target_cff.py

### Re-run HLT step
cmsDriver.py --conditions 160X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2026 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/398/859/00000/e37530b2-90d8-434c-9eeb-9267f66d5d2b.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2025G_Target

cmsRun hlt_ReRun_Config_Target.py
```

### Run the PAT step to create miniAOD (Common for Reference and Target)
```
# Run locally
cmsDriver.py stepMINI -s PAT --conditions 160X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2026 --filein file:../HLT_Reference/hltOutput_RECO_Reference.root --fileout file:stepMINI.root --hltProcess MYHLT
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
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3719/CMSSW_16_0_2_patch1/src/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3719/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3719/CMSSW_16_0_2_patch1/src/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3719/PATstep_MINIAOD_RootFiles_Reference -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
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
