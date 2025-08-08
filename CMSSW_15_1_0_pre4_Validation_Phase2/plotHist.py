import os
import logging
import sys
import json
sys.dont_write_bytecode = True
from PlotFunc import *
from Inputs import *
from PlotCMSLumi import *
from PlotTDRStyle import *
from ROOT import TFile, TLegend, gPad, gROOT, TCanvas, THStack, TF1, TH1F, TGraphAsymmErrors
from filter_configs import FILTERS, get_filters_for_path, get_denominator_filter

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

padGap = 0.01
iPeriod = 13;
iPosX = 10;
ModTDRStyle()
xPadRange = [0.0,1.0]
yPadRange = [0.0,0.30-padGap, 0.30+padGap,1.0]

os.system("rm -r %s"%outPlotDir)
os.system("mkdir -p %s"%outPlotDir)

for PlotType in ["pt", "eta", "phi"]:
#for PlotType in ["pt_TurnOn"]:
    #for region in ["_EB", "_EE", ""]:
    for region in [""]:
        for trigger_name, filter_list in FILTERS.items():
            # Use consistent naming: trigger_name_den_ele_PlotType_region
            denominator_filter = get_denominator_filter(trigger_name)
            #denominator = f"{trigger_name}_den_ele_{PlotType}_{denominator_filter}{region}"
            denominator = f"{trigger_name}_den_ele_{PlotType}{region}"
            for filter_name in filter_list:
                numerator = f"{trigger_name}_num_ele_{PlotType}{region}_{filter_name}"
                logger.info(f"Processing {PlotType} {region} plot for {numerator} and {denominator}")
                makeEff(numerator, denominator, PlotType, forRatio, forOverlay, padGap, iPeriod, iPosX, xPadRange, yPadRange, outPlotDir)
