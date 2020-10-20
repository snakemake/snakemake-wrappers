__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
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

shell(
    "picard "
    "CreateSequenceDictionary "
    "{java_opts} {extra} "
    "R={snakemake.input[0]} "
    "O={snakemake.output[0]} "
    "{log}"
)
