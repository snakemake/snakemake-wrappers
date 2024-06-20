__author__ = "Vito Zanotelli"
__copyright__ = "Copyright 2024, Vito Zanotelli"
__email__ = "vito.zanotelli@kispi.uzh.ch"
__license__ = "MIT"

import tempfile
from pathlib import Path
import warnings
from snakemake.shell import shell


def parse_renv(renv_path: Path) -> str:
    """Parse the renv path

    Args:
        renv_path (Path): A path to an renv folder
            or a file in the renv folder

    Returns:
        str: the resolved path pointing to the
            renv folder
    """
    if renv_path.is_file():
        renv_path = renv_path.parent
    return str(renv_path.resolve())


def add_parameter(name: str, value, param_list: list[str]) -> None:
    """Add a parameter to the parameter list in place

    Args:
        name (str): The name of the parameter
        value (str): The value of the parameter
        param_list (list[str]): The list of parameters

    Returns:
        None
    """
    if isinstance(value, list):
        value = ",".join(value)
    param_list.append("-P {}:{}".format(name, value))


renv = parse_renv(Path(snakemake.input.get("renv", ".")))
script = Path(snakemake.input.get("script"))
report = snakemake.output.get("report", None)


# Build params
params = []
for name, value in snakemake.input.items():
    if name not in {"renv", "script"}:
        add_parameter(name, value, params)

for name, value in snakemake.params.items():
    add_parameter(name, value, params)

for name, value in snakemake.output.items():
    if name not in {"report"}:
        add_parameter(name, value, params)
logfile = snakemake.log
if logfile:
    snakemake.log = str(Path(str(logfile)).resolve())
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)

args = " ".join(params)

with tempfile.TemporaryDirectory() as temp_output:
    if report is None:
        out_report = Path(temp_output) / script.name
        out_report_rendered = out_report
        report_path = f"{out_report}.tmp"
    else:
        report_path = Path(report).resolve()
        out_report = (
            report_path.parent / f"{report_path.stem}_temp_{report_path.suffix[1:]}.qmd"
        )
        out_report_rendered = out_report.with_suffix(report_path.suffix)
        if report_path.suffix == ".pdf":
            warnings.warn(
                "PDF output is likely not supported yet, as tinytex not installable"
                " via conda: https://github.com/conda-forge/quarto-feedstock/issues/26"
            )
        args += f" --to={report_path.suffix[1:]}"
    shell("""
        # copy the input script to prevent name clashes
        cp {script} {out_report}
        WD=$(pwd)
        # Change to renv directory to enable the renv
        cd "{renv}"
        quarto render {out_report} \
                {args} \
                --execute-dir="$WD" \
          {log}
        # move the output to the final destination
        mv {out_report_rendered} {report_path}
        """)
