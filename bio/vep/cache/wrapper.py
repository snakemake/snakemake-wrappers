__author__ = "Johannes Köster"
__copyright__ = "Copyright 2023, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


try:
    release = int(snakemake.params.release)
except ValueError:
    raise ValueError("The parameter release is supposed to be an integer.")


with tempfile.TemporaryDirectory() as tmpdir:
    # We download the cache tarball manually because vep_install does not consider proxy settings (in contrast to curl).
    # See https://github.com/bcbio/bcbio-nextgen/issues/1080
    cache_url = snakemake.params.get("url", "ftp://ftp.ensembl.org/pub")
    cache_tarball = (
        f"{snakemake.params.species}_vep_{release}_{snakemake.params.build}.tar.gz"
    )
    vep_dir = "vep" if snakemake.params.get("url") or release >= 97 else "VEP"
    shell(
        "curl -L {cache_url}/release-{release}/variation/{vep_dir}/{cache_tarball} -o {tmpdir}/{cache_tarball} {log}"
    )

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell(
        "vep_install --AUTO c "
        "--SPECIES {snakemake.params.species} "
        "--ASSEMBLY {snakemake.params.build} "
        "--CACHE_VERSION {release} "
        "--CACHEURL {tmpdir} "
        "--CACHEDIR {snakemake.output} "
        "--CONVERT "
        "--NO_UPDATE "
        "{extra} {log}"
    )
