__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_ref=False)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(rbt vcf-fix-iupac-alleles {extra} < {snakemake.input[0]} | bcftools sort --temp-dir {tmpdir} {bcftools_opts}) {log}"
    )
