#!/usr/bin/env python

#RUN it like this
#python3 filename.py inputFile.root -o=outFile.root

import ROOT
from DataFormats.FWLite import Events, Handle
import argparse
import glob
import os
import time
import math

# Constants
MAX_DR = 0.1



def match_egm_trig_objs_to_ecal_cands(egm_trig_eta: float, egm_trig_phi: float, ecal_sc: list, max_dr: float = MAX_DR) -> list:
    """
    Match EGM trigger object to Ecal SC candidates using deltaR
    
    Args:
        egm_trig_eta: EGM trigger object eta
        egm_trig_phi: EGM trigger object phi
        ecal_sc: List of Ecal SC candidates
        max_dr: Maximum deltaR for matching (default 0.1)
        
    Returns:
        List of matched Ecal SC candidates within max_dr
    """
    max_dr2 = max_dr * max_dr
    matched_candidates = [obj for obj in ecal_sc if ROOT.reco.deltaR2(egm_trig_eta, egm_trig_phi, obj.eta(), obj.phi()) < max_dr2]    
    return matched_candidates

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Egamma HLT analyser',
            epilog="""
Examples:
  python3 makeNtuples_Run3.py /path/to/input/folder -o output.root
  python3 makeNtuples_Run3.py input.root -o output.root  # Still works with individual files
        """            
    )
    parser.add_argument('input_path', help='input folder path or individual filename(s)')
    parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
    args = parser.parse_args()

    output_file = args.output

    # Check if input_path is a directory or file(s)
    input_path = args.input_path
    
    if os.path.isdir(input_path):
        # It's a directory - find all ROOT files in it
        print(f"🔍 Scanning directory: {input_path}")
        root_files = glob.glob(os.path.join(input_path, "*.root"))
        if not root_files:
            print(f"❌ No ROOT files found in directory: {input_path}")
            exit(1)
        print(f"📁 Found {len(root_files)} ROOT files in directory")
        file_list = root_files
    else:
        # It's a file or doesn't exist - treat as before
        file_list = [input_path]
    
    # Validate files (remove corrupted ones)
    to_remove = []
    for file in file_list:
        if not os.path.exists(file):
            print(f"⚠️  File does not exist: {file}")
            to_remove.append(file)
            continue
            
        file_temp = ROOT.TFile(file)
        if file_temp.IsZombie():
            print(f"💀 Corrupted file detected: {file}")
            to_remove.append(file)
        file_temp.Close()
    
    file_list = [x for x in file_list if x not in to_remove]
    
    if not file_list:
        print("❌ No valid input files found!")
        exit(1)
        
    print(f"✅ Processing {len(file_list)} valid files:")
    for i, file in enumerate(file_list, 1):
        print(f"  {i}. {os.path.basename(file)}")

    # Create handles for the collections
    egtrigobjs_handle = Handle("std::vector<trigger::EgammaObject>")
    egtrigobjs_label = ("hltEgammaHLTExtra", "", "MYHLT")
    #egtrigobjs_label = ("hltEgammaHLTExtra", "", "") # Original HLT result
    ecal_handle = Handle("std::vector<reco::RecoEcalCandidate>")
    ecal_label = ("hltEgammaCandidates", "", "MYHLT")
    
    # Pixel match variable handles
    s2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    s2_label = ("hltEgammaPixelMatchVars", "s2", "MYHLT")
    
    dphi1_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi1_label = ("hltEgammaPixelMatchVars", "dPhi1", "MYHLT")
    
    dphi1bests2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi1bests2_label = ("hltEgammaPixelMatchVars", "dPhi1BestS2", "MYHLT")
    
    dphi2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi2_label = ("hltEgammaPixelMatchVars", "dPhi2", "MYHLT")
    
    dphi2bests2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi2bests2_label = ("hltEgammaPixelMatchVars", "dPhi2BestS2", "MYHLT")
    
    dphi3_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi3_label = ("hltEgammaPixelMatchVars", "dPhi3", "MYHLT")
    
    dphi4_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dphi4_label = ("hltEgammaPixelMatchVars", "dPhi4", "MYHLT")
    
    drz1_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    drz1_label = ("hltEgammaPixelMatchVars", "dRZ1", "MYHLT")
    
    drz2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    drz2_label = ("hltEgammaPixelMatchVars", "dRZ2", "MYHLT")
    
    drz3_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    drz3_label = ("hltEgammaPixelMatchVars", "dRZ3", "MYHLT")
    
    drz4_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    drz4_label = ("hltEgammaPixelMatchVars", "dRZ4", "MYHLT")
    
    dzbests2_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    dzbests2_label = ("hltEgammaPixelMatchVars", "dzBestS2", "MYHLT")
    
    etawidth_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    etawidth_label = ("hltEgammaPixelMatchVars", "etaWidth", "MYHLT")
    
    nrclus_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    nrclus_label = ("hltEgammaPixelMatchVars", "nrClus", "MYHLT")
    
    phiwidth_handle = Handle("edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> >")
    phiwidth_label = ("hltEgammaPixelMatchVars", "phiWidth", "MYHLT")

    # Create output file and tree
    out_file = ROOT.TFile(output_file, "RECREATE")
    tree = ROOT.TTree("egHLTTree", "EGamma Tree")

    # Create variables for the tree
    run = ROOT.std.vector("int")()
    lumi = ROOT.std.vector("int")()

    # E/Gamma object variables
    eg_et = ROOT.std.vector("float")()
    eg_energy = ROOT.std.vector("float")()
    eg_eta = ROOT.std.vector("float")()
    eg_phi = ROOT.std.vector("float")()
    
    # Ecal candidate variables
    ecal_eta = ROOT.std.vector("float")()
    ecal_phi = ROOT.std.vector("float")()
    
    # Pixel match variables
    s2_values = ROOT.std.vector("float")()
    dphi1_values = ROOT.std.vector("float")()
    dphi1bests2_values = ROOT.std.vector("float")()
    dphi2_values = ROOT.std.vector("float")()
    dphi2bests2_values = ROOT.std.vector("float")()
    dphi3_values = ROOT.std.vector("float")()
    dphi4_values = ROOT.std.vector("float")()
    drz1_values = ROOT.std.vector("float")()
    drz2_values = ROOT.std.vector("float")()
    drz3_values = ROOT.std.vector("float")()
    drz4_values = ROOT.std.vector("float")()
    dzbests2_values = ROOT.std.vector("float")()
    etawidth_values = ROOT.std.vector("float")()
    nrclus_values = ROOT.std.vector("float")()
    phiwidth_values = ROOT.std.vector("float")()
    
    # Matching information
    egm_matched_to_ecal = ROOT.std.vector("bool")()
    ecal_matched_to_egm = ROOT.std.vector("bool")()
    delta_r_values = ROOT.std.vector("float")()

    # Create branches
    tree.Branch("run", run)
    tree.Branch("lumi", lumi)
    tree.Branch("eg_et", eg_et)
    tree.Branch("eg_energy", eg_energy)
    tree.Branch("eg_eta", eg_eta)    
    tree.Branch("eg_phi", eg_phi)
    tree.Branch("ecal_eta", ecal_eta)
    tree.Branch("ecal_phi", ecal_phi)
    
    # Pixel match variable branches
    tree.Branch("s2_values", s2_values)
    tree.Branch("dphi1_values", dphi1_values)
    tree.Branch("dphi1bests2_values", dphi1bests2_values)
    tree.Branch("dphi2_values", dphi2_values)
    tree.Branch("dphi2bests2_values", dphi2bests2_values)
    tree.Branch("dphi3_values", dphi3_values)
    tree.Branch("dphi4_values", dphi4_values)
    tree.Branch("drz1_values", drz1_values)
    tree.Branch("drz2_values", drz2_values)
    tree.Branch("drz3_values", drz3_values)
    tree.Branch("drz4_values", drz4_values)
    tree.Branch("dzbests2_values", dzbests2_values)
    tree.Branch("etawidth_values", etawidth_values)
    tree.Branch("nrclus_values", nrclus_values)
    tree.Branch("phiwidth_values", phiwidth_values)
    
    # Matching information branches
    tree.Branch("egm_matched_to_ecal", egm_matched_to_ecal)
    tree.Branch("ecal_matched_to_egm", ecal_matched_to_egm)
    tree.Branch("delta_r_values", delta_r_values)    

    # Open events
    events = Events(file_list)

    percent_step = 1
    start_time = time.time() 
    total_entries = events.size()  
    
    for event_nr,event in enumerate(events):
        #if event_nr >= max_events:  # Process up to max_events
        #    break
        current_percent = (event_nr + 1) / total_entries * 100
        
        # Debug: Show progress for first few events
        if event_nr < 3:
            print(f"Processing event {event_nr}...")
        
        if current_percent % percent_step == 0:
           elapsed_time = time.time()-start_time
           est_finish = "n/a"
           if event_nr!=0 or elapsed_time==0:
                remaining = float(events.size()-event_nr)/event_nr*elapsed_time 
                est_finish = time.ctime(remaining+start_time+elapsed_time)
                print("{} / {} time: {:.1f}s, est finish {}".format(event_nr+1,events.size(),elapsed_time,est_finish))

        # Clear vectors for this event
        run.clear()
        lumi.clear()
        eg_et.clear()
        eg_energy.clear()
        eg_eta.clear()
        eg_phi.clear()
        ecal_eta.clear()
        ecal_phi.clear()
        
        # Clear pixel match variables
        s2_values.clear()
        dphi1_values.clear()
        dphi1bests2_values.clear()
        dphi2_values.clear()
        dphi2bests2_values.clear()
        dphi3_values.clear()
        dphi4_values.clear()
        drz1_values.clear()
        drz2_values.clear()
        drz3_values.clear()
        drz4_values.clear()
        dzbests2_values.clear()
        etawidth_values.clear()
        nrclus_values.clear()
        phiwidth_values.clear()
        
        # Clear matching information
        egm_matched_to_ecal.clear()
        ecal_matched_to_egm.clear()
        delta_r_values.clear()

        # Add event info
        run.push_back(event.eventAuxiliary().run())
        lumi.push_back(event.eventAuxiliary().luminosityBlock())

        # Get trigger objects
        try:
            event.getByLabel(egtrigobjs_label, egtrigobjs_handle)                   
        except Exception as e:
            print(f"  Error getting EgammaObject for event {event_nr}: {e}")
            continue

        if not egtrigobjs_handle.isValid():
            print(f"  No valid EgammaObject for event {event_nr}")
            continue

        eg_trig_objs = egtrigobjs_handle.product()
        if eg_trig_objs.size() == 0:
            print(f"  Empty EgammaObject collection for event {event_nr}")
            continue

        for j, obj in enumerate(eg_trig_objs):
            # Basic properties
            eg_et.push_back(obj.et())
            eg_energy.push_back(obj.energy())
            eg_eta.push_back(obj.eta())
            eg_phi.push_back(obj.phi())

        # Get Ecal candidates and s2 values
        try:
            event.getByLabel(ecal_label, ecal_handle)
        except Exception as e:    
            print(f"  Error getting Ecal candidates for event {event_nr}: {e}")
            continue

        if not ecal_handle.isValid():
            print("  No valid Ecal candidates")
            continue
    
        ecal_cands = ecal_handle.product()
        print(f"  Found {len(ecal_cands)} Ecal candidate(s)")
        
        # Fill ecal candidate variables
        for ecal_cand in ecal_cands:
            ecal_eta.push_back(ecal_cand.eta())
            ecal_phi.push_back(ecal_cand.phi())
        
        # Perform deltaR matching between EGM objects and Ecal candidates
        total_matches = 0
        
        # Initialize matching flags
        for i in range(len(eg_trig_objs)):
            egm_matched_to_ecal.push_back(False)
        for i in range(len(ecal_cands)):
            ecal_matched_to_egm.push_back(False)
        
        # Match each EGM object to Ecal candidates and find best match
        for i, egm_obj in enumerate(eg_trig_objs):
            matched_candidates = match_egm_trig_objs_to_ecal_cands(egm_obj.eta(), egm_obj.phi(), ecal_cands, MAX_DR)
            
            if matched_candidates:
                egm_matched_to_ecal[i] = True
                total_matches += 1  # Only count one match per EGM object (the best one)
                
                # Find the best match (closest in deltaR)
                best_match = None
                best_dr = float('inf')
                best_idx = -1
                
                for matched_cand in matched_candidates:
                    # Find the index of this candidate in the original list
                    for j, ecal_cand in enumerate(ecal_cands):
                        if (ecal_cand.eta() == matched_cand.eta() and 
                            ecal_cand.phi() == matched_cand.phi()):
                            # Calculate deltaR for this match
                            dr2 = ROOT.reco.deltaR2(egm_obj.eta(), egm_obj.phi(), 
                                                   matched_cand.eta(), matched_cand.phi())
                            dr = math.sqrt(dr2)
                            
                            if dr < best_dr:
                                best_dr = dr
                                best_match = matched_cand
                                best_idx = j
                            break
                
                # Mark the best matched Ecal candidate
                if best_idx >= 0:
                    ecal_matched_to_egm[best_idx] = True
                    delta_r_values.push_back(best_dr)
                    print(f"  Best match for EGM {i}: dR={best_dr:.4f}, idx={best_idx}")
        
        print(f"  Found {total_matches} best matches between EGM objects and Ecal candidates")
        
        # Get pixel match variables using the working method (values array)
        pixel_vars = [
            (s2_handle, s2_label, s2_values, "s2"),
            (dphi1_handle, dphi1_label, dphi1_values, "dPhi1"),
            (dphi1bests2_handle, dphi1bests2_label, dphi1bests2_values, "dPhi1BestS2"),
            (dphi2_handle, dphi2_label, dphi2_values, "dPhi2"),
            (dphi2bests2_handle, dphi2bests2_label, dphi2bests2_values, "dPhi2BestS2"),
            (dphi3_handle, dphi3_label, dphi3_values, "dPhi3"),
            (dphi4_handle, dphi4_label, dphi4_values, "dPhi4"),
            (drz1_handle, drz1_label, drz1_values, "dRZ1"),
            (drz2_handle, drz2_label, drz2_values, "dRZ2"),
            (drz3_handle, drz3_label, drz3_values, "dRZ3"),
            (drz4_handle, drz4_label, drz4_values, "dRZ4"),
            (dzbests2_handle, dzbests2_label, dzbests2_values, "dzBestS2"),
            (etawidth_handle, etawidth_label, etawidth_values, "etaWidth"),
            (nrclus_handle, nrclus_label, nrclus_values, "nrClus"),
            (phiwidth_handle, phiwidth_label, phiwidth_values, "phiWidth"),
        ]
        
        # Process each pixel match variable using the working method
        for handle, label, values_vector, var_name in pixel_vars:
            try:
                event.getByLabel(label, handle)
                if handle.isValid():
                    association_map = handle.product()
                    
                    # Use the values() method that works
                    values = association_map.values()
                    
                    # Fill values only for best matched Ecal candidates
                    for i in range(len(ecal_cands)):
                        if ecal_matched_to_egm[i]:  # Only for best matched candidates
                            if i < len(values):
                                value = values[i]
                                values_vector.push_back(value)
                                print(f"    {var_name} value for best match {i}: {value:.6f}")
                            else:
                                values_vector.push_back(-999.0)
                                print(f"    {var_name}: index {i} >= values size {len(values)}")
                        else:
                            values_vector.push_back(-999.0)  # Default for unmatched
                else:
                    print(f"  {var_name} map is not valid")
                    # Fill with default values if map not valid
                    for i in range(len(ecal_cands)):
                        values_vector.push_back(-999.0)
            except Exception as e:
                print(f"  Error getting {var_name} for event {event_nr}: {e}")
                # Fill with default values
                for i in range(len(ecal_cands)):
                    values_vector.push_back(-999.0)
        
        # Fill the tree with data for this event
            tree.Fill()

    # Write and close
    out_file.Write()
    out_file.Close()
    print(f"\nNtuple saved to: {output_file}")
    print("You can open this file in ROOT to inspect the variables:")
    print("  - eg_et, eg_energy, eg_eta, eg_phi (EGM trigger objects)")
    print("  - ecal_eta, ecal_phi (Ecal candidates)")
    print("  - s2_values, dphi1_values, dphi2_values, etc. (pixel match variables)")
    print("  - egm_matched_to_ecal, ecal_matched_to_egm (matching flags)")
    print("  - delta_r_values (deltaR between matches)")