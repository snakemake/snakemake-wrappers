__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")


sorting = snakemake.params.get("sorting")
sort_pipe = snakemake.params.get("sort_extra", "")
if sorting:
    sort_pipe = f"| sortBed {sort_pipe}"
else:
    sort_pipe = ""


shell(
    "(bamToBed"
    " {extra}"
    " -i {snakemake.input[0]}"
    " {sort_pipe}"
    " > {snakemake.output[0]}"
    ") {log}"
)
