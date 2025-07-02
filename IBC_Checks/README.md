## Relevant Links
- JIRA : https://its.cern.ch/jira/browse/CMSHLT-3589
- CMSALCA-325 : https://its.cern.ch/jira/browse/CMSALCA-325
- Menu used: /cdaq/physics/Run2025/2e34/v1.1.4/HLT/V1
- Run used : 393276, 393331, 393346
- CMSSW: CMSSW_15_0_7
- Target Vs Reference: GTs
	- HLT: 150X_dataRun3_HLT_TkAl_Target_w26_v1 (except BS tags) vs 150X_dataRun3_HLT_v1
	- Prompt: 150X_dataRun3_Prompt_TkAl_Target_w26_v1 vs 150X_dataRun3_Prompt_v1

### Set up the rucio rules for the files/blocks as per required minimally for the testing
```
[ssaumya@lxplus952 ~]$ rucio add-rule cms:/EGamma0/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#4c88add9-27f5-4dca-9bd8-8f726f805049  1 T2_CH_CERN  --lifetime 1296000 --comment "For important 2025C EGM-HLT studies"
93145c5906794833a42f58d55d2d3f78
[ssaumya@lxplus952 ~]$ rucio add-rule cms:/EGamma1/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#49df50de-dfb4-4f90-be37-c2b3da4a49e6  1 T2_CH_CERN  --lifetime 1296000 --comment "For important 2025C EGM-HLT studies"
e8177cdc6f4b4432b3bf9c981e91247d
[ssaumya@lxplus952 ~]$ rucio add-rule cms:/EGamma2/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#836b224a-121a-4f28-9619-49f58dbb60c1  1 T2_CH_CERN  --lifetime 1296000 --comment "For important 2025C EGM-HLT studies"
ce3e9d9e885d4f97acfcf49aca1b0e61
[ssaumya@lxplus952 ~]$ rucio add-rule cms:/EGamma3/Run2025C-ZElectron-PromptReco-v2/RAW-RECO#73202192-8584-485e-af18-374c030746d4  1 T2_CH_CERN  --lifetime 1296000 --comment "For important 2025C EGM-HLT studies"
219c50f6f1774ae399562823b2a0b3b3
```

### CMSSW set-up
```
cmsrel CMSSW_15_0_7; cd CMSSW_15_0_7/src; cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
scram b -j 10
```

### Run the HLT step
```
### hltGetConfiguration
hltGetConfiguration adg:/cdaq/physics/Run2025/2e34/v1.1.4/HLT/V1 --output minimal --data --process MYHLT --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2025 --cff > "${CMSSW_BASE}"/src/HLTrigger/Configuration/python/HLT_2025C_cff.py

### Re-run HLT step
cmsDriver.py --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2025 --eventcontent RECO --filein file:/eos/cms/store/data/Run2025C/EGamma0/RAW-RECO/ZElectron-PromptReco-v2/000/393/346/00000/ff8a9f22-21e4-47fc-9f45-b350389d8468.root --fileout file:hltOutput_RECO_Reference.root -n 100 --process MYHLT --python_filename hlt_ReRun_Config_Reference.py --scenario pp --step HLT:2025C
```

##### Reference Vs Target HLT step
Update `hlt_ReRun_Config_Target.py` with respect to `hlt_ReRun_Config_Reference.py` to update the Global Tag as follows:
```
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_HLT_v1', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_HLT_TkAl_Target_w26_v1', '')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
        tag = cms.string('BeamSpotObjects_PCL_byRun_v0_hlt'),
        connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
    ),
    cms.PSet(record = cms.string('BeamSpotOnlineHLTObjectsRcd'),
        tag = cms.string('BeamSpotOnlineHLT'),
        connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
    ),
    cms.PSet(record = cms.string('BeamSpotOnlineLegacyObjectsRcd'),
        tag = cms.string('BeamSpotOnlineLegacy'),
        connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
    )
)
```
 
### Run the PAT step to create miniAOD
```
# Run locally

```
 
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
python3 cmsCondor.py hlt_ReRun_Config_Target.py /afs/cern.ch/work/s/ssaumya/private/Egamma/2025_CMSHLT-3566/CMSSW_15_0_7/src/HLT_Target/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3566/HLTstep_RECO_RootFiles_Target/ -n 7 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/2025_CMSHLT-3566/CMSSW_15_0_7/src/PAT_Reference/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3566/PATstep_MINIAOD_RootFiles_Reference/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
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
