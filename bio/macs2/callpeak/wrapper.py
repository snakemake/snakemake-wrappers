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
opt_input = ""
out_dir = ""

ext = "_peaks.xls"
out_file = [o for o in snakemake.output if o.endswith(ext)][0]
out_name = os.path.basename(out_file[: -len(ext)])
out_dir = os.path.dirname(out_file)

if in_contr:
    opt_input = "-c {contr}".format(contr=in_contr)

if out_dir:
    out_dir = "--outdir {dir}".format(dir=out_dir)

if any(out.endswith(("_peaks.narrowPeak", "_summits.bed")) for out in snakemake.output):
    if any(
        out.endswith(("_peaks.broadPeak", "_peaks.gappedPeak"))
        for out in snakemake.output
    ):
        sys.exit(
            "Output files with _peaks.narrowPeak and/or _summits.bed extensions cannot be created together with _peaks.broadPeak and/or _peaks.gappedPeak extended output files.\n"
            "For usable extensions please see https://snakemake-wrappers.readthedocs.io/en/stable/wrappers/macs2/callpeak.html.\n"
        )
    else:
        if " --broad" in params:
            sys.exit(
                "If --broad option in params is given, the _peaks.narrowPeak and _summits.bed files will not be created. \n"
                "Remove --broad option from params if these files are needed.\n"
            )

if any(
    out.endswith(("_peaks.broadPeak", "_peaks.gappedPeak")) for out in snakemake.output
):
    if "--broad " not in params and not params.endswith("--broad"):
        params += " --broad "

if any(
    out.endswith(("_treat_pileup.bdg", "_control_lambda.bdg"))
    for out in snakemake.output
):
    if all(p not in params for p in ["--bdg", "-B"]):
        params += " --bdg "
else:
    if any(p in params for p in ["--bdg", "-B"]):
        sys.exit(
            "If --bdg or -B option in params is given, the _control_lambda.bdg and _treat_pileup.bdg extended files must be specified in output. \n"
        )

shell(
    "(macs2 callpeak "
    "-t {snakemake.input.treatment} "
    "{opt_input} "
    "{out_dir} "
    "-n {out_name} "
    "{params}) {log}"
)
