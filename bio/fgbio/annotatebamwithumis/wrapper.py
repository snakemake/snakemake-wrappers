__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra_params = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bam_input = snakemake.input.bam

if bam_input is None:
    raise ValueError("Missing bam input file!")
elif not isinstance(bam_input, str):
    raise ValueError("Input bam should be a string: " + str(bam_input) + "!")

umi_input = snakemake.input.umi

if umi_input is None:
    raise ValueError("Missing input file with UMIs")
elif not isinstance(umi_input, str):
    raise ValueError("Input UMIs-file should be a string: " + str(umi_input) + "!")

if not len(snakemake.output) == 1:
    raise ValueError("Only one output value expected: " + str(snakemake.output) + "!")
output_file = snakemake.output[0]


if output_file is None:
    raise ValueError("Missing output file!")
elif not isinstance(output_file, str):
    raise ValueError("Output bam-file should be a string: " + str(output_file) + "!")

shell(
    "fgbio {java_opts} AnnotateBamWithUmis"
    " -i {bam_input}"
    " -f {umi_input}"
    " -o {output_file}"
    " {extra_params}"
    " {log}"
)
