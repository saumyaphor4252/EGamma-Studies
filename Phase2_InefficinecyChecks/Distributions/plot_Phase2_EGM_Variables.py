#!/usr/bin/env python3
"""
🎯 ROOT Histogram Comparison Script for Multiple EGM Variables 🎯

This script takes multiple ROOT files and plots various EGM variables
as normalized histograms with log scale y-axis.

Usage: python plot_Phase2_EGM_Variables.py file1.root file2.root [file3.root ...] [output_name] [legend1] [legend2] [legend3] ...
"""

import sys
import os
import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gROOT, TPaveText, TLatex
import argparse

def setup_root_style():
    """Setup ROOT plot style for beautiful histograms"""
    gROOT.SetBatch(True)  # Run in batch mode for saving
    gStyle.SetOptStat(1111)  # Show all statistics
    gStyle.SetPalette(55)    # Beautiful color palette
    gStyle.SetTitleSize(0.04, "xyz")
    gStyle.SetLabelSize(0.03, "xyz")
    gStyle.SetTitleOffset(1.2, "y")
    gStyle.SetTitleOffset(1.1, "x")
    gStyle.SetPadLeftMargin(0.12)
    gStyle.SetPadRightMargin(0.05)
    gStyle.SetPadTopMargin(0.05)
    gStyle.SetPadBottomMargin(0.12)

