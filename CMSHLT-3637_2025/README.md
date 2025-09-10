
## Relevant Links and information
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3637
- CMSSW: CMSSW_15_0_13
- Menu used: /dev/CMSSW_15_0_0/GRun/V112
- Dataset used: /EGamma0/Run2025E-ZElectron-PromptReco-v1/RAW-RECO
- Run used:
- Difference between target and reference: Customization for `hltGetConfiguration` and GlobalTags (See below)
- GTs
	- HLT: 
		- Reference (no DIGI morphing) : `150X_dataRun3_HLT_Pixel_TkAl_noDigiMorphing_BSfromGT_v2` [CondDB Link](https://cms-conddb.cern.ch/cmsDbBrowser/diff/Prod/gts/150X_dataRun3_HLT_v1/150X_dataRun3_HLT_Pixel_TkAl_noDigiMorphing_BSfromGT_v2)
		- Target (with DIGI morphing) : `150X_dataRun3_HLT_Pixel_TkAl_DigiMorphing_BSfromGT_v2` [CondDB Link](https://cms-conddb.cern.ch/cmsDbBrowser/diff/Prod/gts/150X_dataRun3_HLT_v1/150X_dataRun3_HLT_Pixel_TkAl_DigiMorphing_BSfromGT_v2)
	- Prompt: 150X_dataRun3_Prompt_v1

### Blocks used
```
/EGamma0/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#cdbe05b2-86e5-4008-986c-4350193e3391
/EGamma1/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#2fa1e982-079d-4e7c-936a-0d6eca9f1127
/EGamma2/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#072aab27-998e-417f-9ff6-28e72ccc32b7
/EGamma3/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#1eb3170c-dcd5-45ab-af35-c2b36af16256
```

### Rucio rules for dataset not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/EGamma0/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#cdbe05b2-86e5-4008-986c-4350193e3391 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma1/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#2fa1e982-079d-4e7c-936a-0d6eca9f1127 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma2/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#072aab27-998e-417f-9ff6-28e72ccc32b7 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio add-rule cms:/EGamma3/Run2025E-ZElectron-PromptReco-v1/RAW-RECO#1eb3170c-dcd5-45ab-af35-c2b36af16256 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2025C EGM-HLT studies"
rucio rule-info be54b28bccde4c17923afeefb7403642 
rucio rule-info 6c9a63065d174bc2be1c3a95dee9b973
rucio rule-info 4d26f61d057943d58d0e2d953c29c790
rucio rule-info 3dfde7a4354d4f9cbabe85b3494f5f8d
```

### CMSSW set-up
```
cmsrel CMSSW_15_0_13; cd CMSSW_15_0_13/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
git cms-addpkg RecoLocalTracker/SiPixelClusterizer
git cms-merge-topic CMSTrackerDPG:digimorphing_backport_v2
scram b -j 10
```

### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V112 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025E_cff.py

### Re-run HLT step
##### Reference
cmsDriver.py --conditions 150X_dataRun3_HLT_Pixel_TkAl_noDigiMorphing_BSfromGT_v2 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025E/EGamma2/RAW-RECO/ZElectron-PromptReco-v1/000/396/283/00000/01b18cc0-0fbd-4a24-8d4f-52dd7c13cb95.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025E --customise_commands="process.hltSiPixelClustersSoA.DoDigiMorphing = cms.bool(False); process.hltSiPixelClustersSoASerialSync.DoDigiMorphing = cms.bool(False)"

##### Target
cmsDriver.py --conditions 150X_dataRun3_HLT_Pixel_TkAl_DigiMorphing_BSfromGT_v2 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025E/EGamma2/RAW-RECO/ZElectron-PromptReco-v1/000/396/283/00000/01b18cc0-0fbd-4a24-8d4f-52dd7c13cb95.root --fileout file:hltOutput_RECO_Target.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2025E_Reference --customise_commands="process.hltSiPixelClustersSoA.DoDigiMorphing = cms.bool(True); process.hltSiPixelClustersSoASerialSync.DoDigiMorphing = cms.bool(True)"
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
python3 cmsCondor.py hlt_ReRun_Config_Reference_configDump.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3637/CMSSW_15_0_13/src/ /    eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3637/HLTstep_RECO_RootFiles_Reference/ -n 5 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
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
