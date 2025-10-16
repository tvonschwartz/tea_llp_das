# The number of events to process. -1 means all events.
nEvents = -1

base_path = "/eos/cms/store/group/committee_schools/2025-cmsdas-hamburg/llp/samples/"

#process = "background_ttsemileptonic"
process = "tta_mAlp-12GeV_ctau-1e2mm"

inputFilePath = f"{base_path}/{process}/output_0.root"
histogramsOutputFilePath = f"../histograms/{process}/after_selections.root"

defaultHistParams = (
  #  collection      variable          bins    xmin     xmax     dir
  ("Event", "nMuon", 50, 0, 50, ""),
  ("Muon", "pt", 400, 0, 200, ""),
  ("Muon", "eta", 100, -2.5, 2.5, ""),
)

# Here, we define a custom histogram for the invariant mass of the best dimuon candidate.
# Dimuon_minv is not a standard nanoAOD collection, so we will have to fill this one manually in a C++ program.
histParams = (
  # collection      variable          bins    xmin     xmax     dir
  # TODO: create a histogram for the invariant mass of the best dimuon candidate
  # TODO: add other needed histograms
  ("Dimuon", "minv", 400, 0, 200, ""),
  ("Dimuon", "logLxy", 100, 0, 5, ""),
)

# Collections defined here can be used in other parts of the python configs, and in the C++ code.
extraEventCollections = {
  "TightMuons": {
    "inputCollections": ["Muon"],
    "pt": (30., 9999999.),
    "eta": (-2.4, 2.4),
    "pfRelIso04_all": (0., 0.15),
    "tightId": True,
  },
  "LooseMuons": {
    "inputCollections": ["Muon"],
    # TODO: define selection criteria for loose muons.
    "pt": (3., 9999999.),
    "eta": (-2.5, 2.5),
    "looseId": True,
  },
  "LooseElectrons": {
    "inputCollections": ("Electron", ),
    "pt": (15., 9999999.),
    "eta": (-2.5, 2.5),
    "mvaFall17V2Iso_WPL": True,
  },
}

# These event selections can be applied to standard nanoAOD branches and custom collections defined above.
eventCuts = {
  "MET_pt": (50, 9999999),
  "nTightMuons": (1, 9999999),
  # TODO: add more cuts here
  "nLooseMuons": (3, 9999999),
  "nLooseElectrons": (-1, 0),
}

weightsBranchName = "genWeight"
eventsTreeNames = ["Events"]

specialBranchSizes = {
    "Proton_multiRP": "nProton_multiRP",
    "Proton_singleRP": "nProton_singleRP",
}
