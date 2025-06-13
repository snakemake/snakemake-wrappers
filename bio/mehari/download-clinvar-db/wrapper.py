__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

import re

version_re = re.compile(r"(?P<date>\d{8})\+(?P<annonars>\d+\.\d+\.\d+)")

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

version = snakemake.params["version"]
assert version_re.match(version)
date, annonars_version = version_re.search(version).groups()

build = snakemake.params["build"].lower()
assert build in ["grch37", "grch38"]

flavour = snakemake.params["flavour"].lower()
assert flavour in ["genes", "minimal", "sv"]

shell(
    "mkdir -p {snakemake.output}"
)
shell(
    "(curl -s -L https://github.com/varfish-org/annonars-data-clinvar/releases/download/annonars-data-clinvar-{date}/annonars-clinvar-{flavour}-{build}-{date}+{annonars_version}.tar.gz | "
    "tar xvz --strip-components=1 -C {snakemake.output}"
    ") {log}"
)
