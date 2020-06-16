__author__ = "Tetsuro Hisayoshi"
__copyright__ = "Copyright 2020, Tetsuro Hisayoshi"
__email__ = "hisayoshi0530@gmail.com"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

log_dir = os.path.dirname(snakemake.log[0])
output_dir = os.path.dirname(snakemake.output[0])

# sample basename
basename = os.path.splitext(os.path.basename(snakemake.input.bam[0]))[0]


with tempfile.TemporaryDirectory() as tmp_dir:
    shell(
        "(dv_make_examples.py "
        "--cores {snakemake.threads} "
        "--ref {snakemake.input.ref} "
        "--reads {snakemake.input.bam} "
        "--sample {basename} "
        "--examples {tmp_dir} "
        "--logdir {log_dir} "
        "{extra} \n"
        "dv_call_variants.py "
        "--cores {snakemake.threads} "
        "--outfile {tmp_dir}/{basename}.tmp "
        "--sample {basename} "
        "--examples {tmp_dir} "
        "--model {snakemake.params.model} \n"
        "dv_postprocess_variants.py "
        "--ref {snakemake.input.ref} "
        "--infile {tmp_dir}/{basename}.tmp "
        "--outfile {snakemake.output.vcf} ) {log}"
    )
