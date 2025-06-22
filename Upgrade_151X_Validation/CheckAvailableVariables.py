#!/usr/bin/env python

import ROOT
from DataFormats.FWLite import Events, Handle

# Input MiniAOD file
input_file = "file:/eos/cms/store/relval/CMSSW_15_1_0_pre3/RelValZpToEE_m6000_14TeV/MINIAODSIM/PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1/2590000/47cdaeb2-d0c5-48cb-91d9-546ce22d9bea.root"  # Change this to your file path

# Create the events object
events = Events(input_file)

# Define handle and label for slimmedElectrons
ele_handle = Handle("std::vector<pat::Electron>")
ele_label = ("slimmedElectrons", "", "RECO")  # Usually RECO, might be PAT

# Prepare histogram
hist = ROOT.TH1F("electron_eta", "Electron #eta;#eta;Events", 50, -3.0, 3.0)

# Loop over events
for event in events:
    event.getByLabel(ele_label, ele_handle)
    electrons = ele_handle.product()

    for ele in electrons:
        print(dir(ele))
        break  # Only show for the first PF candidate
    break  # Only do this for the first event
