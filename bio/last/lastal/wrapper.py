""" Snakemake wrapper for lastal """

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# http://last.cbrc.jp/doc/last-evalues.html
d_len = float(snakemake.params.get("D_length", 1000000))  # last default

# set output file formats
maf_out = snakemake.output.get("maf", "")
tab_out = snakemake.output.get("tab", "")
btab_out = snakemake.output.get("blasttab", "")
btabplus_out = snakemake.output.get("blasttabplus", "")
outfiles = [maf_out, tab_out, btab_out, btabplus_out]
# TAB, MAF, BlastTab, BlastTab+ (default=MAF)
assert (
    list(map(bool, outfiles)).count(True) == 1
), "please specify ONE output file using one of: 'maf', 'tab', 'blasttab', or 'blasttabplus' keywords in the output field)"

out_cmd = ""

if maf_out:
    out_cmd = "-f {}".format("MAF")
    outF = maf_out
elif tab_out:
    out_cmd = "-f {}".format("TAB")
    outF = tab_out
if btab_out:
    out_cmd = "-f {}".format("BlastTab")
    outF = btab_out
if btabplus_out:
    out_cmd = "-f {}".format("BlastTab+")
    outF = btabplus_out

frameshift_cost = snakemake.params.get("frameshift_cost", "")
if frameshift_cost:
    f_cmd = f"-F {frameshift_cost}"


lastdb_name = str(snakemake.input["lastdb"]).rsplit(".", 1)[0]

shell(
    "lastal -D {d_len} -P {snakemake.threads} {extra} {lastdb_name} {snakemake.input.data} > {outF} {log}"
)
