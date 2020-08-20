__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os

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

os.system(
    f"arriba "
    f"-x {snakemake.input.bam} "
    f"-a {snakemake.input.genome} "
    f"-g {snakemake.input.annotation} "
    f"{blacklist_cmd} "
    f"{known_cmd} "
    f"{sv_cmd} "
    f"-o {snakemake.output.fusions} "
    f"{discarded_cmd} "
    f"{extra} "
    f"{log}"
)
