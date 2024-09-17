__author__ = "Anfeng Li, Jamie Gooding"
__copyright__ = "Copyright 2024, Anfeng Li"
__email__ = "anfeng.li@cern.ch, jamie.gooding@cern.ch"
__license__ = "MIT"

from typing import Dict, List
import ROOT

ROOT.EnableImplicitMT(snakemake.threads)

# Parse criteria
_smk_criteria = snakemake.params.get("criteria", "true")
if isinstance(_smk_criteria, str):
    criteria = [_smk_criteria]
    labels = [_smk_criteria]
elif isinstance(_smk_criteria, List):
    criteria = _smk_criteria
    labels = _smk_criteria
elif isinstance(_smk_criteria, Dict):
    criteria, labels = _smk_criteria.items()
else:
    raise TypeError("Parameter 'criteria' should be type of 'str', 'list' or 'dict'")

branches_to_save = snakemake.params.get("branches_to_save", None)

df = ROOT.RDataFrame(snakemake.params.input_tree_name, snakemake.input[0])
for criterion, label in zip(criteria, labels):
    df = df.Filter(criterion, label)
if branches_to_save is not None:
    df.Snapshot(
        snakemake.params.output_tree_name,
        snakemake.output[0],
        branches_to_save,
    )
else:
    df.Snapshot(snakemake.params.output_tree_name, snakemake.output[0])

if snakemake.params.get("verbose", False):
    report = df.Report()
    report.Print()