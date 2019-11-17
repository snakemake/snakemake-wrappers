__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

pep_query = snakemake.input.get("pep_query")
nucl_query = snakemake.input.get("nucl_query")
# assert pep_query is not None or nucl_query is not None, "either pep_query or nucl_query are required as input"
queryfiles = [pep_query, nucl_query]
assert (
    list(map(bool, queryfiles)).count(True) == 1
), "one query is required: either a peptide query (pep_query) for diamond blastp OR a nucleotide query (nucl_query) for diamond blastx"

if pep_query:
    query = pep_query
    prog = "blastp"
elif nucl_query:
    query = nucl_query
    prog = "blastx"

taxonlist = snakemake.params.get("taxonlist")
# Comma-separated list of NCBI taxonomic IDs to filter the database by. Any taxonomic rank can be used, and only reference sequences matching one of the specified taxon ids will be searched against. Using this option requires setting the --taxonmap and --taxonnodes parameters for makedb.
txlist_cmd = ""
if taxonlist:
    taxonlist = str(taxonlist)
    assert (
        taxonlist != "0" and taxonlist != "1"
    ), "Option --taxonlist cannot be used with invalid argument (0 or 1)"
    txlist_cmd = f" --taxonlist {str(taxonlist)} "

# Set strand of query to align for translated searches. By default both strands are searched.
strand = snakemake.params.get("strand", "both")  # both, plus, minus
assert strand in [
    "both",
    "plus",
    "minus",
], "please specify 'both', 'plus', or 'minus' for the strand parameter"

# The default mode is mainly designed for short read alignment, i.e. finding significant matches of >50 bits on 30-40aa fragments.
sensitivity = snakemake.params.get(
    "alignment_sensitivity"
)  # optionally increase sensitivity: sensitive, more-sensitive
s_cmd = ""
if sensitivity:
    if sensitivity == "sensitive":
        # this mode is a lot more sensitive that the default and generally recommended for aligning longer sequences.
        s_cmd = " --sensitive "
    elif sensitivity == "more-sensitive":
        # more-sensitive: This mode provides some additional sensitivity compared to the sensitive mode.
        s_cmd = " --more-sensitive "
    else:
        raise ValueError(
            "alignment sensitivity must be either 'sensitive' or 'more-sensitive'"
        )

shell(
    "diamond {prog} --db {snakemake.input.db} -q {query} -o {snakemake.output} --threads {snakemake.threads} {txlist_cmd} {s_cmd} {extra} {log}"
)
