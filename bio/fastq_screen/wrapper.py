import os
import re
from snakemake.shell import shell
import tempfile

__author__ = "Ryan Dale, Thibault Dayris"
__copyright__ = "Copyright 2016, Ryan Dale"
__email__ = "dalerr@niddk.nih.gov, thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

_config = snakemake.params["fastq_screen_config"]

subset = snakemake.params.get("subset", 100000)
aligner = snakemake.params.get("aligner", "bowtie2")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

# fastq_screen hard-codes filenames according to this prefix. We will send
# hard-coded output to a temp dir, and then move them later.
prefix = re.split(".fastq|.fq|.txt|.seq", os.path.basename(snakemake.input[0]))[0]


with tempfile.TemporaryDirectory() as tempdir:
    # snakemake.params.fastq_screen_config can be either a dict or a string. If
    # string, interpret as a filename pointing to the fastq_screen config file.
    # Otherwise, create a new tempfile out of the contents of the dict:
    if isinstance(_config, dict):
        config_file = f"{tempdir}/fastq_screen_config.txt"

        with open(config_file, "w") as fout:
            for label, indexes in _config["database"].items():
                for aligner, index in indexes.items():
                    fout.write(
                        "\t".join(["DATABASE", label, index, aligner.upper()]) + "\n"
                    )
                for aligner, path in _config["aligner_paths"].items():
                    fout.write("\t".join([aligner.upper(), path]) + "\n")
    else:
        config_file = _config

    shell(
        "fastq_screen --outdir {tempdir} "
        "--force "
        "--aligner {aligner} "
        "--conf {config_file} "
        "--subset {subset} "
        "--threads {snakemake.threads} "
        "{extra} "
        "{snakemake.input[0]} "
        "{log}"
    )

    # Move output to the filenames specified by the rule if user expects them
    txt = snakemake.output.get("txt")
    if txt:
        shell("mv --verbose {tempdir}/{prefix}_screen.txt {txt} {log}")

    png = snakemake.output.get("png")
    if png:
        shell("mv --verbose {tempdir}/{prefix}_screen.png {png} {log}")

    conf = snakemake.output.get("conf")
    if conf:
        shell("mv --verbose {config_file} {conf} {log}")
