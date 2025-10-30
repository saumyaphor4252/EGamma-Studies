"""
Filter configurations for HLT paths.
This module contains the filter configurations for different HLT paths used in the analysis.
Each HLT path has its associated filters that are used for efficiency calculations.
"""

# Dictionary containing filter configurations for different HLT paths
FILTERS = {
    "HLTEle26WP70L1Seeded": [
        'hltEGL1SeedsForSingleEleIsolatedFilter',
        'hltEG26EtL1SeededFilter',
        'hltEle26WP70ClusterShapeL1SeededFilter',
        'hltEle26WP70ClusterShapeSigmavvL1SeededFilter',
        'hltEle26WP70ClusterShapeSigmawwL1SeededFilter',
        'hltEle26WP70HgcalHEL1SeededFilter',
        'hltEle26WP70HEL1SeededFilter',
        'hltEle26WP70EcalIsoL1SeededFilter',
        'hltEle26WP70HgcalIsoL1SeededFilter',
        'hltEle26WP70HcalIsoL1SeededFilter',
        'hltEle26WP70PixelMatchL1SeededFilter',
        'hltEle26WP70PMS2L1SeededFilter',
        'hltEle26WP70GsfOneOEMinusOneOPL1SeededFilter',
        'hltEle26WP70GsfDetaL1SeededFilter',
        'hltEle26WP70GsfDphiL1SeededFilter',
        'hltEle26WP70BestGsfNLayerITL1SeededFilter',
        'hltEle26WP70BestGsfChi2L1SeededFilter',
        'hltEle26WP70GsfTrackIsoFromL1TracksL1SeededFilter',
        'hltEle26WP70GsfTrackIsoL1SeededFilter'
    ],
    "HLTEle26WP70Unseeded": [
        'hltEGL1SeedsForSingleEleIsolatedFilter',
        'hltEG26EtUnseededFilter',
        'hltEle26WP70ClusterShapeUnseededFilter',
        'hltEle26WP70ClusterShapeSigmavvUnseededFilter', 
        'hltEle26WP70ClusterShapeSigmawwUnseededFilter',
        'hltEle26WP70HgcalHEUnseededFilter',
        'hltEle26WP70HEUnseededFilter',
        'hltEle26WP70EcalIsoUnseededFilter',
        'hltEle26WP70HgcalIsoUnseededFilter',
        'hltEle26WP70HcalIsoUnseededFilter',
        'hltEle26WP70PixelMatchUnseededFilter',
        'hltEle26WP70PMS2UnseededFilter',
        'hltEle26WP70GsfOneOEMinusOneOPUnseededFilter',
        'hltEle26WP70GsfDetaUnseededFilter', 
        'hltEle26WP70GsfDphiUnseededFilter',
        'hltEle26WP70BestGsfNLayerITUnseededFilter',
        'hltEle26WP70BestGsfChi2UnseededFilter',
        'hltEle26WP70GsfTrackIsoFromL1TracksUnseededFilter',
        'hltEle26WP70GsfTrackIsoUnseededFilter'
    ],
    "HLTEle32WPTightUnseeded": [
        'hltEGL1SeedsForSingleEleIsolatedFilter',
        'hltEG32EtUnseededFilter',
        'hltEle32WPTightClusterShapeUnseededFilter',
        'hltEle32WPTightClusterShapeSigmavvUnseededFilter',
        'hltEle32WPTightClusterShapeSigmawwUnseededFilter', 
        'hltEle32WPTightHgcalHEUnseededFilter',
        'hltEle32WPTightHEUnseededFilter',
        'hltEle32WPTightEcalIsoUnseededFilter',
        'hltEle32WPTightHgcalIsoUnseededFilter',
        'hltEle32WPTightHcalIsoUnseededFilter',
        'hltEle32WPTightPixelMatchUnseededFilter',
        'hltEle32WPTightPMS2UnseededFilter',
        'hltEle32WPTightGsfOneOEMinusOneOPUnseededFilter',
        'hltEle32WPTightGsfDetaUnseededFilter',
        'hltEle32WPTightGsfDphiUnseededFilter', 
        'hltEle32WPTightBestGsfNLayerITUnseededFilter',
        'hltEle32WPTightBestGsfChi2UnseededFilter',
        'hltEle32WPTightGsfTrackIsoFromL1TracksUnseededFilter',
        'hltEle32WPTightGsfTrackIsoUnseededFilter'
    ],
    "HLTEle32WPTightL1Seeded": [
        'hltEGL1SeedsForSingleEleIsolatedFilter',
        'hltEG32EtL1SeededFilter',
        'hltEle32WPTightClusterShapeL1SeededFilter',
        'hltEle32WPTightClusterShapeSigmavvL1SeededFilter',
        'hltEle32WPTightClusterShapeSigmawwL1SeededFilter',
        'hltEle32WPTightHgcalHEL1SeededFilter',
        'hltEle32WPTightHEL1SeededFilter',
        'hltEle32WPTightEcalIsoL1SeededFilter',
        'hltEle32WPTightHgcalIsoL1SeededFilter',
        'hltEle32WPTightHcalIsoL1SeededFilter',
        'hltEle32WPTightPixelMatchL1SeededFilter',
        'hltEle32WPTightPMS2L1SeededFilter',
        'hltEle32WPTightGsfOneOEMinusOneOPL1SeededFilter',
        'hltEle32WPTightGsfDetaL1SeededFilter',
        'hltEle32WPTightGsfDphiL1SeededFilter',
        'hltEle32WPTightBestGsfNLayerITL1SeededFilter',
        'hltEle32WPTightBestGsfChi2L1SeededFilter',
        'hltEle32WPTightGsfTrackIsoFromL1TracksL1SeededFilter',
        'hltEle32WPTightGsfTrackIsoL1SeededFilter'
    ],
    "HLTDoubleEle25CaloIdLPMS2L1Seeded": [
        'hltEGL1SeedsForDoubleEleNonIsolatedFilter',
        'hltDiEG25EtL1SeededFilter', 
        'hltDiEG25CaloIdLClusterShapeL1SeededFilter',
        'hltDiEG25CaloIdLClusterShapeSigmavvL1SeededFilter',
        'hltDiEG25CaloIdLHgcalHEL1SeededFilter', 
        'hltDiEG25CaloIdLHEL1SeededFilter',
        'hltDiEle25CaloIdLPixelMatchL1SeededFilter',
        'hltDiEle25CaloIdLPMS2L1SeededFilter'
    ],
    "HLTDoubleEle25CaloIdLPMS2Unseeded": [
        'hltEGL1SeedsForDoubleEleNonIsolatedFilter',
        'hltDiEG25EtUnseededFilter',
        'hltDiEG25CaloIdLClusterShapeUnseededFilter',
        'hltDiEG25CaloIdLClusterShapeSigmavvUnseededFilter',
        'hltDiEG25CaloIdLHgcalHEUnseededFilter',
        'hltDiEG25CaloIdLHEUnseededFilter',
        'hltDiEle25CaloIdLPixelMatchUnseededFilter',
        'hltDiEle25CaloIdLPMS2UnseededFilter'
    ],
    "HLTDoubleEle2312IsoL1Seeded": [
        'hltEGL1SeedsForDoubleEleIsolatedFilter',
        'hltEG23EtL1SeededFilter',
        'hltDiEG12EtL1SeededFilter', 
        'hltDiEG2312IsoClusterShapeL1SeededFilter',
        'hltDiEG2312IsoClusterShapeSigmavvL1SeededFilter',
        'hltDiEG2312IsoClusterShapeSigmawwL1SeededFilter',
        'hltDiEG2312IsoHgcalHEL1SeededFilter',
        'hltDiEG2312IsoHEL1SeededFilter',
        'hltDiEG2312IsoEcalIsoL1SeededFilter',
        'hltDiEG2312IsoHgcalIsoL1SeededFilter',
        'hltDiEG2312IsoHcalIsoL1SeededFilter',
        'hltDiEle2312IsoPixelMatchL1SeededFilter',
        'hltDiEle2312IsoPMS2L1SeededFilter',
        'hltDiEle2312IsoGsfOneOEMinusOneOPL1SeededFilter',
        'hltDiEle2312IsoGsfDetaL1SeededFilter',
        'hltDiEle2312IsoGsfDphiL1SeededFilter',
        'hltDiEle2312IsoBestGsfNLayerITL1SeededFilter',
        'hltDiEle2312IsoBestGsfChi2L1SeededFilter',
        'hltDiEle2312IsoGsfTrackIsoFromL1TracksL1SeededFilter',
        'hltDiEle2312IsoGsfTrackIsoL1SeededFilter'
    ]
}

