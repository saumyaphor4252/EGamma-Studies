#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Overlay variables from QCD, data, DY and ttbar ntuples (TTrees).

- Assumes each ROOT file contains a TTree named 'egHLTTree'.
- Uses a variable list and binning consistent with plot_ntuple_variables.py.
- For every variable, draws QCD, data, DY, ttbar on the same canvas.
- Saves PNGs and prints mean / median for each distribution.
"""

import ROOT
import os
import argparse
from array import array

ROOT.gROOT.SetBatch(True)


def setup_root_style():
    """Setup ROOT plotting style (similar to plot_ntuple_variables.py)."""
    ROOT.gStyle.SetOptStat(0)  # no stats box (we print stats ourselves)
    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)
    ROOT.gStyle.SetTitleSize(0.05, "x")
    ROOT.gStyle.SetTitleSize(0.05, "y")
    ROOT.gStyle.SetLabelSize(0.04, "x")
    ROOT.gStyle.SetLabelSize(0.04, "y")


def get_median(hist):
    """Compute median using ROOT quantiles."""
    if not hist or hist.GetEntries() == 0:
        return float("nan")
    probs = array("d", [0.5])
    q = array("d", [0.0])
    hist.GetQuantiles(1, q, probs)
    return q[0]


def create_histogram_from_tree(tree, var_name, title, xlabel, ylabel,
                               nbins, xmin, xmax, hist_name, normalize=True):
    """
    Fill a TH1 from a TTree variable using TTree::Draw.

    Returns the filled histogram (possibly normalized).
    """
    if not tree:
        return None

    # Support special derived variables that depend on underlying branches.
    # For tanh(s2_values/10), we internally use the s2_values branch.
    branch_name = var_name
    if var_name == "tanh_s2_over_10":
        branch_name = "s2_values"

    # Check branch exists
    branch = tree.GetBranch(branch_name)
    if not branch:
        print(f"[WARN] Branch '{var_name}' not found in tree '{tree.GetName()}'")
        return None

    hist = ROOT.TH1F(hist_name, title, nbins, xmin, xmax)
    hist.GetXaxis().SetTitle(xlabel)
    hist.GetYaxis().SetTitle("a.u." if normalize else ylabel)
    hist.Sumw2()

    # Choose expression to draw: either the raw branch or a derived expression
    if var_name == "tanh_s2_over_10":
        expr = f"TMath::TanH(s2_values/10.0)"
    else:
        expr = var_name

    draw_cmd = f"{expr}>>{hist_name}"
    # Use "goff" (graphics off) to avoid implicit drawing
    tree.Draw(draw_cmd, "", "goff")

    if hist.GetEntries() == 0:
        return hist

    if normalize:
        integral = hist.Integral()
        if integral > 0:
            hist.Scale(1.0 / integral)

    return hist


def style_hist(hist, color, line_style=1):
    """Apply ROOT style settings to a histogram."""
    if not hist:
        return
    hist.SetLineColor(color)
    hist.SetLineWidth(2)
    hist.SetLineStyle(line_style)
    hist.SetFillStyle(0)


def overlay_variable(var_name, title, xlabel, ylabel, nbins, xmin, xmax,
                     trees, output_dir, normalize=True):
    """
    For a given variable, create one histogram per sample, overlay and save.

    trees: dict { sample_label: TTree }
    """
    colors = {
        "QCD":   ROOT.kRed + 1,
        "data":  ROOT.kBlack,
        "DY":    ROOT.kBlue + 1,
        "ttbar": ROOT.kGreen + 2,
    }

    hists = {}

    # Create and style histograms for each sample
    for sample, tree in trees.items():
        hist_name = f"h_{var_name}_{sample}"
        hist = create_histogram_from_tree(
            tree, var_name, title, xlabel, ylabel,
            nbins, xmin, xmax, hist_name, normalize=normalize
        )
        if hist and hist.GetEntries() > 0:
            style_hist(hist, colors.get(sample, ROOT.kGray + 2))
            hists[sample] = hist
        else:
            if hist:
                print(f"[INFO] '{var_name}' for {sample} has 0 entries in the given range.")

    if not hists:
        print(f"[WARN] No non-empty histograms for variable '{var_name}', skipping.")
        return

    # Determine global y-max (after normalization if applied)
    ymax = max(h.GetMaximum() for h in hists.values())
    for h in hists.values():
        h.SetMaximum(1.4 * ymax)

    # Draw linear and log-y versions
    for logy in (False, True):
        canvas_name = f"c_{var_name}{'_log' if logy else ''}"
        canvas = ROOT.TCanvas(canvas_name, title, 800, 600)
        if logy:
            canvas.SetLogy(True)

        draw_opt = "HIST"
        for sample, hist in hists.items():
            hist.Draw(draw_opt)
            draw_opt = "HIST SAME"

        # Legend
        legend = ROOT.TLegend(0.65, 0.65, 0.88, 0.88)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        for sample, hist in hists.items():
            legend.AddEntry(hist, sample, "l")
        legend.Draw()

        # Save
        suffix = "_log" if logy else ""
        out_name = f"{var_name}_overlay{suffix}.png"
        canvas.SaveAs(os.path.join(output_dir, out_name))
        canvas.Close()

    # Print stats (mean, median and their absolute values) for this variable
    print(f"Variable: {var_name}")
    for sample, hist in hists.items():
        mean = hist.GetMean()
        median = get_median(hist)
        entries = int(hist.GetEntries())
        abs_mean = abs(mean)
        abs_median = abs(median)
        print(
            f"  {sample:6s}: "
            f"entries = {entries:7d}, "
            f"mean = {mean: .5g}, median = {median: .5g}, "
            f"|mean| = {abs_mean: .5g}, |median| = {abs_median: .5g}"
        )
    print("")


def main():
    parser = argparse.ArgumentParser(
        description="Overlay variables from QCD, data, DY and ttbar ntuples.",
        epilog="""
