#!/usr/bin/env python

#RUN it like this
#python3 filename.py  inputFile.root   -o=outFile.root 

from array import array
import re
import argparse
import sys
import math
import logging
import numpy as np
from typing import List, Dict, Any
from DataFormats.FWLite import Events, Handle
import ROOT
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, edm
import json
import FWCore.ParameterSet.Config as cms
from CondCore.CondDB.CondDB_cfi import *
from PhysicsTools.PythonAnalysis import *
import time
import glob
import os
import subprocess

# Constants
EB_ETA_MAX = 1.44
EE_ETA_MIN = 1.56
MIN_GEN_PT = 25.
MAX_DR = 0.1

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HistogramManager:
    def __init__(self, pt_bins: array, pt_bins_TurnOn: array, eta_bins: array, phi_bins: array):
        self.pt_bins = pt_bins
        self.pt_bins_TurnOn = pt_bins_TurnOn
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
            self.histograms[f'{sequence_name}_den_ele_pt_EB'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt_EB", "pT", len(self.pt_bins)-1, self.pt_bins)
            self.histograms[f'{sequence_name}_den_ele_pt_EE'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt_EE", "pT", len(self.pt_bins)-1, self.pt_bins)
            self.histograms[f'{sequence_name}_den_ele_pt'] = ROOT.TH1D(f"{sequence_name}_den_ele_pt", "pT", len(self.pt_bins)-1, self.pt_bins)
            
            # Create eta and phi denominator histograms
            self.histograms[f'{sequence_name}_den_ele_eta'] = ROOT.TH1D(f"{sequence_name}_den_ele_eta", "eta", len(self.eta_bins)-1, self.eta_bins)
            self.histograms[f'{sequence_name}_den_ele_phi'] = ROOT.TH1D(f"{sequence_name}_den_ele_phi", "phi", len(self.phi_bins)-1, self.phi_bins)
            
            # Create numerator histograms for each filter in this sequence
            for filter_name in sequences[sequence_name]:
                self.histograms[f'{sequence_name}_num_ele_pt_EB_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_EB_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)
                self.histograms[f'{sequence_name}_num_ele_pt_EE_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_EE_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)
                self.histograms[f'{sequence_name}_num_ele_pt_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_pt_{filter_name}", "pT", len(self.pt_bins)-1, self.pt_bins)
                        
                # Create eta and phi numerator histograms
                self.histograms[f'{sequence_name}_num_ele_eta_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_eta_{filter_name}", "eta", len(self.eta_bins)-1, self.eta_bins)
                self.histograms[f'{sequence_name}_num_ele_phi_{filter_name}'] = ROOT.TH1D(f"{sequence_name}_num_ele_phi_{filter_name}", "phi", len(self.phi_bins)-1, self.phi_bins)

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

def getFilterIndex(trigEvt, filterName):
    """Get the index of a specific filter in the trigger event.
    
    Args:
        trigEvt: Trigger event object (trigger::TriggerEvent)
        filterName: Name of the filter to search for
        
    Returns:
        Index of the filter if found, otherwise sizeFilters() (invalid index)
        
    Note:
        Handles AOD filter label format by cleaning quotes and bracket notation.
        Example: "hltEle26WP70Filter"[25] -> hltEle26WP70Filter
    """
    for index in range(0, trigEvt.sizeFilters()):
        # Convert C++ string_view to Python string for comparison
        label = str(trigEvt.filterLabel(index))
        
        # Clean the label - remove quotes and bracket notation like [25]
        # Format: "hltDiEG12EtL1SeededFilter"[25] -> hltDiEG12EtL1SeededFilter
        clean_label = label.split('[')[0]  # Remove [38] part first
        clean_label = clean_label.strip('"')  # Remove surrounding quotes
        
        if filterName == clean_label:
                return index
    return trigEvt.sizeFilters()

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
    #ele_handle, ele_label = Handle("vector<reco::Electron>"), ("hltEgammaGsfElectronsUnseeded", "", "HLTX")
    ele_handle, ele_label = Handle("std::vector<trigger::EgammaObject>"), "hltEgammaHLTExtra:Unseeded"
    hlt_handle, hlt_label = Handle("edm::TriggerResults"), ("TriggerResults", "", "HLTX")
    hltevt_handle, hltevt_label = Handle("trigger::TriggerEvent"), "hltTriggerSummaryAOD::HLTX"
    #triggerObjects_handle, triggerObjects_label = Handle("vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
    triggerObjects_handle, triggerObjects_label = Handle("trigger::TriggerEvent"), "hltTriggerSummaryAOD::HLTX"
    gen_handle, gen_label = Handle("vector<reco::GenParticle>"), ("genParticles", "", "HLT")
    
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
            event.getByLabel(hlt_label, hlt_handle)
            event.getByLabel(triggerObjects_label, triggerObjects_handle)
            event.getByLabel(gen_label, gen_handle)
        except Exception as e:
            logger.error(f"Error getting event data: {str(e)}")
            continue
            
        eles = ele_handle.product()
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
                
                # Fill denominator histograms once per electron (using first filter as reference)
                first_filter = filter_names[0] if filter_names else None
                if first_filter:
                    # Fill denominator histograms based on eta region
                    if abs(eg.eta()) <= EB_ETA_MAX:
                        hist_manager.histograms[f'{sequence_name}_den_ele_pt_EB'].Fill(eg.pt())
                    
                    if abs(eg.eta()) >= EE_ETA_MIN:
                        hist_manager.histograms[f'{sequence_name}_den_ele_pt_EE'].Fill(eg.pt())
                        
                    if abs(eg.eta()) <= EB_ETA_MAX or abs(eg.eta()) >= EE_ETA_MIN:
                        hist_manager.histograms[f'{sequence_name}_den_ele_pt'].Fill(eg.pt())
                        hist_manager.histograms[f'{sequence_name}_den_ele_eta'].Fill(eg.eta())
                        hist_manager.histograms[f'{sequence_name}_den_ele_phi'].Fill(eg.phi())
                
                # Process each filter in this sequence
                for ind, filter_name in enumerate(filter_names):
                    # Find trigger objects that passed this filter
                    matched_objs = []
                    
                    # Get filter index from trigger event
                    filter_index = getFilterIndex(trigger_objects, filter_name)
                    
                    if filter_index < trigger_objects.sizeFilters():
                        # Get trigger object keys for this filter
                        trigger_keys = trigger_objects.filterKeys(filter_index)
                        # Loop through trigger objects for this filter
                        for key in trigger_keys:
                            try:
                                trig_obj = trigger_objects.getObjects()[key]
                                matched_objs.append(trig_obj)
                            except Exception as e:
                                logger.error(f"Error accessing trigger object {key}: {e}")
                                continue
                    
                    # Match trigger objects to electron
                    matched_objs_before = len(matched_objs)
                    matched_objs = match_trig_objs(eg.eta(), eg.phi(), matched_objs)
                    nMatched = len(matched_objs)
                    
                    if nMatched > 0:
                        # Fill numerator histograms based on eta region
                        if abs(eg.eta()) <= EB_ETA_MAX:
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_EB_{filter_name}'].Fill(eg.pt())
                        
                        if abs(eg.eta()) >= EE_ETA_MIN:
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_EE_{filter_name}'].Fill(eg.pt())
                            
                        if abs(eg.eta()) <= EB_ETA_MAX or abs(eg.eta()) >= EE_ETA_MIN:
                            hist_manager.histograms[f'{sequence_name}_num_ele_pt_{filter_name}'].Fill(eg.pt())
                            hist_manager.histograms[f'{sequence_name}_num_ele_eta_{filter_name}'].Fill(eg.eta())
                            hist_manager.histograms[f'{sequence_name}_num_ele_phi_{filter_name}'].Fill(eg.phi())

def process_single_file(input_file: str, output_file: str, sequences: Dict[str, List[str]], 
                       pt_bins: array, pt_bins_TurnOn: array, eta_bins: array, phi_bins: array, 
                       max_events: int = -1) -> bool:
    """Process a single input file and create output histograms.
    
    Args:
        input_file: Path to input ROOT file
        output_file: Path to output ROOT file
        sequences: Dictionary mapping sequence names to their filter lists
        pt_bins, pt_bins_TurnOn, eta_bins, phi_bins: Histogram binning arrays
        max_events: Maximum number of events to process (-1 for all events)
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    try:
        print(f"🔄 Processing: {os.path.basename(input_file)}")
        
        # Create histogram manager for this file
        hist_manager = HistogramManager(pt_bins, pt_bins_TurnOn, eta_bins, phi_bins)
        hist_manager.create_histograms(sequences)
        
        # Process events from this single file
        events = Events([input_file])
        process_events(events, hist_manager, sequences, max_events)
        
        # Write output for this file
        output_root_file = TFile(output_file, 'recreate')
        hist_manager.write_histograms(output_root_file)
        output_root_file.Close()
        
        print(f"✅ Completed: {os.path.basename(input_file)} -> {os.path.basename(output_file)}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error processing {input_file}: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='E/gamma HLT analyzer - Memory efficient version 🚀')
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--input-file', help='Single input ROOT file')
    input_group.add_argument('--input-dir', help='Directory containing ROOT files')
    input_group.add_argument('--input-pattern', help='File pattern (e.g., /path/to/files/*.root)')
    
    parser.add_argument("-o", "--output", required=True, help="Output file name (for final merged output)")
    parser.add_argument("--output-dir", default="OutputNtuples_Reference", help="Directory for individual output files")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("-n", "--max-events", type=int, default=-1, help="Maximum number of events to process (-1 for all events)")
    
    args = parser.parse_args()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    # Initialize ROOT
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.gSystem.Load("libDataFormatsFWLite.so")
    ROOT.FWLiteEnabler.enable()
    
    # Create output directory
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created output directory: {output_dir}")
    
    # Determine input files
    input_files = []
    if args.input_file:
        input_files = [args.input_file]
    elif args.input_dir:
        # Handle EOS paths better
        if "eos" in args.input_dir:
            # Use shell expansion for EOS paths
            try:
                result = subprocess.run(f"ls {args.input_dir}/*.root",
                                     capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    input_files = result.stdout.strip().split('\n')
                else:
                    # Fallback to glob
                    input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
            except:
                input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
        else:
            input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
    elif args.input_pattern:
        # Handle EOS paths in patterns
        if "eos" in args.input_pattern:
            try:
                result = subprocess.run(f"ls {args.input_pattern}",
                                     capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    input_files = result.stdout.strip().split('\n')
                else:
                    input_files = glob.glob(args.input_pattern)
            except:
                input_files = glob.glob(args.input_pattern)
        else:
            input_files = glob.glob(args.input_pattern)

    if not input_files:
        print("❌ No input files found!")
        print("💡 Debugging info:")
        if args.input_dir:
            print(f"   Directory: {args.input_dir}")
            print(f"   Directory exists: {os.path.exists(args.input_dir)}")
            if os.path.exists(args.input_dir):
                print(f"   Directory contents:")
                try:
                    for item in os.listdir(args.input_dir):
                        print(f"     {item}")
                except Exception as e:
                    print(f"     Error listing directory: {e}")
        elif args.input_pattern:
            print(f"   Pattern: {args.input_pattern}")
        return
    
    print(f"🎯 Found {len(input_files)} input files")
    
    # Validate input files
    valid_files = []
    for file in input_files:
        try:
            file_temp = ROOT.TFile(file)
            if file_temp.IsZombie():
                logger.warning(f"Skipping invalid file: {file}")
                continue
            valid_files.append(file)
            file_temp.Close()  # Close immediately to free memory
        except Exception as e:
            logger.error(f"Error opening file {file}: {str(e)}")
            continue
    
    if not valid_files:
        logger.error("No valid input files found")
        sys.exit(1)
    
    print(f"✅ Valid files: {len(valid_files)}")
    
    # Setup histogram binning arrays
    # Custom pt binning: 0-50, 50-100, then steps of 100 till 3000, then steps of 250 till 4000
    pt_bins_list = [0, 50, 100]  # Start with 0-50, 50-100
    #pt_bins_list_TurnOn = [0, 20, 30, 40, 50, 60, 80, 100, 125, 150, 175, 200]
    pt_bins_list_TurnOn = [0, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 100, 125, 150, 175, 200]
    
    # Add steps of 100 from 100 to 3000
    for i in range(200, 3001, 100):
        pt_bins_list.append(i)
    
    # Add steps of 250 from 3000 to 4000
    for i in range(3250, 4001, 250):
        pt_bins_list.append(i)
    
    pt_bins = array('d', pt_bins_list)
    pt_bins_TurnOn = array('d', pt_bins_list_TurnOn)
    eta_bins = np.arange(-4, 4.01, 0.25, dtype='d')
    phi_bins = array('d', [-3.32,-2.97,-2.62,-2.27,-1.92,-1.57,-1.22,-0.87,-0.52,-0.18,0.18,0.52,0.87,1.22,1.57,1.92,2.27,2.62,2.97,3.32])
    
    # Define sequences
    sequences = {
       'HLTEle26WP70Unseeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalSequence + HLTPFClusteringForEgammaUnseededSequence + HLTHgcalTiclPFClusteringForEgammaUnseededSequence + hltEgammaCandidatesUnseeded + hltEgammaCandidatesWrapperUnseeded +hltEG26EtUnseededFilter + hltEgammaClusterShapeUnseeded + hltEle26WP70ClusterShapeUnseededFilter + hltEgammaHGCALIDVarsUnseeded +hltEle26WP70ClusterShapeSigmavvUnseededFilter + hltEle26WP70ClusterShapeSigmawwUnseededFilter + hltEle26WP70HgcalHEUnseededFilter +HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEUnseeded + hltEle26WP70HEUnseededFilter +hltEgammaEcalPFClusterIsoUnseeded + hltEle26WP70EcalIsoUnseededFilter + hltEgammaHGCalLayerClusterIsoUnseeded +hltEle26WP70HgcalIsoUnseededFilter + HLTPFHcalClusteringForEgammaSequence + hltEgammaHcalPFClusterIsoUnseeded +hltEle26WP70HcalIsoUnseededFilter + HLTElePixelMatchUnseededSequence + hltEle26WP70PixelMatchUnseededFilter +hltEle26WP70PMS2UnseededFilter + HLTGsfElectronUnseededSequence + hltEle26WP70GsfOneOEMinusOneOPUnseededFilter +hltEle26WP70GsfDetaUnseededFilter + hltEle26WP70GsfDphiUnseededFilter + hltEle26WP70BestGsfNLayerITUnseededFilter +hltEle26WP70BestGsfChi2UnseededFilter + hltEgammaEleL1TrkIsoUnseeded + hltEle26WP70GsfTrackIsoFromL1TracksUnseededFilter +HLTTrackingSequence + hltEgammaEleGsfTrackIsoUnseeded + hltEle26WP70GsfTrackIsoUnseededFilter )",
       'HLTEle26WP70L1Seeded': "cms.Sequence( hltEGL1SeedsForSingleEleIsolatedFilter + HLTDoFullUnpackingEgammaEcalL1SeededSequence + HLTPFClusteringForEgammaL1SeededSequence + HLTHgcalTiclPFClusteringForEgammaL1SeededSequence + hltEgammaCandidatesL1Seeded + hltEgammaCandidatesWrapperL1Seeded + hltEG26EtL1SeededFilter + hltEgammaClusterShapeL1Seeded+hltEle26WP70ClusterShapeL1SeededFilter + hltEgammaHGCALIDVarsL1Seeded+hltEle26WP70ClusterShapeSigmavvL1SeededFilter + hltEle26WP70ClusterShapeSigmawwL1SeededFilter + hltEle26WP70HgcalHEL1SeededFilter + HLTEGammaDoLocalHcalSequence + HLTFastJetForEgammaSequence + hltEgammaHoverEL1Seeded+hltEle26WP70HEL1SeededFilter + hltEgammaEcalPFClusterIsoL1Seeded + hltEle26WP70EcalIsoL1SeededFilter + hltEgammaHGCalLayerClusterIsoL1Seeded + hltEle26WP70HgcalIsoL1SeededFilter + HLTPFHcalClusteringForEgammaSequence + hltEgammaHcalPFClusterIsoL1Seeded + hltEle26WP70HcalIsoL1SeededFilter + HLTElePixelMatchL1SeededSequence + hltEle26WP70PixelMatchL1SeededFilter + hltEle26WP70PMS2L1SeededFilter + HLTGsfElectronL1SeededSequence + hltEle26WP70GsfOneOEMinusOneOPL1SeededFilter + hltEle26WP70GsfDetaL1SeededFilter + hltEle26WP70GsfDphiL1SeededFilter + hltEle26WP70BestGsfNLayerITL1SeededFilter + hltEle26WP70BestGsfChi2L1SeededFilter + hltEgammaEleL1TrkIsoL1Seeded + hltEle26WP70GsfTrackIsoFromL1TracksL1SeededFilter + HLTTrackingSequence + hltEgammaEleGsfTrackIsoL1Seeded + hltEle26WP70GsfTrackIsoL1SeededFilter )",
    }
    
    # Get filter names for each sequence
    sequence_filters = {name: getFilters(seq) for name, seq in sequences.items()}
    print(f"🔍 Sequence Filters Extracted:")
    for seq_name, filters in sequence_filters.items():
        print(f"  {seq_name}: {len(filters)} filters")
    
    # Process files one by one to avoid memory issues
    print(f"\n🚀 Starting individual file processing...")
    print(f"📁 Output directory: {output_dir}")
    
    successful_files = []
    failed_files = []
    
    for i, input_file in enumerate(valid_files, 1):
        # Generate unique output filename based on input filename
        input_basename = os.path.splitext(os.path.basename(input_file))[0]
        output_filename = f"{input_basename}_processed.root"
        output_filepath = os.path.join(output_dir, output_filename)
        
        print(f"\n📊 Processing file {i}/{len(valid_files)}: {os.path.basename(input_file)}")
        
        # Process this single file
        success = process_single_file(
            input_file, 
            output_filepath, 
            sequence_filters, 
            pt_bins, 
            pt_bins_TurnOn, 
            eta_bins, 
            phi_bins, 
            args.max_events
        )
        
        if success:
            successful_files.append(output_filepath)
        else:
            failed_files.append(input_file)
    
    # Print summary
    print(f"\n🎉 Processing Summary:")
    print(f"✅ Successfully processed: {len(successful_files)}/{len(valid_files)} files")
    print(f"❌ Failed files: {len(failed_files)}")
    
    if failed_files:
        print(f"Failed files:")
        for failed_file in failed_files:
            print(f"  - {os.path.basename(failed_file)}")
    
    # Generate hadd command for merging
    if successful_files:
        print(f"\n🔗 To merge all output files, run the following command:")
        successful_basenames = [os.path.basename(f) for f in successful_files]
        hadd_command = f"hadd {args.output} {output_dir}/*.root"
        print(f"   {hadd_command}")
        
        # Also create a script file for convenience
        script_filename = "merge_outputs.sh"
        with open(script_filename, 'w') as script_file:
            script_file.write("#!/bin/bash\n")
            script_file.write(f"# Auto-generated script to merge output files\n")
            script_file.write(f"# Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            script_file.write(f"echo 'Merging {len(successful_files)} output files...'\n")
            script_file.write(f"{hadd_command}\n")
            script_file.write(f"echo 'Merged output saved to: {args.output}'\n")
        
        # Make script executable
        os.chmod(script_filename, 0o755)
        print(f"📝 Merge script saved to: {script_filename}")
        print(f"   Run with: ./{script_filename}")
    else:
        print(f"❌ No files were successfully processed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
