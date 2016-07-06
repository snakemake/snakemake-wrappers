__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

from snakemake.shell import shell

# Placeholder for optional parameters
opt_params = snakemake.params.other \
    if "other" in snakemake.params.keys() else ""

shell(
    "(sickle pe -f {snakemake.input.r1} -r {snakemake.input.r2} "
    "-o {snakemake.output.r1} -p {snakemake.output.r2} "
    "-s {snakemake.output.rs} -t {snakemake.params.qual_type} "
    "{opt_params}) > {snakemake.log}"
)
