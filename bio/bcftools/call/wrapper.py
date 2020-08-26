__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


class CallerOptionError(Exception):
    pass


valid_caller_opts = {"-c", "--consensus-caller", "-m", "--multiallelic-caller"}

caller_opt = snakemake.params.get("caller", "")
if caller_opt.strip() not in valid_caller_opts:
    raise CallerOptionError(
        "bcftools call expects either -m/--multiallelic-caller or "
        "-c/--consensus-caller as caller option."
    )

options = snakemake.params.get("options", "")

shell(
    "bcftools call {options} {caller_opt} --threads {snakemake.threads} "
    "-o {snakemake.output.calls} {snakemake.input.pileup} 2> {snakemake.log}"
)
