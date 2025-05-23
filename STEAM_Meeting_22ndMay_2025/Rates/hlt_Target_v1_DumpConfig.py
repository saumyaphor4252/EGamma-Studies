import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.AlpakaCore.ProcessAcceleratorAlpaka import ProcessAcceleratorAlpaka
from HeterogeneousCore.CUDACore.ProcessAcceleratorCUDA import ProcessAcceleratorCUDA
from HeterogeneousCore.ROCmCore.ProcessAcceleratorROCm import ProcessAcceleratorROCm

process = cms.Process("MYHLT")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:RelVal_Raw_GRun_DATA.root'),
    inputCommands = cms.untracked.vstring('keep *')
)
process.HLTCkfBaseTrajectoryFilterP5 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(4),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTConfigVersion = cms.PSet(
    tableName = cms.string('/dev/CMSSW_15_0_0/GRun/V79')
)

process.HLTGroupedCkfTrajectoryBuilderP5 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESChi2MeasurementEstimatorForP5'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTCkfBaseTrajectoryFilterP5')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0HighPtTkMuPSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter1PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(5.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter2PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTIter4PSetTrajectoryFilterIT')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.3),
    minimumNumberOfHits = cms.int32(6),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetCkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.5),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetHighPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryBuilderPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(3.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetInitialStepTrajectoryFilterPreSplittingForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterBasePreSplittingForFullTrackingPPOnAA')
        ),
        cms.PSet(
            refToPSet_ = cms.string('HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA')
        )
    )
)

process.HLTPSetInitialStepTrajectoryFilterShapePreSplittingPPOnAA = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.HLTPSetJetCoreStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetJetCoreStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForDmesonPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtQuadStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(1.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetLowPtTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetLowPtTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.8),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMixedTripletStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterialForMixedStep'),
    propagatorOpposite = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetMixedTripletStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuTrackJpsiTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(8),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(10.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('MuonCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    deltaEta = cms.double(-1.0),
    deltaPhi = cms.double(-1.0),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    propagatorProximity = cms.string('SteppingHelixPropagatorAny'),
    rescaleErrorIfFail = cms.double(1.0),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetMuonCkfTrajectoryFilter')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSeedLayer = cms.bool(False)
)

process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet(
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    DeltaR = cms.double(0.2),
    DeltaZ = cms.double(15.9),
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    Eta_fixed = cms.bool(False),
    Eta_min = cms.double(0.1),
    MeasurementTrackerName = cms.InputTag("hltESPMeasurementTracker"),
    OnDemand = cms.int32(-1),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.1),
    Pt_fixed = cms.bool(False),
    Pt_min = cms.double(1.5),
    Rescale_Dz = cms.double(3.0),
    Rescale_eta = cms.double(3.0),
    Rescale_phi = cms.double(3.0),
    UseVertex = cms.bool(False),
    Z_fixed = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    input = cms.InputTag("hltL2Muons","UpdatedAtVtx"),
    maxRegions = cms.int32(2),
    precise = cms.bool(True),
    vertexCollection = cms.InputTag("pixelVertices")
)

process.HLTPSetPixelLessStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetCkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HLTPSetPixelLessStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetPvClusterComparerForBTag = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(0.1)
)

process.HLTPSetPvClusterComparerForIT = cms.PSet(
    track_chi2_max = cms.double(20.0),
    track_prob_min = cms.double(-1.0),
    track_pt_max = cms.double(20.0),
    track_pt_min = cms.double(1.0)
)

process.HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryBuilderForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepInOutTrajectoryFilterForFullTrackingPPOnAA')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.0),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA')
    ),
    updator = cms.string('hltESPKFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.HLTPSetTobTecStepTrajectoryFilterForFullTrackingPPOnAA = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(5.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    intermediateCleaning = cms.bool(False),
    lostHitPenalty = cms.double(90.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('hltESPFwdElectronPropagator'),
    propagatorOpposite = cms.string('hltESPBwdElectronPropagator'),
    seedAs5DHit = cms.bool(False),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryFilterForElectrons')
    ),
    updator = cms.string('hltESPKFUpdator')
)

process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    highEtaSwitch = cms.double(5.0),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(999.0),
    maxNumberOfHits = cms.int32(-1),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    minHitsAtHighEta = cms.int32(5),
    minHitsMinPt = cms.int32(-1),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(2.0),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    propagator = cms.string('PropagatorWithMaterial')
)

process.HLTSeedFromProtoTracks = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.HLTSiStripClusterChargeCutForHI = cms.PSet(
    value = cms.double(2069.0)
)

