__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

import os
import os.path as path
import sys

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

control = snakemake.input.get("control", "")
if control == "":
    control_command = ""
else:
    control_command = "-i " + control

os.system(
    f"(findPeaks"
    f" {snakemake.input.tag}"
    f" -style {snakemake.params.style}"
    f" {extra}"
    f" {control_command}"
    f" -o {snakemake.output})"
    f" {log}"
)
