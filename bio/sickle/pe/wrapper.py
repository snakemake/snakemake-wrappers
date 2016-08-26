__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

shell(
    "(sickle pe -f {snakemake.input.r1} -r {snakemake.input.r2} "
    "-o {snakemake.output.r1} -p {snakemake.output.r2} "
    "-s {snakemake.output.rs} -t {snakemake.params.qual_type} "
    "{extra}) {log}"
)
