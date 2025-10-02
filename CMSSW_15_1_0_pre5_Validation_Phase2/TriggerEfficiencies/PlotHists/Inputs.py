import sys
import ROOT
sys.dont_write_bytecode = True
from filter_configs import FILTERS, get_filters_for_path, get_available_paths
eosDir  ="/afs/cern.ch/work/s/ssaumya/private/Egamma/Upgrade/Validation/CMSSW_15_1_0_pre1/src/cms-egamma-hlt/phase2/PlotHists/"

#---------------
# Plotting 
#---------------
outPlotDir  = "%s/%s"%(eosDir, "plots")
#For plotting efficiency
forOverlay = {}
forOverlay = {
#    "CMSSW_15_1_0_pre3": ROOT.TFile.Open("../../../outputFile_CMSSW_15_1_0_pre3.root"),
#    "CMSSW_15_1_0_pre4": ROOT.TFile.Open("../../../CMSSW_15_1_0_pre5_Validation/outputFile_ZpToEE_CMSSW_15_1_0_pre4.root"),
#    "CMSSW_15_1_0_pre5": ROOT.TFile.Open("../../../CMSSW_15_1_0_pre5_Validation/outputFile_ZpToEE_CMSSW_15_1_0_pre5.root"),
    "CMSSW_15_1_0_pre4": ROOT.TFile.Open("../../../CMSSW_15_1_0_pre5_Validation/outputFile_ZEE_CMSSW_15_1_0_pre4.root"),
    "CMSSW_15_1_0_pre5": ROOT.TFile.Open("../../../CMSSW_15_1_0_pre5_Validation/outputFile_ZEE_CMSSW_15_1_0_pre5.root"),    
#    "CMSSW_15_1_0_pre3": ROOT.TFile.Open("../../../outputFile_CMSSW_15_1_0_pre3.root"), 
}

forRatio = ["CMSSW_15_1_0_pre4","CMSSW_15_1_0_pre5"]
#For Ratio: Reference first: target second
#forRatio = ["CMSSW_15_1_0_pre3","CMSSW_15_1_0_pre4"]
#forRatio.append(["Phase2", "L1"])
#forRatio.append(["EGamma0_Run2023C", "EGamma1_Run2023C"])
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
