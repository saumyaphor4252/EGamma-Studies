## Relevant Links
- Presentation: 

### Datasets
```
# ZpEE:
```

#### Rucio rules for dataset not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/RelValZpToEE_m6000_14TeV/CMSSW_16_0_0_pre4-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/GEN-SIM-DIGI-RAW 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For HLT Phase2 Upgrade EGM studies"
rucio rule-info be54b28bccde4c17923afeefb7403642 
```

#### Set-up and commands

```
cmsrel CMSSW_16_0_0_pre4; cd CMSSW_16_0_0_pre4/src; cmsenv
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
scram b -j 10

# Update the configuration files for changes required

cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --filein=file:/eos/cms/store/relval/CMSSW_16_0_0_pre4/RelValZpToEE_m6000_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/4e272bbf-46e0-4a11-8b59-c10d9e5dbe23.root --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' --mc -n 5

python3 cmsCondor.py Phase2_L1P2GT_HLT.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/CMSSW_16_0_0_pre4/src/ZpEE/ /eos/cms/store/group/phys_egamma/ssaumya/Phase2_InefficiencyChecks/ZpToEE/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u122184
./sub_total.jobb

```
