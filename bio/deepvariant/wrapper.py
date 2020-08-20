__author__ = "Tetsuro Hisayoshi"
__copyright__ = "Copyright 2020, Tetsuro Hisayoshi"
__email__ = "hisayoshi0530@gmail.com"
__license__ = "MIT"

import os
import tempfile

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

log_dir = os.path.dirname(snakemake.log[0])
output_dir = os.path.dirname(snakemake.output[0])

# sample basename
basename = os.path.splitext(os.path.basename(snakemake.input.bam[0]))[0]


with tempfile.TemporaryDirectory() as tmp_dir:
    os.system(
        f"(dv_make_examples.py "
        f"--cores {snakemake.threads} "
        f"--ref {snakemake.input.ref} "
        f"--reads {snakemake.input.bam} "
        f"--sample {basename} "
        f"--examples {tmp_dir} "
        f"--logdir {log_dir} "
        f"{extra} \n"
        f"dv_call_variants.py "
        f"--cores {snakemake.threads} "
        f"--outfile {tmp_dir}/{basename}.tmp "
        f"--sample {basename} "
        f"--examples {tmp_dir} "
        f"--model {snakemake.params.model} \n"
        f"dv_postprocess_variants.py "
        f"--ref {snakemake.input.ref} "
        f"--infile {tmp_dir}/{basename}.tmp "
        f"--outfile {snakemake.output.vcf} ) {log}"
    )
