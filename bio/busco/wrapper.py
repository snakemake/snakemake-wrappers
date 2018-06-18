"""Snakemake wrapper for Salmon Index."""

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

out_name = path.dirname(snakemake.output[0])
assert '/' not in out_name, "out name cannot be path"
assert out_name.startswith('run_'), " out name must start with run_"
out_name = out_name.split('run_')[1] # busco adds "run_" automatically

#note: --force allows snakemake to handle rewriting files as necessary
# without needing to specify *all* busco outputs as snakemake outputs
shell("run_busco --in {snakemake.input} --out {out_name} --force "
      " --cpu {snakemake.threads} --mode {mode} --lineage {lineage} "
      " {extra} {log}" )


