__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get('extra', '')

annotate = snakemake.input.get("annotate", "")
if annotate:
  annotate = f"--annotate {annotate}"

shell(
    f"(cnvkit.py target "
    f"{snakemake.input.bed} "
    f"-o {snakemake.output.bed} "
    f"{annotate} "
    f"{extra}) "
    "{log}"
)
        
