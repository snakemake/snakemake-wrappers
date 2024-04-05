__author__ = "Maarten van der Sande"
__copyright__ = "Copyright 2020, Maarten van der Sande"
__email__ = "M.vanderSande@science.ru.nl"
__license__ = "MIT"


from snakemake.shell import shell

# Optional parameters
provider = snakemake.params.get("provider", "ucsc").lower()

# set options for plugins
all_plugins = "blacklist,bowtie2,bwa,gmap,hisat2,minimap2,star"
req_plugins = ","
if any(["blacklist" in out for out in snakemake.output]):
    req_plugins = "blacklist,"

annotation = ""
if any(["annotation" in out for out in snakemake.output]):
    annotation = "--annotation"

# parse the genome dir
genome_dir = "./"
if snakemake.output[0].count("/") > 1:
    genome_dir = "/".join(snakemake.output[0].split("/")[:-1])

log = snakemake.log

# Finally execute genomepy
shell(
    """
    # set a trap so we can reset to original user's settings
    active_plugins=$(genomepy config show | grep -Po '(?<=- ).*' | paste -s -d, -) || echo ""
    trap "genomepy plugin disable {{{all_plugins}}} >> {log} 2>&1;\
          genomepy plugin enable {{$active_plugins,}} >> {log} 2>&1" EXIT

    # disable all, then enable the ones we need
    genomepy plugin disable {{{all_plugins}}} >  {log} 2>&1
    genomepy plugin enable  {{{req_plugins}}} >> {log} 2>&1

    # install the genome
    genomepy install {snakemake.wildcards.assembly} \
    --provider {provider} {annotation} -g {genome_dir} >> {log} 2>&1
    """
)
