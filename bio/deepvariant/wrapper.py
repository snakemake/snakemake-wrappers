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

# sample name defaults to basename
sample_name = snakemake.params.get(
    "sample_name", os.path.splitext(os.path.basename(snakemake.input.bam))[0]
)


make_examples_gvcf = postprocess_gvcf = ""
gvcf = snakemake.output.get("gvcf", None)
if gvcf:
    make_examples_gvcf = "--gvcf {tmp_dir} "
    postprocess_gvcf = (
        "--gvcf_infile {tmp_dir}/{sample_name}.gvcf.tfrecord@{snakemake.threads}.gz "
        "--gvcf_outfile {snakemake.output.gvcf} "
    )

with tempfile.TemporaryDirectory() as tmp_dir:
    shell(
        "(dv_make_examples.py "
        "--cores {snakemake.threads} "
        "--ref {snakemake.input.ref} "
        "--reads {snakemake.input.bam} "
        "--sample {sample_name} "
        "--examples {tmp_dir} "
        "--logdir {log_dir} " + make_examples_gvcf + "{extra} \n"
        "dv_call_variants.py "
        "--cores {snakemake.threads} "
        "--outfile {tmp_dir}/{sample_name}.tmp "
        "--sample {sample_name} "
        "--examples {tmp_dir} "
        "--model {snakemake.params.model} \n"
        "dv_postprocess_variants.py "
        "--ref {snakemake.input.ref} "
        + postprocess_gvcf
        + "--infile {tmp_dir}/{sample_name}.tmp "
        "--outfile {snakemake.output.vcf} ) {log}"
    )
