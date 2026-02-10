import ROOT
import numpy as np
import sys
from ctypes import c_double
from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
from PlotCMSLumi import CMS_lumi

#-----------------------------------------
#Get, add, substract histograms 
#-----------------------------------------
def getEff(inFile, num, den, plotType="pt"):
    try:
        hPass = inFile.Get(num)
        hAll  = inFile.Get(den)
    except Exception:
        print ("Error: Hist not found. \nFile: %s \nHistName: %s"%(inFile, num))
        sys.exit()
    #if(ROOT.TEfficiency::CheckConsistency(hPass, hAll)):
    
    # Set x-axis title based on plot type
    xTitles = {
        "pt": "p_{T} [GeV]",
        "pt_TurnOn": "p_{T} [GeV]",
        "eta": "#eta",
        "phi": "#phi [rad]"
    }
    xTitle = xTitles.get(plotType, num)  # Default to histogram name if plotType not found
    hPass.GetXaxis().SetTitle(xTitle)
    
    h_eff = ROOT.TEfficiency(hPass, hAll)
    #pEff = ROOT.TGraphAsymmErrors(hPass, hAll)
    g_eff = h_eff.CreateGraph()
    g_eff.SetName(num)
    return g_eff

def getEffTH1(inFile, num, den, plotType="pt"):
    try:
        hPass = inFile.Get(num)
        hAll  = inFile.Get(den)
        print(f"DEBUG: Reading from file {inFile.GetName()}: num='{num}' (entries={hPass.GetEntries() if hPass else 0}), den='{den}' (entries={hAll.GetEntries() if hAll else 0})")
        
        # Check if histograms are identical (which would give efficiency = 1.0 everywhere)
        if hPass and hAll:
            print(f"DEBUG: Numerator integral: {hPass.Integral()}, Denominator integral: {hAll.Integral()}")
            if hPass.Integral() == hAll.Integral():
                print(f"WARNING: Numerator and denominator have identical integrals! This will give efficiency = 1.0 everywhere.")
            
            # Check if histograms are actually the same object
            if hPass == hAll:
                print(f"WARNING: Numerator and denominator are the SAME histogram object!")
    except Exception:
        print ("Error: Hist not found. \nFile: %s \nHistName: %s"%(inFile, num))
        sys.exit()

    if not hPass or not hAll:
        print ("Error: Missing hist(s) for efficiency. \nFile: %s \nNum: %s Den: %s"%(inFile, num, den))
        sys.exit(1)

    # Ensure we have sum of squares for proper error propagation
    hPass = hPass.Clone()
    hAll  = hAll.Clone()
    hPass.Sumw2()
    hAll.Sumw2()

    # Set x-axis title based on plot type
    xTitles = {
        "pt": "p_{T} [GeV]",
        "pt_TurnOn": "p_{T} [GeV]",
        "eta": "#eta",
        "phi": "#phi [rad]"
    }
    xTitle = xTitles.get(plotType, num)

    # Build efficiency as TH1 with binomial errors: eff = hPass / hAll
    eff_hist = hPass.Clone(f"eff_{num}")
    eff_hist.Reset("ICES")
    eff_hist.Divide(hPass, hAll, 1.0, 1.0, "B")

    eff_hist.GetXaxis().SetTitle(xTitle)
    eff_hist.GetYaxis().SetTitle("HLT  Efficiency")
    return eff_hist

