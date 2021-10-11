__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

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
            "There must be a named input file for every resource (missing: {})".format(
                resname
            )
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
tranches = ""
if snakemake.output.tranches:
    tranches = "--tranches-file " + snakemake.output.tranches

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' VariantRecalibrator {extra} {annotation_resources} "
    "-R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "-mode {snakemake.params.mode} "
    "--output {snakemake.output.vcf} "
    "{tranches} {annotation} {log}"
)
