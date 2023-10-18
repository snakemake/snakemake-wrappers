__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

import logging
from os import listdir
from os.path import basename
from os.path import dirname
from os.path import join
from tempfile import TemporaryDirectory
import shutil
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)


input_bam_files = f"{snakemake.input.bam}"

target = ""
antitarget = ""
ref_fasta = ""
mappability = ""

create_reference = snakemake.output.get("reference", False)
if create_reference:
    input_bam_files = f"-n {input_bam_files}"
    ref_fasta = "-f {snakemake.input.fasta}"
    target = "-t {snakemake.input.target}"
    antitarget = "-a {snakemake.input.antitarget}"

    if "mappability" in snakemake.input:
        mappability = f"-g {snakemake.input.mappability}"

    if len(snakemake.output) > 1:
        exception_message = (
            "Only one output expected when creating a reference, multiple output "
            f"files defined as output: [{snakemake.output}]"
        )
        raise Exception(exception_message)


reference_cnv = ""
if not create_reference:
    reference_cnv = f"-r {snakemake.input.reference}"

method = snakemake.params.get("method", "hybrid")
if method:
    method = f"-m {method}"

extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tmpdirname:
    if create_reference:
        output = f"--output-reference {join(tmpdirname, 'reference.cnn')}"
        output_list = [snakemake.output.reference]
    else:
        output_list = [value for key, value in snakemake.output.items()]
        output = f"-d {tmpdirname} "
    shell(
        f"(cnvkit.py batch {input_bam_files} "
        f"{reference_cnv} "
        f"{method} "
        f"{ref_fasta} "
        f"{target} "
        f"{antitarget} "
        f"{output} "
        f"{extra}) {log}"
    )

    for output_file in output_list:
        filename = basename(output_file)
        parent = dirname(output_file)

        try:
            shutil.copy2(join(tmpdirname, filename), output_file)
        except FileNotFoundError as e:
            temp_files = listdir(tmpdirname)
            logging.error(
                f"Couldn't locate file {basename} possible files are {[basename(f) for f in temp_files]}"
            )
            raise e
