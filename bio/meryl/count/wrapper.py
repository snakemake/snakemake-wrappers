__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


command = snakemake.params.get("command", "count")
assert command in [
    "count",
    "count-forward",
    "count-reverse",
], "invalid command specified."


mem_gb = get_mem(snakemake, out_unit="GiB")


shell(
    "meryl"
    " {command}"
    " threads={snakemake.threads}"
    " memory={mem_gb}"
    " {extra}"
    " {snakemake.input}"
    " output {snakemake.output}"
    " {log}"
)
