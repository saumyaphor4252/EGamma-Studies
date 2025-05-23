import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import sys


###################################################################
## argument line options
###################################################################
varOptions = VarParsing('analysis')

def registerOption(optionName, defaultValue, description, optionType=VarParsing.varType.bool):
  varOptions.register(
      optionName, 
      defaultValue,
      VarParsing.multiplicity.singleton,
      optionType,
      description
  )

registerOption('isMC',        False,    'Use MC instead of data')
registerOption('isAOD',       False,    'Use AOD samples instead of miniAOD')
registerOption('is80X',       False,    'Compatibility to run on old 80X files')
registerOption('doEleID',     False,    'Include tree for electron ID SF')
registerOption('doPhoID',     False,    'Include tree for photon ID SF')
registerOption('doTrigger',   False,    'Include tree for trigger SF')
registerOption('doRECO',      False,    'Include tree for Reco SF (requires AOD)')
registerOption('calibEn',     False,    'Use EGM smearer to calibrate photon and electron energy')
registerOption('includeSUSY', False,    'Add also the variables used by SUSY')

#registerOption('HLTname',     'HLT',    'HLT process name (default HLT)', optionType=VarParsing.varType.string) # HLTname was HLT2 in now outdated reHLT samples
registerOption('HLTname',     'MYHLT',    'HLT process name', optionType=VarParsing.varType.string) # Modified
registerOption('GT',          'auto',   'Global Tag to be used', optionType=VarParsing.varType.string)
registerOption('era',         '2018',   'Data-taking era: 2016, 2017, 2018, 2022, 2023, 2023preBPIX, 2023postBPIX, 2024, UL2017 or UL2018', optionType=VarParsing.varType.string)
registerOption('logLevel',    'INFO',   'Loglevel: could be DEBUG, INFO, WARNING, ERROR', optionType=VarParsing.varType.string)

registerOption('L1Threshold',  0,       'Threshold for L1 matched objects', optionType=VarParsing.varType.int)

varOptions.parseArguments()

###################################################################
# Some sanity checks
###################################################################
from EgammaAnalysis.TnPTreeProducer.logger import getLogger
log = getLogger(varOptions.logLevel)
if varOptions.isAOD and varOptions.doEleID:    log.warning('AOD is not supported for doEleID, please consider using miniAOD')
if varOptions.isAOD and varOptions.doPhoID:    log.warning('AOD is not supported for doPhoID, please consider using miniAOD')
if varOptions.isAOD and varOptions.doTrigger:  log.warning('AOD is not supported for doTrigger, please consider using miniAOD')
if not varOptions.isAOD and varOptions.doRECO: log.warning('miniAOD is not supported for doRECO, please consider using AOD')

from EgammaAnalysis.TnPTreeProducer.cmssw_version import isReleaseAbove
if varOptions.era not in ['2016', '2017', '2018', '2022', '2023', '2023preBPIX', '2023postBPIX', '2024', 'UL2016preVFP', 'UL2016postVFP', 'UL2017', 'UL2018']: 
  log.error('%s is not a valid era' % varOptions.era)
#if ('UL' in varOptions.era)!=(isReleaseAbove(10, 6)):
  #log.error('Inconsistent release for era %s. Use CMSSW_10_6_X for UL and CMSSW_10_2_X for rereco' % varOptions.era)

if varOptions.includeSUSY: log.info('Including variables for SUSY')
if varOptions.doEleID:     log.info('Producing electron SF tree')
if varOptions.doPhoID:     log.info('Producing photon SF tree')
if varOptions.doTrigger:   log.info('Producing HLT (trigger ele) efficiency tree')
if varOptions.doRECO:      log.info('Producing RECO SF tree')


###################################################################
## Define TnP inputs
###################################################################

options = dict()
options['useAOD']               = varOptions.isAOD
options['use80X']               = varOptions.is80X

options['HLTProcessName']       = varOptions.HLTname
options['era']                  = varOptions.era

