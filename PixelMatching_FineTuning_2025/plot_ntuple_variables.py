#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyROOT script to plot variables from the EGM trigger analysis ntuple

Description: Reads the ntuple file and creates histograms for all variables
Author: Generated for EGM trigger analysis
"""

import ROOT
import os
import math
import sys
import argparse

def create_plots_directory():
    """Create plots directory if it doesn't exist"""
    if not os.path.exists("plots"):
        os.makedirs("plots")
        print("📁 Created plots directory")

def setup_root_style():
    """Setup ROOT plotting style"""
    ROOT.gStyle.SetOptStat(1110)  # Show entries, mean, RMS
    ROOT.gStyle.SetOptFit(1)      # Show fit parameters
    ROOT.gStyle.SetPadTickX(1)    # Ticks on both sides
    ROOT.gStyle.SetPadTickY(1)
    ROOT.gStyle.SetTitleSize(0.05, "x")
    ROOT.gStyle.SetTitleSize(0.05, "y")
    ROOT.gStyle.SetLabelSize(0.04, "x")
    ROOT.gStyle.SetLabelSize(0.04, "y")
    
    # Setup custom color palette for COLZ plots
    setup_custom_palette()

def setup_custom_palette():
    """Setup ROOT's built-in color palette"""
    ROOT.gStyle.SetPalette(1)  # Use ROOT's default palette

def create_histogram(tree, variable_name, title, xlabel, ylabel, nbins=100, xmin=None, xmax=None, normalize=True):
    """
    Create and fill a histogram from tree variable
    
    Args:
        tree: ROOT TTree object
        variable_name: Name of the variable in the tree
        title: Histogram title
        xlabel: X-axis label
        ylabel: Y-axis label
        nbins: Number of bins
        xmin, xmax: X-axis range (auto if None)
        normalize: Whether to normalize the histogram (default: True)
    """
    # Check if the branch exists
    branch = tree.GetBranch(variable_name)
    if not branch:
        print(f"❌ Branch {variable_name} not found in tree")
        return None
    
    # Auto-determine range if not specified
    if xmin is None or xmax is None:
        # Get min/max from the data using ROOT's Draw method
        tree.Draw(f"{variable_name}>>temp_hist(1000)")
        temp_hist = ROOT.gDirectory.Get("temp_hist")
        if temp_hist and temp_hist.GetEntries() > 0:
            xmin = temp_hist.GetXaxis().GetXmin()
            xmax = temp_hist.GetXaxis().GetXmax()
            # Add some margin
            margin = (xmax - xmin) * 0.1
            xmin -= margin
            xmax += margin
        else:
            xmin, xmax = -1, 1  # Default range
    
    # Create histogram
    hist_name = f"h_{variable_name}"
    hist = ROOT.TH1F(hist_name, title, nbins, xmin, xmax)
    hist.GetXaxis().SetTitle(xlabel)
    
    # Set y-axis label based on normalization
    if normalize:
        hist.GetYaxis().SetTitle("a.u.")
    else:
        hist.GetYaxis().SetTitle(ylabel)
    
    hist.SetLineColor(ROOT.kBlue)
    hist.SetLineWidth(2)
    hist.SetFillColor(ROOT.kBlue-10)
    hist.SetFillStyle(3004)
    
    # Use ROOT's Draw method to fill histogram directly
    # This is much more efficient than manual looping
    draw_cmd = f"{variable_name}>>{hist_name}"
    tree.Draw(draw_cmd)
    
    # Get the filled histogram
    filled_hist = ROOT.gDirectory.Get(hist_name)
    if filled_hist:
        # Copy the filled histogram
        hist = filled_hist.Clone(f"h_{variable_name}_final")
        hist.SetTitle(title)
        hist.GetXaxis().SetTitle(xlabel)
        
        # Set y-axis label based on normalization
        if normalize:
            hist.GetYaxis().SetTitle("a.u.")
        else:
            hist.GetYaxis().SetTitle(ylabel)
        
        hist.SetLineColor(ROOT.kBlue)
        hist.SetLineWidth(2)
        hist.SetFillColor(ROOT.kBlue-10)
        hist.SetFillStyle(3004)
        
        # Normalize the histogram if requested
        if normalize and hist.GetEntries() > 0:
            integral = hist.Integral()
            if integral > 0:
                hist.Scale(1.0 / integral)
            else:
                print(f"⚠️  Warning: Histogram {variable_name} has zero integral, skipping normalization")
    
    return hist