process.HLTSiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.HLTSiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.HLTSiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.datasets = cms.PSet(
    AlCaHcalIsoTrk = cms.vstring('AlCa_IsoTrackHBHE_v1'),
    AlCaLowPtJet = cms.vstring(
        'AlCa_AK8PFJet40_v29',
        'AlCa_PFJet40_v34'
    ),
    AlCaLumiPixelsCountsExpress = cms.vstring('AlCa_LumiPixelsCounts_Random_v12'),
    AlCaLumiPixelsCountsPrompt = cms.vstring(
        'AlCa_LumiPixelsCounts_Random_v12',
        'AlCa_LumiPixelsCounts_ZeroBias_v14'
    ),
    AlCaP0 = cms.vstring(
        'AlCa_EcalEtaEBonly_v26',
        'AlCa_EcalEtaEEonly_v26',
        'AlCa_EcalPi0EBonly_v26',
        'AlCa_EcalPi0EEonly_v26'
    ),
    AlCaPPSExpress = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v10',
        'HLT_PPSMaxTracksPerRP4_v10'
    ),
    AlCaPPSPrompt = cms.vstring(
        'HLT_PPSMaxTracksPerArm1_v10',
        'HLT_PPSMaxTracksPerRP4_v10'
    ),
    AlCaPhiSym = cms.vstring('AlCa_EcalPhiSym_v21'),
    BTagMu = cms.vstring(
        'HLT_BTagMu_AK4DiJet110_Mu5_v27',
        'HLT_BTagMu_AK4DiJet170_Mu5_v26',
        'HLT_BTagMu_AK4DiJet20_Mu5_v27',
        'HLT_BTagMu_AK4DiJet40_Mu5_v27',
        'HLT_BTagMu_AK4DiJet70_Mu5_v27',
        'HLT_BTagMu_AK4Jet300_Mu5_v26',
        'HLT_BTagMu_AK8DiJet170_Mu5_v23',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v16',
        'HLT_BTagMu_AK8Jet300_Mu5_v26'
    ),
    Commissioning = cms.vstring(
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v10',
        'HLT_PFJet40_GPUvsCPU_v8'
    ),
    Cosmics = cms.vstring('HLT_L1SingleMuCosmics_v9'),
    DQMGPUvsCPU = cms.vstring(
        'DQM_EcalReconstruction_v13',
        'DQM_HcalReconstruction_v11',
        'DQM_PixelReconstruction_v13'
    ),
    DQMOnlineBeamspot = cms.vstring(
        'HLT_HT300_Beamspot_v25',
        'HLT_ZeroBias_Beamspot_v18'
    ),
    DQMPPSRandom = cms.vstring('HLT_PPSRandom_v1'),
    EGamma0 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v15',
        'HLT_DiPhoton10Time1ns_v11',
        'HLT_DiPhoton10Time1p2ns_v11',
        'HLT_DiPhoton10Time1p4ns_v11',
        'HLT_DiPhoton10Time1p6ns_v11',
        'HLT_DiPhoton10Time1p8ns_v11',
        'HLT_DiPhoton10Time2ns_v11',
        'HLT_DiPhoton10_CaloIdL_v11',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v25',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v13',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v25',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v25',
        'HLT_DiphotonMVA14p25_High_Mass60_v1',
        'HLT_DiphotonMVA14p25_Low_Mass60_v1',
        'HLT_DiphotonMVA14p25_Medium_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightHigh_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightLow_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightMedium_Mass60_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v12',
        'HLT_DoubleEle25_CaloIdL_MW_v17',
        'HLT_DoubleEle27_CaloIdL_MW_v17',
        'HLT_DoubleEle33_CaloIdL_MW_v30',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v12',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v34',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v34',
        'HLT_DoubleEle8_eta1p22_mMax6_v12',
        'HLT_DoublePhoton33_CaloIdL_v18',
        'HLT_DoublePhoton70_v18',
        'HLT_DoublePhoton85_v26',
        'HLT_ECALHT800_v22',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v27',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v20',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v7',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v30',
        'HLT_Ele15_IsoVVVL_PFHT450_v30',
        'HLT_Ele15_IsoVVVL_PFHT600_v34',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v30',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v8',
        'HLT_Ele28_HighEta_SC20_Mass55_v25',
        'HLT_Ele30_WPTight_Gsf_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v21',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele35_WPTight_Gsf_v21',
        'HLT_Ele38_WPTight_Gsf_v21',
        'HLT_Ele40_WPTight_Gsf_v21',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v32',
        'HLT_Ele50_IsoVVVL_PFHT450_v30',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v30',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Photon100EBHE10_v13',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon110EB_TightID_TightIso_v14',
        'HLT_Photon120_R9Id90_HE10_IsoM_v26',
        'HLT_Photon120_v24',
        'HLT_Photon150_v18',
        'HLT_Photon165_R9Id90_HE10_IsoM_v27',
        'HLT_Photon175_v26',
        'HLT_Photon200_v25',
        'HLT_Photon20_HoverELoose_v21',
        'HLT_Photon300_NoHE_v24',
        'HLT_Photon30EB_TightID_TightIso_v14',
        'HLT_Photon30_HoverELoose_v21',
        'HLT_Photon32_OneProng32_M50To105_v12',
        'HLT_Photon33_v16',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v10',
        'HLT_Photon35_TwoProngs35_v15',
        'HLT_Photon40EB_TightID_TightIso_v5',
        'HLT_Photon40EB_v4',
        'HLT_Photon45EB_TightID_TightIso_v5',
        'HLT_Photon45EB_v4',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon50EB_TightID_TightIso_v10',
        'HLT_Photon50EB_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v26',
        'HLT_Photon50_TimeGt2p5ns_v8',
        'HLT_Photon50_TimeLtNeg2p5ns_v8',
        'HLT_Photon50_v24',
        'HLT_Photon55EB_TightID_TightIso_v6',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v12',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v11',
        'HLT_Photon75EB_TightID_TightIso_v10',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v19',
        'HLT_Photon75_R9Id90_HE10_IsoM_v26',
        'HLT_Photon75_v24',
        'HLT_Photon90EB_TightID_TightIso_v10',
        'HLT_Photon90_R9Id90_HE10_IsoM_v26',
        'HLT_Photon90_v24',
        'HLT_SingleEle8_SingleEGL1_v11',
        'HLT_SingleEle8_v11'
    ),
    EGamma1 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v15',
        'HLT_DiPhoton10Time1ns_v11',
        'HLT_DiPhoton10Time1p2ns_v11',
        'HLT_DiPhoton10Time1p4ns_v11',
        'HLT_DiPhoton10Time1p6ns_v11',
        'HLT_DiPhoton10Time1p8ns_v11',
        'HLT_DiPhoton10Time2ns_v11',
        'HLT_DiPhoton10_CaloIdL_v11',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v25',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v13',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v25',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v25',
        'HLT_DiphotonMVA14p25_High_Mass60_v1',
        'HLT_DiphotonMVA14p25_Low_Mass60_v1',
        'HLT_DiphotonMVA14p25_Medium_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightHigh_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightLow_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightMedium_Mass60_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v12',
        'HLT_DoubleEle25_CaloIdL_MW_v17',
        'HLT_DoubleEle27_CaloIdL_MW_v17',
        'HLT_DoubleEle33_CaloIdL_MW_v30',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v12',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v34',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v34',
        'HLT_DoubleEle8_eta1p22_mMax6_v12',
        'HLT_DoublePhoton33_CaloIdL_v18',
        'HLT_DoublePhoton70_v18',
        'HLT_DoublePhoton85_v26',
        'HLT_ECALHT800_v22',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v27',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v20',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v7',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v30',
        'HLT_Ele15_IsoVVVL_PFHT450_v30',
        'HLT_Ele15_IsoVVVL_PFHT600_v34',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v30',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v8',
        'HLT_Ele28_HighEta_SC20_Mass55_v25',
        'HLT_Ele30_WPTight_Gsf_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v21',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele35_WPTight_Gsf_v21',
        'HLT_Ele38_WPTight_Gsf_v21',
        'HLT_Ele40_WPTight_Gsf_v21',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v32',
        'HLT_Ele50_IsoVVVL_PFHT450_v30',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v30',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Photon100EBHE10_v13',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon110EB_TightID_TightIso_v14',
        'HLT_Photon120_R9Id90_HE10_IsoM_v26',
        'HLT_Photon120_v24',
        'HLT_Photon150_v18',
        'HLT_Photon165_R9Id90_HE10_IsoM_v27',
        'HLT_Photon175_v26',
        'HLT_Photon200_v25',
        'HLT_Photon20_HoverELoose_v21',
        'HLT_Photon300_NoHE_v24',
        'HLT_Photon30EB_TightID_TightIso_v14',
        'HLT_Photon30_HoverELoose_v21',
        'HLT_Photon32_OneProng32_M50To105_v12',
        'HLT_Photon33_v16',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v10',
        'HLT_Photon35_TwoProngs35_v15',
        'HLT_Photon40EB_TightID_TightIso_v5',
        'HLT_Photon40EB_v4',
        'HLT_Photon45EB_TightID_TightIso_v5',
        'HLT_Photon45EB_v4',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon50EB_TightID_TightIso_v10',
        'HLT_Photon50EB_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v26',
        'HLT_Photon50_TimeGt2p5ns_v8',
        'HLT_Photon50_TimeLtNeg2p5ns_v8',
        'HLT_Photon50_v24',
        'HLT_Photon55EB_TightID_TightIso_v6',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v12',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v11',
        'HLT_Photon75EB_TightID_TightIso_v10',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v19',
        'HLT_Photon75_R9Id90_HE10_IsoM_v26',
        'HLT_Photon75_v24',
        'HLT_Photon90EB_TightID_TightIso_v10',
        'HLT_Photon90_R9Id90_HE10_IsoM_v26',
        'HLT_Photon90_v24',
        'HLT_SingleEle8_SingleEGL1_v11',
        'HLT_SingleEle8_v11'
    ),
    EGamma2 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v15',
        'HLT_DiPhoton10Time1ns_v11',
        'HLT_DiPhoton10Time1p2ns_v11',
        'HLT_DiPhoton10Time1p4ns_v11',
        'HLT_DiPhoton10Time1p6ns_v11',
        'HLT_DiPhoton10Time1p8ns_v11',
        'HLT_DiPhoton10Time2ns_v11',
        'HLT_DiPhoton10_CaloIdL_v11',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v25',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v13',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v25',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v25',
        'HLT_DiphotonMVA14p25_High_Mass60_v1',
        'HLT_DiphotonMVA14p25_Low_Mass60_v1',
        'HLT_DiphotonMVA14p25_Medium_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightHigh_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightLow_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightMedium_Mass60_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v12',
        'HLT_DoubleEle25_CaloIdL_MW_v17',
        'HLT_DoubleEle27_CaloIdL_MW_v17',
        'HLT_DoubleEle33_CaloIdL_MW_v30',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v12',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v34',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v34',
        'HLT_DoubleEle8_eta1p22_mMax6_v12',
        'HLT_DoublePhoton33_CaloIdL_v18',
        'HLT_DoublePhoton70_v18',
        'HLT_DoublePhoton85_v26',
        'HLT_ECALHT800_v22',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v27',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v20',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v7',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v30',
        'HLT_Ele15_IsoVVVL_PFHT450_v30',
        'HLT_Ele15_IsoVVVL_PFHT600_v34',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v30',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v8',
        'HLT_Ele28_HighEta_SC20_Mass55_v25',
        'HLT_Ele30_WPTight_Gsf_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v21',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele35_WPTight_Gsf_v21',
        'HLT_Ele38_WPTight_Gsf_v21',
        'HLT_Ele40_WPTight_Gsf_v21',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v32',
        'HLT_Ele50_IsoVVVL_PFHT450_v30',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v30',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Photon100EBHE10_v13',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon110EB_TightID_TightIso_v14',
        'HLT_Photon120_R9Id90_HE10_IsoM_v26',
        'HLT_Photon120_v24',
        'HLT_Photon150_v18',
        'HLT_Photon165_R9Id90_HE10_IsoM_v27',
        'HLT_Photon175_v26',
        'HLT_Photon200_v25',
        'HLT_Photon20_HoverELoose_v21',
        'HLT_Photon300_NoHE_v24',
        'HLT_Photon30EB_TightID_TightIso_v14',
        'HLT_Photon30_HoverELoose_v21',
        'HLT_Photon32_OneProng32_M50To105_v12',
        'HLT_Photon33_v16',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v10',
        'HLT_Photon35_TwoProngs35_v15',
        'HLT_Photon40EB_TightID_TightIso_v5',
        'HLT_Photon40EB_v4',
        'HLT_Photon45EB_TightID_TightIso_v5',
        'HLT_Photon45EB_v4',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon50EB_TightID_TightIso_v10',
        'HLT_Photon50EB_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v26',
        'HLT_Photon50_TimeGt2p5ns_v8',
        'HLT_Photon50_TimeLtNeg2p5ns_v8',
        'HLT_Photon50_v24',
        'HLT_Photon55EB_TightID_TightIso_v6',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v12',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v11',
        'HLT_Photon75EB_TightID_TightIso_v10',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v19',
        'HLT_Photon75_R9Id90_HE10_IsoM_v26',
        'HLT_Photon75_v24',
        'HLT_Photon90EB_TightID_TightIso_v10',
        'HLT_Photon90_R9Id90_HE10_IsoM_v26',
        'HLT_Photon90_v24',
        'HLT_SingleEle8_SingleEGL1_v11',
        'HLT_SingleEle8_v11'
    ),
    EGamma3 = cms.vstring(
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v15',
        'HLT_DiPhoton10Time1ns_v11',
        'HLT_DiPhoton10Time1p2ns_v11',
        'HLT_DiPhoton10Time1p4ns_v11',
        'HLT_DiPhoton10Time1p6ns_v11',
        'HLT_DiPhoton10Time1p8ns_v11',
        'HLT_DiPhoton10Time2ns_v11',
        'HLT_DiPhoton10_CaloIdL_v11',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v25',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v13',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v25',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v25',
        'HLT_DiphotonMVA14p25_High_Mass60_v1',
        'HLT_DiphotonMVA14p25_Low_Mass60_v1',
        'HLT_DiphotonMVA14p25_Medium_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightHigh_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightLow_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightMedium_Mass60_v1',
        'HLT_DoubleEle10_eta1p22_mMax6_v12',
        'HLT_DoubleEle25_CaloIdL_MW_v17',
        'HLT_DoubleEle27_CaloIdL_MW_v17',
        'HLT_DoubleEle33_CaloIdL_MW_v30',
        'HLT_DoubleEle6p5_eta1p22_mMax6_v12',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v34',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v34',
        'HLT_DoubleEle8_eta1p22_mMax6_v12',
        'HLT_DoublePhoton33_CaloIdL_v18',
        'HLT_DoublePhoton70_v18',
        'HLT_DoublePhoton85_v26',
        'HLT_ECALHT800_v22',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v27',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v20',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v7',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v30',
        'HLT_Ele15_IsoVVVL_PFHT450_v30',
        'HLT_Ele15_IsoVVVL_PFHT600_v34',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v30',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Loose_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Medium_eta2p3_CrossL1_v8',
        'HLT_Ele24_eta2p1_WPTight_Gsf_PNetTauhPFJet30_Tight_eta2p3_CrossL1_v8',
        'HLT_Ele28_HighEta_SC20_Mass55_v25',
        'HLT_Ele30_WPTight_Gsf_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v21',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele35_WPTight_Gsf_v21',
        'HLT_Ele38_WPTight_Gsf_v21',
        'HLT_Ele40_WPTight_Gsf_v21',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v32',
        'HLT_Ele50_IsoVVVL_PFHT450_v30',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v30',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Photon100EBHE10_v13',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon110EB_TightID_TightIso_v14',
        'HLT_Photon120_R9Id90_HE10_IsoM_v26',
        'HLT_Photon120_v24',
        'HLT_Photon150_v18',
        'HLT_Photon165_R9Id90_HE10_IsoM_v27',
        'HLT_Photon175_v26',
        'HLT_Photon200_v25',
        'HLT_Photon20_HoverELoose_v21',
        'HLT_Photon300_NoHE_v24',
        'HLT_Photon30EB_TightID_TightIso_v14',
        'HLT_Photon30_HoverELoose_v21',
        'HLT_Photon32_OneProng32_M50To105_v12',
        'HLT_Photon33_v16',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v10',
        'HLT_Photon35_TwoProngs35_v15',
        'HLT_Photon40EB_TightID_TightIso_v5',
        'HLT_Photon40EB_v4',
        'HLT_Photon45EB_TightID_TightIso_v5',
        'HLT_Photon45EB_v4',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon50EB_TightID_TightIso_v10',
        'HLT_Photon50EB_v5',
        'HLT_Photon50_R9Id90_HE10_IsoM_v26',
        'HLT_Photon50_TimeGt2p5ns_v8',
        'HLT_Photon50_TimeLtNeg2p5ns_v8',
        'HLT_Photon50_v24',
        'HLT_Photon55EB_TightID_TightIso_v6',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v12',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v11',
        'HLT_Photon75EB_TightID_TightIso_v10',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v19',
        'HLT_Photon75_R9Id90_HE10_IsoM_v26',
        'HLT_Photon75_v24',
        'HLT_Photon90EB_TightID_TightIso_v10',
        'HLT_Photon90_R9Id90_HE10_IsoM_v26',
        'HLT_Photon90_v24',
        'HLT_SingleEle8_SingleEGL1_v11',
        'HLT_SingleEle8_v11'
    ),
    EcalLaser = cms.vstring('HLT_EcalCalibration_v4'),
    EmittanceScan0 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EmittanceScan1 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EmittanceScan2 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EmittanceScan3 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EmittanceScan4 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EmittanceScan5 = cms.vstring('HLT_L1AlwaysTrue_v1'),
    EphemeralHLTPhysics0 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics1 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics2 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics3 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics4 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics5 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics6 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralHLTPhysics7 = cms.vstring('HLT_EphemeralPhysics_v10'),
    EphemeralZeroBias0 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias1 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias2 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias3 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias4 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias5 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias6 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EphemeralZeroBias7 = cms.vstring('HLT_EphemeralZeroBias_v10'),
    EventDisplay = cms.vstring(
        'HLT_DoublePhoton85_v26',
        'HLT_PFJet500_v35',
        'HLT_Physics_v15'
    ),
    ExpressAlignment = cms.vstring(
        'HLT_HT300_Beamspot_v25',
        'HLT_ZeroBias_Beamspot_v18'
    ),
    ExpressPhysics = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_IsoMu20_v29',
        'HLT_IsoMu24_v27',
        'HLT_IsoMu27_v30',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v29',
        'HLT_Physics_v15',
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v9',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v13',
        'HLT_ZeroBias_IsolatedBunches_v13',
        'HLT_ZeroBias_v14'
    ),
    HLTMonitor = cms.vstring(
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT550_DisplacedDijet60_Inclusive_v25',
        'HLT_IsoMu24_HLTTracking_v2',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_HLTTracking_v2',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_HLTTracking_v2',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v29',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v15',
        'HLT_PFHT510_v31',
        'HLT_PFJet260_v34',
        'HLT_PFJet320_v34',
        'HLT_PFMET130_PFMHT130_IDTight_v34',
        'HLT_PFMET140_PFMHT140_IDTight_v34'
    ),
    HLTPhysics = cms.vstring('HLT_Physics_v15'),
    HcalNZS = cms.vstring(
        'HLT_HcalNZS_v22',
        'HLT_HcalPhiSym_v24'
    ),
    JetMET0 = cms.vstring(
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v8',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v8',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v8',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v14',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v8',
        'HLT_AK8PFJet140_v29',
        'HLT_AK8PFJet200_v29',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v11',
        'HLT_AK8PFJet220_SoftDropMass40_v15',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet230_SoftDropMass40_v15',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet260_v30',
        'HLT_AK8PFJet275_Nch40_v8',
        'HLT_AK8PFJet275_Nch45_v8',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet320_v30',
        'HLT_AK8PFJet380_SoftDropMass30_v8',
        'HLT_AK8PFJet400_SoftDropMass30_v8',
        'HLT_AK8PFJet400_v30',
        'HLT_AK8PFJet40_v30',
        'HLT_AK8PFJet425_SoftDropMass30_v8',
        'HLT_AK8PFJet450_SoftDropMass30_v8',
        'HLT_AK8PFJet450_v30',
        'HLT_AK8PFJet500_v30',
        'HLT_AK8PFJet550_v25',
        'HLT_AK8PFJet60_v29',
        'HLT_AK8PFJet80_v30',
        'HLT_AK8PFJetFwd140_v28',
        'HLT_AK8PFJetFwd200_v28',
        'HLT_AK8PFJetFwd260_v29',
        'HLT_AK8PFJetFwd320_v29',
        'HLT_AK8PFJetFwd400_v29',
        'HLT_AK8PFJetFwd40_v29',
        'HLT_AK8PFJetFwd450_v29',
        'HLT_AK8PFJetFwd500_v29',
        'HLT_AK8PFJetFwd60_v28',
        'HLT_AK8PFJetFwd80_v28',
        'HLT_CaloJet500_NoJetID_v24',
        'HLT_CaloJet550_NoJetID_v19',
        'HLT_CaloMET350_NotCleaned_v16',
        'HLT_CaloMET90_NotCleaned_v16',
        'HLT_CaloMHT90_v16',
        'HLT_DiPFJetAve100_HFJEC_v31',
        'HLT_DiPFJetAve140_v27',
        'HLT_DiPFJetAve160_HFJEC_v30',
        'HLT_DiPFJetAve180_PPSMatch_Xi0p3_QuadJet_Max2ProtPerRP_v8',
        'HLT_DiPFJetAve200_v27',
        'HLT_DiPFJetAve220_HFJEC_v30',
        'HLT_DiPFJetAve260_HFJEC_v13',
        'HLT_DiPFJetAve260_v28',
        'HLT_DiPFJetAve300_HFJEC_v30',
        'HLT_DiPFJetAve320_v28',
        'HLT_DiPFJetAve400_v28',
        'HLT_DiPFJetAve40_v28',
        'HLT_DiPFJetAve500_v28',
        'HLT_DiPFJetAve60_HFJEC_v29',
        'HLT_DiPFJetAve60_v28',
        'HLT_DiPFJetAve80_HFJEC_v31',
        'HLT_DiPFJetAve80_v28',
        'HLT_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_HT350_v9',
        'HLT_HT425_v21',
        'HLT_L1ETMHadSeeds_v11',
        'HLT_L1Mu6HT240_v10',
        'HLT_MET105_IsoTrk50_v21',
        'HLT_MET120_IsoTrk50_v21',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12eta2p3_PFJet40_v15',
        'HLT_Mu12eta2p3_v15',
        'HLT_PFHT1050_v32',
        'HLT_PFHT180_v31',
        'HLT_PFHT250_v31',
        'HLT_PFHT350_v33',
        'HLT_PFHT370_v31',
        'HLT_PFHT430_v31',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v26',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v26',
        'HLT_PFHT510_v31',
        'HLT_PFHT590_v31',
        'HLT_PFHT680_v31',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v26',
        'HLT_PFHT780_v31',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v26',
        'HLT_PFHT890_v31',
        'HLT_PFJet110_v14',
        'HLT_PFJet140_v33',
        'HLT_PFJet200_v33',
        'HLT_PFJet260_v34',
        'HLT_PFJet320_v34',
        'HLT_PFJet400_v34',
        'HLT_PFJet40_v35',
        'HLT_PFJet450_v35',
        'HLT_PFJet500_v35',
        'HLT_PFJet550_v25',
        'HLT_PFJet60_v35',
        'HLT_PFJet80_v35',
        'HLT_PFJetFwd140_v32',
        'HLT_PFJetFwd200_v32',
        'HLT_PFJetFwd260_v33',
        'HLT_PFJetFwd320_v33',
        'HLT_PFJetFwd400_v33',
        'HLT_PFJetFwd40_v33',
        'HLT_PFJetFwd450_v33',
        'HLT_PFJetFwd500_v33',
        'HLT_PFJetFwd60_v33',
        'HLT_PFJetFwd80_v32',
        'HLT_PFMET105_IsoTrk50_v15',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v23',
        'HLT_PFMET120_PFMHT120_IDTight_v34',
        'HLT_PFMET130_PFMHT130_IDTight_v34',
        'HLT_PFMET140_PFMHT140_IDTight_v34',
        'HLT_PFMET200_BeamHaloCleaned_v23',
        'HLT_PFMET200_NotCleaned_v23',
        'HLT_PFMET250_NotCleaned_v23',
        'HLT_PFMET300_NotCleaned_v23',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v23',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v34',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v33',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v33',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v25',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v23'
    ),
    JetMET1 = cms.vstring(
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v8',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v8',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v8',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v14',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v8',
        'HLT_AK8PFJet140_v29',
        'HLT_AK8PFJet200_v29',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v11',
        'HLT_AK8PFJet220_SoftDropMass40_v15',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet230_SoftDropMass40_v15',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet260_v30',
        'HLT_AK8PFJet275_Nch40_v8',
        'HLT_AK8PFJet275_Nch45_v8',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet320_v30',
        'HLT_AK8PFJet380_SoftDropMass30_v8',
        'HLT_AK8PFJet400_SoftDropMass30_v8',
        'HLT_AK8PFJet400_v30',
        'HLT_AK8PFJet40_v30',
        'HLT_AK8PFJet425_SoftDropMass30_v8',
        'HLT_AK8PFJet450_SoftDropMass30_v8',
        'HLT_AK8PFJet450_v30',
        'HLT_AK8PFJet500_v30',
        'HLT_AK8PFJet550_v25',
        'HLT_AK8PFJet60_v29',
        'HLT_AK8PFJet80_v30',
        'HLT_AK8PFJetFwd140_v28',
        'HLT_AK8PFJetFwd200_v28',
        'HLT_AK8PFJetFwd260_v29',
        'HLT_AK8PFJetFwd320_v29',
        'HLT_AK8PFJetFwd400_v29',
        'HLT_AK8PFJetFwd40_v29',
        'HLT_AK8PFJetFwd450_v29',
        'HLT_AK8PFJetFwd500_v29',
        'HLT_AK8PFJetFwd60_v28',
        'HLT_AK8PFJetFwd80_v28',
        'HLT_CaloJet500_NoJetID_v24',
        'HLT_CaloJet550_NoJetID_v19',
        'HLT_CaloMET350_NotCleaned_v16',
        'HLT_CaloMET90_NotCleaned_v16',
        'HLT_CaloMHT90_v16',
        'HLT_DiPFJetAve100_HFJEC_v31',
        'HLT_DiPFJetAve140_v27',
        'HLT_DiPFJetAve160_HFJEC_v30',
        'HLT_DiPFJetAve180_PPSMatch_Xi0p3_QuadJet_Max2ProtPerRP_v8',
        'HLT_DiPFJetAve200_v27',
        'HLT_DiPFJetAve220_HFJEC_v30',
        'HLT_DiPFJetAve260_HFJEC_v13',
        'HLT_DiPFJetAve260_v28',
        'HLT_DiPFJetAve300_HFJEC_v30',
        'HLT_DiPFJetAve320_v28',
        'HLT_DiPFJetAve400_v28',
        'HLT_DiPFJetAve40_v28',
        'HLT_DiPFJetAve500_v28',
        'HLT_DiPFJetAve60_HFJEC_v29',
        'HLT_DiPFJetAve60_v28',
        'HLT_DiPFJetAve80_HFJEC_v31',
        'HLT_DiPFJetAve80_v28',
        'HLT_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_HT350_v9',
        'HLT_HT425_v21',
        'HLT_L1ETMHadSeeds_v11',
        'HLT_L1Mu6HT240_v10',
        'HLT_MET105_IsoTrk50_v21',
        'HLT_MET120_IsoTrk50_v21',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12eta2p3_PFJet40_v15',
        'HLT_Mu12eta2p3_v15',
        'HLT_PFHT1050_v32',
        'HLT_PFHT180_v31',
        'HLT_PFHT250_v31',
        'HLT_PFHT350_v33',
        'HLT_PFHT370_v31',
        'HLT_PFHT430_v31',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v26',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v26',
        'HLT_PFHT510_v31',
        'HLT_PFHT590_v31',
        'HLT_PFHT680_v31',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v26',
        'HLT_PFHT780_v31',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v26',
        'HLT_PFHT890_v31',
        'HLT_PFJet110_v14',
        'HLT_PFJet140_v33',
        'HLT_PFJet200_v33',
        'HLT_PFJet260_v34',
        'HLT_PFJet320_v34',
        'HLT_PFJet400_v34',
        'HLT_PFJet40_v35',
        'HLT_PFJet450_v35',
        'HLT_PFJet500_v35',
        'HLT_PFJet550_v25',
        'HLT_PFJet60_v35',
        'HLT_PFJet80_v35',
        'HLT_PFJetFwd140_v32',
        'HLT_PFJetFwd200_v32',
        'HLT_PFJetFwd260_v33',
        'HLT_PFJetFwd320_v33',
        'HLT_PFJetFwd400_v33',
        'HLT_PFJetFwd40_v33',
        'HLT_PFJetFwd450_v33',
        'HLT_PFJetFwd500_v33',
        'HLT_PFJetFwd60_v33',
        'HLT_PFJetFwd80_v32',
        'HLT_PFMET105_IsoTrk50_v15',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v23',
        'HLT_PFMET120_PFMHT120_IDTight_v34',
        'HLT_PFMET130_PFMHT130_IDTight_v34',
        'HLT_PFMET140_PFMHT140_IDTight_v34',
        'HLT_PFMET200_BeamHaloCleaned_v23',
        'HLT_PFMET200_NotCleaned_v23',
        'HLT_PFMET250_NotCleaned_v23',
        'HLT_PFMET300_NotCleaned_v23',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v23',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v34',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v33',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v33',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v25',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v23'
    ),
    L1Accept = cms.vstring(
        'DST_Physics_v17',
        'DST_ZeroBias_v12'
    ),
    MonteCarlo = cms.vstring(
        'MC_AK4CaloJetsFromPV_v20',
        'MC_AK4CaloJets_v21',
        'MC_AK4PFJetPNet_v7',
        'MC_AK4PFJets_v31',
        'MC_AK8CaloHT_v20',
        'MC_AK8PFHT_v30',
        'MC_AK8PFJetPNet_v7',
        'MC_AK8PFJets_v31',
        'MC_CaloHT_v20',
        'MC_CaloMET_JetIdCleaned_v21',
        'MC_CaloMET_v20',
        'MC_CaloMHT_v20',
        'MC_Diphoton10_10_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass10_v25',
        'MC_DoubleEle5_CaloIdL_MW_v28',
        'MC_DoubleMuNoFiltersNoVtx_v19',
        'MC_DoubleMu_TrkIsoVVL_DZ_v25',
        'MC_Egamma_Open_Unseeded_v10',
        'MC_Egamma_Open_v10',
        'MC_Ele15_Ele10_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'MC_Ele5_WPTight_Gsf_v20',
        'MC_IsoMu_v29',
        'MC_PFHT_v30',
        'MC_PFMET_v31',
        'MC_PFMHT_v30',
        'MC_PFScouting_v8',
        'MC_ReducedIterativeTracking_v24'
    ),
    Muon0 = cms.vstring(
        'HLT_CascadeMu100_v15',
        'HLT_CscCluster100_Ele5_v6',
        'HLT_CscCluster100_Mu5_v8',
        'HLT_CscCluster100_PNetTauhPFJet10_Loose_v8',
        'HLT_CscCluster50_Photon20Unseeded_v5',
        'HLT_CscCluster50_Photon30Unseeded_v5',
        'HLT_CscCluster_Loose_v11',
        'HLT_CscCluster_Medium_v11',
        'HLT_CscCluster_Tight_v11',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v10',
        'HLT_DoubleCscCluster100_v8',
        'HLT_DoubleCscCluster75_v8',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v14',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu50_v12',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v13',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v24',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v24',
        'HLT_DoubleMu43NoFiltersNoVtx_v16',
        'HLT_DoubleMu48NoFiltersNoVtx_v16',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v22',
        'HLT_HighPtTkMu100_v14',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Loose_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Medium_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Tight_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_v29',
        'HLT_IsoMu24_OneProng32_v11',
        'HLT_IsoMu24_TwoProngs35_v15',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_PNet1Tauh0p50_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_v2',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet20_eta2p2_SingleL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet60_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet75_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Loose_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet45_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_v29',
        'HLT_IsoMu24_v27',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v10',
        'HLT_IsoMu27_v30',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v14',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v14',
        'HLT_IsoTrk200_L1SingleMuShower_v6',
        'HLT_IsoTrk400_L1SingleMuShower_v6',
        'HLT_L1CSCShower_DTCluster50_v11',
        'HLT_L1CSCShower_DTCluster75_v11',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v5',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v5',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v12',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v7',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v29',
        'HLT_Mu15_IsoVVVL_PFHT450_v29',
        'HLT_Mu15_IsoVVVL_PFHT600_v33',
        'HLT_Mu15_v17',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v8',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v29',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v28',
        'HLT_Mu17_TrkIsoVVL_v27',
        'HLT_Mu17_v27',
        'HLT_Mu18_Mu9_SameSign_v18',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v17',
        'HLT_Mu19_TrkIsoVVL_v18',
        'HLT_Mu19_v18',
        'HLT_Mu20_v26',
        'HLT_Mu27_v27',
        'HLT_Mu37_TkMu27_v19',
        'HLT_Mu3_PFJet40_v30',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v16',
        'HLT_Mu50_IsoVVVL_PFHT450_v29',
        'HLT_Mu50_L1SingleMuShower_v13',
        'HLT_Mu50_v27',
        'HLT_Mu55_v17',
        'HLT_Mu8_TrkIsoVVL_v26',
        'HLT_Mu8_v26',
        'HLT_TripleMu_10_5_5_DZ_v24',
        'HLT_TripleMu_12_10_5_v24',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v17',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v22',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v19'
    ),
    Muon1 = cms.vstring(
        'HLT_CascadeMu100_v15',
        'HLT_CscCluster100_Ele5_v6',
        'HLT_CscCluster100_Mu5_v8',
        'HLT_CscCluster100_PNetTauhPFJet10_Loose_v8',
        'HLT_CscCluster50_Photon20Unseeded_v5',
        'HLT_CscCluster50_Photon30Unseeded_v5',
        'HLT_CscCluster_Loose_v11',
        'HLT_CscCluster_Medium_v11',
        'HLT_CscCluster_Tight_v11',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v10',
        'HLT_DoubleCscCluster100_v8',
        'HLT_DoubleCscCluster75_v8',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v14',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu50_v12',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v13',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v24',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v24',
        'HLT_DoubleMu43NoFiltersNoVtx_v16',
        'HLT_DoubleMu48NoFiltersNoVtx_v16',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v22',
        'HLT_HighPtTkMu100_v14',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Loose_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Medium_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_eta2p1_PNetTauhPFJet27_Tight_eta2p3_CrossL1_v8',
        'HLT_IsoMu20_v29',
        'HLT_IsoMu24_OneProng32_v11',
        'HLT_IsoMu24_TwoProngs35_v15',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_PNet1Tauh0p50_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_v2',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet20_eta2p2_SingleL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet60_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_PFJet75_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet26_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Loose_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_eta2p3_CrossL1_ETau_Monitoring_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet45_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_v29',
        'HLT_IsoMu24_v27',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v10',
        'HLT_IsoMu27_v30',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v14',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v14',
        'HLT_IsoTrk200_L1SingleMuShower_v6',
        'HLT_IsoTrk400_L1SingleMuShower_v6',
        'HLT_L1CSCShower_DTCluster50_v11',
        'HLT_L1CSCShower_DTCluster75_v11',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v5',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v5',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v12',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v7',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v29',
        'HLT_Mu15_IsoVVVL_PFHT450_v29',
        'HLT_Mu15_IsoVVVL_PFHT600_v33',
        'HLT_Mu15_v17',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v8',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v29',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v28',
        'HLT_Mu17_TrkIsoVVL_v27',
        'HLT_Mu17_v27',
        'HLT_Mu18_Mu9_SameSign_v18',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v17',
        'HLT_Mu19_TrkIsoVVL_v18',
        'HLT_Mu19_v18',
        'HLT_Mu20_v26',
        'HLT_Mu27_v27',
        'HLT_Mu37_TkMu27_v19',
        'HLT_Mu3_PFJet40_v30',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v16',
        'HLT_Mu50_IsoVVVL_PFHT450_v29',
        'HLT_Mu50_L1SingleMuShower_v13',
        'HLT_Mu50_v27',
        'HLT_Mu55_v17',
        'HLT_Mu8_TrkIsoVVL_v26',
        'HLT_Mu8_v26',
        'HLT_TripleMu_10_5_5_DZ_v24',
        'HLT_TripleMu_12_10_5_v24',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v17',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v22',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v19'
    ),
    MuonEG = cms.vstring(
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v31',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v31',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v31',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v29',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Mu17_Photon30_IsoCaloId_v20',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v13',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v29',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Mu27_Ele37_CaloIdL_MW_v19',
        'HLT_Mu37_Ele27_CaloIdL_MW_v19',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v13',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v13',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v17',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v17',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v32',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v32',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v33',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v33',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v12',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v12',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet20_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet25_PNet1BTag0p50_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet25_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet1BTag0p20_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v25'
    ),
    NoBPTX = cms.vstring(
        'HLT_CDC_L2cosmic_10_er1p0_v11',
        'HLT_CDC_L2cosmic_5p5_er1p0_v11',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v15',
        'HLT_L2Mu10_NoVertex_NoBPTX_v16',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v15',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v14',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v16',
        'HLT_UncorrectedJetE30_NoBPTX_v16',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v16',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v16'
    ),
    OnlineMonitor = cms.vstring( (
        'HLT_AK8DiPFJet250_250_SoftDropMass40_v8',
        'HLT_AK8DiPFJet250_250_SoftDropMass50_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass30_v8',
        'HLT_AK8DiPFJet260_260_SoftDropMass40_v8',
        'HLT_AK8DiPFJet270_270_SoftDropMass30_v8',
        'HLT_AK8DiPFJet280_280_SoftDropMass30_v14',
        'HLT_AK8DiPFJet290_290_SoftDropMass30_v8',
        'HLT_AK8PFJet140_v29',
        'HLT_AK8PFJet200_v29',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55_v11',
        'HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60_v11',
        'HLT_AK8PFJet220_SoftDropMass40_v15',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet230_SoftDropMass40_v15',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet260_v30',
        'HLT_AK8PFJet275_Nch40_v8',
        'HLT_AK8PFJet275_Nch45_v8',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03_v11',
        'HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05_v11',
        'HLT_AK8PFJet320_v30',
        'HLT_AK8PFJet380_SoftDropMass30_v8',
        'HLT_AK8PFJet400_SoftDropMass30_v8',
        'HLT_AK8PFJet400_v30',
        'HLT_AK8PFJet40_v30',
        'HLT_AK8PFJet425_SoftDropMass30_v8',
        'HLT_AK8PFJet450_SoftDropMass30_v8',
        'HLT_AK8PFJet450_v30',
        'HLT_AK8PFJet500_v30',
        'HLT_AK8PFJet550_v25',
        'HLT_AK8PFJet60_v29',
        'HLT_AK8PFJet80_v30',
        'HLT_AK8PFJetFwd140_v28',
        'HLT_AK8PFJetFwd200_v28',
        'HLT_AK8PFJetFwd260_v29',
        'HLT_AK8PFJetFwd320_v29',
        'HLT_AK8PFJetFwd400_v29',
        'HLT_AK8PFJetFwd40_v29',
        'HLT_AK8PFJetFwd450_v29',
        'HLT_AK8PFJetFwd500_v29',
        'HLT_AK8PFJetFwd60_v28',
        'HLT_AK8PFJetFwd80_v28',
        'HLT_BTagMu_AK4DiJet110_Mu5_v27',
        'HLT_BTagMu_AK4DiJet170_Mu5_v26',
        'HLT_BTagMu_AK4DiJet20_Mu5_v27',
        'HLT_BTagMu_AK4DiJet40_Mu5_v27',
        'HLT_BTagMu_AK4DiJet70_Mu5_v27',
        'HLT_BTagMu_AK4Jet300_Mu5_v26',
        'HLT_BTagMu_AK8DiJet170_Mu5_v23',
        'HLT_BTagMu_AK8Jet170_DoubleMu5_v16',
        'HLT_BTagMu_AK8Jet300_Mu5_v26',
        'HLT_CDC_L2cosmic_10_er1p0_v11',
        'HLT_CDC_L2cosmic_5p5_er1p0_v11',
        'HLT_CaloJet500_NoJetID_v24',
        'HLT_CaloJet550_NoJetID_v19',
        'HLT_CaloMET350_NotCleaned_v16',
        'HLT_CaloMET60_DTCluster50_v13',
        'HLT_CaloMET60_DTClusterNoMB1S50_v13',
        'HLT_CaloMET90_NotCleaned_v16',
        'HLT_CaloMHT90_v16',
        'HLT_CascadeMu100_v15',
        'HLT_CscCluster50_Photon20Unseeded_v5',
        'HLT_CscCluster50_Photon30Unseeded_v5',
        'HLT_CscCluster_Loose_v11',
        'HLT_CscCluster_Medium_v11',
        'HLT_CscCluster_Tight_v11',
        'HLT_DiEle27_WPTightCaloOnly_L1DoubleEG_v15',
        'HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8_v31',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v31',
        'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v31',
        'HLT_DiPFJetAve100_HFJEC_v31',
        'HLT_DiPFJetAve140_v27',
        'HLT_DiPFJetAve160_HFJEC_v30',
        'HLT_DiPFJetAve200_v27',
        'HLT_DiPFJetAve220_HFJEC_v30',
        'HLT_DiPFJetAve260_HFJEC_v13',
        'HLT_DiPFJetAve260_v28',
        'HLT_DiPFJetAve300_HFJEC_v30',
        'HLT_DiPFJetAve320_v28',
        'HLT_DiPFJetAve400_v28',
        'HLT_DiPFJetAve40_v28',
        'HLT_DiPFJetAve500_v28',
        'HLT_DiPFJetAve60_HFJEC_v29',
        'HLT_DiPFJetAve60_v28',
        'HLT_DiPFJetAve80_HFJEC_v31',
        'HLT_DiPFJetAve80_v28',
        'HLT_DiPhoton10Time1ns_v11',
        'HLT_DiPhoton10Time1p2ns_v11',
        'HLT_DiPhoton10Time1p4ns_v11',
        'HLT_DiPhoton10Time1p6ns_v11',
        'HLT_DiPhoton10Time1p8ns_v11',
        'HLT_DiPhoton10Time2ns_v11',
        'HLT_DiPhoton10_CaloIdL_v11',
        'HLT_DiSC30_18_EIso_AND_HE_Mass70_v25',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Dielectron12_5_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_10_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2_v1',
        'HLT_Diphoton15_12_EBEB_TightID_ECALTrackIsoDr0p2to0p4_v1',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT_v12',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55_v13',
        'HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_v13',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v25',
        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v25',
        'HLT_DiphotonMVA14p25_High_Mass60_v1',
        'HLT_DiphotonMVA14p25_Low_Mass60_v1',
        'HLT_DiphotonMVA14p25_Medium_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightHigh_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightLow_Mass60_v1',
        'HLT_DiphotonMVA14p25_TightMedium_Mass60_v1',
        'HLT_DisplacedMu24_MediumChargedIsoDisplacedPFTauHPS24_v10',
        'HLT_DoubleCscCluster100_v8',
        'HLT_DoubleCscCluster75_v8',
        'HLT_DoubleEle25_CaloIdL_MW_v17',
        'HLT_DoubleEle27_CaloIdL_MW_v17',
        'HLT_DoubleEle33_CaloIdL_MW_v30',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350_v34',
        'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350_v34',
        'HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v14',
        'HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm_v13',
        'HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu23NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu25NoVtx_2Cha_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4_v12',
        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v12',
        'HLT_DoubleL2Mu50_v12',
        'HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm_v12',
        'HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm_v13',
        'HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm_v12',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_noDxy_v10',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v15',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS36_Trk1_eta2p1_v10',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_noDCA_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_Mass2p0_v8',
        'HLT_DoubleMu3_DCA_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET50_PFMHT60_v24',
        'HLT_DoubleMu3_DZ_PFMET70_PFMHT70_v24',
        'HLT_DoubleMu3_DZ_PFMET90_PFMHT90_v24',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu43NoFiltersNoVtx_v16',
        'HLT_DoubleMu48NoFiltersNoVtx_v16',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_Mass3p8_DZ_PFHT350_v22',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_DoublePFJets116MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets128MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_DoublePhoton33_CaloIdL_v18',
        'HLT_DoublePhoton70_v18',
        'HLT_DoublePhoton85_v26',
        'HLT_ECALHT800_v22',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v27',
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele135_CaloIdVT_GsfTrkIdT_v20',
        'HLT_Ele14_eta2p5_IsoVVVL_Gsf_PFHT200_PNetBTag0p53_v7',
        'HLT_Ele15_IsoVVVL_PFHT450_PFMET50_v30',
        'HLT_Ele15_IsoVVVL_PFHT450_v30',
        'HLT_Ele15_IsoVVVL_PFHT600_v34',
        'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v30',
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v32',
        'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v31',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31',
        'HLT_Ele28_HighEta_SC20_Mass55_v25',
        'HLT_Ele30_WPTight_Gsf_v13',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v21',
        'HLT_Ele32_WPTight_Gsf_v27',
        'HLT_Ele35_WPTight_Gsf_v21',
        'HLT_Ele38_WPTight_Gsf_v21',
        'HLT_Ele40_WPTight_Gsf_v21',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_v14',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v32',
        'HLT_Ele50_IsoVVVL_PFHT450_v30',
        'HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v30',
        'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v32',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p7_v8',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p8_v8',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v9',
        'HLT_HT350_v9',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT425_v21',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v12',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v9',
        'HLT_HT550_DisplacedDijet60_Inclusive_v25',
        'HLT_HcalNZS_v22',
        'HLT_HcalPhiSym_v24',
        'HLT_HighPtTkMu100_v14',
        'HLT_IsoMu20_v29',
        'HLT_IsoMu24_OneProng32_v11',
        'HLT_IsoMu24_TwoProngs35_v15',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_PNet1Tauh0p50_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_QuadPFJet25_v2',
        'HLT_IsoMu24_eta2p1_L1HT200_v2',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_QuadPFJet25_v8',
        'HLT_IsoMu24_eta2p1_PFHT250_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Loose_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet130_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Medium_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_PNetTauhPFJet30_Tight_L2NN_eta2p3_CrossL1_v8',
        'HLT_IsoMu24_eta2p1_SinglePFJet25_PNet1Tauh0p50_v8',
        'HLT_IsoMu24_eta2p1_v29',
        'HLT_IsoMu24_v27',
        'HLT_IsoMu27_MediumChargedIsoDisplacedPFTauHPS24_eta2p1_SingleL1_v10',
        'HLT_IsoMu27_v30',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet220_SoftDropMass40_v14',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10_v11',
        'HLT_IsoMu50_AK8PFJet230_SoftDropMass40_v14',
        'HLT_L1CSCShower_DTCluster50_v11',
        'HLT_L1CSCShower_DTCluster75_v11',
        'HLT_L1ETMHadSeeds_v11',
        'HLT_L1MET_DTCluster50_v13',
        'HLT_L1MET_DTClusterNoMB1S50_v13',
        'HLT_L1Mu6HT240_v10',
        'HLT_L1SingleLLPJet_v8',
        'HLT_L1SingleMuCosmics_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v9',
        'HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142_v10',
        'HLT_L2Mu10_NoVertex_NoBPTX3BX_v15',
        'HLT_L2Mu10_NoVertex_NoBPTX_v16',
        'HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v15',
        'HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v14',
        'HLT_L2Mu50NoVtx_3Cha_CosmicSeed_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L2Mu50NoVtx_3Cha_VetoL3Mu0DxyMax1cm_v6',
        'HLT_L3Mu30NoVtx_DxyMin0p01cm_v5',
        'HLT_L3Mu50NoVtx_DxyMin0p01cm_v5',
        'HLT_L3dTksMu10_NoVtx_DxyMin0p01cm_v12',
        'HLT_MET105_IsoTrk50_v21',
        'HLT_MET120_IsoTrk50_v21',
        'HLT_Mu12_DoublePFJets100_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets200_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets350_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12_DoublePFJets40_PNetBTag_0p11_v8',
        'HLT_Mu12_DoublePFJets54MaxDeta1p6_PNet2BTag_0p11_v8',
        'HLT_Mu12_IsoVVL_PFHT150_PNetBTag0p53_v7',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v29',
        'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Mu12eta2p3_PFJet40_v15',
        'HLT_Mu12eta2p3_v15',
        'HLT_Mu15_IsoVVVL_PFHT450_PFMET50_v29',
        'HLT_Mu15_IsoVVVL_PFHT450_v29',
        'HLT_Mu15_IsoVVVL_PFHT600_v33',
        'HLT_Mu15_v17',
        'HLT_Mu17_Photon30_IsoCaloId_v20',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_AK8PFJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_CaloJet30_v7',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_PFJet30_v8',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v19',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v29',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v28',
        'HLT_Mu17_TrkIsoVVL_v27',
        'HLT_Mu17_v27',
        'HLT_Mu18_Mu9_SameSign_v18',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_v17',
        'HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_v17',
        'HLT_Mu19_TrkIsoVVL_v18',
        'HLT_Mu19_v18',
        'HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId_v13',
        'HLT_Mu20_v26',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v29',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v21',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu27_Ele37_CaloIdL_MW_v19',
        'HLT_Mu27_v27',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu37_Ele27_CaloIdL_MW_v19',
        'HLT_Mu37_TkMu27_v19',
        'HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL_v13',
        'HLT_Mu3_PFJet40_v30',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight_v16',
        'HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight_v16',
        'HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL_v13',
        'HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL_v17',
        'HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL_v17',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu50_IsoVVVL_PFHT450_v29',
        'HLT_Mu50_L1SingleMuShower_v13',
        'HLT_Mu50_v27',
        'HLT_Mu55_v17',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v32',
        'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v32',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ_v33',
        'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_v33',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50_v12',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_v12',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet20_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet25_PNet1BTag0p50_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_QuadPFJet25_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_L1HT200_v2',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v15',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet1BTag0p20_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_QuadPFJet25_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT250_v8',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_v11',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v27',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v25',
        'HLT_Mu8_TrkIsoVVL_v26',
        'HLT_Mu8_v26',
        'HLT_PFHT1050_v32',
        'HLT_PFHT180_v31',
        'HLT_PFHT250_v31',
        'HLT_PFHT350_v33',
        'HLT_PFHT370_v31',
        'HLT_PFHT430_v31',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v26',
        'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v26',
        'HLT_PFHT510_v31',
        'HLT_PFHT590_v31',
        'HLT_PFHT680_v31',
        'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v26',
        'HLT_PFHT780_v31',
        'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v26',
        'HLT_PFHT890_v31',
        'HLT_PFJet110_v14',
        'HLT_PFJet140_v33',
        'HLT_PFJet200_TimeGt2p5ns_v12',
        'HLT_PFJet200_TimeLtNeg2p5ns_v12',
        'HLT_PFJet200_v33',
        'HLT_PFJet260_v34',
        'HLT_PFJet320_v34',
        'HLT_PFJet400_v34',
        'HLT_PFJet40_v35',
        'HLT_PFJet450_v35',
        'HLT_PFJet500_v35',
        'HLT_PFJet550_v25',
        'HLT_PFJet60_v35',
        'HLT_PFJet80_v35',
        'HLT_PFJetFwd140_v32',
        'HLT_PFJetFwd200_v32',
        'HLT_PFJetFwd260_v33',
        'HLT_PFJetFwd320_v33',
        'HLT_PFJetFwd400_v33',
        'HLT_PFJetFwd40_v33',
        'HLT_PFJetFwd450_v33',
        'HLT_PFJetFwd500_v33',
        'HLT_PFJetFwd60_v33',
        'HLT_PFJetFwd80_v32',
        'HLT_PFMET105_IsoTrk50_v15',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v23',
        'HLT_PFMET120_PFMHT120_IDTight_v34',
        'HLT_PFMET130_PFMHT130_IDTight_v34',
        'HLT_PFMET140_PFMHT140_IDTight_v34',
        'HLT_PFMET200_BeamHaloCleaned_v23',
        'HLT_PFMET200_NotCleaned_v23',
        'HLT_PFMET250_NotCleaned_v23',
        'HLT_PFMET300_NotCleaned_v23',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v23',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v34',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v33',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v14',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v33',
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v25',
        'HLT_PFMETTypeOne200_BeamHaloCleaned_v23',
        'HLT_Photon100EBHE10_v13',
        'HLT_Photon110EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon110EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon110EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon110EB_TightID_TightIso_v14',
        'HLT_Photon120_R9Id90_HE10_IsoM_v26',
        'HLT_Photon120_v24',
        'HLT_Photon150_v18',
        'HLT_Photon165_R9Id90_HE10_IsoM_v27',
        'HLT_Photon175_v26',
        'HLT_Photon200_v25',
        'HLT_Photon20_HoverELoose_v21',
        'HLT_Photon300_NoHE_v24',
        'HLT_Photon30EB_TightID_TightIso_v14',
        'HLT_Photon30_HoverELoose_v21',
        'HLT_Photon32_OneProng32_M50To105_v12',
        'HLT_Photon33_v16',
        'HLT_Photon34_R9Id90_CaloIdL_IsoL_DisplacedIdL_MediumChargedIsoDisplacedPFTauHPS34_v10',
        'HLT_Photon35_TwoProngs35_v15',
        'HLT_Photon40EB_TightID_TightIso_v5',
        'HLT_Photon40EB_v4',
        'HLT_Photon45EB_TightID_TightIso_v5',
        'HLT_Photon45EB_v4',
        'HLT_Photon50EB_TightID_TightIso_AK8CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_AK8PFJet30_v7',
        'HLT_Photon50EB_TightID_TightIso_CaloJet30_v5',
        'HLT_Photon50EB_TightID_TightIso_PFJet30_v8',
        'HLT_Photon50EB_TightID_TightIso_v10',
        'HLT_Photon50_R9Id90_HE10_IsoM_v26',
        'HLT_Photon50_TimeGt2p5ns_v8',
        'HLT_Photon50_TimeLtNeg2p5ns_v8',
        'HLT_Photon50_v24',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380_v12',
        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400_v12',
        'HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v11',
        'HLT_Photon75EB_TightID_TightIso_v10',
        'HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3_v19',
        'HLT_Photon75_R9Id90_HE10_IsoM_v26',
        'HLT_Photon75_v24',
        'HLT_Photon90EB_TightID_TightIso_v10',
        'HLT_Photon90_R9Id90_HE10_IsoM_v26',
        'HLT_Photon90_v24',
        'HLT_Physics_v15',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_Random_v3',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16',
        'HLT_TripleMu_10_5_5_DZ_v24',
        'HLT_TripleMu_12_10_5_v24',
        'HLT_TripleMu_5_3_3_Mass3p8_DCA_v17',
        'HLT_TripleMu_5_3_3_Mass3p8_DZ_v22',
        'HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx_v19',
        'HLT_UncorrectedJetE30_NoBPTX3BX_v16',
        'HLT_UncorrectedJetE30_NoBPTX_v16',
        'HLT_UncorrectedJetE60_NoBPTX3BX_v16',
        'HLT_UncorrectedJetE70_NoBPTX3BX_v16',
        'HLT_ZeroBias_Alignment_v9',
        'HLT_ZeroBias_FirstBXAfterTrain_v11',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v13',
        'HLT_ZeroBias_FirstCollisionInTrain_v12',
        'HLT_ZeroBias_IsolatedBunches_v13',
        'HLT_ZeroBias_LastCollisionInTrain_v11',
        'HLT_ZeroBias_v14'
     ) ),
    ParkingAnomalyDetection = cms.vstring(
        'HLT_L1AXOVVTight_v1',
        'HLT_L1AXOVVVTight_v1',
        'HLT_L1CICADA_VVTight_v1',
        'HLT_L1CICADA_VVVTight_v1',
        'HLT_L1CICADA_VVVVTight_v1'
    ),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass4 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass5 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass6 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingDoubleMuonLowMass7 = cms.vstring(
        'HLT_Dimuon0_Jpsi3p5_Muon2_v19',
        'HLT_Dimuon0_Jpsi_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_L1_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_NoOS_v21',
        'HLT_Dimuon0_Jpsi_NoVertexing_v22',
        'HLT_Dimuon0_Jpsi_v22',
        'HLT_Dimuon0_LowMass_L1_0er1p5_v22',
        'HLT_Dimuon0_LowMass_L1_4_v22',
        'HLT_Dimuon0_LowMass_L1_TM530_v20',
        'HLT_Dimuon0_LowMass_v22',
        'HLT_Dimuon0_Upsilon_L1_4p5_v23',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0M_v21',
        'HLT_Dimuon0_Upsilon_L1_4p5er2p0_v23',
        'HLT_Dimuon0_Upsilon_Muon_NoL1Mass_v20',
        'HLT_Dimuon0_Upsilon_NoVertexing_v21',
        'HLT_Dimuon10_Upsilon_y1p4_v15',
        'HLT_Dimuon12_Upsilon_y1p4_v16',
        'HLT_Dimuon14_Phi_Barrel_Seagulls_v21',
        'HLT_Dimuon14_PsiPrime_noCorrL1_v19',
        'HLT_Dimuon14_PsiPrime_v27',
        'HLT_Dimuon18_PsiPrime_noCorrL1_v20',
        'HLT_Dimuon18_PsiPrime_v28',
        'HLT_Dimuon24_Phi_noCorrL1_v20',
        'HLT_Dimuon24_Upsilon_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_noCorrL1_v20',
        'HLT_Dimuon25_Jpsi_v28',
        'HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v20',
        'HLT_DoubleMu2_Jpsi_LowPt_v8',
        'HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon_v18',
        'HLT_DoubleMu3_TkMu_DsTau3Mu_v18',
        'HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass_v20',
        'HLT_DoubleMu3_Trk_Tau3mu_v26',
        'HLT_DoubleMu4_3_Bs_v29',
        'HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_3_Jpsi_v29',
        'HLT_DoubleMu4_3_LowMass_SS_v8',
        'HLT_DoubleMu4_3_LowMass_v15',
        'HLT_DoubleMu4_3_Photon4_BsToMMG_v14',
        'HLT_DoubleMu4_JpsiTrkTrk_Displaced_v21',
        'HLT_DoubleMu4_JpsiTrk_Bc_v14',
        'HLT_DoubleMu4_Jpsi_Displaced_v21',
        'HLT_DoubleMu4_Jpsi_NoVertexing_v21',
        'HLT_DoubleMu4_LowMass_Displaced_v15',
        'HLT_DoubleMu4_MuMuTrk_Displaced_v29',
        'HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL_v18',
        'HLT_Mu25_TkMu0_Phi_v22',
        'HLT_Mu30_TkMu0_Psi_v15',
        'HLT_Mu30_TkMu0_Upsilon_v15',
        'HLT_Mu4_L1DoubleMu_v15',
        'HLT_Mu7p5_L2Mu2_Jpsi_v24',
        'HLT_Mu7p5_L2Mu2_Upsilon_v24',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1_v18',
        'HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_v18',
        'HLT_Trimuon5_3p5_2_Upsilon_Muon_v19',
        'HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon_v16'
    ),
    ParkingHH0 = cms.vstring(
        'HLT_L1HT200_QuadPFJet20_PNet1BTag0p50_PNet1Tauh0p50_v2',
        'HLT_L1HT200_QuadPFJet25_PNet1BTag0p50_PNet1Tauh0p50_v2',
        'HLT_PFHT250_QuadPFJet25_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v8',
        'HLT_PFHT250_QuadPFJet25_v8',
        'HLT_PFHT250_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT250_QuadPFJet30_PNet2BTagMean0p55_v8',
        'HLT_PFHT280_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v11',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60_v11',
        'HLT_PFHT280_QuadPFJet30_v11',
        'HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60_v11',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_2p0_v7',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_4p3_v7',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v23',
        'HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70_v12',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_4p3_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_5p6_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_v8',
        'HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50_v11',
        'HLT_PFHT400_SixPFJet32_v23',
        'HLT_PFHT450_SixPFJet36_PNetBTag0p35_v11',
        'HLT_PFHT450_SixPFJet36_v22'
    ),
    ParkingHH1 = cms.vstring(
        'HLT_L1HT200_QuadPFJet20_PNet1BTag0p50_PNet1Tauh0p50_v2',
        'HLT_L1HT200_QuadPFJet25_PNet1BTag0p50_PNet1Tauh0p50_v2',
        'HLT_PFHT250_QuadPFJet25_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT250_QuadPFJet25_PNet2BTagMean0p55_v8',
        'HLT_PFHT250_QuadPFJet25_v8',
        'HLT_PFHT250_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT250_QuadPFJet30_PNet2BTagMean0p55_v8',
        'HLT_PFHT280_QuadPFJet30_PNet1BTag0p20_PNet1Tauh0p50_v8',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55_v11',
        'HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60_v11',
        'HLT_PFHT280_QuadPFJet30_v11',
        'HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60_v11',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_2p0_v7',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_PNet3BTag_4p3_v7',
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v23',
        'HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70_v12',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_4p3_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_PNet2BTag_5p6_v8',
        'HLT_PFHT400_FivePFJet_120_120_60_30_30_v8',
        'HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50_v11',
        'HLT_PFHT400_SixPFJet32_v23',
        'HLT_PFHT450_SixPFJet36_PNetBTag0p35_v11',
        'HLT_PFHT450_SixPFJet36_v22'
    ),
    ParkingLLP0 = cms.vstring(
        'HLT_CaloMET60_DTCluster50_v13',
        'HLT_CaloMET60_DTClusterNoMB1S50_v13',
        'HLT_CscCluster150_DisplacedSingleJet30_Inclusive1PtrkShortSig5_v2',
        'HLT_CscCluster150_DisplacedSingleJet35_Inclusive1PtrkShortSig5_v2',
        'HLT_CscCluster150_DisplacedSingleJet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p7_v8',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p8_v8',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v9',
        'HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v12',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v25',
        'HLT_HT650_DisplacedDijet60_Inclusive_v25',
        'HLT_L1MET_DTCluster50_v13',
        'HLT_L1MET_DTClusterNoMB1S50_v13',
        'HLT_L1SingleLLPJet_v8',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v9',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v13',
        'HLT_PFJet200_TimeGt2p5ns_v12',
        'HLT_PFJet200_TimeLtNeg2p5ns_v12'
    ),
    ParkingLLP1 = cms.vstring(
        'HLT_CaloMET60_DTCluster50_v13',
        'HLT_CaloMET60_DTClusterNoMB1S50_v13',
        'HLT_CscCluster150_DisplacedSingleJet30_Inclusive1PtrkShortSig5_v2',
        'HLT_CscCluster150_DisplacedSingleJet35_Inclusive1PtrkShortSig5_v2',
        'HLT_CscCluster150_DisplacedSingleJet40_Inclusive1PtrkShortSig5_v2',
        'HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v13',
        'HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack_v13',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p7_v8',
        'HLT_HT200_L1SingleLLPJet_PFJet60_NeutralHadronFrac0p8_v8',
        'HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack_v13',
        'HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5_v10',
        'HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive_v9',
        'HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive_v9',
        'HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5_v9',
        'HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5_v9',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive_v12',
        'HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive_v13',
        'HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1nsTrackless_v13',
        'HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive_v11',
        'HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2nsInclusive_v13',
        'HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive_v9',
        'HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive_v9',
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v25',
        'HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5_v13',
        'HLT_HT550_DisplacedDijet60_Inclusive_v25',
        'HLT_HT650_DisplacedDijet60_Inclusive_v25',
        'HLT_L1MET_DTCluster50_v13',
        'HLT_L1MET_DTClusterNoMB1S50_v13',
        'HLT_L1SingleLLPJet_v8',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive_v11',
        'HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive_v9',
        'HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive_v9',
        'HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose_v13',
        'HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5_v13',
        'HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5_v13',
        'HLT_PFJet200_TimeGt2p5ns_v12',
        'HLT_PFJet200_TimeLtNeg2p5ns_v12'
    ),
    ParkingSingleMuon0 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon1 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon10 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon11 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon12 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon13 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon14 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon15 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon2 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon3 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon4 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon5 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon6 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon7 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon8 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingSingleMuon9 = cms.vstring(
        'HLT_Mu0_Barrel_L1HP10_v8',
        'HLT_Mu0_Barrel_L1HP11_v8',
        'HLT_Mu0_Barrel_L1HP13_v2',
        'HLT_Mu0_Barrel_L1HP6_IP6_v5',
        'HLT_Mu0_Barrel_L1HP6_v5',
        'HLT_Mu0_Barrel_L1HP7_v5',
        'HLT_Mu0_Barrel_L1HP8_v6',
        'HLT_Mu0_Barrel_L1HP9_v6',
        'HLT_Mu0_Barrel_v8',
        'HLT_Mu10_Barrel_L1HP11_IP4_v2',
        'HLT_Mu10_Barrel_L1HP11_IP6_v8',
        'HLT_Mu12_Barrel_L1HP13_IP4_v2',
        'HLT_Mu12_Barrel_L1HP13_IP6_v2',
        'HLT_Mu4_Barrel_IP4_v2',
        'HLT_Mu4_Barrel_IP6_v2',
        'HLT_Mu6_Barrel_L1HP7_IP6_v5',
        'HLT_Mu7_Barrel_L1HP8_IP6_v6',
        'HLT_Mu8_Barrel_L1HP9_IP6_v6',
        'HLT_Mu9_Barrel_L1HP10_IP6_v8'
    ),
    ParkingVBF0 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF1 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF2 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF3 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF4 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF5 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF6 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    ParkingVBF7 = cms.vstring(
        'HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet100_88_70_30_v12',
        'HLT_QuadPFJet103_88_75_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet103_88_75_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet103_88_75_15_v19',
        'HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight_v12',
        'HLT_QuadPFJet105_88_75_30_v11',
        'HLT_QuadPFJet105_88_76_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet105_88_76_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet105_88_76_15_v19',
        'HLT_QuadPFJet111_90_80_15_PNet2BTag_0p4_0p12_VBF1_v8',
        'HLT_QuadPFJet111_90_80_15_PNetBTag_0p4_VBF2_v8',
        'HLT_QuadPFJet111_90_80_15_v19',
        'HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight_v12',
        'HLT_QuadPFJet111_90_80_30_v11',
        'HLT_VBF_DiPFJet115_40_Mjj1000_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1100_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj1200_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet115_40_Mjj850_DoublePNetTauhPFJet20_eta2p3_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1050_v10',
        'HLT_VBF_DiPFJet125_45_Mjj1150_v2',
        'HLT_VBF_DiPFJet125_45_Mjj1250_v2',
        'HLT_VBF_DiPFJet45_Mjj650_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj750_PNetTauhPFJet45_L2NN_eta2p3_v8',
        'HLT_VBF_DiPFJet45_Mjj850_PNetTauhPFJet45_L2NN_eta2p3_v2',
        'HLT_VBF_DiPFJet50_Mjj600_Ele22_eta2p1_WPTight_Gsf_v8',
        'HLT_VBF_DiPFJet50_Mjj650_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj700_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj750_Photon22_v8',
        'HLT_VBF_DiPFJet50_Mjj800_Ele22_eta2p1_WPTight_Gsf_v2',
        'HLT_VBF_DiPFJet50_Mjj850_Photon22_v2',
        'HLT_VBF_DiPFJet75_45_Mjj1000_DiPFJet60_v2',
        'HLT_VBF_DiPFJet75_45_Mjj800_DiPFJet60_v8',
        'HLT_VBF_DiPFJet75_45_Mjj900_DiPFJet60_v2',
        'HLT_VBF_DiPFJet80_45_Mjj650_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj750_PFMETNoMu85_v8',
        'HLT_VBF_DiPFJet80_45_Mjj850_PFMETNoMu85_v2',
        'HLT_VBF_DiPFJet95_45_Mjj750_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj850_Mu3_TrkIsoVVL_v8',
        'HLT_VBF_DiPFJet95_45_Mjj950_Mu3_TrkIsoVVL_v2'
    ),
    RPCMonitor = cms.vstring('AlCa_RPCMuonNormalisation_v24'),
    ScoutingPFMonitor = cms.vstring(
        'DST_PFScouting_DoubleMuonVtxMonitorJPsi_v2',
        'DST_PFScouting_DoubleMuonVtxMonitorZ_v2',
        'HLT_TriggersForScoutingPFMonitor_PS1000_v1',
        'HLT_TriggersForScoutingPFMonitor_PS125_v1',
        'HLT_TriggersForScoutingPFMonitor_PS250_v1',
        'HLT_TriggersForScoutingPFMonitor_PS500_v1'
    ),
    ScoutingPFRun3 = cms.vstring(
        'DST_PFScouting_AXOLoose_v6',
        'DST_PFScouting_AXOMedium_v2',
        'DST_PFScouting_AXOTight_v8',
        'DST_PFScouting_AXOVLoose_v6',
        'DST_PFScouting_AXOVTight_v6',
        'DST_PFScouting_CICADALoose_v4',
        'DST_PFScouting_CICADAMedium_v4',
        'DST_PFScouting_CICADATight_v4',
        'DST_PFScouting_CICADAVLoose_v4',
        'DST_PFScouting_CICADAVTight_v4',
        'DST_PFScouting_DoubleEG_v8',
        'DST_PFScouting_DoubleMuonNoVtx_v2',
        'DST_PFScouting_DoubleMuonVtxMonitorJPsi_v2',
        'DST_PFScouting_DoubleMuonVtxMonitorZ_v2',
        'DST_PFScouting_DoubleMuonVtx_v2',
        'DST_PFScouting_JetHT_v8',
        'DST_PFScouting_SingleMuon_v8',
        'DST_PFScouting_SinglePhotonEB_v5',
        'DST_PFScouting_ZeroBias_v6'
    ),
    Tau = cms.vstring(
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_noDxy_v10',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1_v15',
        'HLT_DoubleMediumChargedIsoDisplacedPFTauHPS36_Trk1_eta2p1_v10',
        'HLT_DoublePNetTauhPFJet26_L2NN_eta2p3_PFJet60_v8',
        'HLT_DoublePNetTauhPFJet26_L2NN_eta2p3_PFJet75_v8',
        'HLT_DoublePNetTauhPFJet30_Medium_L2NN_eta2p3_v8',
        'HLT_DoublePNetTauhPFJet30_Tight_L2NN_eta2p3_v8',
        'HLT_SinglePNetTauhPFJet130_Loose_L2NN_eta2p3_v8',
        'HLT_SinglePNetTauhPFJet130_Medium_L2NN_eta2p3_v8',
        'HLT_SinglePNetTauhPFJet130_Tight_L2NN_eta2p3_v8'
    ),
    TestDataRaw = cms.vstring('HLT_TestData_v1'),
    TestDataScouting = cms.vstring('HLT_TestData_v1'),
    TestEnablesEcalHcal = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v6'
    ),
    TestEnablesEcalHcalDQM = cms.vstring(
        'HLT_EcalCalibration_v4',
        'HLT_HcalCalibration_v6'
    ),
    ZeroBias = cms.vstring(
        'HLT_Random_v3',
        'HLT_ZeroBias_Alignment_v9',
        'HLT_ZeroBias_FirstBXAfterTrain_v11',
        'HLT_ZeroBias_FirstCollisionAfterAbortGap_v13',
        'HLT_ZeroBias_FirstCollisionInTrain_v12',
        'HLT_ZeroBias_IsolatedBunches_v13',
        'HLT_ZeroBias_LastCollisionInTrain_v11',
        'HLT_ZeroBias_v14'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring( (
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm4',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp4',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfDigi_TIDP_D1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfCluster_TIDP_D1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfDigi_TIB_L1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfCluster_TIB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfDigi_TOB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfCluster_TOB_L1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfDigi_TECP_W1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfCluster_TECP_W1',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfTracks_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPt_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEta_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Strip_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Pixel_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBS_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSdz_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsPhi_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsEta_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackQoverP_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/Quality_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_PUvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtLoose_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaLoose_ImpactPoint_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/NumberOfGoodPVtx_offline',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/GoodPVtxNumberOfTracks_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_PUvtx_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/FractionOfGoodPVtx_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_op_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_op_ImpactPoint_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'OfflinePV/offlinePrimaryVertices/tagDiffX',
        'OfflinePV/offlinePrimaryVertices/tagDiffY',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/PtJetMET/Jet/Cleanedak4PFJetsPuppi/Phi',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/NJets',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta_uncor',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices',
        'JetMET/HIJetValidation/akCs4PFJets/SumPFPt',
        'JetMET/HIJetValidation/akCs4PFJets/NJets',
        'JetMET/HIJetValidation/akCs4PFJets/NPFpart',
        'JetMET/HIJetValidation/akPu4CaloJets/SumCaloPt',
        'JetMET/HIJetValidation/akPu4CaloJets/NCalopart',
        'JetMET/HIJetValidation/akPu4CaloJets/NJets',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi',
        'Muons/MuonRecoAnalyzer/Res_TkGlb_qOverlap',
        'Muons/diMuonHistograms/GlbGlbMuon_LM',
        'Muons/diMuonHistograms/GlbGlbMuon_HM',
        'Muons/Isolation/global/relPFIso_R03',
        'Muons/globalMuons/GeneralProperties/NumberOfMeanRecHitsPerTrack_glb',
        'Muons/standAloneMuonsUpdatedAtVtx/HitProperties/NumberOfValidRecHitsPerTrack_sta',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_pt',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_eta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele0_vertexPt_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele1_vertexPt_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele2_vertexEta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele5_vertexZ',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele101_etaEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele102_phiEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele201_mee_os'
     ) )
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.streams = cms.PSet(
    ALCAHcalIsoTrk = cms.vstring('AlCaHcalIsoTrk'),
    ALCALowPtJet = cms.vstring('AlCaLowPtJet'),
    ALCALumiPixelsCountsExpress = cms.vstring('AlCaLumiPixelsCountsExpress'),
    ALCALumiPixelsCountsPrompt = cms.vstring('AlCaLumiPixelsCountsPrompt'),
    ALCAP0 = cms.vstring('AlCaP0'),
    ALCAPHISYM = cms.vstring('AlCaPhiSym'),
    ALCAPPSExpress = cms.vstring('AlCaPPSExpress'),
    ALCAPPSPrompt = cms.vstring('AlCaPPSPrompt'),
    Calibration = cms.vstring('TestEnablesEcalHcal'),
    DQM = cms.vstring('OnlineMonitor'),
    DQMCalibration = cms.vstring('TestEnablesEcalHcalDQM'),
    DQMEventDisplay = cms.vstring('EventDisplay'),
    DQMGPUvsCPU = cms.vstring('DQMGPUvsCPU'),
    DQMOnlineBeamspot = cms.vstring('DQMOnlineBeamspot'),
    DQMPPSRandom = cms.vstring('DQMPPSRandom'),
    EcalCalibration = cms.vstring('EcalLaser'),
    Express = cms.vstring('ExpressPhysics'),
    ExpressAlignment = cms.vstring('ExpressAlignment'),
    HLTMonitor = cms.vstring('HLTMonitor'),
    LocalTestDataRaw = cms.vstring('TestDataRaw'),
    LocalTestDataScouting = cms.vstring('TestDataScouting'),
    NanoDST = cms.vstring('L1Accept'),
    ParkingAnomalyDetection = cms.vstring('ParkingAnomalyDetection'),
    ParkingDoubleMuonLowMass0 = cms.vstring(
        'ParkingDoubleMuonLowMass0',
        'ParkingDoubleMuonLowMass1'
    ),
    ParkingDoubleMuonLowMass1 = cms.vstring(
        'ParkingDoubleMuonLowMass2',
        'ParkingDoubleMuonLowMass3'
    ),
    ParkingDoubleMuonLowMass2 = cms.vstring(
        'ParkingDoubleMuonLowMass4',
        'ParkingDoubleMuonLowMass5'
    ),
    ParkingDoubleMuonLowMass3 = cms.vstring(
        'ParkingDoubleMuonLowMass6',
        'ParkingDoubleMuonLowMass7'
    ),
    ParkingHH = cms.vstring(
        'ParkingHH0',
        'ParkingHH1'
    ),
    ParkingLLP = cms.vstring(
        'ParkingLLP0',
        'ParkingLLP1'
    ),
    ParkingSingleMuon0 = cms.vstring('ParkingSingleMuon0'),
    ParkingSingleMuon1 = cms.vstring('ParkingSingleMuon1'),
    ParkingSingleMuon10 = cms.vstring('ParkingSingleMuon10'),
    ParkingSingleMuon11 = cms.vstring('ParkingSingleMuon11'),
    ParkingSingleMuon12 = cms.vstring('ParkingSingleMuon12'),
    ParkingSingleMuon13 = cms.vstring('ParkingSingleMuon13'),
    ParkingSingleMuon14 = cms.vstring('ParkingSingleMuon14'),
    ParkingSingleMuon15 = cms.vstring('ParkingSingleMuon15'),
    ParkingSingleMuon2 = cms.vstring('ParkingSingleMuon2'),
    ParkingSingleMuon3 = cms.vstring('ParkingSingleMuon3'),
    ParkingSingleMuon4 = cms.vstring('ParkingSingleMuon4'),
    ParkingSingleMuon5 = cms.vstring('ParkingSingleMuon5'),
    ParkingSingleMuon6 = cms.vstring('ParkingSingleMuon6'),
    ParkingSingleMuon7 = cms.vstring('ParkingSingleMuon7'),
    ParkingSingleMuon8 = cms.vstring('ParkingSingleMuon8'),
    ParkingSingleMuon9 = cms.vstring('ParkingSingleMuon9'),
    ParkingVBF0 = cms.vstring(
        'ParkingVBF0',
        'ParkingVBF1'
    ),
    ParkingVBF1 = cms.vstring(
        'ParkingVBF2',
        'ParkingVBF3'
    ),
    ParkingVBF2 = cms.vstring(
        'ParkingVBF4',
        'ParkingVBF5'
    ),
    ParkingVBF3 = cms.vstring(
        'ParkingVBF6',
        'ParkingVBF7'
    ),
    PhysicsBTagMuEGTau = cms.vstring(
        'BTagMu',
        'MuonEG',
        'Tau'
    ),
    PhysicsCommissioning = cms.vstring(
        'Commissioning',
        'Cosmics',
        'HLTPhysics',
        'HcalNZS',
        'MonteCarlo',
        'NoBPTX',
        'ZeroBias'
    ),
    PhysicsEGamma0 = cms.vstring('EGamma0'),
    PhysicsEGamma1 = cms.vstring('EGamma1'),
    PhysicsEGamma2 = cms.vstring('EGamma2'),
    PhysicsEGamma3 = cms.vstring('EGamma3'),
    PhysicsEmittanceScan0 = cms.vstring(
        'EmittanceScan0',
        'EmittanceScan1'
    ),
    PhysicsEmittanceScan1 = cms.vstring(
        'EmittanceScan2',
        'EmittanceScan3'
    ),
    PhysicsEmittanceScan2 = cms.vstring(
        'EmittanceScan4',
        'EmittanceScan5'
    ),
    PhysicsHLTPhysics0 = cms.vstring(
        'EphemeralHLTPhysics0',
        'EphemeralHLTPhysics1'
    ),
    PhysicsHLTPhysics1 = cms.vstring(
        'EphemeralHLTPhysics2',
        'EphemeralHLTPhysics3'
    ),
    PhysicsHLTPhysics2 = cms.vstring(
        'EphemeralHLTPhysics4',
        'EphemeralHLTPhysics5'
    ),
    PhysicsHLTPhysics3 = cms.vstring(
        'EphemeralHLTPhysics6',
        'EphemeralHLTPhysics7'
    ),
    PhysicsJetMET0 = cms.vstring('JetMET0'),
    PhysicsJetMET1 = cms.vstring('JetMET1'),
    PhysicsMuon0 = cms.vstring('Muon0'),
    PhysicsMuon1 = cms.vstring('Muon1'),
    PhysicsScoutingPFMonitor = cms.vstring('ScoutingPFMonitor'),
    PhysicsZeroBias0 = cms.vstring(
        'EphemeralZeroBias0',
        'EphemeralZeroBias1'
    ),
    PhysicsZeroBias1 = cms.vstring(
        'EphemeralZeroBias2',
        'EphemeralZeroBias3'
    ),
    PhysicsZeroBias2 = cms.vstring(
        'EphemeralZeroBias4',
        'EphemeralZeroBias5'
    ),
    PhysicsZeroBias3 = cms.vstring(
        'EphemeralZeroBias6',
        'EphemeralZeroBias7'
    ),
    RPCMON = cms.vstring('RPCMonitor'),
    ScoutingPF = cms.vstring('ScoutingPFRun3')
)

process.hltDoubletRecoveryClustersRefRemoval = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(16.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("hltSiPixelClusters"),
    stripClusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("hltIter0PFlowTrackSelectionHighPurity")
)


process.hltDoubletRecoveryMaskedMeasurementTrackerEvent = cms.EDProducer("MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag("hltDoubletRecoveryClustersRefRemoval"),
    phase2clustersToSkip = cms.InputTag(""),
    src = cms.InputTag("hltMeasurementTrackerEvent")
)


process.hltDoubletRecoveryPFlowCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltDoubletRecoveryMaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTIter2GroupedCkfTrajectoryBuilderIT')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterialParabolicMf'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialParabolicMfOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(False),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(False),
    maxNSeeds = cms.uint32(100000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltDoubletRecoveryPFlowPixelSeeds"),
    useHitsSplitting = cms.bool(False)
)


process.hltDoubletRecoveryPFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltDoubletRecovery'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltDoubletRecoveryMaskedMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    reMatchSplitHits = cms.bool(False),
    src = cms.InputTag("hltDoubletRecoveryPFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    usePropagatorForPCA = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltDoubletRecoveryPFlowPixelClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("hltMeasurementTrackerEvent"),
    DontCountDetsAboveNClusters = cms.uint32(0),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    MaxNumberOfStripClusters = cms.uint32(50000),
    PixelClusterCollectionLabel = cms.InputTag("hltSiPixelClusters"),
    cut = cms.string(''),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)


process.hltDoubletRecoveryPFlowPixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("hltDoubletRecoveryPFlowPixelClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    putEmptyIfMaxElementReached = cms.bool(False),
    seedingLayers = cms.InputTag(""),
    trackingRegions = cms.InputTag(""),
    trackingRegionsSeedingLayers = cms.InputTag("hltDoubletRecoveryPixelLayersAndRegions")
)


process.hltDoubletRecoveryPFlowPixelSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltDoubletRecoveryPFlowPixelHitDoublets")
)


process.hltDoubletRecoveryPFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.4, 0.4),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.3, 0.3)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.4, 0.4),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.35, 0.35)
        ),
        maxChi2 = cms.vdouble(9999.0, 25.0, 16.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 0.7),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltDoubletRecoveryPFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltDoubletRecoveryPFlowTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltDoubletRecoveryPFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltDoubletRecoveryPFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltDoubletRecoveryPFlowCtfWithMaterialTracks")
)


process.hltDoubletRecoveryPixelLayersAndRegions = cms.EDProducer("PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        skipClusters = cms.InputTag("hltDoubletRecoveryClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        skipClusters = cms.InputTag("hltDoubletRecoveryClustersRefRemoval"),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        extraEta = cms.double(0.0),
        extraPhi = cms.double(0.0),
        maxNVertices = cms.int32(3),
        measurementTrackerName = cms.InputTag("hltDoubletRecoveryMaskedMeasurementTrackerEvent"),
        nSigmaZBeamSpot = cms.double(4.0),
        nSigmaZVertex = cms.double(3.0),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(1.2),
        searchOpt = cms.bool(False),
        vertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
        whereToUseMeasurementTracker = cms.string('ForSiStrips'),
        zErrorBeamSpot = cms.double(15.0),
        zErrorVertex = cms.double(0.03)
    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("hltSiPixelDigiErrors"),
    createPlottingFiles = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    ignoreSingleFPixPanelModules = cms.bool(True),
    inactivePixelDetectorLabels = cms.VInputTag("hltSiPixelDigiErrors"),
    layerList = cms.vstring(
        'BPix1+BPix2',
        'BPix2+FPix1_pos',
        'BPix2+FPix1_neg',
        'FPix1_pos+FPix2_pos',
        'FPix1_neg+FPix2_neg',
        'BPix1+FPix2_neg',
        'BPix2+FPix2_neg',
        'FPix2_neg+FPix3_neg',
        'BPix2+BPix3'
    )
)


