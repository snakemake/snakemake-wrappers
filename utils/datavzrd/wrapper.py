__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"

import tempfile
from yte import process_yaml
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

with tempfile.NamedTemporaryFile(mode="w") as processed, open(
    snakemake.input.config
) as f:
    # support templating in the config file
    process_yaml(
        f,
        outfile=processed,
        variables={
            "params": snakemake.params,
            "wildcards": snakemake.wildcards,
            "input": snakemake.input,
        },
        require_use_yte=True,
    )
    processed.flush()

    shell("datavzrd {processed.name} {extra} --output {snakemake.output[0]} {log}")
