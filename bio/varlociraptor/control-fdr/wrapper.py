import subprocess as sp

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

sp.run(
    "varlociraptor filter-calls control-fdr "
    f"{snakemake.input[0]} "
    f"--mode {snakemake.params.mode} "
    f"--fdr {snakemake.params.fdr} "
    f"--events {' '.join(snakemake.params.events)} "
    f"> {snakemake.output[0]} {log}",
    check=True,
    shell=True,
)
