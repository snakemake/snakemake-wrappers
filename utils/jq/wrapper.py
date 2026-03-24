# coding: utf-8

"""Snakemake wrapper for jq"""
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# jq expression should be quoted
expression = snakemake.params.get("expression", ".")

shell("jq {extra} {expression:q} {snakemake.input[0]} > {snakemake.output[0]} {log}")
