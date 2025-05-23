## Rates Recipe

### Relevent Links: 
- https://twiki.cern.ch/twiki/bin/viewauth/CMS/SteamHLTRatesCalculation#Rate_calculation_AN1

### STEAM Git repo:
- https://github.com/cms-steam/SteamRatesEdmWorkflow/tree/master


#### Set up
```
# CMSSW set-up
cmsrel CMSSW_15_0_1; cd CMSSW_15_0_1/src; cmsenv
git cms-merge-topic cms-tsg-storm:devel_customizeHLTfor2025Studies_from_CMSSW_15_0_3 
scram b -j 10

# Clone Rates caluculation set-up
git clone https://github.com/sanuvarghese/SteamRatesEdmWorkflow.git
cd SteamRatesEdmWorkflow/Prod/
scram b -j 10

# hltGetConfiguration: get desired menu
hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V79 --full --offline --no-output --data --process MYHLT --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --customise HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu,HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2025Studies --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v13,HLT_Ele32_WPTight_Gsf_v27,HLT_Ele115_CaloIdVT_GsfTrkIdT_v27,HLT_Ele135_CaloIdVT_GsfTrkIdT_v20,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31,HLT_DoubleEle33_CaloIdL_MW_v30,HLTriggerFinalPath > hlt_Reference.py

edmConfigDump hlt_Reference.py > hlt_Reference_DumpConfig.py

# proxy set-up
voms-proxy-init --voms cms --valid 168:00
cp /tmp/x509up_<user proxy> /afs/cern.ch/user/<letter>/<username>/private/

# create jobs
# ./cmsCondorData.py run_steamflow_cfg.py  <path to your CMSSW src directory>  <path to your output  reference directory >  -n 1 -q workday -p /afs/cern.ch/user/<first letter>/<username>/private/x509up_<user proxy>

./cmsCondorData.py run_steamflow_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/STEAM_23rdMay2025/CMSSW_15_0_5/src/SteamRatesEdmWorkflow/Prod/Reference/ /eos/cms/store/group/phys_egamma/ssaumya/STEAM_22ndMay_2025/RATES/Reference/ -n 1 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>

# submit jobs
./sub_total.jobb

# Repeat the same for target
hltGetConfiguration /users/ssaumya/Test/STEAM_23.05.2025/Target/V1 --full --offline --no-output --data --process MYHL
T --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --globaltag 150X_dataRun3_HLT_v1 --max-events 100 --customise HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2024L1TMenu,HLTrigger/Configuration/customizeHLTfor2025Studies.customizeHLTfor2025Studies --path HLTriggerFirstPath,HLT_Ele30_WPTight_Gsf_v13,HLT_Ele32_WPTight_Gsf_v27,HLT_Ele115_CaloIdVT_GsfTrkIdT_v27,HLT_Ele135_CaloIdVT_GsfTrkIdT_v20,HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31,HLT_DoubleEle33_CaloIdL_MW_v30,HLTriggerFinalPath > hlt_Target_v2.py
./cmsCondorData.py run_steamflow_cfg.py /afs/cern.ch/work/s/ssaumya/private/Egamma/STEAM_23rdMay2025/CMSSW_15_0_5/src/SteamRatesEdmWorkflow/Prod/Target_v2/ /eos/cms/store/group/phys_egamma/ssaumya/STEAM_22ndMay_2025/RATES/Target_v2/ -n 1 -q workday -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb
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
