__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
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


uncompressed_bcf = snakemake.params.get("uncompressed_bcf", False)


out_name, out_ext = path.splitext(snakemake.output[0])
if out_ext == ".vcf":
    out_format = "v"
elif out_ext == ".bcf":
    if uncompressed_bcf:
        out_format = "u"
    else:
        out_format = "b"
elif out_ext == ".gz":
    out_name, out_ext = path.splitext(out_name)
    if out_ext == ".vcf":
        out_format = "z"
    else:
        raise ValueError("output file with invalid extension (.vcf, .vcf.gz, .bcf).")
else:
    raise ValueError("output file with invalid extension (.vcf, .vcf.gz, .bcf).")


shell(
    "bcftools sort {max_mem} {tmp_dir} {extra} --output-type {out_format} --output-file {snakemake.output[0]} {snakemake.input[0]} {log}"
)
