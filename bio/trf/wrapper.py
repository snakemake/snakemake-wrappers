__author__ = "Muhammad Rohan Ali Asmat"
__copyright__ = "Copyright 2025, Muhammad Rohan Ali Asmat"
__email__ = "Muhammad.R.Ali.A@proton.me"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format


input_file = snakemake.input.sample
output_dir = snakemake.output[0]

fmt = get_format(input_file)
print(f"file file file file file : {fmt}")

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(f'mkdir -p {output_dir} && trf -u || true')
