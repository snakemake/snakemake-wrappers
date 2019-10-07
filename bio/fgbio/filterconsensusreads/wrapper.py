__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra_params = snakemake.params.get("extra", "")

min_base_quality = snakemake.params.get("min_base_quality", None)
if not isinstance(min_base_quality, int):
    raise ValueError("min_base_quality needs to be provided as an Int!")

min_reads = snakemake.params.get("min_reads", None)
if not isinstance(min_reads, list) or not (1 <= len(min_reads) <= 3):
    raise ValueError(
        "min_reads needs to be provided as list of Ints, min length 1, max length 3!"
    )

ref = snakemake.params.get("ref", None)
if ref is None:
    raise ValueError("A reference needs to be provided!")

bam_input = snakemake.input[0]

if not isinstance(bam_input, str) and len(snakemake.input) != 1:
    raise ValueError("Input bam should be one bam file: " + str(bam_input) + "!")

bam_output = snakemake.output[0]

if not isinstance(bam_output, str) and len(snakemake.output) != 1:
    raise ValueError("Output should be one bam file: " + str(bam_output) + "!")

shell(
    "fgbio FilterConsensusReads"
    " -i {bam_input}"
    " -o {bam_output}"
    " -r {ref}"
    " --min-reads {min_reads}"
    " --min-base-quality {min_base_quality}"
    " {extra_params}"
    " {log}"
)
