__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

from snakemake.remote.FTP import RemoteProvider as FTPRemoteProvider
FTP = FTPRemoteProvider()

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

taxinf = snakemake.params.get("use_taxonomy_info", "False")

if taxinf:
   #Path to mapping file that maps NCBI protein accession numbers to taxon ids (gzip com- pressed). This parameter is optional and needs to be supplied in order to provide taxon- omy features.
    taxonmap_file = snakemake.input.get("taxonmap")
    if not taxonmap_file:
        # try to download it and move it somewhere relevant
        taxmap_link = "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/prot.accession2taxid.gz"
        # add to cmd
        txmap_cmd = f"i --taxonmap {taxonmap_file} "

#
    #Path to the nodes.dmp file from the NCBI taxonomy. This parameter is optional and needs to be supplied in order to provide taxonomy features.
    taxonnodes_file = snakemake.input.get("taxonnodes_file")
    if not taxonnodes_file:
        # try to download it and move it somewhere relevant
        taxdmp_link="ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdmp.zip"
        # add to cmd
        txmap_cmd += f" --taxonnodes {taxonnodes_file} "



shell("diamond makedb --in {snakemake.input} --db {snakemake.output} --threads {snakemake.threads} {log}")