def plot_egm_variables(file_paths, output_name="egm_variables_comparison", legends=None):
    """Plot multiple variables from multiple ROOT files, creating separate plots for each"""
    
    # Set up default legends if not provided
    if legends is None or len(legends) == 0:
        legends = [f"File {i+1}" for i in range(len(file_paths))]
    elif len(legends) < len(file_paths):
        # Extend legends if not enough provided
        legends.extend([f"File {i+1}" for i in range(len(legends), len(file_paths))])
    
    print(f"🎯 Starting variable comparison plots! 🎯")
    print(f"📁 Processing {len(file_paths)} files:")
    for i, (file_path, legend) in enumerate(zip(file_paths, legends)):
        print(f"   {i+1}. {file_path} (Legend: {legend})")
    print(f"📂 Output base name: {output_name}")
    print(f"🎨 Color scheme: Blue, Red, Green, Magenta, Orange, Cyan, Yellow, Pink, Violet, Teal")
    print("=" * 60)
    
    # Define variables to plot with their binning
    variables = {
        "eg_hcalHForHoverE": {"bins": 25, "xmin": 0.0, "xmax": 1, "title": "HCal H/E", "xlabel": "H/E"},
        "eg_et": {"bins": 100, "xmin": 0.0, "xmax": 3000.0, "title": "E_{T}", "xlabel": "E_{T} [GeV]"},
        "eg_energy": {"bins": 25, "xmin": 0.0, "xmax": 5000.0, "title": "Energy", "xlabel": "Energy [GeV]"},
        "eg_rawEnergy": {"bins": 25, "xmin": 0.0, "xmax": 5000.0, "title": "Raw Energy", "xlabel": "Raw Energy [GeV]"},
        "eg_nrClus": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Number of Clusters", "xlabel": "Number of Clusters"},
        "eg_hgcaliso_layerclus": {"bins": 12, "xmin": 0.0, "xmax": 12.0, "title": "HgCal Isolated Clusters", "xlabel": "Layer Number"},
        "eg_phi": {"bins": 32, "xmin": -3.2, "xmax": 3.2, "title": "#phi", "xlabel": "#phi [rad]"},
        "eg_eta": {"bins": 30, "xmin": -3.0, "xmax": 3.0, "title": "#eta", "xlabel": "#eta"},
        "eg_sigmaIEtaIEta": {"bins": 50, "xmin": 0.0, "xmax": 0.03, "title": "#sigma_{i#eta i#eta}", "xlabel": "#sigma_{i#eta i#eta}"},
        "eg_sigma2uu": {"bins": 50, "xmin": 0.0, "xmax": 10.0, "title": "#sigma_{2uu}", "xlabel": "#sigma_{2uu}"},
        "eg_sigma2vv": {"bins": 50, "xmin": 0.0, "xmax": 3.0, "title": "#sigma_{2vv}", "xlabel": "#sigma_{2vv}"},
        "eg_sigma2ww": {"bins": 50, "xmin": 0.0, "xmax": 200.0, "title": "#sigma_{2ww}", "xlabel": "#sigma_{2ww}"},
        "eg_sigma2xx": {"bins": 50, "xmin": 0.0, "xmax": 10.0, "title": "#sigma_{2xx}", "xlabel": "#sigma_{2xx}"},
        "eg_sigma2xy": {"bins": 50, "xmin": -5.0, "xmax": 5.0, "title": "#sigma_{2xy}", "xlabel": "#sigma_{2xy}"},
        "eg_sigma2yy": {"bins": 50, "xmin": 0.0, "xmax": 10.0, "title": "#sigma_{2yy}", "xlabel": "#sigma_{2yy}"},
        "eg_sigma2yz": {"bins": 50, "xmin": -20.0, "xmax": 20.0, "title": "#sigma_{2yz}", "xlabel": "#sigma_{2yz}"},
        "eg_sigma2zx": {"bins": 50, "xmin": -20.0, "xmax": 20.0, "title": "#sigma_{2zx}", "xlabel": "#sigma_{2zx}"},
        "eg_sigma2zz": {"bins": 50, "xmin": 0.0, "xmax": 100.0, "title": "#sigma_{2zz}", "xlabel": "#sigma_{2zz}"},
        "eg_invEInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.01, "title": "1/E - 1/p", "xlabel": "1/E - 1/p"},
        "eg_invESeedInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.1, "title": "1/E_{seed} - 1/p", "xlabel": "1/E_{seed} - 1/p"},
        "eg_trkDEta": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Track}", "xlabel": "#Delta#eta_{Track}"},
        #"eg_trkDEtaSeed": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Track}^{Seed}", "xlabel": "#Delta#eta_{Track}^{Seed}"},
        "eg_ecalPFIsol_default": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "ECAL PF Isolation", "xlabel": "ECAL PF Isolation [GeV]"},
        "eg_hcalPFIsol_default": {"bins": 25, "xmin": 0.0, "xmax": 100.0, "title": "HCAL PF Isolation", "xlabel": "HCAL PF Isolation [GeV]"},
        "eg_hgcalPFIsol_default": {"bins": 25, "xmin": -1.0, "xmax": 1.0, "title": "HgCal PF Isolation", "xlabel": "HgCal PF Isolation"},
        "eg_trkIsolV0_default": {"bins": 50, "xmin": 0.0, "xmax": 0.5, "title": "Track Isolation V0", "xlabel": "Track Isolation V0"},
        "eg_trkChi2_default": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Track #chi^{2}", "xlabel": "Track #chi^{2}"},
        "eg_pms2_default": {"bins": 20, "xmin": 0.0, "xmax": 0.8, "title": "PMS2", "xlabel": "PMS2"},
        "eg_l1TrkIsoCMSSW": {"bins": 20, "xmin": 0.0, "xmax": 200.0, "title": "L1 Track Isolation CMSSW", "xlabel": "L1 Track Isolation CMSSW"}
    }
    
    # Open ROOT files
    try:
        files = []
        trees = []
        
        for i, file_path in enumerate(file_paths):
            file_obj = TFile(file_path, "READ")
            if file_obj.IsZombie():
                print(f"💀 Oops! File {i+1} ({file_path}) is a zombie! Check your file paths!")
                return
            files.append(file_obj)
            
            # Get the egHLTTree from each file
            tree = file_obj.Get("egHLTTree")
            if not tree:
                print(f"🌳 'egHLTTree' not found in file {i+1} ({file_path})!")
                return
            trees.append(tree)
            print(f"🌳 Tree {i+1}: {tree.GetName()} with {tree.GetEntries()} entries")
        
        # Define colors for different files (cycling through a nice palette)
        colors = [ROOT.kBlue, ROOT.kRed, ROOT.kGreen+2, ROOT.kMagenta+2, ROOT.kOrange+2, 
                 ROOT.kCyan+2, ROOT.kYellow+2, ROOT.kPink+2, ROOT.kViolet+2, ROOT.kTeal+2]
        
        # Loop over each variable and create separate plots
        for var_name, var_config in variables.items():
            print(f"\n📊 Creating plot for: {var_name}")
            print(f"   Bins: {var_config['bins']}, Range: {var_config['xmin']} to {var_config['xmax']}")
            
            # Create histograms for this variable for all files
            histograms = []
            for i, tree in enumerate(trees):
                hist = TH1F(f"hist_{i}_{var_name}", "", var_config['bins'], var_config['xmin'], var_config['xmax'])
                tree.Draw(f"{var_name}>>hist_{i}_{var_name}", "", "goff")
                print(f"   File {i+1}: {hist.GetEntries()} entries")
                
                # Normalize histogram to 1
                if hist.GetEntries() > 0:
                    hist.Scale(1.0 / hist.GetEntries())
                
                # Style the histogram
                hist.SetLineColor(colors[i % len(colors)])
                hist.SetLineWidth(2)
                hist.SetFillColor(0)
                hist.SetFillStyle(3001)
                hist.SetStats(0)  # Hide statistics box
                
                histograms.append(hist)
            
            # Set up axis labels for the first histogram (they'll be the same for all)
            if histograms:
                histograms[0].GetXaxis().SetTitle(var_config['xlabel'])
                histograms[0].GetXaxis().SetTitleSize(0.05)
                histograms[0].GetXaxis().SetLabelSize(0.04)
                histograms[0].GetXaxis().SetTitleOffset(1.1)
                histograms[0].GetYaxis().SetTitle("a.u.")
                histograms[0].GetYaxis().SetLabelSize(0.045)
                histograms[0].GetYaxis().SetTitleSize(0.06)
                histograms[0].GetYaxis().SetTitleOffset(0.8)
            
            # Create canvas and draw - simplified without ratio panel
            canvas = TCanvas(f"canvas_{var_name}", f"{var_config['title']} Comparison", 800, 800)
            canvas.SetLogy(True)
            canvas.SetGridx(True)
            canvas.SetGridy(True)
            
            # Find the maximum to set proper scale
            max_val = max([hist.GetMaximum() for hist in histograms])
            histograms[0].SetMaximum(max_val * 1.5)
            
            # Draw histograms
            for i, hist in enumerate(histograms):
                if i == 0:
                    hist.Draw("")
                else:
                    hist.Draw("same")
            
            # Add legend with custom labels
            legend = TLegend(0.62, 0.75, 0.93, 0.89)
            legend.SetBorderSize(1)
            legend.SetLineColor(1)
            legend.SetLineStyle(1)
            legend.SetLineWidth(1)
            legend.SetFillColor(0)
            legend.SetFillStyle(1001)
            legend.SetTextSize(0.045)
            
            # Add entries for all histograms
            for i, (hist, legend_label) in enumerate(zip(histograms, legends)):
                legend.AddEntry(hist, legend_label, "lpf")
            legend.Draw()

            # Add CMS labels
            tex = TLatex()
            tex.SetTextFont(42)
            tex.SetTextSize(0.04)
            tex.SetLineWidth(2)
            tex.DrawLatexNDC(0.7,0.97,"Run4 MC (14 TeV)")
            
            tex_cms = TLatex()
            tex_cms.SetTextSize(0.06)
            tex_cms.SetTextFont(42)
            tex_cms.DrawLatexNDC(0.18, 0.85, "#bf{CMS}")
            
            tex_private = TLatex()
            tex_private.SetTextSize(0.045)
            tex_private.SetTextFont(52)
            tex_private.DrawLatexNDC(0.18, 0.8, "#it{Private Work}")
            
            
            # Save the plot for this variable
            var_output_name = f"{output_name}_{var_name.replace('eg_', '')}"
            output_path = f"{var_output_name}.png"
            canvas.SaveAs(output_path)
            print(f"   💾 Saved: {output_path}")
                        
            # Clean up canvas and histograms for this variable
            canvas.Close()
            for hist in histograms:
                hist.Delete()
            
            print(f"   ✅ Completed plot for {var_name}")
        
        print("\n" + "=" * 60)
        print("🎉 All variable comparisons complete! 🎉")
        print(f"📁 Check out your separate plots in the current directory!")
        
    except Exception as e:
        print(f"💥 Oops! Something went wrong: {e}")
    
    finally:
        # Clean up
        if 'files' in locals():
            for file_obj in files:
                file_obj.Close()

