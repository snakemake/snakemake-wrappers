__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = " ".format(snakemake.params.get("view", ""))
if view:
    view = f"--view {view}"
else:
    view = ""
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "(cooltools expected-trans"
    " {snakemake.input.cooler}::resolutions/{snakemake.wildcards.resolution} "
    " {view} "
    " {extra} "
    " -o {snakemake.output}) {log}"
)
