__author__ = "Fritjof Lammers"
__copyright__ = "Copyright 2022, Fritjof Lammers"
__email__ = "f.lammers@dkfz.de"

__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)

if java_opts:
    java_opts_str = f'JAVA_OPTS="{java_opts}"'
else:
    java_opts_str = ""

# unset DISPLAY environment variable to avoid X11 error message issued by qualimap
if os.environ.get("DISPLAY"):
    del os.environ["DISPLAY"]

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "{java_opts_str} qualimap bamqc {extra} "
    "-bam {snakemake.input.bam} "
    "-outdir {snakemake.output} "
    "{log}"
)
