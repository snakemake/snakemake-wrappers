__author__ = "Roman Valls Guimera"
__copyright__ = "Copyright 2018, Roman Valls Guimera"
__email__ = "brainstorm@nopcode.org"
__license__ = "MIT"


import os
from snakemake.shell import shell

shell(
    "sambamba slice {snakemake.params} -t {snakemake.threads} "
    "-o {snakemake.output[0]} {snakemake.input[0]}")
