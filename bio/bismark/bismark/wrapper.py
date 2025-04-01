"""Snakemake wrapper for aligning methylation BS-Seq data using Bismark."""

# https://github.com/FelixKrueger/Bismark/blob/master/bismark

__author__ = "Roman Chernyatchik, David Lähnemann"
__copyright__ = "Copyright (c) 2019 JetBrains, DKTK Essen Düsseldorf"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# double-check params: extra= against auto-options
extra = snakemake.params.get("extra", "")
automatic_command_line_args = [
    "-1",
    "-2",
    "--se",
    "--single_end",
    "--parallel",
    "--multicore",
    "-un",
    "--unmapped",
    "--ambiguous",
    "--sam",
    "--bam",
    "--cram",
    "--samtools_path",
    "--prefix",
    "-B",
    "--basename",
    "--ambig_bam",
    "--nucleotide_coverage",
    "--bowtie2",
    "--hisat2",
    "--mm2",
    "--minimap2",
]

if any(s in extra for s in automatic_command_line_args):
    raise ValueError(
        "Please do not use any of the following command-line arguments under "
        "`params: extra=''`, as setting them is either determined automatically "
        "or is not possible with this wrapper:\n"
        f"{automatic_command_line_args}"
    )

# this dict will be used for moving named outputs from the temporary directory
# to the location requested under output
move_dict = dict()

args = []


def handle_optional_output(
    output_name, flag, file_suffix, extra_implicit_args=args, mv_dict=move_dict
):
    output = snakemake.output.get(output_name)
    if output:
        if flag not in extra_implicit_args:
            extra_implicit_args.append(flag)
        mv_dict[file_suffix] = output


# check whether report is specified
report = snakemake.output.get("report", None)
if not report:
    raise ValueError("The named output `report=` has to be specified.")

# determine the output format by checking named outputs
sam = snakemake.output.get("sam", None)
bam = snakemake.output.get("bam", None)
cram = snakemake.output.get("cram", None)

n_out = sum(o is not None for o in [sam, bam, cram])

if n_out == 0:
    raise ValueError(
        "Exactly one of the named outputs `sam=`, `bam=` or `cram=` must be specified.\n"
        "You specified none."
    )
elif n_out > 1:
    raise ValueError(
        "Exactly one of the named outputs `sam=`, `bam=` or `cram=` must be specified.\n"
        f"You specified more than one, namely: {[sam, bam, cram]}"
    )

nt_stats = snakemake.output.get("nucleotide_stats")

if sam and nt_stats:
    raise ValueError(
        "Named output `nucleotide_stats=` and the respective command line argument\n"
        "`--nucleotide_coverage` are not compatible with output type `sam=`.\n"
    )

genome_stats = snakemake.input.get("genomic_freq")

if nt_stats and not genome_stats:
    raise ValueError(
        "Named output `nucleotide_stats=` requires named input `genomic_freq=` as\n"
        "produced by `bam2nuc`, because it would otherwise implicitly attempt to\n"
        "write this file, risking race conditions. Please separately run `bam2nuc` with\n"
        "`--genomic_composition_only` and provide as input via `genomic_freq=`.\n"
    )

# determine input fastq file(s)
single_end_fq = snakemake.input.get("fq", None)
fq_1 = snakemake.input.get("fq_1", None)
fq_2 = snakemake.input.get("fq_2", None)

threads = snakemake.threads


def get_auto_prefix(file_path):
    (pref, ext) = path.splitext(path.basename(file_path))
    if ext == ".gz":
        (pref, _) = path.splitext(pref)
    return pref


