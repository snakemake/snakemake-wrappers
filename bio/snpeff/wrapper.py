__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell
from os import path
import shutil
import tempfile

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

dataDir = snakemake.params.get("dataDir", "")
if dataDir:
    dataDir = '-dataDir "%s"'%dataDir

stats = snakemake.output.get("stats", "")
genes = snakemake.output.get("genes", "")
if stats or genes:
    stats_tempdir = tempfile.mkdtemp()
    if not stats:
        if genes.endswith('.genes.txt'):
            stats = genes[:-10] + '.html'
        else:
            stats = genes + '.html'
    if not genes:
        if stats.endswith('.html'):
            genes = stats[:-5] + '.genes.txt'
        else:
            genes = stats + '.genes.txt'
    statsOpt = '-stats "%s"'%path.join(stats_tempdir, 'stats')
else:
    stats_tempdir = None
    statsOpt = '-noStats'

shell("(snpEff {dataDir} {statsOpt} {extra} {snakemake.params.reference} {snakemake.input}"
      " > {snakemake.output.vcf}) {log}")

if stats_tempdir:
    shutil.move(path.join(stats_tempdir, 'stats'), stats)
    shutil.move(path.join(stats_tempdir, 'stats.genes.txt'), genes)
    shutil.rmtree(stats_tempdir)
