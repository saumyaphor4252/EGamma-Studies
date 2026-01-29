## Relevant Links
- JIRA : To be opened
- Presentations: [TSG General Meeting, 28th Jan 2025](https://indico.cern.ch/event/1636490/#35-optimizing-pixel-matching-s)

### Set up the rucio rules for the files/blocks as per required minimally for the testing

Datasets
- Data: /EGamma0/Run2025G-ZElectron-PromptReco-v1/RAW-RECO
- QCD: 
	- /QCD_Bin-PT-20to30_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW
	- /QCD_Bin-PT-30to50_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW
	- /QCD_Bin-PT-50to80_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW
- TTto2L2nu: /TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW
- DY: /DYto2L-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW

```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/EGamma0/Run2025G-ZElectron-PromptReco-v1/RAW-RECO 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info a725447bc7cd4b4fa8d35d43bd35a278
rucio add-rule cms:/EGamma1/Run2025G-ZElectron-PromptReco-v1/RAW-RECO 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info 2416ef3a12524824981d2eed109e8ed7
rucio add-rule cms:/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW#0297562b-4bfb-401f-a17f-9eec9ac025f7 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-infoe3a829e88f6c4bbb81a4888f4461c5e4
rucio add-rule cms:/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW#03e1f25d-fecc-46f6-b9a3-e13875d45d44 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info3c718b36892c48aca7430fbc07623524
rucio add-rule cms:/QCD_Bin-PT-20to30_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info 9f2cab708e664bea8bf77eeca7a362e8
rucio add-rule cms:/QCD_Bin-PT-30to50_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info 265ea0a0643845fcb94e3845155a4890
rucio add-rule cms:/QCD_Bin-PT-50to80_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info f3d6d16e547644e19ca9950750b01d88
rucio add-rule cms:/DYto2L-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW#00029bbf-dd36-41df-a9ec-a620b4492bbf 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info d7cb359a19f4419e873a79403ea5c241
rucio add-rule cms:/DYto2L-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW#0276a3f3-539a-4e22-aef8-3bcc65c49d40 1 T2_CH_CERN --lifetime 604800 --comment "For urgent TSG EGM studies"
rucio rule-info 27878e9e53d44af18d4d9bf08b6c0a07
```

Local files for testing
```
/eos/cms/store/data/Run2025G/EGamma0/RAW/v1/000/398/859/00000/1fc4f40f-35f0-44af-8fa2-168133f5e0d0.root
/eos/cms/store/mc/Run3Winter25Digi/DYto2L-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7-v2/2810006/61f5c550-8216-4f35-9ada-d07538e22d29.root
/eos/cms/store/mc/Run3Winter25Digi/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7-v2/2540001/0041d7ec-4b44-431e-91a5-227891f6534a.root
```

### CMSSW set-up
```
cmsrel CMSSW_16_0_0_pre3
cd CMSSW_16_0_0_pre3/src/
cmsenv
git cms-addpkg HLTrigger/Configuration
git cms-addpkg RecoEgamma/EgammaHLTProducers
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
scram b -j 10
```

For ease, make separate directories to run on different samples: EGamma, QCD_20To30, DY, TTto2L2nu

### Run the HLT step and get hlt.root output files 
- EGamma Data
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_16_0_0/GRun/V5 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v*,HLT_Ele32_WPTight_Gsf_v*,HLT_Ele115_CaloIdVT_GsfTrkIdT_v*,HLT_Ele135_CaloIdVT_GsfTrkIdT_v*,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*,HLT_DoubleEle33_CaloIdL_MW_v*,HLTriggerFinalPath --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 10 --unprescale --eras Run3_2025 --input file:/eos/cms/store/data/Run2025G/EGamma0/RAW/v1/000/398/859/00000/1fc4f40f-35f0-44af-8fa2-168133f5e0d0.root --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py

### Modification to store the relevant Pixel Matching variables
Update the `productsToWrite` parameter in 
1. `hltEgammaPixelMatchVarsUnseeded` 
2. `hltEgammaPixelMatchVars` 
EDProducer modules from 0 to 2 as below

`productsToWrite = cms.int32( 0 )` to `productsToWrite = cms.int32( 2 )`

### Sometimes running the hlt.py directly crashes with cmsRun, edmConfigDump avoids that
edmConfigDump hlt.py > hlt_configDump.py

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Reference.py

### Submit on condor
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
python3 cmsCondor.py hlt_configDump.py /afs/cern.ch/work/s/ssaumya/private/Egamma/PMS2_FineTuning/CMSSW_16_0_0_pre3/src/EGamma/ /eos/cms/store/group/phys_egamma/ssaumya/PixelMatching_Reoptimization/28thJan/HLT_Files/EGamma -n 5 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
```

- DY
When running on MC, just change the GT and input file in `hltGetConfiguration`
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_16_0_0/GRun/V5 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v*,HLT_Ele32_WPTight_Gsf_v*,HLT_Ele115_CaloIdVT_GsfTrkIdT_v*,HLT_Ele135_CaloIdVT_GsfTrkIdT_v*,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*,HLT_DoubleEle33_CaloIdL_MW_v*,HLTriggerFinalPath --output minimal --mc --process MYHLT --type GRun --globaltag 142X_mcRun3_2025_realistic_v7 --max-events 5 --unprescale --eras Run3_2025 --input file:/eos/cms/store/mc/Run3Winter25Digi/DYto2L-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7-v2/2810006/61f5c550-8216-4f35-9ada-d07538e22d29.root --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaInputContent > hlt.py
```

### Get ntuples from hlt.root files

```
python3 makeNTuples_Run3_Backup.py /eos/cms/store/group/phys_egamma/ssaumya/PixelMatching_Reoptimization/28thJan/HLT_Files/EGamma/hlt_0.root -o Ntuple_EGamma.root
```


### Plot the distributions from ntuples

```
python3 plot_ntuple_variables.py Ntuple_EGamma.root -o plots
```
