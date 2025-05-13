"""Snakemake wrapper for Bismark indexes preparing using bismark_genome_preparation."""

# https://github.com/FelixKrueger/Bismark/blob/master/bismark_genome_preparation

__author__ = "Roman Chernyatchik, David Lähnemann"
__copyright__ = "Copyright (c) 2019 JetBrains, 2025 DKTK Essen-Düsseldorf"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


from os import path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

output_dir = snakemake.output.bismark_genome_dir
fasta_out = f"{output_dir}/{path.basename(snakemake.input.genome)}"

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

threads = max(threads // 2, 1)
parallel = ""
if threads > 1:
    parallel = f"--parallel {threads}"

params_extra = snakemake.params.get("extra", "")

shell(
    f"( mkdir -p {output_dir}/Bisulfite_Genome; "
    f"  if [ ! -f {fasta_out} ]; then ln -sr {snakemake.input.genome} {fasta_out}; fi; "
    f"  bismark_genome_preparation --verbose --bowtie2 {parallel} {params_extra} {output_dir};"
    ") {log}"
)
