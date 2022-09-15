__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


command = snakemake.params.get("command", "view")
assert command in [
    "view",
    "stat",
    "gfa2fa",
    "gfa2bed",
    "blacklist",
    "bubble",
    "asm",
    "sql",
    "version",
], "invalid command specified."


shell("gfatools {command} {extra} {snakemake.input[0]} > {snakemake.output[0]} {log}")