options['ELECTRON_COLL']        = "gedGsfElectrons" if options['useAOD'] else "slimmedElectrons"
options['PHOTON_COLL']          = "gedPhotons" if options['useAOD'] else "slimmedPhotons"
options['SUPERCLUSTER_COLL']    = "reducedEgamma:reducedSuperClusters" ### not used in AOD

options['ELECTRON_CUTS']        = "ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)"
options['SUPERCLUSTER_CUTS']    = "abs(eta)<2.5 &&  et>5.0"
options['PHOTON_CUTS']          = "(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10"
options['ELECTRON_TAG_CUTS']    = "(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && !(1.4442<=abs(-log(tan(superClusterPosition.theta/2)))<=1.566) && pt >= 30.0"

options['MAXEVENTS']            = cms.untracked.int32(varOptions.maxEvents)
#options['MAXEVENTS']            = cms.untracked.int32(1000)
options['DoTrigger']            = varOptions.doTrigger
options['DoRECO']               = varOptions.doRECO
options['DoEleID']              = varOptions.doEleID
options['DoPhoID']              = varOptions.doPhoID

options['DEBUG']                = False 
options['isMC']                 = varOptions.isMC
options['UseCalibEn']           = varOptions.calibEn
options['addSUSY']              = varOptions.includeSUSY and not options['useAOD']

options['OUTPUT_FILE_NAME']     = "TnPTree_%s.root" % ("mc" if options['isMC'] else "data")

log.info('outputfile: %s' % options['OUTPUT_FILE_NAME'])

#################################################
# Settings for global tag
#################################################
if varOptions.GT == "auto":
  if options['isMC']:
    if options['era'] == '2016':   options['GLOBALTAG'] = '94X_mcRun2_asymptotic_v3'
    if options['era'] == '2017':   options['GLOBALTAG'] = '94X_mc2017_realistic_v17'
    if options['era'] == '2018':   options['GLOBALTAG'] = '102X_upgrade2018_realistic_v21'
    if options['era'] == 'UL2016preVFP':  options['GLOBALTAG'] = '106X_mcRun2_asymptotic_preVFP_v9'
    if options['era'] == 'UL2016postVFP': options['GLOBALTAG'] = '106X_mcRun2_asymptotic_v15'
    if options['era'] == 'UL2017': options['GLOBALTAG'] = '106X_dataRun2_v28'
    if options['era'] == 'UL2018': options['GLOBALTAG'] = '106X_dataRun2_v28'
    if options['era'] == '2022': options['GLOBALTAG'] = 'auto:phase1_2022_realistic' 
    if options['era'] == '2023preBPIX': options['GLOBALTAG'] = '130X_mcRun3_2023_realistic_v14' 
    if options['era'] == '2023postBPIX': options['GLOBALTAG'] = '130X_mcRun3_2023_realistic_postBPix_v2'
    if options['era'] == '2024': options['GLOBALTAG'] = '140X_mcRun3_2024_realistic_v14'
  else:
    if options['era'] == '2016':   options['GLOBALTAG'] = '94X_dataRun2_v10'
    if options['era'] == '2017':   options['GLOBALTAG'] = '94X_dataRun2_v11'
    if options['era'] == '2018':   options['GLOBALTAG'] = '102X_dataRun2_v13'
    if options['era'] == 'UL2016preVFP':  options['GLOBALTAG'] = '106X_dataRun2_v32'
    if options['era'] == 'UL2016postVFP': options['GLOBALTAG'] = '106X_dataRun2_v32'
    if options['era'] == 'UL2017': options['GLOBALTAG'] = '106X_mc2017_realistic_v7'
    if options['era'] == 'UL2018': options['GLOBALTAG'] = '106X_upgrade2018_realistic_v11_L1v1'
    if options['era'] == '2022': options['GLOBALTAG'] = '124X_dataRun3_Prompt_v10'
    if options['era'] == '2023': options['GLOBALTAG'] = '130X_dataRun3_PromptAnalysis_v1'
    if options['era'] == '2024': options['GLOBALTAG'] = '140X_dataRun3_Prompt_v3' # GT being used for here
