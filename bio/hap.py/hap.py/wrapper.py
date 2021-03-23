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
    " -r {snakemake.input.genome}"
    " {extra}"
    " {snakemake.input.truth}"
    " {snakemake.input.query}"
    " -f {snakemake.input.truth_regions}"
    " --stratification {snakemake.input.strats}"
    " -o {snakemake.output})"
    " {log}"
)
