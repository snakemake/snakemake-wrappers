__author__ = "Johannes Köster, Jorge Langa"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
compression_level = snakemake.params.get("compression_level", "-5")
trimmer = " ".join(snakemake.params.trimmer)


if snakemake.input.get("r2", False):
    trim_mode = "PE"
    in_files = [snakemake.input.r1, snakemake.input.r2]
    out_files = [snakemake.output.r1, snakemake.output.r1_unpaired, snakemake.output.r2, snakemake.output.r2_unpaired]
else:
    trim_mode = "SE"
    in_files = snakemake.input[0]
    out_files = snakemake.output[0]


shell(
    "trimmomatic {trim_mode}"
    " -threads {trimmomatic_threads}"
    " {java_opts}"
    " {extra}"
    " {in_files}"
    " {out_files}"
    " {trimmer}"
    " {log}"
)
