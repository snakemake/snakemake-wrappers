__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell


class MissingReferenceError(Exception):
    pass


options = snakemake.params.get("options", "")

# determine if a fasta reference is provided or not and add to options
if "--no-reference" not in options:
    ref = snakemake.input.get("ref", "")
    if not ref:
        raise MissingReferenceError(
            "The --no-reference option was not given, but no fasta reference was "
            "provided."
        )
    options += " --fasta-ref {}".format(ref)

shell(
    "bcftools mpileup {options} --threads {snakemake.threads} "
    "--output {snakemake.output.pileup} "
    "{snakemake.input.alignments} 2> {snakemake.log}"
)