process.hltEcalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("hltEcalDigisLegacy"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("hltEcalDigisLegacy"),
    integrityBlockSizeErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("hltEcalDigisLegacy","EcalIntegrityTTIdErrors")
)


process.hltEcalDigis = cms.EDProducer("EcalDigisFromPortableProducer",
    digisInLabelEB = cms.InputTag("hltEcalDigisSoA","ebDigis"),
    digisInLabelEE = cms.InputTag("hltEcalDigisSoA","eeDigis"),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False)
)


process.hltEcalDigisLegacy = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35,
        36, 37, 38, 39, 40,
        41, 42, 43, 44, 45,
        46, 47, 48, 49, 50,
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)


process.hltEcalDigisSoA = cms.EDProducer("EcalRawToDigiPortable@alpaka",
    FEDs = cms.vint32(
        601, 602, 603, 604, 605,
        606, 607, 608, 609, 610,
        611, 612, 613, 614, 615,
        616, 617, 618, 619, 620,
        621, 622, 623, 624, 625,
        626, 627, 628, 629, 630,
        631, 632, 633, 634, 635,
        636, 637, 638, 639, 640,
        641, 642, 643, 644, 645,
        646, 647, 648, 649, 650,
        651, 652, 653, 654
    ),
    InputLabel = cms.InputTag("rawDataCollector"),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    digisLabelEB = cms.string('ebDigis'),
    digisLabelEE = cms.string('eeDigis'),
    maxChannelsEB = cms.uint32(61200),
    maxChannelsEE = cms.uint32(14648)
)


process.hltEcalPreshowerDigis = cms.EDProducer("ESRawToDigi",
    ESdigiCollection = cms.string(''),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    debugMode = cms.untracked.bool(False),
    sourceTag = cms.InputTag("rawDataCollector")
)


process.hltEcalPreshowerRecHit = cms.EDProducer("ESRecHitProducer",
    ESRecoAlgo = cms.int32(0),
    ESdigiCollection = cms.InputTag("hltEcalPreshowerDigis"),
    ESrechitCollection = cms.string('EcalRecHitsES'),
    algo = cms.string('ESRecHitWorker')
)


process.hltEcalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("hltEcalUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    bdtWeightFileCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_onlyCracks_ZskimData2017_v1.xml'),
    bdtWeightFileNoCracks = cms.FileInPath('RecoLocalCalo/EcalDeadChannelRecoveryAlgos/data/BDTWeights/bdtgAllRH_8GT700MeV_noCracks_ZskimData2017_v1.xml'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4.0),
        cThreshold_double = cms.double(10.0),
        cThreshold_endcap = cms.double(15.0),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.04),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(-0.024),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2.0),
        tightenCrack_e1_single = cms.double(2.0),
        tightenCrack_e4e1_single = cms.double(3.0),
        tightenCrack_e6e2_double = cms.double(3.0)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("hltEcalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk',
            'kDAC',
            'kNoLaser',
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0',
            'kNonRespondingIsolated',
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy',
            'kFixedG6',
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(-1.0),
    logWarningEtThreshold_EE_FE = cms.double(-1.0),
    recoverEBFE = cms.bool(False),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(False),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8.0),
    skipTimeCalib = cms.bool(False),
    sum8ChannelRecoveryThreshold = cms.double(0.0),
    timeCalibTag = cms.ESInputTag("",""),
    timeOffsetTag = cms.ESInputTag("",""),
    triggerPrimitiveDigiCollection = cms.InputTag("hltEcalDigisLegacy","EcalTriggerPrimitives")
)


process.hltEcalUncalibRecHit = cms.EDProducer("EcalUncalibRecHitSoAToLegacy",
    inputCollectionEB = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEB"),
    inputCollectionEE = cms.InputTag("hltEcalUncalibRecHitSoA","EcalUncalibRecHitsEE"),
    isPhase2 = cms.bool(False),
    outputLabelEB = cms.string('EcalUncalibRecHitsEB'),
    outputLabelEE = cms.string('EcalUncalibRecHitsEE')
)


process.hltEcalUncalibRecHitSoA = cms.EDProducer("EcalUncalibRecHitProducerPortable@alpaka",
    EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
    EBtimeConstantTerm = cms.double(0.6),
    EBtimeFitLimits_Lower = cms.double(0.2),
    EBtimeFitLimits_Upper = cms.double(1.4),
    EBtimeFitParameters = cms.vdouble(
        -2.015452, 3.130702, -12.3473, 41.88921, -82.83944,
        91.01147, -50.35761, 11.05621
    ),
    EBtimeNconst = cms.double(28.5),
    EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
    EEtimeConstantTerm = cms.double(1.0),
    EEtimeFitLimits_Lower = cms.double(0.2),
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeFitParameters = cms.vdouble(
        -2.390548, 3.553628, -17.62341, 67.67538, -133.213,
        140.7432, -75.41106, 16.20277
    ),
    EEtimeNconst = cms.double(31.8),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    amplitudeThresholdEB = cms.double(10.0),
    amplitudeThresholdEE = cms.double(10.0),
    digisLabelEB = cms.InputTag("hltEcalDigisSoA","ebDigis"),
    digisLabelEE = cms.InputTag("hltEcalDigisSoA","eeDigis"),
    kernelMinimizeThreads = cms.untracked.vuint32(32, 1, 1),
    outOfTimeThresholdGain12mEB = cms.double(1000.0),
    outOfTimeThresholdGain12mEE = cms.double(1000.0),
    outOfTimeThresholdGain12pEB = cms.double(1000.0),
    outOfTimeThresholdGain12pEE = cms.double(1000.0),
    outOfTimeThresholdGain61mEB = cms.double(1000.0),
    outOfTimeThresholdGain61mEE = cms.double(1000.0),
    outOfTimeThresholdGain61pEB = cms.double(1000.0),
    outOfTimeThresholdGain61pEE = cms.double(1000.0),
    recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelEE = cms.string('EcalUncalibRecHitsEE'),
    shouldRunTimingComputation = cms.bool(True)
)


process.hltEgammaCandidates = cms.EDProducer("EgammaHLTRecoEcalCandidateProducers",
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterECALL1Seeded","hltParticleFlowSuperClusterECALEndcapWithPreshower")
)


process.hltEgammaCandidatesUnseeded = cms.EDProducer("EgammaHLTRecoEcalCandidateProducers",
    recoEcalCandidateCollection = cms.string(''),
    scHybridBarrelProducer = cms.InputTag("hltParticleFlowSuperClusterECALUnseeded","hltParticleFlowSuperClusterECALBarrel"),
    scIslandEndcapProducer = cms.InputTag("hltParticleFlowSuperClusterECALUnseeded","hltParticleFlowSuperClusterECALEndcapWithPreshower")
)


process.hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('HLTPSetTrajectoryBuilderForGsfElectrons')
    ),
    TrajectoryCleaner = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag(""),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(1000000),
    maxSeedsBeforeCleaning = cms.uint32(1000),
    numHitsForSeedCleaner = cms.int32(4),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    phase2clustersToSkip = cms.InputTag(""),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("hltEgammaElectronPixelSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.hltEgammaClusterShape = cms.EDProducer("EgammaHLTClusterShapeProducer",
    ecalRechitEB = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE"),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaClusterShapeUnseeded = cms.EDProducer("EgammaHLTClusterShapeProducer",
    ecalRechitEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
    ecalRechitEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
    multThresEB = cms.double(1.0),
    multThresEE = cms.double(1.25),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)


process.hltEgammaEcalPFClusterIso = cms.EDProducer("EgammaHLTEcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducer = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0)
)


process.hltEgammaEcalPFClusterIsoDr0p2 = cms.EDProducer("EgammaHLTEcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.2),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.085, 0.0),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducer = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0)
)


process.hltEgammaEleGsfTrackIso = cms.EDProducer("EgammaHLTElectronTrackIsolationProducers",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    egTrkIsoConeSize = cms.double(0.2),
    egTrkIsoPtMin = cms.double(1.0),
    egTrkIsoRSpan = cms.double(999999.0),
    egTrkIsoStripBarrel = cms.double(0.01),
    egTrkIsoStripEndcap = cms.double(0.01),
    egTrkIsoVetoConeSizeBarrel = cms.double(0.03),
    egTrkIsoVetoConeSizeEndcap = cms.double(0.03),
    egTrkIsoZSpan = cms.double(0.15),
    electronProducer = cms.InputTag("hltEgammaGsfElectrons"),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    trackProducer = cms.InputTag("hltMergedTracks"),
    useGsfTrack = cms.bool(True),
    useSCRefs = cms.bool(True)
)


process.hltEgammaElectronPixelSeeds = cms.EDProducer("ElectronNHitSeedProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    initialSeeds = cms.InputTag("hltElePixelSeedsCombined"),
    matcherConfig = cms.PSet(
        detLayerGeom = cms.ESInputTag("","hltESPGlobalDetLayerGeometry"),
        matchingCuts = cms.VPSet(
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            )
        ),
        minNrHits = cms.vuint32(2, 3),
        minNrHitsValidLayerBins = cms.vint32(4),
        navSchool = cms.ESInputTag("","SimpleNavigationSchool"),
        paramMagField = cms.ESInputTag("","ParabolicMf"),
        useRecoVertex = cms.bool(False)
    ),
    measTkEvt = cms.InputTag("hltMeasurementTrackerEvent"),
    superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
    vertices = cms.InputTag("")
)


process.hltEgammaElectronPixelSeedsUnseeded = cms.EDProducer("ElectronNHitSeedProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    initialSeeds = cms.InputTag("hltElePixelSeedsCombinedUnseeded"),
    matcherConfig = cms.PSet(
        detLayerGeom = cms.ESInputTag("","hltESPGlobalDetLayerGeometry"),
        matchingCuts = cms.VPSet(
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.05),
                dPhiMaxHighEtThres = cms.vdouble(20.0),
                dPhiMaxLowEtGrad = cms.vdouble(-0.002),
                dRZMaxHighEt = cms.vdouble(9999.0),
                dRZMaxHighEtThres = cms.vdouble(0.0),
                dRZMaxLowEtGrad = cms.vdouble(0.0),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            ),
            cms.PSet(
                dPhiMaxHighEt = cms.vdouble(0.003),
                dPhiMaxHighEtThres = cms.vdouble(0.0),
                dPhiMaxLowEtGrad = cms.vdouble(0.0),
                dRZMaxHighEt = cms.vdouble(0.05),
                dRZMaxHighEtThres = cms.vdouble(30.0),
                dRZMaxLowEtGrad = cms.vdouble(-0.002),
                etaBins = cms.vdouble(),
                version = cms.int32(2)
            )
        ),
        minNrHits = cms.vuint32(2, 3),
        minNrHitsValidLayerBins = cms.vint32(4),
        navSchool = cms.ESInputTag("","SimpleNavigationSchool"),
        paramMagField = cms.ESInputTag("","ParabolicMf"),
        useRecoVertex = cms.bool(False)
    ),
    measTkEvt = cms.InputTag("hltMeasurementTrackerEvent"),
    superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatchUnseeded"),
    vertices = cms.InputTag("")
)


process.hltEgammaGsfElectrons = cms.EDProducer("EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag("hltOnlineBeamSpot"),
    GsfTrackProducer = cms.InputTag("hltEgammaGsfTracks"),
    TrackProducer = cms.InputTag(""),
    UseGsfTracks = cms.bool(True)
)


process.hltEgammaGsfTrackVars = cms.EDProducer("EgammaHLTGsfTrackVarProducer",
    beamSpotProducer = cms.InputTag("hltOnlineBeamSpot"),
    inputCollection = cms.InputTag("hltEgammaGsfTracks"),
    lowerTrackNrToRemoveCut = cms.int32(-1),
    produceAbsValues = cms.bool(False),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    upperTrackNrToRemoveCut = cms.int32(9999),
    useDefaultValuesForBarrel = cms.bool(True),
    useDefaultValuesForEndcap = cms.bool(False)
)


process.hltEgammaGsfTracks = cms.EDProducer("GsfTrackProducer",
    AlgorithmName = cms.string('gsf'),
    Fitter = cms.string('hltESPGsfElectronFittingSmoother'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string('hltESPMeasurementTracker'),
    MeasurementTrackerEvent = cms.InputTag("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('hltESPFwdElectronPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    reMatchSplitHits = cms.bool(False),
    src = cms.InputTag("hltEgammaCkfTrackCandidatesForGSF"),
    useHitsSplitting = cms.bool(False),
    usePropagatorForPCA = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.hltEgammaHcalPFClusterIso = cms.EDProducer("EgammaHLTHcalPFClusterIsolationProducer",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    doEffAreaCorrection = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    drMax = cms.double(0.3),
    drVetoBarrel = cms.double(0.0),
    drVetoEndcap = cms.double(0.0),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    effectiveAreasCorr = cms.vdouble(0.0, 0.0),
    effectiveAreasThres = cms.vdouble(0.0, 0.0),
    energyBarrel = cms.double(0.0),
    energyEndcap = cms.double(0.0),
    etaStripBarrel = cms.double(0.0),
    etaStripEndcap = cms.double(0.0),
    pfClusterProducerHCAL = cms.InputTag("hltParticleFlowClusterHCAL"),
    pfClusterProducerHFEM = cms.InputTag(""),
    pfClusterProducerHFHAD = cms.InputTag(""),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    useEt = cms.bool(True),
    useHF = cms.bool(False)
)


process.hltEgammaHoverE = cms.EDProducer("EgammaHLTHcalVarProducerFromRecHit",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    depth = cms.int32(0),
    doEtSum = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    effectiveAreas = cms.vdouble(0.105, 0.17),
    etThresHB = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    etThresHE = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    innerCone = cms.double(0.0),
    maxSeverityHB = cms.int32(9),
    maxSeverityHE = cms.int32(9),
    outerCone = cms.double(0.14),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    usePFThresholdsFromDB = cms.bool(True),
    useSingleTower = cms.bool(False)
)


process.hltEgammaHoverEUnseeded = cms.EDProducer("EgammaHLTHcalVarProducerFromRecHit",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    depth = cms.int32(0),
    doEtSum = cms.bool(False),
    doRhoCorrection = cms.bool(False),
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    effectiveAreas = cms.vdouble(0.105, 0.17),
    etThresHB = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    etThresHE = cms.vdouble(
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    innerCone = cms.double(0.0),
    maxSeverityHB = cms.int32(9),
    maxSeverityHE = cms.int32(9),
    outerCone = cms.double(0.14),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded"),
    rhoMax = cms.double(99999999.0),
    rhoProducer = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    rhoScale = cms.double(1.0),
    usePFThresholdsFromDB = cms.bool(True),
    useSingleTower = cms.bool(False)
)


process.hltEgammaPixelMatchVars = cms.EDProducer("EgammaHLTPixelMatchVarProducer",
    dPhi1SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00112, 0.000752, -0.00122, 0.00109),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00222, 0.000196, -0.000203, 0.000447),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00236, 0.000691, 0.000199, 0.000416),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00823, -0.0029),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00282),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.010838, -0.00345),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0043),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0208, -0.0125, 0.00231),
                funcType = cms.string('TF1:=pol2'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            )
        )
    ),
    dPhi2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00013),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(1.6),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00045, -0.000199),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(1.9),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(7.94e-05),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.9),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    dRZ2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00299, 0.000299, -4.13e-06, 0.00191),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.248, -0.329, 0.148, -0.0222),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    pixelSeedsProducer = cms.InputTag("hltEgammaElectronPixelSeeds"),
    productsToWrite = cms.int32(0),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidates")
)


