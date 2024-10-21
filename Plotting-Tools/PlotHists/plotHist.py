import os
import sys
import json
sys.dont_write_bytecode = True
from PlotFunc import *
from Inputs import *
from PlotCMSLumi import *
from PlotTDRStyle import *
from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors

padGap = 0.01
iPeriod = 4;
iPosX = 10;
ModTDRStyle()
xPadRange = [0.0,1.0]
yPadRange = [0.0,0.30-padGap, 0.30+padGap,1.0]

os.system("rm -r %s"%outPlotDir)
os.system("mkdir -p %s"%outPlotDir)


######################################################################
############### What does the fn do
############### What is the input
############### What is the output
######################################################################

def makeEff(num, den):
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

    # For plot effs
    leg = TLegend(0.5,0.4,0.7,0.5);
    #leg = TLegend(0.6,0.72,0.9,0.9);
    decoLegend(leg, 4, 0.027)

    #get effs 
    effs = []
    for name, f in files.items(): 
        eff   = getEff(f, num, den)
        effs.append(eff)
        print(name)
        leg.AddEntry(eff, name, "APL")


    #plot effs
    #leg = TLegend(0.25,0.85,0.95,0.92); 
    #decoLegend(leg, 4, 0.027)

    #Legend = ["Winter24", "Summer23BPix"]
    for index, eff in enumerate(effs): 
        xTitle = num #"Electron p_T"
        yTitle = "Efficiency"
        temp = 0
        decoHist(eff, xTitle, yTitle, index+1)
        eff.SetMaximum(1.3)
        eff.SetMinimum(0.0)
        eff.GetXaxis().SetRangeUser(10, 400)
        if index==0:
            eff.Draw("AP")
        else:
            eff.Draw("Psame")
        #leg.AddEntry(eff, "%s"%(eff.GetName().replace("HistNano_", "")), "APL")
        #leg.AddEntry(eff, "%s"%(forRatio[index]), "APL") 
        #print("Printing the Legend temp...........")
        #print(Legend[temp])
        #temp += 1
        #print(forRatio[index])
        #leg.AddEntry(eff, "%s"%(eff.GetName()), "APL")
    
    #Draw CMS, Lumi, channel
    extraText  = "Preliminary"
    year = "XYZ"
    lumi_13TeV = getLumiLabel(year)
    CMS_lumi(lumi_13TeV, canvas, iPeriod, iPosX, extraText)
    leg.Draw()
    
    #Ratio plots
    if len(forRatio)>0: 
        canvas.cd(2)
        gPad.SetTopMargin(padGap); 
        gPad.SetBottomMargin(0.30); 
        gPad.SetRightMargin(0.03);
        #gPad.SetTickx(0);
        gPad.SetPad(xPadRange[0],yPadRange[0],xPadRange[1],yPadRange[2]);
        gPad.RedrawAxis();
        rLeg = TLegend(0.15, 0.15, 0.35, 0.35); 
        decoLegend(rLeg, 4, 0.085)
        baseLine = TF1("baseLine","1", -100, 10000);
        baseLine.SetLineColor(3);
        #baseLine.Draw()
        for index_, two in enumerate(forRatio):
            files = {}
            files[two[0]] = forOverlay[two[0]]
            files[two[1]] = forOverlay[two[1]]
            hRatio = getRatio(files, num, den)
            #decoHistRatio(hRatio, xTitle, "Ratio", index_+1)
            decoHistRatio(hRatio, xTitle, "2024 / 2023", index_+1)
            hRatio.GetYaxis().SetRangeUser(0.7, 1.3)
            hRatio.GetXaxis().SetRangeUser(-2.5,2.5)#(10, 400)
            if index_==0:
                hRatio.Draw("AP")
            else:
                hRatio.Draw("Psame")
            rLeg.AddEntry(hRatio, "%s"%(hRatio.GetName()), "L")
        #rLeg.Draw()
    #pdf = "%s/effPlot_%s.pdf"%(outPlotDir, num)
    pdf = "./plots/effPlot_%s.pdf"%(num)
    png = pdf.replace("pdf", "png")
    #canvas.SaveAs(pdf)
    canvas.SaveAs("./plots/effPlot_{}.pdf".format(num))
    canvas.SaveAs("./plots/effPlot_{}.png".format(num))


#for num in numPtEE:
#    makeEff(num, "den_ele_pt_EE")
#for num in numPtEB:
#    makeEff(num, "den_ele_pt_EB")
#for num in numEta:
#    makeEff(num, "den_ele_eta")

makeEff("num_ele_pt_EE", "den_ele_pt_EE")
makeEff("num_ele_pt_EE1", "den_ele_pt_EE1")
makeEff("num_ele_pt_EE2", "den_ele_pt_EE2")
makeEff("num_ele_pt_EB", "den_ele_pt_EB")
makeEff("num_ele_pt_EB1", "den_ele_pt_EB1")
makeEff("num_ele_pt_EB2", "den_ele_pt_EB2")
makeEff("num_ele_pt", "den_ele_pt")
#for filter in filters:
    #print(filter)
    #makeEff("num_ele_eta_hltEGL1SingleEGOrFilter", "den_ele_eta")
    #makeEff("num_ele_phi_{}".format(filter), "den_ele_phi")
makeEff("num_ele_pt", "den_ele_pt")
makeEff("num_ele_phi", "den_ele_phi")
