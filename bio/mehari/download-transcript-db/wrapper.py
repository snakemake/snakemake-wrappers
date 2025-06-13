__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

import re

version_re = re.compile(r"\d+\.\d+\.\d+")

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

version = snakemake.params["version"]
assert version_re.match(version)

build = snakemake.params["build"]
assert build in ["GRCh37", "GRCh38"]

source = snakemake.params["source"].lower()
assert source in ["ensembl", "refseq", "ensembl-and-refseq"]


shell(
    "curl -L https://github.com/varfish-org/mehari-data-tx/releases/download/v{version}/mehari-data-txs-{build}-{source}-{version}.bin.zst -o {snakemake.output} {log}"
)
