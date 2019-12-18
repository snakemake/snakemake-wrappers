"""Snakemake wrapper for Infernal CMscan"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

profile = snakemake.input.get("profile")
profile = profile.rsplit(".i", 1)[0]

assert profile.endswith(".cm"), 'your profile file should end with ".cm"'

# direct output to file <f>, not stdout
out_cmd = ""
outfile = snakemake.output.get("outfile", "")
if outfile:
    out_cmd += " -o {} ".format(outfile)

# save parseable table of hits to file <s>
tblout = snakemake.output.get("tblout", "")
if tblout:
    out_cmd += " --tblout {} ".format(tblout)

## default params: enable evalue threshold. If bitscore thresh is provided, use that instead (both not allowed)

# report <= this evalue threshold in output
evalue_threshold = snakemake.params.get("evalue_threshold", 10)  # use cmscan default
# report >= this score threshold in output
score_threshold = snakemake.params.get("score_threshold", "")

if score_threshold:
    thresh_cmd = f" -T {float(score_threshold)} "
else:
    thresh_cmd = f" -E {float(evalue_threshold)} "

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "cmscan {out_cmd} {thresh_cmd} {extra} --cpu {snakemake.threads} {profile} {snakemake.input.fasta} {log}"
)