process.hltEgammaPixelMatchVarsUnseeded = cms.EDProducer("EgammaHLTPixelMatchVarProducer",
    dPhi1SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00112, 0.000752, -0.00122, 0.00109),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00222, 0.000196, -0.000203, 0.000447),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00236, 0.000691, 0.000199, 0.000416),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00823, -0.0029),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00282),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(1),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.010838, -0.00345),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(2.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0043),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(2.0),
                yMax = cms.int32(2),
                yMin = cms.int32(2)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.0208, -0.0125, 0.00231),
                funcType = cms.string('TF1:=pol2'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(3)
            )
        )
    ),
    dPhi2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00013),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(1.6),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00045, -0.000199),
                funcType = cms.string('TF1:=pol1'),
                xMax = cms.double(1.9),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(7.94e-05),
                funcType = cms.string('TF1:=pol0'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.9),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    dRZ2SParams = cms.PSet(
        bins = cms.VPSet(
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.00299, 0.000299, -4.13e-06, 0.00191),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(1.5),
                xMin = cms.double(0.0),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            ),
            cms.PSet(
                binType = cms.string('AbsEtaClus'),
                funcParams = cms.vdouble(0.248, -0.329, 0.148, -0.0222),
                funcType = cms.string('TF1:=pol3'),
                xMax = cms.double(3.0),
                xMin = cms.double(1.5),
                yMax = cms.int32(99999),
                yMin = cms.int32(1)
            )
        )
    ),
    pixelSeedsProducer = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded"),
    productsToWrite = cms.int32(0),
    recoEcalCandidateProducer = cms.InputTag("hltEgammaCandidatesUnseeded")
)


process.hltEgammaSuperClustersToPixelMatch = cms.EDProducer("EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag("hltEgammaCandidates"),
    cuts = cms.VPSet(cms.PSet(
        barrelCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        endcapCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        var = cms.InputTag("hltEgammaHoverE")
    )),
    minEtCutEB = cms.double(0.0),
    minEtCutEE = cms.double(0.0)
)


process.hltEgammaSuperClustersToPixelMatchUnseeded = cms.EDProducer("EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag("hltEgammaCandidatesUnseeded"),
    cuts = cms.VPSet(cms.PSet(
        barrelCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        endcapCut = cms.PSet(
            cutOverE = cms.double(0.2),
            useEt = cms.bool(False)
        ),
        var = cms.InputTag("hltEgammaHoverEUnseeded")
    )),
    minEtCutEB = cms.double(0.0),
    minEtCutEE = cms.double(0.0)
)


process.hltElePixelHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    putEmptyIfMaxElementReached = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsForTriplets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    putEmptyIfMaxElementReached = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsForTripletsUnseeded = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    putEmptyIfMaxElementReached = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerTriplets"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegionsUnseeded"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitDoubletsUnseeded = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag(""),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(0),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(True),
    putEmptyIfMaxElementReached = cms.bool(False),
    seedingLayers = cms.InputTag("hltPixelLayerPairs"),
    trackingRegions = cms.InputTag("hltEleSeedsTrackingRegionsUnseeded"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.hltElePixelHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.004),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltElePixelHitDoubletsForTriplets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltElePixelHitTripletsUnseeded = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.1),
    CAPhiCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    CAThetaCut = cms.double(0.004),
    CAThetaCut_byTriplets = cms.VPSet(cms.PSet(
        cut = cms.double(-1.0),
        seedingLayers = cms.string('')
    )),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("hltElePixelHitDoubletsForTripletsUnseeded"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8.0),
        value1 = cms.double(100.0),
        value2 = cms.double(6.0)
    ),
    useBendingCorrection = cms.bool(True)
)


process.hltElePixelSeedsCombined = cms.EDProducer("SeedCombiner",
    clusterRemovalInfos = cms.VInputTag(),
    seedCollections = cms.VInputTag("hltElePixelSeedsDoublets", "hltElePixelSeedsTriplets")
)


process.hltElePixelSeedsCombinedUnseeded = cms.EDProducer("SeedCombiner",
    clusterRemovalInfos = cms.VInputTag(),
    seedCollections = cms.VInputTag("hltElePixelSeedsDoubletsUnseeded", "hltElePixelSeedsTripletsUnseeded")
)


process.hltElePixelSeedsDoublets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitDoublets")
)


process.hltElePixelSeedsDoubletsUnseeded = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitDoubletsUnseeded")
)


process.hltElePixelSeedsTriplets = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTriplets")
)


process.hltElePixelSeedsTripletsUnseeded = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("hltElePixelHitTripletsUnseeded")
)


process.hltEleSeedsTrackingRegions = cms.EDProducer("TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        defaultZ = cms.double(0.0),
        deltaEtaRegion = cms.double(0.1),
        deltaPhiRegion = cms.double(0.4),
        measurementTrackerEvent = cms.InputTag(""),
        minBSDeltaZ = cms.double(0.0),
        nrSigmaForBSDeltaZ = cms.double(4.0),
        originHalfLength = cms.double(12.5),
        originRadius = cms.double(0.05),
        precise = cms.bool(True),
        ptMin = cms.double(1.5),
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatch"),
        useZInBeamspot = cms.bool(False),
        useZInVertex = cms.bool(False),
        vertices = cms.InputTag(""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)


process.hltEleSeedsTrackingRegionsUnseeded = cms.EDProducer("TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("hltOnlineBeamSpot"),
        defaultZ = cms.double(0.0),
        deltaEtaRegion = cms.double(0.1),
        deltaPhiRegion = cms.double(0.4),
        measurementTrackerEvent = cms.InputTag(""),
        minBSDeltaZ = cms.double(0.0),
        nrSigmaForBSDeltaZ = cms.double(4.0),
        originHalfLength = cms.double(12.5),
        originRadius = cms.double(0.05),
        precise = cms.bool(True),
        ptMin = cms.double(1.5),
        superClusters = cms.VInputTag("hltEgammaSuperClustersToPixelMatchUnseeded"),
        useZInBeamspot = cms.bool(False),
        useZInVertex = cms.bool(False),
        vertices = cms.InputTag(""),
        whereToUseMeasTracker = cms.string('kNever')
    )
)


process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer("FixedGridRhoProducerFastjetFromRecHit",
    eThresHB = cms.vdouble(0.4, 0.3, 0.3, 0.3),
    eThresHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    ),
    ebRecHitsTag = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
    eeRecHitsTag = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
    gridSpacing = cms.double(0.55),
    hbheRecHitsTag = cms.InputTag("hltHbhereco"),
    maxRapidity = cms.double(2.5),
    skipECAL = cms.bool(False),
    skipHCAL = cms.bool(False),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataCollector"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)


process.hltGtStage2ObjectMap = cms.EDProducer("L1TGlobalProducer",
    AlgoBlkInputTag = cms.InputTag("hltGtStage2Digis"),
    AlgorithmTriggersUnmasked = cms.bool(True),
    AlgorithmTriggersUnprescaled = cms.bool(True),
    AlternativeNrBxBoardDaq = cms.uint32(0),
    BstLengthBytes = cms.int32(-1),
    CICADAInputTag = cms.InputTag("hltGtStage2Digis","CICADAScore"),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    EmulateBxInEvent = cms.int32(1),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    EtSumZdcInputTag = cms.InputTag("hltGtStage2Digis","EtSumZDC"),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    GetPrescaleColumnFromData = cms.bool(False),
    JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1DataBxInEvent = cms.int32(5),
    MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    PrescaleSet = cms.uint32(1),
    PrintL1Menu = cms.untracked.bool(False),
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    TriggerMenuLuminosity = cms.string('startup'),
    Verbosity = cms.untracked.int32(0),
    produceAXOL1TLScore = cms.bool(False),
    resetPSCountersEachLumiSec = cms.bool(True),
    semiRandomInitialPSCounters = cms.bool(False),
    useMuonShowers = cms.bool(True)
)


process.hltHbheRecoSoA = cms.EDProducer("HBHERecHitProducerPortable@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    applyTimeSlew = cms.bool(True),
    digisLabelF01HE = cms.InputTag("hltHcalDigisSoA","f01HEDigis"),
    digisLabelF3HB = cms.InputTag("hltHcalDigisSoA","f3HBDigis"),
    digisLabelF5HB = cms.InputTag("hltHcalDigisSoA","f5HBDigis"),
    firstSampleShift = cms.int32(0),
    kernelMinimizeThreads = cms.vuint32(16, 1, 1),
    kprep1dChannelsPerBlock = cms.uint32(32),
    maxTimeSamples = cms.uint32(10),
    meanTime = cms.double(0.0),
    pulseOffsets = cms.vint32(
        -3, -2, -1, 0, 1,
        2, 3, 4
    ),
    recHitsLabelM0HBHE = cms.string(''),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    slopeTimeSlewParameters = cms.vdouble(-3.178648, -1.5610227, -1.075824),
    timeSigmaHPD = cms.double(5.0),
    timeSigmaSiPM = cms.double(2.5),
    tmaxTimeSlewParameters = cms.vdouble(16.0, 10.0, 6.25),
    ts4Thresh = cms.double(0.0),
    tzeroTimeSlewParameters = cms.vdouble(23.960177, 11.977461, 9.109694),
    useEffectivePedestals = cms.bool(True)
)


process.hltHbhereco = cms.EDProducer("HcalRecHitSoAToLegacy",
    src = cms.InputTag("hltHbheRecoSoA")
)


process.hltHcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(False),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)


process.hltHcalDigisSoA = cms.EDProducer("HcalDigisSoAProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    digisLabelF01HE = cms.string('f01HEDigis'),
    digisLabelF3HB = cms.string('f3HBDigis'),
    digisLabelF5HB = cms.string('f5HBDigis'),
    hbheDigisLabel = cms.InputTag("hltHcalDigis"),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    qie11DigiLabel = cms.InputTag("hltHcalDigis")
)


process.hltHfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hltHcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)


process.hltHfreco = cms.EDProducer("HFPhase1Reconstructor",
    HFStripFilter = cms.PSet(
        gap = cms.int32(2),
        lstrips = cms.int32(2),
        maxStripTime = cms.double(10.0),
        maxThreshold = cms.double(100.0),
        seedHitIetaMax = cms.int32(35),
        stripThreshold = cms.double(40.0),
        timeMax = cms.double(6.0),
        verboseLevel = cms.untracked.int32(10),
        wedgeCut = cms.double(0.05)
    ),
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            40.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0, 100.0, 100.0,
            100.0, 100.0, 100.0
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82,
            58.7, 63.0, 67.72, 72.86, 78.42,
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317,
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132,
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296,
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422,
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            2.0, 0.0, 1.0, 0.0, 0.0,
            1.0, 0.0, 1.0, 0.0, 2.0,
            0.0, 2.0, 0.0, 2.0, 0.0,
            1.0
        ),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(False),
    inputLabel = cms.InputTag("hltHfprereco"),
    runHFStripFilter = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(False)
)


process.hltHoreco = cms.EDProducer("HcalHitReconstructor",
    HFInWindowStat = cms.PSet(

    ),
    PETstat = cms.PSet(

    ),
    S8S1stat = cms.PSet(

    ),
    S9S1stat = cms.PSet(

    ),
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(False),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hltHcalDigis"),
    digiTimeFromDB = cms.bool(True),
    digistat = cms.PSet(

    ),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    hfTimingTrustParameters = cms.PSet(

    ),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(False),
    setSaturationFlags = cms.bool(False),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)


process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag("hltPixelTracks"),
    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
    SeedCreatorPSet = cms.PSet(
        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
    ),
    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
    includeFourthHit = cms.bool(True),
    originHalfLength = cms.double(0.3),
    originRadius = cms.double(0.1),
    produceComplement = cms.bool(False),
    useEventsWithNoVertex = cms.bool(True),
    usePV = cms.bool(False),
    useProtoTrackKinematics = cms.bool(False)
)


process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer("MkFitOutputConverter",
    batchSize = cms.int32(16),
    candMVASel = cms.bool(False),
    candWP = cms.double(0.0),
    doErrorRescale = cms.bool(True),
    mkFitEventOfHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits"),
    mkFitPixelHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits"),
    mkFitSeeds = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSeeds"),
    mkFitStripHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits"),
    propagatorAlong = cms.ESInputTag("","PropagatorWithMaterialParabolicMf"),
    propagatorOpposite = cms.ESInputTag("","PropagatorWithMaterialParabolicMfOpposite"),
    qualityMaxInvPt = cms.double(100.0),
    qualityMaxPosErr = cms.double(100.0),
    qualityMaxR = cms.double(120.0),
    qualityMaxZ = cms.double(280.0),
    qualityMinTheta = cms.double(0.01),
    qualitySignPt = cms.bool(True),
    seeds = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    tfDnnLabel = cms.string('trackSelectionTf'),
    tracks = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFit"),
    ttrhBuilder = cms.ESInputTag("","hltESPTTRHBWithTrackAngle")
)


process.hltIter0PFlowCkfTrackCandidatesMkFit = cms.EDProducer("MkFitProducer",
    backwardFitInCMSSW = cms.bool(False),
    buildingRoutine = cms.string('cloneEngine'),
    clustersToSkip = cms.InputTag(""),
    config = cms.ESInputTag("","hltESPIter0PFlowTrackCandidatesMkFitConfig"),
    eventOfHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits"),
    limitConcurrency = cms.untracked.bool(False),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    mkFitSilent = cms.untracked.bool(True),
    pixelHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits"),
    removeDuplicates = cms.bool(True),
    seedCleaning = cms.bool(True),
    seeds = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSeeds"),
    stripHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits")
)


process.hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits = cms.EDProducer("MkFitEventOfHitsProducer",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    pixelHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits"),
    stripHits = cms.InputTag("hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits"),
    usePixelQualityDB = cms.bool(True),
    useStripStripQualityDB = cms.bool(True)
)


process.hltIter0PFlowCkfTrackCandidatesMkFitSeeds = cms.EDProducer("MkFitSeedConverter",
    maxNSeeds = cms.uint32(500000),
    seeds = cms.InputTag("hltIter0PFLowPixelSeedsFromPixelTracks"),
    ttrhBuilder = cms.ESInputTag("","hltESPTTRHBWithTrackAngle")
)


process.hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits = cms.EDProducer("MkFitSiPixelHitConverter",
    clusters = cms.InputTag("hltSiPixelClusters"),
    hits = cms.InputTag("hltSiPixelRecHits"),
    ttrhBuilder = cms.ESInputTag("","hltESPTTRHBWithTrackAngle")
)


process.hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits = cms.EDProducer("MkFitSiStripHitConverter",
    clusters = cms.InputTag("hltSiStripRawToClustersFacility"),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    rphiHits = cms.InputTag("hltSiStripRecHits","rphiRecHit"),
    stereoHits = cms.InputTag("hltSiStripRecHits","stereoRecHit"),
    ttrhBuilder = cms.ESInputTag("","hltESPTTRHBWithTrackAngle")
)


process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('hltIter0'),
    Fitter = cms.string('hltESPFittingSmootherIT'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("hltMeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    reMatchSplitHits = cms.bool(False),
    src = cms.InputTag("hltIter0PFlowCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    usePropagatorForPCA = cms.bool(False),
    useSimpleMF = cms.bool(True)
)


process.hltIter0PFlowTrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("hltOnlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            dr_exp = cms.vint32(4, 4, 4),
            dr_par1 = cms.vdouble(3.40282346639e+38, 0.6, 0.6),
            dr_par2 = cms.vdouble(3.40282346639e+38, 0.45, 0.45)
        ),
        dz_par = cms.PSet(
            dz_exp = cms.vint32(4, 4, 4),
            dz_par1 = cms.vdouble(3.40282346639e+38, 0.6, 0.6),
            dz_par2 = cms.vdouble(3.40282346639e+38, 0.51, 0.51)
        ),
        maxChi2 = cms.vdouble(999.0, 25.0, 99.0),
        maxChi2n = cms.vdouble(1.2, 1.0, 999.0),
        maxDr = cms.vdouble(0.5, 0.03, 3.40282346639e+38),
        maxDz = cms.vdouble(0.5, 0.2, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24.0, 15.0),
        maxLostLayers = cms.vint32(1, 1, 1),
        min3DLayers = cms.vint32(0, 0, 0),
        minLayers = cms.vint32(3, 3, 3),
        minNVtxTrk = cms.int32(3),
        minNdof = cms.vdouble(1e-05, 1e-05, 1e-05),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks"),
    vertices = cms.InputTag("hltTrimmedPixelVertices")
)


process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer("TrackCollectionFilterCloner",
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    minQuality = cms.string('highPurity'),
    originalMVAVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","MVAValues"),
    originalQualVals = cms.InputTag("hltIter0PFlowTrackCutClassifier","QualityMasks"),
    originalSource = cms.InputTag("hltIter0PFlowCtfWithMaterialTracks")
)


process.hltMeasurementTrackerEvent = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("hltSiPixelDigiErrors"),
    inactivePixelDetectorLabels = cms.VInputTag("hltSiPixelDigiErrors"),
    inactiveStripDetectorLabels = cms.VInputTag("hltSiStripExcludedFEDListProducer"),
    measurementTracker = cms.string('hltESPMeasurementTracker'),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('hltSiPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('hltSiStripRawToClustersFacility'),
    switchOffPixelsIfEmpty = cms.bool(True),
    vectorHits = cms.InputTag(""),
    vectorHitsRej = cms.InputTag("")
)


process.hltMergedTracks = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(20.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltDoubletRecoveryPFlowTrackSelectionHighPurity"),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(False),
    hasSelector = cms.vint32(0, 0),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag("hltIter0PFlowTrackSelectionHighPurity", "hltDoubletRecoveryPFlowTrackSelectionHighPurity"),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(False),
        tLists = cms.vint32(0, 1)
    )),
    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.hltOnlineBeamSpot = cms.EDProducer("BeamSpotOnlineProducer",
    beamMode = cms.untracked.uint32(11),
    changeToCMSCoordinates = cms.bool(False),
    gtEvmLabel = cms.InputTag(""),
    maxRadius = cms.double(2.0),
    maxZ = cms.double(40.0),
    setSigmaZ = cms.double(0.0),
    sigmaXYThreshold = cms.double(4.0),
    sigmaZThreshold = cms.double(2.0),
    src = cms.InputTag(""),
    timeThreshold = cms.int32(48),
    useBSOnlineRecords = cms.bool(True)
)


process.hltOnlineBeamSpotDevice = cms.EDProducer("BeamSpotDeviceProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    src = cms.InputTag("hltOnlineBeamSpot")
)


process.hltOnlineMetaDataDigis = cms.EDProducer("OnlineMetaDataRawToDigi",
    onlineMetaDataInputLabel = cms.InputTag("rawDataCollector")
)


process.hltPSetMap = cms.EDProducer("ParameterSetBlobProducer")


process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        ebSrFlagLabel = cms.InputTag("hltEcalDigisLegacy"),
        eeSrFlagLabel = cms.InputTag("hltEcalDigisLegacy"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedL1Seeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSL1Seeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    ),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                gatheringThreshold = cms.double(0.08),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                gatheringThreshold = cms.double(0.3),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(True)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(0.08),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(9),
            timeResolutionCalcBarrel = cms.PSet(
                constantTerm = cms.double(0.428192),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0510871),
                noiseTerm = cms.double(1.10889),
                noiseTermLowE = cms.double(1.31883),
                threshHighE = cms.double(5.0),
                threshLowE = cms.double(0.5)
            ),
            timeResolutionCalcEndcap = cms.PSet(
                constantTerm = cms.double(0.0),
                constantTermLowE = cms.double(0.0),
                corrTermLowE = cms.double(0.0),
                noiseTerm = cms.double(5.72489999999),
                noiseTermLowE = cms.double(6.92683000001),
                threshHighE = cms.double(10.0),
                threshLowE = cms.double(1.0)
            )
        ),
        positionCalcForConvergence = cms.PSet(
            T0_EB = cms.double(7.4),
            T0_EE = cms.double(3.1),
            T0_ES = cms.double(1.2),
            W0 = cms.double(4.2),
            X0 = cms.double(0.89),
            algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
            minAllowedNormalization = cms.double(0.0),
            minFractionInCalc = cms.double(0.0)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                recHitEnergyNorm = cms.double(0.08)
            ),
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                recHitEnergyNorm = cms.double(0.3)
            )
        ),
        showerSigma = cms.double(1.5),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(
        T0_EB = cms.double(7.4),
        T0_EE = cms.double(3.1),
        T0_ES = cms.double(1.2),
        W0 = cms.double(4.2),
        X0 = cms.double(0.89),
        algoName = cms.string('ECAL2DPositionCalcWithDepthCorr'),
        minAllowedNormalization = cms.double(0.0),
        minFractionInCalc = cms.double(0.0)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitECALUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('ECAL_ENDCAP'),
                seedingThreshold = cms.double(0.6),
                seedingThresholdPt = cms.double(0.15)
            ),
            cms.PSet(
                detector = cms.string('ECAL_BARREL'),
                seedingThreshold = cms.double(0.23),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    ),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowClusterECALUnseeded = cms.EDProducer("CorrectedECALPFClusterProducer",
    energyCorrector = cms.PSet(
        applyCrackCorrections = cms.bool(False),
        applyMVACorrections = cms.bool(True),
        ebSrFlagLabel = cms.InputTag("hltEcalDigisLegacy"),
        eeSrFlagLabel = cms.InputTag("hltEcalDigisLegacy"),
        maxPtForMVAEvaluation = cms.double(300.0),
        recHitsEBLabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        recHitsEELabel = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        srfAwareCorrection = cms.bool(True)
    ),
    inputECAL = cms.InputTag("hltParticleFlowClusterECALUncorrectedUnseeded"),
    inputPS = cms.InputTag("hltParticleFlowClusterPSUnseeded"),
    minimumPSEnergy = cms.double(0.0),
    skipPS = cms.bool(False)
)


process.hltParticleFlowClusterHBHE = cms.EDProducer("LegacyPFClusterProducer",
    PFRecHitsLabelIn = cms.InputTag("hltParticleFlowRecHitHBHESoA"),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        clusterTimeResFromSeed = cms.bool(False),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(5),
        maxNSigmaTime = cms.double(10.0),
        minChi2Prob = cms.double(0.0),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(5)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                depths = cms.vint32(1, 2, 3, 4),
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.4, 0.3, 0.3, 0.3)
            ),
            cms.PSet(
                depths = cms.vint32(
                    1, 2, 3, 4, 5,
                    6, 7
                ),
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeSigmaEB = cms.double(10.0),
        timeSigmaEE = cms.double(10.0)
    ),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitHBHE"),
    src = cms.InputTag("hltParticleFlowClusterHBHESoA"),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowClusterHBHESoA = cms.EDProducer("PFClusterSoAProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    initialClusteringStep = cms.PSet(
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                gatheringThreshold = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                gatheringThreshold = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        )
    ),
    pfClusterBuilder = cms.PSet(
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(5),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                recHitEnergyNorm = cms.vdouble(0.1, 0.2, 0.3, 0.3)
            ),
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                recHitEnergyNorm = cms.vdouble(
                    0.1, 0.2, 0.2, 0.2, 0.2,
                    0.2, 0.2
                )
            )
        ),
        showerSigma = cms.double(10.0),
        stoppingTolerance = cms.double(1e-08),
        timeResolutionCalcBarrel = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        ),
        timeResolutionCalcEndcap = cms.PSet(
            constantTerm = cms.double(2.82),
            constantTermLowE = cms.double(4.24),
            corrTermLowE = cms.double(0.0),
            noiseTerm = cms.double(21.86),
            noiseTermLowE = cms.double(8.0),
            threshHighE = cms.double(15.0),
            threshLowE = cms.double(6.0)
        )
    ),
    pfRecHits = cms.InputTag("hltParticleFlowRecHitHBHESoA"),
    seedFinder = cms.PSet(
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('HCAL_BARREL1'),
                seedingThreshold = cms.vdouble(0.125, 0.25, 0.35, 0.35),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('HCAL_ENDCAP'),
                seedingThreshold = cms.vdouble(
                    0.1375, 0.275, 0.275, 0.275, 0.275,
                    0.275, 0.275
                ),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    ),
    synchronise = cms.bool(False),
    topology = cms.ESInputTag("hltESPPFRecHitHCALTopology","")
)


