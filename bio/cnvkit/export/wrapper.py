__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os.path import splitext

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

file_name, file_extension = splitext(snakemake.output)

shell(
    "(cnvkit.py export {file_extenseion} "
    "{snakemake.input} "
    "-o {snakemake.output} "
    "{extra}) "
    "{log}"
)
