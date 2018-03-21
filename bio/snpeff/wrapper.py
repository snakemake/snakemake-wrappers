__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

dataDir = snakemake.params.get("dataDir", "")
if dataDir:
    dataDir = '-dataDir "%s"'%dataDir

stats = snakemake.output.get("stats", "")
if stats:
    stats = '-stats "%s"'%stats
else:
    stats = '-noStats'

shell("(snpEff {dataDir} {stats} {extra} {snakemake.params.reference} {snakemake.input}"
      " > {snakemake.output.vcf}) {log}")
