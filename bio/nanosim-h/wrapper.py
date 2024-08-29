"""Snakemake wrapper for NanoSim-H."""

__author__ = "Michael Hall"
__copyright__ = "Copyright 2019, Michael Hall"
__email__ = "mbhall88@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


def is_header(query):
    return query.startswith(">")


def get_length_of_longest_sequence(fh):
    current_length = 0
    all_lengths = []
    for line in fh:
        if not is_header(line):
            current_length += len(line.rstrip())
        else:
            all_lengths.append(current_length)
            current_length = 0
    all_lengths.append(current_length)

    return max(all_lengths)


# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
prefix = snakemake.params.get("prefix", snakemake.output.reads.rpartition(".")[0])
num_reads = snakemake.params.get("num_reads", 10000)
profile = snakemake.params.get("profile", "ecoli_R9_2D")
perfect_reads = snakemake.params.get("perfect_reads", False)
min_read_len = snakemake.params.get("min_read_len", 50)
max_read_len = snakemake.params.get("max_read_len", 0)
input_fasta = snakemake.input.get("fasta", "")
input_profile_dir = snakemake.input.get("profile_dir", "")

# need to do this as the default read length of infinity can cause nanosim-h to
# hang if the reference is short
if max_read_len == 0:
    with open(snakemake.input[0]) as fh:
        max_read_len = get_length_of_longest_sequence(fh)

perfect_reads_flag = "--perfect " if perfect_reads else ""
# Formats the log redrection string
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Executed shell command
shell(
    "nanosim-h {extra} "
    "{perfect_reads_flag} "
    "--max-len {max_read_len} "
    "--min-len {min_read_len} "
    "--profile {profile} "
    "--number {num_reads} "
    "--out-pref {prefix} "
    "{input_fasta} {input_profile_dir} {log}"
)
