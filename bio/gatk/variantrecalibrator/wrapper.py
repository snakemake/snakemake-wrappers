__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")


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
resources = " ".join(resources)
annotation = " ".join(list(map("-an {}".format, snakemake.params.annotation)))
tranches = ""
if snakemake.output.tranches:
    tranches = "--tranches-file " + snakemake.output.tranches

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
os.system(
    f"gatk --java-options '{java_opts}' VariantRecalibrator {extra} {resources} "
    f"-R {snakemake.input.ref} -V {snakemake.input.vcf} "
    f"-mode {snakemake.params.mode} "
    f"--output {snakemake.output.vcf} "
    f"{tranches} {annotation} {log}"
)
