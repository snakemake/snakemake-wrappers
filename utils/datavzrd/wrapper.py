__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"

import tempfile
from yte import process_yaml
from snakemake.shell import shell
import shutil
import sys

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

with tempfile.NamedTemporaryFile(mode="w") as processed, open(
    snakemake.input.config
) as f:
    with open(snakemake.log[0], "a") as log_file:
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = log_file
        try:
            # support templating in the config file
            process_yaml(
                f,
                outfile=processed,
                variables={
                    "snakemake": snakemake,
                    # keep the ones below for backwards compatibility
                    "params": snakemake.params,
                    "wildcards": snakemake.wildcards,
                    "input": snakemake.input,
                },
                require_use_yte=True,
            )
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr
    processed.flush()

    if config_out := snakemake.output.get("config"):
        shutil.copy(processed.name, config_out)
    shell("datavzrd {processed.name} {extra} --output {snakemake.output[0]} {log}")
