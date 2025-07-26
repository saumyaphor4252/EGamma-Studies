### Setup 

```
cmssw-el8
cmsrel CMSSW_15_0_10; cd CMSSW_15_0_10/src; cmsenv

hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V101 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Reference.py

hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_60/V1 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Target_60.py

hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_65/V1 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Target_65.py

hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_70/V1 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Target_70.py

hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/PMS2_Update/Target_75/V1 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Target_75.py

git clone ssh://git@gitlab.cern.ch:7999/cms-tsg/steam/timing.git
python3 -m venv venv
source venv/bin/activate
pip3 install -r timing/requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD/timing
python3 timing/submit.py hlt_Reference.py --tag _Reference
python3 timing/job_manager.py

python3 timing/submit.py hlt_Target_60.py --tag _Target_60
python3 timing/job_manager.py

python3 timing/submit.py hlt_Target_65.py --tag _Target_65
python3 timing/job_manager.py

python3 timing/submit.py hlt_Target_70.py --tag _Target_70
python3 timing/job_manager.py

python3 timing/submit.py hlt_Target_75.py --tag _Target_75
python3 timing/job_manager.py

deactivate
```
