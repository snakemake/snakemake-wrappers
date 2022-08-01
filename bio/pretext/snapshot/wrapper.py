__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


out_maps = snakemake.output.keys()
sequences = "=" + ", =".join(snakemake.output.keys())


format = Path(snakemake.output.full).suffix.removeprefix(".")
if format == "jpg":
    format = "jpeg"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "PretextSnapshot"
        " --map {snakemake.input[0]}"
        " {extra}"
        " --sequences {sequences:q}"
        " --format {format}"
        " --folder {tmpdir}"
        " --prefix out_"
        " {log}"
    )

    if snakemake.output.get("full"):
        shell("mv {tmpdir}/out_FullMap.{format} {snakemake.output.full}")
    if snakemake.output.get("all"):
        Path(snakemake.output.all).mkdir(parents=True, exist_ok=True)
        shell("mv {tmpdir}/out_*.{format} {snakemake.output.all}/.")
