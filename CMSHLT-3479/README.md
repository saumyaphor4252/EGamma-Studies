## Relevant Links
- https://its.cern.ch/jira/browse/CMSHLT-3479
- Results: https://indico.cern.ch/event/1527098/contributions/6425132/subcontributions/539022/attachments/3043138/5376302/EGM_FineTuning.pdf

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
mkdir CMSHLT-3749
cd CMSHLT-3749/
cmsrel CMSSW_15_0_2; cd CMSSW_15_0_2/src; cmsenv
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

We will first re-run the HLT step, and then run the PAT step because of the required offline ID info in miniAOD/AOD (See https://github.com/saumyaphor4252/EGamma-Studies/tree/main/EGamma_BPix_Issue_Mitigation#readme)

## Run the HLT step
```
### hltGetConfiguration
# Reference:
hltGetConfiguration /users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3479/Test01/GRun/V1 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2024 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO_Reference.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2024I_Reference

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config_Reference.py

### Create list of Files to be used for running the jobs using DAS query file
python3 dasFileQuery.py # Update the dataset manually used here if not already; /EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO in this case
# This will generate List_cff.py with files list

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/FineTuning/UpdatedMenu/CMSSW_15_0_2/src/HLT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/FineTuning/UpdatedMenu/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
# Format for above command: python3 cmsCondor.py <config_file> <CMSSW_Area> <Output_Files_Area> -n <number_of_files_per_job> -q <flavour> -p <voms_proxy_area>
./sub_total.jobb
```

For Target, update the target menu and repeat above commands as follows:
```

hltGetConfiguration /users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3479/Test01/GRun/V2 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2024 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_Target_cff.py

cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO_Target.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target.py --scenario pp --step HLT:2024I_Target

cmsRun hlt_ReRun_Config_Target.py

python3 cmsCondor.py hlt_ReRun_Config_Target.py /afs/cern.ch/work/s/ssaumya/private/Egamma/FineTuning/UpdatedMenu/CMSSW_15_0_2/src/HLT_Target/ /eos/cms/store/group/phys_egamma/ssaumya/FineTuning/UpdatedMenu/HLTstep_RECO_RootFiles_Target/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
```

## Run the PAT step to create miniAOD (Common for Reference and Target)
```
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:../HLT_Reference/hltOutput_RECO_Reference.root --fileout file:stepMINI.root --hltProcess MYHLT

#### For condor submission ####
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
# L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name

python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/FineTuning/UpdatedMenu/CMSSW_15_0_2/src/PAT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/FineTuning/UpdatedMenu/PATstep_MINIAOD_RootFiles_Reference/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb
```

### Make the ntuples
Set up inside `CMSSW_XYZ/src`
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

If you running the tool for the first time see also https://github.com/saumyaphor4252/egamma-tnp/tree/2024_Studies 

## First time setup
If you running the tool for the first time: 
```
ssh ssaumya@lxplus9.cern.ch -L8787:localhost:8787
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/IasonTool/
git clone -b 2024_Studies git@github.com:saumyaphor4252/egamma-tnp.git
cd egamma-tnp/
python3 -m venv egmtnpenv
source egmtnpenv/bin/activate
pip install jupyter
pip install ipython
pip install ipykernel
ipython kernel install --user --name=egmtnpenv
python -m ipykernel install --user --name=egmtnpenv
pip install . --no-cache-dir
jupyter lab --no-browser --port 8787
```

## After initial set-up 
Once the set-up is done, once can use the below commands from next time:
```
ssh -o ServerAliveInterval=10 ssaumya@lxplus9.cern.ch -L8787:localhost:8787
cd /afs/cern.ch/work/s/ssaumya/private/Egamma/IasonTool/egamma-tnp/
source egmtnpenv/bin/activate
jupyter lab --no-browser --port 8787

# Code/Branch used: https://github.com/saumyaphor4252/egamma-tnp/tree/2024_Studies
# Notebook template: https://github.com/saumyaphor4252/egamma-tnp/blob/2024_Studies/SpikeKiller_FineTuning.ipynb
```
