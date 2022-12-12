__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
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
blacklist = snakemake.params.get("default_blacklist", False)

known_fusions = snakemake.params.get("default_known_fusions", False)

if (blacklist or known_fusions) and not build:
    raise ValueError(
        "Please provide a genome build when using blacklist- or known_fusion-filtering"
    )


if blacklist_input and not blacklist:
    blacklist_cmd = "-b " + blacklist_input
elif not blacklist_input and blacklist:
    blacklist_dict = {
        "GRCh37": "blacklist_hg19_hs37d5_GRCh37_v2.3.0.tsv.gz",
        "GRCh38": "blacklist_hg38_GRCh38_v2.3.0.tsv.gz",
        "GRCm38": "blacklist_mm10_GRCm38_v2.3.0.tsv.gz",
        "GRCm39": "blacklist_mm39_GRCm39_v2.3.0.tsv.gz",
    }
    blacklist_path = os.path.join(database_dir, blacklist_dict[build])
    blacklist_cmd = "-b " + blacklist_path
elif not blacklist_input and not blacklist:
    blacklist_cmd = "-f blacklist"
else:
    raise ValueError(
        "blacklist input file and blacklist parameter option defined. Please set only one of both."
    )

if known_fusions:
    fusions_dict = {
        "GRCh37": "known_fusions_hg19_hs37d5_GRCh37_v2.3.0.tsv.gz",
        "GRCh38": "known_fusions_hg38_GRCh38_v2.3.0.tsv.gz",
        "GRCm38": "known_fusions_mm10_GRCm38_v2.3.0.tsv.gz",
        "GRCm39": "known_fusions_mm39_GRCm39_v2.3.0.tsv.gz",
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
