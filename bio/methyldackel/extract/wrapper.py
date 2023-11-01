#!/bin/env python3
# coding: utf-8

from snakemake import shell
from tempfile import TemporaryDirectory


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")
extension = "bedGraph"
if "fraction" in extra:
    extension = "meth.bedGraph"
elif "counts" in extra:
    extension = "counts.bedGraph"
elif "logit" in extra:
    extension = "logit.bedGraph"

# Input files
bed = snakemake.input.get("bed", "")
if bed:
    extra += f" -l {bed} "


bw = snakemake.input.get("bw", "")
if bw:
    extra += f" --mappability {bw} "


bbm_in = snakemake.input.get("bbm", "")
if bbm_in:
    extra += f" --mappabilityBB {bbm_in}"


# Output files
chg = snakemake.output.get("chg")
if chg:
    extra += " --CHG "


chh = snakemake.output.get("chh")
if chh:
    extra += " --CHH "


methylkit = snakemake.output.get("methylkit")
if methylkit:
    extra += " --methylKit "
    extension = "methylKit"


report = snakemake.output.get("cytosine_report")
if report:
    extra += " --cytosine_report "


if not (snakemake.output.get("cpg") or report):
    extra += " --noCpG "

with TemporaryDirectory() as tempdir:
    shell(
        "MethylDackel extract "
        "{extra} "
        "-@ {snakemake.threads} "
        "--opref {tempdir}/methyldackel_results "
        "{snakemake.input.ref} "
        "{snakemake.input.aln} "
        "{log} "
    )

    if report:
        shell(
            "mv --verbose {tempdir}/methyldackel_results.cytosine_report.txt {report} {log}"
        )
    else:
        if snakemake.output.get("cpg"):
            shell(
                "mv --verbose {tempdir}/methyldackel_results_CpG.{extension} {snakemake.output.cpg} {log}"
            )

        if chg:
            shell(
                "mv --verbose {tempdir}/methyldackel_results_CHG.{extension} {chg} {log}"
            )

        if chh:
            shell(
                "mv --verbose {tempdir}/methyldackel_results_CHH.{extension} {chh} {log}"
            )
