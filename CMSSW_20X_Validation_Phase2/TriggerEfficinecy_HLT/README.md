## Relevant Links
- Presentation: 
- Link: https://cms-pdmv-prod.web.cern.ch/valdb/campaigns/20_0_0_Phase2

### Datasets: RelValZpToEE_m6000_14TeV, GEN-SIM-DIGI-RAW
```
# Reference: : /RelValZpToEE_m6000_14TeV/CMSSW_20_0_0-PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU_16Aug26-v6/GEN-SIM-DIGI-RAW
# Target: /RelValZpToEE_m6000_14TeV/CMSSW_20_0_0_pre1-PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU_16Aug26-v3/GEN-SIM-DIGI-RAW
```

#### Rucio rules for dataset if not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/RelValZpToEE_m6000_14TeV/CMSSW_20_0_0_pre1-PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU_16Aug26-v3/GEN-SIM-DIGI-RAW 1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For HLT Phase2 Upgrade EGM Validation of CMSSW_20_0_0"
rucio rule-info be54b28bccde4c17923afeefb7403642
```

## Set-up and commands
```
cmsrel CMSSW_20_0_0; cd CMSSW_20_0_0/src; cmsenv
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6
scram b -j 10

/afs/cern.ch/work/s/ssaumya/private/Egamma/STEAM_4thSeptember/Distributions/CMSSW_20_0_0/src/EGamma-Studies/CMSSW_20X_Validation_Phase2/TriggerEfficinecy_HLT
git clone git@github.com:saumyaphor4252/EGamma-Studies.git
cd EGamma-Studies/CMSSW_20X_Validation_Phase2/TriggerEfficinecy_HLT/
voms-proxy-init --voms cms --valid 100:00
```

### Local Testing of the cmsDriver for the Phase2 dataset (to check geometry, era etc compatibility)

```
cmsDriver.py Phase2 -s L1P2GT,HLT:75e33 --processName=HLTX \
--conditions auto:phase2_realistic_T35 \
--geometry ExtendedRun4D121 \
--era Phase2C22I13M9 \
--eventcontent FEVTDEBUGHLT \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev \
--filein file:/eos/cms//store/relval/CMSSW_20_0_0/RelValZpToEE_m6000_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU_16Aug26-v6/2590000/c3126285-719b-4754-a56f-7cf725cc8310.root 
--fileout file:output_Phas2_HLT.root \
--inputCommands='keep *, drop *_hlt*_*_HLT, drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT' \
--mc \
--python_filename rerunHLT_cfg.py \
-n 1 --nThreads 1
```

### Make/Test ntuples from the HLT Output files
uses the script `makeNtuples_Phase2_HLT.py`

### Submit the jobs on condor to run the HLT step and make ntuples

The yaml configuration (`phase2_ZpToEE_Efficiency_HLT.yaml`) contains the cmsDriver, datasets for Reference and Target, and the directories for running/storing output files.
Upadate the file as per your need.
The jobs are submitted using the script `submit_condor_MC.py`.
 
```
cd EGamma-Workflow/
python3 submit_condor_MC.py --n 1 --config phase2_ZpToEE_Efficiency_HLT.yaml --proxy /afs/cern.ch/user/s/ssaumya/private/x509up_<XXXXXXX> --farm Jobs --nEvent 50
```
This will produce the output ntuples in the output directories specified in the yaml configuration. Hadd them for plotting in the next step.  

### Plotting trigger efficinecy curves from the tuples
```
cd plot_func/
# Update the input tuple files and Ratio labels in Inputs.py, from above tuples after hadd-ing.
python3 plotHist.py
```
