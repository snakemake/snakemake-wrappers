""" Snakemake wrapper for lastal """

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2010, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

cutoff = snakemake.params.get("evalue_threshold", 0.000001)

#-Q: input format: 0=fasta or fastq-ignore, 1=fastq-sanger, 2=fastq-solexa,
#                  3=fastq-illumina, 4=prb, 5=PSSM (fasta)

#input_format = snakemake.params.get("input-format", "")
#if not input_format:
#    if "fq" in input_data or "fastq" in input_data:
#        input_format = 3 # guess illumina? or fastq-ignore? (0)
#    elif "fa" in input_data or "fasta" in input_data:
#        input_format = 0
#    else:
#        assert (input_format is not None), "Please specify 'input_format' param (0=fasta or fastq-ignore, 1=fastq-sanger, 2=fastq-solexa, 3=fastq-illumina, 4=prb, 5=PSSM (fasta)"


# set output file formats
maf_out = snakemake.output.get("maf", "")
tab_out = snakemake.output.get("tab", "")
btab_out= snakemake.output.get("blast-tab", "")
btabplus_out = snakemake.output.get("blast-tab-plus", "")
outfiles = [maf_out, tab_out, btab_out, btabplus_out]
#TAB, MAF, BlastTab, BlastTab+ (default=MAF)
assert list(map(bool, outfiles)).count(True) == 1, "please specify ONE output file using one of: 'maf', 'tab', 'blasttab', or 'blasttabplus' keywords in the output field)"

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


lastdb_name = str(snakemake.input["lastdb"]).rsplit('.', 1)[0]

#lastal [options] lastdb-name fasta-sequence-file(s)
shell("lastal -D {cutoff} -P {snakemake.threads} {extra} {lastdb_name} {snakemake.input.data} > {outF} {log}")
