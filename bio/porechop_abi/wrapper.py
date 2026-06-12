"""Snakemake wrapper for porechop_abi."""

__author__ = "Snakemake Wrapper Team"
__copyright__ = "Copyright 2026, Snakemake Wrapper Team"
__email__ = ""
__license__ = "MIT"

import tempfile

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
ab_initio = snakemake.params.get("ab_initio", False)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

ab_initio_flag = "--ab_initio" if ab_initio else ""
ab_initio_config = snakemake.input.get("ab_initio_config", "")
ab_initio_config_arg = (
    f"--ab_initio_config {ab_initio_config:q}" if ab_initio_config else ""
)

custom_adapters = snakemake.input.get("custom_adapters", "")
custom_adapters_arg = (
    f"--custom_adapters {custom_adapters:q}" if custom_adapters else ""
)

consensus = snakemake.output.get("consensus", "")
if consensus and not ab_initio:
    raise ValueError("output.consensus requires params.ab_initio=True")
consensus_arg = f"--export_consensus {consensus:q}" if consensus else ""

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "porechop_abi"
        " -i {snakemake.input.fq:q}"
        " -o {snakemake.output.fq:q}"
        " -t {snakemake.threads}"
        " -tmp {tmpdir:q}"
        " {ab_initio_flag}"
        " {ab_initio_config_arg}"
        " {custom_adapters_arg}"
        " {consensus_arg}"
        " {extra}"
        " {log}"
    )
