__author__ = "Nathan Olson"
__copyright__ = "TODO - add government"
__email__ = "nolson@nist.gov"
__license__ = "Add NIST"

from os import path

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "(hap.py"
    " --threads {snakemake.threads}"
    " --engine={snakemake.params.engine}"
    " -r {snakemake.params.genome}"
    " {extra}"
    " {snakemake.input.truth}"
    " {snakemake.input.query}"
    " -f {snakemake.input.truth_regions}"
    " --stratification {snakemake.input.strats}"
    " -o {snakemake.output})"
    " {log}"
)

## Questions
# - using a default value for engine
# - best practices for using output directories in wrappers
# - best practices for using input directories (specficially for stratifications)
# - file size recommendations for testing
