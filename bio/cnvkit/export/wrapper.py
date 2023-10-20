__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os.path import splitext

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")


file_name, file_extension = splitext(snakemake.output[0])

if file_extension == ".gz":
    file_extension = splitext(file_name)[1][1:]
    output = f" | bgzip > {snakemake.output}"
else:
    file_extension = file_extension[1:]
    output = f"-o {snakemake.output} "

shell(
    "(cnvkit.py export {file_extension} "
    "{snakemake.input} "
    "{extra} "
    "{output}) "
    "{log}"
)