else:
  options['GLOBALTAG'] = varOptions.GT

log.info('Globaltag: %s' % options['GLOBALTAG'])

#################################################
# Settings for trigger tag and probe measurement
#################################################

#Filters used in different paths
#HLT_Ele30_WPTight_Gsf
ele30_allFilters = {'passHLTEG30L1SingleEGOrEtFilter': cms.vstring('hltEG30L1SingleEGOrEtFilter'), 'passHLTEle30WPTightClusterShapeFilter': cms.vstring('hltEle30WPTightClusterShapeFilter'), 'passHLTEle30WPTightHEFilter': cms.vstring('hltEle30WPTightHEFilter'), 'passHLTEle30WPTightEcalIsoFilter': cms.vstring('hltEle30WPTightEcalIsoFilter'), 'passHLTEle30WPTightHcalIsoFilter': cms.vstring('hltEle30WPTightHcalIsoFilter'), 'passHLTEle30WPTightPixelMatchFilter': cms.vstring('hltEle30WPTightPixelMatchFilter'), 'passHLTEle30WPTightPMS2Filter': cms.vstring('hltEle30WPTightPMS2Filter'), 'passHLTEle30WPTightGsfOneOEMinusOneOPFilter': cms.vstring('hltEle30WPTightGsfOneOEMinusOneOPFilter'), 'passHLTEle30WPTightGsfMissingHitsFilter': cms.vstring('hltEle30WPTightGsfMissingHitsFilter'), 'passHLTEle30WPTightGsfDetaFilter': cms.vstring('hltEle30WPTightGsfDetaFilter'), 'passHLTEle30WPTightGsfDphiFilter': cms.vstring('hltEle30WPTightGsfDphiFilter'), 'passHLTEle30WPTightGsfTrackIsoFilter': cms.vstring('hltEle30WPTightGsfTrackIsoFilter')}

#HLT_Ele32_WPTight_Gsf
ele32_allFilters = {'passHLTEG32L1SingleEGOrEtFilter': cms.vstring('hltEG32L1SingleEGOrEtFilter'), 'passHLTEle32WPTightClusterShapeFilter': cms.vstring('hltEle32WPTightClusterShapeFilter'), 'passHLTEle32WPTightHEFilter': cms.vstring('hltEle32WPTightHEFilter'), 'passHLTEle32WPTightEcalIsoFilter': cms.vstring('hltEle32WPTightEcalIsoFilter'), 'passHLTEle32WPTightHcalIsoFilter': cms.vstring('hltEle32WPTightHcalIsoFilter'), 'passHLTEle32WPTightPixelMatchFilter': cms.vstring('hltEle32WPTightPixelMatchFilter'), 'passHLTEle32WPTightPMS2Filter': cms.vstring('hltEle32WPTightPMS2Filter'), 'passHLTEle32WPTightGsfOneOEMinusOneOPFilter': cms.vstring('hltEle32WPTightGsfOneOEMinusOneOPFilter'), 'passHLTEle32WPTightGsfMissingHitsFilter': cms.vstring('hltEle32WPTightGsfMissingHitsFilter'), 'passHLTEle32WPTightGsfDetaFilter': cms.vstring('hltEle32WPTightGsfDetaFilter'), 'passHLTEle32WPTightGsfDphiFilter': cms.vstring('hltEle32WPTightGsfDphiFilter'), 'passHLTEle32WPTightGsfTrackIsoFilter': cms.vstring('hltEle32WPTightGsfTrackIsoFilter')}

