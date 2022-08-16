__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True)


command = snakemake.params.get("command", "statistics")
assert command in [
    "statistics",
    "histogram",
    "print",
], "invalid command specified."


shell("meryl {command} {snakemake.input} > {snakemake.output} {log}")
