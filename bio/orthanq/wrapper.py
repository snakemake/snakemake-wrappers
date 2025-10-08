__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2025, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Required parameters
command = snakemake.params.command  # candidates, preprocess, call
subcommand = snakemake.params.subcommand  # hla, virus

# Shared inputs and params
genome = snakemake.input.get("genome", "")
extra = snakemake.params.get("extra", "")

cmd = f"orthanq {command} {subcommand}"

# Determine output depending on command/subcommand
if command == "candidates" and subcommand == "hla":
    output = snakemake.output.candidates_dir
else:
    output = snakemake.output[0]

if command == "candidates":
    if subcommand == "hla":
        alleles = snakemake.input.alleles
        xml = snakemake.input.xml
        cmd += f" --alleles {alleles} --genome {genome} --xml {xml} {extra}"
    elif subcommand == "virus":
        lineages = snakemake.input.lineages
        cmd += f" --genome {genome} --lineages {lineages}"
    else:
        raise ValueError(f"Unsupported subcommand for 'candidates': {subcommand}")

# === Preprocess ===
elif command == "preprocess":
    reads = snakemake.input.reads
    haplotype_variants = snakemake.input.haplotype_variants
    cmd += (
        f" --genome {genome} --haplotype-variants {haplotype_variants} --reads {reads}"
    )

    if subcommand == "hla":
        vg_index = snakemake.input.vg_index
        cmd += f" --vg-index {vg_index}"
    elif subcommand == "virus":
        pass  # already complete
    else:
        raise ValueError(f"Unsupported subcommand for 'preprocess': {subcommand}")

# === Call ===
elif command == "call":
    # Require prior
    if not hasattr(snakemake.params, "prior"):
        raise ValueError("Missing required param: 'prior' is required for orthanq call")
    prior = snakemake.params.prior

    haplotype_calls = snakemake.input.haplotype_calls
    haplotype_variants = snakemake.input.haplotype_variants
    cmd += f" --haplotype-calls {haplotype_calls} --haplotype-variants {haplotype_variants} --prior {prior}"

    if subcommand == "hla":
        xml = snakemake.input.xml
        cmd += f" --xml {xml} {extra}"
    elif subcommand == "virus":
        pass  # already complete
    else:
        raise ValueError(f"Unsupported subcommand for 'call': {subcommand}")

else:
    raise ValueError(f"Unsupported command: {command}")

# Finalize with output and log
cmd += f" --output {output} {log}"

shell(cmd)

