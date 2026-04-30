#!/usr/bin/env python3
"""
🎯 ROOT Histogram Comparison Script for Multiple EGM Variables 🎯

This script takes multiple ROOT files and plots various EGM variables
as normalized histograms with both linear and log scale y-axis.

Usage: python plot_Phase2_EGM_Variables.py file1.root file2.root [file3.root ...] [output_name] [legend1] [legend2] [legend3] ...

Example: python3 plot_Phase2_EGM_Variables.py ../Ntuple_16_0_0_pre4_QCD.root ../Ntuple_16_0_0_pre4_SingleE.root ../Ntuple_16_0_0_pre4_ZEE.root ../Ntuple_16_0_0_pre4_ZpEE.root Comparison "QCD" "SingleE" "ZEE" "ZpEE"
"""

import os
import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gROOT, TPaveText, TLatex
import argparse

# Minimum E_T (GeV) for candidates to be included in the distributions (pt > 30 GeV)
PT_MIN_GEV = 30.0

def setup_root_style():
    """Setup ROOT plot style for beautiful histograms"""
    gROOT.SetBatch(True)  # Run in batch mode for saving
    gStyle.SetOptStat(1111)  # Show all statistics
    gStyle.SetPalette(55)    # Beautiful color palette
    gStyle.SetTitleSize(0.04, "xyz")
    gStyle.SetLabelSize(0.03, "xyz")
    gStyle.SetTitleOffset(1.2, "y")
    gStyle.SetTitleOffset(1.1, "x")
    # Extra border space for axis titles/labels and CMS text.
    gStyle.SetPadLeftMargin(0.14)
    gStyle.SetPadRightMargin(0.06)
    gStyle.SetPadTopMargin(0.08)
    gStyle.SetPadBottomMargin(0.14)

