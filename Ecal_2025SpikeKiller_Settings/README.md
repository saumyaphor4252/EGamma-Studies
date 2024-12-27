### Set up the rucio rules if needed for the files/blocks as per required minimally 
```
rucio add-rule cms:/SpecialHLTPhysics0/Run2024H-v1/RAW 1 T2_CH_CERN --lifetime 432000 --comment "For TSG EGM studies of Ecal 2025 spike killer settings"
4d2794c5123245468e57f12dab4f7647
rucio add-rule cms:/SpecialHLTPhysics1/Run2024H-v1/RAW 1 T2_CH_CERN --lifetime 432000 --comment "For TSG EGM studies of Ecal 2025 spike killer settings"
35e228367b2c4e12b02ac4e0bd1f903b
```

#### Dataset used: SpecialHLTPhysics0 Run 386050
```
/SpecialHLTPhysics0/Run2024H-v1/RAW
```

### Recipe from L1 
```
### CMSSW set-up
cmsrel CMSSW_14_0_13
cd CMSSW_14_0_13/src
cmsenv
git cms-init
git cms-addpkg L1Trigger/L1TGlobal
git cms-addpkg L1Trigger/Configuration
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
cp EG_Iso_LUT_*SEP2024.txt L1Trigger/L1TCalorimeter/data
cp caloParams_2024_v0_3_cfi.py L1Trigger/L1TCalorimeter/python
cat << EOF >> L1Trigger/Configuration/python/customiseSettings.py
def L1TSettingsToCaloParams_2024_v0_3(process):
    process.load("L1Trigger.L1TCalorimeter.caloParams_2024_v0_3_cfi")
    return process
EOF

git cms-checkdeps -A -a
scram b -j 8

### RAWRECO (L1T+HLT re-emu with new spike killer settings) 
cmsDriver.py test -s RAW2DIGI,L1REPACK:FullSimTP,HLT --conditions 140X_dataRun3_HLT_v3 --python_filename=L1-HLT_re-emu.py --filein /store/data/Run2024H/SpecialHLTPhysics0/RAW/v1/000/386/048/00000/1efac410-2883-4bce-a01c-93e617ac26a3.root --customise=L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2024_v0_3 --geometry DB:Extended --era Run3_2024 --data --processName=MYHLT -n -1 --no_exec
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
