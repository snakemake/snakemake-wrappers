__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import os
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
extra = snakemake.params.get("extra", "")


# File formats
in_name, in_format = os.path.splitext(snakemake.input[0])
in_format = in_format.lstrip(".")
out_name, out_format = os.path.splitext(snakemake.output[0])
out_format = out_format.lstrip(".")


index = snakemake.output.get("index", "")
if index:
    index = f"indexfilename={index}"


metrics = snakemake.output.get("metrics", "")
if metrics:
    metrics = f"M={metrics}"


shell(
    "bamsormadup threads={snakemake.threads} inputformat={in_format} outputformat={out_format} {index} {metrics} {extra} < {snakemake.input[0]} > {snakemake.output[0]} {log}"
)
