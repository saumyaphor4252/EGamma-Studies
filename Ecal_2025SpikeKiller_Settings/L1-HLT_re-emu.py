# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test -s RAW2DIGI,L1REPACK:FullSimTP,HLT --conditions 140X_dataRun3_HLT_v3 --python_filename=L1-HLT_re-emu.py --filein /eos/cms/store/data/Run2024I/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/ff6e1a65-1120-433e-845b-b5f2d87b7dc8.root --customise=L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML --customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2024_v0_3 --geometry DB:Extended --era Run3_2024 --data --processName=MYHLT -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2024_cff import Run3_2024

process = cms.Process('MYHLT',Run3_2024)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorRepack_FullSimTP_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/eos/cms/store/data/Run2024I/EGamma0/RAW-RECO/ZElectron-PromptReco-v1/000/386/509/00000/ff6e1a65-1120-433e-845b-b5f2d87b7dc8.root'),
    secondaryFileNames = cms.untracked.vstring()
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
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('test_RAW2DIGI_L1REPACK_HLT.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_HLT_v3', '')

#process.GlobalTag.toGet = cms.VPSet(
#    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),
#        tag = cms.string('EcalTPGSpike_16'),
#        tag = cms.string('EcalTPGSpike_14'),
#        connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#    ),
#    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
#    tag = cms.string('EcalTPGFineGrainStrip_28'),
#    tag = cms.string('EcalTPGFineGrainStrip_26'),
#    connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#    )
#)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1RePack_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.raw2digi_step)
process.schedule.insert(1, process.L1RePack_step)
process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseUtils
from L1Trigger.Configuration.customiseUtils import L1TGlobalMenuXML 

#call to customisation function L1TGlobalMenuXML imported from L1Trigger.Configuration.customiseUtils
process = L1TGlobalMenuXML(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2024_v0_3 

#call to customisation function L1TSettingsToCaloParams_2024_v0_3 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2024_v0_3(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
process.load('L1Trigger.L1TGlobal.simGtStage2Digis_cfi')
process.load('L1Trigger.L1TGlobal.hackConditions_cff')
process.L1TGlobalPrescalesVetosFract.PrescaleXMLFile = cms.string('UGT_BASE_RS_PRESCALES_L1Menu_Collisions2024_v1_3_0.xml')
process.L1TGlobalPrescalesVetosFract.FinOrMaskXMLFile = cms.string('UGT_BASE_RS_FINOR_MASK_L1MenuCollisions2023_v1_3_0.xml')
process.simGtStage2Digis.AlgorithmTriggersUnmasked = cms.bool(False)
process.simGtStage2Digis.AlgorithmTriggersUnprescaled = cms.bool(False)
process.simGtStage2Digis.PrescaleSet = cms.uint32(7)
process.simGtStage2Digis.resetPSCountersEachLumiSec = cms.bool(False)
process.simGtStage2Digis.semiRandomInitialPSCounters = cms.bool(True)
