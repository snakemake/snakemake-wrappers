__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra_params = snakemake.params.get("extra", "")

bam_input = snakemake.input[0]

if not isinstance(bam_input, str) and len(snakemake.input) != 1:
    raise ValueError("Input bam should be one bam file: " + str(bam_input) + "!")

output_file = snakemake.output[0]

if not isinstance(output_file, str) and len(snakemake.output) != 1:
    raise ValueError("Output should be one bam file: " + str(output_file) + "!")

shell(
    "fgbio SetMateInformation"
    " -i {bam_input}"
    " -o {output_file}"
    " {extra_params}"
    " {log}"
)
