### Set up the rucio rules if needed for the files/blocks as per required minimally 
```
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#4a2f0c6d-e420-4818-9bef-7d6d05b5fe1a 1 T2_CH_CERN --lifetime 1296000 --comment "For important EGM-HLT studies"
ffdc6aca96574e899933d726b90f1569
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#a49af9ca-d948-46ba-b2e6-f772da0a83fe 1 T2_CH_CERN --lifetime 1296000 --comment "For urgent TSG EGM Deep Dive studies"
c7b2f5110b2c48e4aea188220fbd450c
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#35ff20a6-563a-4de9-a62a-5ae603bc9098 1 T2_CH_CERN --lifetime 1296000 --comment "For important EGM-HLT studies"
27d4b8ac0d05414ca00448f278d6d5be
rucio add-rule cms:/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO#dce53cd5-669d-4c00-afa5-2625c1470d99 1 T2_CH_CERN --lifetime 1296000 --comment "For important EGM-HLT studies"
e70d5aff71dd4bdfac4732ae4706aced
```

#### Dataset used: SpecialHLTPhysics0 Run 386050
```
/EGamma1/Run2024I-ZElectron-PromptReco-v1/RAW-RECO
```

### Recipe from L1 
```
### CMSSW set-up
cmsrel CMSSW_14_0_13; cd CMSSW_14_0_13/src; cmsenv
git cms-init
git cms-addpkg L1Trigger/L1TGlobal
git cms-addpkg L1Trigger/Configuration
git cms-addpkg HLTrigger/Configuration
git cms-addpkg L1Trigger/L1TCalorimeter
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

### L1 modifications
mkdir -p L1Trigger/L1TGlobal/data/Luminosity/startup
cd L1Trigger/L1TGlobal/data/Luminosity/startup
wget https://raw.githubusercontent.com/cms-l1-dpg/L1MenuRun3/master/development/L1Menu_Collisions2024_v1_3_0/L1Menu_Collisions2024_v1_3_0.xml
wget https://raw.githubusercontent.com/cms-l1-dpg/L1MenuRun3/master/development/L1Menu_Collisions2024_v1_3_0/PrescaleTable/UGT_BASE_RS_PRESCALES_L1Menu_Collisions2024_v1_3_0.xml
wget https://raw.githubusercontent.com/cms-l1-dpg/L1MenuRun3/master/development/L1Menu_Collisions2024_v1_3_0/PrescaleTable/UGT_BASE_RS_FINOR_MASK_L1MenuCollisions2023_v1_3_0.xml
cd -
sed -i "s|process\.TriggerMenu\.L1TriggerMenuFile = cms\.string('L1Menu_Collisions2022_v1_2_0\.xml')|process.TriggerMenu.L1TriggerMenuFile = cms.string('L1Menu_Collisions2024_v1_3_0.xml')|" L1Trigger/Configuration/python/customiseUtils.py

### Add last EG LUTs (by copy attached files manually)
vi EG_Iso_LUT_Loose_582_10p0_0p7_40p0_v2_SEP2024.txt
vi EG_Iso_LUT_Tight_1290_20p0_0p7_40p0_v2_SEP2024.txt
cp EG_Iso_LUT_*SEP2024.txt L1Trigger/L1TCalorimeter/data
vi caloParams_2024_v0_3_cfi.py
cp caloParams_2024_v0_3_cfi.py L1Trigger/L1TCalorimeter/python
cat << EOF >> L1Trigger/Configuration/python/customiseSettings.py
def L1TSettingsToCaloParams_2024_v0_3(process):
    process.load("L1Trigger.L1TCalorimeter.caloParams_2024_v0_3_cfi")
    return process
EOF

git cms-checkdeps -A -a
scram b -j 8

### RAWRECO (L1T+HLT re-emu with new spike killer settings) 
cmsDriver.py test --step RAW2DIGI,L1REPACK:FullSimTP,HLT --conditions 150X_dataRun3_HLT_v1 --data --datatier RECO --era Run3_2024 --eventcontent RECO --filein file:/eos/cms/store/data/Run2024I/EGamma1/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/fc9479a6-fffe-4e2a-94b7-3eea7f245216.root --fileout file:hltOutput_RECO_Reference.root --no_exec -n 100 --process MYHLT --python_filename L1-HLT_re-emu.py --customise=L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2024_v0_3 --geometry DB:Extended
```

This will create the config file L1-HLT_re-emu.py to be used. 

```
# customize the config file 
cat << EOF >> L1-HLT_re-emu.py
process.load('L1Trigger.L1TGlobal.simGtStage2Digis_cfi')
process.load('L1Trigger.L1TGlobal.hackConditions_cff')
process.L1TGlobalPrescalesVetosFract.PrescaleXMLFile = cms.string('UGT_BASE_RS_PRESCALES_L1Menu_Collisions2024_v1_3_0.xml')
process.L1TGlobalPrescalesVetosFract.FinOrMaskXMLFile = cms.string('UGT_BASE_RS_FINOR_MASK_L1MenuCollisions2023_v1_3_0.xml')
process.simGtStage2Digis.AlgorithmTriggersUnmasked = cms.bool(False)
process.simGtStage2Digis.AlgorithmTriggersUnprescaled = cms.bool(False)
process.simGtStage2Digis.PrescaleSet = cms.uint32(7)
process.simGtStage2Digis.resetPSCountersEachLumiSec = cms.bool(False)
process.simGtStage2Digis.semiRandomInitialPSCounters = cms.bool(True)
EOF
```

Update the config manually to change the required values/settings by editing this config file or directly in cmsCondor submission script below:
```
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_HLT_v3', '')
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),
        tag = cms.string('EcalTPGSpike_16'),
        connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
    ),
    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
    tag = cms.string('EcalTPGFineGrainStrip_28'),
    #tag = cms.string('EcalTPGFineGrainStrip_26'),
    connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
    )
)
```

Now run the configuration file for local testing
```
cmsRun L1-HLT_re-emu.py
```
 
### Config for PAT step set-up from the re-HLT output file
```
cmsDriver.py stepMINI -s PAT --conditions 140X_dataRun3_Prompt_v3 --datatier MINIAOD -n 200 --eventcontent MINIAOD --python_filename makeMini_cfg.py --geometry DB:Extended --era Run3_2024 --filein file:test_RAW2DIGI_L1REPACK_HLT.root --fileout file:stepMINI.root --hltProcess MYHLT
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
python3 cmsCondor.py L1-HLT_re-emu.py /afs/cern.ch/work/s/ssaumya/private/Egamma/SpikeKiller/CMSSW_14_0_13/src/ /eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/HLTstep_RECO_RootFiles_Reference/ -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
# -n 10 --> 10 files per job, 41 jobs created in this case
./sub_total.jobb

##### For PAT step #####

# Update the cmsCondor.py accordingly for input and output, and the change needed in hltConfiguration  
python3 cmsCondor.py makeMini_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/SpikeKiller/CMSSW_14_0_13/src/ /eos/cms/store/group/phys_egamma/ssaumya/2025_SpikeKiller/PATstep_MINIAOD_RootFiles_Reference/ -n 5 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
```

### Make the ntuples
Set up inside `CMSSW_14_0_1333rc`
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
