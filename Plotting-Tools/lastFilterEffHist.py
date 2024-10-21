#!/usr/bin/env python

#RUN it like this
#python3 filename.py  inputFile.root   -o=outFile.root 

from array import array
import re
import argparse
import sys
import math
from DataFormats.FWLite import Events, Handle
import ROOT
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
import json
import FWCore.ParameterSet.Config as cms
from CondCore.CondDB.CondDB_cfi import *
from PhysicsTools.PythonAnalysis import *
import time

def getListFilterPassedObj(filterName,hltsevt):
        eg_trig_objs = []
        #get a list of trigger objects that passed a given filter
        filterIndex = getFilterIndex(hltsevt,filterName)
#        print(f"In fn getListFilterPassedObj {hltsevt.sizeFilters()}")
        if (filterIndex < hltsevt.sizeFilters() ):
#                print("I m in if condition of L24")
                for filterKey in hltsevt.filterKeys(filterIndex):
                        obj = hltsevt.getObjects()[filterKey]
                        eg_trig_objs.append(obj)
        return eg_trig_objs


#from https://github.com/cms-egamma/EgammaDAS2020/blob/solutions/test/egFWLiteExercise2a.py
def match_trig_objs(eta,phi,trig_objs,max_dr=0.1):    
    max_dr2 = max_dr*max_dr
    matched_objs = [obj for obj in trig_objs if ROOT.reco.deltaR2(eta,phi,obj.eta(),obj.phi()) < max_dr2]
    return matched_objs


#from https://github.com/Sam-Harper/usercode/blob/100XNtup/SHNtupliser/test/checkTrigsAOD.py
def getFilterIndex(trigEvt,filterName):
    for index in range(0,trigEvt.sizeFilters()):
#        print(f"filterName {filterName} is being compared to {trigEvt.filterLabel(index)}")
#        print(type(trigEvt.filterLabel(index)))
        if filterName==trigEvt.filterLabel(index):
                #print 'filtername found' 
                return index
    return trigEvt.sizeFilters()


def get_genparts(genparts,pid=11,antipart=True,status=1):
    """                               
    returns a list of the gen particles matching the given criteria from hard process                                                                                                 
    might not work for all generators as depends on isHardProcess()                                                                                                                 
    """
    selected = []
    if genparts==None:
        return selected

    for part in genparts:
        pdg_id = part.pdgId()
        if pdg_id == pid or (antipart and abs(pdg_id) == abs(pid)):
            if part.isHardProcess():
                if status == 1:
                    selected.append(part)
    return selected

def match_to_gen(eta,phi,genparts,pid=11,antipart=True,max_dr=0.1,status=1):
    """ 
    Matches an eta,phi to gen level particle from the hard process                                                                                                                  
    might not work for all generaters as depends on isHardProcess()                                                                                                                  
    """
    best_match = None
    best_dr2 = max_dr*max_dr
    best_pt = -1
    selected_parts = get_genparts(genparts,pid,antipart,status)
    for part in selected_parts:
        dr2 = ROOT.reco.deltaR2(eta,phi,part.eta(),part.phi())
        if dr2 < best_dr2:
            best_match = part
            best_dr2 = dr2
            best_pt=part.pt()
    return best_match,best_dr2,best_pt

def getFilters(cmsPath):
    filts = []
    for fil in cmsPath.split(",")[0].split("+"):
        if "Filter" in fil:
            filts.append(fil.replace("process.", ""))
    return filts

if __name__ == "__main__":

    oldargv = sys.argv[:]
    sys.argv = [ '-b-' ]
    sys.argv = oldargv
    ROOT.gSystem.Load("libFWCoreFWLite.so");
    ROOT.gSystem.Load("libDataFormatsFWLite.so");
    ROOT.FWLiteEnabler.enable()

    parser = argparse.ArgumentParser(description='example e/gamma HLT analyser')
    parser.add_argument('in_filename',nargs="+",help='input filename')
    parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")

    args = parser.parse_args()

    ele_handle, ele_label = Handle("vector<trigger::EgammaObject>"), "hltEgammaHLTExtra"
    #ele_handle, ele_label = Handle("std::vector<trigger::EgammaObject>"), "hltEgammaHLTExtra:Unseeded"
    hlt_handle, hlt_label = Handle("edm::TriggerResults"), "TriggerResults::HLTX"
    hltevt_handle, hltevt_label = Handle("trigger::TriggerEvent"), "hltTriggerSummaryAOD::HLTX"
    gen_handle, gen_label = Handle("vector<reco::GenParticle>"), "genParticles"

    to_remove=[]
    print(args.in_filename)
    for file in args.in_filename:
        print(file)
        file_temp = ROOT.TFile(file)
        if ( file_temp.IsZombie() ) :
            to_remove.append(file)

    new_list = [x for x in args.in_filename if x not in to_remove]

    events = Events(new_list)

    #process.HLT_Ele32_WPTight_Unseeded = cms.Path(process.HLTBeginSequence+process.hltPreEle32WPTightUnseeded+process.HLTEle32WPTightUnseededSequence+process.HLTEndSequence)
    HLTEle32WPTightGsfSequence = "cms.Sequence(HLTDoFullUnpackingEgammaEcalSequence+HLTPFClusteringForEgamma+hltEgammaCandidates+hltEGL1SingleEGOrFilter+hltEG32L1SingleEGOrEtFilter+hltEgammaClusterShape+hltEle32WPTightClusterShapeFilter+HLTDoLocalHcalSequence+HLTFastJetForEgamma+hltEgammaHoverE+hltEle32WPTightHEFilter+hltEgammaEcalPFClusterIso+hltEle32WPTightEcalIsoFilter+HLTPFHcalClustering+hltEgammaHcalPFClusterIso+hltEle32WPTightHcalIsoFilter+HLTElePixelMatchSequence+hltEle32WPTightPixelMatchFilter+hltEle32WPTightPMS2Filter+HLTGsfElectronSequence+hltEle32WPTightGsfOneOEMinusOneOPFilter+hltEle32WPTightGsfMissingHitsFilter+hltEle32WPTightGsfDetaFilter+hltEle32WPTightGsfDphiFilter+HLTTrackReconstructionForIsoElectronIter02+hltEgammaEleGsfTrackIso+hltEle32WPTightGsfTrackIsoFilter"
