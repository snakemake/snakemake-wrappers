__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os
import sys
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

in_contr = snakemake.input.get("control")
params = "{}".format(snakemake.params)
out_file = snakemake.output[0]
out_name = ""
opt_input = ""

exts = {
    "_peaks.xls",
    "_peaks.narrowPeak",
    "_summits.bed",
    "_peaks.broadPeak",
    "_peaks.gappedPeak",
    "_treat_pileup.bdg",
    "_control_lambda.bdg",
}

for ext in exts:
    if out_file.endswith(ext):
        out_name = out_file[: -len(ext)]
        out_dir = os.path.dirname(out_file)
        list(
            map(os.unlink, (os.path.join(out_dir, i) for i in os.listdir(out_dir)))
        )  # removes old result files
        os.makedirs(out_dir, exist_ok=True)
        break

if in_contr:
    opt_input = " -c {contr}".format(contr=in_contr)

if " --broad" in params:
    for out in snakemake.output:
        if out.endswith("_peaks.narrowPeak") or out.endswith("_summits.bed"):
            sys.exit(
                "If --broad option in params is given, the _peaks.narrowPeak and _summits.bed files will not be created. \n"
                "Remove --broad option from params if these files are needed.\n"
            )
else:
    for out in snakemake.output:
        if out.endswith("_peaks.broadPeak") or out.endswith("_peaks.gappedPeak"):
            sys.exit(
                "If --broad option in params is not given, the _peaks.broadPeak and _peaks.gappedPeak files will not be created. \n"
                "Add --broad option to params if these files are needed.\n"
            )

for out in snakemake.output:
    if out.endswith("_treat_pileup.bdg") or out.endswith("_control_lambda.bdg"):
        if (
            "--bdg" not in params
            and " -B " not in params
            and not params.endswith(" -B")
        ):
            params = "{params} {bdg}".format(params=params, bdg="--bdg")
            break

shell(
    "(macs2 callpeak "
    "-t {snakemake.input.treatment} "
    "{opt_input} "
    "-n {out_name} "
    "{params}) {log}"
)