def main():
    """Main function to parse arguments and run the comparison"""
    
    # Show help if no arguments or --help
    if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
        print("""
🎯 Plot multiple EGM variables comparison from multiple ROOT files

Usage:
  python plot_Phase2_EGM_Variables.py file1.root file2.root [file3.root ...] [output_name] [legend1] [legend2] ...

Examples:
  python plot_Phase2_EGM_Variables.py file1.root file2.root file3.root
  python plot_Phase2_EGM_Variables.py file1.root file2.root file3.root my_comparison
  python plot_Phase2_EGM_Variables.py file1.root file2.root file3.root my_comparison "Ref" "Target1" "Target2"

Note: 
  - First file will be plotted in BLUE
  - Other files will be plotted in different colors (RED, GREEN, etc.)
  - You can provide up to 10 files with different colors
        """)
        sys.exit(0)
    
    # Parse arguments manually to handle the mixed file/string arguments
    all_args = sys.argv[1:]  # Get all command line arguments except script name
    
    if len(all_args) < 2:
        print("💀 Error: At least 2 ROOT files are required!")
        sys.exit(1)
    
    # Find the first non-file argument (output_name)
    files = []
    output_name = "egm_variables_comparison"
    legends = []
    
    i = 0
    while i < len(all_args):
        arg = all_args[i]
        # Check if it's a file (ends with .root and exists)
        if arg.endswith('.root') and os.path.exists(arg):
            files.append(arg)
            i += 1
        else:
            # This is the output_name
            output_name = arg
            # Everything after this are legends
            legends = all_args[i+1:]
            break
    
    # Check if we have at least 2 files
    if len(files) < 2:
        print("💀 Error: At least 2 ROOT files are required!")
        sys.exit(1)
    
    # Check if files exist (double check)
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"💀 File not found: {file_path}")
            sys.exit(1)
    
    # Setup ROOT style
    setup_root_style()
    
    # Let's plot this! 🚀
    plot_egm_variables(files, output_name, legends)

if __name__ == "__main__":
    main()
