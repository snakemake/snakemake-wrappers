__author__ = "Anfeng Li"
__copyright__ = "Copyright 2024, Anfeng Li"
__email__ = "anfeng.li@cern.ch"
__license__ = "MIT"


import ROOT

ROOT.EnableImplicitMT(snakemake.threads)

redefine_list = snakemake.params.get("redefine", [])
branches = snakemake.params.get("branches", [])
branches_to_save = snakemake.params.get("branches_to_save", None)

df = ROOT.RDataFrame(snakemake.params.input_tree_name, snakemake.input[0])
for branch_name, branch_definition in branches:
    if branch_name in redefine_list:
        df = df.Redefine(branch_name, branch_definition)
    else:
        df = df.Define(branch_name, branch_definition)
if branches_to_save is not None:
    df.Snapshot(
        snakemake.params.output_tree_name,
        snakemake.output[0],
        branches_to_save,
    )
else:
    df.Snapshot(snakemake.params.output_tree_name, snakemake.output[0])
