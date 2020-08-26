"""Snakemake wrapper for Bismark bismark2bedGraph tool."""
# https://github.com/FelixKrueger/Bismark/blob/master/bismark2bedGraph

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


import os

bedGraph = snakemake.output.get("bedGraph", "")
if not bedGraph:
    raise ValueError("bismark/bismark2bedGraph: Please specify bedGraph output path")

params_extra = snakemake.params.get("extra", "")
cmdline_args = [f"bismark2bedGraph {params_extra}"]

dir_name = os.path.dirname(bedGraph)
if dir_name:
    cmdline_args.append(f"--dir {dir_name}")

fname = os.path.basename(bedGraph)
cmdline_args.append(f"--output {fname}")

cmdline_args.append(f"{snakemake.input}")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmdline_args.append(f"{log}")

# run
command = " ".join(cmdline_args)
os.system(command)
