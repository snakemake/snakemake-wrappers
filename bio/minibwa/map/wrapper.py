# coding: utf-8

"""Snakemake wrapper for minibwa mapping"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from os.path import commonprefix
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts
from tempfile import TemporaryDirectory

# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Extract ordering parameters (if any)
sort = snakemake.params.get("sort")
available_sort_tools = {"samtools", "picard", "sambamba", None}
if sort not in available_sort_tools:
    raise ValueError(
        "Unexpected value for `params.sort`. "
        f"Expected one of {available_sort_tools}, got `{sort}`."
    )
sort_extra = snakemake.params.get("sort_extra", "")

expected_sort_orders = {"coordinate", "queryname", None}
sort_order = snakemake.params.get("sort_order", "coordinate")
if sort_order not in expected_sort_orders:
    raise ValueError(
        "Unexpected value for `params.sort_order`. "
        f"Expected one of {expected_sort_orders}, got `{sort_order}`."
    )

# Extract index from input
# and check that all required indices are declared
index_prefix = commonprefix([str(o) for o in snakemake.input.index]).rstrip(".")
if len(index_prefix) == 0:
    raise ValueError("Could not determine common prefix of `input.index` files.")

# Build command line(s)
align_format = get_format(snakemake.output[0])
align_format_available = {"sam", "bam", "cram"}
if align_format not in align_format_available:
    raise ValueError(
        "Unexpected alignment format in `output[0]`: "
        f"{align_format_available}, got `{align_format}`."
    )
out_cmd = f"> '{snakemake.output[0]}'"

with TemporaryDirectory() as tempdir:
    if (sort is None) and (align_format in {"bam", "cram"}):
        # Get samtools view optional parameters
        samtools_view_opts = get_samtools_opts(
            snakemake,
            parse_threads=False,
            parse_ref=True,
            parse_regions=False,
            parse_write_index=True,
            parse_output=True,
            parse_output_format=True,
        )
        out_cmd = f" | samtools view {samtools_view_opts}"

    elif sort == "samtools":
        # Get samtools sort optional parameters
        samtools_sort_opts = get_samtools_opts(
            snakemake,
            parse_threads=True,
            parse_ref=True,
            parse_regions=False,
            parse_write_index=True,
            parse_output=True,
            parse_output_format=True,
        )

        # Add sort order
        if sort_order == "queryname":
            samtools_sort_opts += " -n "

        # Add user-defined sort arguments
        samtools_sort_opts += f" {sort_extra}"

        out_cmd = f" | samtools sort {samtools_sort_opts} -T '{tempdir}'"

    elif sort == "picard":
        # Get java optional parameters
        java_opts = get_java_opts(snakemake)
        out_cmd = str(
            f" | picard SortSam {java_opts} "
            "--INPUT /dev/stdin "
            f"--TMP_DIR '{tempdir}' "
            f"--SORT_ORDER '{sort_order}' "
            f"--OUTPUT '{snakemake.output[0]}' "
            f"{sort_extra}"  # Add user-defined sort arguments
        )
        if "fasta" in snakemake.input.keys():
            out_cmd += f" --REFERENCE_SEQUENCE {snakemake.input.fasta}"

        if "idx" in snakemake.output.keys():
            out_cmd += f" --CREATE_INDEX"

    elif sort == "sambamba":
        # Define sambamba default arguments
        # Note that sambamba sort only reads bam format
        out_cmd = str(
            f" | samtools view -bh | sambamba sort '/dev/stdin' "
            f"--tmpdir '{tempdir}' "
            f"--nthreads {snakemake.threads} "
            f"{sort_extra}"  # Add user-defined sort arguments
        )
        # Add sort order
        if sort_order == "queryname":
            out_cmd += " --sort-by-name"

        # Sambamba only output sam/bam/json/unpacked streams
        # We have to handle cram and format auto-detection.
        if align_format in {"sam", "cram"}:
            # Compression starts once sort is done, there is no
            # threads concurrency
            samtools_view_opts = get_samtools_opts(
                snakemake,
                parse_threads=False,
                parse_ref=True,
                parse_regions=False,
                parse_write_index=True,
                parse_output=True,
                parse_output_format=True,
            )
            # Pipe the output to samtools view to enable CRAM compression, or
            # plain SAM output.
            out_cmd += f"  --out '/dev/stdout' "
            out_cmd += f" | samtools view {samtools_view_opts}"
        else:
            # Else, let sambamba write bam.
            out_cmd += f"  --out '{snakemake.output[0]}' "

            # Optionally write index
            if "idx" in snakemake.output.keys():
                out_cmd += str(
                    f" && sambamba index --nthreads {snakemake.threads} "
                    f"'{snakemake.output[0]}' '{snakemake.output.idx}'"
                )

    # Run command(s)
    shell(
        "(minibwa map -t {snakemake.threads} {extra} {index_prefix} "
        "{snakemake.input.reads} {out_cmd}) {log}"
    )
