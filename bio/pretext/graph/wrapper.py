__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


if snakemake.input[0].endswith(".gz"):
    pipe = "gunzip -c"
elif snakemake.input[0].endswith(".bz2"):
    pipe = "bunzip2 -c"
else:
    pipe = "cat"


shell(
    "({pipe}"
    " {snakemake.input.bedgraph} | "
    "PretextGraph"
    " -i {snakemake.input.map}"
    " -n {snakemake.params.graph_name}"
    " {extra}"
    " -o {snakemake.output}"
    ") {log}"
)
