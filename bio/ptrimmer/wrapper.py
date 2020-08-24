__author__ = "Felix Mölder"
__copyright__ = "Copyright 2020, Felix Mölder"
__email__ = "felix.moelder@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path
import ntpath

input_reads = "-f {r1}".format(r1=snakemake.input.r1)

out_r1 = ntpath.basename(snakemake.output.r1)
output_reads = "-d {o1}".format(o1=out_r1)

if snakemake.input.get("r2", ""):
    seqmode = "pair"
    input_reads = "{reads} -r {r2}".format(reads=input_reads, r2=snakemake.input.r2)
    out_r2 = ntpath.basename(snakemake.output.r2)
    output_reads = "{reads} -e {o2}".format(reads=output_reads, o2=out_r2)
else:
    seqmode = "single"

primers = snakemake.input.primers

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

ptrimmer_params = "-t {mode} {in_reads} -a {primers} {out_reads}".format(
    mode=seqmode, in_reads=input_reads, primers=primers, out_reads=output_reads
)

process_r1 = "mv {out_read} {final_output_path}".format(
    out_read=out_r1, final_output_path=snakemake.output.r1
)

process_r2 = ""
if snakemake.input.get("r2", ""):
    process_r2 = "&& mv {out_read} {final_output_path}".format(
        out_read=out_r2, final_output_path=snakemake.output.r2
    )

shell("(ptrimmer {ptrimmer_params} && {process_r1} {process_r2}) {log}")
