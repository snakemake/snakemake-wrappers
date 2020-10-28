__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

out_parts = Path(snakemake.output[0]).parts
# Check if output folder follows Ensembl path structure
assert (
    str(Path(*out_parts[-2:])) == f"{snakemake.wildcards.species}/{snakemake.wildcards.release}_{snakemake.wildcards.build}"
), "output folder must end in '{species}/{release}_{build}'"
# Extract CACHE_DIR
cache_dir = str(Path(*out_parts[:-2]))

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "vep_install --AUTO cf "
    "--SPECIES {snakemake.wildcards.species} "
    "--ASSEMBLY {snakemake.wildcards.build} "
    "--CACHE_VERSION {snakemake.wildcards.release} "
    "--CACHEDIR {cache_dir} "
    "--CONVERT "
    "--NO_UPDATE "
    "{extra} {log}"
)
