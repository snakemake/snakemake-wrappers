__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

accessible = snakemake.input.get("accessible", "")
if accessible:
    accessible = f"-g {accessible}"

shell(
    "cnvkit.py antitarget "
    "{snakemake.input.bed} "
    "-o {snakemake.output.bed} "
    "{accessible} "
    "{extra} "
    "{log}"
)
