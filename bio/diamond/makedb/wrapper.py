__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Path to mapping file that maps NCBI protein accession numbers to taxon ids (gzip com- pressed). This parameter is optional and needs to be supplied in order to provide taxonomy features.
taxonmap = snakemake.input.get("taxonmap")
txmap_cmd = ""
if taxonmap:
    txmap_cmd = f" --taxonmap {taxonmap} "

# Path to the nodes.dmp file from the NCBI taxonomy. This parameter is optional and needs to be supplied in order to provide taxonomy features.
taxonnodes = snakemake.input.get("taxonnodes")
txnode_cmd = ""
if taxonnodes:
    txnode_cmd = f" --taxonnodes {taxonnodes} "

shell(
    "diamond makedb --in {snakemake.input.db} --db {snakemake.output} --threads {snakemake.threads} {txmap_cmd} {txnode_cmd} {extra} {log}"
)
