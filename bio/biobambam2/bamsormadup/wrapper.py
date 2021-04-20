__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import os
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
extra = snakemake.params.get("extra", "")


# File formats
in_name, in_format = os.path.splitext(snakemake.input[0])
out_name, out_format = os.path.splitext(snakemake.output[0])


index = snakemake.output.get("index", "")
if index:
    index = f"indexfilename={index}"


metrics = snakemake.output.get("metrics", "")
if metrics:
    metrics = f"M={metrics}"


shell(
    "bamsormadup threads={snakemake.threads} inputformat={in_format[1:]} outputformat={out_format[1:]} {index} {metrics} {extra} < {snakemake.input[0]} > {snakemake.output[0]} {log}"
)
