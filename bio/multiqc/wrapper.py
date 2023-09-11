"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Set this to False if multiqc should use the actual input directly
# instead of parsing the folders where the provided files are located
use_input_files_only = snakemake.params.get("use_input_files_only", False)
if not use_input_files_only:
    input_data = set(Path(fp).parent for fp in snakemake.input)
else:
    input_data = set(snakemake.input)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "multiqc"
        " {extra}"
        " --outdir {tmpdir}"
        " --filename out"
        " {input_data}"
        " {log}"
    )

    for output in snakemake.output:
        if output.endswith("_data"):
            ext = "_data"
        elif output.endswith(".zip"):
            ext = "_data.zip"
        else:
            ext = Path(output).suffix
        shell("mv {tmpdir}/out{ext} {output}")
