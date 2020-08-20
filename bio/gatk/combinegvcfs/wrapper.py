__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")
gvcfs = " ".join(list(map("-V {}".format, snakemake.input.gvcfs)))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
os.system(
    f"gatk --java-options '{java_opts}' CombineGVCFs {extra} "
    f"{gvcfs} "
    f"-R {snakemake.input.ref} "
    f"-O {snakemake.output.gvcf} {log}"
)
