"""Snakemake wrapper for Salmon Quant"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

def manual_decompression (reads, zip_ext):
    """ Allow *.bz2 input into salmon. Also provide same
    decompression for *gz files, as salmon devs mention
    it may be faster in some cases."""
    if zip_ext and reads:
        if zip_ext == 'bz2':
            reads = ' < (bunzip2 -c ' + reads + ')'
        elif zip_ext == 'gz':
            reads = ' < (gunzip -c ' + reads + ')'
    return reads

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
zip_extension = snakemake.params.get("zip_extension", "")
libtype = snakemake.params.get("libtype", "A")

r1 = snakemake.input.get("r1")
r2 =  snakemake.input.get("r2")
r = snakemake.input.get("r")

assert (r1 is not None and r2 is not None) or r is not None, "either r1 and r2 (paired), or r (unpaired) are required as input"
if r1:
    r1 = [snakemake.input.r1] if isinstance(snakemake.input.r1, str) else snakemake.input.r1
    r2 = [snakemake.input.r2] if isinstance(snakemake.input.r2, str) else snakemake.input.r2
    assert len(r1) == len(r2), "input-> equal number of files required for r1 and r2"
    r1_cmd = ' -1 ' + manual_decompression(" ".join(r1), zip_extension)
    r2_cmd = ' -2 ' + manual_decompression(" ".join(r2), zip_extension)
    read_cmd = " ".join([r1_cmd,r2_cmd])
if r:
    assert r1 is None and r2 is None, "Salmon cannot quantify mixed paired/unpaired input files. Please input either r1,r2 (paired) or r (unpaired)"
    r = [snakemake.input.r] if isinstance(snakemake.input.r, str) else snakemake.input.r
    read_cmd = ' -r ' + manual_decompression(" ".join(r), zip_extension)

outdir = path.dirname(snakemake.output.get('quant'))

shell("salmon quant -i {snakemake.input.index} "
      " -l {libtype} {read_cmd} -o {outdir} "
      " -p {snakemake.threads} {extra} {log} ")
