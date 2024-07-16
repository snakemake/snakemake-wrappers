__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# See: https://deeptools.readthedocs.io/en/latest/content/feature/effectiveGenomeSize.html
default_effective_genome_size = {
    "GRCh37": {
        "50": 2685511454,
        "75": 2736124898,
        "100": 2776919708,
        "150": 2827436883,
        "200": 2855463800,
        "250": 2855044784,
    },
    "GRCh38": {
        "50": 2701495711,
        "75": 2747877702,
        "100": 2805636231,
        "150": 2862010428,
        "200": 2887553103,
        "250": 2898802627,
    },
    "GRCm37": {
        "50": 2304947876,
        "75": 2404646149,
        "100": 2462480910,
        "150": 2489384085,
        "200": 2513019076,
        "250": 2528988583,
    },
    "GRCm38": {
        "50": 2308125299,
        "75": 2407883243,
        "100": 2467481008,
        "150": 2494787038,
        "200": 2520868989,
        "250": 2538590322,
    },
    "GRCz10": {
        "50": 1195445541,
        "75": 1251132611,
        "100": 1280188944,
        "150": 1312207019,
        "200": 1321355041,
        "250": 1339205109,
    },
    "GRCz11": {
        "50": 1197575653,
        "75": 1250812288,
        "100": 1280354977,
        "150": 1311832909,
        "200": 1322366338,
        "250": 1342093482,
    },
    "T2T/CHM13CAT_v2": {
        "50": 2725240337,
        "75": 2786136059,
        "100": 2814334875,
        "150": 2931551487,
        "200": 2936403235,
        "250": 2960856300,
    },
    "TAIR10": {
        "50": 114339094,
        "75": 115317469,
        "100": 118459858,
        "150": 118504138,
        "200": 117723393,
        "250": 119585546,
    },
    "WBcel235": {
        "50": 95159402,
        "75": 96945370,
        "100": 98259898,
        "150": 98721103,
        "200": 98672558,
        "250": 101271756,
    },
    "dm3": {
        "50": 130428510,
        "75": 135004387,
        "100": 139647132,
        "150": 144307658,
        "200": 148523810,
        "250": 151901455,
    },
    "dm6": {
        "50": 125464678,
        "75": 127324557,
        "100": 129789773,
        "150": 129940985,
        "200": 132508963,
        "250": 132900923,
    },
}

effective_genome_size = snakemake.params.get("effective_genome_size", "")
if not effective_genome_size:
    genome = snakemake.params.get("genome")
    read_length = snakemake.params.get("read_length")
    if genome and read_length:
        try:
            effective_genome_size = f"--effectiveGenomeSize {default_effective_genome_size[genome][str(read_length)]}"
        except KeyError:
            raise KeyError(
                (
                    "A valid genome and read_length need to be provided. See "
                    "https://deeptools.readthedocs.io/en/latest/content/feature/effectiveGenomeSize.html"
                )
            )
else:
    effective_genome_size = f"--effectiveGenomeSize {effective_genome_size}"


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
