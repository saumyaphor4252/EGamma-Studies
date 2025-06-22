import sys
import logging
sys.dont_write_bytecode = True
from plotter import EfficiencyPlotter
from Inputs import forOverlay
from filter_configs import FILTERS, get_filters_for_path, get_denominator_filter

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        plotter = EfficiencyPlotter()
        
        for PlotType in ["pt", "eta", "phi"]:
            for region in ["_EB", "_EE", ""]:
                for trigger_name, filter_list in FILTERS.items():
                    # Use consistent naming: trigger_name_den_ele_PlotType_region
                    denominator_filter = get_denominator_filter(trigger_name)
                    #denominator = f"{trigger_name}_den_ele_{PlotType}_{denominator_filter}{region}"
                    denominator = f"{trigger_name}_den_ele_{PlotType}{region}"
                    for filter_name in filter_list:
                        numerator = f"{trigger_name}_num_ele_{PlotType}_{filter_name}{region}"
                        logger.info(f"Processing {PlotType} {region} plot for {numerator} and {denominator}")
                        plotter.plot_efficiency(numerator, denominator, forOverlay)
            
    except Exception as e:
        logger.error(f"Error in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()    
