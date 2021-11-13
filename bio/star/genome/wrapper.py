"""Snakemake wrapper for STAR genome"""

__author__ = "Ruiyu Ray Wang"
__copyright__ = "Copyright 2021, Ruiyu Wang"
__email__ = "raywong.chn@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

index = snakemake.input.get("index")
loadmode = snakemake.params.get("loadmode")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    """
    STAR --genomeLoad {loadmode} \
         --runThreadN {snakemake.threads} \
         --genomeDir {index} \
         --outSAMmode None \
         {log}
    rm -f Log.final.out Log.out Log.progress.out SJ.out.tab
    """
)
