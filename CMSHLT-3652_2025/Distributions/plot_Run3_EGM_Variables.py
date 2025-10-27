#!/usr/bin/env python3
"""
🎯 ROOT Histogram Comparison Script for EGM Variables 🎯

This script takes two ROOT files created by makeNtuples_Run3_Seeded.py and plots
multiple E/Gamma trigger variables as normalized histograms with ratio plots.

Usage: python plot_Run3_EGM_Variables.py file1.root file2.root [output_name] [legend1] [legend2] [--collection-type seeded|unseeded] [--output-dir directory] [--make-2d] [--make-diff]
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

def plot_egm_variables(file1_path, file2_path, output_name="egm_variables_comparison", legend1="Reference", legend2="Target", output_dir="plots", make_2d=False, make_diff=False):
    """Plot multiple variables from two ROOT files, creating separate plots for each"""
    
    print(f"🎯 Starting variable comparison plots! 🎯")
    print(f"📁 File 1: {file1_path} (Legend: {legend1})")
    print(f"📁 File 2: {file2_path} (Legend: {legend2})")
    print(f"📂 Output base name: {output_name}")
    print(f"📁 Output directory: {output_dir}")
    if make_2d:
        print("📊 Will also create 2D plots: variable vs eta")
    if make_diff:
        print("📈 Will also create difference plots: (target - reference) vs eta")
    print("=" * 60)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created output directory: {output_dir}")
    else:
        print(f"📁 Using existing output directory: {output_dir}")
    
    # Define variables to plot with their binning
    variables = {
        # Basic object properties
        "eg_et": {"bins": 100, "xmin": 0.0, "xmax": 200.0, "title": "E_{T}", "xlabel": "E_{T} [GeV]"},
        "eg_energy": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "Energy", "xlabel": "Energy [GeV]"},
        "eg_eta": {"bins": 30, "xmin": -3.0, "xmax": 3.0, "title": "#eta", "xlabel": "#eta"},
        "eg_phi": {"bins": 32, "xmin": -3.2, "xmax": 3.2, "title": "#phi", "xlabel": "#phi [rad]"},

        # SuperCluster properties
        "eg_rawEnergy": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "Raw Energy", "xlabel": "Raw Energy [GeV]"},
        "eg_nrClus": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Number of Clusters", "xlabel": "Number of Clusters"},
        "eg_phiWidth": {"bins": 50, "xmin": 0.0, "xmax": 0.5, "title": "#phi Width", "xlabel": "#phi Width"},
        "eg_seedId": {"bins": 100, "xmin": 0.0, "xmax": 2000000000.0, "title": "Seed ID", "xlabel": "Seed ID"},
        "eg_seedDet": {"bins": 10, "xmin": 0.0, "xmax": 10.0, "title": "Seed Detector", "xlabel": "Seed Detector"},

        # Cluster shape variables
        "eg_sigmaIEtaIEta": {"bins": 50, "xmin": 0.0, "xmax": 0.1, "title": "#sigma_{i#eta i#eta}", "xlabel": "#sigma_{i#eta i#eta}"},
        "eg_sigmaIPhiIPhi": {"bins": 50, "xmin": 0.0, "xmax": 0.1, "title": "#sigma_{i#phi i#phi}", "xlabel": "#sigma_{i#phi i#phi}"},

        # Isolation variables
        "eg_ecalPFIsol_default": {"bins": 25, "xmin": 0.0, "xmax": 500.0, "title": "ECAL PF Isolation", "xlabel": "ECAL PF Isolation [GeV]"},
        "eg_hcalPFIsol_default": {"bins": 25, "xmin": 0.0, "xmax": 100.0, "title": "HCAL PF Isolation", "xlabel": "HCAL PF Isolation [GeV]"},
        "eg_trkIsolV0_default": {"bins": 50, "xmin": 0.0, "xmax": 0.5, "title": "Track Isolation V0", "xlabel": "Track Isolation V0"},
        "eg_trkIsolV6_default": {"bins": 50, "xmin": 0.0, "xmax": 0.5, "title": "Track Isolation V6", "xlabel": "Track Isolation V6"},
        "eg_trkIsolV72_default": {"bins": 50, "xmin": 0.0, "xmax": 0.5, "title": "Track Isolation V72", "xlabel": "Track Isolation V72"},

        # Track variables
        "eg_trkChi2_default": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Track #chi^{2}", "xlabel": "Track #chi^{2}"},
        "eg_invESeedInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.1, "title": "1/E_{seed} - 1/p", "xlabel": "1/E_{seed} - 1/p"},
        "eg_invEInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.01, "title": "1/E - 1/p", "xlabel": "1/E - 1/p"},
        "eg_trkDEta": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Track}", "xlabel": "#Delta#eta_{Track}"},

        # Pixel match and other variables
        "eg_pms2_default": {"bins": 20, "xmin": 0.0, "xmax": 0.8, "title": "PMS2", "xlabel": "PMS2"},
        "eg_hcalHForHoverE": {"bins": 25, "xmin": 0.0, "xmax": 1, "title": "HCal H/E", "xlabel": "H/E"},

        # Best track variables
        "eg_bestTrkChi2": {"bins": 50, "xmin": 0.0, "xmax": 1.0, "title": "Best Track #chi^{2}", "xlabel": "Best Track #chi^{2}"},
        "eg_bestTrkDEta": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Best Track}", "xlabel": "#Delta#eta_{Best Track}"},
        "eg_bestTrkDEtaSeed": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#eta_{Best Track}^{Seed}", "xlabel": "#Delta#eta_{Best Track}^{Seed}"},
        "eg_bestTrkDPhi": {"bins": 30, "xmin": 0.0, "xmax": 0.08, "title": "#Delta#phi_{Best Track}", "xlabel": "#Delta#phi_{Best Track}"},
        "eg_bestTrkESeedInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.1, "title": "Best Track 1/E_{seed} - 1/p", "xlabel": "Best Track 1/E_{seed} - 1/p"},
        "eg_bestTrkInvEInvP": {"bins": 30, "xmin": 0.0, "xmax": 0.01, "title": "Best Track 1/E - 1/p", "xlabel": "Best Track 1/E - 1/p"},
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
            tex.DrawLatexNDC(0.7,0.97,"Run4 MC (14 TeV)")
            
            tex_cms = TLatex()
            tex_cms.SetTextSize(0.06)
            tex_cms.SetTextFont(42)
            tex_cms.DrawLatexNDC(0.18, 0.85, "#bf{CMS}")
            
            tex_private = TLatex()
            tex_private.SetTextSize(0.045)
            tex_private.SetTextFont(52)
            tex_private.DrawLatexNDC(0.18, 0.8, "#it{Private Work}")
            
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
            output_path = os.path.join(output_dir, f"{var_output_name}.png")
            canvas.SaveAs(output_path)
            print(f"   💾 Saved: {output_path}")
                        
            # Clean up canvas and histograms for this variable
            canvas.Close()
            hist1.Delete()
            hist2.Delete()
            ratio_hist.Delete()
            
            print(f"   ✅ Completed plot for {var_name}")
        
        # Create 2D plots if requested
        if make_2d:
            print("\n" + "=" * 40)
            print("📊 Creating 2D plots: variable vs eta 📊")
            print("=" * 40)

            # Create subdirectory for 2D plots
            plot_2d_dir = os.path.join(output_dir, "2d_plots")
            if not os.path.exists(plot_2d_dir):
                os.makedirs(plot_2d_dir)
                print(f"📁 Created 2D plots directory: {plot_2d_dir}")

            # Loop over each variable for 2D plots
            for var_name, var_config in variables.items():
                print(f"\n📊 Creating 2D plot for: {var_name} vs eta")

                # Create 2D histograms for this variable vs eta
                hist2d_1 = ROOT.TH2F(f"hist2d_1_{var_name}", f"{var_config['title']} vs #eta ({legend1})",
                                    30, -3.0, 3.0,  # eta bins
                                    var_config['bins'], var_config['xmin'], var_config['xmax'])  # variable bins

                hist2d_2 = ROOT.TH2F(f"hist2d_2_{var_name}", f"{var_config['title']} vs #eta ({legend2})",
                                    30, -3.0, 3.0,  # eta bins
                                    var_config['bins'], var_config['xmin'], var_config['xmax'])  # variable bins

                # Fill the 2D histograms
                tree1.Draw(f"{var_name}:eg_eta>>hist2d_1_{var_name}", "", "goff")
                tree2.Draw(f"{var_name}:eg_eta>>hist2d_2_{var_name}", "", "goff")

                print(f"   File 1: {hist2d_1.GetEntries()} entries")
                print(f"   File 2: {hist2d_2.GetEntries()} entries")

                # Create canvas for 2D plots (side by side)
                canvas_2d = ROOT.TCanvas(f"canvas_2d_{var_name}", f"{var_config['title']} vs #eta Comparison", 1200, 500)
                canvas_2d.Divide(2, 1)  # Two pads side by side

                # Style and draw first histogram
                canvas_2d.cd(1)
                ROOT.gPad.SetLogz(True)
                hist2d_1.GetXaxis().SetTitle("#eta")
                hist2d_1.GetYaxis().SetTitle(var_config['xlabel'])
                hist2d_1.GetZaxis().SetTitle("Counts")
                hist2d_1.GetXaxis().SetTitleSize(0.04)
                hist2d_1.GetYaxis().SetTitleSize(0.04)
                hist2d_1.GetZaxis().SetTitleSize(0.04)
                hist2d_1.Draw("COLZ")

                # Add title
                title1 = ROOT.TLatex()
                title1.SetTextSize(0.04)
                title1.DrawLatexNDC(0.1, 0.92, legend1)

                # Style and draw second histogram
                canvas_2d.cd(2)
                ROOT.gPad.SetLogz(True)
                hist2d_2.GetXaxis().SetTitle("#eta")
                hist2d_2.GetYaxis().SetTitle(var_config['xlabel'])
                hist2d_2.GetZaxis().SetTitle("Counts")
                hist2d_2.GetXaxis().SetTitleSize(0.04)
                hist2d_2.GetYaxis().SetTitleSize(0.04)
                hist2d_2.GetZaxis().SetTitleSize(0.04)
                hist2d_2.Draw("COLZ")

                # Add title
                title2 = ROOT.TLatex()
                title2.SetTextSize(0.04)
                title2.DrawLatexNDC(0.1, 0.92, legend2)

                # Save the 2D plot
                var_2d_output_name = f"{output_name}_{var_name.replace('eg_', '')}_vs_eta"
                output_2d_path = os.path.join(plot_2d_dir, f"{var_2d_output_name}.png")
                canvas_2d.SaveAs(output_2d_path)
                print(f"   💾 Saved 2D plot: {output_2d_path}")

                # Clean up
                canvas_2d.Close()
                hist2d_1.Delete()
                hist2d_2.Delete()

                print(f"   ✅ Completed 2D plot for {var_name}")

            print("\n" + "=" * 40)
            print("🎉 All 2D plots complete! 🎉")
            print(f"📁 Check out your 2D plots in: {plot_2d_dir}/")

        # Create difference plots if requested
        if make_diff:
            print("\n" + "=" * 40)
            print("📈 Creating difference plots: (target - reference) vs eta 📈")
            print("=" * 40)

            # Create subdirectory for difference plots
            diff_dir = os.path.join(output_dir, "diff_plots")
            if not os.path.exists(diff_dir):
                os.makedirs(diff_dir)
                print(f"📁 Created difference plots directory: {diff_dir}")

            # Define eta bins for difference calculation
            eta_bins = 12  # 12 bins from -3.0 to 3.0
            eta_edges = [-3.0, -2.4, -1.8, -1.2, -0.6, 0.0, 0.6, 1.2, 1.8, 2.4, 3.0]
            eta_centers = [0.5*(eta_edges[i] + eta_edges[i+1]) for i in range(len(eta_edges)-1)]
            eta_widths = [eta_edges[i+1] - eta_edges[i] for i in range(len(eta_edges)-1)]

            # Loop over each variable for difference plots
            for var_name, var_config in variables.items():
                print(f"\n📈 Creating difference plot for: {var_name}")

                # Create histogram for difference vs eta
                diff_hist = ROOT.TH1F(f"diff_{var_name}", f"({legend2} - {legend1}) vs #eta: {var_config['title']}",
                                     eta_bins, -3.0, 3.0)

                # Calculate differences for each eta bin
                for i in range(len(eta_centers)):
                    eta_min = eta_edges[i]
                    eta_max = eta_edges[i+1]
                    eta_center = eta_centers[i]

                    # Create cuts for eta bin
                    eta_cut = f"eg_eta >= {eta_min} && eg_eta < {eta_max}"

                    # Get mean values for both files in this eta bin
                    mean1 = ROOT.TH1F(f"temp1_{var_name}_{i}", "", 100, var_config['xmin'], var_config['xmax'])
                    mean2 = ROOT.TH1F(f"temp2_{var_name}_{i}", "", 100, var_config['xmin'], var_config['xmax'])

                    tree1.Draw(f"{var_name}>>temp1_{var_name}_{i}", eta_cut, "goff")
                    tree2.Draw(f"{var_name}>>temp2_{var_name}_{i}", eta_cut, "goff")

                    # Calculate mean difference
                    if mean1.GetEntries() > 10 and mean2.GetEntries() > 10:  # Require minimum statistics
                        diff_value = mean2.GetMean() - mean1.GetMean()
                        diff_error = ROOT.TMath.Sqrt(mean1.GetMeanError()**2 + mean2.GetMeanError()**2)
                        diff_hist.SetBinContent(i+1, diff_value)
                        diff_hist.SetBinError(i+1, diff_error)
                    else:
                        diff_hist.SetBinContent(i+1, 0)
                        diff_hist.SetBinError(i+1, 0)

                    # Clean up temporary histograms
                    mean1.Delete()
                    mean2.Delete()

                # Create canvas for difference plot
                canvas_diff = ROOT.TCanvas(f"canvas_diff_{var_name}", f"Difference Plot: {var_config['title']}", 800, 600)

                # Style the difference histogram
                diff_hist.SetLineColor(ROOT.kBlue)
                diff_hist.SetLineWidth(2)
                diff_hist.SetMarkerColor(ROOT.kBlue)
                diff_hist.SetMarkerStyle(20)
                diff_hist.SetMarkerSize(0.8)
                diff_hist.SetStats(0)

                # Set axis labels and titles
                diff_hist.GetXaxis().SetTitle("#eta")
                diff_hist.GetYaxis().SetTitle(f"({legend2} - {legend1}) [{var_config['xlabel'].split('[')[-1].strip(']') if '[' in var_config['xlabel'] else 'units'}]")
                diff_hist.GetXaxis().SetTitleSize(0.04)
                diff_hist.GetYaxis().SetTitleSize(0.04)
                diff_hist.GetXaxis().SetLabelSize(0.04)
                diff_hist.GetYaxis().SetLabelSize(0.04)

                # Set reasonable Y range based on data
                max_diff = max(abs(diff_hist.GetMaximum()), abs(diff_hist.GetMinimum()))
                if max_diff > 0:
                    diff_hist.GetYaxis().SetRangeUser(-max_diff*1.2, max_diff*1.2)
                else:
                    diff_hist.GetYaxis().SetRangeUser(-1, 1)  # Default range if no variation

                # Draw the histogram
                diff_hist.Draw("E1")

                # Add horizontal line at y=0
                zero_line = ROOT.TLine(-3.0, 0, 3.0, 0)
                zero_line.SetLineColor(ROOT.kRed)
                zero_line.SetLineStyle(2)
                zero_line.SetLineWidth(2)
                zero_line.Draw()

                # Add CMS label
                tex_cms = ROOT.TLatex()
                tex_cms.SetTextSize(0.05)
                tex_cms.SetTextFont(42)
                tex_cms.DrawLatexNDC(0.15, 0.85, "#bf{CMS}")

                tex_private = ROOT.TLatex()
                tex_private.SetTextSize(0.04)
                tex_private.SetTextFont(52)
                tex_private.DrawLatexNDC(0.15, 0.8, "#it{Private Work}")

                # Save the difference plot
                diff_output_name = f"{output_name}_{var_name.replace('eg_', '')}_diff_vs_eta"
                output_diff_path = os.path.join(diff_dir, f"{diff_output_name}.png")
                canvas_diff.SaveAs(output_diff_path)
                print(f"   💾 Saved difference plot: {output_diff_path}")

                # Clean up
                canvas_diff.Close()
                diff_hist.Delete()

                print(f"   ✅ Completed difference plot for {var_name}")

            print("\n" + "=" * 40)
            print("🎉 All difference plots complete! 🎉")
            print(f"📁 Check out your difference plots in: {diff_dir}/")

        print("\n" + "=" * 60)
        print("🎉 All plotting tasks complete! 🎉")
        print(f"📁 1D plots in: {output_dir}/")
        if make_2d:
            print(f"📁 2D plots in: {os.path.join(output_dir, '2d_plots')}/")
        if make_diff:
            print(f"📁 Difference plots in: {os.path.join(output_dir, 'diff_plots')}/")
        
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
        description="🎯 Plot multiple EGM variables comparison from ROOT files created by makeNtuples_Run3_Seeded.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python plot_Run3_EGM_Variables.py file1.root file2.root
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Reference" "Target"
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Ref" "Tgt" --output-dir results
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Ref" "Tgt" --make-2d
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Ref" "Tgt" --make-diff
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Ref" "Tgt" --make-2d --make-diff
  python plot_Run3_EGM_Variables.py file1.root file2.root my_comparison "Ref" "Tgt" --collection-type unseeded --output-dir analysis_plots --make-2d --make-diff

Notes:
  - Plots 26+ E/Gamma trigger variables from makeNtuples_Run3_Seeded.py output
  - file1.root plotted as BLUE (Reference), file2.root as RED (Target)
  - Ratio plot shows: Target/Reference (hist2/hist1)
  - Use --make-2d to also create 2D plots of each variable vs eta
  - Use --make-diff to create difference plots: (target - reference) mean vs eta
  - 2D plots show variable distributions as function of eta (side-by-side comparison)
  - Difference plots show how variables differ across eta bins
  - Plots are saved in specified output directory (created if doesn't exist)
  - Use --collection-type to document whether files were created with seeded/unseeded collections
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
    parser.add_argument("--collection-type", "-c",
                       choices=["seeded", "unseeded"],
                       default="seeded",
                       help="Collection type used to create the ROOT files (default: seeded)")
    parser.add_argument("--output-dir", "-d",
                       default="plots",
                       help="Directory to save plots (default: plots)")
    parser.add_argument("--make-2d", action="store_true",
                       help="Also create 2D plots of variables vs eta")
    parser.add_argument("--make-diff", action="store_true",
                       help="Also create difference plots: (target - reference) vs eta")

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
    plot_egm_variables(args.file1, args.file2, args.output_name, args.legend1, args.legend2, args.output_dir, args.make_2d, args.make_diff)

if __name__ == "__main__":
    main()
