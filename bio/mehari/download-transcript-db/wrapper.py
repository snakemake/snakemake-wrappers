__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

import re

version_re = re.compile(r"\d+\.\d+\.\d+")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

version = snakemake.params["version"]
if not version_re.fullmatch(version):
    raise ValueError("version must have format MAJOR.MINOR.PATCH")

build = snakemake.params["build"]
if build not in {"GRCh37", "GRCh38"}:
    raise ValueError("build must be 'GRCh37' or 'GRCh38'")

source = snakemake.params["source"].lower()
if source not in {"ensembl", "refseq", "ensembl-and-refseq"}:
    raise ValueError("source must be 'ensembl', 'refseq' or 'ensembl-and-refseq'")

output = snakemake.output[0]

shell(
    "curl --fail -L https://github.com/varfish-org/mehari-data-tx/releases/download/v{version}/mehari-data-txs-{build}-{source}-{version}.bin.zst -o {output:q} {log}"
)
