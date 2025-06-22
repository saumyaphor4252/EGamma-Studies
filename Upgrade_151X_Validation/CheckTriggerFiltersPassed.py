#!/usr/bin/env python

from DataFormats.FWLite import Events, Handle
import ROOT
from ROOT import TFile
import argparse
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_events(events, max_events=100):
    """Process events and print trigger filter information.
    
    Args:
        events: Events to process
        max_events: Maximum number of events to process
    """
    # Initialize handles
    hlt_handle, hlt_label = Handle("edm::TriggerResults"), ("TriggerResults", "", "HLT")
    triggerObjects_handle, triggerObjects_label = Handle("vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
    
    for event_nr, event in enumerate(events):
        if event_nr >= max_events:
            break
            
        print(f"\n{'='*50}")
        print(f"🎯 Processing Event {event_nr}")
        print(f"{'='*50}")
        
        # Get event data
        try:
            event.getByLabel(hlt_label, hlt_handle)
            event.getByLabel(triggerObjects_label, triggerObjects_handle)
        except Exception as e:
            logger.error(f"Error getting event data: {str(e)}")
            continue
            
        hlts = hlt_handle.product()
        trigger_objects = triggerObjects_handle.product()
        
        # Get trigger names from the trigger results
        trigger_names = event.object().triggerNames(hlts)
        
        # Print trigger paths and their status
        print("\n🔍 Trigger Paths Status:")
        for i in range(hlts.size()):
            path_name = trigger_names.triggerName(i)
            path_status = hlts.accept(i)
            if path_status:  # Only print paths that passed
                print(f"   ✅ {path_name}")
        
        # Process trigger objects
        print("\n🔍 Trigger Objects and their Filters:")
        for i, obj in enumerate(trigger_objects):
            # Unpack filter labels and path names
            obj.unpackFilterLabels(event.object(), hlts)
            obj.unpackPathNames(trigger_names)
            
            # Get filter labels and convert bytes to strings
            filter_labels = [label.decode('utf-8') if isinstance(label, bytes) else str(label) 
                           for label in obj.filterLabels()]
            
            if filter_labels:  # Only print objects with filter labels
                print(f"\n   📌 Trigger Object {i+1}:")
                print(f"      Filter Labels: {filter_labels}")
                print(f"      Path Names: {[path for path in obj.pathNames()]}")
                print(f"      pT: {obj.pt():.2f}, η: {obj.eta():.2f}, φ: {obj.phi():.2f}")

def main():
    parser = argparse.ArgumentParser(description='Check trigger filters passed in events')
    parser.add_argument('in_filename', nargs="+", help='input filename(s)')
    parser.add_argument("-n", "--max-events", type=int, default=100, 
                       help="Maximum number of events to process (default: 100)")
    
    args = parser.parse_args()
    
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
    
    # Process events
    events = Events(valid_files)
    process_events(events, args.max_events)

if __name__ == "__main__":
    main() 