import sys
import ROOT
sys.dont_write_bytecode = True
eosDir  ="/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/CMSSW_13_0_10/src/cms-egamma-hlt/phase2/PlotHists"

def getFilters(cmsPath):
    filts = []
    for fil in cmsPath.split(",")[0].split("+"):
        if "Filter" in fil:
            filts.append(fil.replace("process.", ""))
    return filts

#---------------
# Plotting 
#---------------
outPlotDir  = "%s/%s"%(eosDir, "plots")
#For plotting efficiency
forOverlay = {}
#forOverlay["2023postBPix"] =ROOT.TFile.Open("../output_file2023.root")
#forOverlay["Run3Winter2024"] =ROOT.TFile.Open("../output_file2024.root")
#forOverlay["2023postBPix"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test/Efficiency_Modified_2023_3million.root")
#forOverlay["Run3Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Modified_2024_3million.root")
forOverlay["2023postBPix"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test/Efficiency_Modified_2023_16102024.root")
forOverlay["Run3Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Modified_2024_16102024.root")
#forOverlay["2023postBPix"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test/50000Events/Efficiency_Modified_2023_07082024.root")
#forOverlay["Run3Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/400000Events/Efficiency_Modified_2024_07082024.root")

#For filters
#forOverlay["2023postBPix"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/CMSSW_13_0_10/src/cms-egamma-hlt/phase2/Efficiency_Modified_2023WithPt.root")
#forOverlay["Run3Winter2024"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/FilterPlots_for2024/CMSSW_13_3_3/src/cms-egamma-hlt/phase2/Efficiency_Modified_2024WithPt.root")

#forOverlay["No Change 133X"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_NoChange.root")
#forOverlay["HcalSiPM"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalSiPM.root")
#forOverlay["HcalZS"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalZS.root")
#forOverlay["HcalResponseCorrs"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalResponse.root")
#forOverlay["HcalSiPM"] =ROOT.TFile.Open("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Test_133X_with_130XGT_HcalSiPM.root")

forRatio = []
#forRatio.append(["2023postBPix", "Run3Winter2024"])
forRatio.append(["Run3Winter2024", "2023postBPix"])
#forRatio.append(["2024", "NoChange133X"])
#forRatio.append(["HLT_Ele30_WPTight_Gsf/EGamma_Run2023C", "HLT_Ele32_WPTight_Gsf/EGamma_Run2023C"])


filters = []
HLTEle32WPTightGsfSequence = "cms.Sequence(HLTDoFullUnpackingEgammaEcalSequence+HLTPFClusteringForEgamma+hltEgammaCandidates+hltEGL1SingleEGOrFilter+hltEG32L1SingleEGOrEtFilter+hltEgammaClusterShape+hltEle32WPTightClusterShapeFilter+HLTDoLocalHcalSequence+HLTFastJetForEgamma+hltEgammaHoverE+hltEle32WPTightHEFilter+hltEgammaEcalPFClusterIso+hltEle32WPTightEcalIsoFilter+HLTPFHcalClustering+hltEgammaHcalPFClusterIso+hltEle32WPTightHcalIsoFilter+HLTElePixelMatchSequence+hltEle32WPTightPixelMatchFilter+hltEle32WPTightPMS2Filter+HLTGsfElectronSequence+hltEle32WPTightGsfOneOEMinusOneOPFilter+hltEle32WPTightGsfMissingHitsFilter+hltEle32WPTightGsfDetaFilter+hltEle32WPTightGsfDphiFilter+HLTTrackReconstructionForIsoElectronIter02+hltEgammaEleGsfTrackIso+hltEle32WPTightGsfTrackIsoFilter"

#filters = ['hltEGL1SeedsForSingleEleIsolatedFilter', 'hltEG32EtUnseededFilter', 'hltEle32WPTightClusterShapeUnseededFilter', 'hltEle32WPTightClusterShapeSigmavvUnseededFilter', 'hltEle32WPTightClusterShapeSigmawwUnseededFilter', 'hltEle32WPTightHgcalHEUnseededFilter', 'hltEle32WPTightHEUnseededFilter', 'hltEle32WPTightEcalIsoUnseededFilter', 'hltEle32WPTightHgcalIsoUnseededFilter', 'hltEle32WPTightHcalIsoUnseededFilter', 'hltEle32WPTightPixelMatchUnseededFilter', 'hltEle32WPTightPMS2UnseededFilter', 'hltEle32WPTightGsfOneOEMinusOneOPUnseededFilter', 'hltEle32WPTightGsfDetaUnseededFilter', 'hltEle32WPTightGsfDphiUnseededFilter', 'hltEle32WPTightBestGsfNLayerITUnseededFilter', 'hltEle32WPTightBestGsfChi2UnseededFilter', 'hltEle32WPTightGsfTrackIsoFromL1TracksUnseededFilter', 'hltEle32WPTightGsfTrackIsoUnseededFilter']
#filters = ['hltEGL1SeedsForSingleEleIsolatedFilter', 'hltEG32EtL1SeededFilter', 'hltEle32WPTightClusterShapeL1SeededFilter', 'hltEle32WPTightClusterShapeSigmavvL1SeededFilter', 'hltEle32WPTightClusterShapeSigmawwL1SeededFilter', 'hltEle32WPTightHgcalHEL1SeededFilter', 'hltEle32WPTightHEL1SeededFilter', 'hltEle32WPTightEcalIsoL1SeededFilter', 'hltEle32WPTightHgcalIsoL1SeededFilter', 'hltEle32WPTightHcalIsoL1SeededFilter', 'hltEle32WPTightPixelMatchL1SeededFilter', 'hltEle32WPTightPMS2L1SeededFilter', 'hltEle32WPTightGsfOneOEMinusOneOPL1SeededFilter', 'hltEle32WPTightGsfDetaL1SeededFilter', 'hltEle32WPTightGsfDphiL1SeededFilter', 'hltEle32WPTightBestGsfNLayerITL1SeededFilter', 'hltEle32WPTightBestGsfChi2L1SeededFilter', 'hltEle32WPTightGsfTrackIsoFromL1TracksL1SeededFilter', 'hltEle32WPTightGsfTrackIsoL1SeededFilter'] 

filters = getFilters(HLTEle32WPTightGsfSequence)
print("Filters: ",filters)
#filters.append('l1tTkEmSingle51Filter')
#filters.append('l1tTkEleSingle36Filter')
#filters.append('l1tTkIsoEleSingle28Filter')

numPtEE = []
numPtEB = []
#for f in filters:
#    numPtEE.append("num_ele_pt_%s_EE"%f)
#    numPtEB.append("num_ele_pt_%s_EB"%f)
numEta = []
numPhi = []
#for f in filters:
#    numEta.append("num_ele_eta_%s"%f)


numPtEE.append("num_ele_pt_EE")
#List = ["num_ele_pt_EB", "num_ele_pt_EB1", "num_ele_pt_EB2", "num_ele_pt_EE", "num_ele_pt_EE1", "num_ele_pt_EE2", "num_ele_eta", "num_ele_phi"]
