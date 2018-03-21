__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

pedigree = snakemake.params.get("pedigree", "")
if pedigree:
      pedigree = '--pedigree "%s"'%pedigree

shell("jannovar annotate-vcf --database {snakemake.params.database}"
      " --input-vcf {snakemake.input} --output-vcf {snakemake.output}"
      " {pedigree} {extra} {log}")
