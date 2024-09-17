__author__ = "Jamie Gooding"
__copyright__ = "Copyright 2024, Jamie Gooding"
__email__ = "jamie.gooding@cern.ch"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

object_in = snakemake.params.get("input_object_name", "")
if object_in:
    object_in = ":" + object_in

object_out = snakemake.params.get("output_object_name", "")
if object_out:
    object_out = ":" + object_out

shell(
    "rootcp {extra} {snakemake.input}{object_in} {snakemake.output}{object_out} {log}"
)
