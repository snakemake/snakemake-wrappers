__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

import os
from snakemake.shell import shell
import sys

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


def check_file_exists(filename):
    if filename is not None and not os.path.exists(filename):
        raise FileNotFoundError(filename)


def check_bedfiles(argstring):
    include_bedfile = None
    exclude_bedfile = None
    extra_params = argstring.split()

    # Get bed file arguments, if supplied
    for i, arg in enumerate(extra_params):
        if arg == "-j" or arg == "--include":
            include_bedfile = extra_params[i + 1]
            continue
        if arg == "-J" or arg == "--exclude":
            exclude_bedfile = extra_params[i + 1]
            continue

    check_file_exists(include_bedfile)
    check_file_exists(exclude_bedfile)


try:
    check_bedfiles(extra)
except FileNotFoundError as e:
    with open(str(snakemake.log), "a") as logfile:
        print("error: file not found: {}".format(e), file=logfile)
    sys.exit(1)

shell(
    "pindel -T {snakemake.threads} {snakemake.params.extra} -i {snakemake.input.config} "
    "-f {snakemake.input.ref} -o {snakemake.params.prefix} {log}"
)
