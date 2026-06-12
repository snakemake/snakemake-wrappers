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
if ab_initio_config:
    ab_initio_config = f"--ab_initio_config {ab_initio_config}"

custom_adapters = snakemake.input.get("custom_adapters", "")
if custom_adapters:
    custom_adapters = f"--custom_adapters {custom_adapters}"

consensus = snakemake.output.get("consensus", "")
if consensus:
    if not ab_initio:
        raise ValueError("output.consensus requires params.ab_initio=True")
    else:
        consensus = f"--export_consensus {consensus}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "porechop_abi"
        " -i {snakemake.input.fq:q}"
        " -o {snakemake.output.fq:q}"
        " -t {snakemake.threads}"
        " -tmp {tmpdir:q}"
        " {ab_initio_flag}"
        " {ab_initio_config}"
        " {custom_adapters}"
        " {consensus}"
        " {extra}"
        " {log}"
    )
