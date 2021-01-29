__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

if len(snakemake.input) != 1:
    raise ValueError("One bam input file expected, got: " + str(len(snakemake.input)))

shell("bamtools split -in {snakemake.input} {extra} {log}")
