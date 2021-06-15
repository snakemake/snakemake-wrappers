__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell

# the reference_name argument is inferred by stripping the .seq suffix from
# the output.seq value
output_directory = os.path.dirname(os.path.abspath(snakemake.output.seq))
seq_file = os.path.basename(snakemake.output.seq)
if seq_file.endswith(".seq"):
    reference_name = os.path.join(output_directory, seq_file[:-4])
else:
    raise Exception("output.seq has an invalid file suffix (must be .seq)")

for output_variable, output_path in snakemake.output.items():
    if not os.path.abspath(output_path).startswith(reference_name):
        raise Exception(
            "the path for {} is inconsistent with that of output.seq".format(
                output_variable
            )
        )

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "rsem-prepare-reference --num-threads {snakemake.threads} {extra} "
    "{snakemake.input.reference_genome} {reference_name} "
    "{log}"
)
