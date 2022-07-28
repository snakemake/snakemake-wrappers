__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


format = Path(snakemake.output[0]).suffix.removeprefix(".")
if format == "jpg":
    format = "jpeg"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "PretextSnapshot"
        " --map {snakemake.input[0]}"
        " {extra}"
        " --format {format}"
        " --folder {tmpdir}"
        " --prefix out_"
        " {log}"
    )

    if snakemake.output.get("xx"):
        shell("mv {tmpdir}/out_xx.{format} {snakemake.output.xx}")
    if snakemake.output.get("full_map"):
        shell("mv {tmpdir}/out_FullMap.{format} {snakemake.output.full_map}")
