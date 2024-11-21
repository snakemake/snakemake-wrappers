import subprocess as sp

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

sp.run(
    "varlociraptor estimate alignment-properties "
    f"{snakemake.params.get('extra', '')} {snakemake.input.ref} "
    f"--bam {snakemake.input.alignments} "
    f"> {snakemake.output[0]} {log}",
    check=True,
    shell=True,
)
