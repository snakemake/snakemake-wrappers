__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from os import listdir
from os.path import join
from tempfile import TemporaryDirectory
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

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
    else:
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

    # actual generated files
    temp_files = listdir(tmpdirname)

    # mapping of file suffixes to snakemake.output attributes
    file_map = {
        ".antitargetcoverage.cnn": "antitarget_coverage",
        ".bintest.cns": "bins",
        ".cnr": "regions",
        ".call.cns": "segments_called",
        ".targetcoverage.cnn": "target_coverage",
        ".cns": "segments",
        "reference.cnn": "reference",
    }

    mapping = {}

    # find matches btw generated files and snakemake output
    for suffix, attr in file_map.items():
        if not snakemake.output.get(attr):
            continue
        for file in temp_files:
            if file.endswith(suffix):
                # Skip ambiguous matches
                if attr == "segments" and any(
                    x in file for x in ["call.cns", "bintest.cns"]
                ):
                    continue
                mapping[attr] = join(tmpdirname, file)
                break  # stop after first match

    for file in move_files(snakemake, mapping):
        shell("{file} {log}")
