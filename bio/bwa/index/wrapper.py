__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2016, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from os.path import splitext
from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

# Prefix that should be used for the database
prefix = snakemake.params.get("prefix", splitext(snakemake.output[0])[0])

# Block size should be a 10th of the reference length (https://github.com/lh3/bwa/issues/104)
block_size = Path(snakemake.input[0]).stat().st_size / 1024 / 1024 / 10
# If GZip, assume a 4-fold compression rate:
# - https://scfbm.biomedcentral.com/articles/10.1186/s13029-019-0073-5/tables/3
# - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7336184/
# - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3866555/bin/supp_btt594_supplement-rev2.pdf
# - https://softpanorama.org/HPC/DNA_sequencing/Genomic_data_compression/index.shtml
if snakemake.input[0].endswith(".gz"):
    block_size *= 4

# Ensure minimum (10 Mb as BWA default) and maximum (50Gb since no apparent gain and to limit memory usage) block size
block_size = min(50 * 1024, max(10, int(block_size)))

shell("bwa index -b {block_size}M -p {prefix} {extra} {snakemake.input} {log}")