process.hltParticleFlowClusterHCAL = cms.EDProducer("PFMultiDepthClusterProducer",
    clustersSource = cms.InputTag("hltParticleFlowClusterHBHE"),
    energyCorrector = cms.PSet(

    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('PFMultiDepthClusterizer'),
        allCellsPositionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominatorByDetector = cms.VPSet(
                cms.PSet(
                    depths = cms.vint32(1, 2, 3, 4),
                    detector = cms.string('HCAL_BARREL1'),
                    logWeightDenominator = cms.vdouble(0.4, 0.3, 0.3, 0.3)
                ),
                cms.PSet(
                    depths = cms.vint32(
                        1, 2, 3, 4, 5,
                        6, 7
                    ),
                    detector = cms.string('HCAL_ENDCAP'),
                    logWeightDenominator = cms.vdouble(
                        0.1, 0.2, 0.2, 0.2, 0.2,
                        0.2, 0.2
                    )
                )
            ),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        minFractionToKeep = cms.double(1e-07),
        nSigmaEta = cms.double(2.0),
        nSigmaPhi = cms.double(2.0)
    ),
    positionReCalc = cms.PSet(

    ),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSL1Seeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    ),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowClusterPSUnseeded = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('Basic2DGenericTopoClusterizer'),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                gatheringThreshold = cms.double(6e-05),
                gatheringThresholdPt = cms.double(0.0)
            )
        ),
        useCornerCells = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowClusterizer'),
        excludeOtherSeeds = cms.bool(True),
        maxIterations = cms.uint32(50),
        minFracTot = cms.double(1e-20),
        minFractionToKeep = cms.double(1e-07),
        positionCalc = cms.PSet(
            algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
            logWeightDenominator = cms.double(6e-05),
            minAllowedNormalization = cms.double(1e-09),
            minFractionInCalc = cms.double(1e-09),
            posCalcNCrystals = cms.int32(-1)
        ),
        recHitEnergyNorms = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                recHitEnergyNorm = cms.double(6e-05)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                recHitEnergyNorm = cms.double(6e-05)
            )
        ),
        showerSigma = cms.double(0.3),
        stoppingTolerance = cms.double(1e-08)
    ),
    positionReCalc = cms.PSet(

    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("hltParticleFlowRecHitPSUnseeded"),
    seedCleaners = cms.VPSet(),
    seedFinder = cms.PSet(
        algoName = cms.string('LocalMaximumSeedFinder'),
        nNeighbours = cms.int32(4),
        thresholdsByDetector = cms.VPSet(
            cms.PSet(
                detector = cms.string('PS1'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            ),
            cms.PSet(
                detector = cms.string('PS2'),
                seedingThreshold = cms.double(0.00012),
                seedingThresholdPt = cms.double(0.0)
            )
        )
    ),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltRechitInRegionsECAL","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        barrel = cms.PSet(

        ),
        endcap = cms.PSet(

        ),
        name = cms.string('PFRecHitECALNavigator')
    ),
    producers = cms.VPSet(
        cms.PSet(
            name = cms.string('PFEBRecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")
        ),
        cms.PSet(
            name = cms.string('PFEERecHitCreator'),
            qualityTests = cms.VPSet(
                cms.PSet(
                    applySelectionsToAllCrystals = cms.bool(True),
                    name = cms.string('PFRecHitQTestDBThreshold')
                ),
                cms.PSet(
                    cleaningThreshold = cms.double(2.0),
                    name = cms.string('PFRecHitQTestECAL'),
                    skipTTRecoveredHits = cms.bool(True),
                    timingCleaning = cms.bool(True),
                    topologicalCleaning = cms.bool(True)
                )
            ),
            srFlags = cms.InputTag(""),
            src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")
        )
    )
)


process.hltParticleFlowRecHitHBHE = cms.EDProducer("LegacyPFRecHitProducer",
    src = cms.InputTag("hltParticleFlowRecHitHBHESoA")
)


process.hltParticleFlowRecHitHBHESoA = cms.EDProducer("PFRecHitSoAProducerHCAL@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    producers = cms.VPSet(cms.PSet(
        params = cms.ESInputTag("hltESPPFRecHitHCALParams",""),
        src = cms.InputTag("hltHbheRecoSoA")
    )),
    synchronise = cms.untracked.bool(False),
    topology = cms.ESInputTag("hltESPPFRecHitHCALTopology","")
)


process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltRechitInRegionsES","EcalRecHitsES")
    ))
)


process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer("PFRecHitProducer",
    navigator = cms.PSet(
        name = cms.string('PFRecHitPreshowerNavigator')
    ),
    producers = cms.VPSet(cms.PSet(
        name = cms.string('PFPSRecHitCreator'),
        qualityTests = cms.VPSet(cms.PSet(
            name = cms.string('PFRecHitQTestThreshold'),
            threshold = cms.double(7e-06)
        )),
        src = cms.InputTag("hltEcalPreshowerRecHit","EcalRecHitsES")
    ))
)


process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('hltParticleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('hltParticleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('hltParticleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("hltParticleFlowClusterECALL1Seeded"),
    PFSuperClusterCollectionBarrel = cms.string('hltParticleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('hltParticleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('hltParticleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag(""),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag(""),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        isHLT = cms.bool(True),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.5),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.hltParticleFlowSuperClusterECALUnseeded = cms.EDProducer("PFECALSuperClusterProducer",
    BeamSpot = cms.InputTag("hltOnlineBeamSpot"),
    ClusteringType = cms.string('Mustache'),
    ESAssociation = cms.InputTag("hltParticleFlowClusterECALUnseeded"),
    EnergyWeight = cms.string('Raw'),
    PFBasicClusterCollectionBarrel = cms.string('hltParticleFlowBasicClusterECALBarrel'),
    PFBasicClusterCollectionEndcap = cms.string('hltParticleFlowBasicClusterECALEndcap'),
    PFBasicClusterCollectionPreshower = cms.string('hltParticleFlowBasicClusterECALPreshower'),
    PFClusters = cms.InputTag("hltParticleFlowClusterECALUnseeded"),
    PFSuperClusterCollectionBarrel = cms.string('hltParticleFlowSuperClusterECALBarrel'),
    PFSuperClusterCollectionEndcap = cms.string('hltParticleFlowSuperClusterECALEndcap'),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string('hltParticleFlowSuperClusterECALEndcapWithPreshower'),
    applyCrackCorrections = cms.bool(False),
    barrelRecHits = cms.InputTag(""),
    doSatelliteClusterMerge = cms.bool(False),
    dropUnseedable = cms.bool(False),
    endcapRecHits = cms.InputTag(""),
    etawidth_SuperClusterBarrel = cms.double(0.04),
    etawidth_SuperClusterEndcap = cms.double(0.04),
    isOOTCollection = cms.bool(False),
    phiwidth_SuperClusterBarrel = cms.double(0.6),
    phiwidth_SuperClusterEndcap = cms.double(0.6),
    regressionConfig = cms.PSet(
        ecalRecHitsEB = cms.InputTag("hltEcalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("hltEcalRecHit","EcalRecHitsEE"),
        isHLT = cms.bool(True),
        regTrainedWithPS = cms.bool(True),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_online'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_online'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_online'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_online')
    ),
    satelliteClusterSeedThreshold = cms.double(50.0),
    satelliteMajorityFraction = cms.double(0.5),
    seedThresholdIsET = cms.bool(True),
    thresh_PFClusterBarrel = cms.double(0.5),
    thresh_PFClusterES = cms.double(0.5),
    thresh_PFClusterEndcap = cms.double(0.5),
    thresh_PFClusterSeedBarrel = cms.double(1.0),
    thresh_PFClusterSeedEndcap = cms.double(1.0),
    thresh_SCEt = cms.double(4.0),
    useDynamicDPhiWindow = cms.bool(True),
    useRegression = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.hltPixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2',
        'BPix1+BPix3',
        'BPix1+BPix4',
        'BPix2+BPix3',
        'BPix2+BPix4',
        'BPix3+BPix4',
        'FPix1_pos+FPix2_pos',
        'FPix1_pos+FPix3_pos',
        'FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos',
        'BPix1+FPix2_pos',
        'BPix1+FPix3_pos',
        'BPix2+FPix1_pos',
        'BPix2+FPix2_pos',
        'BPix2+FPix3_pos',
        'BPix3+FPix1_pos',
        'BPix3+FPix2_pos',
        'BPix3+FPix3_pos',
        'BPix4+FPix1_pos',
        'BPix4+FPix2_pos',
        'BPix4+FPix3_pos',
        'FPix1_neg+FPix2_neg',
        'FPix1_neg+FPix3_neg',
        'FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg',
        'BPix1+FPix2_neg',
        'BPix1+FPix3_neg',
        'BPix2+FPix1_neg',
        'BPix2+FPix2_neg',
        'BPix2+FPix3_neg',
        'BPix3+FPix1_neg',
        'BPix3+FPix2_neg',
        'BPix3+FPix3_neg',
        'BPix4+FPix1_neg',
        'BPix4+FPix2_neg',
        'BPix4+FPix3_neg'
    )
)


process.hltPixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('hltSiPixelRecHits'),
        TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+BPix3+FPix1_pos',
        'BPix1+BPix2+FPix2_pos',
        'BPix1+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix2_neg',
        'BPix1+FPix2_neg+FPix3_neg',
        'BPix1+FPix1_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_pos+FPix3_pos'
    )
)


process.hltPixelTracks = cms.EDProducer("PixelTrackProducerFromSoAAlpakaPhase1",
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    minNumberOfHits = cms.int32(0),
    minQuality = cms.string('loose'),
    pixelRecHitLegacySrc = cms.InputTag("hltSiPixelRecHits"),
    trackSrc = cms.InputTag("hltPixelTracksSoA")
)


process.hltPixelTracksSoA = cms.EDProducer("CAHitNtupletAlpakaPhase1@alpaka",
    CAThetaCutBarrel = cms.double(0.00123302705499),
    CAThetaCutForward = cms.double(0.00355691321774),
    CPE = cms.string('PixelCPEFastParams'),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    cellPtCut = cms.double(0.5),
    cellZ0Cut = cms.double(12.0),
    dcaCutInnerTriplet = cms.double(0.0918113099491),
    dcaCutOuterTriplet = cms.double(0.420724617835),
    doClusterCut = cms.bool(True),
    doPtCut = cms.bool(True),
    doSharedHitCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    earlyFishbone = cms.bool(True),
    fillStatistics = cms.bool(False),
    fitNas4 = cms.bool(False),
    hardCurvCut = cms.double(0.503169690002),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(True),
    lateFishbone = cms.bool(False),
    maxNumberOfDoublets = cms.uint32(524288),
    minHitsForSharingCut = cms.uint32(10),
    minHitsPerNtuplet = cms.uint32(3),
    minYsizeB1 = cms.int32(1),
    minYsizeB2 = cms.int32(1),
    phiCuts = cms.vint32(
        965, 1241, 395, 698, 1058,
        1211, 348, 782, 1016, 810,
        463, 755, 694, 531, 770,
        471, 592, 750, 348
    ),
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsSoA"),
    ptmin = cms.double(0.9),
    trackQualityCuts = cms.PSet(
        chi2Coeff = cms.vdouble(0.9, 1.8),
        chi2MaxPt = cms.double(10.0),
        chi2Scale = cms.double(8.0),
        quadrupletMaxTip = cms.double(0.5),
        quadrupletMaxZip = cms.double(12.0),
        quadrupletMinPt = cms.double(0.3),
        tripletMaxTip = cms.double(0.3),
        tripletMaxZip = cms.double(12.0),
        tripletMinPt = cms.double(0.5)
    ),
    useRiemannFit = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True)
)


process.hltPixelVertices = cms.EDProducer("PixelVertexProducerFromSoAAlpaka",
    TrackCollection = cms.InputTag("hltPixelTracks"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    src = cms.InputTag("hltPixelVerticesSoA")
)


process.hltPixelVerticesSoA = cms.EDProducer("PixelVertexProducerAlpakaPhase1@alpaka",
    PtMax = cms.double(75.0),
    PtMin = cms.double(0.5),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    chi2max = cms.double(9.0),
    doSplitting = cms.bool(True),
    eps = cms.double(0.07),
    errmax = cms.double(0.01),
    maxVertices = cms.int32(256),
    minT = cms.int32(2),
    oneKernel = cms.bool(True),
    pixelTrackSrc = cms.InputTag("hltPixelTracksSoA"),
    useDBSCAN = cms.bool(False),
    useDensity = cms.bool(True),
    useIterative = cms.bool(False)
)


process.hltRechitInRegionsECAL = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring(
        'EcalRecHitsEB',
        'EcalRecHitsEE'
    ),
    recHitLabels = cms.VInputTag("hltEcalRecHit:EcalRecHitsEB", "hltEcalRecHit:EcalRecHitsEE")
)


process.hltRechitInRegionsES = cms.EDProducer("HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","EGamma"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(5.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('EGamma')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Jet"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(170.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Jet')
        ),
        cms.PSet(
            inputColl = cms.InputTag("hltGtStage2Digis","Tau"),
            maxEt = cms.double(999999.0),
            minEt = cms.double(100.0),
            regionEtaMargin = cms.double(0.9),
            regionPhiMargin = cms.double(1.2),
            type = cms.string('Tau')
        )
    ),
    productLabels = cms.vstring('EcalRecHitsES'),
    recHitLabels = cms.VInputTag("hltEcalPreshowerRecHit:EcalRecHitsES")
)


process.hltSiPixelClusters = cms.EDProducer("SiPixelDigisClustersFromSoAAlpakaPhase1",
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    produceDigis = cms.bool(False),
    src = cms.InputTag("hltSiPixelClustersSoA"),
    storeDigis = cms.bool(False)
)


process.hltSiPixelClustersSoA = cms.EDProducer("SiPixelRawToClusterPhase1@alpaka",
    CablingMapLabel = cms.string(''),
    IncludeErrors = cms.bool(True),
    InputLabel = cms.InputTag("rawDataCollector"),
    Regions = cms.PSet(

    ),
    UseQualityInfo = cms.bool(False),
    VCaltoElectronGain = cms.double(1.0),
    VCaltoElectronGain_L1 = cms.double(1.0),
    VCaltoElectronOffset = cms.double(0.0),
    VCaltoElectronOffset_L1 = cms.double(0.0),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000)
)


process.hltSiPixelDigiErrors = cms.EDProducer("SiPixelDigiErrorsFromSoAAlpaka",
    CablingMapLabel = cms.string(''),
    ErrorList = cms.vint32(29),
    UsePhase1 = cms.bool(True),
    UserErrorList = cms.vint32(40),
    digiErrorSoASrc = cms.InputTag("hltSiPixelClustersSoA"),
    fmtErrorsSoASrc = cms.InputTag("hltSiPixelClustersSoA")
)


process.hltSiPixelRecHits = cms.EDProducer("SiPixelRecHitFromSoAAlpakaPhase1",
    pixelRecHitSrc = cms.InputTag("hltSiPixelRecHitsSoA"),
    src = cms.InputTag("hltSiPixelClusters")
)


process.hltSiPixelRecHitsSoA = cms.EDProducer("SiPixelRecHitAlpakaPhase1@alpaka",
    CPE = cms.string('PixelCPEFastParams'),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    beamSpot = cms.InputTag("hltOnlineBeamSpotDevice"),
    src = cms.InputTag("hltSiPixelClustersSoA")
)


process.hltSiStripExcludedFEDListProducer = cms.EDProducer("SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag("rawDataCollector")
)


process.hltSiStripRawToClustersFacility = cms.EDProducer("SiStripClusterizerFromRaw",
    Algorithms = cms.PSet(
        CommonModeNoiseSubtractionMode = cms.string('Median'),
        PedestalSubtractionFedMode = cms.bool(True),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        Use10bitsTruncation = cms.bool(False),
        doAPVRestore = cms.bool(False),
        useCMMeanMap = cms.bool(False)
    ),
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        ConditionsLabel = cms.string(''),
        MaxAdjacentBad = cms.uint32(0),
        MaxClusterSize = cms.uint32(16),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
        ),
        setDetId = cms.bool(True)
    ),
    ConditionsLabel = cms.string(''),
    DoAPVEmulatorCheck = cms.bool(False),
    HybridZeroSuppressed = cms.bool(False),
    LegacyUnpacker = cms.bool(False),
    ProductLabel = cms.InputTag("rawDataCollector"),
    onDemand = cms.bool(False)
)


process.hltSiStripRecHits = cms.EDProducer("SiStripRecHitConverter",
    ClusterProducer = cms.InputTag("hltSiStripRawToClustersFacility"),
    MaskBadAPVFibers = cms.bool(False),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    StripCPE = cms.ESInputTag("hltESPStripCPEfromTrackAngle","hltESPStripCPEfromTrackAngle"),
    doMatching = cms.bool(False),
    matchedRecHits = cms.string('matchedRecHit'),
    rphiRecHits = cms.string('rphiRecHit'),
    siStripQualityLabel = cms.ESInputTag("",""),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False)
)


process.hltTriggerSummaryAOD = cms.EDProducer("TriggerSummaryProducerAOD",
    moduleLabelPatternsToMatch = cms.vstring('hlt*'),
    moduleLabelPatternsToSkip = cms.vstring(),
    processName = cms.string('@'),
    throw = cms.bool(False)
)


process.hltTriggerSummaryRAW = cms.EDProducer("TriggerSummaryProducerRAW",
    processName = cms.string('@')
)


process.hltTrimmedPixelVertices = cms.EDProducer("PixelVertexCollectionTrimmer",
    PVcomparer = cms.PSet(
        refToPSet_ = cms.string('HLTPSetPvClusterComparerForIT')
    ),
    fractionSumPt2 = cms.double(0.3),
    maxVtx = cms.uint32(100),
    minSumPt2 = cms.double(0.0),
    src = cms.InputTag("hltPixelVertices")
)


process.hltBoolEnd = cms.EDFilter("HLTBool",
    result = cms.bool(True)
)


process.hltBoolFalse = cms.EDFilter("HLTBool",
    result = cms.bool(False)
)


process.hltDiEG33CaloIdLClusterShapeUnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEG33HEUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.014),
    thrRegularEE = cms.vdouble(0.035),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShapeUnseeded","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltDiEG33EtUnseededFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(33.0),
    etcutEE = cms.double(33.0),
    inputTag = cms.InputTag("hltEgammaCandidatesWrapperUnseeded"),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(2),
    saveTags = cms.bool(True)
)


process.hltDiEG33HEUnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEG33EtUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.15),
    thrOverEEE = cms.vdouble(0.1),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverEUnseeded")
)


process.hltDiEle33CaloIdLMWPMS2UnseededFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltDiEle33CaloIdLPixelMatchUnseededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(150.0),
    thrRegularEE = cms.vdouble(150.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVarsUnseeded","s2")
)


process.hltDiEle33CaloIdLPixelMatchUnseededFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltDiEG33CaloIdLClusterShapeUnseededFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidatesUnseeded"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeedsUnseeded"),
    ncandcut = cms.int32(2),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEG115CaloIdVTClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG115EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.03),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG115CaloIdVTHEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG115CaloIdVTClusterShapeFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.075),
    thrOverEEE = cms.vdouble(0.075),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEG115EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(115.0),
    etcutEE = cms.double(115.0),
    inputTag = cms.InputTag("hltEGL1SingleEGNonIsoOrWithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG135CaloIdVTClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG135EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.011),
    thrRegularEE = cms.vdouble(0.03),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG135CaloIdVTHEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG135CaloIdVTClusterShapeFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.075),
    thrOverEEE = cms.vdouble(0.075),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEG135EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(135.0),
    etcutEE = cms.double(135.0),
    inputTag = cms.InputTag("hltEGL1SingleEGNonIsoOrWithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG30L1SingleEGOrEtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(30.0),
    etcutEE = cms.double(30.0),
    inputTag = cms.InputTag("hltEGL1SingleEGOrFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG32L1SingleEGOrEtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(32.0),
    etcutEE = cms.double(32.0),
    inputTag = cms.InputTag("hltEGL1SingleEGOrFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG33CaloIdLClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG33HEFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.014),
    thrRegularEE = cms.vdouble(0.035),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEG33EtFilter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(33.0),
    etcutEE = cms.double(33.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEG33HEFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG33EtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.15),
    thrOverEEE = cms.vdouble(0.1),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleAndDoubleEGOrPairFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleAndDoubleEG"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(2),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleEGNonIsoOrWithJetAndTau"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEGL1SingleEGOrFilter = cms.EDFilter("HLTEgammaL1TMatchFilterRegional",
    L1SeedFilterTag = cms.InputTag("hltL1sSingleEGor"),
    barrel_end = cms.double(1.4791),
    candIsolatedTag = cms.InputTag("hltEgammaCandidates"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(False),
    endcap_end = cms.double(2.65),
    l1CenJetsTag = cms.InputTag("hltGtStage2Digis","Jet"),
    l1IsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1NonIsolatedTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    l1TausTag = cms.InputTag("hltGtStage2Digis","Tau"),
    ncandcut = cms.int32(1),
    region_eta_size = cms.double(0.522),
    region_eta_size_ecap = cms.double(1.0),
    region_phi_size = cms.double(1.044),
    saveTags = cms.bool(True)
)


process.hltEgammaCandidatesWrapperUnseeded = cms.EDFilter("HLTEgammaTriggerFilterObjectWrapper",
    candIsolatedTag = cms.InputTag("hltEgammaCandidatesUnseeded"),
    candNonIsolatedTag = cms.InputTag(""),
    doIsolated = cms.bool(True),
    saveTags = cms.bool(True)
)


process.hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle115CaloIdVTPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.007),
    thrRegularEE = cms.vdouble(0.007),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.07),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle115CaloIdVTPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG115CaloIdVTHEFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle135CaloIdVTPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.007),
    thrRegularEE = cms.vdouble(0.007),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.07),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle135CaloIdVTPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG135CaloIdVTHEFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.013),
    thrRegularEE = cms.vdouble(0.035),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.013),
    thrRegularEE = cms.vdouble(0.035),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.01),
    thrRegularEE = cms.vdouble(0.015),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.01),
    thrRegularEE = cms.vdouble(0.015),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.1),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.07),
    thrRegularEE = cms.vdouble(0.1),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.5),
    thrOverEEE = cms.vdouble(0.5),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.29, 0.21),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.5),
    thrOverEEE = cms.vdouble(0.5),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(23.0),
    etcutEE = cms.double(23.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGOrPairFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(1),
    saveTags = cms.bool(True)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter = cms.EDFilter("HLTEgammaEtFilter",
    etcutEB = cms.double(12.0),
    etcutEE = cms.double(12.0),
    inputTag = cms.InputTag("hltEGL1SingleAndDoubleEGOrPairFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    maxEtaCut = cms.double(9999.0),
    minEtaCut = cms.double(-9999.0),
    ncandcut = cms.int32(2),
    saveTags = cms.bool(True)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.13),
    thrOverEEE = cms.vdouble(0.13),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.13),
    thrOverEEE = cms.vdouble(0.13),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.3),
    thrOverEEE = cms.vdouble(0.3),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.2, 0.25),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.3),
    thrOverEEE = cms.vdouble(0.3),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999999.0),
    thrRegularEE = cms.vdouble(999999.0),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999999.0),
    thrRegularEE = cms.vdouble(999999.0),
    useAbs = cms.bool(True),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(2),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.2),
    thrOverEEE = cms.vdouble(0.2),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(0.2),
    thrOverEEE = cms.vdouble(0.2),
    thrRegularEB = cms.vdouble(-1.0),
    thrRegularEE = cms.vdouble(-1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle30WPTightClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG30L1SingleEGOrEtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.0105),
    thrRegularEE = cms.vdouble(0.0305),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle30WPTightEcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightHEFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.1, 0.08, 0.06, 0.06),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.01),
    thrOverEEB2 = cms.vdouble(0.01),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(3.0),
    thrRegularEB2 = cms.vdouble(3.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIsoDr0p2")
)


process.hltEle30WPTightGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfMissingHitsFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.003),
    thrRegularEE = cms.vdouble(0.005),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle30WPTightGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.03),
    thrRegularEE = cms.vdouble(0.023),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle30WPTightGsfMissingHitsFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightGsfOneOEMinusOneOPFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999.0),
    thrRegularEE = cms.vdouble(1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","MissingHits")
)


process.hltEle30WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightPMS2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.025),
    thrRegularEE = cms.vdouble(0.011),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle30WPTightGsfTrackIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightGsfDphiFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.03, 0.04, 0.114, 0.032),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.0),
    thrOverEEB2 = cms.vdouble(0.0),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(2.0),
    thrRegularEB2 = cms.vdouble(2.0),
    thrRegularEE1 = cms.vdouble(-0.363),
    thrRegularEE2 = cms.vdouble(0.702),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle30WPTightHEFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle30WPTightClusterShapeFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.066, 0.14, 0.3, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.06),
    thrOverEEB2 = cms.vdouble(0.06),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(1.0),
    thrRegularEB2 = cms.vdouble(1.0),
    thrRegularEE1 = cms.vdouble(3.0),
    thrRegularEE2 = cms.vdouble(5.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle30WPTightHcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.0),
    candTag = cms.InputTag("hltEle30WPTightEcalIsoFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.26, 0.32, 0.4, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.04),
    thrOverEEB2 = cms.vdouble(0.04),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(4.0),
    thrRegularEB2 = cms.vdouble(4.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle30WPTightPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle30WPTightPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(200.0),
    thrRegularEE = cms.vdouble(45.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle30WPTightPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle30WPTightHcalIsoFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle32WPTightClusterShapeFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEG32L1SingleEGOrEtFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.0105),
    thrRegularEE = cms.vdouble(0.0305),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5NoiseCleaned")
)


process.hltEle32WPTightEcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightHEFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.1, 0.08, 0.06, 0.06),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.01),
    thrOverEEB2 = cms.vdouble(0.01),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(3.0),
    thrRegularEB2 = cms.vdouble(3.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIsoDr0p2")
)


process.hltEle32WPTightGsfDetaFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfMissingHitsFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.003),
    thrRegularEE = cms.vdouble(0.005),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","DetaSeed")
)


process.hltEle32WPTightGsfDphiFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfDetaFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.03),
    thrRegularEE = cms.vdouble(0.023),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","Dphi")
)


process.hltEle32WPTightGsfMissingHitsFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightGsfOneOEMinusOneOPFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(999.0),
    thrRegularEE = cms.vdouble(1.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","MissingHits")
)


process.hltEle32WPTightGsfOneOEMinusOneOPFilter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightPMS2Filter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(0.025),
    thrRegularEE = cms.vdouble(0.011),
    useAbs = cms.bool(True),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP")
)


process.hltEle32WPTightGsfTrackIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightGsfDphiFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.03, 0.04, 0.114, 0.032),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.0),
    thrOverEEB2 = cms.vdouble(0.0),
    thrOverEEE1 = cms.vdouble(0.025),
    thrOverEEE2 = cms.vdouble(0.025),
    thrRegularEB1 = cms.vdouble(2.0),
    thrRegularEB2 = cms.vdouble(2.0),
    thrRegularEE1 = cms.vdouble(-0.363),
    thrRegularEE2 = cms.vdouble(0.702),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
)


process.hltEle32WPTightHEFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltEle32WPTightClusterShapeFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.066, 0.14, 0.3, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.06),
    thrOverEEB2 = cms.vdouble(0.06),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(1.0),
    thrRegularEB2 = cms.vdouble(1.0),
    thrRegularEE1 = cms.vdouble(3.0),
    thrRegularEE2 = cms.vdouble(5.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaHoverE")
)


