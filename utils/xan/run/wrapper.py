# coding: utf-8

"""This snakemake wrapper handle xan pipelines run"""

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

script = snakemake.input.get("script")
if script:
    extra += f" --file '{script}'"

expression = snakemake.params.get("expression", "")
if script and expression:
    raise ValueError("Either provide a xan script, or a xan run expression. Not both.")
elif not (script or expression):
    raise ValueError("Please provide either a xan script or a xan run expression.")

shell(
    "xan run {extra} {expression:q} {snakemake.input.data:q} "
    "> {snakemake.output[0]:q} {log}"
)
