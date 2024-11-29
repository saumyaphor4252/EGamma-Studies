### Set up the rucio rules for the files/blocks as per required minimally for the testing
```
rucio add-rule cms:/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO#0c946de0-a120-4210-89a0-65fea93afc08 1 T2_CH_CERN --lifetime 259200 --comment "For urgent EGM Deep Dive studies"
33aaefdb3e764fcd8faeed0b9f8d4a6e
rucio add-rule cms:/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO#19000750-6ead-4130-b07c-9627f4a68171 1 T2_CH_CERN --lifetime 259200 --comment "For urgent EGM Deep Dive studies"
3f9409d90498440282596633e8f6b284
rucio add-rule cms:/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO#21c3f19c-fb78-45d2-a7fe-06204ad321a5 1 T2_CH_CERN --lifetime 259200 --comment "For urgent EGM Deep Dive studies"
b3368500d2a644598203c8833970a4fb
rucio add-rule cms:/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO#37fa4659-271f-4f1c-9453-db6e079e6e00 1 T2_CH_CERN --lifetime 259200 --comment "For urgent EGM Deep Dive studies" 
af48d2749241445c9be72e6f450a2914
rucio add-rule cms:/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO#49711f9d-decf-4860-8b3e-e6634978ae2b 1 T2_CH_CERN --lifetime 259200 --comment "For urgent EGM Deep Dive studies"
5aa880378fff4a4193c1ad44c5bddee3
```

### CMSSW set-up
```
cmsrel CMSSW_14_0_15
cd cmsrel CMSSW_14_0_15/src
cmsenv
```

### Run the L1T-HLT step
```
cmsDriver.py  --conditions 140X_dataRun3_HLT_v3 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/385/447/00000/f596385d-f448-4f54-baee-93b8bd21e8e2.root --fileout file:hltOutput_RECO.root --no_exec -n 200 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:GRun
```

This will create the config file to be used. Update the config manually to change the required values by adding editing this config file or directly in cmsCondor submission script:

```
# Load the GRun menu
from HLTrigger.Configuration.HLT_GRun_cff import *
# Modify parameters
## Disble 3 seeds
process.hltL1sSingleEGor.L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5')
## Disable 2 seeds
#process.hltL1sSingleEGor.L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5')
# Original
#process.hltL1sSingleEGor.L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5')
```

Now run the configuration file for local testing
```
cmsRun hlt_ReRun_Config.py
```
 
### Run the PAT step to create miniAOD
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

### Condor Submission Tools
```
##### Input setup #####

# Use the dasFileQuery script to control the number of files/events in the dataset you want to run on
# dasgoclient --query "file dataset=/EGamma0/Run2024G-ZElectron-PromptReco-v1/RAW-RECO | grep file.name,file.nevents" --limit 1425 | awk '{sum += $2} END {print sum}'
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

##### For HLT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration
## L49-L56 for configuration modification, L57-L74 for input source, L77 for events, L80-81 and L129-132 for output file name
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSSW_14_0_15/src/ /eos/cms/store/group/phys_egamma/ssaumya/DeepDive/HLTstep_RECO_RootFiles/ -n 9 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
# -n 10 --> 10 files per job, 145 jobs created in this case
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
## L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/EGM_Bpix/CMSSW_14_0_15/src/ /eos/cms/store/group/phys_egamma/ssaumya/EGM_BPix_Fix/PATstep_MINIAOD_RootFiles/ -n 5 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
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

