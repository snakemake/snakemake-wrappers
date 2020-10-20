"""Snakemake wrapper for picard SortSam."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
java_opts = ""
# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and "-Djava.io.tmpdir" not in extra:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

fastq1 = snakemake.output.fastq1
fastq2 = snakemake.output.get("fastq2", None)
fastq_unpaired = snakemake.output.get("unpaired_fastq", None)

if not isinstance(fastq1, str):
    raise ValueError("f1 needs to be provided")

output = " FASTQ=" + fastq1

if isinstance(fastq2, str):
    output += " SECOND_END_FASTQ=" + fastq2

if isinstance(fastq_unpaired, str):
    if not isinstance(fastq2, str):
        raise ValueError("f2 is required if fastq_unpaired is set")

    output += " UNPAIRED_FASTQ=" + fastq_unpaired

shell(
    "picard"
    " SamToFastq"
    " {java_opts}"
    " {extra}"
    " INPUT={snakemake.input[0]}"
    " {output}"
    " {log}"
)