#HLT_Ele115_CaloIdVT_GsfTrkIdT
ele115_allFilters = {'passHLTEGL1SingleEGNonIsoOrWithJetAndTauFilter': cms.vstring('hltEGL1SingleEGNonIsoOrWithJetAndTauFilter'), 'passHLTEG115EtFilter': cms.vstring('hltEG115EtFilter'), 'passHLTEG115CaloIdVTClusterShapeFilter': cms.vstring('hltEG115CaloIdVTClusterShapeFilter'), 'passHLTEG115CaloIdVTHEFilter': cms.vstring('hltEG115CaloIdVTHEFilter'), 'passHLTEle115CaloIdVTPixelMatchFilter': cms.vstring('hltEle115CaloIdVTPixelMatchFilter'), 'passHLTEle115CaloIdVTGsfTrkIdTGsfDetaFilter': cms.vstring('hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter'), 'passHLTEle115CaloIdVTGsfTrkIdTGsfDphiFilter': cms.vstring('hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter')}

#HLT_Ele135_CaloIdVT_GsfTrkIdT
ele135_allFilters = {'passHLTEG135EtFilter': cms.vstring('hltEG135EtFilter'), 'passHLTEG135CaloIdVTClusterShapeFilter': cms.vstring('hltEG135CaloIdVTClusterShapeFilter'), 'passHLTEG135CaloIdVTHEFilter': cms.vstring('hltEG135CaloIdVTHEFilter'), 'passHLTEle135CaloIdVTPixelMatchFilter': cms.vstring('hltEle135CaloIdVTPixelMatchFilter'), 'passHLTEle135CaloIdVTGsfTrkIdTGsfDetaFilter': cms.vstring('hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter'), 'passHLTEle135CaloIdVTGsfTrkIdTGsfDphiFilter': cms.vstring('hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter')}

#HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL
ele23ele12_allFilters = {'passHLTEGL1SingleAndDoubleEGOrPairFilter': cms.vstring('hltEGL1SingleAndDoubleEGOrPairFilter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter')}

#HLT_DoubleEle33_CaloIdL_MW
doubleEle33_leg1_allFilters = {'passHLTEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter': cms.vstring('hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter'), 'passHLTEG33EtFilter': cms.vstring('hltEG33EtFilter'), 'passHLTEG33HEFilter': cms.vstring('hltEG33HEFilter'), 'passHLTEG33CaloIdLClusterShapeFilter': cms.vstring('hltEG33CaloIdLClusterShapeFilter'), 'passHLTEle33CaloIdLPixelMatchFilter': cms.vstring('hltEle33CaloIdLPixelMatchFilter'), 'passHLTEle33CaloIdLMWPMS2Filter': cms.vstring('hltEle33CaloIdLMWPMS2Filter')}

#HLT_DoubleEle33_CaloIdL_MW
doubleEle33_leg2_allFilters = {'passHLTDiEG33EtUnseededFilter': cms.vstring('hltDiEG33EtUnseededFilter'), 'passHLTDiEG33HEUnseededFilter': cms.vstring('hltDiEG33HEUnseededFilter'), 'passHLTDiEG33CaloIdLClusterShapeUnseededFilter': cms.vstring('hltDiEG33CaloIdLClusterShapeUnseededFilter'), 'passHLTDiEle33CaloIdLPixelMatchUnseededFilter': cms.vstring('hltDiEle33CaloIdLPixelMatchUnseededFilter'), 'passHLTDiEle33CaloIdLMWPMS2UnseededFilter': cms.vstring('hltDiEle33CaloIdLMWPMS2UnseededFilter')}

if '2016' in options['era']:
  options['TnPPATHS']           = cms.vstring("HLT_Ele27_eta2p1_WPTight_Gsf_v*")
  options['TnPHLTTagFilters']   = cms.vstring("hltEle27erWPTightGsfTrackIsoFilter")
  options['TnPHLTProbeFilters'] = cms.vstring()
  options['HLTFILTERSTOMEASURE']= {"passHltEle27WPTightGsf" :                           cms.vstring("hltEle27WPTightGsfTrackIsoFilter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match" : cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2" :        cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter"),
                                   "passHltDoubleEle33CaloIdLMWSeedLegL1match" :        cms.vstring("hltEG33CaloIdLMWPMS2Filter"),
                                   "passHltDoubleEle33CaloIdLMWUnsLeg" :                cms.vstring("hltDiEle33CaloIdLMWPMS2UnseededFilter"),
                                  } # Some examples, you can add multiple filters (or OR's of filters, note the vstring) here, each of them will be added to the tuple

