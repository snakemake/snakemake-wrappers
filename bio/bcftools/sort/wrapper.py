__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

max_mem = snakemake.resources.get("mem_mb", "")
if max_mem:
    max_mem = "--max-mem {}M".format(max_mem)
else:
    max_mem = snakemake.resources.get("mem_gb", "")
    if max_mem:
        max_mem = "--max-mem {}G".format(max_mem)
    else:
        max_mem = ""

tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    tmp_dir = "--temp-dir {}".format(tmp_dir)
else:
    tmp_dir = ""


shell(
    "bcftools sort {max_mem} {tmp_dir} {extra} --output-file {snakemake.output[0]} {snakemake.input[0]} {log}"
)
