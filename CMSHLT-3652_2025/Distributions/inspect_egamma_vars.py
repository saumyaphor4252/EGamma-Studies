#!/usr/bin/env python3

import ROOT
from DataFormats.FWLite import Events, Handle
import argparse
import glob
import os
import sys

def inspect_egamma_object(obj, verbose=False):
    """
    Inspect an EgammaObject and print available variables/methods
    """
    print("\n=== Inspecting EgammaObject ===")

    # First, try to get basic properties
    print("Basic properties:")
    try:
        print(f"  pt(): {obj.pt()}")
        print(f"  et(): {obj.et()}")
        print(f"  energy(): {obj.energy()}")
        print(f"  eta(): {obj.eta()}")
        print(f"  phi(): {obj.phi()}")
    except Exception as e:
        print(f"  Error accessing basic properties: {e}")

    # Check if it has a superCluster
    print("\nSuperCluster properties:")
    try:
        sc = obj.superCluster()
        print(f"  superCluster().rawEnergy(): {sc.rawEnergy()}")
        print(f"  superCluster().phiWidth(): {sc.phiWidth()}")
        print(f"  superCluster().etaWidth(): {sc.etaWidth()}")

        # Check clusters
        clusters = sc.clusters()
        print(f"  superCluster().clusters().size(): {clusters.size()}")

        # Check seed
        seed = sc.seed()
        print(f"  superCluster().seed().energy(): {seed.energy()}")
        seed_crystal = seed.seed()
        print(f"  superCluster().seed().seed().rawId(): {seed_crystal.rawId()}")
        print(f"  superCluster().seed().seed().det(): {seed_crystal.det()}")

    except Exception as e:
        print(f"  Error accessing superCluster: {e}")

    # Check what variables are available in this EgammaObject
    print("\nChecking available variables in collection:")

    try:
        var_names = obj.varNames()
        num_vars = var_names.size()
        print(f"  ✓ Found {num_vars} variables in this object")

        if verbose:
            print("  Variable names and values:")
            for i in range(num_vars):
                var_name = var_names[i]
                try:
                    value = obj.var(var_name, 0)
                    print(f"    {var_name}: {value}")
                except Exception as e:
                    print(f"    {var_name}: ERROR - {e}")
        else:
            # Show first few variable names
            print("  First few variables:")
            for i in range(min(5, num_vars)):
                print(f"    {var_names[i]}")
            if num_vars > 5:
                print(f"    ... and {num_vars - 5} more")

        return [var_names[i] for i in range(num_vars)]

    except Exception as e:
        print(f"  ✗ Could not access variables: {e}")
        print("  💡 Check if your collection label is correct")
        return []

    # Try to access some methods directly
    print("\nTrying direct method access:")
    methods_to_try = ['hasPixelMatch', 'hasMatchedElectron', 'isIsolated', 'charge']
    for method in methods_to_try:
        try:
            result = getattr(obj, method)()
            print(f"  ✓ obj.{method}(): {result}")
        except Exception as e:
            print(f"  ✗ obj.{method}(): {e}")

    return available_vars

def main():
    parser = argparse.ArgumentParser(
        description="Inspect EgammaObject collections to see available trigger variables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script checks what variables are available in your EgammaObject collection
using the CMSSW varNames() method.

Examples:
  python3 inspect_egamma_vars.py input.root
  python3 inspect_egamma_vars.py input.root --verbose
  python3 inspect_egamma_vars.py --collection-type seeded input.root
  python3 inspect_egamma_vars.py --input-dir /path/to/files/ --max-events 5
        """
    )

    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("input_file", nargs='?',
                           help="Input ROOT file containing E/Gamma trigger objects")
    input_group.add_argument("--input-dir", "-d",
                           help="Directory containing ROOT files to process")
    input_group.add_argument("--input-pattern", "-p",
                           help="Pattern to match ROOT files (e.g., '*.root')")

    parser.add_argument("--max-events", "-n",
                       type=int, default=1,
                       help="Maximum number of events to process (default: 1)")
    parser.add_argument("--verbose", "-v",
                       action="store_true",
                       help="Show all variable names and values instead of just the first few")
    parser.add_argument("--collection-type", "-c",
                       choices=["seeded", "unseeded"],
                       default="unseeded",
                       help="Type of Egamma collection: seeded or unseeded (default: unseeded)")

    args = parser.parse_args()

    # Set collection label based on type
    if args.collection_type == "unseeded":
        collection_label_suffix = "Unseeded"
    else:  # seeded
        collection_label_suffix = ""

    print(f"📋 Inspecting {args.collection_type} collection")
    print(f"   Label: ('hltEgammaHLTExtra', '{collection_label_suffix}', 'MYHLT')")

    # Determine input files
    input_files = []
    if args.input_file:
        input_files = [args.input_file]
    elif args.input_dir:
        if "eos" in args.input_dir:
            import subprocess
            try:
                result = subprocess.run(f"ls {args.input_dir}/*.root",
                                     capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    input_files = result.stdout.strip().split('\n')
                else:
                    input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
            except:
                input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
        else:
            input_files = glob.glob(os.path.join(args.input_dir, "*.root"))
    elif args.input_pattern:
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
        return

    print(f"📁 Found {len(input_files)} input files:")
    for f in input_files:
        print(f"   {f}")

    # Create handles for the collections
    egtrigobjs_handle = Handle("std::vector<trigger::EgammaObject>")
    egtrigobjs_label = ("hltEgammaHLTExtra", collection_label_suffix, "MYHLT")

    # Open events
    events = Events(input_files)

    print(f"\n🔍 Processing up to {args.max_events} events for inspection...")

    event_count = 0
    for i, evt in enumerate(events):
        if event_count >= args.max_events:
            break

        print(f"\n=== Event {i} ===")
        print(f"Run: {evt.eventAuxiliary().run()}, Lumi: {evt.eventAuxiliary().luminosityBlock()}, Event: {evt.eventAuxiliary().event()}")

        try:
            evt.getByLabel(egtrigobjs_label, egtrigobjs_handle)
            if egtrigobjs_handle.isValid():
                egobjs = egtrigobjs_handle.product()
                print(f"✓ Found {egobjs.size()} objects")

                if egobjs.size() > 0:
                    # Inspect first object
                    obj = egobjs[0]
                    available_vars = inspect_egamma_object(obj, args.verbose)

                    if len(available_vars) > 0:
                        print(f"\n📋 Summary of available variables ({len(available_vars)} found):")
                        for var in available_vars:
                            print(f"   {var}")

                    event_count += 1

            else:
                print(f"✗ Invalid handle for {egtrigobjs_label}")

        except Exception as e:
            print(f"✗ Error accessing {egtrigobjs_label}: {e}")

    print("\n✅ Inspection complete!")

if __name__ == "__main__":
    main()
