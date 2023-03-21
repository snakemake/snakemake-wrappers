__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with TemporaryDirectory() as tempdir:
    shell(
        "sambamba markdup {snakemake.params.extra} --nthreads {snakemake.threads} "
        "--tmpdir {tempdir} {snakemake.input[0]} {snakemake.output[0]} "
        "{log}"
    )
