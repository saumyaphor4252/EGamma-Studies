#!/usr/bin/env python3

import ROOT
from DataFormats.FWLite import Events, Handle
import argparse
import glob
import os

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Create debug ntuples for E/Gamma trigger objects from Run3 data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 makeNtuples_Run3_Seeded.py input.root -o output.root
  python3 makeNtuples_Run3_Seeded.py --collection-type unseeded input.root -o output.root
  python3 makeNtuples_Run3_Seeded.py --output output.root input.root
  python3 makeNtuples_Run3_Seeded.py --max-events 100 -o output.root input.root
  python3 makeNtuples_Run3_Seeded.py --input-dir /path/to/files/ -o output.root
  python3 makeNtuples_Run3_Seeded.py --input-pattern "*.root" -o output.root
  python3 makeNtuples_Run3_Seeded.py --help
        """
    )
    
    # Add new input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("input_file", nargs='?',
                           help="Input ROOT file containing E/Gamma trigger objects")
    input_group.add_argument("--input-dir", "-d",
                           help="Directory containing ROOT files to process")
    input_group.add_argument("--input-pattern", "-p",
                           help="Pattern to match ROOT files (e.g., '*.root')")
    
    parser.add_argument("--output", "-o", 
                       required=True,
                       help="Output ROOT file for debug ntuples")
    parser.add_argument("--max-events", "-n", 
                       type=int, default=10,
                       help="Maximum number of events to process (default: 10)")
    parser.add_argument("--verbose", "-v",
                       action="store_true",
                       help="Enable verbose output")
    parser.add_argument("--collection-type", "-c",
                       choices=["seeded", "unseeded"],
                       default="seeded",
                       help="Type of Egamma collection: seeded or unseeded (default: seeded)")

    args = parser.parse_args()

    # Set collection parameters based on type
    if args.collection_type == "unseeded":
        collection_label_suffix = "Unseeded"
        variable_suffix = "Unseeded"
    else:  # seeded
        collection_label_suffix = ""
        variable_suffix = ""

    print(f"📋 Collection type: {args.collection_type}")
    if args.collection_type == "unseeded":
        print(f"   Label: ('hltEgammaHLTExtra', '{collection_label_suffix}', 'MYHLT')")
        print(f"   Variables: *{variable_suffix}* (with Unseeded suffix)")
    else:
        print(f"   Label: ('hltEgammaHLTExtra', '{collection_label_suffix}', 'MYHLT')")
        print(f"   Variables: *{variable_suffix}* (without suffix)")

    # Determine input files
    input_files = []
    if args.input_file:
        input_files = [args.input_file]
    elif args.input_dir:
        # Handle EOS paths better
        if "eos" in args.input_dir:
            # Use shell expansion for EOS paths
            import subprocess
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
            import subprocess
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
    
    # Sort files for consistent processing order
    input_files.sort()
    
    output_file = args.output
    max_events = args.max_events
    verbose = args.verbose
    
    print(f"📁 Found {len(input_files)} input files:")
    for f in input_files:
        print(f"   {f}")
    print(f"💾 Output will be saved to: {output_file}")
    print(f"⚡ Processing up to {max_events} events")
    if verbose:
        print("🔍 Verbose mode enabled")
    
    # Create handles for the collections
    egtrigobjs_handle = Handle("std::vector<trigger::EgammaObject>")
    #egtrigobjs_label = ("hltEgammaHLTExtra", "", "MYHLT")
    egtrigobjs_label = ("hltEgammaHLTExtra", collection_label_suffix, "MYHLT")

    # Define variable name patterns based on collection type
    cluster_shape_prefix = f"hltEgammaClusterShape{variable_suffix}"
    ecal_isol_prefix = f"hltEgammaEcalPFClusterIso{variable_suffix}"
    hcal_isol_prefix = f"hltEgammaHcalPFClusterIso{variable_suffix}"
    hgcal_isol_prefix = f"hltEgammaHGCalPFClusterIso{variable_suffix}"
    ele_gsf_track_prefix = f"hltEgammaEleGsfTrackIso{variable_suffix}"
    gsf_track_vars_prefix = f"hltEgammaGsfTrackVars{variable_suffix}"
    pixel_match_prefix = f"hltEgammaPixelMatchVars{variable_suffix}"
    hgcal_id_prefix = f"hltEgammaHGCALIDVars{variable_suffix}"
    hovere_prefix = f"hltEgammaHoverE{variable_suffix}"
    ele_l1_trk_iso_prefix = f"hltEgammaEleL1TrkIso{variable_suffix}"
    best_gsf_track_prefix = f"hltEgammaBestGsfTrackVars{variable_suffix}"
    
    # Create output file and tree
    out_file = ROOT.TFile(output_file, "RECREATE")
    tree = ROOT.TTree("egHLTTree", "EGamma Tree")
    
    # Create variables for the tree
    run = ROOT.std.vector("int")()
    lumi = ROOT.std.vector("int")()
    event = ROOT.std.vector("unsigned int")()
    
    # E/Gamma object variables
    eg_et = ROOT.std.vector("float")()
    eg_energy = ROOT.std.vector("float")()
    eg_eta = ROOT.std.vector("float")()
    eg_phi = ROOT.std.vector("float")()
    eg_rawEnergy = ROOT.std.vector("float")()
    eg_nrClus = ROOT.std.vector("int")()
    eg_phiWidth = ROOT.std.vector("float")()
    eg_seedId = ROOT.std.vector("unsigned int")()
    eg_seedDet = ROOT.std.vector("int")()
    eg_sigmaIEtaIEta = ROOT.std.vector("float")()
    eg_sigmaIPhiIPhi = ROOT.std.vector("float")()
    
    # HLT Isolation variables
    eg_ecalPFIsol_default = ROOT.std.vector("float")()
    eg_hcalPFIsol_default = ROOT.std.vector("float")()
    eg_trkIsolV0_default = ROOT.std.vector("float")()
    
    # Track variables
    eg_trkChi2_default = ROOT.std.vector("float")()
    eg_trkMissHits = ROOT.std.vector("int")()
    eg_trkValidHits = ROOT.std.vector("int")()
    eg_invESeedInvP = ROOT.std.vector("float")()
    eg_invEInvP = ROOT.std.vector("float")()
    eg_trkDEta = ROOT.std.vector("float")()
    eg_trkDEtaSeed = ROOT.std.vector("float")()
    eg_trkDPhi = ROOT.std.vector("float")()
    eg_trkNrLayerIT = ROOT.std.vector("int")()
        
    # Pixel match and other variables
    eg_pms2_default = ROOT.std.vector("float")()
    eg_hcalHForHoverE = ROOT.std.vector("float")()
    eg_l1TrkIsoCMSSW = ROOT.std.vector("float")()
    eg_bestTrkChi2 = ROOT.std.vector("float")()
    eg_bestTrkDEta = ROOT.std.vector("float")()
    eg_bestTrkDEtaSeed = ROOT.std.vector("float")()
    eg_bestTrkDPhi = ROOT.std.vector("float")()
    eg_bestTrkMissHits = ROOT.std.vector("int")()
    eg_bestTrkNrLayerIT = ROOT.std.vector("int")()
    eg_bestTrkESeedInvP = ROOT.std.vector("float")()
    eg_bestTrkInvEInvP = ROOT.std.vector("float")()
    eg_bestTrkValidHits = ROOT.std.vector("int")()
        
    # Legacy variables (keeping for compatibility)
    eg_ecalPFIsol = ROOT.std.vector("float")()
    eg_hcalPFIsol = ROOT.std.vector("float")()
    
    # Collection info
    collection_name = ROOT.std.vector("string")()
    nr_objects = ROOT.std.vector("int")()
    
    # Create branches
    tree.Branch("run", run)
    tree.Branch("lumi", lumi)
    tree.Branch("event", event)
    tree.Branch("eg_et", eg_et)
    tree.Branch("eg_energy", eg_energy)
    tree.Branch("eg_eta", eg_eta)
    tree.Branch("eg_phi", eg_phi)
    tree.Branch("eg_rawEnergy", eg_rawEnergy)
    tree.Branch("eg_nrClus", eg_nrClus)
    tree.Branch("eg_phiWidth", eg_phiWidth)
    tree.Branch("eg_seedId", eg_seedId)
    tree.Branch("eg_seedDet", eg_seedDet)
    tree.Branch("eg_sigmaIEtaIEta", eg_sigmaIEtaIEta)
    tree.Branch("eg_sigmaIPhiIPhi", eg_sigmaIPhiIPhi)
    
    # HLT Isolation branches
    tree.Branch("eg_ecalPFIsol_default", eg_ecalPFIsol_default)
    tree.Branch("eg_hcalPFIsol_default", eg_hcalPFIsol_default)
    tree.Branch("eg_trkIsolV0_default", eg_trkIsolV0_default)
    
    # Track variable branches
    tree.Branch("eg_trkChi2_default", eg_trkChi2_default)
    tree.Branch("eg_trkMissHits", eg_trkMissHits)
    tree.Branch("eg_trkValidHits", eg_trkValidHits)
    tree.Branch("eg_invESeedInvP", eg_invESeedInvP)
    tree.Branch("eg_invEInvP", eg_invEInvP)
    tree.Branch("eg_trkDEta", eg_trkDEta)
    tree.Branch("eg_trkDEtaSeed", eg_trkDEtaSeed)
    tree.Branch("eg_trkDPhi", eg_trkDPhi)
    tree.Branch("eg_trkNrLayerIT", eg_trkNrLayerIT)
        
    # Pixel match and other variable branches
    tree.Branch("eg_pms2_default", eg_pms2_default)
    tree.Branch("eg_hcalHForHoverE", eg_hcalHForHoverE)
    tree.Branch("eg_l1TrkIsoCMSSW", eg_l1TrkIsoCMSSW)
    tree.Branch("eg_bestTrkChi2", eg_bestTrkChi2)
    tree.Branch("eg_bestTrkDEta", eg_bestTrkDEta)
    tree.Branch("eg_bestTrkDEtaSeed", eg_bestTrkDEtaSeed)
    tree.Branch("eg_bestTrkDPhi", eg_bestTrkDPhi)
    tree.Branch("eg_bestTrkMissHits", eg_bestTrkMissHits)
    tree.Branch("eg_bestTrkNrLayerIT", eg_bestTrkNrLayerIT)
    tree.Branch("eg_bestTrkESeedInvP", eg_bestTrkESeedInvP)
    tree.Branch("eg_bestTrkInvEInvP", eg_bestTrkInvEInvP)
    tree.Branch("eg_bestTrkValidHits", eg_bestTrkValidHits)
    
    # Legacy branches (keeping for compatibility)
    tree.Branch("eg_ecalPFIsol", eg_ecalPFIsol)
    tree.Branch("eg_hcalPFIsol", eg_hcalPFIsol)
    tree.Branch("collection_name", collection_name)
    tree.Branch("nr_objects", nr_objects)
    
    # Open events
    events = Events(input_files)
    
    print("Processing events...")
    for i, evt in enumerate(events):
        if i >= max_events:  # Process up to max_events
            break
            
        print(f"\n=== Event {i} ===")
        print(f"Run: {evt.eventAuxiliary().run()}, Lumi: {evt.eventAuxiliary().luminosityBlock()}, Event: {evt.eventAuxiliary().event()}")
                
        # Clear vectors for this event
        run.clear()
        lumi.clear()
        event.clear()
        eg_et.clear()
        eg_energy.clear()
        eg_eta.clear()
        eg_phi.clear()
        eg_rawEnergy.clear()
        eg_nrClus.clear()
        eg_phiWidth.clear()
        eg_seedId.clear()
        eg_seedDet.clear()
        eg_sigmaIEtaIEta.clear()
        eg_sigmaIPhiIPhi.clear()
        
        # Clear HLT Isolation vectors
        eg_ecalPFIsol_default.clear()
        eg_hcalPFIsol_default.clear()
        eg_trkIsolV0_default.clear()
        
        # Clear Track variable vectors
        eg_trkChi2_default.clear()
        eg_trkMissHits.clear()
        eg_trkValidHits.clear()
        eg_invESeedInvP.clear()
        eg_invEInvP.clear()
        eg_trkDEta.clear()
        eg_trkDEtaSeed.clear()
        eg_trkDPhi.clear()
        eg_trkNrLayerIT.clear()
                
        # Clear Pixel match and other variable vectors
        eg_pms2_default.clear()
        eg_hcalHForHoverE.clear()
        eg_l1TrkIsoCMSSW.clear()
        eg_bestTrkChi2.clear()
        eg_bestTrkDEta.clear()
        eg_bestTrkDEtaSeed.clear()
        eg_bestTrkDPhi.clear()
        eg_bestTrkMissHits.clear()
        eg_bestTrkNrLayerIT.clear()
        eg_bestTrkESeedInvP.clear()
        eg_bestTrkInvEInvP.clear()
        eg_bestTrkValidHits.clear()
        
        # Clear Legacy vectors
        eg_ecalPFIsol.clear()
        eg_hcalPFIsol.clear()
        collection_name.clear()
        nr_objects.clear()
        
        # Add event info
        run.push_back(evt.eventAuxiliary().run())
        lumi.push_back(evt.eventAuxiliary().luminosityBlock())
        event.push_back(evt.eventAuxiliary().event())
        
        try:
            evt.getByLabel(egtrigobjs_label, egtrigobjs_handle)
            if egtrigobjs_handle.isValid():
                egobjs = egtrigobjs_handle.product()
                print(f"  ✓ Found {egobjs.size()} objects")

                if egobjs.size() > 0:
                    # Store collection info
                    nr_objects.push_back(egobjs.size())

                    # Process each object
                    for j, obj in enumerate(egobjs):

                        # Basic properties
                        eg_et.push_back(obj.et())
                        eg_energy.push_back(obj.energy())
                        eg_eta.push_back(obj.eta())
                        eg_phi.push_back(obj.phi())

                        # SuperCluster properties
                        eg_nrClus.push_back(obj.superCluster().clusters().size())
                        eg_rawEnergy.push_back(obj.superCluster().rawEnergy())
                        eg_phiWidth.push_back(obj.superCluster().phiWidth())
                        eg_seedId.push_back(obj.superCluster().seed().seed().rawId())
                        eg_seedDet.push_back(obj.superCluster().seed().seed().det())                                                                

                        # HLT variables - try different naming conventions
                        eg_sigmaIEtaIEta.push_back(obj.var(f"{cluster_shape_prefix}_sigmaIEtaIEta5x5",0))
                        eg_sigmaIPhiIPhi.push_back(obj.var(f"{cluster_shape_prefix}_sigmaIPhiIPhi5x5",0))
                        eg_ecalPFIsol_default.push_back(obj.var(f"{ecal_isol_prefix}",0))
                        eg_hcalPFIsol_default.push_back(obj.var(f"{hcal_isol_prefix}",0))
                        eg_trkIsolV0_default.push_back(obj.var(f"{ele_gsf_track_prefix}",0))
                        eg_trkChi2_default.push_back(obj.var(f"{gsf_track_vars_prefix}_Chi2",0))
                        #eg_trkMissHits.push_back(obj.var(f"{gsf_track_vars_prefix}_MissingHits",0))
                        #eg_trkValidHits.push_back(obj.var(f"{gsf_track_vars_prefix}_ValidHits",0))
                        eg_invESeedInvP.push_back(obj.var(f"{gsf_track_vars_prefix}_OneOESeedMinusOneOP",0))
                        eg_invEInvP.push_back(obj.var(f"{gsf_track_vars_prefix}_OneOESuperMinusOneOP",0))
                        eg_trkDEta.push_back(obj.var(f"{gsf_track_vars_prefix}_Deta",0))
                        eg_trkDEtaSeed.push_back(obj.var(f"{gsf_track_vars_prefix}_DetaSeed",0))
                        eg_trkDPhi.push_back(obj.var(f"{gsf_track_vars_prefix}_Dphi",0))
                        #eg_trkNrLayerIT.push_back(obj.var(f"{gsf_track_vars_prefix}_NLayerIT",0))
                        #eg_rVar.push_back(obj.var(f"{hgcal_id_prefix}_rVar",0))

                        eg_pms2_default.push_back(obj.var(f"{pixel_match_prefix}_s2",0))
                        eg_hcalHForHoverE.push_back(obj.var(f"{hgcal_id_prefix}_hForHOverE",0))

#                        eg_l1TrkIsoCMSSW.push_back(obj.var(f"{hovere_prefix}",0))
                        eg_bestTrkChi2.push_back(obj.var(f"{ele_l1_trk_iso_prefix}",0))
                        eg_bestTrkDEta.push_back(obj.var(f"{best_gsf_track_prefix}_Chi2",0))
                        eg_bestTrkDEtaSeed.push_back(obj.var(f"{best_gsf_track_prefix}_Deta",0))
                        eg_bestTrkDPhi.push_back(obj.var(f"{best_gsf_track_prefix}_DetaSeed",0))
                        #eg_bestTrkMissHits.push_back(obj.var(f"{best_gsf_track_prefix}_Dphi",0))
                        #eg_bestTrkNrLayerIT.push_back(obj.var(f"{best_gsf_track_prefix}_MissingHits",0))
                        eg_bestTrkESeedInvP.push_back(obj.var(f"{best_gsf_track_prefix}_NLayerIT",0))
                        eg_bestTrkInvEInvP.push_back(obj.var(f"{best_gsf_track_prefix}_OneOESeedMinusOneOP",0))
                        #eg_bestTrkValidHits.push_back(obj.var(f"{best_gsf_track_prefix}_OneOESuperMinusOneOP",0))

                    # Fill tree for this collection
                    tree.Fill()

            else:
                print(f"  ✗ Invalid handle for {label}")

        except Exception as e:
            print(f"  ✗ Error accessing {label}: {e}")
    
    # Write and close
    out_file.Write()
    out_file.Close()
    print(f"\n✅ Debug ntuple saved to: {output_file}")
    print("You can open this file in ROOT to inspect the variables:")

if __name__ == "__main__":
    main() 
