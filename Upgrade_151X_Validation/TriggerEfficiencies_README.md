## Relevant Links
- Presentation: 
- RelMon: 

### Datasets
```
# CMSSW_15_0_0_pre3:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2/MINIAODSIM 

# CMSSW_15_1_0_pre1:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1/MINIAODSIM

# CMSSW_15_1_0_pre2:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/MINIAODSIM

# CMSSW_15_1_0_pre3:
	/RelValZpToEE_m6000_14TeV/CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/MINIAODSIM
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
python3 lastFilterEffHist_Upgrade.py /eos/cms/store/relval/CMSSW_15_0_0_pre3/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2/2580000/*.root -o outputFile_CMSSW_15_0_0_pre3.root 2>&1 | tee log_CMSSW_15_0_0_pre3.out

python3 lastFilterEffHist_Upgrade.py /eos/cms/store/relval/CMSSW_15_1_0_pre1/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_CMSSW_15_1_0_pre1.root 2>&1 | tee log_CMSSW_15_1_0_pre1.out

python3 lastFilterEffHist_Upgrade.py /eos/cms/store/relval/CMSSW_15_1_0_pre2/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2580000/*.root -o outputFile_CMSSW_15_1_0_pre2.root 2>&1 | tee log_CMSSW_15_1_0_pre2.out

python3 lastFilterEffHist_Upgrade.py /eos/cms/store/relval/CMSSW_15_1_0_pre3/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2590000/*.root -o outputFile_CMSSW_15_1_0_pre3.root 2>&1 | tee log_CMSSW_15_1_0_pre3.out

```

### Plotting

```
python3 plotHist.py
```
