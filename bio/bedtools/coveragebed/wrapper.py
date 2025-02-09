__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

shell.executable("bash")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra_params = snakemake.params.get("extra", "")

input_a = snakemake.input.a
input_b = snakemake.input.b

output_file = snakemake.output[0]

compress = "| bgzip" if snakemake.output[0].endswith(".gz") else ""

if not isinstance(output_file, str) and len(snakemake.output) != 1:
    raise ValueError("Output should be one file: " + str(output_file) + "!")

shell(
    "coverageBed"
    " -a {input_a}"
    " -b {input_b}"
    " {extra_params}"
    " {compress}"
    " > {output_file}"
    " {log}"
)
