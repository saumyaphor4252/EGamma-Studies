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
cmsrel CMSSW_14_0_15
cd cmsrel CMSSW_14_0_15/src
cmsenv
```
Check the content of the RAWRECO file and save it
```
edmDumpEventContent /eos/cms/store/data/Run2024G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/385/443/00000/f9934f4e-60de-4ef6-a48a-77b7e1b07ebf.root > Original_RAWRECO_Content.txt
```

Re-run HLT step
```
cmsDriver.py  --conditions 140X_dataRun3_HLT_v3 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/385/443/00000/f9934f4e-60de-4ef6-a48a-77b7e1b07ebf.root --fileout file:hltOutput_RECO.root --no_exec -n 200 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:GRun
```
This will create the config file to be used. Update the config manually to change the required `maxCand` and `OriginRadius` values by adding:
```
process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    maxCand = cms.int32(5),
)

process.hltEleSeedsTrackingRegions = cms.EDProducer( "TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
            originRadius = cms.double(0.2),
    )        
)
```
Now run the configuration file
```
cmsRun hlt_ReRun_Config.py
```
Check the content of the output RAWRECO file and compare it with the original RAWRECO file. The RAW should be removed and the additional `MYHLT` results should be added.

```
edmDumpEventContent hltOutput_RECO.root > Updated_hltStep_RECO_Content.txt
```

Use the above new RECO root file to get the MINIAOD files
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:hltOutput_RECO.root --fileout file:stepMINI.root --hltProcess MYHLT
```

Compare to see the difference in the eventContent for this output file Vs a standard MINIAOD file. It should be mainly in the collection name: RECO or PAT, and the additional `MYHLT` collection 

```
edmDumpEventContent stepMINI.root > Updated_MINIAOD_Content.txt
edmDumpEventContent /eos/cms/store/data/Run2024J/EGamma0/MINIAOD/PromptReco-v1/000/387/343/00000/02584808-456f-47ef-a729-50aad0a3bc02.root > Original_MINIAOD_Content.txt
```

Now check that the output file from above can be used as input to the TnP Producer


# Datasets
- The RAWRECO dataset: `/EGamma1/Run2024G-ZElectron-PromptReco-v1/RAW-RECO` ([DAS Link](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FEGamma0%2FRun2024G-ZElectron-PromptReco-v1%2FRAW-RECO))
- MINIAOD: `/EGamma0/Run2024G-PromptReco-v1/MINIAOD` ([DAS Link](https://cmsweb.cern.ch/das/request?view=plain&limit=50&instance=prod%2Fglobal&input=file+dataset%3D%2FEGamma0%2FRun2024G-PromptReco-v1%2FMINIAOD))

# Test Files
- RAWRECO file: 
```
edmDumpEventContent /eos/cms/store/data/Run2024G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/385/443/00000/f9934f4e-60de-4ef6-a48a-77b7e1b07ebf.root
```

# Set up
```
cmsDriver.py  --conditions 140X_dataRun3_HLT_v3 --data --datatier RECO --era Run3 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024G/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/385/443/00000/f9934f4e-60de-4ef6-a48a-77b7e1b07ebf.root --fileout file:stepHLT.root --no_exec -n 200 --process MYHLT --python_filename hlt_ReRun_Config.py --scenario pp --step HLT:GRun

```
