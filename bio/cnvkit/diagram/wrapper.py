__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

cns_file = [f for f in snakemake.input if f.endswith(".cns")]
cnr_file = [f for f in snakemake.input if f.endswith(".cnr") or f.endswith(".cnn")]

if cns_file:
    if len(cns_file) > 1:
        raise Exception(f"Expecting only one input cns file {cns_file}")
    cns_file = f"-s {cns_file[0]}"

if cnr_file:
    if len(cnr_file) > 1:
        raise Exception(f"Expecting only one input cnr/cnn file {cnr_file}")
    cnr_file = f"{cnr_file[0]}"

extra = snakemake.params.get("extra", "")

shell(
    "(cnvkit.py diagram "
    "{cns_file} "
    "{cnr_file} "
    "-o {snakemake.output} "
    "{extra}) "
    "{log}"
)
