__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

import re

version_re = re.compile(r"(?P<date>\d{8})\+(?P<annonars>\d+\.\d+\.\d+)")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

match = version_re.fullmatch(snakemake.params.version)
if not match:
    raise ValueError("Version must have format YYYYMMDD+MAJOR.MINOR.PATCH")
date, annonars_version = match.groups()

build = snakemake.params.get("build", "").lower()
if build not in {"grch37", "grch38"}:
    raise ValueError("build must be 'grch37' or 'grch38'")

flavour = snakemake.params.get("flavour", "").lower()
if flavour not in {"genes", "minimal", "sv"}:
    raise ValueError("flavour must be 'genes', 'minimal' or 'sv'")

output = snakemake.output[0]

# FIXME: investigate why the second shell command fails without the explicit mkdir call
#  snakemake should have created all output dirs/files before launching the wrapper.
shell("mkdir -p {output:q}")
shell(
    "(curl --fail --silent --location https://github.com/varfish-org/annonars-data-clinvar/releases/download/annonars-data-clinvar-{date}/annonars-clinvar-{flavour}-{build}-{date}+{annonars_version}.tar.gz | "
    "tar xvz -f- --strip-components=1 -C {output:q}"
    ") {log}"
)
