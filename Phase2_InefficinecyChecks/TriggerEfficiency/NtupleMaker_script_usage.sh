#!/bin/bash

# Example usage script for the memory-efficient lastFilterEfficiency_Upgrade.py
# This demonstrates how to run the updated script that processes files individually

echo "🚀 Example Usage for Memory-Efficient Processing"
echo "=============================================="

# Example 1: Process files from a directory
echo "📂 Example 1: Process all ROOT files in a directory"
echo "python3 lastFilterEfficiency_Upgrade.py --input-dir /path/to/input/files/ -o final_merged_output.root"
echo ""

# Example 2: Process files matching a pattern
echo "🔍 Example 2: Process files matching a pattern"
echo "python3 lastFilterEfficiency_Upgrade.py --input-pattern '/eos/cms/store/user/*/my_files_*.root' -o final_merged_output.root"
echo ""

# Example 3: Process a single file
echo "📄 Example 3: Process a single file"
echo "python3 lastFilterEfficiency_Upgrade.py --input-file /path/to/single/file.root -o final_merged_output.root"
echo ""

# Example 4: Custom output directory and debugging
echo "🔧 Example 4: Custom output directory with debugging"
echo "python3 lastFilterEfficiency_Upgrade.py --input-dir /path/to/input/files/ -o final_output.root --output-dir MyOutputs --debug"
echo ""

# Example 5: Limit number of events for testing
echo "⚡ Example 5: Process limited events for testing"
echo "python3 lastFilterEfficiency_Upgrade.py --input-dir /path/to/input/files/ -o test_output.root -n 1000"
echo ""

echo "📝 Key Features of the Updated Script:"
echo "   • Processes files individually to avoid memory issues"
echo "   • Creates OutputNtuples_Reference directory (or custom with --output-dir)"
echo "   • Generates unique output files for each input file"
echo "   • Automatically creates merge_outputs.sh script for final hadd"
echo "   • Provides detailed progress and summary information"
echo ""

echo "🔗 After processing, merge files with:"
echo "   ./merge_outputs.sh"
echo "   OR manually:"
echo "   hadd final_output.root OutputNtuples_Reference/*.root"
