import os
import logging
from ROOT import TCanvas, TLegend, gPad, gROOT, TF1
from config import *
from PlotFunc import *
from PlotCMSLumi import *

logger = logging.getLogger(__name__)

class EfficiencyPlotter:
    def __init__(self, output_dir=OUTPUT_DIR):
        self.output_dir = output_dir
        self._setup_output_dir()
        
    def _setup_output_dir(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
        
    def create_canvas(self, has_ratio=False):
        """Create and configure the canvas"""
        canvas = TCanvas()
        if has_ratio:
            canvas.Divide(1, 2)
            canvas.cd(1)
            gPad.SetRightMargin(0.03)
            gPad.SetPad(*X_PAD_RANGE, *Y_PAD_RANGE[2:])
            gPad.SetTopMargin(0.09)
            gPad.SetBottomMargin(PAD_GAP)
            gPad.RedrawAxis()
        else:
            canvas.cd()
        return canvas
        
    def create_legend(self, is_ratio=False):
        """Create and configure the legend"""
        config = LEGEND_CONFIG['ratio' if is_ratio else 'main']
        leg = TLegend(config['x1'], config['y1'], config['x2'], config['y2'])
        decoLegend(leg, config['columns'], config['text_size'])
        return leg
        
    def plot_efficiency(self, num, den, files, for_ratio=None):
        """Main method to create efficiency plots"""
        try:
            gROOT.SetBatch(True)
            canvas = self.create_canvas(bool(for_ratio))
            
            # Process efficiencies
            effs = []
            for name, f in files.items():
                logger.info(f"Processing efficiency for {name}")
                eff = getEff(f, num, den)
                effs.append(eff)
                
            # Plot efficiencies
            leg = self.create_legend()
            for index, eff in enumerate(effs):
                self._decorate_and_draw_hist(eff, num, index, leg)
                
            # Add CMS and luminosity information
            self._add_cms_info(canvas)
            leg.Draw()
            
            # Handle ratio plots if needed
            if for_ratio:
                self._plot_ratio(canvas, for_ratio, files, num, den)
                
            # Save the plot
            self._save_plot(canvas, num)
            
        except Exception as e:
            logger.error(f"Error in plot_efficiency: {e}")
            raise
            
    def _decorate_and_draw_hist(self, hist, x_title, index, legend):
        """Decorate and draw a histogram"""
        decoHist(hist, x_title, "Efficiency", index + 1)
        hist.SetMaximum(PLOT_STYLE['maximum'])
        hist.SetMinimum(PLOT_STYLE['minimum'])
        hist.GetXaxis().SetRangeUser(*PLOT_STYLE['x_range'])
        
        if index == 0:
            hist.Draw("AP")
        else:
            hist.Draw("Psame")
            
        legend.AddEntry(hist, hist.GetName().replace("HistNano_", ""), "APL")
        
    def _add_cms_info(self, canvas):
        """Add CMS and luminosity information to the plot"""
        extra_text = "Preliminary"
        year = "XYZ"
        lumi_13TeV = getLumiLabel(year)
        CMS_lumi(lumi_13TeV, canvas, None, 10, extra_text)
        
    def _plot_ratio(self, canvas, for_ratio, files, num, den):
        """Create ratio plots"""
        canvas.cd(2)
        gPad.SetTopMargin(PAD_GAP)
        gPad.SetBottomMargin(0.30)
        gPad.SetRightMargin(0.03)
        gPad.SetPad(*X_PAD_RANGE, *Y_PAD_RANGE[:2])
        gPad.RedrawAxis()
        
        r_leg = self.create_legend(is_ratio=True)
        base_line = TF1("baseLine", "1", -100, 10000)
        base_line.SetLineColor(3)
        
        for index_, two in enumerate(for_ratio):
            ratio_files = {two[0]: files[two[0]], two[1]: files[two[1]]}
            h_ratio = getRatio(ratio_files, num, den)
            decoHistRatio(h_ratio, num, "Ratio", index_ + 1)
            h_ratio.GetYaxis().SetRangeUser(*PLOT_STYLE['y_range'])
            h_ratio.GetXaxis().SetRangeUser(*PLOT_STYLE['x_range'])
            
            if index_ == 0:
                h_ratio.Draw("AP")
            else:
                h_ratio.Draw("Psame")
            r_leg.AddEntry(h_ratio, h_ratio.GetName(), "L")
            
    def _save_plot(self, canvas, num):
        """Save the plot to file"""
        png_path = os.path.join(self.output_dir, f"effPlot_{num}.png")
        canvas.SaveAs(png_path)
        logger.info(f"Plot saved to {png_path}") 