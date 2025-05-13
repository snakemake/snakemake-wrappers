import subprocess as sp
import sys

if snakemake.log:
    sys.stderr = open(snakemake.log[0], "w")

cmd = ["efetch"]


def add_param(param, required=False):
    if snakemake.params.get(param):
        cmd.extend(["-" + param, snakemake.params[param]])
    elif required:
        raise ValueError("Missing required parameter: " + param)
    else:
        return []


add_param("id", required=True)
for param in ["db", "format", "mode"]:
    add_param(param)

with open(snakemake.output[0], "w") as out:
    sp.run(cmd, stderr=sp.STDOUT, stdout=out, check=True)
