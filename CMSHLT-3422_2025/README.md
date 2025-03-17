## Relevant Links
- The baseline for these studies has to be the mkFit+CA tuning (as recommended by TSG)
- From Tracking: the latest recipe for `15_0_X` cycle
https://docs.google.com/document/d/1bX-ckRcYcMqfykcWAbIPfkCCwkpheywtNW981OP-r80/edit?tab=t.0#heading=h.mw406pivxy4q
   - The section for "CA pixel-only (patatrack) re-tuning + mkFit at HLT (for iter-0)"

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
mkdir L1_min_Cluster_Charge
cd L1_min_Cluster_Charge/
cmsrel CMSSW_15_0_0; cd CMSSW_15_0_0/src; cmsenv
git cms-addpkg HLTrigger/Configuration
git cms-addpkg RecoTracker/MkFit/
git remote add ElusianTempRepo git@github.com:elusian/cmssw.git
git fetch ElusianTempRepo 1500p3_newCAtuning
git cherry-pick d73d7272d66e7c702a615557bc4ced4ba8766019
git cherry-pick 622039de51b5cac83fa72fa901990e1eeeb9b8d0
scram b -j 10
```
## Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration /dev/CMSSW_14_2_0/GRun/V12 --output minimal --data --process MYHLT --type GRun --globaltag 141X_dataRun3_HLT_v2 --max-events 100 --unprescale --eras Run3_2024 --customise HLTrigger/Configuration/customize_CAPixelOnlyRetune.customize_CAPixelOnlyRetuneSameEff,RecoTracker/MkFit/customizeHLTIter0ToMkFit.customizeHLTIter0ToMkFit --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_cff.py

### Re-run HLT step
cmsDriver.py --conditions 141X_dataRun3_HLT_v2 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2024I

### Now run the configuration file for local testing
cmsRun hlt_ReRun_Config.py

### Create list of Files to be used for running the jobs using DAS query file
python3 dasFileQuery.py # Update the dataset manually used here if not already; /EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO in this case
# This will generate List_cff.py with files list

### Submit on condor
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/L1_min_Cluster_Charge/CMSSW_14_2_2/src /eos/cms/store/group/phys_egamma/ssaumya/L1_min_Cluster_Charge/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<9999>
# Format for above command: python3 cmsCondor.py <config_file> <CMSSW_Area> <Output_Files_Area> -n <number_of_files_per_job> -q <flavour> -p <voms_proxy_area>
./sub_total.jobb
```
For Target, add the following in the `cmsCondor.py` for the HLT step:

```
process.hltSiPixelClustersSoA.clusterThreshold_layer1 = 2000
process.hltSiPixelClusters.clusterThreshold_layer1 = 2000
process.hltSiPixelClustersSoASerialSync.clusterThreshold_layer1 = 2000
process.hltSiPixelClustersSerialSync.clusterThreshold_layer1 = 2000
process.hltSiPixelClustersRegForDisplaced.ClusterThreshold_L1 = 2000
```
 
## Run the PAT step to create miniAOD (Common for Reference and Target)
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT

#### For condor submission ####
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
# L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/L1_min_Cluster_Charge/CMSSW_15_0_0/src/PAT_Step/ /eos/cms/store/group/phys_egamma/ssaumya/L1_min_Cluster_Charge/PATstep_MINIAOD_RootFiles_Reference/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<9999>
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
```
ssh -o ServerAliveInterval=10 ssaumya@lxplus9.cern.ch -L8777:localhost:8777
cd /afs/cern.ch/user/s/ssaumya/Egamma/egamma-tnp/
source egmtnpenv/bin/activate
jupyter lab --no-browser --port 8777

# Code used: https://github.com/saumyaphor4252/egamma-tnp/tree/2024_Studies
# Notebook templates: Winter24Checks.ipynb, Wniter24_DataMC_Checks.ipynb
```
