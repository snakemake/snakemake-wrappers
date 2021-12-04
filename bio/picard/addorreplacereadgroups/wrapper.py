__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params
java_opts = get_java_opts(snakemake)

shell(
    "picard AddOrReplaceReadGroups {java_opts} {extra} "
    "I={snakemake.input} O={snakemake.output} &> {snakemake.log}"
)
