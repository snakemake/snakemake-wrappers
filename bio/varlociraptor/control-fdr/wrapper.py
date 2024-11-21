import subprocess as sp

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Validate inputs
samples = snakemake.params.samples
observations = snakemake.input.observations
if len(samples) != len(observations):
    raise ValueError("Number of samples must match number of observations")
if not samples:
    raise ValueError("At least one sample is required")
# Quote paths to handle spaces
obs = " ".join(f"{sample}='{path}'" for sample, path in zip(samples, observations))

sp.run(
    "varlociraptor call variants "
    f"{snakemake.params.get('extra', '')} "
    f"generic --obs {obs} "
    f"--scenario {snakemake.input.scenario} "
    f"> {snakemake.output[0]} {log}",
    check=True,
    shell=True,
)
