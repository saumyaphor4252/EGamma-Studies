import sys
import ROOT
sys.dont_write_bytecode = True
from filter_configs import FILTERS, get_filters_for_path, get_available_paths
eosDir  ="/afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/InefficiencyChecls/3rdFeb_2026/Efficiencies/CMSSW_16_0_0_pre4/src/PlotHists/"

#---------------
# Plotting 
#---------------
outPlotDir  = "%s/%s"%(eosDir, "plots")
#For plotting efficiency
forOverlay = {}
forOverlay = {
    "Reference": ROOT.TFile.Open("../Ntuple_Reference.root"),
    "Target": ROOT.TFile.Open("../Ntuple_Target_v2.root"),
}

#forRatio = ["CMSSW_15_1_0_pre2","CMSSW_15_1_0_pre3"]
forRatio = ["Reference", "Target"]

filters = FILTERS
# Use list comprehensions for better performance and readability

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
