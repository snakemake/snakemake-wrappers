__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

pipe = ""
if snakemake.output[0].endswith(".bcf"):
    pipe = "| bcftools view -Ob -"

shell("(freebayes {snakemake.params} -f {snakemake.input.ref} "
      " {snakemake.input.samples} {pipe} > {snakemake.output[0]}) {log}")