#HLTEle32WPTightL1SeededSequence = "cms.Sequence(process.HLTL1Sequence+process.hltEGL1SeedsForSingleEleIsolatedFilter+process.HLTDoFullUnpackingEgammaEcalL1SeededSequence+process.HLTPFClusteringForEgammaL1Seeded+process.HLTHgcalTiclPFClusteringForEgammaL1Seeded+process.hltEgammaCandidatesWrapperL1Seeded+process.hltEG32EtL1SeededFilter+process.hltEle32WPTightClusterShapeL1SeededFilter+process.hltEle32WPTightClusterShapeSigmavvL1SeededFilter+process.hltEle32WPTightClusterShapeSigmawwL1SeededFilter+process.hltEle32WPTightHgcalHEL1SeededFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEle32WPTightHEL1SeededFilter+process.hltEle32WPTightEcalIsoL1SeededFilter+process.hltEle32WPTightHgcalIsoL1SeededFilter+process.HLTPFHcalClusteringForEgamma+process.hltEle32WPTightHcalIsoL1SeededFilter+process.HLTElePixelMatchL1SeededSequence+process.hltEle32WPTightPixelMatchL1SeededFilter+process.hltEle32WPTightPMS2L1SeededFilter+process.HLTGsfElectronL1SeededSequence+process.hltEle32WPTightGsfOneOEMinusOneOPL1SeededFilter+process.hltEle32WPTightGsfDetaL1SeededFilter+process.hltEle32WPTightGsfDphiL1SeededFilter+process.hltEle32WPTightBestGsfNLayerITL1SeededFilter+process.hltEle32WPTightBestGsfChi2L1SeededFilter+process.hltEle32WPTightGsfTrackIsoFromL1TracksL1SeededFilter+process.HLTTrackingV61Sequence+process.hltEle32WPTightGsfTrackIsoL1SeededFilter, process.HLTEle32WPTightL1SeededTaski)"

    filt32 = getFilters(HLTEle32WPTightGsfSequence)
    #filt32 = getFilters(HLTEle32WPTightL1SeededSequence)
    #filt32.append("l1tTkIsoEleSingle28Filter")
    #filt32 = ['hltEG32EtUnseededFilter']
    ptBins  = array('d', [5,10,15,20,22,26,28,30,32,34,36,38,40,45,50,60,80,100,150,250,500])
    #ptBins  = array('d', [5,10,15,20,22,26,28,30,32,34,36,38,40,45,50,60,80,100,150,250,500])
    etaBins = array('d', [-2.5,-2.4,-2.3,-2.2,-2.1,-2.0,-1.9,-1.8,-1.7,-1.56,-1.44,-1.3,-1.2,-1.1,-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.44,1.56,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5])
    phiBins = array('d', [-3.32,-2.97,-2.62,-2.27,-1.92,-1.57,-1.22,-0.87,-0.52,-0.18,0.18,0.52,0.87,1.22,1.57,1.92,2.27,2.62,2.97,3.32])
    den_ele_eta         = ROOT.TH1D("den_ele_eta", "#eta",len(etaBins)-1, etaBins)
    den_ele_pt_EB       = ROOT.TH1D("den_ele_pt_EB","pT", len(ptBins)-1,  ptBins)
    den_ele_pt_EE       = ROOT.TH1D("den_ele_pt_EE","pT", len(ptBins)-1,  ptBins)
    den_ele_pt          = ROOT.TH1D("den_ele_pt","pT", len(ptBins)-1,  ptBins)
    den_ele_phi         = ROOT.TH1D("den_ele_phi","#phi", len(phiBins)-1,  phiBins)

    # Dictionary to hold histograms for each filter
    num_ele_eta_histos = {}
    num_ele_pt_EB_histos = {}
    num_ele_pt_EE_histos = {}
    num_ele_pt_histos = {}
    num_ele_phi_histos = {}

    for f32 in filt32:
        #declare histograms
        num_ele_eta_histos[f32] = ROOT.TH1D(f"num_ele_eta_{f32}", "#eta", len(etaBins)-1, etaBins)
        num_ele_pt_EB_histos[f32] = ROOT.TH1D(f"num_ele_pt_{f32}_EB", "pT", len(ptBins)-1, ptBins)
        num_ele_pt_EE_histos[f32] = ROOT.TH1D(f"num_ele_pt_{f32}_EE", "pT", len(ptBins)-1, ptBins)
        num_ele_pt_histos[f32] = ROOT.TH1D(f"num_ele_pt_{f32}", "pT", len(ptBins)-1, ptBins)
        num_ele_phi_histos[f32] = ROOT.TH1D(f"num_ele_phi_{f32}", "#phi", len(phiBins)-1, phiBins)        

    percent_step = 1
    start_time = time.time() 
    total_entries = events.size()  
    for event_nr,event in enumerate(events):
        current_percent = (event_nr + 1) / total_entries * 100
        if current_percent % percent_step == 0:
           elapsed_time = time.time()-start_time
           est_finish = "n/a"
           if event_nr!=0 or elapsed_time==0:
                remaining = float(events.size()-event_nr)/event_nr*elapsed_time 
                est_finish = time.ctime(remaining+start_time+elapsed_time)
                print("{} / {} time: {:.1f}s, est finish {}".format(event_nr+1,events.size(),elapsed_time,est_finish))

        event.getByLabel(ele_label,ele_handle)
        event.getByLabel(hlt_label,hlt_handle)
        event.getByLabel(hltevt_label,hltevt_handle)
        event.getByLabel(gen_label,gen_handle)

        eles = ele_handle.product()
        hlts = hlt_handle.product()
        hltsevt = hltevt_handle.product()
        genobjs=gen_handle.product()

        # Print basic information about trigger filters
