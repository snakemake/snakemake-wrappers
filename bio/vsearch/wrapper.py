__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


# Parse input files
input = " ".join([f"--{key} {value}" for key, value in snakemake.input.items()])

# Parse output files
out_list = list()
for key, value in snakemake.output.items():
    if value.endswith(".gz"):
        out_list.append(f"--{key} /dev/stdout | gzip > {value}")
    elif value.endswith(".bz2"):
        out_list.append(f"--{key} /dev/stdout | bzip2 > {value}")
    else:
        out_list.append(f"--{key} {value}")

# Check which output files are to be compressed
out_gz = [out.endswith(".gz") for out in out_list]
out_bz2 = [out.endswith(".bz2") for out in out_list]
assert sum(out_gz + out_bz2) <= 1, "only one output can be compressed"

# Move compressed file (if any) to last
output = [
    out for _, out in sorted(zip([x | y for x, y in zip(out_gz, out_bz2)], out_list))
]


shell("(vsearch --threads {snakemake.threads} {input} {extra} {output}) {log}")
