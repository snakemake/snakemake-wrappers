__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2022, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell
from tempfile import TemporaryDirectory

# Formats the log redrection string
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    # Executed shell command
    html_path = f"{tempdir}/genefuse.html"
    json_path = f"{tempdir}/genefuse.json"
    txt_path = f"{tempdir}/gene_fuse_fusions.txt"
    shell(
        "(genefuse "
        "-r {snakemake.input.reference} "
        "-t {snakemake.threads} "
        "-f {snakemake.input.config} "
        "-1 {snakemake.input.fastq1} "
        "-2 {snakemake.input.fastq2} "
        f"-h {html_path} "
        f"-h {json_path} "
        "{extra} > "
        f"{txt_path} "
        "{log}"
    )

    if snakemake.output.get('html', None):
        shell(f"mv {html_path} {snakemake.output.html}")

    if snakemake.output.get('json', None):
        shell(f"mv {json_path} {snakemake.output.json}")

    if snakemake.output.get('fusions', None):
        shell(f"mv {txt_path} {snakemake.output.fusions}")
