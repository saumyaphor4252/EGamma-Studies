# Set up for studies for the BPix issue mitigation 

Ideally we would like to re-run HLT step to check the impact, but the issue here are some:
- HLT can only be re-run on RAW, and for calculating the trigger efficiencies we need the EGamma TnP tool which can only run on AOD or MiniAOD because the identification reco IDs are only available there. 
- This means that one would privately have to run all the mediatory steps (AOD, miniAOD) on the output hlt.root files from `hltGetConfiguration`, which require both eos area space, the data on DISK for submitting jobs and the correct cmsDrivers to work. 

A partial less painful solution can be to use the RAW-RECO dataset. 
- Re-run the hlt step using cmsDriver on the RAW-RECO dataset and store all the RECO eventcontent excluding the RAW in the output root file. 
- ReReun the miniAOD step cmsDriver directly on the output root files from above step. 
- Run the TnP producer on the MINIAOD root files from the above output. 
- Use the TnP analysis package to get the efficiency plots. 



# Testing Set-up 
```
cmsrel CMSSW_14_2_1
cd CMSSW_14_2_1/src
cmsenv
git cms init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

Re-run HLT step
```
hltGetConfiguration /dev/CMSSW_14_2_0/GRun/V11 --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v11,HLT_Ele32_WPTight_Gsf_v25,HLT_Ele115_CaloIdVT_GsfTrkIdT_v25,HLT_Ele135_CaloIdVT_GsfTrkIdT_v18,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v29,HLT_DoubleEle33_CaloIdL_MW_v28,HLTriggerFinalPath --output minimal --data --process MYHLT --type GRun --globaltag 141X_dataRun3_HLT_v2 --max-events 100 --unprescale --eras Run3 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2024I_cff.py
cmsDriver.py --conditions 141X_dataRun3_HLT_v2 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO.root --no_exec -n 100 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:2024I
```

This will create the config file to be used. Update the config manually to change the required `maxCand` and `OriginRadius` values by adding eitin this config file or directly in cmsCondor submission script:
```
# Load the GRun menu
from HLTrigger.Configuration.HLT_2024I_cff import *
# Modify parameters
# Reference : Do nothing
# Suggestion 1
#process.HLTPSetTrajectoryBuilderForGsfElectrons.maxCand = cms.int32( 5 )
#process.hltEleSeedsTrackingRegions.RegionPSet.originRadius = cms.double( 0.05 )
# Suggestion 2
process.hltEleSeedsTrackingRegions.RegionPSet.originRadius = cms.double( 0.05 )
process.hltEleSeedsTrackingRegionsUnseeded.RegionPSet.originRadius = cms.double( 0.05 )
```
Now run the configuration file locally to check that the configuration does not crash for the changes needed
```
cmsRun hlt_ReRun_Config.py
```
PAT step
Use the above new RECO root file to get the MINIAOD files
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

# Condor Submission set up
```
# Use the dasFileQuery script to control the number of files/events in the dataset you want to run on
python3 dasFileQuery.py
# This will create the List_cff.py file with the list of input files to be used.
voms-proxy-init --valid 100:00
cp /tmp/x509up_u<999999> /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

#### For HLT step ####
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration
# L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py hlt_ReRun_Config.py /afs/cern.ch/work/s/ssaumya/private/Egamma/EGM_Bpix/CMSSW_14_2_1/src/ /eos/cms/store/group/phys_egamma/ssaumya/EGM_BPix_Fix/10thFeb/HLTstep_RECO_RootFiles_Suggestion1 -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u999999
# -n 10 --> 10 files per job, 149 jobs created in this case
./sub_total.jobb

#### For PAT step ####
# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
# L49-L53 for configuration modification, L55-L72 for input source, L75 for events, L78-79 and L127-130 for output file name
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/EGM_Bpix/CMSSW_14_0_15/src/ /eos/cms/store/group/phys_egamma/ssaumya/EGM_BPix_Fix/PATstep_MINIAOD_RootFiles/ -n 5 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
./sub_total.jobb
```

### Make the ntuples
Set up inside `CMSSW_14_2_1/src`
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

# Code Repo: https://github.com/saumyaphor4252/egamma-tnp/tree/2024_Studies
# Notebook Template: Winter24Checks.ipynb, Wniter24_DataMC_Checks.ipynb
```
