__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")
# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and not "-Djava.io.tmpdir" in java_opts:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])


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
    return "{},known={},training={},truth={},prior={}:{}".format(
        resname,
        fmt_bool(resparams["known"]),
        fmt_bool(resparams["training"]),
        fmt_bool(resparams["truth"]),
        resparams["prior"],
        f,
    )


resources = [
    "--resource {}".format(fmt_res(resname, resparams))
    for resname, resparams in snakemake.params["resources"].items()
]
annotation = list(map("-an {}".format, snakemake.params.annotation))
tranches = ""
if snakemake.output.tranches:
    tranches = "--tranches-file " + snakemake.output.tranches

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' VariantRecalibrator {extra} {resources} "
    "-R {snakemake.input.ref} -V {snakemake.input.vcf} "
    "-mode {snakemake.params.mode} "
    "--output {snakemake.output.vcf} "
    "{tranches} {annotation} {log}"
)