elif '2017' in options['era']:
  options['TnPPATHS']           = cms.vstring("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*")
  options['TnPHLTTagFilters']   = cms.vstring("hltEle32L1DoubleEGWPTightGsfTrackIsoFilter","hltEGL1SingleEGOrFilter")
  options['TnPHLTProbeFilters'] = cms.vstring()
  options['HLTFILTERSTOMEASURE']= {"passHltEle32DoubleEGWPTightGsf" :                   cms.vstring("hltEle32L1DoubleEGWPTightGsfTrackIsoFilter"),
                                   "passEGL1SingleEGOr" :                               cms.vstring("hltEGL1SingleEGOrFilter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match" : cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2" :        cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter"),
                                   "passHltDoubleEle33CaloIdLMWSeedLegL1match" :        cms.vstring("hltEle33CaloIdLMWPMS2Filter"),
                                   "passHltDoubleEle33CaloIdLMWUnsLeg" :                cms.vstring("hltDiEle33CaloIdLMWPMS2UnseededFilter"),
                                  }

elif '2018'  in options['era']:
  options['TnPPATHS']           = cms.vstring("HLT_Ele32_WPTight_Gsf_v*")
  options['TnPHLTTagFilters']   = cms.vstring("hltEle32WPTightGsfTrackIsoFilter")
  options['TnPHLTProbeFilters'] = cms.vstring()
  options['HLTFILTERSTOMEASURE']= {"passHltEle32WPTightGsf" :                           cms.vstring("hltEle32WPTightGsfTrackIsoFilter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match" : cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter"),
                                   "passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2" :        cms.vstring("hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter"),
                                   "passHltDoubleEle33CaloIdLMWSeedLegL1match" :        cms.vstring("hltEle33CaloIdLMWPMS2Filter"),
                                   "passHltDoubleEle33CaloIdLMWUnsLeg" :                cms.vstring("hltDiEle33CaloIdLMWPMS2UnseededFilter"),
                                  }

else:#Run-3
  options['TnPPATHS']           = cms.vstring("HLT_Ele30_WPTight_Gsf_v*")
  options['TnPHLTTagFilters']   = cms.vstring("hltEle30WPTightGsfTrackIsoFilter")
  options['TnPHLTProbeFilters'] = cms.vstring()
  options['HLTFILTERSTOMEASURE']= {}
  options['HLTFILTERSTOMEASURE'].update(ele30_allFilters)
  options['HLTFILTERSTOMEASURE'].update(ele32_allFilters)
  options['HLTFILTERSTOMEASURE'].update(ele115_allFilters)
  options['HLTFILTERSTOMEASURE'].update(ele135_allFilters)
  options['HLTFILTERSTOMEASURE'].update(ele23ele12_allFilters)
  options['HLTFILTERSTOMEASURE'].update(doubleEle33_leg1_allFilters)
  options['HLTFILTERSTOMEASURE'].update(doubleEle33_leg2_allFilters)

# Apply L1 matching (using L1Threshold) when flag contains "L1match" in name
options['ApplyL1Matching']      = any(['L1match' in flag for flag in options['HLTFILTERSTOMEASURE'].keys()])
options['L1Threshold']          = varOptions.L1Threshold


###################################################################
## Define input files for test local run
###################################################################
importTestFiles = 'from EgammaAnalysis.TnPTreeProducer.etc.tnpInputTestFiles_cff import files%s_%s as inputs' % ('AOD' if options['useAOD'] else 'MiniAOD', options['era'])
exec(importTestFiles)

options['INPUT_FILE_NAME'] = inputs['mc' if options['isMC'] else 'data']

###################################################################
## Standard imports, GT and pile-up
###################################################################
process = cms.Process("tnpEGM")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff') #old
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff') #new
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, options['GLOBALTAG'] , '')

