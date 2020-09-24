__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

mem_mb = snakemake.resources.get("mem_mb", "")
if mem_mb:
    mem_mb = "--max-mem {}M".format(mem_mb)
else:
    mem_mb = ""

tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    tmp_dir = "--temp-dir {}".format(tmp_dir)
else:
    tmp_dir = ""


shell("bcftools sort {mem_mb} {tmp_dir} {extra} -o {snakemake.output[0]} {snakemake.input[0]} {log}")
