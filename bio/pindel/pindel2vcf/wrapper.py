__author__ = "Johannes Köster, Patrik Smeds"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

expected_endings = [
    "INT",
    "D",
    "SI",
    "INV",
    "INV_final",
    "TD",
    "LI",
    "BP",
    "CloseEndMapped",
    "RP",
]


def split_file_name(file_parts, file_ending_index):
    return (
        "_".join(file_parts[:file_ending_index]),
        "_".join(file_parts[file_ending_index:]),
    )


def process_input_path(input_file):
    """
    :params input_file: Input file from rule, ex /path/to/file/all_D or /path/to/file/all_INV_final
    :return: ""/path/to/file", "all"

    """
    file_path, file_name = os.path.split(input_file)
    file_parts = file_name.split("_")
    # seperate ending and name, to name: all ending: D or name: all ending: INV_final
    file_name, file_ending = split_file_name(
        file_parts, -2 if file_name.endswith("_final") else -1
    )
    if not file_ending in expected_endings:
        raise Exception("Unexpected variant type: " + file_ending)
    return file_path, file_name


with tempfile.TemporaryDirectory() as tmpdirname:
    input_flag = "-p"
    input_file = snakemake.input.get("pindel")
    if isinstance(input_file, list) and len(input_file) > 1:
        input_flag = "-P"
        input_path, input_name = process_input_path(input_file[0])
        input_file = os.path.join(input_path, input_name)
        for variant_input in snakemake.input.pindel:
            if not variant_input.startswith(input_file):
                raise Exception(
                    "Unable to extract common path from multi file input, expect path is: "
                    + input_file
                )
            if not os.path.isfile(variant_input):
                raise Exception('Input "' + input_file + '" is not a file!')
            os.symlink(
                os.path.abspath(variant_input),
                os.path.join(tmpdirname, os.path.basename(variant_input)),
            )
        input_file = os.path.join(tmpdirname, input_name)
    shell(
        "pindel2vcf {snakemake.params.extra} {input_flag} {input_file} -r {snakemake.input.ref} -R {snakemake.params.refname} -d {snakemake.params.refdate} -v {snakemake.output[0]} {log}"
    )
