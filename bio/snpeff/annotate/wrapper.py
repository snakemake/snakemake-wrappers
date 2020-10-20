__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell
from os import path
import shutil
import tempfile
from pathlib import Path

outcalls = snakemake.output.calls
if outcalls.endswith(".vcf.gz"):
    outprefix = "| bcftools view -Oz"
elif outcalls.endswith(".bcf"):
    outprefix = "| bcftools view -Ob"
else:
    outprefix = ""

incalls = snakemake.input[0]
if incalls.endswith(".bcf"):
    incalls = "< <(bcftools view {})".format(incalls)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

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


data_dir = Path(snakemake.input.db).parent.resolve()

stats = snakemake.output.get("stats", "")
csvstats = snakemake.output.get("csvstats", "")
csvstats_opt = "" if not csvstats else "-csvStats {}".format(csvstats)
stats_opt = "-noStats" if not stats else "-stats {}".format(stats)

reference = path.basename(snakemake.input.db)

shell(
    "snpEff {java_opts} -dataDir {data_dir} "
    "{stats_opt} {csvstats_opt} {extra} "
    "{reference} {incalls} "
    "{outprefix} > {outcalls} {log}"
)
