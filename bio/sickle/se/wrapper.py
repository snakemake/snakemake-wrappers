__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

shell(
    "(sickle se -f {snakemake.input[0]} -o {snakemake.output[0]} "
    "-t {snakemake.params.qual_type} {extra}) {log}"
)