import EgammaAnalysis.TnPTreeProducer.pileupConfiguration_cff as pileUpSetup
pileUpSetup.setPileUpConfiguration(process, options)


###################################################################
## Import tnpVars to store in tree and configure for AOD
###################################################################
import EgammaAnalysis.TnPTreeProducer.egmTreesContent_cff as tnpVars
if options['useAOD']: tnpVars.setupTnPVariablesForAOD()
mcTruthCommonStuff = tnpVars.getTnPVariablesForMCTruth(options['isMC'])

###################################################################
## Import Tnp setup
###################################################################
import EgammaAnalysis.TnPTreeProducer.egmTreesSetup_cff as tnpSetup
tnpSetup.setupTreeMaker(process,options)

###################################################################
# If miniAOD, adding some leptonMva versions, as well
# as some advanced input variables like miniIso
###################################################################
if not options['useAOD']:
  from EgammaAnalysis.TnPTreeProducer.leptonMva_cff import leptonMvaSequence
  process.init_sequence += leptonMvaSequence(process, options, tnpVars)

###################################################################
## Init and Load
###################################################################
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource", fileNames = options['INPUT_FILE_NAME'])
process.maxEvents = cms.untracked.PSet( input = options['MAXEVENTS'])


###################################################################
## Define sequences and TnP pairs
###################################################################
process.cand_sequence = cms.Sequence( process.init_sequence + process.tag_sequence )
if options['DoEleID'] or options['DoTrigger'] : process.cand_sequence += process.ele_sequence
if options['DoPhoID']                         : process.cand_sequence += process.pho_sequence
if options['DoTrigger']                       : process.cand_sequence += process.hlt_sequence
if options['DoRECO']                          : process.cand_sequence += process.sc_sequence

process.tnpPairs_sequence = cms.Sequence()
if options['DoTrigger'] : process.tnpPairs_sequence *= process.tnpPairingEleHLT
if options['DoRECO']    : process.tnpPairs_sequence *= process.tnpPairingEleRec
if options['DoEleID']   : process.tnpPairs_sequence *= process.tnpPairingEleIDs
if options['DoPhoID']   : process.tnpPairs_sequence *= process.tnpPairingPhoIDs

##########################################################################
## TnP Trees
##########################################################################
process.tnpEleTrig = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                    mcTruthCommonStuff,
                                    tnpVars.CommonStuffForGsfElectronProbe,
                                    tagProbePairs = cms.InputTag("tnpPairingEleHLT"),
                                    probeMatches  = cms.InputTag("genProbeEle"),
                                    allProbes     = cms.InputTag("probeEle"),
                                    flags         = cms.PSet(),
                                    )

for flag in options['HLTFILTERSTOMEASURE']:
  setattr(process.tnpEleTrig.flags, flag, cms.InputTag(flag))


process.tnpEleReco = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                    mcTruthCommonStuff,
                                    tnpVars.CommonStuffForSuperClusterProbe,
                                    tagProbePairs = cms.InputTag("tnpPairingEleRec"),
                                    probeMatches  = cms.InputTag("genProbeSC"),
                                    allProbes     = cms.InputTag("probeSC"),
                                    flags         = cms.PSet(
        passingRECO   = cms.InputTag("probeSCEle", "superclusters"),
        passingRECOEcalDriven   = cms.InputTag("probeSCEle", "superclustersEcalDriven"),
        passingRECOTrackDriven   = cms.InputTag("probeSCEle", "superclustersTrackDriven")
        ),

                                    )

process.tnpEleIDs = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                    mcTruthCommonStuff,
                                    tnpVars.CommonStuffForGsfElectronProbe,
                                    tagProbePairs = cms.InputTag("tnpPairingEleIDs"),
                                    probeMatches  = cms.InputTag("genProbeEle"),
                                    allProbes     = cms.InputTag("probeEle"),
                                    flags         = cms.PSet(),
                                    )

