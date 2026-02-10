## Relevant Links
- Presentation: https://indico.cern.ch/event/1578363/contributions/6650120/subcontributions/568183/attachments/3119988/5532472/EGM_HLT_151X_pre4_Validation_19thAugust_2025.pdf
- Link: https://cms-pdmv-prod.web.cern.ch/valdb/campaigns/15_1_0_pre4_Phase2_D110

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

cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX --conditions auto:phase2_realistic_T33 --geometry ExtendedRun4D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --filein=file:/eos/cms/store/relval/CMSSW_15_1_0_pre3/RelValZpToEE_m6000_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2590000/fe4d939e-c351-47e6-8fd2-8c1be859bfda.root --inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' --mc -n 10

python3 cmsCondor.py Phase2_L1P2GT_HLT.py /afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/Distributions/CMSSW_15_1_0_pre4/src/15_1_0_pre4/ /eos/cms/store/group/phys_egamma/ssaumya/15_1_0_pre4_Validation/Target/ -n 1 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u999999
./sub_total.jobb

python3 makeNtuples_Phase2.py --input-dir "/eos/cms/store/group/phys_egamma/ssaumya/15_1_0_pre4_Validation/Reference/" -o Ntuple_15_1_0_pre3_Validation.root -n 10000

python plot_Phase2_EGM_Variables.py Ntuple_15_1_0_pre4_Validation.root Ntuple_15_1_0_pre4_Validation.root 15_1_0_pre4_Validation_ Reference Target
```

## For Tracker relevant EGM variables


## For Trigger Efficiencies