def plot_egm_variables(file_paths, output_name="egm_variables_comparison", legends=None, tree_name="egHLTRun3Tree"):
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
    print(f"✂️  Cut: eg_et > {PT_MIN_GEV} GeV (pt > {PT_MIN_GEV} GeV)")
    print(f"🎨 Color scheme: Blue, Red, Green, Magenta, Orange, Cyan, Yellow, Pink, Violet, Teal")
    print("=" * 60)
    
    # Define variables to plot with their binning
    variables = {
        "nrEgs": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Number of EG Candidates", "xlabel": "Number of EG Candidates"},
        "eg_hcalHForHoverE": {"bins": 25, "xmin": 0.0, "xmax": 25, "title": "HCal H/E", "xlabel": "H/E"},
        "eg_et": {"bins": 25, "xmin": 0.0, "xmax": 200.0, "title": "E_{T}", "xlabel": "E_{T} [GeV]"},
        "eg_energy": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "Energy", "xlabel": "Energy [GeV]"},
        "eg_rawEnergy": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "Raw Energy", "xlabel": "Raw Energy [GeV]"},
        "eg_nrClus": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Number of Clusters", "xlabel": "Number of Clusters"},
        "eg_phi": {"bins": 32, "xmin": -3.2, "xmax": 3.2, "title": "#phi", "xlabel": "#phi [rad]"},
        "eg_phiWidth": {"bins": 40, "xmin": 0.0, "xmax": 0.2, "title": "#phi Width", "xlabel": "#phi Width"},
        "eg_eta": {"bins": 30, "xmin": -3.0, "xmax": 3.0, "title": "#eta", "xlabel": "#eta"},
        #"eg_seedId": {"bins": 120, "xmin": -60.0, "xmax": 60.0, "title": "Seed ID", "xlabel": "Seed ID"},
        "eg_seedDet": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Seed Detector", "xlabel": "Seed Detector"},
        "eg_sigmaIEtaIEta": {"bins": 50, "xmin": 0.0, "xmax": 0.03, "title": "#sigma_{i#eta i#eta}", "xlabel": "#sigma_{i#eta i#eta}"},
        "eg_sigmaIEtaIEtaNoise": {"bins": 50, "xmin": 0.0, "xmax": 0.03, "title": "#sigma_{i#eta i#eta}^{Noise}", "xlabel": "#sigma_{i#eta i#eta}^{Noise}"},
        "eg_invEInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.01, "title": "1/E - 1/p", "xlabel": "1/E - 1/p"},
        "eg_invESeedInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.1, "title": "1/E_{seed} - 1/p", "xlabel": "1/E_{seed} - 1/p"},
        "eg_trkDEta": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Track}", "xlabel": "#Delta#eta_{Track}"},
        "eg_trkDEtaSeed": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Track}^{Seed}", "xlabel": "#Delta#eta_{Track}^{Seed}"},
        "eg_trkDPhi": {"bins": 30, "xmin": 0.0, "xmax": 0.2, "title": "#Delta#phi_{Track}", "xlabel": "#Delta#phi_{Track}"},
        "eg_ecalPFIsol": {"bins": 25, "xmin": 0.0, "xmax": 20.0, "title": "ECAL PF Isolation", "xlabel": "ECAL PF Isolation [GeV]"},
        "eg_hcalPFIsol": {"bins": 25, "xmin": 0.0, "xmax": 20.0, "title": "HCAL PF Isolation", "xlabel": "HCAL PF Isolation [GeV]"},
        "eg_trkIsol": {"bins": 50, "xmin": 0.0, "xmax": 0.05, "title": "Track Isolation", "xlabel": "Track Isolation"},
        "eg_trkChi2": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Track #chi^{2}", "xlabel": "Track #chi^{2}"},
        "eg_trkMissHits": {"bins": 5, "xmin": 0.0, "xmax": 5.0, "title": "Track Missing Hits", "xlabel": "Track Missing Hits"},
        "eg_trkValidHits": {"bins": 30, "xmin": 0.0, "xmax": 30.0, "title": "Track Valid Hits", "xlabel": "Track Valid Hits"},
        "eg_trkNrLayerIT": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Track Inner Layers", "xlabel": "Track Inner Layers"},
        "eg_pms2": {"bins": 25, "xmin": 0.0, "xmax": 10, "title": "PMS2", "xlabel": "PMS2"},
        "eg_bestTrkChi2": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Best Track #chi^{2}", "xlabel": "Best Track #chi^{2}"},
        "eg_bestTrkDEta": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "Best Track #Delta#eta", "xlabel": "Best Track #Delta#eta"},
        "eg_bestTrkDEtaSeed": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "Best Track #Delta#eta^{Seed}", "xlabel": "Best Track #Delta#eta^{Seed}"},
        "eg_bestTrkDPhi": {"bins": 30, "xmin": 0.0, "xmax": 0.2, "title": "Best Track #Delta#phi", "xlabel": "Best Track #Delta#phi"},
        "eg_bestTrkMissHits": {"bins": 20, "xmin": 0.0, "xmax": 20.0, "title": "Best Track Missing Hits", "xlabel": "Best Track Missing Hits"},
        "eg_bestTrkNrLayerIT": {"bins": 20, "xmin": 0.0, "xmax": 20.0, "title": "Best Track Inner Layers", "xlabel": "Best Track Inner Layers"},
        "eg_bestTrkESeedInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.1, "title": "Best Track 1/E_{seed} - 1/p", "xlabel": "Best Track 1/E_{seed} - 1/p"},
        "eg_bestTrkInvEInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.01, "title": "Best Track 1/E - 1/p", "xlabel": "Best Track 1/E - 1/p"},
        "eg_bestTrkValidHits": {"bins": 30, "xmin": 0.0, "xmax": 30.0, "title": "Best Track Valid Hits", "xlabel": "Best Track Valid Hits"},
        "eg_r9Frac": {"bins": 25, "xmin": 0.0, "xmax": 1.1, "title": "R9 Fraction", "xlabel": "R9 Fraction"},
        "eg_r9Full": {"bins": 25, "xmin": 0.0, "xmax": 1.5, "title": "R9 Full", "xlabel": "R9 Full"},
        "eg_trkIsolPhoton": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Track Isolation Photon", "xlabel": "Track Isolation Photon"},
        
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
            
            # Get the requested tree from each file
            tree = file_obj.Get(tree_name)
            if not tree:
                print(f"🌳 '{tree_name}' not found in file {i+1} ({file_path})!")
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

            region_configs = (
                ("", "", ""),
                ("EB", " && abs(eg_eta) < 1.479", "EB |#eta| < 1.479"),
                ("EE", " && abs(eg_eta) > 1.479", "EE |#eta| > 1.479"),
            )

            for region_suffix, region_cut, region_title in region_configs:
                # Create histograms for this variable for all files
                histograms = []
                # Selection: only candidates with pt (eg_et) > PT_MIN_GEV
                selection = f"eg_et > {PT_MIN_GEV}{region_cut}"
                draw_expr = var_config.get("draw", var_name)
                print(f"   Region {region_title}: selection = {selection}")

                for i, tree in enumerate(trees):
                    hist_name = f"hist_{region_suffix}_{i}_{var_name}" if region_suffix else f"hist_{i}_{var_name}"
                    hist = TH1F(hist_name, "", var_config['bins'], var_config['xmin'], var_config['xmax'])
                    tree.Draw(f"{draw_expr}>>{hist_name}", selection, "goff")
                    print(f"      File {i+1}: {hist.GetEntries()} entries")

                    # Normalize histogram to 1
                    if hist.GetEntries() > 0:
                        hist.Scale(1.0 / hist.GetEntries())

                    # Style the histogram
                    hist.SetLineColor(colors[i % len(colors)])
                    hist.SetLineWidth(2)
                    hist.SetFillColor(0)
                    hist.SetFillStyle(0)
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
                # Draw both linear and log scale versions
                for ytag, logy in (("lin", False), ("log", True)):
                    canvas_name = f"canvas_{var_name}_{region_suffix}_{ytag}" if region_suffix else f"canvas_{var_name}_{ytag}"
                    canvas = TCanvas(canvas_name, f"{var_config['title']} Comparison {region_title} ({ytag})", 800, 800)
                    canvas.SetLogy(logy)
                    canvas.SetGridx(True)
                    canvas.SetGridy(True)

                    # Find the maximum to set proper scale
                    max_val = max([hist.GetMaximum() for hist in histograms])
                    histograms[0].SetMaximum(max_val * 1.5)

                    # For log scale, avoid issues with bins at/near 0 by setting a sensible minimum.
                    if logy:
                        min_positive = None
                        for hist in histograms:
                            nbins = hist.GetNbinsX()
                            for b in range(1, nbins + 1):
                                c = hist.GetBinContent(b)
                                if c > 0 and (min_positive is None or c < min_positive):
                                    min_positive = c
                        if min_positive is not None:
                            histograms[0].SetMinimum(min_positive * 0.2)

                    # Draw histograms (step-like line representation)
                    for i, hist in enumerate(histograms):
                        if i == 0:
                            hist.Draw("HIST")
                        else:
                            hist.Draw("HIST SAME")

                    # Add legend with custom labels
                    legend = TLegend(0.62, 0.75, 0.93, 0.89)
                    legend.SetBorderSize(1)
                    legend.SetLineColor(1)
                    legend.SetLineStyle(1)
                    legend.SetLineWidth(1)
                    legend.SetFillColor(ROOT.kWhite)
                    legend.SetFillStyle(1001)
                    legend.SetTextSize(0.045)

                    # Add entries for all histograms
                    for i, (hist, legend_label) in enumerate(zip(histograms, legends)):
                        legend.AddEntry(hist, legend_label, "l")
                    legend.Draw()

                    # Add CMS labels (keep existing text content)
                    tex = TLatex()
                    tex.SetTextFont(42)
                    tex.SetTextSize(0.045)
                    tex.SetLineWidth(2)
                    tex.DrawLatexNDC(0.62, 0.94, "2026B (13.6 TeV)")

                    tex_cms = TLatex()
                    tex_cms.SetTextSize(0.058)
                    tex_cms.SetTextFont(42)
                    tex_cms.DrawLatexNDC(0.14, 0.94, "#bf{CMS}")

                    tex_private = TLatex()
                    tex_private.SetTextSize(0.045)
                    tex_private.SetTextFont(42)  # normal font
                    tex_private.DrawLatexNDC(0.27, 0.94, "#it{Preliminary}")

                    # Region annotation
                    tex_region = TLatex()
                    tex_region.SetTextFont(42)
                    tex_region.SetTextSize(0.04)
                    tex_region.DrawLatexNDC(0.62, 0.70, region_title)

                    # Save the plot for this variable
                    var_output_name = f"{output_name}_{var_name.replace('eg_', '')}"
                    if region_suffix:
                        var_output_name = f"{var_output_name}_{region_suffix}"
                    if ytag == "log":
                        # Backward-compatible output name for the inclusive log version
                        output_path = f"{var_output_name}.png"
                    else:
                        output_path = f"{var_output_name}_lin.png"
                    canvas.SaveAs(output_path)
                    print(f"   💾 Saved: {output_path}")

                    canvas.Close()

                # Clean up histograms for this variable and region
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

    parser = argparse.ArgumentParser(
        description="Plot Run3 EGM HLT variable distributions from multiple ntuple files"
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Input ROOT files to compare (example: reference.root target.root)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="egm_variables_comparison",
        help="Output filename prefix",
    )
    parser.add_argument(
        "-l",
        "--labels",
        nargs="*",
        default=None,
        help="Legend labels (same order as inputs). Missing labels are auto-filled.",
    )
    parser.add_argument(
        "-t",
        "--tree",
        default="egHLTRun3Tree",
        help="Tree name to plot (default: egHLTRun3Tree). Use egHLTUnseededRun3Tree for unseeded.",
    )

    args = parser.parse_args()

    if len(args.inputs) < 2:
        parser.error("At least 2 ROOT files are required for comparison.")

    for file_path in args.inputs:
        if not os.path.exists(file_path):
            parser.error(f"File not found: {file_path}")

    if args.labels is not None and len(args.labels) > len(args.inputs):
        parser.error("More labels were provided than input files.")

    setup_root_style()
    plot_egm_variables(args.inputs, args.output, args.labels, args.tree)

if __name__ == "__main__":
    main()