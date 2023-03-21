__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with TemporaryDirectory() as tempdir:
    shell(
        "sambamba sort {snakemake.params} --nthreads {snakemake.threads} "
        "--tmpdir {tempdir} --out {snakemake.output[0]} {snakemake.input[0]} "
        "{log}"
    )
