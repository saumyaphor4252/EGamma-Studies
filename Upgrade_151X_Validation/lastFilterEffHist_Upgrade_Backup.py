#!/usr/bin/env python

#RUN it like this
#python3 filename.py  inputFile.root   -o=outFile.root 

from array import array
import re
import argparse
import sys
import math
import logging
from typing import List, Dict, Any
from DataFormats.FWLite import Events, Handle
import ROOT
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, edm
import json
import FWCore.ParameterSet.Config as cms
from CondCore.CondDB.CondDB_cfi import *
from PhysicsTools.PythonAnalysis import *
import time

# Constants
EB_ETA_MAX = 1.44
EE_ETA_MIN = 1.56
MIN_GEN_PT = 30.0
MAX_DR = 0.1

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HistogramManager:
    def __init__(self, pt_bins: array, eta_bins: array, phi_bins: array):
        self.pt_bins = pt_bins
        self.eta_bins = eta_bins
        self.phi_bins = phi_bins
        self.histograms = {}
        
    def create_histograms(self, sequences: Dict[str, List[str]]) -> None:
        """Create all necessary histograms for the analysis.
        
        Args:
            sequences: Dictionary mapping sequence names to their filter lists
        """
        # Create denominator histograms for each sequence
        for sequence_name in sequences.keys():
            self.histograms[f'{sequence_name}_den_ele_eta_EB'] = ROOT.TH1D(f"{sequence_name}_den_ele_eta_EB", "#eta", len(self.eta_bins)-1, self.eta_bins)
            self.histograms[f'{sequence_name}_den_ele_eta_EE'] = ROOT.TH1D(f"{sequence_name}_den_ele_eta_EE", "#eta", len(self.eta_bins)-1, self.eta_bins)
            self.histograms[f'{sequence_name}_den_ele_eta'] = ROOT.TH1D(f"{sequence_name}_den_ele_eta", "#eta", len(self.eta_bins)-1, self.eTa_bins)
            self.histograms[f'{sequence_name}_den_ele_phi_EB'] = ROOT.TH1D(f"{sequence_name}_den_ele_phi_EB", "#phi", len(self.phi_bins)-1, self.phi_bins)
            self.histograms[f'{sequence_name}_den_ele_phi_EE'] = ROOT.TH1D(f"{sequence_name}_den_ele_phi_EE", "#phi", len(self.phi_bins)-1, self.phi_bins)
            self.histograms[f'{sequence_name}_den_ele_phi'] = ROOT.TH1D(f"{sequence_name}_den_ele_phi", "#phi", len(self.phi_bins)-1, self.phi_bins)
            self.histograms[f'{sequence_name}_den_ele_pt_EB'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt_EB", "pT", len(self.pt_bins)-1, self.pt_bins)
            self.histograms[f'{sequence_name}_den_ele_pt_EE'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt_EE", "pT", len(self.pt_bins)-1, self.pt_bins)
            self.histograms[f'{sequence_name}_den_ele_pt'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt", "pT", len(self.pt_bins)-1, self.pt_bins)
            
            # Create numerator histograms for each filter in this sequence
            for filter_name in sequences[sequence_name]:
                self.histograms[f'{sequence_name}_num_ele_eta_EB_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_eta_EB_{filter_name}", "#eta", len(self.eta_bins)-1, self.eta_bins)
                self.histograms[f'{sequence_name}_num_ele_eta_EE_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_eta_EE_{filter_name}", "#eta", len(self.eta_bins)-1, self.eta_bins)
                self.histograms[f'{sequence_name}_num_ele_eta_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_eta_{filter_name}", "#eta", len(self.eta_bins)-1, self.eta_bins)
                self.histograms[f'{sequence_name}_num_ele_phi_EB_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_phi_EB_{filter_name}", "#phi", len(self.phi_bins)-1, self.phi_bins)
                self.histograms[f'{sequence_name}_num_ele_phi_EE_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_phi_EE_{filter_name}", "#phi", len(self.phi_bins)-1, self.phi_bins)
                self.histograms[f'{sequence_name}_num_ele_phi_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_phi_{filter_name}", "#phi", len(self.phi_bins)-1, self.phi_bins)
                self.histograms[f'{sequence_name}_num_ele_pt_EB_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_EB_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)
                self.histograms[f'{sequence_name}_num_ele_pt_EE_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_EE_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)
                self.histograms[f'{sequence_name}_num_ele_pt_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)

    def write_histograms(self, output_file: TFile) -> None:
        """Write all histograms to the output file."""
        for hist in self.histograms.values():
            hist.Write()

def match_trig_objs(eta: float, phi: float, trig_objs: List[Any], max_dr: float = MAX_DR) -> List[Any]:    
    """Match trigger objects to a given eta,phi position.
    
    Args:
        eta: Eta coordinate of offline electron
        phi: Phi coordinate of offline electron
        trig_objs: List of trigger objects to match against
        max_dr: Maximum delta R for matching
        
    Returns:
        List of matched trigger objects
    """
    max_dr2 = max_dr * max_dr
    matched_objs = [obj for obj in trig_objs if ROOT.reco.deltaR2(eta, phi, obj.eta(), obj.phi()) < max_dr2]
    return matched_objs

def get_genparts(genparts: Any, pid: int = 11, antipart: bool = True, status: int = 1) -> List[Any]:
    """Get a list of gen particles matching the given criteria.
    
    Args:
        genparts: GenParticle collection
        pid: PDG ID to match
        antipart: Whether to include antiparticles
        status: Particle status to match
        
    Returns:
        List of matching gen particles
    """
    selected = []
    if genparts is None:
        return []
        
    for part in genparts:
        pdg_id = part.pdgId()
        if pdg_id == pid or (antipart and abs(pdg_id) == abs(pid)):
            if part.isHardProcess():
                if status == 1:
                    selected.append(part)
    return selected

def match_to_gen(eta: float, phi: float, genparts: Any, pid: int = 11, 
                antipart: bool = True, max_dr: float = MAX_DR, status: int = 1) -> tuple:
    """Match an eta,phi to gen level particle.
    
    Args:
        eta: Eta coordinate
        phi: Phi coordinate
        genparts: GenParticle collection
        pid: PDG ID to match
        antipart: Whether to include antiparticles
        max_dr: Maximum delta R for matching
        status: Particle status to match
        
    Returns:
        Tuple of (best_match, best_dr2, best_pt)
    """
    best_match = None
    best_dr2 = max_dr * max_dr
    best_pt = -1
    
    selected_parts = get_genparts(genparts, pid, antipart, status)
    for part in selected_parts:
        dr2 = ROOT.reco.deltaR2(eta, phi, part.eta(), part.phi())
        if dr2 < best_dr2:
            best_match = part
            best_dr2 = dr2
            best_pt = part.pt()
            
    return best_match, best_dr2, best_pt

def getFilters(cms_path: str) -> List[str]:
    """Extract filter names from a CMS path sequence.
    
    Args:
        cms_path: CMS path string or cms.Sequence object
        
    Returns:
        List of filter names
    """
    filts = []
    
    # Handle both string and cms.Sequence inputs
    if isinstance(cms_path, str):
        # Remove cms.Sequence wrapper if present
        seq_str = cms_path.replace("cms.Sequence(", "").replace(")", "")
        # Split by + and clean each module
        for module in seq_str.split("+"):
            module = module.strip()
            if "Filter" in module:
                # Remove all whitespace, process. prefix, and parentheses
                module = module.replace("process.", "").replace(" ", "").replace("(", "").replace(")", "")
                filts.append(module)
    else:
        # Handle cms.Sequence object
        # Convert sequence to string and clean it
        seq_str = str(cms_path)
        # Remove the cms.Sequence wrapper
        seq_str = seq_str.replace("cms.Sequence(", "").replace(")", "")
        # Split by + and clean each module
        for module in seq_str.split("+"):
            module = module.strip()
            if "Filter" in module:
                # Remove all whitespace, process. prefix, and parentheses
                module = module.replace("process.", "").replace(" ", "").replace("(", "").replace(")", "")
                filts.append(module)
    
    return filts

def process_events(events: Events, hist_manager: HistogramManager, sequences: Dict[str, List[str]], max_events: int = -1) -> None:
    """Process events and fill histograms for multiple sequences.
    
    Args:
        events: Events to process
        hist_manager: Histogram manager instance
        sequences: Dictionary mapping sequence names to their filter lists
        max_events: Maximum number of events to process (-1 for all events)
    """
    # Initialize handles
    ele_handle, ele_label = Handle("vector<pat::Electron>"), "slimmedElectrons"
    ele_HGC_handle, ele_HGC_label = Handle("vector<pat::Electron>"), "slimmedElectronsHGC"
    hlt_handle, hlt_label = Handle("edm::TriggerResults"), ("TriggerResults", "", "HLT")
    triggerObjects_handle, triggerObjects_label = Handle("vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
    gen_handle, gen_label = Handle("vector<reco::GenParticle>"), "prunedGenParticles"
    
    percent_step = 1
    start_time = time.time()
    total_entries = events.size() if max_events == -1 else min(events.size(), max_events)
    
    for event_nr, event in enumerate(events):
        if max_events != -1 and event_nr >= max_events:
            break
            
        # Progress reporting
        current_percent = (event_nr + 1) / total_entries * 100
        if current_percent % percent_step == 0:
            elapsed_time = time.time()-start_time
            est_finish = "n/a"
            if event_nr!=0 or elapsed_time==0:
                remaining = float(total_entries-event_nr)/event_nr*elapsed_time 
                est_finish = time.ctime(remaining+start_time+elapsed_time)
                print("{} / {} time: {:.1f}s, est finish {}".format(event_nr+1,total_entries,elapsed_time,est_finish))
        
        # Get event data
        try:
            event.getByLabel(ele_label, ele_handle)
            event.getByLabel(ele_HGC_label, ele_HGC_handle)
            event.getByLabel(hlt_label, hlt_handle)
            event.getByLabel(triggerObjects_label, triggerObjects_handle)
            event.getByLabel(gen_label, gen_handle)
        except Exception as e:
            logger.error(f"Error getting event data: {str(e)}")
            continue
            
        eles = ele_handle.product()
        eles_HGC = ele_HGC_handle.product()
        hlts = hlt_handle.product()
        trigger_objects = triggerObjects_handle.product()
        genobjs = gen_handle.product()
        
        # Get trigger names from the trigger results
        trigger_names = event.object().triggerNames(hlts)
        
        # Process each sequence
        for sequence_name, filter_names in sequences.items():
            # Process electrons
            for eg in eles:
                gen_match_ele, _, gen_pt = match_to_gen(eg.eta(), eg.phi(), genobjs, pid=11)
                
                if not gen_match_ele:
                    continue
                    
                # Skip transition region and low pt
                if (abs(eg.eta()) > EB_ETA_MAX and abs(eg.eta()) < EE_ETA_MIN) or gen_pt < MIN_GEN_PT:
                    continue
                
                # Process each filter in this sequence
                for ind, filter_name in enumerate(filter_names):
                    # Find trigger objects that passed this filter
                    matched_objs = []
                    for obj in trigger_objects:
                        # Unpack filter labels and path names
                        obj.unpackFilterLabels(event.object(), hlts)
                        obj.unpackPathNames(trigger_names)
                        
                        # Print debug info for first few objects
#                        if event_nr < 100 and ind == 0:
#                            print(f"\n🔍 Filter we're looking for: {filter_name}")
#                            # Convert bytes to strings for filter labels
#                            filter_labels = [label.decode('utf-8') if isinstance(label, bytes) else str(label) for label in obj.filterLabels()]
#                            print(f"   Filter Labels: {filter_labels}")
#                            print(f"   Path Names: {[path for path in obj.pathNames()]}")
                        
                        # Check if this object passed the filter
                        if obj.hasFilterLabel(filter_name):
                            print(f"🎯 Found object passing filter {filter_name}!")
                            matched_objs.append(obj)
                    
                    # Match trigger objects to electron
                    matched_objs = match_trig_objs(eg.eta(), eg.phi(), matched_objs)
                    n_matched = len(matched_objs)
                    
                    if n_matched > 0:
                        # Fill histograms based on eta region
                        if abs(eg.eta()) <= EB_ETA_MAX:
                            if ind == 1:
                                hist_manager.histograms[f'{sequence_name}_den_ele_pt_EB'].Fill(gen_pt)
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_EB_{filter_name}'].Fill(gen_pt)
                            
                        if abs(eg.eta()) >= EE_ETA_MIN:
                            if ind == 1:
                                hist_manager.histograms[f'{sequence_name}_den_ele_pt_EE'].Fill(gen_pt)
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_EE_{filter_name}'].Fill(gen_pt)
                            
                        if abs(eg.eta()) <= EB_ETA_MAX or abs(eg.eta()) >= EE_ETA_MIN:
                            if ind == 1:
                                hist_manager.histograms[f'{sequence_name}_den_ele_pt'].Fill(gen_pt)
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_{filter_name}'].Fill(gen_pt)
                            
                        if ind == 1:
                            hist_manager.histograms[f'{sequence_name}_den_ele_eta'].Fill(eg.eta())
                            hist_manager.histograms[f'{sequence_name}_den_ele_phi'].Fill(eg.phi())
                            
                        hist_manager.histograms[f'{sequence_name}_num_ele_eta_{filter_name}'].Fill(eg.eta())
                        hist_manager.histograms[f'{sequence_name}_num_ele_phi_{filter_name}'].Fill(eg.phi())

def main():
    parser = argparse.ArgumentParser(description='E/gamma HLT analyzer')
    parser.add_argument('in_filename', nargs="+", help='input filename(s)')
    parser.add_argument("-o", "--output", required=True, help="Output file name")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("-n", "--max-events", type=int, default=-1, help="Maximum number of events to process (-1 for all events)")
    
    args = parser.parse_args()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    # Initialize ROOT
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.gSystem.Load("libDataFormatsFWLite.so")
    ROOT.FWLiteEnabler.enable()
    
    # Validate input files
    valid_files = []
    for file in args.in_filename:
        try:
            file_temp = ROOT.TFile(file)
            if file_temp.IsZombie():
                logger.warning(f"Skipping invalid file: {file}")
                continue
            valid_files.append(file)
        except Exception as e:
            logger.error(f"Error opening file {file}: {str(e)}")
            continue
    
    if not valid_files:
        logger.error("No valid input files found")
        sys.exit(1)
    
    # Create histogram manager
    pt_bins = array('d', [5,10,15,20,22,26,28,30,32,34,36,38,40,45,50,60,80,100,150,250,500])
    eta_bins = array('d', [-2.5,-2.4,-2.3,-2.2,-2.1,-2.0,-1.9,-1.8,-1.7,-1.56,-1.44,-1.3,-1.2,-1.1,-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.44,1.56,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5])
    phi_bins = array('d', [-3.32,-2.97,-2.62,-2.27,-1.92,-1.57,-1.22,-0.87,-0.52,-0.18,0.18,0.52,0.87,1.22,1.57,1.92,2.27,2.62,2.97,3.32])
    
    hist_manager = HistogramManager(pt_bins, eta_bins, phi_bins)
    
    # Define sequences
    sequences = {
      'HLTEle26WP70Unseeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgammaUnseededSequence + HLTHgcalTiclPFClusteringForEgammaUnseededSequence + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded +hltEG26EtUnseededFilter + hltEgammaClusterShapeUnseeded + hltEle26WP70ClusterShapeUnseededFilter + hltEgammaHGCALIDVarsUnseeded +hltEle26WP70ClusterShapeSigmavvUnseededFilter + hltEle26WP70ClusterShapeSigmawwUnseededFilter + hltEle26WP70HgcalHEUnseededFilter +HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEUnseeded + hltEle26WP70HEUnseededFilter +hltEgammaEcalPFClusterIsoUnseeded + hltEle26WP70EcalIsoUnseededFilter + hltEgammaHGCalLayerClusterIsoUnseeded +hltEle26WP70HgcalIsoUnseededFilter + HLTPFHcalClusteringForEgammaSequence + hltEgammaHcalPFClusterIsoUnseeded +hltEle26WP70HcalIsoUnseededFilter + HLTElePixelMatchUnseededSequence + hltEle26WP70PixelMatchUnseededFilter +hltEle26WP70PMS2UnseededFilter + HLTGsfElectronUnseededSequence + hltEle26WP70GsfOneOEMinusOneOPUnseededFilter +hltEle26WP70GsfDetaUnseededFilter + hltEle26WP70GsfDphiUnseededFilter + hltEle26WP70BestGsfNLayerITUnseededFilter +hltEle26WP70BestGsfChi2UnseededFilter + hltEgammaEleL1TrkIsoUnseeded + hltEle26WP70GsfTrackIsoFromL1TracksUnseededFilter +HLTTrackingSequence + hltEgammaEleGsfTrackIsoUnseeded + hltEle26WP70GsfTrackIsoUnseededFilter )",
       'HLTEle26WP70L1Seeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalL1SeededSequence + HLTPFClusteringForEgammaL1SeededSequence + HLTHgcalTiclPFClusteringForEgammaL1SeededSequence + hltEgammaCandidatesL1Seeded + hltEgammaCandidatesWrapperL1Seeded + hltEG26EtL1SeededFilter + hltEgammaClusterShapeL1Seeded+hltEle26WP70ClusterShapeL1SeededFilter + hltEgammaHGCALIDVarsL1Seeded+hltEle26WP70ClusterShapeSigmavvL1SeededFilter + hltEle26WP70ClusterShapeSigmawwL1SeededFilter + hltEle26WP70HgcalHEL1SeededFilter + HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEL1Seeded+hltEle26WP70HEL1SeededFilter + hltEgammaEcalPFClusterIsoL1Seeded + hltEle26WP70EcalIsoL1SeededFilter + hltEgammaHGCalLayerClusterIsoL1Seeded + hltEle26WP70HgcalIsoL1SeededFilter + HLTPFHcalClusteringForEgammaSequence + hltEgammaHcalPFClusterIsoL1Seeded + hltEle26WP70HcalIsoL1SeededFilter + HLTElePixelMatchL1SeededSequence + hltEle26WP70PixelMatchL1SeededFilter + hltEle26WP70PMS2L1SeededFilter + HLTGsfElectronL1SeededSequence + hltEle26WP70GsfOneOEMinusOneOPL1SeededFilter + hltEle26WP70GsfDetaL1SeededFilter + hltEle26WP70GsfDphiL1SeededFilter + hltEle26WP70BestGsfNLayerITL1SeededFilter + hltEle26WP70BestGsfChi2L1SeededFilter + hltEgammaEleL1TrkIsoL1Seeded + hltEle26WP70GsfTrackIsoFromL1TracksL1SeededFilter + HLTTrackingSequence + hltEgammaEleGsfTrackIsoL1Seeded + hltEle26WP70GsfTrackIsoL1SeededFilter )",
       'HLTEle32WPTightUnseeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgammaUnseededSequence + HLTHgcalTiclPFClusteringForEgammaUnseededSequence + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded + hltEG32EtUnseededFilter+hltEgammaClusterShapeUnseeded + hltEle32WPTightClusterShapeUnseededFilter + hltEgammaHGCALIDVarsUnseeded + hltEle32WPTightClusterShapeSigmavvUnseededFilter + hltEle32WPTightClusterShapeSigmawwUnseededFilter + hltEle32WPTightHgcalHEUnseededFilter + HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEUnseeded + hltEle32WPTightHEUnseededFilter + hltEgammaEcalPFClusterIsoUnseeded + hltEle32WPTightEcalIsoUnseededFilter + hltEgammaHGCalLayerClusterIsoUnseeded + hltEle32WPTightHgcalIsoUnseededFilter + HLTPFHcalClusteringForEgammaSequence + hltEgammaHcalPFClusterIsoUnseeded + hltEle32WPTightHcalIsoUnseededFilter + HLTElePixelMatchUnseededSequence + hltEle32WPTightPixelMatchUnseededFilter + hltEle32WPTightPMS2UnseededFilter + HLTGsfElectronUnseededSequence + hltEle32WPTightGsfOneOEMinusOneOPUnseededFilter + hltEle32WPTightGsfDetaUnseededFilter + hltEle32WPTightGsfDphiUnseededFilter + hltEle32WPTightBestGsfNLayerITUnseededFilter + hltEle32WPTightBestGsfChi2UnseededFilter + hltEgammaEleL1TrkIsoUnseeded + hltEle32WPTightGsfTrackIsoFromL1TracksUnseededFilter + HLTTrackingSequence + hltEgammaEleGsfTrackIsoUnseeded + hltEle32WPTightGsfTrackIsoUnseededFilter )",
       'HLTEle32WPTightL1Seeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalL1SeededSequence +HLTPFClusteringForEgammaL1SeededSequence +HLTHgcalTiclPFClusteringForEgammaL1SeededSequence +hltEgammaCandidatesL1Seeded +hltEgammaCandidatesWrapperL1Seeded +hltEG32EtL1SeededFilter +hltEgammaClusterShapeL1Seeded +hltEle32WPTightClusterShapeL1SeededFilter +hltEgammaHGCALIDVarsL1Seeded +hltEle32WPTightClusterShapeSigmavvL1SeededFilter +hltEle32WPTightClusterShapeSigmawwL1SeededFilter +hltEle32WPTightHgcalHEL1SeededFilter +HLTEGammaDoLocalHcalSequence +HLTFastJetForEgammaSequence +hltEgammaHoverEL1Seeded +hltEle32WPTightHEL1SeededFilter +hltEgammaEcalPFClusterIsoL1Seeded +hltEle32WPTightEcalIsoL1SeededFilter +hltEgammaHGCalLayerClusterIsoL1Seeded +hltEle32WPTightHgcalIsoL1SeededFilter +HLTPFHcalClusteringForEgammaSequence +hltEgammaHcalPFClusterIsoL1Seeded +hltEle32WPTightHcalIsoL1SeededFilter +HLTElePixelMatchL1SeededSequence +hltEle32WPTightPixelMatchL1SeededFilter +hltEle32WPTightPMS2L1SeededFilter +HLTGsfElectronL1SeededSequence +hltEle32WPTightGsfOneOEMinusOneOPL1SeededFilter +hltEle32WPTightGsfDetaL1SeededFilter +hltEle32WPTightGsfDphiL1SeededFilter +hltEle32WPTightBestGsfNLayerITL1SeededFilter +hltEle32WPTightBestGsfChi2L1SeededFilter +hltEgammaEleL1TrkIsoL1Seeded +hltEle32WPTightGsfTrackIsoFromL1TracksL1SeededFilter +HLTTrackingSequence +hltEgammaEleGsfTrackIsoL1Seeded +hltEle32WPTightGsfTrackIsoL1SeededFilter )",
       'HLTDoubleEle25CaloIdLPMS2L1Seeded': "cms.Sequence( hltEGL1SeedsForDoubleEleNonIsolatedFilter + HLTDoFullUnpackingEgammaEcalL1SeededSequence + HLTPFClusteringForEgammaL1SeededSequence + HLTHgcalTiclPFClusteringForEgammaL1SeededSequence + hltEgammaCandidatesL1Seeded + hltEgammaCandidatesWrapperL1Seeded + hltDiEG25EtL1SeededFilter + hltEgammaClusterShapeL1Seeded + hltDiEG25CaloIdLClusterShapeL1SeededFilter + hltEgammaHGCALIDVarsL1Seeded + hltDiEG25CaloIdLClusterShapeSigmavvL1SeededFilter + hltDiEG25CaloIdLHgcalHEL1SeededFilter + HLTEGammaDoLocalHcalSequence + hltEgammaHoverEL1Seeded + hltDiEG25CaloIdLHEL1SeededFilter + HLTElePixelMatchL1SeededSequence + hltDiEle25CaloIdLPixelMatchL1SeededFilter + hltDiEle25CaloIdLPMS2L1SeededFilter )",
       'HLTDoubleEle25CaloIdLPMS2Unseeded': "cms.Sequence( HLTL1Sequence + hltEGL1SeedsForDoubleEleNonIsolatedFilter + HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgammaUnseededSequence + HLTHgcalTiclPFClusteringForEgammaUnseededSequence + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded + hltDiEG25EtUnseededFilter + hltEgammaClusterShapeUnseeded + hltDiEG25CaloIdLClusterShapeUnseededFilter + hltEgammaHGCALIDVarsUnseeded + hltDiEG25CaloIdLClusterShapeSigmavvUnseededFilter + hltDiEG25CaloIdLHgcalHEUnseededFilter + HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEUnseeded + hltDiEG25CaloIdLHEUnseededFilter + HLTElePixelMatchUnseededSequence + hltDiEle25CaloIdLPixelMatchUnseededFilter + hltDiEle25CaloIdLPMS2UnseededFilter )",
       'HLTDoubleEle2312IsoL1Seeded': "cms.Sequence( hltEGL1SeedsForDoubleEleIsolatedFilter +HLTDoFullUnpackingEgammaEcalL1SeededSequence +HLTPFClusteringForEgammaL1SeededSequence +HLTHgcalTiclPFClusteringForEgammaL1SeededSequence +hltEgammaCandidatesL1Seeded +hltEgammaCandidatesWrapperL1Seeded +hltEG23EtL1SeededFilter +hltDiEG12EtL1SeededFilter +hltEgammaClusterShapeL1Seeded +hltDiEG2312IsoClusterShapeL1SeededFilter +hltEgammaHGCALIDVarsL1Seeded +hltDiEG2312IsoClusterShapeSigmavvL1SeededFilter +hltDiEG2312IsoClusterShapeSigmawwL1SeededFilter +hltDiEG2312IsoHgcalHEL1SeededFilter +HLTEGammaDoLocalHcalSequence +HLTFastJetForEgammaSequence +hltEgammaHoverEL1Seeded +hltDiEG2312IsoHEL1SeededFilter +hltEgammaEcalPFClusterIsoL1Seeded +hltDiEG2312IsoEcalIsoL1SeededFilter +hltEgammaHGCalLayerClusterIsoL1Seeded +hltDiEG2312IsoHgcalIsoL1SeededFilter +HLTPFHcalClusteringForEgammaSequence +hltEgammaHcalPFClusterIsoL1Seeded +hltDiEG2312IsoHcalIsoL1SeededFilter +HLTElePixelMatchL1SeededSequence +hltDiEle2312IsoPixelMatchL1SeededFilter +hltDiEle2312IsoPMS2L1SeededFilter +HLTGsfElectronL1SeededSequence +hltDiEle2312IsoGsfOneOEMinusOneOPL1SeededFilter +hltDiEle2312IsoGsfDetaL1SeededFilter +hltDiEle2312IsoGsfDphiL1SeededFilter +hltDiEle2312IsoBestGsfNLayerITL1SeededFilter +hltDiEle2312IsoBestGsfChi2L1SeededFilter +hltEgammaEleL1TrkIsoL1Seeded +hltDiEle2312IsoGsfTrackIsoFromL1TracksL1SeededFilter +HLTTrackingSequence +hltEgammaEleGsfTrackIsoL1Seeded +hltDiEle2312IsoGsfTrackIsoL1SeededFilter )"
    }
    
    # Get filter names for each sequence
    sequence_filters = {name: getFilters(seq) for name, seq in sequences.items()}
    print(f"Sequence Filter: {sequence_filters}")
    
    # Create histograms for all sequences
    hist_manager.create_histograms(sequence_filters)
    
    # Process events
    events = Events(valid_files)
    process_events(events, hist_manager, sequence_filters, args.max_events)
    
    # Write output
    try:
        output_file = TFile(args.output, 'recreate')
        hist_manager.write_histograms(output_file)
        output_file.Close()
    except Exception as e:
        logger.error(f"Error writing output file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
