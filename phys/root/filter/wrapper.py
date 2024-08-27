__author__ = "Anfeng Li"
__copyright__ = "Copyright 2024, Anfeng Li"
__email__ = "anfeng.li@cern.ch"
__license__ = "MIT"


import ROOT

ROOT.EnableImplicitMT(snakemake.threads)

criteria = snakemake.params.get("criteria", "true")
branches_to_save = snakemake.params.get("branches_to_save", None)

df = ROOT.RDataFrame(snakemake.params.input_tree_name, snakemake.input[0])
df = df.Filter(criteria)
if branches_to_save is not None:
    df.Snapshot(
        snakemake.params.output_tree_name,
        snakemake.output[0],
        branches_to_save,
    )
else:
    df.Snapshot(snakemake.params.output_tree_name, snakemake.output[0])
