__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

taxonlist = snakemake.input.get("taxonlist")
if taxonlist:
    txlist_cmd = f"--taxonlist {taxonlist}"

## input options
#--taxonlist <list>
#Comma-separated list of NCBI taxonomic IDs to filter the database by. Any taxonomic rank can be used, and only reference sequences matching one of the specified taxon ids will be searched against. Using this option requires setting the --taxonmap and --taxonnodes parameters for makedb.
#--query-gencode #
#Genetic code used for translation of query in BLASTX mode. A list of possible values can be found at the NCBI website. By default, the Standard Code is used. Note: changing the genetic code is currently not fully supported for the DAA format.
#--strand {both, plus, minus}
#Set strand of query to align for translated searches. By default both strands are searched.
#--min-orf/-l #
#Ignore translated sequences that do not contain an open reading frame of at least this length. By default this feature is disabled for sequences of length below 30, set to 20 for sequences of length below 100, and set to 40 otherwise. Setting this option to 1 will disable this feature.

## alignment options
#--sensitive
#This mode is a lot more sensitive that the default and generally recommended for aligning longer sequences. The default mode is mainly designed for short read alignment, i.e. finding significant matches of >50 bits on 30-40aa fragments.
#--more-sensitive
#This mode provides some additional sensitivity compared to the sensitive mode.
#--frameshift/-F #
#Penalty for frameshifts in DNA-vs-protein alignments. Values around 15 are reasonable for this parameter. Enabling this feature will have the aligner tolerate missing bases in DNA sequences and is most recommended for long, error-prone sequences like MinION reads. In the pairwise output format, frameshifts will be indicated by \ and / for a shift by +1 and -1 nucleotide in the direction of translation respectively.
#Note that this feature is disabled by default.
#--gapopen #
#Gap open penalty.
#--gapextend #
#Gap extension penalty.
#--matrix <matrix name>
#Scoring matrix. The following matrices are supported, with the default being BLOSUM62.
#--comp-based-stats (0,1)
#Compositional bias correction of alignment scores. 0 means no score correction, 1 means compositional bias correction as described in [2] (default). Compositionally biased se- quences often cause false positive matches, which are effectively filtered by this algorithm in a way similar to the composition based statistics used by BLAST [3].
#--algo (0,1)
#Algorithm for seed search. 0 means double-indexed and 1 means query-indexed. Thedouble-indexed algorithm is the program’s main algorithm, but it is inefficient for very small query files, where the query-indexed algorithm should be used instead.
#By default, the program will automatically choose one of the algorithms based on the size of the query and database files. The algorithm used will be displayed at program startup. Note that while the two algorithms are configured to provide roughly the same sensitivity for the respective modes, results will not be exactly identical to each other.

shell("diamond blastx -db {snakemake.input.db} -q {snakemake.input.query} -o {output} --threads {snakemake.threads} {log}")
