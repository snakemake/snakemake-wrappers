"""Snakemake wrapper for NanoSim."""

__author__ = "David Lähnemann"
__copyright__ = "Copyright 2024, David Lähnemann"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"

import tempfile
from os import path

from snakemake.shell import shell
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

def message_input_missing_for_subcommand(input_provided, subcommand, input_required):
    return (
        f"Providing 'input: {input_provided}' implies subcommand "
        f"'{subcommand}', but you did not provide the necessary "
        f"'input: {input_required}' that this subcommand requires."
    )

sample_infix=""

if "reference_genomes" in snakemake.input.keys():
    subcommand = "metagenome"
    # nanosim names samples `sample0`, `sample1`, ... and this wrapper forces
    # it to output only one single sample, to sanely handle output
    sample_infix = "sample0_"

    with open(snakemake.output.abundance_list_tsv, "w") as abun_out, open(snakemake.input.sample_abundances, "r") as abun_in:
        abundances_dict = dict()
        for line in abun_in:
            (k, v) = line.rstrip().split("\t")
            abundances_dict[k] = v
        total_abundance = 0.0
        for key in abundances_dict:
            total_abundance += float(abundances_dict[key])
        abun_out.write(f"Size\t{int(total_abundance)}\n")
        for key in abundances_dict:
            abun_out.write(f"{key}\t{abundances_dict[key]}\n")

    with open(snakemake.output.dna_type_list_tsv, "w") as dna_type:
        for spec in snakemake.params.species:
            dna_type.write(
                f"{spec}\t"
                f"{snakemake.params.species[spec]['chromosome']}\t"
                f"{snakemake.params.species[spec]['dna_type']}\n"
            )

    with open(snakemake.output.reference_genomes_list_tsv, "w") as genomes_list:
        for spec in snakemake.params.species:
            filename = [
                f for f in snakemake.input.reference_genomes
                if f.endswith(snakemake.params.species[spec]['ref_suffix'])
            ]
            if len(filename) == 1:
                genomes_list.write(
                    f"{spec}\t"
                    f"{filename[0]}\n"
                )
            elif len(filename) == 0:
                ValueError(
                    f"The params: species='{spec}' 'ref_suffix' you specified is: {snakemake.params.species[spec]['ref_suffix']}\n"
                    "This suffix does not match any of the specified 'input: reference_genomes=':\n"
                    f"{snakemake.input.reference_genomes}\n"
                )
            else:
                ValueError(
                    f"The params: species='{spec}' 'ref_suffix' you specified is: {snakemake.params.species[spec]['ref_suffix']}\n"
                    "This suffix is ambiguous with regard to the specified 'input: reference_genomes=':\n"
                    f"{snakemake.input.reference_genomes}\n"
                    "It matches all of these filename:\n"
                    f"{filename}\n"
                )

    input = (
        f"--genome_list {snakemake.output.reference_genomes_list_tsv} "
        f"--abun {snakemake.output.abundance_list_tsv} "
        f"--dna_type_list {snakemake.output.dna_type_list_tsv} "
    )
elif "reference_transcriptome" in snakemake.input.keys():
    subcommand = "transcriptome"
    if "expression_profile" not in snakemake.input.keys():
        raise KeyError(
            message_input_missing_for_subcommand("reference_transcriptome", subcommand, "expression_profile")
        )
    if "reference_genome" in snakemake.input.keys():
        genome = f"--ref_g {snakemake.input.reference_genome}"
    else:
        genome = "--no_model_ir"
    input = f"--ref_t {snakemake.input.reference_transcriptome} --exp {snakemake.input.expression_profile} {genome}"
elif "reference_genome" in snakemake.input.keys():
    subcommand = "genome"
    input = f"--ref_g {snakemake.input.reference_genome}"
else:
    raise KeyError(
        print(
            "None of the provided inputs clearly signify which subcommand should "
            "be used. Specify at least one of the following three:\n"
            "* reference_genome\n"
            "* reference_genomes\n"
            "* reference_transcriptome\n"
            "You provided:\n"
            f"{snakemake.input.keys()}"
        )
    )

if "model" not in snakemake.input.keys():
    raise KeyError(
        "NanoSim requires a model as input, please provide it via the named"
        "'input: model='."
    )
else:
    model_prefix=path.commonprefix(snakemake.input.model).rstrip("_")
    model=f"--model_prefix {model_prefix}"

if "--perfect" in snakemake.params.extra:
    raise ValueError(
        "The command line flag --perfect is set implicitly by the wrapper, if\n"
        "you do not specify an output file for 'output: unaligned_reads='.\n"
        "Please do not specify it under 'params: extra'."
    )

if path.splitext(snakemake.output.reads)[1] in [".fastq", ".fq"]:
    fq="--fastq"
    extension=".fastq"
else:
    fq=""
    extension=".fasta"

with tempfile.TemporaryDirectory() as tempdir:
    prefix = f"{tempdir}/simulated"

    if "unaligned_reads" in snakemake.output.keys():
        perfect=""
        mv_unaligned_reads=f" mv {prefix}_{sample_infix}unaligned_reads{extension} {snakemake.output.unaligned_reads}; "
    else:
        perfect="--perfect"
        mv_unaligned_reads=""
    
    # Executed shell command
    shell(
        "(simulator.py {subcommand} "
        " {input} "
        " {model} "
        " {extra} "
        " {fq} "
        " {perfect} "
        " --num_threads {snakemake.threads} "
        " --output {prefix}; "
        " mv {prefix}_{sample_infix}aligned_reads{extension} {snakemake.output.reads}; "
        " mv {prefix}_{sample_infix}aligned_error_profile {snakemake.output.errors}; "
        " {mv_unaligned_reads}"
        ") {log}; "
    )
