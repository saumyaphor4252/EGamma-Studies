import sys
import ROOT
from pathlib import Path
from filter_configs import FILTERS, get_filters_for_path, get_available_paths
sys.dont_write_bytecode = True

# Use Path for more robust path handling
eosDir = Path("/afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/Validation/CMSSW_15_1_0_pre1/src/PlotHists/")
outPlotDir = eosDir / "plots"

# For plotting efficiency
forOverlay = {
    "CMSSW_15_1_0_pre1": ROOT.TFile.Open("../outputFile_CMSSW_15_1_0_pre1.root"),
    "CMSSW_15_1_0_pre2": ROOT.TFile.Open("../outputFile_CMSSW_15_1_0_pre2.root"),
    "CMSSW_15_1_0_pre3": ROOT.TFile.Open("../outputFile_CMSSW_15_1_0_pre3.root")
    # Alternative path commented out
    # "Phase2": ROOT.TFile.Open(str(eosDir / "s3Hist/RelValTTbar_14TeV_Phase2Setup/Phase2_HLT_All.root"))
}

forRatio = []
forRatio.append(["CMSSW_15_1_0_pre1","CMSSW_15_1_0_pre2","CMSSW_15_1_0_pre3"])
#forRatio.append(["HLT_Ele30_WPTight_Gsf/EGamma_Run2023C", "HLT_Ele32_WPTight_Gsf/EGamma_Run2023C"])
# Use a set for faster lookups if needed
forRatio = set()
# forRatio.add(("Phase2", "L1"))
# forRatio.add(("HLT_Ele30_WPTight_Gsf/EGamma_Run2023C", "HLT_Ele32_WPTight_Gsf/EGamma_Run2023C"))

# Use the imported filter configurations
filters = FILTERS

# You can now use the helper functions if needed
# Example:
# path_filters = get_filters_for_path("HLTEle26WP70L1Seeded")
# available_paths = get_available_paths()

# Use list comprehensions for better performance and readability
numPtEE = [f"{trigger_name}_num_ele_pt_{filter_name}_EE" 
          for trigger_name, filter_list in filters.items() 
          for filter_name in filter_list]

numPtEB = [f"{trigger_name}_num_ele_pt_{filter_name}_EB" 
          for trigger_name, filter_list in filters.items() 
          for filter_name in filter_list]

numPt = [f"{trigger_name}_num_ele_pt_{filter_name}" 
        for trigger_name, filter_list in filters.items() 
        for filter_name in filter_list]

# Use list comprehensions for eta and phi
numEta = [f"{trigger_name}_num_ele_eta_{filter_name}" 
         for trigger_name, filter_list in filters.items() 
         for filter_name in filter_list]

numPhi = [f"{trigger_name}_num_ele_phi_{filter_name}" 
         for trigger_name, filter_list in filters.items() 
         for filter_name in filter_list]
