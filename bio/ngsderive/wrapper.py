# coding: utf-8

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from os.path import commonprefix, dirname
from snakemake import shell
from warnings import warn

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

gene_model = snakemake.input.get("gene_model", "")
if gene_model:
    gene_model = f"--gene-model {gene_model}"


junction_dir = snakemake.output.get("junction_dir", "")
if isinstance(junction_dir, list):
    junction_dir = commonprefix([dirname(fp) for fp in junction_dir])
    if not junction_dir:
        warn(
            "No common prefix was found within the list of "
            "files given as `junction_files_dir`. Falling "
            "back to default ngsderive value"
        )

if junction_dir:
    junction_dir = f"--junction-files-dir {junction_dir}"


shell(
    "ngsderive {snakemake.params.command} "
    "{extra} {gene_model} {junction_dir} "
    "{snakemake.input.ngs} "
    "--outfile {snakemake.output.tsv} "
    "{log} "
)
