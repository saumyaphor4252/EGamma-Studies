## Relevant Links
- Presentation: 

### Datasets
```
# ZpEE: /RelValZpToEE\_m6000\_14TeV/CMSSW\_16\_0\_0\_pre4-PU\_150X\_mcRun4\_realistic\_v1\_STD\_Run4D110\_PU-v1/GEN-SIM-DIGI-RAW
	
# ZEE: /RelValZEE\_14/CMSSW\_16\_0\_0\_pre4-PU\_150X\_mcRun4\_realistic\_v1\_STD\_Run4D110\_PU-v1/GEN-SIM-DIGI-RAW

# QCD: /RelValQCD\_Pt15To7000\_Flat\_14/CMSSW\_16\_0\_0\_pre4-PU\_150X\_mcRun4\_realistic\_v1\_STD\_Run4D110\_PU-v1/GEN-SIM-DIGI-RAW

# SingleElectron: /RelValSingleEFlatPt2To100/CMSSW_16_0_0_pre4-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/GEN-SIM-DIGI-RAW

# SingleGamma: /RelValSingleGammaFlatPt8To150/CMSSW\_16\_0\_0\_pre4-PU\_150X\_mcRun4\_realistic\_v1\_STD\_Run4D110\_PU-v1/GEN-SIM-DIGI-RAW
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

# HLT step
cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --filein=file:/eos/cms/store/relval/CMSSW_16_0_0_pre4/RelValZpToEE_m6000_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/4e272bbf-46e0-4a11-8b59-c10d9e5dbe23.root --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' --mc -n 5
cmsRun Phase2_L1P2GT_HLT.py

# Submit jobs on condor
python3 cmsCondor.py Phase2_L1P2GT_HLT.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/CMSSW_16_0_0_pre4/src/ZpEE/ /eos/cms/store/group/phys_egamma/ssaumya/Phase2_InefficiencyChecks/ZpToEE/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>
./sub_total.jobb

# Make ntuples from the HLT files
python3 lastFilterEfficiency_Upgrade.py --input-dir /eos/cms/store/group/phys_egamma/ssaumya/Phase2_InefficiencyChecks/ZpToEE/ -o Target.root --output-dir OutputNtuples_Target

# Plot the distributions for different samples together
python3 plot_Phase2_EGM_Variables.py ../Ntuple_16_0_0_pre4_QCD.root ../Ntuple_16_0_0_pre4_SingleE.root ../Ntuple_16_0_0_pre4_ZEE.root ../Ntuple_16_0_0_pre4_ZpEE.root Comparison "QCD" "SingleE" "ZEE" "ZpEE"
```
