__author__ = "Endre Bakken Stovner"
__copyright__ = "Copyright 2017, Endre Bakken Stovner"
__email__ = "endrebak85@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
threads = snakemake.threads or 1

treatment = snakemake.input.get("treatment")
background = snakemake.input.get("background")

# Executed shell command
enriched_regions = snakemake.output.get("enriched_regions")

bed = snakemake.output.get("bed")
matrix = snakemake.output.get("matrix")

if len(snakemake.log) > 0:
    log = snakemake.log[0]

genome = snakemake.params.get("genome")

cmd = "epic -cpu {threads} -t {treatment} -c {background} -o {enriched_regions} -gn {genome}"

if bed:
    cmd += " -b {bed}"
if matrix:
    cmd += " -sm {matrix}"
if log:
    cmd += " -l {log}"

cmd += " {extra}"

shell(cmd)