process.hltEle32WPTightHcalIsoFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.0),
    candTag = cms.InputTag("hltEle32WPTightEcalIsoFilter"),
    doRhoCorrection = cms.bool(True),
    effectiveAreas = cms.vdouble(0.26, 0.32, 0.4, 0.5),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.04),
    thrOverEEB2 = cms.vdouble(0.04),
    thrOverEEE1 = cms.vdouble(0.03),
    thrOverEEE2 = cms.vdouble(0.03),
    thrRegularEB1 = cms.vdouble(4.0),
    thrRegularEB2 = cms.vdouble(4.0),
    thrRegularEE1 = cms.vdouble(1.0),
    thrRegularEE2 = cms.vdouble(2.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
)


process.hltEle32WPTightPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle32WPTightPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(200.0),
    thrRegularEE = cms.vdouble(45.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle32WPTightPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEle32WPTightHcalIsoFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltEle33CaloIdLMWPMS2Filter = cms.EDFilter("HLTEgammaGenericFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.479),
    candTag = cms.InputTag("hltEle33CaloIdLPixelMatchFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.0, 0.0),
    energyLowEdges = cms.vdouble(0.0),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(1),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag(""),
    saveTags = cms.bool(True),
    thrOverE2EB = cms.vdouble(-1.0),
    thrOverE2EE = cms.vdouble(-1.0),
    thrOverEEB = cms.vdouble(-1.0),
    thrOverEEE = cms.vdouble(-1.0),
    thrRegularEB = cms.vdouble(150.0),
    thrRegularEE = cms.vdouble(150.0),
    useAbs = cms.bool(False),
    useEt = cms.bool(False),
    varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
)


process.hltEle33CaloIdLPixelMatchFilter = cms.EDFilter("HLTElectronPixelMatchFilter",
    candTag = cms.InputTag("hltEG33CaloIdLClusterShapeFilter"),
    l1EGCand = cms.InputTag("hltEgammaCandidates"),
    l1PixelSeedsTag = cms.InputTag("hltEgammaElectronPixelSeeds"),
    ncandcut = cms.int32(1),
    npixelmatchcut = cms.double(1.0),
    pixelVeto = cms.bool(False),
    s2_threshold = cms.double(0.4),
    s_a_phi1B = cms.double(0.0069),
    s_a_phi1F = cms.double(0.0076),
    s_a_phi1I = cms.double(0.0088),
    s_a_phi2B = cms.double(0.00037),
    s_a_phi2F = cms.double(0.00906),
    s_a_phi2I = cms.double(0.0007),
    s_a_rF = cms.double(0.04),
    s_a_rI = cms.double(0.027),
    s_a_zB = cms.double(0.012),
    saveTags = cms.bool(True),
    tanhSO10BarrelThres = cms.double(0.35),
    tanhSO10ForwardThres = cms.double(1.0),
    tanhSO10InterThres = cms.double(1.0),
    useS = cms.bool(False)
)


process.hltL1sSingleAndDoubleEG = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1EtSumZdcInputTag = cms.InputTag("hltGtStage2Digis","EtSumZDC"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_DoubleEG_LooseIso22_12_er2p5'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1EtSumZdcInputTag = cms.InputTag("hltGtStage2Digis","EtSumZDC"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleEG26er2p5 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_DoubleEG_22_10_er2p5 OR L1_DoubleEG_25_12_er2p5 OR L1_DoubleEG_25_14_er2p5 OR L1_SingleJet160er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleEGNonIsoOrWithJetAndTau = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1EtSumZdcInputTag = cms.InputTag("hltGtStage2Digis","EtSumZDC"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleJet160er2p5 OR L1_SingleJet180 OR L1_SingleJet200 OR L1_SingleTau120er2p1 OR L1_SingleTau130er2p1 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltL1sSingleEGor = cms.EDFilter("HLTL1TSeed",
    L1EGammaInputTag = cms.InputTag("hltGtStage2Digis","EGamma"),
    L1EtSumInputTag = cms.InputTag("hltGtStage2Digis","EtSum"),
    L1EtSumZdcInputTag = cms.InputTag("hltGtStage2Digis","EtSumZDC"),
    L1GlobalInputTag = cms.InputTag("hltGtStage2Digis"),
    L1JetInputTag = cms.InputTag("hltGtStage2Digis","Jet"),
    L1MuonInputTag = cms.InputTag("hltGtStage2Digis","Muon"),
    L1MuonShowerInputTag = cms.InputTag("hltGtStage2Digis","MuonShower"),
    L1ObjectMapInputTag = cms.InputTag("hltGtStage2ObjectMap"),
    L1SeedsLogicalExpression = cms.string('L1_SingleLooseIsoEG26er2p5 OR L1_SingleLooseIsoEG26er1p5 OR L1_SingleLooseIsoEG28er2p5 OR L1_SingleLooseIsoEG28er2p1 OR L1_SingleLooseIsoEG28er1p5 OR L1_SingleLooseIsoEG30er2p5 OR L1_SingleLooseIsoEG30er1p5 OR L1_SingleEG26er2p5 OR L1_SingleEG38er2p5 OR L1_SingleEG40er2p5 OR L1_SingleEG42er2p5 OR L1_SingleEG45er2p5 OR L1_SingleEG60 OR L1_SingleEG34er2p5 OR L1_SingleEG36er2p5 OR L1_SingleIsoEG24er2p1 OR L1_SingleIsoEG26er2p1 OR L1_SingleIsoEG28er2p1 OR L1_SingleIsoEG30er2p1 OR L1_SingleIsoEG32er2p1 OR L1_SingleIsoEG26er2p5 OR L1_SingleIsoEG28er2p5 OR L1_SingleIsoEG30er2p5 OR L1_SingleIsoEG32er2p5 OR L1_SingleIsoEG34er2p5'),
    L1TauInputTag = cms.InputTag("hltGtStage2Digis","Tau"),
    saveTags = cms.bool(True)
)


process.hltPreDoubleEle33CaloIdLMW = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle115CaloIdVTGsfTrkIdT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle135CaloIdVTGsfTrkIdT = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle23Ele12CaloIdLTrackIdLIsoVL = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle30WPTightGsf = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltPreEle32WPTightGsf = cms.EDFilter("HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag("hltGtStage2Digis"),
    offset = cms.uint32(0)
)


process.hltTriggerType = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)


process.hltGetRaw = cms.EDAnalyzer("HLTGetRaw",
    RawDataCollection = cms.InputTag("rawDataCollector")
)


process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string('DQMIO.root')
)


process.DQMStore = cms.Service("DQMStore",
    MEsToSave = cms.untracked.vstring( (
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm4',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp4',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfDigi_TIDP_D1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfCluster_TIDP_D1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfDigi_TIB_L1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfCluster_TIB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfDigi_TOB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfCluster_TOB_L1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfDigi_TECP_W1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfCluster_TECP_W1',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfTracks_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPt_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEta_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Strip_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Pixel_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBS_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSdz_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsPhi_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsEta_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackQoverP_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/Quality_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_PUvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtLoose_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaLoose_ImpactPoint_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/NumberOfGoodPVtx_offline',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/GoodPVtxNumberOfTracks_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_PUvtx_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/FractionOfGoodPVtx_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_op_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_op_ImpactPoint_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'OfflinePV/offlinePrimaryVertices/tagDiffX',
        'OfflinePV/offlinePrimaryVertices/tagDiffY',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/PtJetMET/Jet/Cleanedak4PFJetsPuppi/Phi',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/NJets',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta_uncor',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices',
        'JetMET/HIJetValidation/akCs4PFJets/SumPFPt',
        'JetMET/HIJetValidation/akCs4PFJets/NJets',
        'JetMET/HIJetValidation/akCs4PFJets/NPFpart',
        'JetMET/HIJetValidation/akPu4CaloJets/SumCaloPt',
        'JetMET/HIJetValidation/akPu4CaloJets/NCalopart',
        'JetMET/HIJetValidation/akPu4CaloJets/NJets',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi',
        'Muons/MuonRecoAnalyzer/Res_TkGlb_qOverlap',
        'Muons/diMuonHistograms/GlbGlbMuon_LM',
        'Muons/diMuonHistograms/GlbGlbMuon_HM',
        'Muons/Isolation/global/relPFIso_R03',
        'Muons/globalMuons/GeneralProperties/NumberOfMeanRecHitsPerTrack_glb',
        'Muons/standAloneMuonsUpdatedAtVtx/HitProperties/NumberOfValidRecHitsPerTrack_sta',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_pt',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_eta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele0_vertexPt_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele1_vertexPt_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele2_vertexEta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele5_vertexZ',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele101_etaEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele102_phiEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele201_mee_os'
     ) ),
    assertLegacySafe = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(True),
    onlineMode = cms.untracked.bool(False),
    saveByLumi = cms.untracked.bool(False),
    trackME = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)


process.FastTimerService = cms.Service("FastTimerService",
    dqmLumiSectionsRange = cms.untracked.uint32(2500),
    dqmMemoryRange = cms.untracked.double(1000000.0),
    dqmMemoryResolution = cms.untracked.double(5000.0),
    dqmModuleMemoryRange = cms.untracked.double(100000.0),
    dqmModuleMemoryResolution = cms.untracked.double(500.0),
    dqmModuleTimeRange = cms.untracked.double(40.0),
    dqmModuleTimeResolution = cms.untracked.double(0.2),
    dqmPath = cms.untracked.string('HLT/TimerService'),
    dqmPathMemoryRange = cms.untracked.double(1000000.0),
    dqmPathMemoryResolution = cms.untracked.double(5000.0),
    dqmPathTimeRange = cms.untracked.double(100.0),
    dqmPathTimeResolution = cms.untracked.double(0.5),
    dqmTimeRange = cms.untracked.double(2000.0),
    dqmTimeResolution = cms.untracked.double(5.0),
    enableDQM = cms.untracked.bool(True),
    enableDQMTransitions = cms.untracked.bool(False),
    enableDQMbyLumiSection = cms.untracked.bool(True),
    enableDQMbyModule = cms.untracked.bool(False),
    enableDQMbyPath = cms.untracked.bool(False),
    enableDQMbyProcesses = cms.untracked.bool(True),
    jsonFileName = cms.untracked.string('resources.json'),
    printEventSummary = cms.untracked.bool(False),
    printJobSummary = cms.untracked.bool(True),
    printRunSummary = cms.untracked.bool(True),
    writeJSONSummary = cms.untracked.bool(False)
)


process.MessageLogger = cms.Service("MessageLogger",
    FastReport = cms.untracked.PSet(

    ),
    HLTrigReport = cms.untracked.PSet(

    ),
    L1GtTrigReport = cms.untracked.PSet(

    ),
    L1TGlobalSummary = cms.untracked.PSet(

    ),
    ThroughputService = cms.untracked.PSet(

    ),
    TriggerSummaryProducerAOD = cms.untracked.PSet(

    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enableStatistics = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        threshold = cms.untracked.string('INFO')
    ),
    debugModules = cms.untracked.vstring(),
    suppressDebug = cms.untracked.vstring(),
    suppressError = cms.untracked.vstring(
        'hltL3TkTracksFromL2IOHit',
        'hltL3TkTracksFromL2OIHit',
        'hltL3TkTracksFromL2OIState'
    ),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(
        'hltL3MuonsIOHit',
        'hltL3MuonsOIHit',
        'hltL3MuonsOIState',
        'hltLightPFTracks',
        'hltPixelTracks',
        'hltPixelTracksForHighMult',
        'hltSiPixelClusters',
        'hltSiPixelDigis'
    )
)


process.PrescaleService = cms.Service("PrescaleService",
    forceDefault = cms.bool(True),
    lvl1DefaultLabel = cms.string('2p0E34+ZeroBias+HLTPhysics'),
    lvl1Labels = cms.vstring(
        'Emergency',
        'EmittanceScan',
        '2p0E34+ZeroBias+HLTPhysics',
        '2p0E34',
        '1p95E34',
        '1p9E34',
        '1p85E34',
        '1p8E34',
        '1p6E34',
        '1p4E34',
        '2p0E34_OnlyMuons',
        '2p0E34_NoL1CICADA',
        'Backup1',
        'Backup2',
        'HIon',
        'PRef'
    ),
    prescaleTable = cms.VPSet(
        cms.PSet(
            pathName = cms.string('HLT_DoubleEle33_CaloIdL_MW_v30'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        ),
        cms.PSet(
            pathName = cms.string('HLT_Ele30_WPTight_Gsf_v13'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        ),
        cms.PSet(
            pathName = cms.string('HLT_Ele32_WPTight_Gsf_v27'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        ),
        cms.PSet(
            pathName = cms.string('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        ),
        cms.PSet(
            pathName = cms.string('HLT_Ele115_CaloIdVT_GsfTrkIdT_v27'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        ),
        cms.PSet(
            pathName = cms.string('HLT_Ele135_CaloIdVT_GsfTrkIdT_v20'),
            prescales = cms.vuint32(
                0, 1, 1, 1, 1,
                1, 1, 1, 1, 1,
                0, 1, 1, 1, 1,
                0
            )
        )
    )
)


process.ThroughputService = cms.Service("ThroughputService",
    dqmPath = cms.untracked.string('HLT/Throughput'),
    dqmPathByProcesses = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    timeRange = cms.untracked.double(60000.0),
    timeResolution = cms.untracked.double(5.828)
)


process.ProcessAcceleratorAlpaka = ProcessAcceleratorAlpaka()


process.ProcessAcceleratorCUDA = ProcessAcceleratorCUDA()


process.ProcessAcceleratorROCm = ProcessAcceleratorROCm()


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection'),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESProducer = cms.ESProducer("CSCChannelMapperESProducer",
    AlgoName = cms.string('CSCChannelMapperPostls1')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSCIndexerESProducer = cms.ESProducer("CSCIndexerESProducer",
    AlgoName = cms.string('CSCIndexerPostls1')
)


process.CSCObjectMapESProducer = cms.ESProducer("CSCObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapAuto = cms.untracked.bool(False),
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz'),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string(''),
    dump = cms.untracked.vstring()
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.DTObjectMapESProducer = cms.ESProducer("DTObjectMapESProducer",
    appendToDataLabel = cms.string('')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    appendToDataLabel = cms.string(''),
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalParameters = cms.ESProducer("StableParametersTrivialProducer",
    IfCaloEtaNumberBits = cms.uint32(4),
    IfMuEtaNumberBits = cms.uint32(6),
    NumberChips = cms.uint32(1),
    NumberConditionChips = cms.uint32(1),
    NumberL1CenJet = cms.uint32(4),
    NumberL1EGamma = cms.uint32(12),
    NumberL1ForJet = cms.uint32(4),
    NumberL1IsoEG = cms.uint32(4),
    NumberL1Jet = cms.uint32(12),
    NumberL1JetCounts = cms.uint32(12),
    NumberL1Mu = cms.uint32(4),
    NumberL1Muon = cms.uint32(8),
    NumberL1NoIsoEG = cms.uint32(4),
    NumberL1Tau = cms.uint32(12),
    NumberL1TauJet = cms.uint32(4),
    NumberPhysTriggers = cms.uint32(512),
    NumberPhysTriggersExtended = cms.uint32(64),
    NumberPsbBoards = cms.int32(7),
    NumberTechnicalTriggers = cms.uint32(64),
    OrderConditionChip = cms.vint32(1),
    OrderOfChip = cms.vint32(1),
    PinsOnChip = cms.uint32(512),
    PinsOnConditionChip = cms.uint32(512),
    TotalBxInEvent = cms.int32(5),
    UnitLength = cms.int32(8),
    WordLength = cms.int32(64),
    appendToDataLabel = cms.string('')
)


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.HcalTopologyIdealEP = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorForHI = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOppositeForHI'),
    Mass = cms.double(0.139),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStepOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.ParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForMixedStep = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForMixedStep'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiPixelTemplateStoreESProducer = cms.ESProducer("SiPixelTemplateStoreESProducer",
    appendToDataLabel = cms.string('')
)


process.SiStripClusterizerConditionsESProducer = cms.ESProducer("SiStripClusterizerConditionsESProducer",
    Label = cms.string(''),
    QualityLabel = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.SiStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.SiStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SiStripRegionConnectivity = cms.ESProducer("SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32(20),
    EtaMax = cms.untracked.double(2.5),
    PhiDivisions = cms.untracked.uint32(20),
    appendToDataLabel = cms.string('')
)


process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    appendToDataLabel = cms.string(''),
    minTracks = cms.uint32(3),
    minVertices = cms.uint32(1),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    appendToDataLabel = cms.string(''),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.TrackerAdditionalParametersPerDetESModule = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerDigiGeometryESModule = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.TrackerGeometricDetESModule = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder'),
    appendToDataLabel = cms.string('')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('CaloDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    PluginName = cms.string(''),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.ctppsGeometryESModule = cms.ESProducer("CTPPSGeometryESModule",
    appendToDataLabel = cms.string(''),
    buildMisalignedGeometry = cms.bool(False),
    compactViewTag = cms.string(''),
    dbTag = cms.string(''),
    fromDD4hep = cms.untracked.bool(False),
    fromPreprocessedDB = cms.untracked.bool(True),
    isRun2 = cms.bool(False),
    verbosity = cms.untracked.uint32(1)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True)
)


process.ecalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('EcalDetIdAssociator'),
    etaBinSize = cms.double(0.02),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(300),
    nPhi = cms.int32(360)
)


process.ecalElectronicsMappingHostESProducer = cms.ESProducer("EcalElectronicsMappingHostESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.ecalMultifitConditionsHostESProducer = cms.ESProducer("EcalMultifitConditionsHostESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.ecalSeverityLevel = cms.ESProducer("EcalSeverityLevelESProducer",
    dbstatusMask = cms.PSet(
        kBad = cms.vstring(
            'kNonRespondingIsolated',
            'kDeadVFE',
            'kDeadFE',
            'kNoDataNoTP'
        ),
        kGood = cms.vstring('kOk'),
        kProblematic = cms.vstring(
            'kDAC',
            'kNoLaser',
            'kNoisy',
            'kNNoisy',
            'kNNNoisy',
            'kNNNNoisy',
            'kNNNNNoisy',
            'kFixedG6',
            'kFixedG1',
            'kFixedG0'
        ),
        kRecovered = cms.vstring(),
        kTime = cms.vstring(),
        kWeird = cms.vstring()
    ),
    flagMask = cms.PSet(
        kBad = cms.vstring(
            'kFaultyHardware',
            'kDead',
            'kKilled'
        ),
        kGood = cms.vstring('kGood'),
        kProblematic = cms.vstring(
            'kPoorReco',
            'kPoorCalib',
            'kNoisy',
            'kSaturated'
        ),
        kRecovered = cms.vstring(
            'kLeadingEdgeRecovered',
            'kTowerRecovered'
        ),
        kTime = cms.vstring('kOutOfTime'),
        kWeird = cms.vstring(
            'kWeird',
            'kDiWeird'
        )
    ),
    timeThresh = cms.double(2.0)
)


process.hcalChannelPropertiesESProd = cms.ESProducer("HcalChannelPropertiesEP")


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HcalDetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(70),
    nPhi = cms.int32(72)
)


process.hcalMahiConditionsESProducer = cms.ESProducer("HcalMahiConditionsESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
    DropChannelStatusBits = cms.vstring(
        'HcalCellMask',
        'HcalCellOff',
        'HcalCellDead'
    ),
    RecoveredRecHitBits = cms.vstring(''),
    SeverityLevels = cms.VPSet(
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(0),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerProb'),
            Level = cms.int32(1),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellExcludeFromHBHENoiseSummary'),
            Level = cms.int32(5),
            RecHitFlags = cms.vstring(
                'HBHEIsolatedNoise',
                'HFAnomalousHit'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(8),
            RecHitFlags = cms.vstring(
                'HBHEHpdHitMultiplicity',
                'HBHESpikeNoise',
                'HBHETS4TS5Noise',
                'HBHEOOTPU',
                'HBHEFlatNoise',
                'HBHENegativeNoise'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(''),
            Level = cms.int32(11),
            RecHitFlags = cms.vstring(
                'HFLongShort',
                'HFS8S1Ratio',
                'HFPET',
                'HFSignalAsymmetry'
            )
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellCaloTowerMask'),
            Level = cms.int32(12),
            RecHitFlags = cms.vstring()
        ),
        cms.PSet(
            ChannelStatus = cms.vstring('HcalCellHot'),
            Level = cms.int32(15),
            RecHitFlags = cms.vstring('')
        ),
        cms.PSet(
            ChannelStatus = cms.vstring(
                'HcalCellOff',
                'HcalCellDead'
            ),
            Level = cms.int32(20),
            RecHitFlags = cms.vstring('')
        )
    ),
    appendToDataLabel = cms.string(''),
    phase = cms.uint32(1)
)


process.hcalRecoParamWithPulseShapeESProducer = cms.ESProducer("HcalRecoParamWithPulseShapeESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hcalSiPMCharacteristicsESProducer = cms.ESProducer("HcalSiPMCharacteristicsESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer")


process.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    appendToDataLabel = cms.string(''),
    gbrForestLabel = cms.string(''),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.hltCombinedSecondaryVertex = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    appendToDataLabel = cms.string(''),
    calibrationRecord = cms.string(''),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertex',
        'CombinedSVPseudoVertex',
        'CombinedSVNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSelection = cms.PSet(
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltCombinedSecondaryVertexV2 = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    appendToDataLabel = cms.string(''),
    calibrationRecord = cms.string(''),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string('HLT'),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(3),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5.0),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500.0),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3.0),
        min_pT = cms.double(120.0),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    appendToDataLabel = cms.string(''),
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any')
)


process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    appendToDataLabel = cms.string(''),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESChi2MeasurementEstimatorForP5 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESChi2MeasurementEstimatorForP5'),
    MaxChi2 = cms.double(100.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(100000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESFittingSmootherRKP5 = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESFittingSmootherRKP5'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(0.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(4),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.hltESPBwdAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('hltESPBwdAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
)


process.hltESPBwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPBwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeLooseMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator2000'),
    MaxChi2 = cms.double(2000.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9ForHI'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutForHI')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2ChargeTightMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPChi2MeasurementEstimator100 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator100'),
    MaxChi2 = cms.double(40.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hltESPChi2MeasurementEstimator16 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator30 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPChi2MeasurementEstimator9 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPChi2MeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPCloseComponentsMerger5D = cms.ESProducer("CloseComponentsMergerESProducer5D",
    ComponentName = cms.string('hltESPCloseComponentsMerger5D'),
    DistanceMeasure = cms.string('hltESPKullbackLeiblerDistance5D'),
    MaxComponents = cms.int32(12),
    appendToDataLabel = cms.string('')
)


process.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPDetachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer("PromptTrackCountingESProducer",
    appendToDataLabel = cms.string(''),
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any')
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer("PromptTrackCountingESProducer",
    appendToDataLabel = cms.string(''),
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.2),
    maxImpactParameterSig = cms.double(999999.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any')
)


process.hltESPDisplacedDijethltPromptTrackCountingESProducerShortSig5 = cms.ESProducer("PromptTrackCountingESProducer",
    appendToDataLabel = cms.string(''),
    deltaR = cms.double(-1.0),
    deltaRmin = cms.double(0.0),
    impactParameterType = cms.int32(1),
    maxImpactParameter = cms.double(0.05),
    maxImpactParameterSig = cms.double(5.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(999999.0),
    nthTrack = cms.int32(-1),
    trackQualityClass = cms.string('any')
)


process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    appendToDataLabel = cms.string(''),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.05),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D1stLoose = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    appendToDataLabel = cms.string(''),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.03),
    nthTrack = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(False),
    useVariableJTA = cms.bool(False)
)


process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    appendToDataLabel = cms.string(''),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(1),
    max_pT = cms.double(500.0),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3.0),
    maximumDecayLength = cms.double(999999.0),
    maximumDistanceToJetAxis = cms.double(9999999.0),
    min_pT = cms.double(120.0),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(0.2),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.hltESPDummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPDummyDetLayerGeometry'),
    appendToDataLabel = cms.string('')
)


process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.hltESPElectronMaterialEffects = cms.ESProducer("GsfMaterialEffectsESProducer",
    BetheHeitlerCorrection = cms.int32(2),
    BetheHeitlerParametrization = cms.string('BetheHeitler_cdfmom_nC6_O5.par'),
    ComponentName = cms.string('hltESPElectronMaterialEffects'),
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    Mass = cms.double(0.000511),
    MultipleScatteringUpdator = cms.string('MultipleScatteringUpdator')
)


process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    appendToDataLabel = cms.string(''),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    appendToDataLabel = cms.string(''),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(True)
)


process.hltESPFittingSmootherIT = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPFittingSmootherIT'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFittingSmootherRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPFittingSmootherRK'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPTrajectoryFitterRK'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTrajectorySmootherRK'),
    appendToDataLabel = cms.string('')
)


process.hltESPFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPKFFittingSmootherForLoopers'),
    standardFitter = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK')
)


process.hltESPFwdElectronPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPFwdElectronPropagator'),
    Mass = cms.double(0.000511),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.hltESPGlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('hltESPGlobalDetLayerGeometry'),
    appendToDataLabel = cms.string('')
)