# ID's to store in the electron ID and trigger tree
# Simply look which probeEleX modules were made in egmElectronIDModules_cff.py and convert them into a passingX boolean in the tree 
for probeEleModule in str(process.ele_sequence).split('+'):
  if not 'probeEle' in probeEleModule or probeEleModule in ['probeEle', 'probeEleL1matched']: continue
  setattr(process.tnpEleTrig.flags, probeEleModule.replace('probeEle', 'passing'), cms.InputTag(probeEleModule))
  setattr(process.tnpEleIDs.flags,  probeEleModule.replace('probeEle', 'passing'), cms.InputTag(probeEleModule))



process.tnpPhoIDs = cms.EDAnalyzer("TagProbeFitTreeProducer",
                                    mcTruthCommonStuff,
                                    tnpVars.CommonStuffForPhotonProbe,
                                    tagProbePairs = cms.InputTag("tnpPairingPhoIDs"),
                                    probeMatches  = cms.InputTag("genProbePho"),
                                    allProbes     = cms.InputTag("probePho"),
                                    flags         = cms.PSet(),
                                    )

# ID's to store in the photon ID tree
# Simply look which probePhoX modules were made in egmPhotonIDModules_cff.py and convert them into a passingX boolean in the tree 
for probePhoModule in str(process.pho_sequence).split('+'):
  if not 'probePho' in probePhoModule or probePhoModule=='probePho': continue
  setattr(process.tnpPhoIDs.flags, probePhoModule.replace('probePho', 'passing'), cms.InputTag(probePhoModule))


# Add SUSY variables to the "variables", add SUSY IDs to the "flags" [kind of deprecated, better ways to add these]
if options['addSUSY'] :
    setattr( process.tnpEleIDs.variables , 'el_miniIsoChg', cms.string("userFloat('miniIsoChg')") )
    setattr( process.tnpEleIDs.variables , 'el_miniIsoAll', cms.string("userFloat('miniIsoAll')") )
    setattr( process.tnpEleIDs.variables , 'el_ptRatio', cms.string("userFloat('ptRatio')") )
    setattr( process.tnpEleIDs.variables , 'el_ptRatioUncorr', cms.string("userFloat('ptRatioUncorr')") )
    setattr( process.tnpEleIDs.variables , 'el_ptRel', cms.string("userFloat('ptRel')") )
    setattr( process.tnpEleIDs.variables , 'el_MVATTH', cms.InputTag("susyEleVarHelper:electronMVATTH") )
    setattr( process.tnpEleIDs.variables , 'el_sip3d', cms.InputTag("susyEleVarHelper:sip3d") )


tnpSetup.customize( process.tnpEleTrig , options )
tnpSetup.customize( process.tnpEleIDs  , options )
tnpSetup.customize( process.tnpPhoIDs  , options )
tnpSetup.customize( process.tnpEleReco , options )


process.tree_sequence = cms.Sequence()
if (options['DoTrigger']): process.tree_sequence *= process.tnpEleTrig
if (options['DoRECO'])   : process.tree_sequence *= process.tnpEleReco
if (options['DoEleID'])  : process.tree_sequence *= process.tnpEleIDs
if (options['DoPhoID'])  : process.tree_sequence *= process.tnpPhoIDs

##########################################################################
## PATHS
##########################################################################
if options['DEBUG']:
  process.out = cms.OutputModule("PoolOutputModule",
                                 fileName = cms.untracked.string('edmFile_for_debug.root'),
                                 SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
                                 )
  process.outpath = cms.EndPath(process.out)

process.evtCounter = cms.EDAnalyzer('SimpleEventCounter')

process.p = cms.Path(
        process.evtCounter        +
        process.hltFilter         +
        process.cand_sequence     +
        process.tnpPairs_sequence +
        process.mc_sequence       +
        process.tree_sequence
        )

process.TFileService = cms.Service(
    "TFileService", fileName = cms.string(options['OUTPUT_FILE_NAME']),
    closeFileFast = cms.untracked.bool(True)
    )
