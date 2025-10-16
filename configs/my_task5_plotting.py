import ROOT
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

luminosity = 63670.  # pb^-1 (2018)

samples = (
  Sample(
    name="mc",
    #file_path="/afs/cern.ch/user/t/tvonschw/tea_llp_das/Outputs/output_task1_bkg.root",  # your path should go here
    file_path="/afs/cern.ch/user/t/tvonschw/tea_llp_das/histograms/background_ttsemileptonic/ttCR.root",
    type=SampleType.background,
    cross_section=365.34,
    line_alpha=1.0,
    line_color=ROOT.kRed - 2,
    fill_color=ROOT.kRed - 2,
    fill_alpha=0.7,
    marker_size=0.0,
    legend_description="MC",
  ),
  Sample(
    name="data",
    #file_path="/afs/cern.ch/user/t/tvonschw/tea_llp_das/Outputs/output_task1_signal.root",  # your path should go here
    file_path="/afs/cern.ch/user/t/tvonschw/tea_llp_das/histograms/collision_data_2018/ttCR.root",
    type=SampleType.data,
    cross_section=1.0,
    line_alpha=1,
    line_style=1,
    fill_alpha=0,
    marker_size=1,
    marker_style=8,
    line_color=ROOT.kBlack,
    legend_description="Data",
  ),
)
output_path = "/afs/cern.ch/user/t/tvonschw/tea_llp_das/Outputs/"

histograms = (
  #         name      title logx   logy   norm_type                  rebin  xmin  xmax ymin   ymax xlabel         ylabel
  Histogram("TightMuons_pt" , "", False, True , NormalizationType.to_data, 5,     30   , 200, 1    , 1e2, "#p_{T} [GeV]", "#Events"),
  Histogram("TightMuons_eta", "", False, False, NormalizationType.to_data, 2,     -3., 3., 0    , 50, r"\eta", "#Events"),
  Histogram("GoodJets_pt" , "", False, True , NormalizationType.to_data, 5,     30   , 250, 1    , 400, "#p_{T} [GeV]", "#Events"),
  Histogram("GoodJets_eta", "", False, False, NormalizationType.to_data, 2,     -3., 3., 0    , 350, r"\eta", "#Events"),
)

legends = {
  SampleType.background: Legend(0.5, 0.8, 0.78, 0.85, "f"),
  SampleType.data: Legend(0.5, 0.7, 0.78, 0.75, "l"),
}

plotting_options = {
  SampleType.background: "hist",
  SampleType.signal: "nostack hist",
  SampleType.data: "nostack pe",
}

canvas_size = (800, 600)

show_ratio_plots = True
ratio_limits = (0.7, 1.3)