# FILTERS = {
#     "HLTEle26WP70L1Seeded": [
#         'hltEGL1SeedsForSingleEleIsolatedFilter',
#         'hltEG26EtL1SeededFilter',
#         'hltEle26WP70GsfTrackIsoL1SeededFilter'
#     ],
#     "HLTEle26WP70Unseeded": [
#         'hltEGL1SeedsForSingleEleIsolatedFilter',
#         'hltEG26EtUnseededFilter',
#         'hltEle26WP70GsfTrackIsoUnseededFilter'
#     ],
#     "HLTEle32WPTightUnseeded": [
#         'hltEGL1SeedsForSingleEleIsolatedFilter',
#         'hltEG32EtUnseededFilter',
#         'hltEle32WPTightGsfTrackIsoUnseededFilter'
#     ],
#     "HLTEle32WPTightL1Seeded": [
#         'hltEGL1SeedsForSingleEleIsolatedFilter',
#         'hltEG32EtL1SeededFilter',
#         'hltEle32WPTightGsfTrackIsoL1SeededFilter'
#     ],
#     "HLTDoubleEle25CaloIdLPMS2L1Seeded": [
#         'hltEGL1SeedsForDoubleEleNonIsolatedFilter',
#         'hltDiEG25EtL1SeededFilter', 
#         'hltDiEle25CaloIdLPMS2L1SeededFilter'
#     ],
#     "HLTDoubleEle25CaloIdLPMS2Unseeded": [
#         'hltEGL1SeedsForDoubleEleNonIsolatedFilter',
#         'hltDiEG25EtUnseededFilter',
#         'hltDiEle25CaloIdLPMS2UnseededFilter'
#     ],
#     "HLTDoubleEle2312IsoL1Seeded": [
#         'hltEGL1SeedsForDoubleEleIsolatedFilter',
#         'hltEG23EtL1SeededFilter',
#         'hltDiEle2312IsoGsfTrackIsoL1SeededFilter'
#     ]
# }

# Helper function to get all available HLT paths
def get_available_paths():
    """
    Get a list of all available HLT paths.
    
    Returns:
        list: List of all HLT path names
    """
    return list(FILTERS.keys())

# Helper function to get filters for a specific HLT path
def get_filters_for_path(path_name):
    """
    Get the list of filters for a specific HLT path.
    
    Args:
        path_name (str): Name of the HLT path
        
    Returns:
        list: List of filters for the specified path
        
    Raises:
        KeyError: If the path name is not found in the configuration
    """
    if path_name not in FILTERS:
        raise KeyError(f"HLT path '{path_name}' not found in filter configurations")
    return FILTERS[path_name]

def get_denominator_filter(path_name):
    """
    Get the first filter from a trigger path (to use as denominator)
    
    Args:
        path_name (str): Name of the HLT path
        
    Returns:
        str: Name of the first filter in the path
    """
    filters = get_filters_for_path(path_name)
    if len(filters) < 2:
        raise ValueError(f"Path {path_name} has less than 2 filters")
    return filters[1]  # Return the second filter (first filter filters[0]currently empty)    

