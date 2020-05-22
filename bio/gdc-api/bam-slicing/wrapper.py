__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
import os.path as path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

uuid = snakemake.params.get("uuid", "")
if uuid == "":
    raise ValueError("You need to provide a GDC UUID via the 'uuid' in 'params'.")

token = snakemake.params.get("gdc_token", "")
if token == "":
    raise ValueError(
        "You need to provide a GDC data access token via the 'token' in 'params'."
    )

slices = snakemake.params.get("slices", "")
if slices == "":
    raise ValueError(
        "You need to provide 'region=chr1:1000-2000' or 'gencode=BRCA2' slice(s)  via the 'slices' in 'params'."
    )

extra = snakemake.params.get("extra", "")

shell(
    "curl --silent"
    " --header 'X-Auth-Token: {token}'"
    " 'https://api.gdc.cancer.gov/slicing/view/{uuid}?{slices}'"
    " {extra}"
    " --output {snakemake.output.bam} {log}"
)

if path.getsize(snakemake.output.bam) < 100000:
    with open(snakemake.output.bam) as f:
        if "error" in f.read():
            shell("cat {snakemake.output.bam} {log}")
            raise RuntimeError(
                "Your GDC API request returned an error, check your log file for the error message."
            )
