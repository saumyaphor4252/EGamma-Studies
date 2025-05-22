### Dataset used:
```
/EGamma0/Run2025C-ZElectron-PromptReco-v1/RAW-RECO
/EGamma1/Run2025C-ZElectron-PromptReco-v1/RAW-RECO
/EGamma2/Run2025C-ZElectron-PromptReco-v1/RAW-RECO
/EGamma3/Run2025C-ZElectron-PromptReco-v1/RAW-RECO
```
Files used listed in List_cff.py.

## CMSSW set-up
```
cmsrel CMSSW_15_0_5; cd CMSSW_15_0_5/src; cmsenv
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V79 --output minimal --data --process MYHLT --type GRun --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/392/296/00000/e44e2412-446a-4bb7-807e-163ecb4451fc.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2025C

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config.py
```
 
### Run the PAT step to create miniAOD
```
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2025 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

### CONDOR submission
```
##### Input setup #####

# Use the dasFileQuery script to control the number of files/events in the dataset you want to run on
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

##### For HLT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration
## L49-L56 for configuration modification, L57-L74 for input source, L77 for events, L80-81 and L129-132 for output file name
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/STEAM_23rdMay2025/CMSSW_15_0_5/src/ /eos/cms/store/group/phys_egamma/ssaumya/STEAM_22ndMay_2025/HLTstep_RECO_RootFiles/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output
## L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/STEAM_23rdMay2025/CMSSW_15_0_5/src/ /eos/cms/store/group/phys_egamma/ssaumya/STEAM_22ndMay_2025/PATstep_MINIAOD_RootFiles/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
./sub_total.jobb
```

### Make the ntuples
Set up inside `CMSSW_15_0_5/src`
```
git clone -b Private_MINIAOD_2025_Data git@github.com:saumyaphor4252/EgammaAnalysis-TnPTreeProducer.git EgammaAnalysis/TnPTreeProducer
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