#        print(f"Number of filters: {hltsevt.sizeFilters()}")
#        for i in range(hltsevt.sizeFilters()):
#            print(f"Filter {i}: {hltsevt.filterLabel(i)}")

        trigdict=event.object().triggerNames(hlts).triggerNames()
        #Get trigger objects
        eg_trig_objs = {}
        for f32 in filt32:
            eg_trig_objs[f32] = getListFilterPassedObj(f32,hltsevt)
#            print(eg_trig_objs[f32])

        #Loop over egamma candiates
        for eg in eles:
            gen_match_ele = match_to_gen(eg.eta(),eg.phi(),gen_handle.product(),pid=11)[0]
            gen_pt = match_to_gen(eg.eta(),eg.phi(),gen_handle.product(),pid=11)[2]

            if (gen_match_ele):
                if (abs(eg.eta()) > 1.44 and abs(eg.eta()) < 1.56): 
                    continue 

                if (gen_pt<30.0): 
                    continue

                for ind, f32 in enumerate(filt32):
                    matched_objs = match_trig_objs(eg.eta(),eg.phi(),eg_trig_objs[f32])
                    nMatched = len(matched_objs)

                    if (abs(eg.eta()) <= 1.44): 
                        if ind==0: 
                            den_ele_pt_EB.Fill(gen_pt)
                        if nMatched> 0:
                            num_ele_pt_EB_histos[f32].Fill(gen_pt)

                    if (abs(eg.eta())>=1.56): 
                        if ind==0:
                            den_ele_pt_EE.Fill(gen_pt)
                        if nMatched> 0:
                            num_ele_pt_EE_histos[f32].Fill(gen_pt)

                    if ind==0:
                        den_ele_eta.Fill(eg.eta())
                        den_ele_phi.Fill(eg.phi())
                        den_ele_pt.Fill(eg.pt())

                    if nMatched> 0:
                        num_ele_eta_histos[f32].Fill(eg.eta())
                        num_ele_phi_histos[f32].Fill(eg.phi())
                        num_ele_pt_histos[f32].Fill(eg.pt())
#                       print("I am trigger matched and should be seen in the histogram")
                    
    output_file = TFile( args.output, 'recreate' )

    # Write the denominator histograms
    den_ele_eta.Write()
    den_ele_pt_EB.Write()
    den_ele_pt_EE.Write()
    den_ele_phi.Write()
    den_ele_pt.Write()

    # Write the numerator histograms
    for f32 in filt32:
        num_ele_eta_histos[f32].Write()
        num_ele_pt_EB_histos[f32].Write()
        num_ele_pt_EE_histos[f32].Write()
        num_ele_phi_histos[f32].Write()
        num_ele_pt_histos[f32].Write()

    output_file.Close()
