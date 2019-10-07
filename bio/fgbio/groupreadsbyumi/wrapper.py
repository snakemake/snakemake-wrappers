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

output_bam_file = snakemake.output.bam

if not isinstance(output_bam_file, str) and len(output_bam_file) != 1:
    raise ValueError("Bam output should be one bam file: " + str(output_bam_file) + "!")

output_histo_file = snakemake.output.hist

if not isinstance(output_histo_file, str) and len(output_histo_file) != 1:
    raise ValueError(
        "Histo output should be one histogram file path: "
        + str(output_histo_file)
        + "!"
    )

shell(
    "fgbio GroupReadsByUmi"
    " -i {bam_input}"
    " -o {output_bam_file}"
    " -f {output_histo_file}"
    " {extra_params}"
    " {log}"
)
