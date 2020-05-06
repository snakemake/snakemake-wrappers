__author__ = "Felix Mölder"
__copyright__ = "Copyright 2020, Felix Mölder"
__email__ = "felix.moelder@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path
import ntpath

reads="-f {r1}".format(r1=snakemake.input.r1)
read_prefix=ntpath.basename(snakemake.input.r1).split("_R1")[0]
intermediate_output_r1 = snakemake.output.r1.strip(".gz")

if snakemake.input.get("r2", ""):
    seqmode = "pair"
    reads="{reads} -r {r2}".format(reads=reads, r2=snakemake.input.r2)
    intermediate_output_r2 = snakemake.output.r2.strip(".gz")
else:
    seqmode = "single"

primers = snakemake.params.primers
outdir = Path(snakemake.output[0]).parent.resolve()
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("ptrimmer -s {seqmode} {reads} -a {primers} -o {output_dir} {log}")
shell("mv {output_dir}/{read_prefix}_trim_R1.fq > {intermediate_output_r1}")
if snakemake.output.r1.endswith(".gz"):
    shell("gzip -9 -c {intermediate_output_r1}> {snakemake.output.r1}")

if snakemake.input.get("r2", ""):
    shell("mv {output_dir}/{read_prefix}_trim_R2.fq > {intermediate_output_r2}")
    if snakemake.output.r2.endswith(".gz"):
        shell("gzip -9 -c {intermediate_output_r2}> {snakemake.output.r2}")
