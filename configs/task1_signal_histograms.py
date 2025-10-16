# The number of events to process. -1 means all events.
nEvents = -1

base_path = "/eos/cms/store/group/committee_schools/2025-cmsdas-hamburg/llp/samples/"

# Fill in these paths. The output path must be some directory where you can write - I recommend that you store it inside of your project directory.
inputFilePath = f"{base_path}/tta_mAlp-12GeV_ctau-1e2mm/output_0.root"
histogramsOutputFilePath = "/afs/cern.ch/user/t/tvonschw/tea_llp_das/Outputs/output_task1_signal.root"

# You'll need to add some histogram parameters here.
defaultHistParams = (
  #  collection      variable          bins    xmin     xmax     dir
  ("Event", "nMuon", 50, 0, 50, ""),
  ("Muon", "pt", 200, 0, 200, ""),
  ("Muon", "eta", 100, -2.5, 2.5, ""),

)

# No need to change this - this is the branch name for event weights in nanoAOD.
weightsBranchName = "genWeight"
