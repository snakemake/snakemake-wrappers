__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

threads = "" if snakemake.threads <= 1 else "--threads {}".format(snakemake.threads - 1)


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
    "bcftools concat {threads} {snakemake.params} --output-type {out_format} -o {snakemake.output[0]} "
    "{snakemake.input.calls} "
    "{log}"
)
