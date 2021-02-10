__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if snakemake.output[0].endswith("bcf"):
    output_format = "-Ou"
elif snakemake.output[0].endswith("bcf.gz"):
    output_format = "-Ob"
elif snakemake.output[0].endswith("vcf"):
    output_format = "-Ov"
elif snakemake.output[0].endswith("vcf.gz"):
    output_format = "-Oz"


if len(snakemake.input) > 1:
    raise Exception("Only one input file expected, got: " + str(len(snakemake.input)))

if len(snakemake.output) > 1:
    raise Exception("Only one output file expected, got: " + str(len(snakemake.output)))

filter = snakemake.params.get("filter", "")
extra = snakemake.params.get("extra", "")

shell(
    "bcftools filter {filter} {extra} {snakemake.input[0]} "
    "{output_format} "
    "-o {snakemake.output[0]} "
    "{log}"
)
