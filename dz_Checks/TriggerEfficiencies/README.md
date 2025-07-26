
## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3610
- Menu used: 
	- Reference: /dev/CMSSW_15_0_0/GRun/V101
	- Target 60: /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_60/V1
	- Target 65: /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_65/V1
	- Target 70: /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_70/V1
	- Target 75: /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_75/V1
- Run used : 393276, 393331, 393346
- CMSSW: CMSSW_15_0_7
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

### CMSSW set-up
```
cmsrel CMSSW_15_0_10; cd CMSSW_15_0_10/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V101 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Reference_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v2/000/393/346/00000/ff8a9f22-21e4-47fc-9f45-b350389d8468.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025C_Reference
```

Repeat the same steps for Target menu

```
### hltGetConfiguration
hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_60/V1 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_Target_60_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v2/000/393/346/00000/ff8a9f22-21e4-47fc-9f45-b350389d8468.root --fileout file:hltOutput_RECO_Traget_60.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Target_60.py --scenario pp --step HLT:2025C_Target_60
```

There is also check where we try to remove the `dz` term in `S^2`. For that we apply change in CMSSW by redefining the `PMS2` variable as follows: 

```
cmsrel CMSSW_15_0_10; cd CMSSW_15_0_10/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
git cms-addpkg RecoEgamma/EgammaHLTProducers
vi RecoEgamma/EgammaHLTProducers/plugins/EgammaHLTPixelMatchVarProducer.cc
# Change line 325 here and remove the last 2 terms coressponding to dz
# float s2 = dPhi1 * dPhi1 + dPhi2 * dPhi2 + dRz2 * dRz2; --> Before
# float s2 = dPhi1 * dPhi1 + dPhi2 * dPhi2; --> After
scram b -j 10
```

Then one can repeat the same steps as for Reference HLT.

An analogus recipe provided by Sanu, where we only checkout the particular file, instead of the whole package is:
```
git remote add sanuvarghese git@github.com:sanuvarghese/cmssw.git  
git fetch sanuvarghese  remove-dRz2-from-s2
git sparse-checkout add RecoEgamma/EgammaHLTProducers/
git cherry-pick b67a936adaf6304d0adfa50f228a5a3a8468a3af
scram b -j 8
``` 

### Run the PAT step to create miniAOD
```
# Run locally
cmsDriver.py stepMINI -s PAT --conditions 150X_dataRun3_Prompt_v1 --datatier MINIAOD -n 100 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2025 --filein file:/hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

This step will be same for both Reference and Targets.
 
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
## L49-L63 for configuration modification of the HLT step, L65-L82 for input source, L85 for events, L90-92 and L140-143 for output file name
# -n 10 --> 10 files per job
python3 cmsCondor.py hlt_ReRun_Config_Reference.py /afs/cern.ch/work/s/ssaumya/private/Egamma/dz_Checks/Reduced_Threshold/CMSSW_15_0_10/src/ /eos/cms/store/group/phys_egamma/ssaumya/dz_Checks/Reduced_Threshold/HLTstep_RECO_RootFiles_Reference/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
python3 cmsCondor.py hlt_ReRun_Config_Target_60.py /afs/cern.ch/work/s/ssaumya/private/Egamma/dz_Checks/Reduced_Threshold/CMSSW_15_0_10/src/ /eos/cms/store/group/phys_egamma/ssaumya/dz_Checks/Reduced_Threshold/HLTstep_RECO_RootFiles_Target_60/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
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
