import subprocess as sp

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

sp.run(
    "varlociraptor preprocess variants "
    f"{snakemake.params.get('extra', '')} {snakemake.input.ref} "
    f"--alignment-properties {snakemake.input.alignment_properties} "
    f"--candidates {snakemake.input.candidate_vars} "
    f"--bam {snakemake.input.alignments} "
    f"--output {snakemake.output[0]} {log}",
    check=True,
    shell=True,
)