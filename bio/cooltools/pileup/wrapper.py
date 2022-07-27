__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
view = snakemake.input.get("view", "")
if view:
    view = f"--view {view}"
features = snakemake.input.get("features", "")
if not features:
    raise ValueError("Please provide features file")
features_format = snakemake.params.get("features_format", "")
if not features_format:
    raise ValueError("Please provide features format")
expected = snakemake.input.get("expected", "")
if expected:
    expected = f"--expected {expected}"
else:
    expected = ""
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

resolution = snakemake.params.get(
    "resolution", snakemake.wildcards.get("resolution", 0)
)
if not resolution:
    raise ValueError("Please specify resolution either as a wildcard or as a parameter")

shell(
    "(cooltools pileup"
    " {snakemake.input.cooler}::resolutions/{resolution} "
    " {features} "
    " {expected} "
    " --features-format {features_format} "
    " {view} "
    " -p {snakemake.threads} "
    " {extra} "
    " -o {snakemake.output}) {log}"
)
