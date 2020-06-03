__author__ = "Tetsuro Hisayoshi"
__copyright__ = "Copyright 2020, Tetsuro Hisayoshi"
__email__ = "hisayoshi0530@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

log_dir = os.path.dirname(str(snakemake.log))
output_dir = os.path.dirname(str(snakemake.output))

# sample basename
basename = os.path.splitext(os.path.basename(str(snakemake.input.bam)))[0]


shell(
    "(mkdir -p {output_dir}/{basename} \n"
    "dv_make_examples.py "
    "--cores {snakemake.threads} " 
    "--ref {snakemake.input.ref} "
    "--reads {snakemake.input.bam} "
    "--sample {basename} "
    "--examples {output_dir}/{basename} "
    "--logdir {log_dir} \n"
    "dv_call_variants.py "
    "--cores {snakemake.threads} "
    "--outfile {output_dir}/{basename}.tmp "
    "--sample {basename} "
    "--examples {output_dir}/{basename} "
    "--model {snakemake.params.model} \n"
    "dv_postprocess_variants.py "
    "--ref {snakemake.input.ref} "
    "--infile {output_dir}/{basename}.tmp "
    "--outfile {snakemake.output.vcf} \n"
    "rm -rf {output_dir}/{basename}.tmp ) {log}"
)