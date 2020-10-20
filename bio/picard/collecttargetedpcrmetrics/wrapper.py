__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@mail.com"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell()

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


shell(
    "picard CollectTargetedPcrMetrics "
    "{java_opts} {extra} "
    "INPUT={snakemake.input.bam} "
    "OUTPUT={snakemake.output[0]} "
    "AMPLICON_INTERVALS={snakemake.input.amplicon_intervals} "
    "TARGET_INTERVALS={snakemake.input.target_intervals} "
    "{log}"
)
