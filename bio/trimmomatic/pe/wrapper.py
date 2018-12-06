"""
bio/trimmomatic/pe

Snakemake wrapper to trim reads with trimmomatic in PE mode with help of pigz.
pigz is the parallel implementation of gz. Trimmomatic spends most of the time
compressing and decompressing instead of trimming sequences. By using process
substitution (<(command), >(command)), we can accelerate trimmomatic a lot.
"""

__author__ = "Johannes Köster, Jorge Langa"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


def compose_input_gz(filename):
    if filename.endswith(".gz"):
        filename = "<(pigz --decompress --stdout {filename})".format(
            filename=filename
        )
    return filename


def compose_output_gz(filename, compression_level="-5"):
    if filename.endswith(".gz"):
        return ">(pigz {compression_level} > {filename})".format(
            compression_level=compression_level,
            filename=filename
        )
    return filename


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
compression_level = snakemake.params.get("compression_level", "-5")
trimmer = " ".join(snakemake.params.trimmer)


# Collect files
input_r1 = compose_input_gz(snakemake.input.r1)
input_r2 = compose_input_gz(snakemake.input.r2)

output_r1 = compose_output_gz(snakemake.output.r1, compression_level)
output_r1_unp = compose_output_gz(snakemake.output.r1_unpaired, compression_level)
output_r2 = compose_output_gz(snakemake.output.r2, compression_level)
output_r2_unp = compose_output_gz(snakemake.output.r2_unpaired, compression_level)

shell(
    "trimmomatic PE {extra} "
    "{input_r1} {input_r2} "
    "{output_r1} {output_r1_unp} "
    "{output_r2} {output_r2_unp} "
    "{trimmer} "
    "{log}"
)
