__author__ = "Maarten van der Sande"
__copyright__ = "Copyright 2020, Maarten van der Sande"
__email__ = "M.vanderSande@science.ru.nl"
__license__ = "MIT"


import re

from snakemake.shell import shell

# Optional parameters
provider = snakemake.params.get("provider", "UCSC")

# set options for plugins
all_plugins = "blacklist,bowtie2,bwa,gmap,hisat2,minimap2,star"
req_plugins = ","
if any(["blacklist" in out for out in snakemake.output]):
    req_plugins = "blacklist"

annotation = ""
if any(["annotation" in out for out in snakemake.output]):
    annotation = "--annotation"

# Run log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Finally execute genomepy
shell(
    """
    # set a trap so we can reset to original user's settings
    active_plugins=$(genomepy config show | grep -Po '(?<=- ).*' | paste -s -d, -) || echo ""
    trap "genomepy plugin disable {{{all_plugins}}};\
          genomepy plugin enable {{$active_plugins,}}" EXIT

    # disable all, then enable the ones we need
    genomepy plugin disable {{{all_plugins}}}
    genomepy plugin enable  {{{req_plugins}}}

    # install the genome
    genomepy install {snakemake.wildcards.assembly} \
    {provider} {annotation} -g ./
    """
)
