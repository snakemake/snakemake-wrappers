__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

r1 = snakemake.input.get("read1")
r2 = snakemake.input.get("read2")
assert r1 is not None and r2 is not None, "r1 and r2 files are required as input"

assembled = snakemake.output.get("assembled")
assert assembled is not None, "require 'assembled' outfile"
gzip = True if assembled.endswith(".gz") else False

out_base, out_end = assembled.rsplit(".f")
out_end = ".f" + out_end

df_assembled = out_base + ".assembled.fastq"
df_discarded = out_base + ".discarded.fastq"
df_unassembled_r1 = out_base + ".unassembled.forward.fastq"
df_unassembled_r2 = out_base + ".unassembled.reverse.fastq"

df_outputs = [df_assembled, df_discarded, df_unassembled_r1, df_unassembled_r2]

discarded = snakemake.output.get("discarded", out_base + ".discarded" + out_end)
unassembled_r1 = snakemake.output.get(
    "unassembled_read1", out_base + ".unassembled_r1" + out_end
)
unassembled_r2 = snakemake.output.get(
    "unassembled_read2", out_base + ".unassembled_r2" + out_end
)

final_outputs = [assembled, discarded, unassembled_r1, unassembled_r2]


def move_files(in_list, out_list, gzip):
    for f, o in zip(in_list, out_list):
        if f != o:
            if gzip:
                shell("gzip -9 -c {f} > {o}")
                shell("rm -f {f}")
            else:
                shell("cp {f} {o}")
                shell("rm -f {f}")
        elif gzip:
            shell("gzip -9 {f}")


pval = float(snakemake.params.get("pval", ".01"))
max_mem = snakemake.resources.get("mem_mb", "4000")
extra = snakemake.params.get("extra", "")

shell(
    "pear -f {r1} -r {r2} -p {pval} -j {snakemake.threads} -y {max_mem} {extra} -o {out_base} {log}"
)

move_files(df_outputs, final_outputs, gzip)
