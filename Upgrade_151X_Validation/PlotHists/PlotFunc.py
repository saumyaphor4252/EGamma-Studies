import ROOT as rt
import numpy as np
import sys
from ctypes import c_double

#-----------------------------------------
#Get, add, substract histograms 
#-----------------------------------------
def getEff(inFile, num, den):
    try:
        hPass = inFile.Get(num)
        hAll  = inFile.Get(den)
        
        # Add debug information
        if not hPass:
            print(f"Error: Numerator histogram '{num}' not found in file {inFile.GetName()}")
            print(f"Available histograms in file:")
            for key in inFile.GetListOfKeys():
                print(f"  - {key.GetName()}")
            sys.exit(1)
        if not hAll:
            print(f"Error: Denominator histogram '{den}' not found in file {inFile.GetName()}")
            print(f"Available histograms in file:")
            for key in inFile.GetListOfKeys():
                print(f"  - {key.GetName()}")
            sys.exit(1)
            
        # Verify the objects are histograms
        if not isinstance(hPass, rt.TH1):
            print(f"Error: '{num}' is not a histogram (type: {type(hPass)})")
            sys.exit(1)
        if not isinstance(hAll, rt.TH1):
            print(f"Error: '{den}' is not a histogram (type: {type(hAll)})")
            sys.exit(1)
            
        hPass.GetXaxis().SetTitle(num)
        pEff = rt.TGraphAsymmErrors(hPass, hAll)
        pEff.SetName(num)
        return pEff
        
    except Exception as e:
        print(f"Error in getEff: {str(e)}")
        print(f"File: {inFile.GetName()}")
        print(f"Numerator: {num}")
        print(f"Denominator: {den}")
        sys.exit(1)

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
def getRatio(files, num, den):
    effs  = []
    names = []
    for name, f in files.items():
        names.append(name)
        effs.append(getEff(f, num, den))
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
    lumi = "Run4 MC (14 TeV)"
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
