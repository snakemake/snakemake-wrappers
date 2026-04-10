__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2026, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Parse output files
output = list()
for key, value in snakemake.output.items():
    if key in ["structure"]:
        output.append(f"--internal-{key} {value}")
    elif key in ["network", "output", "statistics", "uclust"]:
        output.append(f"--{key}-file {value}")
    elif key in ["seeds", "log"]:
        output.append(f"--{key} {value}")
    else:
        raise ValueError(f"Unknown named output '{key}' with file name '{value}'.")

shell("swarm --threads {snakemake.threads} {extra} {output} {snakemake.input[0]} {log}")
