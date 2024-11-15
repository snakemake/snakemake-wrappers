import subprocess as sp

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

obs = " ".join(f"{sample}={path}" for sample, path in zip(snakemake.params.samples, snakemake.input.observations))

sp.run(
    "varlociraptor call variants "
    f"{snakemake.params.get('extra', '')} "
    f"generic --obs {obs} "
    f"--scenario {snakemake.input.scenario} "
    f"> {output[0]} {log}",
    check=True,
    shell=True,
)