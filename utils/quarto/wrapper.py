__author__ = "Vito Zanotelli"
__copyright__ = "Copyright 2024, Vito Zanotelli"
__email__ = "vito.zanotelli@kispi.uzh.ch"
__license__ = "MIT"

import tempfile
from pathlib import Path
import warnings
import yaml
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


def parse_qmd_header(fn_script):
    """Parse the yml header of the a
    quarto markdown file

    Args:
        fn_script (path): Path to the qmd script

    Raises:
        ValueError: qmd has not valid header

    Returns:
        dict: parsed header
    """
    with open(fn_script, mode="r") as f:
        first = f.readline()
        if first != "---\n":
            raise ValueError(".qmd file has no valid yaml header.")
        line = f.readline()
        yml_lines = []
        while line != "---\n":
            yml_lines.append(line)
            line = f.readline()
    return yaml.safe_load("".join(yml_lines))


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


# Build params to be passed to Quarto params (-P flag)
params = []
for name, value in snakemake.input.items():
    if name not in {"renv", "script"}:
        add_parameter(name, value, params)

for name, value in snakemake.params.items():
    add_parameter(name, value, params)

for name, value in snakemake.output.items():
    if name not in {"report"}:
        add_parameter(name, value, params)


# Get the snakemake resources that correspond to
# Params in the qmd header that are prefixed with the resource prefix
# RESOURCE_PARAMS_PREFIX.
# eg resources_mem -> snakemake.resources.mem
RESOURCE_PARAMS_PREFIX = "resources_"
params_header = parse_qmd_header(script)["params"]
resources = {**snakemake.resources}
resources["threads"] = snakemake.threads
passed_resource_params = {
    f"{RESOURCE_PARAMS_PREFIX}{k}": v
    for k, v in resources.items()
    if f"{RESOURCE_PARAMS_PREFIX}{k}" in params_header.keys()
}

for name, value in passed_resource_params.items():
    add_parameter(name, value, params)


# Resolve the logfile path and set the log_fmt_shell
# This is required as we may change the working directory
# to the renv folder for execution of quarto.
logfile = snakemake.log
if logfile:
    snakemake.log = str(Path(str(logfile)).resolve())
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
else:
    log = ""

args = " ".join(params)

with tempfile.TemporaryDirectory() as temp_output:
    if report is None:
        # In case no report output is specified,
        # the output is created in a temporary folder
        out_report = Path(temp_output) / script.name
        out_report_rendered = out_report
        report_path = f"{out_report}.tmp"
    else:
        # In case an output is specified,
        # the output is created in the target folder.
        report_path = Path(report).resolve()
        # The report to-be-rendered is namespaced
        # to prevent clashes.
        out_report = (
            report_path.parent / f"{report_path.stem}_{report_path.suffix[1:]}.qmd"
        )
        # The rendered report is named as the final report with the correct suffix
        # Note that in addition ot the target report file, also a folder `*_files/`
        # is created, which contains the images and other files linked in the html report.
        out_report_rendered = out_report.with_suffix(report_path.suffix)
        if report_path.suffix == ".pdf":
            warnings.warn(
                "PDF output is likely not supported yet, as tinytex not installable"
                " via conda: https://github.com/conda-forge/quarto-feedstock/issues/26"
            )
        args += f" --to={report_path.suffix[1:]}"
    shell(
        """
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
        """
    )
