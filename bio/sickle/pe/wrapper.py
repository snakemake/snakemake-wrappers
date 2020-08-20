__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"

import os

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

os.system(
    f"(sickle pe -f {snakemake.input.r1} -r {snakemake.input.r2} "
    f"-o {snakemake.output.r1} -p {snakemake.output.r2} "
    f"-s {snakemake.output.rs} -t {snakemake.params.qual_type} "
    f"{extra}) {log}"
)
