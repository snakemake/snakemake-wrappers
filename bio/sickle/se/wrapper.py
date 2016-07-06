__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

from snakemake.shell import shell

# Placeholder for optional parameters
opt_params = snakemake.params.other \
    if "other" in snakemake.params.keys() else ""

shell(
    "(sickle se -f {snakemake.input[0]} -o {snakemake.output[0]} "
    "-t {snakemake.params.qual_type} {opt_params}) > {snakemake.log}"
)
