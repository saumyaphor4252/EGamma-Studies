## Relevant Links and information
- CMSSW: `CMSSW_16_0_2_patch1`
- Menu used: 
	- Target: `/users/STORM/CMSSW_16_0_0/etc/testFromPycustomizeHLTfor49436/V1`
	- Reference: `/users/STORM/CMSSW_16_0_0/etc/testFromPy/V1`
- Dataset used: `/EGamma1/Run2025G-ZElectron-PromptReco-v1/RAW-RECO`

- HLT GT: `160X_dataRun3_HLT_v1`

### Rucio rules for dataset if not available on disk
```
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -voms cms
export RUCIO_ACCOUNT=`whoami`
rucio add-rule cms:/EGamma0/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#38515497-07d6-42b4-8a41-12f97f79d8a4  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
d7306e9e2f64474e920c6266296acec2
rucio add-rule cms:/EGamma1/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#92d60088-708a-4420-825d-9f473634415f  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
4a4019c0231443169dbb68392ff04c2b
rucio add-rule cms:/EGamma1/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#a4be8f17-8c3d-47bc-aaf3-001792f8bbb5  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
5a0c4876036b46f6bfb419a35e431a21
rucio add-rule cms:/EGamma2/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#083aa652-9bf1-4228-a646-36b4518765d6  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
58f8ce4685d94a69856433d9262a56ec
rucio add-rule cms:/EGamma2/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#4e4b957f-a440-4fd1-97c4-dc00ec2262ff  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
8254adb1bf7b459385a972507d59bcbf
rucio add-rule cms:/EGamma2/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#8589fe86-3d04-4cb2-b883-9ca6ccf0a97a  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
3bc71e0953794ce1a3304b013cbd0dc9
rucio add-rule cms:/EGamma2/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#ed63ba90-d1c7-459b-932a-a83a865a193f  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
83cc68a1710543f29cdc1dc577dc303d
rucio add-rule cms:/EGamma3/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#143946ac-5bd4-4483-bf44-92d76b9fefc9  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
546f587c1db0432c92021cf4a2d31d91
rucio add-rule cms:/EGamma3/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#2e4b8435-50e2-444d-8f75-cd4e8a9fdb5a  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
e1ba26a82339456384c7821fa2e215db
rucio add-rule cms:/EGamma4/Run2026B-ZElectron-PromptReco-v1/RAW-RECO#934c3572-d7bf-4a56-baa0-92204e9b6eb2  1 T2_CH_CERN  --lifetime 864000 --activity "User AutoApprove" --ask-approval --comment "For important 2026 EGM-HLT studies"
31a8939f92564c18bd9621f41f76111a
```

### CMSSW set-up
```
cmsrel CMSSW_16_0_5; cd CMSSW_16_0_5/src/; cmsenv; 
git cms-addpkg HLTrigger/Configuration
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1230pre6 
scram b -j 10
```

### Run the HLT step
- Reference
```
### hltGetConfiguration
hltGetConfiguration /users/STORM/CMSSW_16_0_0/etc/testFromPy/V1 --output minimal --data --process MYHLT --type GRun --globaltag 160X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2026 --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --input file:/eos/cms/store/data/Run2026B/EGamma4/RAW-RECO/ZElectron-PromptReco-v1/000/402/101/00000/60ccf70e-8338-42e9-8c15-c4a7fa3bc6e9.root --l1-emulator --l1 L1Menu_Collisions2026_v1_1_0_xml > hlt_Reference_Customized.py

edmConfigDump hlt_Reference_Customized.py >  hlt_Reference_Customized_ConfigDump.py

cmsRun hlt_Reference_Customized_ConfigDump.py > Log.out 1>&2
```
- Target
```
### hltGetConfiguration
hltGetConfiguration /users/STORM/CMSSW_16_0_0/etc/testFromPycustomizeHLTfor49436/V1 --output minimal --data --process MYHLT --type GRun --globaltag 160X_dataRun3_HLT_v1 --max-events 100 --unprescale --eras Run3_2026 --customise HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --input file:/eos/cms/store/data/Run2026B/EGamma4/RAW-RECO/ZElectron-PromptReco-v1/000/402/101/00000/60ccf70e-8338-42e9-8c15-c4a7fa3bc6e9.root --l1-emulator --l1 L1Menu_Collisions2026_v1_1_0_xml > hlt_Target_Customized.py

edmConfigDump hlt_Target_Customized.py >  hlt_Target_Customized_ConfigDump.py

cmsRun hlt_Target_Customized_ConfigDump.py > Log.out 1>&2
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
## L49-L63 for configuration modification of the HLT step, L53-L58 for input source, L73 for events, L76-77 and L125-128 for output file name
# -n 10 --> 10 files per job
python3 cmsCondor.py hlt_Reference_Customized_ConfigDump.py /afs/cern.ch/work/s/ssaumya/private/Egamma/CMSHLT-3764/CMSSW_16_0_5/src/ /eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3746/HLTstep_RootFiles_Reference -n 10 -q tomorrow -p /afs/cern.ch/user/s/ssaumya/private/x509up_u<99999>
./sub_total.jobb
```

### Make the ntuples
```
git clone ssh://git@gitlab.cern.ch:7999/sharper/HLTAnalyserPy.git Analysis/HLTAnalyserPy

# Remove some non-working dependencies for now
rm -rf Analysis/HLTAnalyserPy/interface/RateFuncs.h
rm -rf Analysis/HLTAnalyserPy/src/RateFuncs.cc 
rm -rf Analysis/HLTAnalyserPy/interface/QCDWeightCalc.h
rm -rf Analysis/HLTAnalyserPy/src/QCDWeightCalc.cc
vi Analysis/HLTAnalyserPy/src/classes.h
vi Analysis/HLTAnalyserPy/src/classes_def.xml
scram b -j 10

python3 Analysis/HLTAnalyserPy/test/ntup/makeRun3Ntup.py -o ntup_Reference.root eos/cms/store/group/phys_egamma/ssaumya/CMSHLT-3746/HLTstep_RootFiles_Reference/*.root
```

### Plotting
```
python3 plot_Run3_EGMHLT_variables.py \
  ntup_Reference.root ntup_Target.root \
  -o comparison \
  -l "Reference" "Target" \
  -t egHLTRun3Tree
```
