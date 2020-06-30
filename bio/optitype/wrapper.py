__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
outdir = os.path.dirname(snakemake.output[0])

# get sequencing type
seq_type = snakemake.params.get("sequencing_type", "dna")
seq_type = "--{}".format(seq_type)

# check if non-default config.ini is used
config = snakemake.params.get("config", "")
if any(config):
    config = "--config {}".format(config)

shell(
    "(OptiTypePipeline.py"
    " --input {snakemake.input.reads}"
    " --outdir {outdir}"
    " --prefix {snakemake.wildcards.sample}"
    " {seq_type}"
    " {config}"
    " {extra})"
    " {log}"
)
