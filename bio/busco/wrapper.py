"""Snakemake wrapper for BUSCO assessment"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
mode = snakemake.params.get("mode")
assert mode is not None, "please input a run mode: genome, transcriptome or proteins"
lineage = snakemake.params.get("lineage_path")
assert lineage is not None, "please input the path to a lineage for busco assessment"

# busco does not allow you to direct output location: handle this by moving output
outdir = path.dirname(snakemake.output[0])
if "/" in outdir:
    out_name = path.basename(outdir)
else:
    out_name = outdir

# note: --force allows snakemake to handle rewriting files as necessary
# without needing to specify *all* busco outputs as snakemake outputs
shell(
    "run_busco --in {snakemake.input} --out {out_name} --force "
    " --cpu {snakemake.threads} --mode {mode} --lineage {lineage} "
    " {extra} {log}"
)

busco_outname = "run_" + out_name

# move to intended location
shell("cp -r {busco_outname}/* {outdir}")
shell("rm -rf {busco_outname}")
