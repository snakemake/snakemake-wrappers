from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
subcommand = snakemake.params.subcommand

output = snakemake.output[0]
genome = snakemake.input.genome  # shared input
extra = snakemake.params.get("extra", "")

if subcommand == "hla":
    alleles = snakemake.input.alleles
    xml = snakemake.input.xml

    shell(
        "orthanq candidates hla "
        "--alleles {alleles} "
        "--genome {genome} "
        "--xml {xml} "
        "{extra} "
        "--output {output} "
        "{log}"
    )

elif subcommand == "virus":
    lineages = snakemake.input.lineages

    shell(
        "orthanq candidates virus "
        "--genome {genome} "
        "--lineages {lineages} "
        "--output {output} "
        "{log}"
    )

else:
    raise ValueError(f"Unsupported subcommand: {subcommand}")
