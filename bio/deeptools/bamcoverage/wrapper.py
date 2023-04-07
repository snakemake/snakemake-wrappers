__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# See: https://deeptools.readthedocs.io/en/latest/content/feature/effectiveGenomeSize.html
default_effective_genome_size = {
    "GRCz10": {
        "50": 1195445591,
        "75": 1251132686,
        "100": 1280189044,
        "150": 1312207169,
        "200": 1321355241,
    },
    "WBcel235": {
        "50": 95159452,
        "75": 96945445,
        "100": 98259998,
        "150": 98721253,
        "200": 98672758,
    },
    "dm3": {
        "50": 130428560,
        "75": 135004462,
        "100": 139647232,
        "150": 144307808,
        "200": 148524010,
    },
    "dm6": {
        "50": 125464728,
        "75": 127324632,
        "100": 129789873,
        "150": 129941135,
        "200": 132509163,
    },
    "GRCh37": {
        "50": 2685511504,
        "75": 2736124973,
        "100": 2776919808,
        "150": 2827437033,
        "200": 2855464000,
    },
    "GRCh38": {
        "50": 2701495761,
        "75": 2747877777,
        "100": 2805636331,
        "150": 2862010578,
        "200": 2887553303,
    },
    "GRCm37": {
        "50": 2304947926,
        "75": 2404646224,
        "100": 2462481010,
        "150": 2489384235,
        "200": 2513019276,
    },
    "GRCm38": {
        "50": 2308125349,
        "75": 2407883318,
        "100": 2467481108,
        "150": 2494787188,
        "200": 2520869189,
    },
}

effective_genome_size = snakemake.params.get("effective_genome_size")
if not effective_genome_size:
    genome = snakemake.params.get("genome")
    read_length = snakemake.params.get("read_length")
    if genome and read_length:
        effective_genome_size = "--effectiveGenomeSize "
        effective_genome_size += default_effective_genome_size[genome][str(read_length)]
else:
    effective_genome_size = "--effectiveGenomeSize " + str(effective_genome_size)


output_format = ""
bigwig_format = ["bw", "bigwig"]
bedgraph_format = ["bg", "bedgraph"]
output_ext = str(snakemake.output[0]).split(".")[-1].lower()
if output_ext in bigwig_format:
    output_format = "bigwig"
elif output_ext in bedgraph_format:
    output_format = "bedgraph"
else:
    raise ValueError("Output file should be either a bigwig or a bedgraph file")


blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = "--blackListFileName " + blacklist

shell(
    "bamCoverage "
    "{blacklist} {extra} "
    "--numberOfProcessors {snakemake.threads} "
    "{effective_genome_size} "
    "--bam {snakemake.input.bam} "
    "--outFileName {snakemake.output} "
    "--outFileFormat {output_format} "
    "{log} "
)
