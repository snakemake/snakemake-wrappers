__author__ = "Maarten van der Sande"
__copyright__ = "Copyright 2019, Maarten van der Sande"
__email__ = "m.vandersande@science.ru.nl"
__license__ = "BSD"


from snakemake.shell import shell

# Optional parameters
provider = snakemake.params.get("provider", "NCBI")
plugins = snakemake.params.get("plugins", "")
if snakemake.params.get("annotation", False):
    annotation = "--annotation"
else:
    annotation = ""

# Run log
log = snakemake.log_fmt_shell()

# Finally execute genomepy
shell(
    # Disable all plugins and then enable the provided ones
    f"genomepy plugin disable blacklist bowtie2 bwa gmap hisat2 minimap2 sizes star {log}; "
    f"genomepy plugin enable {plugins} {log}; "
    # Install the genome
    f"genomepy install {snakemake.wildcards.assembly} {provider} --genome_dir {snakemake.output} {annotation} {log}"
)
