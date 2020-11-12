__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell
from os import path
import shutil
import tempfile
from pathlib import Path
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

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
