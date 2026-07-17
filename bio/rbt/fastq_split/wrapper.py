# coding: utf-8

"""Snakemake wrapper for rbt fastq-split"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from os.path import splitext
from snakemake_wrapper_utils.snakemake import get_format
from snakemake.shell import shell

def get_compression_threads(available_threads, compression_jobs):
    q, r = divmod(available_threads, compression_jobs)
    return tuple(q + 1 if job < r else q for job in range(compression_jobs))

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append = True)
compression_extra = snakemake.params.get("compression_extra", "")

command_lines = []
rbt_output_paths = []
files_to_compress = {}
required_threads = 1

# rbt split-fastq does not read compressed fastq files
read_cmd = f"< {snakemake.input[0]}"
if str(snakemake.input[0]).endswith("gz"):
    read_cmd = f"< <(crabz --decompress {snakemake.input[0]})"
    required_threads += 1


for outfile in snakemake.output:
    if get_format(outfile) == "gzip":
        # If user requests a compressed gzip, then
        uncompressed_outfile = splitext(outfile)
        rbt_output_paths.append(uncompressed_outfile)
        files_to_compress[uncompressed_outfile] = outfile
    else:
        # No compression required
        rbt_output_paths.append(outfile)


if required_threads > snakemake.threads:
    raise ValueError(
        f"This wrapper required at least {required_threads + len(files_to_compress)} "
        f"threads. Got {snakemake.threads}."
    )

if len(files_to_compress) > 0:
    compression_threads = get_compression_threads(
        available_threads=snakemake.threads - required_threads,
        compression_jobs=len(files_to_compress),
    )
    command_lines.append(f"mkfifo {files_to_compress.keys()} ;")

    crabz_params = zip(files_to_compress.items(), compression_threads)
    for uncompressed_compressed, threads in crabz_params:
        # Using crabz to compress faster than gzip
        command_lines.append(
            f"crabz --output {uncompressed_compressed[1]} {compression_extra} "
            f"--compression-threads {threads} {uncompressed_compressed[0]} {log} &"
        )

    command_lines.append(f"rbt fastq-split {rbt_output_paths} {read_cmd} {log} ; wait")
    command_lines = "\n".join(command_lines)
else:
    command_lines = f"rbt fastq-split {snakemake.output} {read_cmd} {log}"

shell(command_lines)
 
