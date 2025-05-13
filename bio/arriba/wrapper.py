__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
import subprocess as sp
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

discarded_fusions = snakemake.output.get("discarded", "")
if discarded_fusions:
    discarded_cmd = "-O " + discarded_fusions
else:
    discarded_cmd = ""

database_dir = os.path.join(os.environ["CONDA_PREFIX"], "var/lib/arriba")
build = snakemake.params.get("genome_build", None)

blacklist_input = snakemake.input.get("custom_blacklist")
default_blacklist = snakemake.params.get("default_blacklist", False)

default_known_fusions = snakemake.params.get("default_known_fusions", False)

if default_blacklist or default_known_fusions:
    if not build:
        raise ValueError(
            "Please provide a genome build when using blacklist- or known_fusion-filtering"
        )
    command = "arriba -h | grep -e 'Arriba ' -e '^Version: ' | grep -om1 '[0-9.]\\+$'"
    arriba_vers = sp.run(
        command, shell=True, capture_output=True, text=True
    ).stdout.strip()

if blacklist_input and not default_blacklist:
    blacklist_cmd = "-b " + blacklist_input
elif not blacklist_input and default_blacklist:
    blacklist_dict = {
        "GRCh37": f"blacklist_hg19_hs37d5_GRCh37_v{arriba_vers}.tsv.gz",
        "GRCh38": f"blacklist_hg38_GRCh38_v{arriba_vers}.tsv.gz",
        "GRCm38": f"blacklist_mm10_GRCm38_v{arriba_vers}.tsv.gz",
        "GRCm39": f"blacklist_mm39_GRCm39_v{arriba_vers}.tsv.gz",
    }
    blacklist_path = os.path.join(database_dir, blacklist_dict[build])
    blacklist_cmd = "-b " + blacklist_path
elif not blacklist_input and not default_blacklist:
    blacklist_cmd = "-f blacklist"
else:
    raise ValueError(
        "custom_blacklist input file and default_blacklist parameter option defined. Please set only one of both."
    )

if default_known_fusions:
    fusions_dict = {
        "GRCh37": f"known_fusions_hg19_hs37d5_GRCh37_v{arriba_vers}.tsv.gz",
        "GRCh38": f"known_fusions_hg38_GRCh38_v{arriba_vers}.tsv.gz",
        "GRCm38": f"known_fusions_mm10_GRCm38_v{arriba_vers}.tsv.gz",
        "GRCm39": f"known_fusions_mm39_GRCm39_v{arriba_vers}.tsv.gz",
    }
    known_fusions_path = os.path.join(database_dir, fusions_dict[build])
    known_cmd = "-k " + known_fusions_path
else:
    known_cmd = ""

sv_file = snakemake.params.get("sv_file")
if sv_file:
    sv_cmd = "-d " + sv_file
else:
    sv_cmd = ""

shell(
    "arriba "
    "-x {snakemake.input.bam} "
    "-a {snakemake.input.genome} "
    "-g {snakemake.input.annotation} "
    "{blacklist_cmd} "
    "{known_cmd} "
    "{sv_cmd} "
    "-o {snakemake.output.fusions} "
    "{discarded_cmd} "
    "{extra} "
    "{log}"
)