def divideGraphs(graph1, graph2): #from ChatGPT
    g_ratio = ROOT.TGraphAsymmErrors()
    # Loop over the points in graph1 and graph2
    n_points = min(graph1.GetN(), graph2.GetN())  # Use the smaller number of points
    
    for i in range(n_points):
        # Get the values and errors for each point in graph1
        # Reference
        x1 = c_double(0.0)
        y1 = c_double(0.0)
        ex_l1 = graph1.GetErrorXlow(i)
        ex_h1 = graph1.GetErrorXhigh(i)
        ey_l1 = graph1.GetErrorYlow(i)
        ey_h1 = graph1.GetErrorYhigh(i)
        graph1.GetPoint(i, x1, y1)

        # Get the values and errors for the corresponding point in graph2
        # Target
        x2 = c_double(0.0)
        y2 = c_double(0.0)
        ex_l2 = graph2.GetErrorXlow(i)
        ex_h2 = graph2.GetErrorXhigh(i)
        ey_l2 = graph2.GetErrorYlow(i)
        ey_h2 = graph2.GetErrorYhigh(i)
        graph2.GetPoint(i, x2, y2)

        # Perform the division of y values and errors
        if y2.value != 0 and y2.value > 1e-2 and y1.value >= 0:  # Avoid division by zero
            result_y = y1.value / y2.value
            # Propagate asymmetric errors conservatively
            if y1.value > 0 and y2.value > 0:
                rel_low  = ((ey_l1 / y1.value)**2 + (ey_h2 / y2.value)**2) ** 0.5 if y1.value != 0 and y2.value != 0 else 0.0
                rel_high = ((ey_h1 / y1.value)**2 + (ey_l2 / y2.value)**2) ** 0.5 if y1.value != 0 and y2.value != 0 else 0.0
                result_eyl = abs(result_y) * rel_low
                result_eyh = abs(result_y) * rel_high
            else:
                result_eyl = 0.0
                result_eyh = 0.0
        else:
            result_y = 0.0
            result_eyl = 0.0
            result_eyh = 0.0
        
        # Set the values and errors to the result graph
        g_ratio.SetPoint(i, x1.value, result_y)
        # Combine X errors conservatively by taking the larger
        ex_low  = max(ex_l1, ex_l2)
        ex_high = max(ex_h1, ex_h2)
        g_ratio.SetPointError(i, ex_low, ex_high, result_eyl, result_eyh)
    return g_ratio


#-----------------------------------------
#Get ratio of two eff histograms
#-----------------------------------------
def getRatio(files, num, den, plotType="pt"):
    effs  = []
    names = []
    for name, f in files.items():
        names.append(name)
        effs.append(getEff(f, num, den, plotType))
    rName  = "%s/%s"%(names[0], names[1])
    ratio  = divideGraphs(effs[0], effs[1])
    ratio.SetName(rName) 
    return ratio


#-----------------------------------------
#Decorate a histogram
#-----------------------------------------
def decoHist(hist, xTit, yTit, color):
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit);
    hist.SetFillColor(color);
    hist.SetLineColor(color);
    hist.SetMarkerColor(color);
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit)
    #hist.GetYaxis().CenterTitle()
    hist.GetXaxis().SetTitleOffset(1.0)
    hist.GetYaxis().SetTitleOffset(1.2)
    hist.GetXaxis().SetTitleSize(0.05);
    hist.GetYaxis().SetTitleSize(0.05);
    hist.GetXaxis().SetTitleSize(0.05);
    hist.GetYaxis().SetTitleSize(0.05);
    hist.GetXaxis().SetTickLength(0.04);
    hist.GetXaxis().SetMoreLogLabels();
    hist.GetXaxis().SetNoExponent()

def decoHistRatio(hist, xTit, yTit, color):
    #hist.SetFillColor(color);
    hist.SetLineColor(color);
    hist.GetXaxis().SetTitle(xTit);
    hist.GetYaxis().SetTitle(yTit);
    hist.GetXaxis().SetTitleSize(0.11);
    hist.GetXaxis().SetLabelSize(0.10);
    hist.GetXaxis().SetLabelFont(42);
    #hist.GetXaxis().SetLabelColor(kBlack);
    #hist.GetXaxis().SetAxisColor(kBlack);
    hist.GetYaxis().SetRangeUser(0.0, 2.0);
    hist.GetXaxis().SetTitleOffset(1);
    hist.GetXaxis().SetLabelOffset(0.01);
    hist.SetMarkerStyle(20); 
    hist.SetMarkerColor(color)
    #hist.SetMarkerSize(1.2);
    hist.GetYaxis().SetTitleSize(0.11);
    hist.GetYaxis().SetLabelSize(0.10);
    hist.GetYaxis().SetLabelFont(42);
    #hist.GetYaxis().SetAxisColor(1);
    hist.GetYaxis().SetNdivisions(6,5,0);
    hist.GetXaxis().SetTickLength(0.08);
    hist.GetYaxis().SetTitleOffset(0.6);
    hist.GetYaxis().SetLabelOffset(0.01);
    hist.GetXaxis().SetMoreLogLabels()
    hist.GetYaxis().CenterTitle();
    hist.GetXaxis().SetNoExponent()

