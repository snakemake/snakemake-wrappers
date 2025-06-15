__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

import re

version_re = re.compile(r"\d+\.\d+\.\d+")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

version = snakemake.params.get("version", "")
if not version_re.fullmatch(version):
    raise ValueError("version must have format MAJOR.MINOR.PATCH")

build = snakemake.params.get("build", "").lower()
if build not in {"grch37", "grch38"}:
    raise ValueError("build must be 'GRCh37' or 'GRCh38'")
build = {"grch37": "GRCh37", "grch38": "GRCh38"}[build]

source = snakemake.params.get("source", "").lower()
if source not in {"ensembl", "refseq", "ensembl-and-refseq"}:
    raise ValueError("source must be 'ensembl', 'refseq' or 'ensembl-and-refseq'")

shell(
    "curl --fail --location https://github.com/varfish-org/mehari-data-tx/releases/download/v{version}/mehari-data-txs-{build}-{source}-{version}.bin.zst -o {snakemake.output[0]:q} {log}"
)
