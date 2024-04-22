__author__ = "Anfeng Li"
__copyright__ = "Copyright 2024, Anfeng Li"
__email__ = "anfeng.li@cern.ch"
__license__ = "MIT"


import ROOT

ROOT.EnableImplicitMT(snakemake.threads)

redefine_list = snakemake.params.get("redefine", [])
input_tree_name = snakemake.params.get("input_tree_name", "")
output_tree_name = snakemake.params.get("output_tree_name", "")
branches = snakemake.params.get("branches", [])
branches_to_save = snakemake.params.get("branches_to_save", None)

for i in range(len(snakemake.input)):
    df = ROOT.RDataFrame(snakemake.params.input_tree_name, snakemake.input[i])
    for branch_name, branch_definition in branches:
        if branch_name in redefine_list:
            df = df.Redefine(branch_name, branch_definition)
        else:
            df = df.Define(branch_name, branch_definition)
    if branches_to_save is not None:
        df.Snapshot(
            output_tree_name,
            snakemake.output[i],
            branches_to_save,
        )
    else:
        df.Snapshot(output_tree_name, snakemake.output[i])