Examples:
  python3 overlay_ntuple_variables.py \\
      --qcd   QCD/Ntuple_QCD.root \\
      --data  EGamma/Ntuple_EGamma.root \\
      --dy    DY/Ntuple_DY.root \\
      --ttbar TTbar/Ntuple_TTbar.root
"""
    )
    parser.add_argument("--qcd",   required=True, help="QCD ntuple ROOT file")
    parser.add_argument("--data",  required=True, help="data/EGamma ntuple ROOT file")
    parser.add_argument("--dy",    required=True, help="DY ntuple ROOT file")
    parser.add_argument("--ttbar", required=True, help="ttbar ntuple ROOT file")
    parser.add_argument(
        "-o", "--output-dir", default="plots_overlay_trees",
        help="Output directory for plots (default: plots_overlay_trees)"
    )
    parser.add_argument(
        "--no-normalize", action="store_true",
        help="Do NOT normalize histograms (default: normalize)"
    )
    parser.add_argument(
        "--only", nargs="*", default=None,
        help="Optional list of variable names to process (default: all configured below)"
    )
    args = parser.parse_args()

    setup_root_style()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Open files and get trees
    def open_file(path, label):
        if not os.path.exists(path):
            raise RuntimeError(f"{label} file not found: {path}")
        f = ROOT.TFile.Open(path)
        if not f or f.IsZombie():
            raise RuntimeError(f"Cannot open {label} file: {path}")
        tree = f.Get("egHLTTree")
        if not tree:
            raise RuntimeError(f"Tree 'egHLTTree' not found in {label} file: {path}")
        return f, tree

    f_qcd,   t_qcd   = open_file(args.qcd,   "QCD")
    f_data,  t_data  = open_file(args.data,  "data")
    f_dy,    t_dy    = open_file(args.dy,    "DY")
    f_ttbar, t_ttbar = open_file(args.ttbar, "ttbar")

    trees = {
        "QCD":   t_qcd,
        "data":  t_data,
        "DY":    t_dy,
        "ttbar": t_ttbar,
    }

    # Variable definition (aligned with plot_ntuple_variables.py)
    variables_to_plot = [
        ("eg_et",           "EGM Trigger Object E_{T} Distribution",      "E_{T} [GeV]",      "a.u.", 50, 0,   200),
        ("eg_energy",       "EGM Trigger Object Energy Distribution",     "Energy [GeV]",     "a.u.", 50, 0,   500),
        ("eg_eta",          "EGM Trigger Object #eta Distribution",       "#eta",             "a.u.", 50, -3,  3),
        ("eg_phi",          "EGM Trigger Object #phi Distribution",       "#phi [rad]",       "a.u.", 50, -3.2, 3.2),

        ("ecal_eta",        "Ecal Candidate #eta Distribution",           "#eta",             "a.u.", 50, -3,  3),
        ("ecal_phi",        "Ecal Candidate #phi Distribution",           "#phi [rad]",       "a.u.", 50, -3.2, 3.2),

        ("s2_values",       "S2 Values Distribution",                     "S2",               "a.u.", 50, 0,   1),
        ("tanh_s2_over_10", "tanh(S2/10) Distribution",                   "tanh(S2/10)",      "a.u.", 50, 0,   1),
        ("dphi1_values",    "dPhi1 Values Distribution",                  "dPhi1 [rad]",      "a.u.", 100, -0.08, 0.08),
        ("dphi1bests2_values", "dPhi1BestS2 Values Distribution",        "dPhi1BestS2 [rad]","a.u.", 50, -0.1, 0.1),
        ("dphi2_values",    "dPhi2 Values Distribution",                  "dPhi2 [rad]",      "a.u.", 100, -0.004, 0.004),
        ("dphi2bests2_values", "dPhi2BestS2 Values Distribution",        "dPhi2BestS2 [rad]","a.u.", 50, -0.1, 0.1),
        ("dphi3_values",    "dPhi3 Values Distribution",                  "dPhi3 [rad]",      "a.u.", 50, -0.5, 0.5),
        ("dphi4_values",    "dPhi4 Values Distribution",                  "dPhi4 [rad]",      "a.u.", 50, -0.5, 0.5),
        ("drz1_values",     "dRZ1 Values Distribution",                   "dRZ1 [cm]",        "a.u.", 50, -1,  1),
        ("drz2_values",     "dRZ2 Values Distribution",                   "dRZ2 [cm]",        "a.u.", 100, -0.08,  0.08),
        ("drz3_values",     "dRZ3 Values Distribution",                   "dRZ3 [cm]",        "a.u.", 50, -1,  1),
        ("drz4_values",     "dRZ4 Values Distribution",                   "dRZ4 [cm]",        "a.u.", 50, -1,  1),
        ("dzbests2_values", "dzBestS2 Values Distribution",               "dzBestS2 [cm]",    "a.u.", 50, -1,  1),
        ("etawidth_values", "Eta Width Values Distribution",              "Eta Width",        "a.u.", 50, 0,   0.05),
        ("nrclus_values",   "Number of Clusters Distribution",            "Number of Clusters","a.u.", 20, 0,  20),
        ("phiwidth_values", "Phi Width Values Distribution",              "Phi Width",        "a.u.", 50, 0,   0.5),

        ("delta_r_values",  "Delta R Values Distribution",                "Delta R",          "a.u.", 50, 0,   0.2),
    ]

    # Apply optional --only filter
    if args.only:
        selected = []
        available = {v[0] for v in variables_to_plot}
        missing = []
        for name in args.only:
            if name in available:
                selected.append(name)
            else:
                missing.append(name)
        if missing:
            print("[WARN] These requested variables are not in variables_to_plot and will be ignored:")
            for m in missing:
                print("   ", m)
        variables_to_plot = [v for v in variables_to_plot if v[0] in selected]

    normalize = not args.no_normalize
    print(f"Normalization: {'ON' if normalize else 'OFF'}")
    print("")

    for var_name, title, xlabel, ylabel, nbins, xmin, xmax in variables_to_plot:
        print(f"Processing variable: {var_name}")
        overlay_variable(
            var_name, title, xlabel, ylabel, nbins, xmin, xmax,
            trees, args.output_dir, normalize=normalize
        )

    # Close files
    f_qcd.Close()
    f_data.Close()
    f_dy.Close()
    f_ttbar.Close()

    print(f"All overlay plots saved in '{args.output_dir}'.")


if __name__ == "__main__":
    main()

