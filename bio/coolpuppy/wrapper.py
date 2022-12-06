__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"
expected = snakemake.input.get("expected", "")
if expected:
    expected = f"--expected {expected}"

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

resolution = snakemake.params.get("resolution", snakemake.wildcards.get("resolution"))
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

shell(
    "(coolpup.py"
    " {snakemake.input.cooler}::resolutions/{resolution}"
    " {snakemake.input.features}"
    " {expected}"
    " --features-format {snakemake.params.features_format}"
    " {view}"
    " -p {snakemake.threads}"
    " {extra}"
    " -o {snakemake.output}) {log}"
)
