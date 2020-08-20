__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

import os

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

os.system(
    f"(sickle se -f {snakemake.input[0]} -o {snakemake.output[0]} "
    "-t {snakemake.params.qual_type} {extra}) {log}"
)
