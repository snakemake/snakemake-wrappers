__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)


command = snakemake.params.get("command", "union")
assert command in [
    "union",
    "union-min",
    "union-max",
    "union-sum",
    "intersect",
    "intersect-min",
    "intersect-max",
    "intersect-sum",
    "subtract",
    "difference",
    "symmetric-difference",
], "invalid command specified."


shell("meryl {command} {snakemake.input} output {snakemake.output} {log}")
