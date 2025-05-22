#!/usr/bin/env python3

import ROOT
import os
import sys

# Ensure ROOT doesn't pop up any GUI
ROOT.gROOT.SetBatch(True)

# Check for input directory
if len(sys.argv) < 2:
    print("Usage: python check_root_zombie.py <directory_path>")
    sys.exit(1)

root_dir = sys.argv[1]

if not os.path.isdir(root_dir):
    print(f"Error: Directory '{root_dir}' does not exist.")
    sys.exit(1)

# Walk through the directory and check all .root files
for dirpath, _, filenames in os.walk(root_dir):
    for fname in filenames:
        if fname.endswith(".root"):
            fpath = os.path.join(dirpath, fname)

            # Try to open the ROOT file
            f = ROOT.TFile.Open(fpath)
            if not f or f.IsZombie():
                print(f"CORRUPT: {fpath}")
            else:
                print(f"OK:      {fpath}")
            if f:
                f.Close()

