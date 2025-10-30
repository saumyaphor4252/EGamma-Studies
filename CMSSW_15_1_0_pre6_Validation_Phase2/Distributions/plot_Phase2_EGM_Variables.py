#!/usr/bin/env python3
"""
🎯 ROOT Histogram Comparison Script for eg_hcalHForHoverE 🎯

This script takes two ROOT files and plots the eg_hcalHForHoverE branch
as normalized histograms with log scale y-axis.

Usage: python plot_hcal_hovere.py Target.root Reference.root [output_name] [Reference_Legend] [Target_Legend] 
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

def plot_hcal_hovere(file1_path, file2_path, output_name="hcal_hovere_comparison", legend1="Reference", legend2="Target"):
    """Plot multiple variables from two ROOT files, creating separate plots for each"""
    
    print(f"🎯 Starting variable comparison plots! 🎯")
    print(f"📁 File 1: {file1_path} (Legend: {legend1})")
    print(f"📁 File 2: {file2_path} (Legend: {legend2})")
    print(f"📂 Output base name: {output_name}")
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
        file1 = TFile(file1_path, "READ")
        file2 = TFile(file2_path, "READ")
        
        if file1.IsZombie() or file2.IsZombie():
            print("💀 Oops! One of the files is a zombie! Check your file paths!")
            return
        
        # Get the egHLTTree from both files
        tree1 = file1.Get("egHLTTree")
        tree2 = file2.Get("egHLTTree")
        
        if not tree1:
            print("🌳 'egHLTTree' not found in file 1!")
            return
        
        if not tree2:
            print("🌳 'egHLTTree' not found in file 2!")
            return
        
        print(f"🌳 Tree 1: {tree1.GetName()} with {tree1.GetEntries()} entries")
        print(f"🌳 Tree 2: {tree2.GetName()} with {tree2.GetEntries()} entries")
        
        # Loop over each variable and create separate plots
        for var_name, var_config in variables.items():
            print(f"\n📊 Creating plot for: {var_name}")
            print(f"   Bins: {var_config['bins']}, Range: {var_config['xmin']} to {var_config['xmax']}")
            
            # Create histograms for this variable
            hist1 = TH1F(f"hist1_{var_name}", "", var_config['bins'], var_config['xmin'], var_config['xmax'])
            hist2 = TH1F(f"hist2_{var_name}", "", var_config['bins'], var_config['xmin'], var_config['xmax'])
            
            # Draw the branch into histograms
            tree1.Draw(f"{var_name}>>hist1_{var_name}", "", "goff")
            tree2.Draw(f"{var_name}>>hist2_{var_name}", "", "goff")
            
            print(f"   File 1: {hist1.GetEntries()} entries")
            print(f"   File 2: {hist2.GetEntries()} entries")
            
            # Normalize histograms to 1
            if hist1.GetEntries() > 0:
                hist1.Scale(1.0 / hist1.GetEntries())
            if hist2.GetEntries() > 0:
                hist2.Scale(1.0 / hist2.GetEntries())
            
            # Style the histograms
            hist1.SetLineColor(ROOT.kBlue)
            hist1.SetLineWidth(2)
            hist1.SetFillColor(0)
            hist1.SetFillStyle(3001)
            hist1.SetStats(0)  # Hide statistics box
            hist1.GetXaxis().SetTitle("")  # Remove X-axis title from main plot
            hist1.GetXaxis().SetLabelOffset(999)  # Hide X-axis labels by moving them far away
            hist1.GetYaxis().SetTitle("a.u.")
            hist1.GetYaxis().SetLabelSize(0.045)
            hist1.GetYaxis().SetTitleSize(0.06)
            hist1.GetYaxis().SetTitleOffset(0.8)
            
            hist2.SetLineColor(ROOT.kRed)
            hist2.SetLineWidth(2)
            hist2.SetFillColor(0)
            hist2.SetFillStyle(3001)
            hist2.SetStats(0)  # Hide statistics box
            
            # Create canvas and draw - same dimensions as original
            canvas = TCanvas(f"canvas_{var_name}", f"{var_config['title']} Comparison", 800, 1000)
            canvas.SetLogy(True)
            canvas.SetGridx(True)
            canvas.SetGridy(True)
            
            # Create pads for main plot and ratio - same as original
            main_pad = ROOT.TPad(f"main_pad_{var_name}", "Main", 0.0, 0.3, 1.0, 0.97)  # Top 70%
            ratio_pad = ROOT.TPad(f"ratio_pad_{var_name}", "Ratio", 0.0, 0.0, 1.0, 0.3)  # Bottom 30%
            
            main_pad.SetLeftMargin(0.12)
            main_pad.SetRightMargin(0.05)
            main_pad.SetTopMargin(0.05)
            main_pad.SetBottomMargin(0.02)  # Smaller bottom margin for main pad
            
            ratio_pad.SetLeftMargin(0.12)
            ratio_pad.SetRightMargin(0.05)
            ratio_pad.SetTopMargin(0.02)  # Smaller top margin for ratio pad
            ratio_pad.SetBottomMargin(0.25)  # Larger bottom margin for ratio pad
            
            main_pad.Draw()
            ratio_pad.Draw()
            
            # Draw main plot on main pad
            main_pad.cd()
            main_pad.SetLogy(True)
            main_pad.SetGridx(True)
            main_pad.SetGridy(True)
            
            # Find the maximum to set proper scale
            max_val = max(hist1.GetMaximum(), hist2.GetMaximum())
            hist1.SetMaximum(max_val * 1.5)
            
            # Draw histograms
            hist1.Draw("")
            hist2.Draw("same")
            
            # Add legend with custom labels
            legend = TLegend(0.62, 0.75, 0.93, 0.89)
            legend.SetBorderSize(1)
            legend.SetLineColor(1)
            legend.SetLineStyle(1)
            legend.SetLineWidth(1)
            legend.SetFillColor(0)
            legend.SetFillStyle(1001)
            legend.SetTextSize(0.045)
            
            legend.AddEntry(hist1, legend1, "lpf")
            legend.AddEntry(hist2, legend2, "lpf")
            legend.Draw()

            # Add CMS labels
            tex = TLatex()
            tex.SetTextFont(42)
            tex.SetTextSize(0.04)
            tex.SetLineWidth(2)
            tex.DrawLatexNDC(0.6,0.97,"Z'#rightarrow ee, 200 PU (14 TeV)")
            
            tex_cms = TLatex()
            tex_cms.SetTextSize(0.06)
            tex_cms.SetTextFont(42)
            tex_cms.DrawLatexNDC(0.18, 0.85, "#bf{CMS}")
            
            tex_private = TLatex()
            tex_private.SetTextSize(0.045)
            tex_private.SetTextFont(52)
            tex_private.DrawLatexNDC(0.18, 0.8, "Phase-2 Simulation")
            
            # Now create ratio panel
            ratio_pad.cd()
            ratio_pad.SetGridx(True)
            ratio_pad.SetGridy(True)
            
            # Create ratio histogram
            ratio_hist = hist2.Clone(f"ratio_{var_name}")
            ratio_hist.Divide(hist1)  # Target / Reference
            
            # Style the ratio histogram
            ratio_hist.SetLineColor(ROOT.kBlack)
            ratio_hist.SetLineWidth(2)
            ratio_hist.SetMarkerColor(ROOT.kBlack)
            ratio_hist.SetMarkerStyle(20)
            ratio_hist.SetMarkerSize(0.8)
            ratio_hist.SetStats(0)
            
            # Set ratio plot range and labels
            ratio_hist.SetMinimum(0.0)  # Ratio can't be negative
            ratio_hist.SetMaximum(2.0)  # Adjust this based on your data
            ratio_hist.GetXaxis().SetTitle(var_config['xlabel'])
            ratio_hist.GetXaxis().SetTitleSize(0.1)  # X-axis title size
            ratio_hist.GetXaxis().SetLabelSize(0.09) 
            ratio_hist.GetXaxis().SetTitleOffset(0.9)
            ratio_hist.GetYaxis().SetTitle("Ratio")
            ratio_hist.GetYaxis().SetTitleSize(0.11)  # Y-axis title size
            ratio_hist.GetYaxis().SetTitleOffset(0.5)
            ratio_hist.GetYaxis().SetLabelSize(0.08)
                    
            # Draw ratio histogram
            ratio_hist.Draw("E1")  # Error bars
            
            # Add horizontal line at ratio = 1.0
            line = ROOT.TLine(var_config['xmin'], 1.0, var_config['xmax'], 1.0)
            line.SetLineColor(ROOT.kRed)
            line.SetLineStyle(2)
            line.SetLineWidth(2)
            line.Draw()
            
            # Save the plot for this variable
            var_output_name = f"{output_name}_{var_name.replace('eg_', '')}"
            output_path = f"{var_output_name}.png"
            canvas.SaveAs(output_path)
            print(f"   💾 Saved: {output_path}")
                        
            # Clean up canvas and histograms for this variable
            canvas.Close()
            hist1.Delete()
            hist2.Delete()
            ratio_hist.Delete()
            
            print(f"   ✅ Completed plot for {var_name}")
        
        print("\n" + "=" * 60)
        print("🎉 All variable comparisons complete! 🎉")
        print(f"📁 Check out your separate plots in the current directory!")
        
    except Exception as e:
        print(f"💥 Oops! Something went wrong: {e}")
    
    finally:
        # Clean up
        if 'file1' in locals():
            file1.Close()
        if 'file2' in locals():
            file2.Close()

def main():
    """Main function to parse arguments and run the comparison"""
    
    parser = argparse.ArgumentParser(
        description="🎯 Plot multiple EGM variables comparison from two ROOT files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python plot_Phase2_EGM_Variables.py file1.root file2.root
  python plot_Phase2_EGM_Variables.py file1.root file2.root my_comparison
  python plot_Phase2_EGM_Variables.py file1.root file2.root my_comparison "Reference Sample" "Target Sample"

Note: 
  - file1.root will be plotted as BLUE (Reference)
  - file2.root will be plotted as RED (Target)  
  - Ratio plot shows: Target/Reference (hist2/hist1)
        """
    )
    
    parser.add_argument("file1", help="First ROOT file path")
    parser.add_argument("file2", help="Second ROOT file path")
    parser.add_argument("output_name", nargs="?", default="hcal_hovere_comparison", 
                       help="Output name for plots (default: hcal_hovere_comparison)")
    parser.add_argument("legend1", nargs="?", default="Reference", 
                       help="Legend label for first file (default: Target)")
    parser.add_argument("legend2", nargs="?", default="Target", 
                       help="Legend label for second file (default: Reference)")
    
    args = parser.parse_args()
    
    # Check if files exist
    if not os.path.exists(args.file1):
        print(f"💀 File not found: {args.file1}")
        sys.exit(1)
    
    if not os.path.exists(args.file2):
        print(f"💀 File not found: {args.file2}")
        sys.exit(1)
    
    # Setup ROOT style
    setup_root_style()
    
    # Let's plot this! 🚀
    plot_hcal_hovere(args.file1, args.file2, args.output_name, args.legend1, args.legend2)

if __name__ == "__main__":
    main()
