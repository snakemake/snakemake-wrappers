__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell
from os import path
import shutil
import tempfile

shell.executable("bash")
shell_command = (
    "(snpEff {data_dir} {stats_opt} {csvstats_opt} {extra}"
    " {snakemake.params.reference} {snakemake.input}"
    " > {snakemake.output.vcf}) {log}"
)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

data_dir = snakemake.params.get("data_dir", "")
if data_dir:
    data_dir = '-dataDir "%s"' % data_dir

stats = snakemake.output.get("stats", "")
csvstats = snakemake.output.get("csvstats", "")
csvstats_opt = "" if not csvstats else "-csvStats {}".format(csvstats)
stats_opt = "-noStats" if not stats else "-stats {}".format(stats)

shell(shell_command)

