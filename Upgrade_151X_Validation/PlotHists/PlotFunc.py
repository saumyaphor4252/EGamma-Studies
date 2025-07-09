import ROOT as rt
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
    #if(rt.TEfficiency::CheckConsistency(hPass, hAll)):
    
    # Set x-axis title based on plot type
    xTitles = {
        "pt": "p_{T} [GeV]",
        "pt_TurnOn": "p_{T} [GeV]",
        "eta": "#eta",
        "phi": "#phi [rad]"
    }
    xTitle = xTitles.get(plotType, num)  # Default to histogram name if plotType not found
    hPass.GetXaxis().SetTitle(xTitle)
    
    #pEff = rt.TEfficiency(hPass, hAll)
    pEff = rt.TGraphAsymmErrors(hPass, hAll)
    pEff.SetName(num)
    return pEff

def divideGraphs(graph1, graph2): #from ChatGPT
    result_graph = rt.TGraphAsymmErrors()
    # Loop over the points in graph1 and graph2
    n_points = graph1.GetN()
    for i in range(n_points):
        # Get the values and errors for each point in graph1
        x1 = c_double(0.0)
        y1 = c_double(0.0)
        exl1 = graph1.GetErrorXlow(i)
        exh1 = graph1.GetErrorXhigh(i)
        eyl1 = graph1.GetErrorYlow(i)
        eyh1 = graph1.GetErrorYhigh(i)
        graph1.GetPoint(i, x1, y1)

        # Get the values and errors for the corresponding point in graph2
        x2 = c_double(0.0)
        y2 = c_double(0.0)
        exl2 = graph2.GetErrorXlow(i)
        exh2 = graph2.GetErrorXhigh(i)
        eyl2 = graph2.GetErrorYlow(i)
        eyh2 = graph2.GetErrorYhigh(i)
        graph2.GetPoint(i, x2, y2)

        # Perform the division of y values and errors
        result_y = y1.value / y2.value if y2.value != 0 else 0.0
        result_eyl = (eyl1 / y2.value) if y2.value != 0 else 0.0
        result_eyh = (eyh1 / y2.value) if y2.value != 0 else 0.0
        
        # Set the values and errors to the result graph
        result_graph.SetPoint(i, x1.value, result_y)
        result_graph.SetPointError(i, exl1, exh1, result_eyl, result_eyh)
    return result_graph


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
    lumi = "Run4MC"
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
    colDict = {"Mu": rt.kBlue, "Ele": rt.kRed}
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
        "pt": [0, 4000],      # pT range: 0-1000 GeV
        "pt_TurnOn": [0, 200], 
        "eta": [-4.0, 4.0],   # Eta range: -3 to 3
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
    for name, f in files.items(): 
        eff   = getEff(f, num, den, plotType)
        effs.append(eff)

    #plot effs
    #leg = TLegend(0.25,0.85,0.95,0.92); 
    leg = TLegend(0.36,0.4,0.8,0.5); 
    decoLegend(leg, 4, 0.027)
    for index, eff in enumerate(effs): 
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
        eff.SetMaximum(1.2)
        eff.SetMinimum(0.1)
        eff.GetXaxis().SetRangeUser(xRange[0], xRange[1])
        if index==0:
            eff.Draw("AP")
        else:
            eff.Draw("Psame")
        #leg.AddEntry(eff, "%s"%(eff.GetName().replace("HistNano_", "")), "APL")
        leg.AddEntry(eff, "%s"%(forRatio[index]), "APL")
        #print(f"HERE I AM :{forRatio[index]}")
        #leg.AddEntry(eff, "%s"%(eff.GetName()), "APL")
    
    #Draw CMS, Lumi, channel
    extraText  = "Preliminary"
    year = "XYZ"
    lumi_13TeV = getLumiLabel(year)
    CMS_lumi(lumi_13TeV, canvas, iPeriod, iPosX, extraText)
    leg.Draw()
    
    #Ratio lots
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
        baseLine = TF1("baseLine","1", -100, 10000);
        baseLine.SetLineColor(3);
        #baseLine.Draw()
        files = {}
        files[forRatio[0]] = forOverlay[forRatio[0]]  # First version
        files[forRatio[1]] = forOverlay[forRatio[1]]  # Second version
        hRatio = getRatio(files, num, den, plotType)
        decoHistRatio(hRatio, xTitle, "Ratio", 1)
        hRatio.GetYaxis().SetRangeUser(0.7, 1.3)
        hRatio.GetXaxis().SetRangeUser(xRange[0], xRange[1])
        hRatio.Draw("AP")
        rLeg.AddEntry(hRatio, "%s"%(hRatio.GetName()), "L")
        #rLeg.Draw()
    #pdf = "%s/effPlot_%s.pdf"%(outPlotDir, num)
    pdf = "./plots/effPlot_%s.pdf"%(num)
    png = pdf.replace("pdf", "png")
    canvas.SaveAs(pdf)
    canvas.SaveAs(png)
