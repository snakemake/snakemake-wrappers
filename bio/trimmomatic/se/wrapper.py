__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
trimmer = " ".join(snakemake.params.trimmer)

shell("trimmomatic SE {snakemake.params.extra} "
      "{snakemake.input} {snakemake.output} "
      "{trimmer} "
      "{log}")
