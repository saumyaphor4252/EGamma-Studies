## Relevant Links
- Presentation: https://indico.cern.ch/event/1602818/#sc-2-2-egamma
- Link: https://cms-pdmv-prod.web.cern.ch/valdb/campaigns/15_1_0_pre6_Phase2_D110

### Datasets
```
# Reference: CMSSW_15_1_0_pre5:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/GEN-SIM-DIGI-RAW
# Target: CMSSW_15_1_0_pre6:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre6-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/GEN-SIM-DIGI-RAW
```

#### Rucio rules for dataset not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/GEN-SIM-DIGI-RAW 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For HLT Phase2 Upgrade EGM Validation of CMSSW_15_1_0_pre6"
rucio rule-info be54b28bccde4c17923afeefb7403642 
```

## For EGM Variable distributions

### Scripts with details
 
- makeNtuples_Phase2.py
	- To make tuples from hlt.root files
- plot_Phase2_EGM_Variables.py 
	- To get the plots from tuples

#### Set-up and commands

```
cmsrel CMSSW_15_1_0_pre4; cd CMSSW_15_1_0_pre4/src; cmsenv
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
scram b -j 10

cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --filein=file:/eos/cms/store/relval/CMSSW_15_1_0_pre5/RelValZpToEE_m6000_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/60162ee0-7e0e-427b-b358-847a52097dfe.root --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' --mc -n 5

python3 cmsCondor.py Phase2_L1P2GT_HLT.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/Distributions/CMSSW_15_1_0_pre4/src/15_1_0_pre5/ /eos/cms/store/group/phys_egamma/ssaumya/15_1_0_pre6_Validation/Target/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb

python3 makeNtuples_Phase2.py --input-dir "/eos/cms/store/group/phys_egamma/ssaumya/15_1_0_pre6_Validation/Target/" -o Ntuple_15_1_0_pre6_Validation.root -n 10000

python3 plot_Phase2_EGM_Variables.py Ntuple_15_1_0_pre5_Validation.root Ntuple_15_1_0_pre6_Validation.root 15_1_0_pre6_Validation 15_1_0_pre5 15_1_0_pre6
```