process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.hltESPGsfElectronFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPGsfElectronFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPGsfTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPGsfTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectoryFitter = cms.ESProducer("GsfTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPGsfTrajectoryFitter'),
    GeometricalPropagator = cms.string('hltESPAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    appendToDataLabel = cms.string('')
)


process.hltESPGsfTrajectorySmoother = cms.ESProducer("GsfTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPGsfTrajectorySmoother'),
    ErrorRescaling = cms.double(100.0),
    GeometricalPropagator = cms.string('hltESPBwdAnalyticalPropagator'),
    MaterialEffectsUpdator = cms.string('hltESPElectronMaterialEffects'),
    Merger = cms.string('hltESPCloseComponentsMerger5D'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    appendToDataLabel = cms.string('')
)


process.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2ChargeMeasurementEstimator30'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPInitialStepChi2MeasurementEstimator36'),
    MaxChi2 = cms.double(36.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPIter0PFlowTrackCandidatesMkFitConfig = cms.ESProducer("MkFitIterationConfigESProducer",
    ComponentName = cms.string('hltESPIter0PFlowTrackCandidatesMkFitConfig'),
    appendToDataLabel = cms.string(''),
    config = cms.FileInPath('RecoTracker/MkFit/data/mkfit-phase1-hltiter0.json'),
    maxClusterSize = cms.uint32(8),
    minPt = cms.double(0.0)
)


process.hltESPKFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmoother'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPKFFittingSmootherForL2Muon'),
    EstimateCut = cms.double(-1.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherForLoopers'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('hltESPKFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('hltESPRKTrajectoryFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPRKTrajectorySmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPKFTrajectoryFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForL2Muon'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAnyOpposite'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.hltESPKFUpdator = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string('')
)


process.hltESPKullbackLeiblerDistance5D = cms.ESProducer("DistanceBetweenComponentsESProducer5D",
    ComponentName = cms.string('hltESPKullbackLeiblerDistance5D'),
    DistanceMeasure = cms.string('KullbackLeibler'),
    appendToDataLabel = cms.string('')
)


process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPL3MuKFTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPSmartPropagatorAny'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPLowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hltESPMeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('hltESPMeasurementTracker'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    appendToDataLabel = cms.string(''),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPMixedStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPMixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer("MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
    appendToDataLabel = cms.string('')
)


process.hltESPPFRecHitHCALParams = cms.ESProducer("PFRecHitHCALParamsESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    energyThresholdsHB = cms.vdouble(0.1, 0.2, 0.3, 0.3),
    energyThresholdsHE = cms.vdouble(
        0.1, 0.2, 0.2, 0.2, 0.2,
        0.2, 0.2
    )
)


process.hltESPPFRecHitHCALTopology = cms.ESProducer("PFRecHitHCALTopologyESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    usePFThresholdsFromDB = cms.bool(True)
)


process.hltESPPixelCPEFastParamsHIonPhase1 = cms.ESProducer("PixelCPEFastParamsESProducerAlpakaHIonPhase1@alpaka",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEFastParamsHIonPhase1'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPEFastParamsPhase1 = cms.ESProducer("PixelCPEFastParamsESProducerAlpakaPhase1@alpaka",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEFastParams'),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPEGeneric = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag("",""),
    NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
    SmallPitch = cms.bool(False),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    appendToDataLabel = cms.string(''),
    doLorentzFromAlignment = cms.bool(False),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    isPhase2 = cms.bool(False),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(False),
    xerr_barrel_l1 = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_l1_def = cms.double(0.0103),
    xerr_barrel_ln = cms.vdouble(0.00115, 0.0012, 0.00088),
    xerr_barrel_ln_def = cms.double(0.0103),
    xerr_endcap = cms.vdouble(0.002, 0.002),
    xerr_endcap_def = cms.double(0.002),
    yerr_barrel_l1 = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_l1_def = cms.double(0.0021),
    yerr_barrel_ln = cms.vdouble(
        0.00375, 0.0023, 0.0025, 0.0025, 0.0023,
        0.0023, 0.0021, 0.0021, 0.0024
    ),
    yerr_barrel_ln_def = cms.double(0.0021),
    yerr_endcap = cms.vdouble(0.0021),
    yerr_endcap_def = cms.double(0.00075)
)


process.hltESPPixelCPETemplateReco = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('hltESPPixelCPETemplateReco'),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    appendToDataLabel = cms.string(''),
    barrelTemplateID = cms.int32(0),
    directoryWithTemplates = cms.int32(0),
    doLorentzFromAlignment = cms.bool(False),
    forwardTemplateID = cms.int32(0),
    lAOffset = cms.double(0.0),
    lAWidthBPix = cms.double(0.0),
    lAWidthFPix = cms.double(0.0),
    speed = cms.int32(-2),
    useLAFromDB = cms.bool(True),
    useLAWidthFromDB = cms.bool(True)
)


process.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelLessStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPPixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2ChargeMeasurementEstimator9'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPPixelPairStepChi2MeasurementEstimator25'),
    MaxChi2 = cms.double(25.0),
    MaxDisplacement = cms.double(100.0),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(10.0),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPPixelPairTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPRKTrajectoryFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPRKTrajectorySmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPGlobalDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('hltESPRungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.hltESPSiPixelCablingSoA = cms.ESProducer("SiPixelCablingSoAESProducer@alpaka",
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hltESPSiPixelGainCalibrationForHLTSoA = cms.ESProducer("SiPixelGainCalibrationForHLTSoAESProducer@alpaka",
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string('')
    ),
    appendToDataLabel = cms.string('')
)


process.hltESPSmartPropagator = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagator'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('hltESPSteppingHelixPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    appendToDataLabel = cms.string('')
)


process.hltESPSmartPropagatorAny = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAny'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('alongMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    appendToDataLabel = cms.string('')
)


process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer("SmartPropagatorESProducer",
    ComponentName = cms.string('hltESPSmartPropagatorAnyOpposite'),
    Epsilon = cms.double(5.0),
    MuonPropagator = cms.string('SteppingHelixPropagatorAny'),
    PropagationDirection = cms.string('oppositeToMomentum'),
    TrackerPropagator = cms.string('PropagatorWithMaterialOpposite'),
    appendToDataLabel = cms.string('')
)


process.hltESPSoftLeptonByDistance = cms.ESProducer("LeptonTaggerByDistanceESProducer",
    appendToDataLabel = cms.string(''),
    distance = cms.double(0.5)
)


process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    appendToDataLabel = cms.string(''),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('hltESPSteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    appendToDataLabel = cms.string(''),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.hltESPStripCPEfromTrackAngle = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('hltESPStripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.hltESPTTRHBWithTrackAngle = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBWithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPETemplateReco'),
    StripCPE = cms.string('hltESPStripCPEfromTrackAngle'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderPixelOnly = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderPixelOnly'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('hltESPTTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    Phase2StripCPE = cms.string(''),
    PixelCPE = cms.string('hltESPPixelCPEGeneric'),
    StripCPE = cms.string('Fake'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('hltESPTobTecStepChi2ChargeMeasurementEstimator16'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1.0)
)


process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('hltESPTobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par'),
    PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase1_loose.par'),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('HLTSiStripClusterChargeCutTight')
    ),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    isPhase2 = cms.bool(False)
)


process.hltESPTobTecStepFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmoother'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitter'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    HighEtaSwitch = cms.double(5.0),
    LogPixelProbabilityCut = cms.double(-16.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    MinNumberOfHitsHighEta = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(False),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('hltESPTobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('hltESPTobTecStepFitterSmoother')
)


process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitter'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKFitterForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmoother'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.hltESPTrackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('hltESPTrackAlgoPriorityOrder'),
    algoOrder = cms.vstring(),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackSelectionTfCKF = cms.ESProducer("TfGraphDefProducer",
    ComponentName = cms.string('hltESPTrackSelectionTfCKF'),
    FileName = cms.FileInPath('RecoTracker/FinalTrackSelectors/data/TrackTfClassifier/CKF_Run3_12_5_0_pre5.pb'),
    appendToDataLabel = cms.string('')
)


process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    appendToDataLabel = cms.string(''),
    trackerGeometryLabel = cms.untracked.string(''),
    usePhase2Stacks = cms.bool(False)
)


process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(0.0),
    ValidHitBonus = cms.double(100.0),
    allowSharedFirstHit = cms.bool(False),
    fractionShared = cms.double(0.5)
)


process.hltESPTrajectoryCleanerBySharedHitsP5 = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHitsP5'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.hltESPTrajectoryFitterRK = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('hltESPTrajectoryFitterRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.hltESPTrajectorySmootherRK = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('hltESPTrajectorySmootherRK'),
    Estimator = cms.string('hltESPChi2MeasurementEstimator30'),
    Propagator = cms.string('hltESPRungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('hltESPDummyDetLayerGeometry'),
    Updator = cms.string('hltESPKFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100.0),
    minHits = cms.int32(3)
)


process.hltPixelTracksCleanerBySharedHits = cms.ESProducer("PixelTrackCleanerBySharedHitsESProducer",
    ComponentName = cms.string('hltPixelTracksCleanerBySharedHits'),
    appendToDataLabel = cms.string(''),
    useQuadrupletAlgo = cms.bool(False)
)


process.hltTrackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('hltTrackCleaner'),
    appendToDataLabel = cms.string('')
)


process.hoDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('HODetIdAssociator'),
    etaBinSize = cms.double(0.087),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(30),
    nPhi = cms.int32(72)
)


process.mkFitGeometryESProducer = cms.ESProducer("MkFitGeometryESProducer",
    appendToDataLabel = cms.string('')
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('MuonDetIdAssociator'),
    etaBinSize = cms.double(0.125),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(True),
    includeGEM = cms.bool(True),
    includeME0 = cms.bool(False),
    nEta = cms.int32(48),
    nPhi = cms.int32(48)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    PluginName = cms.string(''),
    SimpleMagneticField = cms.string('ParabolicMf'),
    appendToDataLabel = cms.string('')
)


process.preshowerDetIdAssociator = cms.ESProducer("DetIdAssociatorESProducer",
    ComponentName = cms.string('PreshowerDetIdAssociator'),
    etaBinSize = cms.double(0.1),
    hcalRegion = cms.int32(2),
    includeBadChambers = cms.bool(False),
    includeGEM = cms.bool(False),
    includeME0 = cms.bool(False),
    nEta = cms.int32(60),
    nPhi = cms.int32(30)
)


process.siPixelGainCalibrationForHLTGPU = cms.ESProducer("SiPixelGainCalibrationForHLTGPUESProducer",
    appendToDataLabel = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityFromDbLabel = cms.string('')
)


process.siPixelROCsStatusAndMappingWrapperESProducer = cms.ESProducer("SiPixelROCsStatusAndMappingWrapperESProducer",
    CablingMapLabel = cms.string(''),
    ComponentName = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.zdcTopologyEP = cms.ESProducer("ZdcTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CSCChannelMapperESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCChannelMapperRecord')
)


process.CSCINdexerESSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('CSCIndexerRecord')
)


process.GlobalParametersRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1TGlobalParametersRcd')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    JsonDumpFileName = cms.untracked.string(''),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    frontierKey = cms.untracked.string(''),
    globaltag = cms.string('150X_dataRun3_HLT_v1'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    recordsToDebug = cms.untracked.vstring(),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('HcalPFCutsRcd'),
            tag = cms.string('HcalPFCuts_2025_mc')
        ),
        cms.PSet(
            label = cms.untracked.string('HLT'),
            record = cms.string('PFCalibrationRcd'),
            tag = cms.string('PFCalibration_Run3Winter25_MC_hlt_v1')
        ),
        cms.PSet(
            label = cms.untracked.string('AK4CaloHLT'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Run3Winter25Digi_AK4CaloHLT_v2')
        ),
        cms.PSet(
            label = cms.untracked.string('AK8CaloHLT'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Run3Winter25Digi_AK8CaloHLT_v2')
        ),
        cms.PSet(
            label = cms.untracked.string('AK4PFHLT'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Run3Winter25Digi_AK4PFHLT_v2')
        ),
        cms.PSet(
            label = cms.untracked.string('AK8PFHLT'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Run3Winter25Digi_AK8PFHLT_v2')
        )
    )
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.hltESSBTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.hltESSEcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalSeverityLevelAlgoRcd')
)


process.hltESSHcalSeverityLevel = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('HcalSeverityLevelComputerRcd')
)


process.hltESSPFRecHitHCALParamsRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('PFRecHitHCALParamsRecord')
)


process.hltESSPFRecHitHCALTopologyRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('PFRecHitHCALTopologyRecord')
)


process.hltESSTfGraphRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('TfGraphRecord')
)


process.ppsPixelTopologyESSource = cms.ESSource("PPSPixelTopologyESSource",
    PitchSimX = cms.double(0.1),
    PitchSimY = cms.double(0.15),
    RunType = cms.string('Run3'),
    activeEdgeSigma = cms.double(0.02),
    appendToDataLabel = cms.string(''),
    deadEdgeWidth = cms.double(0.2),
    noOfPixelSimX = cms.int32(160),
    noOfPixelSimY = cms.int32(104),
    noOfPixels = cms.int32(16640),
    physActiveEdgeDist = cms.double(0.15),
    simXWidth = cms.double(16.6),
    simYWidth = cms.double(16.2),
    thickness = cms.double(0.23)
)


process.HLTL1UnpackerSequence = cms.Sequence(process.hltGtStage2Digis+process.hltGtStage2ObjectMap)


process.HLTBeamSpot = cms.Sequence(process.hltOnlineMetaDataDigis+process.hltOnlineBeamSpot)


process.HLTBeginSequence = cms.Sequence(process.hltTriggerType+process.HLTL1UnpackerSequence+process.HLTBeamSpot)


process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence(process.hltEcalDigisLegacy+process.hltEcalDigisSoA+process.hltEcalDigis+process.hltEcalUncalibRecHitSoA+process.hltEcalUncalibRecHit+process.hltEcalDetIdToBeRecovered+process.hltEcalRecHit)


process.HLTPreshowerSequence = cms.Sequence(process.hltEcalPreshowerDigis+process.hltEcalPreshowerRecHit)


process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence+process.HLTPreshowerSequence)


process.HLTPFClusteringForEgamma = cms.Sequence(process.hltRechitInRegionsECAL+process.hltRechitInRegionsES+process.hltParticleFlowRecHitECALL1Seeded+process.hltParticleFlowRecHitPSL1Seeded+process.hltParticleFlowClusterPSL1Seeded+process.hltParticleFlowClusterECALUncorrectedL1Seeded+process.hltParticleFlowClusterECALL1Seeded+process.hltParticleFlowSuperClusterECALL1Seeded)


process.HLTDoLocalHcalSequence = cms.Sequence(process.hltHcalDigis+process.hltHcalDigisSoA+process.hltHbheRecoSoA+process.hltHbhereco+process.hltHfprereco+process.hltHfreco+process.hltHoreco)


process.HLTFastJetForEgamma = cms.Sequence(process.hltFixedGridRhoFastjetAllCaloForMuons)


process.HLTDoLocalPixelSequence = cms.Sequence(process.hltOnlineBeamSpotDevice+process.hltSiPixelClustersSoA+process.hltSiPixelClusters+process.hltSiPixelDigiErrors+process.hltSiPixelRecHitsSoA+process.hltSiPixelRecHits)


process.HLTDoLocalStripSequence = cms.Sequence(process.hltSiStripExcludedFEDListProducer+process.hltSiStripRawToClustersFacility+process.hltMeasurementTrackerEvent)


process.HLTElePixelMatchSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltPixelLayerPairs+process.hltPixelLayerTriplets+process.hltEgammaHoverE+process.hltEgammaSuperClustersToPixelMatch+process.hltEleSeedsTrackingRegions+process.hltElePixelHitDoublets+process.hltElePixelHitDoubletsForTriplets+process.hltElePixelHitTriplets+process.hltElePixelSeedsDoublets+process.hltElePixelSeedsTriplets+process.hltElePixelSeedsCombined+process.hltEgammaElectronPixelSeeds+process.hltEgammaPixelMatchVars)


process.HLTEle33CaloIdLSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter+process.hltEG33EtFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG33HEFilter+process.hltEgammaClusterShape+process.hltEG33CaloIdLClusterShapeFilter+process.HLTElePixelMatchSequence+process.hltEle33CaloIdLPixelMatchFilter)


process.HLTEle33CaloIdLMWSequence = cms.Sequence(process.HLTEle33CaloIdLSequence+process.hltEle33CaloIdLMWPMS2Filter)


process.HLTPFClusteringForEgammaUnseeded = cms.Sequence(process.hltParticleFlowRecHitECALUnseeded+process.hltParticleFlowRecHitPSUnseeded+process.hltParticleFlowClusterPSUnseeded+process.hltParticleFlowClusterECALUncorrectedUnseeded+process.hltParticleFlowClusterECALUnseeded+process.hltParticleFlowSuperClusterECALUnseeded)


process.HLTElePixelMatchUnseededSequence = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTDoLocalStripSequence+process.hltPixelLayerPairs+process.hltPixelLayerTriplets+process.hltEgammaHoverEUnseeded+process.hltEgammaSuperClustersToPixelMatchUnseeded+process.hltEleSeedsTrackingRegionsUnseeded+process.hltElePixelHitDoubletsUnseeded+process.hltElePixelHitDoubletsForTripletsUnseeded+process.hltElePixelHitTripletsUnseeded+process.hltElePixelSeedsDoubletsUnseeded+process.hltElePixelSeedsTripletsUnseeded+process.hltElePixelSeedsCombinedUnseeded+process.hltEgammaElectronPixelSeedsUnseeded+process.hltEgammaPixelMatchVarsUnseeded)


process.HLTDoubleEle33CaloIdLUnseededSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgammaUnseeded+process.hltEgammaCandidatesUnseeded+process.hltEgammaCandidatesWrapperUnseeded+process.hltDiEG33EtUnseededFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverEUnseeded+process.hltDiEG33HEUnseededFilter+process.hltEgammaClusterShapeUnseeded+process.hltDiEG33CaloIdLClusterShapeUnseededFilter+process.HLTElePixelMatchUnseededSequence+process.hltDiEle33CaloIdLPixelMatchUnseededFilter)


process.HLTDoubleEle33CaloIdLMWSequence = cms.Sequence(process.HLTDoubleEle33CaloIdLUnseededSequence+process.hltDiEle33CaloIdLMWPMS2UnseededFilter)


process.HLTEndSequence = cms.Sequence(process.hltBoolEnd)


process.HLTPFHcalClustering = cms.Sequence(process.hltParticleFlowRecHitHBHESoA+process.hltParticleFlowRecHitHBHE+process.hltParticleFlowClusterHBHESoA+process.hltParticleFlowClusterHBHE+process.hltParticleFlowClusterHCAL)


process.HLTGsfElectronSequence = cms.Sequence(process.hltEgammaCkfTrackCandidatesForGSF+process.hltEgammaGsfTracks+process.hltEgammaGsfElectrons+process.hltEgammaGsfTrackVars)


process.HLTRecoPixelTracksSequence = cms.Sequence(process.hltPixelTracksSoA+process.hltPixelTracks)


process.HLTRecopixelvertexingSequence = cms.Sequence(process.HLTRecoPixelTracksSequence+process.hltPixelVerticesSoA+process.hltPixelVertices+process.hltTrimmedPixelVertices)


process.HLTIterativeTrackingIteration0 = cms.Sequence(process.hltIter0PFLowPixelSeedsFromPixelTracks+process.hltIter0PFlowCkfTrackCandidatesMkFitSiPixelHits+process.hltSiStripRecHits+process.hltIter0PFlowCkfTrackCandidatesMkFitSiStripHits+process.hltIter0PFlowCkfTrackCandidatesMkFitEventOfHits+process.hltIter0PFlowCkfTrackCandidatesMkFitSeeds+process.hltIter0PFlowCkfTrackCandidatesMkFit+process.hltIter0PFlowCkfTrackCandidates+process.hltIter0PFlowCtfWithMaterialTracks+process.hltIter0PFlowTrackCutClassifier+process.hltIter0PFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingDoubletRecovery = cms.Sequence(process.hltDoubletRecoveryClustersRefRemoval+process.hltDoubletRecoveryMaskedMeasurementTrackerEvent+process.hltDoubletRecoveryPixelLayersAndRegions+process.hltDoubletRecoveryPFlowPixelClusterCheck+process.hltDoubletRecoveryPFlowPixelHitDoublets+process.hltDoubletRecoveryPFlowPixelSeeds+process.hltDoubletRecoveryPFlowCkfTrackCandidates+process.hltDoubletRecoveryPFlowCtfWithMaterialTracks+process.hltDoubletRecoveryPFlowTrackCutClassifier+process.hltDoubletRecoveryPFlowTrackSelectionHighPurity)


process.HLTIterativeTrackingIter02 = cms.Sequence(process.HLTIterativeTrackingIteration0+process.HLTIterativeTrackingDoubletRecovery+process.hltMergedTracks)


process.HLTTrackReconstructionForPFNoMu = cms.Sequence(process.HLTDoLocalPixelSequence+process.HLTRecopixelvertexingSequence+process.HLTDoLocalStripSequence+process.HLTIterativeTrackingIter02)


process.HLTTrackReconstructionForIsoElectronIter02 = cms.Sequence(process.HLTTrackReconstructionForPFNoMu)


process.HLTEle30WPTightGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGOrFilter+process.hltEG30L1SingleEGOrEtFilter+process.hltEgammaClusterShape+process.hltEle30WPTightClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle30WPTightHEFilter+process.hltEgammaEcalPFClusterIsoDr0p2+process.hltEle30WPTightEcalIsoFilter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle30WPTightHcalIsoFilter+process.HLTElePixelMatchSequence+process.hltEle30WPTightPixelMatchFilter+process.hltEle30WPTightPMS2Filter+process.HLTGsfElectronSequence+process.hltEle30WPTightGsfOneOEMinusOneOPFilter+process.hltEle30WPTightGsfMissingHitsFilter+process.hltEle30WPTightGsfDetaFilter+process.hltEle30WPTightGsfDphiFilter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle30WPTightGsfTrackIsoFilter)


process.HLTEle32WPTightGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGOrFilter+process.hltEG32L1SingleEGOrEtFilter+process.hltEgammaClusterShape+process.hltEle32WPTightClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle32WPTightHEFilter+process.hltEgammaEcalPFClusterIsoDr0p2+process.hltEle32WPTightEcalIsoFilter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle32WPTightHcalIsoFilter+process.HLTElePixelMatchSequence+process.hltEle32WPTightPixelMatchFilter+process.hltEle32WPTightPMS2Filter+process.HLTGsfElectronSequence+process.hltEle32WPTightGsfOneOEMinusOneOPFilter+process.hltEle32WPTightGsfMissingHitsFilter+process.hltEle32WPTightGsfDetaFilter+process.hltEle32WPTightGsfDphiFilter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle32WPTightGsfTrackIsoFilter)


process.HLTEle23Ele12CaloIdLTrackIdLIsoVLSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleAndDoubleEGOrPairFilter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter+process.hltEgammaClusterShape+process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter+process.hltEgammaEcalPFClusterIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter+process.HLTPFHcalClustering+process.hltEgammaHcalPFClusterIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter+process.HLTElePixelMatchSequence+process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter+process.HLTGsfElectronSequence+process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter+process.HLTTrackReconstructionForIsoElectronIter02+process.hltEgammaEleGsfTrackIso+process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter+process.hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter)


process.HLTEle115CaloIdVTGsfTrkIdTGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter+process.hltEG115EtFilter+process.hltEgammaClusterShape+process.hltEG115CaloIdVTClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG115CaloIdVTHEFilter+process.HLTElePixelMatchSequence+process.hltEle115CaloIdVTPixelMatchFilter+process.HLTGsfElectronSequence+process.hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter+process.hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter)


process.HLTEle135CaloIdVTGsfTrkIdTGsfSequence = cms.Sequence(process.HLTDoFullUnpackingEgammaEcalSequence+process.HLTPFClusteringForEgamma+process.hltEgammaCandidates+process.hltEGL1SingleEGNonIsoOrWithJetAndTauFilter+process.hltEG135EtFilter+process.hltEgammaClusterShape+process.hltEG135CaloIdVTClusterShapeFilter+process.HLTDoLocalHcalSequence+process.HLTFastJetForEgamma+process.hltEgammaHoverE+process.hltEG135CaloIdVTHEFilter+process.HLTElePixelMatchSequence+process.hltEle135CaloIdVTPixelMatchFilter+process.HLTGsfElectronSequence+process.hltEle135CaloIdVTGsfTrkIdTGsfDetaFilter+process.hltEle135CaloIdVTGsfTrkIdTGsfDphiFilter)


process.HLTriggerFirstPath = cms.Path(process.hltGetRaw+process.hltPSetMap+process.hltBoolFalse)


process.HLT_DoubleEle33_CaloIdL_MW_v30 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleAndDoubleEGNonIsoOrWithEG26WithJetAndTau+process.hltPreDoubleEle33CaloIdLMW+process.HLTEle33CaloIdLMWSequence+process.HLTDoubleEle33CaloIdLMWSequence+process.HLTEndSequence)


process.HLT_Ele30_WPTight_Gsf_v13 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleEGor+process.hltPreEle30WPTightGsf+process.HLTEle30WPTightGsfSequence+process.HLTEndSequence)


process.HLT_Ele32_WPTight_Gsf_v27 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleEGor+process.hltPreEle32WPTightGsf+process.HLTEle32WPTightGsfSequence+process.HLTEndSequence)


process.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleAndDoubleEG+process.hltPreEle23Ele12CaloIdLTrackIdLIsoVL+process.HLTEle23Ele12CaloIdLTrackIdLIsoVLSequence+process.HLTEndSequence)


process.HLT_Ele115_CaloIdVT_GsfTrkIdT_v27 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleEGNonIsoOrWithJetAndTau+process.hltPreEle115CaloIdVTGsfTrkIdT+process.HLTEle115CaloIdVTGsfTrkIdTGsfSequence+process.HLTEndSequence)


process.HLT_Ele135_CaloIdVT_GsfTrkIdT_v20 = cms.Path(process.HLTBeginSequence+process.hltL1sSingleEGNonIsoOrWithJetAndTau+process.hltPreEle135CaloIdVTGsfTrkIdT+process.HLTEle135CaloIdVTGsfTrkIdTGsfSequence+process.HLTEndSequence)


process.HLTriggerFinalPath = cms.Path(process.hltGtStage2Digis+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)


process.DQMOutput = cms.EndPath(process.dqmOutput)


process.schedule = cms.Schedule(*[ process.HLTriggerFirstPath, process.HLT_DoubleEle33_CaloIdL_MW_v30, process.HLT_Ele30_WPTight_Gsf_v13, process.HLT_Ele32_WPTight_Gsf_v27, process.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v31, process.HLT_Ele115_CaloIdVT_GsfTrkIdT_v27, process.HLT_Ele135_CaloIdVT_GsfTrkIdT_v20, process.HLTriggerFinalPath, process.DQMOutput ])

