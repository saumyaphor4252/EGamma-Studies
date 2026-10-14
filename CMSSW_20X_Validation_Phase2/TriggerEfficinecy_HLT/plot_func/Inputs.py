import sys
import ROOT
sys.dont_write_bytecode = True
from filter_configs import FILTERS, get_filters_for_path, get_available_paths
eosDir  ="/afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade_PR42850/CMSSW_13_1_0/src/EGamma-Workflow/plot_func/"

#---------------
# Plotting 
#---------------
outPlotDir  = "%s/%s"%(eosDir, "plots")
#For plotting efficiency
forOverlay = {}
forOverlay = {
    "13_1_X": ROOT.TFile.Open("/eos/cms/store/group/phys_egamma/ssaumya/Phase2_Inefficiency/Upgrade_PR42850/CMSSW_13_1_0/tnpNtupler.root"),
    "20_0_X": ROOT.TFile.Open("/eos/cms/store/group/phys_egamma/ssaumya/Upgrade_PR42850/CMSSW_20_0_0/tnpNtupler_Eff.root"),    
}

forRatio = ["13_1_X","20_0_X"]
#forRatio = ["CMSSW_15_1_0_pre3","CMSSW_15_1_0_pre4"]
#forRatio.append(["Phase2", "L1"])
#forRatio.append(["HLT_Ele30_WPTight_Gsf/EGamma_Run2023C", "HLT_Ele32_WPTight_Gsf/EGamma_Run2023C"])

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
