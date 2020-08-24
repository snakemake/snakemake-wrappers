__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


from snakemake.shell import shell

## Extract arguments
header = snakemake.input.get("header", "")
if header:
    header_cmd = "-h " + header
else:
    header_cmd = ""

samples = snakemake.input.get("samples", "")
if samples:
    samples_cmd = "-s " + samples
else:
    samples_cmd = ""

extra = snakemake.params.get("extra", "")
view_extra = snakemake.params.get("view_extra", "")

shell(
    "bcftools reheader "
    "{extra} "
    "{header_cmd} "
    "{samples_cmd} "
    "{snakemake.input.vcf} "
    "| bcftools view "
    "{view_extra} "
    "> {snakemake.output}"
)
