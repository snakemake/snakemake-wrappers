__author__ = "Roman Valls Guimera"
__copyright__ = "Copyright 2018, Roman Valls Guimera"
__email__ = "brainstorm+snakemake@nopcode.org"
__license__ = "MIT"


from snakemake.shell import shell

shell("sambamba slice -o {snakemake.output[0]} {snakemake.input[0]} {snakemake.params}")
