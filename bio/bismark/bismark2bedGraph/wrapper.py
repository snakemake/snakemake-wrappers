"""Snakemake wrapper for Bismark bismark2bedGraph tool."""

# https://github.com/FelixKrueger/Bismark/blob/master/bismark2bedGraph

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

bedGraph = snakemake.output.get("bedGraph", "")
if not bedGraph:
    raise ValueError("bismark/bismark2bedGraph: Please specify bedGraph output path")

params_extra = snakemake.params.get("extra", "")
cmdline_args = ["bismark2bedGraph {params_extra}"]

dir_name = os.path.dirname(bedGraph)
if dir_name:
    cmdline_args.append("--dir {dir_name}")

fname = os.path.basename(bedGraph)
cmdline_args.append("--output {fname}")

cmdline_args.append("{snakemake.input}")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmdline_args.append("{log}")

# run
shell(" ".join(cmdline_args))