#-----------------------------------------
#Legends for all histograms, graphs
#-----------------------------------------
def decoLegend(legend, nCol, textSize):
    #legend.SetNColumns(nCol);
    legend.SetFillStyle(0);
    legend.SetBorderSize(0);
    #legend.SetFillColor(kBlack);
    legend.SetTextFont(42);
    legend.SetTextAngle(0);
    legend.SetTextSize(textSize);
    legend.SetTextAlign(12);
    return legend

def getLumiLabel(year):
    lumi = "Z #rightarrow ee" # "Z'#rightarrow ee"
    if "16Pre" in year:
        lumi = "19.5 fb^{-1} (2016Pre)"
    if "16Post" in year:
        lumi = "16.8 fb^{-1} (2016Post)"
    if "17" in year:
        lumi = "41.5 fb^{-1} (2017)"
    if "18" in year:
        lumi = "59.8 fb^{-1} (2018)"
    if "__" in year:
        lumi = "138 fb^{-1} (Run2)"
    if "2023" in year:
        lumi = "X fb^{-1} (2023)"
    return lumi

def getChLabel(decay, channel):
    nDict   = {"Semilep": "1", "Dilep":2}
    chDict  = {"Mu": "#mu", "Ele": "e"}
    colDict = {"Mu": ROOT.kBlue, "Ele": ROOT.kRed}
    name = ""
    for ch in channel.split("__"):
        name += "%s#color[%i]{%s}"%(nDict[decay], colDict[ch], chDict[ch])
    name += ", p_{T}^{miss} #geq 20 GeV"
    return name

