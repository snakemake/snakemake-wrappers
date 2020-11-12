__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
sort_file = snakemake.input.get("sort_file", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if sort_file:
    if not "-g" in extra and not "-faidx" in extra:
        extra = "-g"
else:
    if "-g" in extra or "-faidx" in extra:
        sys.exit(
            "The -g or -faidx option requires as input a sort_file that determines the sorting order and contains the chromosome names."
        )

shell(
    "(bedtools sort"
    " {extra} {sort_file}"
    " -i {snakemake.input.in_file}"
    " > {snakemake.output[0]})"
    " {log}"
)
