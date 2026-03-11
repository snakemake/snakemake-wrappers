"""Snakemake wrapper for sequali."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

import re
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Assert input
n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

# Input files
if n == 1:
    reads = "{}".format(snakemake.input.sample)
else:
    reads = "{} {}".format(*snakemake.input.sample)

# Output files name

sample = snakemake.wildcards.sample

json = "--json {}.json".format(sample)

html = "--html {}.html".format(sample)

outdir = "--outdir {}".format(re.sub(r"/[^/]+$", "", snakemake.output.json))


# ==Change outputdir - Not Implemented==

# if snakemake.params.get("json", None):
#     json = "--json {}".format(snakemake.params.json)
# else:
#     json = "--json {}.json".format(sample)

# if snakemake.params.get("html", None):
#     html = "--html {}".format(snakemake.params.json)
# else:
#     html = "--html {}.html".format(sample)

# if snakemake.params.get("outdir", None):
#     outdir = "--outdir {}".format(snakemake.params.outdir)
# else:
#     outdir = "--outdir {}".format(
#         re.sub(r"/[^/]+$", "", snakemake.output.json)
#     )
# ==Change outputdir - Not Implemented==

shell("sequali" "{extra} " "{outdir} " "{json} " "{html} " "{reads} " "{log} ")