#-----------------------------------------
#Make efficiency plots
#-----------------------------------------
def makeEff(num, den, plotType, forRatio, forOverlay, padGap=0.01, iPeriod=13, iPosX=10, 
            xPadRange=[0.0,1.0], yPadRange=[0.0,0.30-0.01, 0.30+0.01,1.0], outPlotDir="./plots"):
    """
    Create efficiency plots with optional ratio panels.
    
    Args:
        num (str): Numerator histogram name
        den (str): Denominator histogram name  
        plotType (str): Type of plot (pt, eta, phi)
        forRatio (list): List of ratio pairs to plot
        forOverlay (dict): Dictionary of files to overlay
        padGap (float): Gap between pads
        iPeriod (int): CMS period
        iPosX (int): X position for CMS label
        xPadRange (list): X range for pads
        yPadRange (list): Y range for pads
        outPlotDir (str): Output directory for plots
    """
    # Define x-axis ranges for different plot types
    xRanges = {
        "pt": [0, 4000],      # pT range: 0-4000 GeV
        "pt_TurnOn": [0, 200], 
        "eta": [-4.0, 4.0],   # Eta range: -4.0 to 4.0 
        "phi": [-3.2, 3.2]    # Phi range: -π to π (approximately)
    }
    
    # Get the appropriate x-range for this plot type
    xRange = xRanges.get(plotType, [0, 4000])  # Default fallback
    
    gROOT.SetBatch(True)
    canvas = TCanvas()
    if len(forRatio)>0: 
        canvas.Divide(1, 2)
        canvas.cd(1)
        gPad.SetRightMargin(0.03);
        gPad.SetPad(xPadRange[0],yPadRange[2],xPadRange[1],yPadRange[3]);
        gPad.SetTopMargin(0.09);
        gPad.SetBottomMargin(padGap);
        #gPad.SetTickx(0);
        gPad.RedrawAxis();
    else:
        canvas.cd()

    #get files
    files = forOverlay

    #get effs 
    effs = []
    file_names = []  # Track file names to debug
    for name, f in files.items(): 
        print(f"DEBUG: Processing file '{name}' with TFile pointer: {f}")
        eff   = getEff(f, num, den, plotType)  # Use TEfficiency for top panel (TGraphAsymmErrors)
        effs.append(eff)
        file_names.append(name)
        print(f"DEBUG: Created efficiency graph '{eff.GetName()}' for file '{name}'")

    #plot effs
    #leg = TLegend(0.25,0.85,0.95,0.92); 
    leg = TLegend(0.36,0.4,0.8,0.5); 
    decoLegend(leg, 4, 0.027)
    for index, (name, f) in enumerate(files.items()): 
        eff = effs[index]
        print(f"DEBUG: Plotting index {index}, file '{name}', histogram '{eff.GetName()}'")
        # Set x-axis title based on plot type
        xTitles = {
            "pt": "p_{T} [GeV]",
            "pt_TurnOn": "p_{T} [GeV]",
            "eta": "#eta",
            "phi": "#phi [rad]"
        }
        xTitle = xTitles.get(plotType, num)  # Default to histogram name if plotType not found
        yTitle = "HLT  Efficiency"
        decoHist(eff, xTitle, yTitle, index+1)
        eff.SetMaximum(1.25)
        eff.SetMinimum(0.3)
        
        # Force exact same x-axis range for alignment
        eff.GetXaxis().SetRangeUser(xRange[0], xRange[1])
        eff.GetXaxis().SetLimits(xRange[0], xRange[1])  # Force limits for TGraph
        
        # Force identical x-axis settings for alignment
        #eff.GetXaxis().SetNdivisions(510)
        #eff.GetXaxis().SetMoreLogLabels()
        eff.GetXaxis().SetNoExponent()
                
        # # Add transparency to see overlap better
        # if index == 0:  # First line (black)
        #     eff.SetLineWidth(3)
        #     eff.SetMarkerSize(1.2)
        # else:  # Second line (red) 
        #     eff.SetLineWidth(2)
        #     eff.SetMarkerSize(1.0)
        #     eff.SetLineStyle(2)  # Dashed line for second curve
        
        if index==0:
            eff.Draw("AP")  # Use AP for TGraphAsymmErrors
        else:
            eff.Draw("Psame")  # Use Psame for TGraphAsymmErrors
        #leg.AddEntry(eff, "%s"%(eff.GetName().replace("HistNano_", "")), "APL")
        leg.AddEntry(eff, "%s"%(name), "APL")  # Use APL for TGraphAsymmErrors
        
        # Debug: Print efficiency values to check if both are plotted
        if hasattr(eff, 'GetNbinsX'):  # TH1
            print(f"DEBUG: {name} - Efficiency histogram has {eff.GetNbinsX()} bins")
            print(f"DEBUG: {name} - First bin: {eff.GetBinContent(1):.3f} ± {eff.GetBinError(1):.3f}")
            print(f"DEBUG: {name} - Last bin: {eff.GetBinContent(eff.GetNbinsX()):.3f} ± {eff.GetBinError(eff.GetNbinsX()):.3f}")
        else:  # TGraphAsymmErrors
            print(f"DEBUG: {name} - Efficiency graph has {eff.GetN()} points")
            x, y = c_double(0.0), c_double(0.0)
            eff.GetPoint(0, x, y)
            ey_low = eff.GetErrorYlow(0)
            ey_high = eff.GetErrorYhigh(0)
            print(f"DEBUG: {name} - First point: {y.value:.3f} ± [{ey_low:.3f}, {ey_high:.3f}]")
            
            eff.GetPoint(eff.GetN()-1, x, y)
            ey_low = eff.GetErrorYlow(eff.GetN()-1)
            ey_high = eff.GetErrorYhigh(eff.GetN()-1)
            print(f"DEBUG: {name} - Last point: {y.value:.3f} ± [{ey_low:.3f}, {ey_high:.3f}]")
        #leg.AddEntry(eff, "%s"%(eff.GetName()), "APL")
    
    #Draw CMS, Lumi, channel
    extraText  = "Phase2 Simulation"
    year = "XYZ"
    lumi_13TeV = getLumiLabel(year)
    CMS_lumi(lumi_13TeV, canvas, iPeriod, iPosX, extraText)
    leg.Draw()
    
    # Ratio Plots
    if len(forRatio)>0: 
        canvas.cd(2)
        gPad.SetTopMargin(padGap); 
        gPad.SetBottomMargin(0.30); 
        gPad.SetRightMargin(0.03);
        #gPad.SetTickx(0);
        gPad.SetPad(xPadRange[0],yPadRange[0],xPadRange[1],yPadRange[2]);
        gPad.RedrawAxis();
        rLeg = TLegend(0.25,0.75,0.95,0.85); 
        decoLegend(rLeg, 4, 0.085)
        # Build efficiencies as TH1 for proper ratio calculation
        eff1_h = getEffTH1(forOverlay[forRatio[1]], num, den, plotType)  # numerator (newer)
        eff0_h = getEffTH1(forOverlay[forRatio[0]], num, den, plotType)  # denominator (older)

        eff1_h.Sumw2(); eff0_h.Sumw2()
        hRatio = eff1_h.Clone(f"ratio_{forRatio[1]}_{forRatio[0]}")
        hRatio.Divide(eff0_h)  # standard propagated errors for ratio of two efficiencies
        
        # Convert TH1 ratio to TGraphAsymmErrors for plotting consistency
        gRatio = ROOT.TGraphAsymmErrors()
        point_index = 0
        for i in range(1, hRatio.GetNbinsX() + 1):
            x = hRatio.GetBinCenter(i)
            y = hRatio.GetBinContent(i)
            ey = hRatio.GetBinError(i)  # Symmetric y error
            
            # Only add points that have data (similar to TEfficiency behavior)
            if plotType == "eta" or plotType == "phi":
                if y > 0 or ey > 0:  # Only include bins with content or errors
                    ex = hRatio.GetBinWidth(i) / 2.0  # Half bin width for x error
                    gRatio.SetPoint(point_index, x, y)
                    gRatio.SetPointError(point_index, ex, ex, ey, ey)  # Symmetric errors
                    point_index += 1
            elif plotType == "pt" or plotType == "pt_TurnOn":
                ex = hRatio.GetBinWidth(i) / 2.0  # Half bin width for x error                ex = hRatio.GetBinWidth(i) / 2.0  # Half bin width for x error
                gRatio.SetPoint(point_index, x, y)
                gRatio.SetPointError(point_index, ex, ex, ey, ey)  # Symmetric errors
                point_index += 1
                                
        gRatio.SetName(f"{forRatio[1]}/{forRatio[0]}")
        decoHistRatio(gRatio, xTitle, "Ratio", 1)
        gRatio.GetYaxis().SetRangeUser(0.7, 1.3)
        
        # Get the actual range from the top panel efficiency curves
        top_min_x = effs[0].GetXaxis().GetXmin()
        top_max_x = effs[0].GetXaxis().GetXmax()
        print(f"DEBUG: Top panel x-range: [{top_min_x:.2f}, {top_max_x:.2f}]")
        
        # Get the number of points in the top panel
        top_n_points = effs[0].GetN()
        print(f"DEBUG: Top panel has {top_n_points} points")
        
        # Force ratio panel to match top panel's exact range
        gRatio.GetXaxis().SetRangeUser(top_min_x, top_max_x)
        gRatio.GetXaxis().SetLimits(top_min_x, top_max_x)
        
        # Print ratio panel info for comparison
        ratio_min_x = gRatio.GetXaxis().GetXmin()
        ratio_max_x = gRatio.GetXaxis().GetXmax()
        ratio_n_points = gRatio.GetN()
        print(f"DEBUG: Ratio panel x-range: [{ratio_min_x:.2f}, {ratio_max_x:.2f}]")
        print(f"DEBUG: Ratio panel has {ratio_n_points} points")
        print(f"DEBUG: Original TH1 ratio had {hRatio.GetNbinsX()} bins")
        
        # Force identical x-axis settings for perfect alignment
        #hRatio.GetXaxis().SetNdivisions(510)  # Same as efficiency panel
        #hRatio.GetXaxis().SetMoreLogLabels()
        hRatio.GetXaxis().SetNoExponent()
        hRatio.GetXaxis().SetTitleOffset(1.0)  # Same as efficiency panel
        hRatio.GetXaxis().SetTitleSize(0.05)   # Same as efficiency panel
        hRatio.GetXaxis().SetLabelSize(0.05)   # Same as efficiency panel
        
        # Create baseline with the correct range
        baseLine = TF1("baseLine","1", xRange[0], xRange[1]);
        baseLine.SetLineColor(1);  # Black color
        baseLine.SetLineStyle(2);  # Make it dashed
        baseLine.SetLineWidth(2);  # Make it thicker for better visibility
        
        gRatio.Draw("AP")  # Use AP for TGraphAsymmErrors (same as top panel)
        baseLine.Draw("same")  # Draw the dashed line on top
        rLeg.AddEntry(gRatio, "%s"%(gRatio.GetName()), "APL")  # Use APL for TGraphAsymmErrors
        rLeg.AddEntry(baseLine, "Unity", "L")  # Add legend entry for the line
        #rLeg.Draw()
    #pdf = "%s/effPlot_%s.pdf"%(outPlotDir, num)
    pdf = "./plots/effPlot_%s.pdf"%(num)
    png = pdf.replace("pdf", "png")
    canvas.SaveAs(pdf)
    canvas.SaveAs(png)
