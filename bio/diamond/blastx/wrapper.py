__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

taxonlist = snakemake.input.get("taxonlist")
#Comma-separated list of NCBI taxonomic IDs to filter the database by. Any taxonomic rank can be used, and only reference sequences matching one of the specified taxon ids will be searched against. Using this option requires setting the --taxonmap and --taxonnodes parameters for makedb.
if taxonlist:
    txlist_cmd = f" --taxonlist {taxonlist} "

#Set strand of query to align for translated searches. By default both strands are searched.
strand=snakemake.params.get("strand", "both") #both, plus, minus

#The default mode is mainly designed for short read alignment, i.e. finding significant matches of >50 bits on 30-40aa fragments.
sensitivity=snakemake.params.get("alignment_sensitivity") # optionally increase sensitivity: sensitive, more-sensitive
s_cmd = ""
if sensitivity:
    if sensitivity == "sensitive":
       # this mode is a lot more sensitive that the default and generally recommended for aligning longer sequences.
        s_cmd = " --sensitive "
    elif sensitivity == "more-sensitive":
       # more-sensitive: This mode provides some additional sensitivity compared to the sensitive mode.
        s_cmd = " --more-sensitive "

shell("diamond blastx -db {snakemake.input.db} -q {snakemake.input.query} -o {output} --threads {snakemake.threads} {txlist_cmd} {s_cmd} {extra} {log}")