def plot_histogram(hist, filename, output_dir="plots", logy=False):
    """
    Plot histogram and save as PNG
    
    Args:
        hist: ROOT histogram
        filename: Output filename
        output_dir: Output directory
        logy: Use log scale for Y-axis
    """
    if not hist or hist.GetEntries() == 0:
        print(f"⚠️  No data for {filename}")
        return
    
    # Create canvas
    canvas = ROOT.TCanvas(f"c_{hist.GetName()}", hist.GetTitle(), 800, 600)
    canvas.SetLogy(logy)
    
    # Draw histogram
    hist.Draw("HIST")
    
    # Add statistics box
    ROOT.gPad.Update()
    stats = hist.FindObject("stats")
    if stats:
        stats.SetX1NDC(0.7)
        stats.SetY1NDC(0.7)
        stats.SetX2NDC(0.95)
        stats.SetY2NDC(0.95)
    
    # Save plot
    canvas.SaveAs(f"{output_dir}/{filename}")
    print(f"📊 Saved: {filename}")
    
    # Clean up
    canvas.Close()

def main():
    """Main function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Plot variables from EGM trigger analysis ntuple',
        epilog="""
Examples:
  python3 plot_ntuple_variables.py input.root
  python3 plot_ntuple_variables.py my_analysis.root
        """
    )
    parser.add_argument('input_file', help='Input ROOT ntuple file')
    parser.add_argument('-o', '--output-dir', default='plots', 
                       help='Output directory for plots (default: plots)')
    parser.add_argument('--no-normalize', action='store_true', 
                       help='Create non-normalized histograms (default: normalized)')
    args = parser.parse_args()
    
    print("🚀 Starting EGM trigger analysis plotting...")
    print(f"📂 Input file: {args.input_file}")
    print(f"📁 Output directory: {args.output_dir}")
    
    # Setup
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"📁 Created {args.output_dir} directory")
    
    setup_root_style()
    
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"❌ Input file {args.input_file} not found!")
        print("Please check the file path and try again")
        return
    
    print(f"📂 Opening file: {args.input_file}")
    file = ROOT.TFile(args.input_file, "READ")
    tree = file.Get("egHLTTree")
    
    if not tree:
        print("❌ Tree 'egHLTTree' not found in file!")
        return
    
    print(f"📊 Tree has {tree.GetEntries()} entries")
    
    # Define variables to plot
    variables_to_plot = [
        # EGM trigger object variables
        ("eg_et", "EGM Trigger Object E_{T} Distribution", "E_{T} [GeV]", "a.u.", 50, 0, 200),
        ("eg_energy", "EGM Trigger Object Energy Distribution", "Energy [GeV]", "a.u.", 50, 0, 500),
        ("eg_eta", "EGM Trigger Object #eta Distribution", "#eta", "a.u.", 50, -3, 3),
        ("eg_phi", "EGM Trigger Object #phi Distribution", "#phi [rad]", "a.u.", 50, -3.2, 3.2),
        
        # Ecal candidate variables
        ("ecal_eta", "Ecal Candidate #eta Distribution", "#eta", "a.u.", 50, -3, 3),
        ("ecal_phi", "Ecal Candidate #phi Distribution", "#phi [rad]", "a.u.", 50, -3.2, 3.2),
        
        # Pixel match variables (with appropriate ranges)
        ("s2_values", "S2 Values Distribution", "S2", "a.u.", 50, 0, 1),
        ("dphi1_values", "dPhi1 Values Distribution", "dPhi1 [rad]", "a.u.", 100, -0.08, 0.08),
        ("dphi1bests2_values", "dPhi1BestS2 Values Distribution", "dPhi1BestS2 [rad]", "a.u.", 50, -0.1, 0.1),
        ("dphi2_values", "dPhi2 Values Distribution", "dPhi2 [rad]", "a.u.", 100, -0.004, 0.004),
        ("dphi2bests2_values", "dPhi2BestS2 Values Distribution", "dPhi2BestS2 [rad]", "a.u.", 50, -0.1, 0.1),
        ("dphi3_values", "dPhi3 Values Distribution", "dPhi3 [rad]", "a.u.", 50, -0.5, 0.5),
        ("dphi4_values", "dPhi4 Values Distribution", "dPhi4 [rad]", "a.u.", 50, -0.5, 0.5),
        ("drz1_values", "dRZ1 Values Distribution", "dRZ1 [cm]", "a.u.", 50, -1, 1),
        ("drz2_values", "dRZ2 Values Distribution", "dRZ2 [cm]", "a.u.", 100, -0.08, 0.08),
        ("drz3_values", "dRZ3 Values Distribution", "dRZ3 [cm]", "a.u.", 50, -1, 1),
        ("drz4_values", "dRZ4 Values Distribution", "dRZ4 [cm]", "a.u.", 50, -1, 1),
        ("dzbests2_values", "dzBestS2 Values Distribution", "dzBestS2 [cm]", "a.u.", 50, -1, 1),
        ("etawidth_values", "Eta Width Values Distribution", "Eta Width", "a.u.", 50, 0, 0.05),
        ("nrclus_values", "Number of Clusters Distribution", "Number of Clusters", "a.u.", 20, 0, 20),
        ("phiwidth_values", "Phi Width Values Distribution", "Phi Width", "a.u.", 50, 0, 0.5),
        
        # Matching information
        ("delta_r_values", "Delta R Values Distribution", "Delta R", "a.u.", 50, 0, 0.2),
    ]
    
    # Create and plot histograms
    print("📈 Creating histograms...")
    normalize = not args.no_normalize
    print(f"📊 Normalization: {'ON' if normalize else 'OFF'}")
    
    for var_name, title, xlabel, ylabel, nbins, xmin, xmax in variables_to_plot:
        print(f"  Processing: {var_name}")
        
        # Create histogram
        hist = create_histogram(tree, var_name, title, xlabel, ylabel, nbins, xmin, xmax, normalize=normalize)
        
        if hist and hist.GetEntries() > 0:
            # Create both nominal (linear) and log scale versions for all variables
            # Nominal version
            filename = f"{var_name}_histogram.png"
            plot_histogram(hist, filename, args.output_dir, logy=False)
            print(f"  📊 Created nominal version: {filename}")
            
            # Log scale version
            log_filename = f"{var_name}_histogram_log.png"
            plot_histogram(hist, log_filename, args.output_dir, logy=True)
            print(f"  📊 Created log-scale version: {log_filename}")
        elif hist and hist.GetEntries() == 0:
            print(f"⚠️  Skipping {var_name}: No entries found in the range of the histogram. Try updating the histogram range.")
    
    # Create summary plots
    print("📊 Creating summary plots...")
    
    # Delta R distribution (both nominal and log scale)
    delta_r_hist = create_histogram(tree, "delta_r_values", "Delta R Distribution", "Delta R", "a.u.", 50, 0, 0.2, normalize=normalize)
    if delta_r_hist and delta_r_hist.GetEntries() > 0:
        # Nominal version
        plot_histogram(delta_r_hist, "delta_r_summary.png", args.output_dir, logy=False)
        print("  📊 Created nominal version: delta_r_summary.png")
        # Log scale version
        plot_histogram(delta_r_hist, "delta_r_summary_log.png", args.output_dir, logy=True)
        print("  📊 Created log-scale version: delta_r_summary_log.png")
    elif delta_r_hist and delta_r_hist.GetEntries() == 0:
        print("⚠️  Skipping delta_r_summary: No entries found")
    
    # EGM ET distribution (both nominal and log scale)
    eg_et_hist = create_histogram(tree, "eg_et", "EGM Trigger Object E_{T} Distribution", "E_{T} [GeV]", "a.u.", 50, 0, 200, normalize=normalize)
    if eg_et_hist and eg_et_hist.GetEntries() > 0:
        # Nominal version
        plot_histogram(eg_et_hist, "eg_et_summary.png", args.output_dir, logy=False)
        print("  📊 Created nominal version: eg_et_summary.png")
        # Log scale version
        plot_histogram(eg_et_hist, "eg_et_summary_log.png", args.output_dir, logy=True)
        print("  📊 Created log-scale version: eg_et_summary_log.png")
    elif eg_et_hist and eg_et_hist.GetEntries() == 0:
        print("⚠️  Skipping eg_et_summary: No entries found")
    
    # Eta-Phi scatter plot
    print("📊 Creating eta-phi scatter plot...")
    canvas = ROOT.TCanvas("eta_phi_scatter", "EGM Trigger Objects: Eta vs Phi", 800, 600)
    
    # Create and fill 2D histogram using ROOT's Draw method
    tree.Draw("eg_phi:eg_eta>>h2d_eta_phi(50,-3,3,50,-3.2,3.2)", "", "COLZ")
    
    # Get the created histogram
    h2d = ROOT.gDirectory.Get("h2d_eta_phi")
    if h2d:
        h2d.SetTitle("EGM Trigger Objects: #eta vs #phi")
        h2d.GetXaxis().SetTitle("#eta")
        h2d.GetYaxis().SetTitle("#phi [rad]")
        h2d.Draw("COLZ")
    
    # Nominal version
    canvas.SaveAs(f"{args.output_dir}/eta_phi_scatter.png")
    print("📊 Saved: eta_phi_scatter.png")
    
    # Log scale version
    canvas.SetLogz(1)
    canvas.SaveAs(f"{args.output_dir}/eta_phi_scatter_log.png")
    print("📊 Saved: eta_phi_scatter_log.png")
    canvas.SetLogz(0)
    
    canvas.Close()
    
    # 2D Correlation plots
    print("📊 Creating 2D correlation plots...")
    
    # dPhi1 vs eg_eta (COLZ)
    print("  Creating dPhi1 vs eg_eta correlation...")
    canvas = ROOT.TCanvas("dphi1_eta", "dPhi1 vs EGM #eta", 800, 600)
    tree.Draw("dphi1_values:eg_eta>>h2d_dphi1_eta(50,-3,3,50,-0.1,0.1)", "", "COLZ")
    h2d_dphi1 = ROOT.gDirectory.Get("h2d_dphi1_eta")
    if h2d_dphi1 and h2d_dphi1.GetEntries() > 0:
        h2d_dphi1.SetTitle("dPhi1 vs EGM #eta")
        h2d_dphi1.GetXaxis().SetTitle("EGM #eta")
        h2d_dphi1.GetYaxis().SetTitle("dPhi1 [rad]")
        h2d_dphi1.Draw("COLZ")
        # Nominal version
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_eta.png")
        print("📊 Saved: dphi1_vs_eg_eta.png")
        
        # Log scale version
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_eta_log.png")
        print("📊 Saved: dphi1_vs_eg_eta_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi1_vs_eg_eta: No entries found")
    canvas.Close()
    
    # dPhi2 vs eg_eta (COLZ)
    print("  Creating dPhi2 vs eg_eta correlation...")
    canvas = ROOT.TCanvas("dphi2_eta", "dPhi2 vs EGM #eta", 800, 600)
    tree.Draw("dphi2_values:eg_eta>>h2d_dphi2_eta(50,-3,3,50,-0.002,0.002)", "", "COLZ")
    h2d_dphi2 = ROOT.gDirectory.Get("h2d_dphi2_eta")
    if h2d_dphi2 and h2d_dphi2.GetEntries() > 0:
        h2d_dphi2.SetTitle("dPhi2 vs EGM #eta")
        h2d_dphi2.GetXaxis().SetTitle("EGM #eta")
        h2d_dphi2.GetYaxis().SetTitle("dPhi2 [rad]")
        h2d_dphi2.Draw("COLZ")
        # Nominal version
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_eta.png")
        print("📊 Saved: dphi2_vs_eg_eta.png")
        
        # Log scale version
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_eta_log.png")
        print("📊 Saved: dphi2_vs_eg_eta_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi2_vs_eg_eta: No entries found")
    canvas.Close()
    
    # dRZ1 vs eg_eta (COLZ)
    print("  Creating dRZ1 vs eg_eta correlation...")
    canvas = ROOT.TCanvas("drz1_eta", "dRZ1 vs EGM #eta", 800, 600)
    tree.Draw("drz1_values:eg_eta>>h2d_drz1_eta(50,-3,3,50,-1,1)", "", "COLZ")
    h2d_drz1 = ROOT.gDirectory.Get("h2d_drz1_eta")
    if h2d_drz1 and h2d_drz1.GetEntries() > 0:
        h2d_drz1.SetTitle("dRZ1 vs EGM #eta")
        h2d_drz1.GetXaxis().SetTitle("EGM #eta")
        h2d_drz1.GetYaxis().SetTitle("dRZ1 [cm]")
        h2d_drz1.Draw("COLZ")
        # Nominal version
        canvas.SaveAs(f"{args.output_dir}/drz1_vs_eg_eta.png")
        print("📊 Saved: drz1_vs_eg_eta.png")
        
        # Log scale version
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/drz1_vs_eg_eta_log.png")
        print("📊 Saved: drz1_vs_eg_eta_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping drz1_vs_eg_eta: No entries found")
    canvas.Close()
    
    # dRZ2 vs eg_eta (COLZ)
    print("  Creating dRZ2 vs eg_eta correlation...")
    canvas = ROOT.TCanvas("drz2_eta", "dRZ2 vs EGM #eta", 800, 600)
    tree.Draw("drz2_values:eg_eta>>h2d_drz2_eta(50,-3,3,100,-0.1,0.1)", "", "COLZ")
    h2d_drz2 = ROOT.gDirectory.Get("h2d_drz2_eta")
    if h2d_drz2 and h2d_drz2.GetEntries() > 0:
        h2d_drz2.SetTitle("dRZ2 vs EGM #eta")
        h2d_drz2.GetXaxis().SetTitle("EGM #eta")
        h2d_drz2.GetYaxis().SetTitle("dRZ2 [cm]")
        h2d_drz2.Draw("COLZ")
        # Nominal version
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_eta.png")
        print("📊 Saved: drz2_vs_eg_eta.png")
        
        # Log scale version
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_eta_log.png")
        print("📊 Saved: drz2_vs_eg_eta_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping drz2_vs_eg_eta: No entries found")
    canvas.Close()

    # Additional 2D correlations (COLZ): dPhi1, dPhi2, dRZ2 vs eg_et and eg_phi

    # dPhi1 vs eg_et (COLZ)
    print("  Creating dPhi1 vs eg_et correlation...")
    canvas = ROOT.TCanvas("dphi1_et", "dPhi1 vs EGM E_{T}", 800, 600)
    tree.Draw("dphi1_values:eg_et>>h2d_dphi1_et(50,0,200,50,-0.1,0.1)", "", "COLZ")
    h2d_dphi1_et = ROOT.gDirectory.Get("h2d_dphi1_et")
    if h2d_dphi1_et and h2d_dphi1_et.GetEntries() > 0:
        h2d_dphi1_et.SetTitle("dPhi1 vs EGM E_{T}")
        h2d_dphi1_et.GetXaxis().SetTitle("EGM E_{T} [GeV]")
        h2d_dphi1_et.GetYaxis().SetTitle("dPhi1 [rad]")
        h2d_dphi1_et.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_et.png")
        print("📊 Saved: dphi1_vs_eg_et.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_et_log.png")
        print("📊 Saved: dphi1_vs_eg_et_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi1_vs_eg_et: No entries found")
    canvas.Close()

    # dPhi1 vs eg_phi (COLZ)
    print("  Creating dPhi1 vs eg_phi correlation...")
    canvas = ROOT.TCanvas("dphi1_phi", "dPhi1 vs EGM #phi", 800, 600)
    tree.Draw("dphi1_values:eg_phi>>h2d_dphi1_phi(50,-3.2,3.2,50,-0.1,0.1)", "", "COLZ")
    h2d_dphi1_phi = ROOT.gDirectory.Get("h2d_dphi1_phi")
    if h2d_dphi1_phi and h2d_dphi1_phi.GetEntries() > 0:
        h2d_dphi1_phi.SetTitle("dPhi1 vs EGM #phi")
        h2d_dphi1_phi.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_dphi1_phi.GetYaxis().SetTitle("dPhi1 [rad]")
        h2d_dphi1_phi.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_phi.png")
        print("📊 Saved: dphi1_vs_eg_phi.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_phi_log.png")
        print("📊 Saved: dphi1_vs_eg_phi_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi1_vs_eg_phi: No entries found")
    canvas.Close()

    # dPhi2 vs eg_et (COLZ)
    print("  Creating dPhi2 vs eg_et correlation...")
    canvas = ROOT.TCanvas("dphi2_et", "dPhi2 vs EGM E_{T}", 800, 600)
    tree.Draw("dphi2_values:eg_et>>h2d_dphi2_et(50,0,200,50,-0.002,0.002)", "", "COLZ")
    h2d_dphi2_et = ROOT.gDirectory.Get("h2d_dphi2_et")
    if h2d_dphi2_et and h2d_dphi2_et.GetEntries() > 0:
        h2d_dphi2_et.SetTitle("dPhi2 vs EGM E_{T}")
        h2d_dphi2_et.GetXaxis().SetTitle("EGM E_{T} [GeV]")
        h2d_dphi2_et.GetYaxis().SetTitle("dPhi2 [rad]")
        h2d_dphi2_et.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_et.png")
        print("📊 Saved: dphi2_vs_eg_et.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_et_log.png")
        print("📊 Saved: dphi2_vs_eg_et_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi2_vs_eg_et: No entries found")
    canvas.Close()

    # dPhi2 vs eg_phi (COLZ)
    print("  Creating dPhi2 vs eg_phi correlation...")
    canvas = ROOT.TCanvas("dphi2_phi", "dPhi2 vs EGM #phi", 800, 600)
    tree.Draw("dphi2_values:eg_phi>>h2d_dphi2_phi(50,-3.2,3.2,50,-0.002,0.002)", "", "COLZ")
    h2d_dphi2_phi = ROOT.gDirectory.Get("h2d_dphi2_phi")
    if h2d_dphi2_phi and h2d_dphi2_phi.GetEntries() > 0:
        h2d_dphi2_phi.SetTitle("dPhi2 vs EGM #phi")
        h2d_dphi2_phi.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_dphi2_phi.GetYaxis().SetTitle("dPhi2 [rad]")
        h2d_dphi2_phi.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_phi.png")
        print("📊 Saved: dphi2_vs_eg_phi.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_phi_log.png")
        print("📊 Saved: dphi2_vs_eg_phi_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping dphi2_vs_eg_phi: No entries found")
    canvas.Close()

    # dRZ2 vs eg_et (COLZ)
    print("  Creating dRZ2 vs eg_et correlation...")
    canvas = ROOT.TCanvas("drz2_et", "dRZ2 vs EGM E_{T}", 800, 600)
    tree.Draw("drz2_values:eg_et>>h2d_drz2_et(50,0,200,50,-0.1,0.1)", "", "COLZ")
    h2d_drz2_et = ROOT.gDirectory.Get("h2d_drz2_et")
    if h2d_drz2_et and h2d_drz2_et.GetEntries() > 0:
        h2d_drz2_et.SetTitle("dRZ2 vs EGM E_{T}")
        h2d_drz2_et.GetXaxis().SetTitle("EGM E_{T} [GeV]")
        h2d_drz2_et.GetYaxis().SetTitle("dRZ2 [cm]")
        h2d_drz2_et.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_et.png")
        print("📊 Saved: drz2_vs_eg_et.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_et_log.png")
        print("📊 Saved: drz2_vs_eg_et_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping drz2_vs_eg_et: No entries found")
    canvas.Close()

    # dRZ2 vs eg_phi (COLZ)
    print("  Creating dRZ2 vs eg_phi correlation...")
    canvas = ROOT.TCanvas("drz2_phi", "dRZ2 vs EGM #phi", 800, 600)
    tree.Draw("drz2_values:eg_phi>>h2d_drz2_phi(50,-3.2,3.2,50,-0.1,0.1)", "", "COLZ")
    h2d_drz2_phi = ROOT.gDirectory.Get("h2d_drz2_phi")
    if h2d_drz2_phi and h2d_drz2_phi.GetEntries() > 0:
        h2d_drz2_phi.SetTitle("dRZ2 vs EGM #phi")
        h2d_drz2_phi.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_drz2_phi.GetYaxis().SetTitle("dRZ2 [cm]")
        h2d_drz2_phi.Draw("COLZ")
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_phi.png")
        print("📊 Saved: drz2_vs_eg_phi.png")
        canvas.SetLogz(1)
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_phi_log.png")
        print("📊 Saved: drz2_vs_eg_phi_log.png")
        canvas.SetLogz(0)
    else:
        print("⚠️  Skipping drz2_vs_eg_phi: No entries found")
    canvas.Close()

    # Standard 2D scatter-style plots (eta/phi on x-axis, dPhi1/dPhi2/dRZ2 on y-axis)
    print("📊 Creating 2D scatter-style correlation plots...")

    # dPhi1 vs eg_eta (scatter)
    print("  Creating dPhi1 vs eg_eta scatter plot...")
    canvas = ROOT.TCanvas("dphi1_eta_scatter", "dPhi1 vs EGM #eta (scatter)", 800, 600)
    tree.Draw("dphi1_values:eg_eta>>h2d_dphi1_eta_scatter(50,-3,3,50,-0.1,0.1)", "", "SCAT")
    h2d_dphi1_eta_scatter = ROOT.gDirectory.Get("h2d_dphi1_eta_scatter")
    if h2d_dphi1_eta_scatter and h2d_dphi1_eta_scatter.GetEntries() > 0:
        h2d_dphi1_eta_scatter.SetTitle("dPhi1 vs EGM #eta (scatter)")
        h2d_dphi1_eta_scatter.GetXaxis().SetTitle("EGM #eta")
        h2d_dphi1_eta_scatter.GetYaxis().SetTitle("dPhi1 [rad]")
        h2d_dphi1_eta_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_eta_scatter.png")
        print("📊 Saved: dphi1_vs_eg_eta_scatter.png")
    else:
        print("⚠️  Skipping dphi1_vs_eg_eta_scatter: No entries found")
    canvas.Close()

    # dPhi1 vs eg_phi (scatter)
    print("  Creating dPhi1 vs eg_phi scatter plot...")
    canvas = ROOT.TCanvas("dphi1_phi_scatter", "dPhi1 vs EGM #phi (scatter)", 800, 600)
    tree.Draw("dphi1_values:eg_phi>>h2d_dphi1_phi_scatter(50,-3.2,3.2,50,-0.1,0.1)", "", "SCAT")
    h2d_dphi1_phi_scatter = ROOT.gDirectory.Get("h2d_dphi1_phi_scatter")
    if h2d_dphi1_phi_scatter and h2d_dphi1_phi_scatter.GetEntries() > 0:
        h2d_dphi1_phi_scatter.SetTitle("dPhi1 vs EGM #phi (scatter)")
        h2d_dphi1_phi_scatter.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_dphi1_phi_scatter.GetYaxis().SetTitle("dPhi1 [rad]")
        h2d_dphi1_phi_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/dphi1_vs_eg_phi_scatter.png")
        print("📊 Saved: dphi1_vs_eg_phi_scatter.png")
    else:
        print("⚠️  Skipping dphi1_vs_eg_phi_scatter: No entries found")
    canvas.Close()

    # dPhi2 vs eg_eta (scatter)
    print("  Creating dPhi2 vs eg_eta scatter plot...")
    canvas = ROOT.TCanvas("dphi2_eta_scatter", "dPhi2 vs EGM #eta (scatter)", 800, 600)
    tree.Draw("dphi2_values:eg_eta>>h2d_dphi2_eta_scatter(50,-3,3,50,-0.002,0.002)", "", "SCAT")
    h2d_dphi2_eta_scatter = ROOT.gDirectory.Get("h2d_dphi2_eta_scatter")
    if h2d_dphi2_eta_scatter and h2d_dphi2_eta_scatter.GetEntries() > 0:
        h2d_dphi2_eta_scatter.SetTitle("dPhi2 vs EGM #eta (scatter)")
        h2d_dphi2_eta_scatter.GetXaxis().SetTitle("EGM #eta")
        h2d_dphi2_eta_scatter.GetYaxis().SetTitle("dPhi2 [rad]")
        h2d_dphi2_eta_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_eta_scatter.png")
        print("📊 Saved: dphi2_vs_eg_eta_scatter.png")
    else:
        print("⚠️  Skipping dphi2_vs_eg_eta_scatter: No entries found")
    canvas.Close()

    # dPhi2 vs eg_phi (scatter)
    print("  Creating dPhi2 vs eg_phi scatter plot...")
    canvas = ROOT.TCanvas("dphi2_phi_scatter", "dPhi2 vs EGM #phi (scatter)", 800, 600)
    tree.Draw("dphi2_values:eg_phi>>h2d_dphi2_phi_scatter(50,-3.2,3.2,50,-0.002,0.002)", "", "SCAT")
    h2d_dphi2_phi_scatter = ROOT.gDirectory.Get("h2d_dphi2_phi_scatter")
    if h2d_dphi2_phi_scatter and h2d_dphi2_phi_scatter.GetEntries() > 0:
        h2d_dphi2_phi_scatter.SetTitle("dPhi2 vs EGM #phi (scatter)")
        h2d_dphi2_phi_scatter.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_dphi2_phi_scatter.GetYaxis().SetTitle("dPhi2 [rad]")
        h2d_dphi2_phi_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/dphi2_vs_eg_phi_scatter.png")
        print("📊 Saved: dphi2_vs_eg_phi_scatter.png")
    else:
        print("⚠️  Skipping dphi2_vs_eg_phi_scatter: No entries found")
    canvas.Close()

    # dRZ2 vs eg_eta (scatter)
    print("  Creating dRZ2 vs eg_eta scatter plot...")
    canvas = ROOT.TCanvas("drz2_eta_scatter", "dRZ2 vs EGM #eta (scatter)", 800, 600)
    tree.Draw("drz2_values:eg_eta>>h2d_drz2_eta_scatter(50,-3,3,100,-0.1,0.1)", "", "SCAT")
    h2d_drz2_eta_scatter = ROOT.gDirectory.Get("h2d_drz2_eta_scatter")
    if h2d_drz2_eta_scatter and h2d_drz2_eta_scatter.GetEntries() > 0:
        h2d_drz2_eta_scatter.SetTitle("dRZ2 vs EGM #eta (scatter)")
        h2d_drz2_eta_scatter.GetXaxis().SetTitle("EGM #eta")
        h2d_drz2_eta_scatter.GetYaxis().SetTitle("dRZ2 [cm]")
        h2d_drz2_eta_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_eta_scatter.png")
        print("📊 Saved: drz2_vs_eg_eta_scatter.png")
    else:
        print("⚠️  Skipping drz2_vs_eg_eta_scatter: No entries found")
    canvas.Close()

    # dRZ2 vs eg_phi (scatter)
    print("  Creating dRZ2 vs eg_phi scatter plot...")
    canvas = ROOT.TCanvas("drz2_phi_scatter", "dRZ2 vs EGM #phi (scatter)", 800, 600)
    tree.Draw("drz2_values:eg_phi>>h2d_drz2_phi_scatter(50,-3.2,3.2,100,-0.1,0.1)", "", "SCAT")
    h2d_drz2_phi_scatter = ROOT.gDirectory.Get("h2d_drz2_phi_scatter")
    if h2d_drz2_phi_scatter and h2d_drz2_phi_scatter.GetEntries() > 0:
        h2d_drz2_phi_scatter.SetTitle("dRZ2 vs EGM #phi (scatter)")
        h2d_drz2_phi_scatter.GetXaxis().SetTitle("EGM #phi [rad]")
        h2d_drz2_phi_scatter.GetYaxis().SetTitle("dRZ2 [cm]")
        h2d_drz2_phi_scatter.Draw("SCAT")
        canvas.SaveAs(f"{args.output_dir}/drz2_vs_eg_phi_scatter.png")
        print("📊 Saved: drz2_vs_eg_phi_scatter.png")
    else:
        print("⚠️  Skipping drz2_vs_eg_phi_scatter: No entries found")
    canvas.Close()
    
    # Clean up
    file.Close()
    
    print(f"✅ All plots saved to '{args.output_dir}/' directory!")
    print("📁 Check the plots folder for all generated histograms")

if __name__ == "__main__":
    main()
