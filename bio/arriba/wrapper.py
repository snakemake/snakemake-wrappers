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

blacklist = snakemake.params.get("blacklist")
if blacklist:
    blacklist_cmd = "-b " + blacklist
else:
    blacklist_cmd = ""

known_fusions = snakemake.params.get("known_fusions")
if known_fusions:
    known_cmd = "-k" + known_fusions
else:
    known_cmd = ""

sv_file = snakemake.params.get("sv_file")
if sv_file:
    sv_cmd = "-d" + sv_file
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
