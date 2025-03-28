"""Snakemake wrapper for Bismark indexes preparing using bismark_genome_preparation."""

# https://github.com/FelixKrueger/Bismark/blob/master/bismark_genome_preparation

__author__ = "Roman Chernyatchik, David Lähnemann"
__copyright__ = "Copyright (c) 2019 JetBrains, 2025 DKTK Essen-Düsseldorf"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


from os import path
from math import floor
from warnings import warn
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

output_dir = snakemake.output["bismark_genome_dir"]
fasta_dir = path.dirname(output_dir)

threads = snakemake.threads

if threads < 2:
    raise ValueError(
        "Please provide at least threads: 2 for bismark_genome_preparation, as\n"
        "it will always run the two conversion types in parallel. See\n"
        "`bismark_genome_preparation --help` on the `--parallel` argument for\n"
        "more details. As snakemake's --cores argument will limit your job's\n"
        "threads, your workflow will need to run with at least --cores 2.\n"
        "Otherwise, this rule will always fail with this error.\n"
    )

threads = max(floor(threads/2), 1)
parallel = ""
if threads > 1:
    parallel = f"--parallel {threads}"

# we also want to allow using the standard bismark folder name with
# no mv required

rename_output_dir = f"mv {fasta_dir}/Bisulfite_Genome {output_dir}"
if f"{fasta_dir}/Bisulfite_Genome" == output_dir:
    rename_output_dir = ""

params_extra = snakemake.params.get("extra", "")

shell(
    f'( if [ ! -f {snakemake.input["genome"]} ]; then ln -s {snakemake.input["genome"]} {{fasta_dir}}/; fi;'
    "  bismark_genome_preparation --verbose --bowtie2 {parallel} {params_extra} {fasta_dir};"
    f"  {rename_output_dir} "
    ") {log}"
)
