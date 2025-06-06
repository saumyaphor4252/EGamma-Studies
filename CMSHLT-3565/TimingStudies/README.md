### Setup 

```
cmssw-el8
cmsrel CMSSW_15_0_6_patch1; cd CMSSW_15_0_6_patch1/src; cmsenv

hltGetConfiguration /users/ssaumya/Test/dev/CMSSW_15_0_0/CMSHLT_3565/Test01/GRun/v1/V3 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun    --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Target.py

git clone ssh://git@gitlab.cern.ch:7999/cms-tsg/steam/timing.git
python3 -m venv venv
source venv/bin/activate
pip3 install -r timing/requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD/timing
python3 timing/submit.py hlt_Target.py --tag _Target
python3 timing/job_manager.py

hltGetConfiguration /dev/CMSSW_15_0_0/GRun/V79 --globaltag 150X_dataRun3_HLT_v1 --data --type GRun --prescale 2p0E34+ZeroBias+HLTPhysics --timing --output minimal > hlt_Reference.py

python3 timing/submit.py hlt_Reference.py --tag _Reference
python3 timing/job_manager.py

deactivate
```
