__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
java_options = snakemake.params.get("java_options", "")

shell("picard {java_options} AddOrReplaceReadGroups {extra} I={snakemake.input} "
      "O={snakemake.output} &> {snakemake.log}")
