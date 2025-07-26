## Rates Recipe

### Relevent Links: 
- https://twiki.cern.ch/twiki/bin/viewauth/CMS/SteamHLTRatesCalculation#Rate_calculation_AN1

### STEAM Git repo:
- https://github.com/cms-steam/SteamRatesEdmWorkflow/tree/master


#### Set up
```
# CMSSW set-up
cmsrel CMSSW_15_0_10; cd CMSSW_15_0_10/src; cmsenv
git clone https://github.com/sanuvarghese/SteamRatesEdmWorkflow.git
scram b -j 8 
cd SteamRatesEdmWorkflow/Prod/

# hltGetConfiguration: get desired menu
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V101 --full --offline --globaltag 150X_dataRun3_HLT_v1 --data --process MYHLT --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --no-output --max-events -1 --input file:/eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/461/00000/ab171c23-c750-4f83-9fea-da7d17503e86.root > hlt.py

edmConfigDump hlt.py > hlt_config_Reference.py

# proxy set-up
voms-proxy-init --voms cms --valid 168:00
	cp /tmp/x509up_<user proxy> /afs/cern.ch/user/<letter>/<username>/private/

# create jobs
# ./cmsCondorData.py run_steamflow_cfg.py  <path to your CMSSW src directory>  <path to your output  reference directory >  -n 1 -q workday -p /afs/cern.ch/user/<first letter>/<username>/private/x509up_<user proxy>

./cmsCondorData.py run_steamflow_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/dz_Checks/Rates/CMSSW_15_0_10/src/ /eos/cms/store/group/phys_egamma/ssaumya/dz_Checks/Rates/Reference/ -n 1 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<999999>

# submit jobs
./sub_total.jobb

# Repeat the same for target
```

### Rate calculation

#### Create and submit counting jobs

Make necessary changes in the `config_makeCondorJobsData.py` (json file, input file directory, cmssw location), create and submit jobs:

```
python3 config_makeCondorJobsData.py
/sub_total.jobb
```

#### Merging and Scaling

To get the correct rates, you need to specify the correct `input lumi`, `target lumi` and `hlt_prescale`. 
To make things easier, you can input the following numbers directly in the `config_mergeOutputsData.py`
```
python3 config_mergeOutputsData.py
```

Output csv files containing the rates will be produced in the Results/Data subdirectory .
