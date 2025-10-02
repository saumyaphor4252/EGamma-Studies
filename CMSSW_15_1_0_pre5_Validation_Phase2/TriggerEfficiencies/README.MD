## Relevant Links
- Presentation: https://indico.cern.ch/event/1587306/#sc-2-2-egamma

### Datasets
```
# Reference: CMSSW_15_1_0_pre4:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre4-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/MINIAODSIM
# Target: CMSSW_15_1_0_pre5:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/MINIAODSIM
```

### CMSSW set-up
```
cmsrel CMSSW_15_1_0_pre1; cd CMSSW_15_1_0_pre1/src; cmsenv
scram b -j 10
```

### Scripts with details
- For getting histograms: 
- For plotting trigger Efficiencies: 
	- Inputs.py
	- plotter
	- filter_configs
	

```
python3 lastFilterEffHist_Upgrade_Test.py /eos/cms/store/relval/CMSSW_15_1_0_pre5/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_ZpToEE_CMSSW_15_1_0_pre5.root 2>&1 | tee log_CMSSW_15_1_0_pre5_ZpToEE.out

python3 lastFilterEffHist_Upgrade_Test.py /eos/cms/store/relval/CMSSW_15_1_0_pre4/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_ZpToEE_CMSSW_15_1_0_pre4.root 2>&1 | tee log_CMSSW_15_1_0_pre4_ZpToEE.out

python3 lastFilterEffHist_Upgrade_MINIAOD.py /eos/cms/store/relval/CMSSW_15_1_0_pre4/RelValZEE_14/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_ZEE_CMSSW_15_1_0_pre4.root 2>&1 | tee log_CMSSW_15_1_0_pre4_ZEE.out

python3 lastFilterEffHist_Upgrade_MINIAOD.py /eos/cms/store/relval/CMSSW_15_1_0_pre5/RelValZEE_14/
MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_ZEE_CMSSW_15_1_0_pre5.root 2>&1 | tee log_CMSSW_15_1_0_pre5_ZEE.out
```

### Plotting

```
python3 plotHist.py
```
