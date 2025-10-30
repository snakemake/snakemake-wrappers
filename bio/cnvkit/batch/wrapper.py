__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

import logging
from os import listdir
from os.path import basename
from os.path import join
from tempfile import TemporaryDirectory
import shutil
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

input_bam_files = f"{snakemake.input.bam}"

target = ""
antitarget = ""
ref_fasta = ""
reference_cnv = ""
mappability = ""

create_reference = snakemake.output.get("reference", False)
if create_reference:
    input_bam_files = f"-n {input_bam_files}"
    ref_fasta = f"-f {snakemake.input.fasta}"
    target = f"-t {snakemake.input.target}"
    antitarget = f"-a {snakemake.input.antitarget}"

    if "mappability" in snakemake.input:
        mappability = f"-g {snakemake.input.mappability}"

    if len(snakemake.output) > 1:
        exception_message = (
            "Only one output expected when creating a reference, multiple output "
            f"files defined as output: [{snakemake.output}]"
        )
        raise Exception(exception_message)
else:
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
        "(cnvkit.py batch {input_bam_files} "
        "{reference_cnv} "
        "{method} "
        "{ref_fasta} "
        "{target} "
        "{antitarget} "
        "{output} "
        "{extra}) {log}"
    )

    temp_files = sorted(listdir(tmpdirname))
    destination_paths = sorted(output_list)
    for source, destination in zip(temp_files, destination_paths):
        try:
            shutil.copy2(join(tmpdirname, source), destination)
        except FileNotFoundError as e:
            logging.error(
                f"Couldn't locate file {join(tmpdirname, source)} to copy it to {destination}. "
                f"Possible files are {[basename(f) for f in temp_files]}"
            )
            raise e
