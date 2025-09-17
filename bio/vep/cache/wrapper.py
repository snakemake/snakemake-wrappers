__author__ = "Johannes Köster"
__copyright__ = "Copyright 2023, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import subprocess as sp
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
    user_url = snakemake.params.get("url", "ftp.ensembl.org/pub")
    if user_url.startswith("https://"):
        url_https = f"{user_url}/release-{release}/variation/{vep_dir}/{cache_tarball}"
        url_ftp = url_https.replace("https://", "ftp://")
    elif user_url.startswith("ftp://"):
        url_ftp = user_url
        url_https = url_ftp.replace("ftp://", "https://")
    else:
        url_https = (
            f"https://{user_url}/release-{release}/variation/{vep_dir}/{cache_tarball}"
        )
        url_ftp = url_https.replace("https://", "ftp://")
    cache_tarball = (
        f"{snakemake.params.species}_vep_{release}_{snakemake.params.build}.tar.gz"
    )
    if snakemake.params.get("indexed"):
        vep_dir = "indexed_vep_cache"
        convert = ""
    else:
        vep_dir = "vep" if snakemake.params.get("url") or release >= 97 else "VEP"
        convert = "--CONVERT "
        try:
            shell(f"curl -L {url_https} -o {tmpdir}/{cache_tarball} {log}")
        except sp.CalledProcessError:
            shell(f"curl -L {url_ftp} -o {tmpdir}/{cache_tarball} {log}")

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell(
        "vep_install --AUTO c "
        "--SPECIES {snakemake.params.species} "
        "--ASSEMBLY {snakemake.params.build} "
        "--CACHE_VERSION {release} "
        "--CACHEURL {tmpdir} "
        "--CACHEDIR {snakemake.output} "
        "{convert}"
        "--NO_UPDATE "
        "{extra} {log}"
    )