if single_end_fq and not (fq_1 or fq_2):
    input_files = f"--se {single_end_fq}"
    auto_prefix = get_auto_prefix(single_end_fq)
    se_basename = path.basename(single_end_fq)

    move_dict[f".{auto_prefix}_bismark_bt2_SE_report.txt"] = report

    threads = max((threads - 1) // 2, 1)

    # main output
    handle_optional_output(
        output_name="sam",
        flag="--sam",
        file_suffix=f".{auto_prefix}_bismark_bt2.sam",
    )
    handle_optional_output(
        output_name="cram",
        flag="--cram",
        file_suffix=f".{auto_prefix}_bismark_bt2.cram",
    )
    handle_optional_output(
        output_name="bam",
        flag="",
        file_suffix=f".{auto_prefix}_bismark_bt2.bam",
    )

    # optional outputs that set command line arguments
    handle_optional_output(
        output_name="fq_unmapped",
        flag="--unmapped",
        file_suffix=f".{se_basename}_unmapped_reads.fq.gz",
    )
    handle_optional_output(
        output_name="fq_ambiguous",
        flag="--ambiguous",
        file_suffix=f".{se_basename}_ambiguous_reads.fq.gz",
    )

    ambig_suffix = f".{se_basename}_bismark_bt2.ambig.bam"
    if threads == 1:
        ambig_suffix = f".{auto_prefix}_bismark_bt2.ambig.bam"
    handle_optional_output(
        output_name="bam_ambiguous",
        flag="--ambig_bam",
        file_suffix=ambig_suffix,
    )
    handle_optional_output(
        output_name="nucleotide_stats",
        flag="--nucleotide_coverage",
        file_suffix=f".{auto_prefix}_bismark_bt2.nucleotide_stats.txt",
    )
elif fq_1 and fq_2:
    input_files = f"-1 {fq_1} -2 {fq_2}"

    auto_prefix_1 = get_auto_prefix(fq_1)
    fq_1_basename = path.basename(fq_1)
    fq_2_basename = path.basename(fq_2)

    move_dict[f".{auto_prefix_1}_bismark_bt2_PE_report.txt"] = report

    threads = max((threads - 1) // 4, 1)

    # main output
    handle_optional_output(
        output_name="sam",
        flag="--sam",
        file_suffix=f".{auto_prefix_1}_bismark_bt2_pe.sam",
    )
    handle_optional_output(
        output_name="cram",
        flag="--cram",
        file_suffix=f".{auto_prefix_1}_bismark_bt2_pe.cram",
    )
    handle_optional_output(
        output_name="bam",
        flag="",
        file_suffix=f".{auto_prefix_1}_bismark_bt2_pe.bam",
    )

    # optional outputs that set command line arguments
    handle_optional_output(
        output_name="fq_unmapped_1",
        flag="--unmapped",
        file_suffix=f".{fq_1_basename}_unmapped_reads_1.fq.gz",
    )
    handle_optional_output(
        output_name="fq_unmapped_2",
        flag="--unmapped",
        file_suffix=f".{fq_2_basename}_unmapped_reads_2.fq.gz",
    )
    handle_optional_output(
        output_name="fq_ambiguous_1",
        flag="--ambiguous",
        file_suffix=f".{fq_1_basename}_ambiguous_reads_1.fq.gz",
    )
    handle_optional_output(
        output_name="fq_ambiguous_2",
        flag="--ambiguous",
        file_suffix=f".{fq_2_basename}_ambiguous_reads_2.fq.gz",
    )

    ambig_suffix_1 = f".{fq_1_basename}_bismark_bt2_pe.ambig.bam"
    if threads == 1:
        ambig_suffix_1 = f".{auto_prefix_1}_bismark_bt2_pe.ambig.bam"
    handle_optional_output(
        output_name="bam_ambiguous",
        flag="--ambig_bam",
        file_suffix=ambig_suffix_1,
    )
    handle_optional_output(
        output_name="nucleotide_stats",
        flag="--nucleotide_coverage",
        file_suffix=f".{auto_prefix_1}_bismark_bt2_pe.nucleotide_stats.txt",
    )
else:
    raise ValueError(
        "As named fastq input files, please specify either of these two options:\n"
        "1. Only the named input `fq=` for single end read data.\n"
        "2. Both the named inputs `fq_1=` and `fq_2` for paired end read data.\n"
    )

args.append(f"--parallel {threads}")

if genome_stats:
    stats_file_fixed_location = (
        f"{snakemake.input['bismark_indexes_dir']}/genomic_nucleotide_frequencies.txt"
    )
    shell(
        f"if [ ! -f {stats_file_fixed_location} ]; "
        f"then ln -sr {genome_stats} {stats_file_fixed_location}; "
        "fi; "
    )

with TemporaryDirectory() as temp_dir:
    bismark_command = (
        f"bismark {extra} --bowtie2 "
        f' {" ".join(args)} '
        f'--genome_folder {snakemake.input["bismark_indexes_dir"]} '
        f"--output_dir {temp_dir} "
        f"--prefix temp_file "
        f" {input_files} "
    )
    move_commands = "; ".join(
        f"mv {temp_dir}/temp_file{suffix} {output_name}"
        for suffix, output_name in move_dict.items()
    )
    shell(
        # run bismark
        f"( {bismark_command}; "
        # move files into wanted paths and file names
        f"  {move_commands}; "
        # capture everything in the logs
        f") {log}"
    )
