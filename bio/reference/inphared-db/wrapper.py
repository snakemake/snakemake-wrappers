__author__ = "Noriko A. Cassman"
__copyright__ = "Copyright 2023, Noriko A. Cassman"
__email__ = "noriko.cassman@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

    shell:
        "curl {params.prefix}{params.date}{params.suffix} -o {params.date}{params.suffix}"
