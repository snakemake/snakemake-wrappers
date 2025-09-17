# coding: utf-8

"""This wrapper handles vcf2maf.pl"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from tempfile import TemporaryDirectory
from snakemake.shell import shell
from warnings import warn
from shlex import quote

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Optional input files
fasta = snakemake.input.get("fasta")
if fasta:
    extra += f" --ref-fasta={quote(fasta)}"

chain = snakemake.input.get("chain")
if chain:
    extra += f" --remap-chain={quote(chain)}"

# Acquiring external VEP installation
# if any...
vep = ""
vep_path = snakemake.input.get("vep", "")
if vep_path:
    vep = f"--vep-path={quote(vep)}"

vep_config = snakemake.input.get("vep_config")
if vep_config:
    vep += f" --vep-config={quote(vep_config)}"

vep_cache = snakemake.input.get("vep_cache")
if vep_cache:
    vep += f" --vep-data={quote(vep_cache)}"

# Automatically turning VEP off if user
# does not provide at least one VEP information
if all([vep_path, vep_cache, vep_config]):
    # vcf2maf.pl can run VEP using more than one thread
    # This would be the only multithreaded section of the code
    vep += f" --vep-forks={snakemake.threads}"
else:
    vep = " --inhibit-vep"
    if snakemake.threads > 1:
        warn("Too many threads requested: only 1 used.")

# Autmatically set temporary directory
with TemporaryDirectory() as tempdir:
    shell(
        "vcf2maf.pl"
        " --input-vcf={snakemake.input.vcf:q}"
        " {vep}"
        " {extra}"
        " --tmp-dir={tempdir:q}"
        " --output-maf={snakemake.output:q}"
        " {log}"
    )
