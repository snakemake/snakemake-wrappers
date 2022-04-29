__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


def fmt_res(resname, resparams):
    fmt_bool = lambda b: str(b).lower()
    try:
        f = snakemake.input.get(resname)
    except KeyError:
        raise RuntimeError(
            f"There must be a named input file for every resource (missing: {resname})"
        )
    return "{},known={},training={},truth={},prior={} {}".format(
        resname,
        fmt_bool(resparams["known"]),
        fmt_bool(resparams["training"]),
        fmt_bool(resparams["truth"]),
        resparams["prior"],
        f,
    )


annotation_resources = [
    "--resource:{}".format(fmt_res(resname, resparams))
    for resname, resparams in snakemake.params["resources"].items()
]

annotation = list(map("-an {}".format, snakemake.params.annotation))

tranches = snakemake.output.get("tranches", "")
if tranches:
    tranches = f"--tranches-file {tranches}"

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' VariantRecalibrator"
        " --variant {snakemake.input.vcf}"
        " --reference {snakemake.input.ref}"
        " --mode {snakemake.params.mode}"
        " {annotation_resources}"
        " {tranches}"
        " {annotation}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
