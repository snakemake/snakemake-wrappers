#! coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from typing import Dict, Generator, List, Tuple, Union  # Compatibility with Python 3.7

import argparse  # Search in command line argument to predict output file suffixes
import os.path  # Get output files prefix
import warnings  # Warn user on un-supported subcommands


def parse_args(io: Dict[str, Union[str, List[str]]]) -> str:
    """
    Build command line from a mapping: arg / path
    """
    args = ""
    for argname, path in io.items():
        # Some keys in a GFF/GTF can contain interpretable characters in bash.
        # Variable `path` is being casted into strings, and `:q` argument
        # cannot be used to quote strings. Back to plain old quotes.
        argname = f" --{argname} " if len(argname) > 1 else f" -{argname} "

        if isinstance(path, str):
            args += f" {argname} '{path}'"

        # Handle repeated arguments for commands like `agat_sp_merge_annotations.pl`
        elif isinstance(path, list):
            args += "".join([f" {argname} '{p}' " for p in path])

    return args


def join_and_run_commands(command_lines: str) -> None:
    """
    Safely join multiple commands and run them.
    """
    # Make sure each command line is use one after each other
    # if and only if the previous had a zero return code
    # (in case default Snakemake behavior was modified)
    command_lines = " && ".join(command_lines)

    # Run all command lines in a subshell to gather all std/err logs
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    shell(f"({command_lines}) {log}")


def shell_rename(source: str, destination: str) -> str:
    """
    Move/Rename files with Shell rather than Python, in order
    to keep a track of renaming scheme in Snakemake logs
    """
    # Make sure bash-interpretable characters are not interpreted
    # Make sure spaces are not splitted
    # Snakemake syntax :q to quote does not work here, using plain quotes
    return f"mv --verbose '{source}' '{destination}'"


def move_multiple_files(
    expected_files: Dict[str, str], snakemake_output: Dict[str, str]
) -> Generator[str, None, None]:
    """
    For each expected file in expected_files mapping, search if user
    expects them in snakemake.output. It so, yield shell_rename.
    """
    for key, path in expected_files.items():
        snake_out = snakemake_output.get(key)
        if snake_out:
            yield shell_rename(path, snake_out)


def get_gff_basename(snake_input) -> str:
    """
    Search the GFF/GTF input file name among the list of possible

    """
    # One of the output file is build on the GFF/GTF input file
    gff_basename = ""
    gff_keys = ("f", "ref", "reffile", "gff", "gff3", "gtf")
    for key in gff_keys:
        gff = snakemake.input.get(key)
        if gff:
            # Case GFF is found
            gff_basename = os.path.basename(gff)
            break
    else:
        # Case no GFF is found at all
        raise KeyError(
            "A GFF/GTF should be provided using one of "
            f"{gff_keys} key in snakemake rule."
        )

    return gff_basename


def find_arg_value(extra: str, param_name: str | Tuple[str], default: str) -> str:
    """
    Somme commands name the output files with suffixes depending on
    parameter value. This function returns the value given to a parameter.

    Note that agat does not allow `--param=value` scheme, and only accepts
    `--param value`
    """
    # Remove double spaces
    extra = " ".join(extra.split())

    if isinstance(param_name, str):
        param_name = (param_name,)

    # Seach parameter name
    params = extra.split()
    for index, param in enumerate(params):
        if param in param_name:
            return params[index + 1]

    # Case parameter is not in the provided `extra`
    return default


# While most of the commands ends with ".pl", some of them don't
# (e.g. `agat config`). We are not adding ".pl" automatically,
# and let user provide the exact agat command/script name.
command = snakemake.params.get("command")

if command is None:
    raise ValueError(
        "An agat script name or subcommand "
        "should be given through the snakemake rule params."
    )
elif command in (
    "agat_sp_compare_two_BUSCOs.pl",
    "agat_sp_filter_by_mrnaBlastValue.pl",
    "agat_sp_load_function_from_protein_align.pl",
):
    warning.warn(f"The command `{command}` was not tested in Agat Snakemake-Wrappers.")


# Handling optional parameters
extra = snakemake.params.get("extra", "")

if command == "agat_convert_minimap2_bam2gff.pl":
    # This command allows either `-i` or `--input` to specify BAM file.
    # Since `input` is a protected keyword in Snakemake, the only key that
    # works to point to BAM is `i`.
    input_file = str(snakemake.input["i"])
    if input_file.endswith("bam"):
        extra += " --bam "
    elif input_file.endswith("sam"):
        extra += " --sam "

# Some commands produce file(s) with fixed names. To avoid collisions
# during possible concurrent execution, these commands will be executed in
# a temporary directory.
if command in ("config", "levels"):
    # Special case: output file name cannot be chosen freely
    with TemporaryDirectory() as tempdir:
        yaml_file = "agat_config.yaml" if command == "config" else "feature_levels.yaml"
        join_and_run_commands(
            [
                # Move to tempdir and execute agat command
                f"cd {tempdir}",
                f"agat {command} --expose",
                "cd -",
                # Make results available where user expects them
                shell_rename(f"{tempdir}/{yaml_file}", snakemake.output),
            ]
        )

elif command == "agat_sp_extract_attributes.pl":
    # Special case: output file name have a fixed suffix.
    # In order to let user choose output file name freely, we must
    # move the results at the end of the command execution.
    # The argument `--att` contains a single attribute, or a comma-separated
    # list of attributes that will be used as file extension.
    # e.g. `--att Parents,ID --out prefix` that will produce both
    # `prefix_Parents` and `prefix_ID` files.

    # We avoid name collision and ensure temporary file deletion
    # with a temporary directory for execution:

    with TemporaryDirectory() as tempdir:
        # We need to identify them in order to rename them correctly. To do so,
        # we'll use the keys in the output section of the Snakemake rule to build
        # the command line and link a result to its correct name.
        att = " --att "
        for argvalue in snakemake.output.keys():
            if att.endswith(" "):
                att += str(argvalue)
            else:
                att += f",{argvalue}"
        basename = f"{tempdir}/snake_out_prefix"
        extra += f" {att} --out {basename} "
        extra += parse_args(snakemake.input)

        # Get GFF
        gff = snakemake.input.get("g")
        if not gff:
            gff = snakemake.input.get("gff")

        command_lines = [f"{command} {extra}"]

        for suffix, path in snakemake.output.items():
            # Make results available where user expects them
            command_lines.append(shell_rename(f"{basename}_{suffix}", path))

        join_and_run_commands(command_lines)

elif command == "agat_sp_filter_by_ORF_size.pl":
    # Special case: This command returns a pair of files:
    # 1. All genic features with and ORF that statisfies command line criteria
    # 2. Rest of the genic features (aka. NOT satisfying command line criteria)
    # Output file extention are defined according to command line content.
    with TemporaryDirectory() as tempdir:
        # Add a known prefix to output files
        prefix = f"{tempdir}/snake_out_ORF"
        extra += f" --outfile {prefix} "
        extra += parse_args(snakemake.input)
        command_lines = ["{command} {extra}"]

        # Output file extension can be predicted from command line:
        test = "sup"  # Default test value is >
        test_value = find_arg_value(
            extra=extra,
            param_name=("--test", "-t"),
            default=">",
        )
        # Either over of inferior
        if ">" in test_value:
            test = "sup"
        elif "<" in test_value:
            test = "inf"

        # May be equal or over (sup=) or equal or inferior (inf=)
        if "=" in test_value:
            test += "="

        size = find_arg_value(
            extra=extra,
            param_name=("--size", "-s"),
            default="100",
        )
        matched = f"{prefix}_{test}{size}.gff"
        unmatched = f"{prefix}_NOT_{test}{size}.gff"

        # Make output files available for user
        snake_matched = snakemake.output.get("matched")
        if snake_matched:
            command_lines.append(shell_rename(matched, snake_matched))

        snake_unmatched = snakemake.output.get("unmatched")
        if snake_unmatched:
            command_lines.append(shell_rename(unmatched, snake_unmatched))

        join_and_run_commands(command_lines)

elif command in ("agat_sp_fix_fusion.pl", "agat_sp_fix_longest_ORF.pl"):
    # Special case: 4 output files with forced suffixes to handle.
    # The same suffixes are applied to both subcommands

    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    with TemporaryDirectory() as tempdir:
        prefix = f"{tempdir}/snake_out_fix_fusion"
        extra += f" --outfile {prefix} "
        extra += parse_args(snakemake.input)
        command_lines = [f"{command} {extra}"]

        # Make output file available on use request
        for expected_output in ("all", "intact", "only_modified", "report"):
            snake_out = snakemake.output.get(expected_output)
            if snake_out:
                ext = "txt" if expected_output == "report" else "gff"
                # Protect bash-interpretable characters in file names
                command_lines.append(
                    shell_rename(f"{prefix}-{expected_output}.{ext}", snake_out)
                )

        join_and_run_commands(command_lines)

elif command == "agat_sp_manage_UTRs.pl":
    # Special case. This command produces between 2 and 4 files, depending on
    # command line parameters.

    # This command does not parse output path name like the others. Only the basename
    # of the output path provided in `--output` is kept. This leads to potential
    # output file name collision: we need to move into the tempdir to execute
    # the command line.
    with TemporaryDirectory() as tempdir:
        command_lines = []
        prefix = f"snake_out_manage_utr"
        extra += f" --output '{prefix}' "
        # extra += parse_args(snakemake.input)

        # Activate histograms on user request
        if any(path.endswith(".pdf") for path in snakemake.output):
            extra += " --plot "

        for input_file_path in snakemake.input:
            arg = "--ref"
            if input_file_path.endswith(".yaml"):
                arg = "--config"

            basename = os.path.basename(input_file_path)
            command_lines.append(
                "ln --symbolic --force --relative --verbose "
                "'{input_file_path}' '{tempdir}/{basename}'"
            )
            extra += f" {arg} '{tempdir}/{basename}' "

        command_lines += [
            f"cd {tempdir}",
            f"{command} {extra}",
            f"cd -",
        ]

        # Default threshold value (used in output suffix)
        threshold = find_arg_value(
            extra=extra,
            param_name=("-n", "-g", "--nb", "--number"),
            default="5",
        )

        # Make output file(s) available on user request
        expected_output_files = {
            "five_prime_utr_overORequal": f"{tempdir}/{prefix}/five_prime_utr_overORequal{threshold}.pdf",
            "five_prime_utr_under": f"{tempdir}/{prefix}/five_prime_utr_under{threshold}.pdf",
            "three_prime_utr_overORequal": f"{tempdir}/{prefix}/three_prime_utr_overORequal{threshold}.pdf",
            "three_prime_utr_under": f"{tempdir}/{prefix}/three_prime_utr_under{threshold}.pdf",
            "both_utr_overORequal": f"{tempdir}/{prefix}/1_UTR3_overORequal{threshold}_and_UTR5_overORequal{threshold}.gff",
            "both_utr_under": f"{tempdir}/{prefix}/1_UTR3_under{threshold}_and_UTR5_under{threshold}.gff",
            "report": f"{tempdir}/{prefix}/report.txt",
        }

        command_lines += list(
            move_multiple_files(expected_output_files, snakemake.output)
        )
        join_and_run_commands(command_lines)

elif command == "agat_sp_manage_introns.pl":
    # Special case: 1 to 5 files are created depending on command line
    # parameters. Quite similar with the previous case, yet the list
    # of output file differs.
    with TemporaryDirectory() as tempdir:
        # Build command line
        if any(path.endswith(".pdf") for path in snakemake.output):
            extra += " --plot "

        extra += parse_args(snakemake.input)
        # The subdir is required here, since the output path cannot end with "/" or
        # be a directory. Or else, an error is raised with output files not being
        # at their expected location
        extra += f" --output {tempdir}/snake_out "
        command_lines = [f"{command} {extra}"]

        expected_output_files = {
            "cds_pdf": f"{tempdir}/snake_out/intronPlot_cds.pdf",
            "exon_pdf": f"{tempdir}/snake_out/intronPlot_exon.pdf",
            "five_prime_utr_pdf": f"{tempdir}/snake_out/intronPlot_five_prime_utr.pdf",
            "three_prime_utr_pdf": f"{tempdir}/snake_out/intronPlot_three_prime_utr.pdf",
            "report": f"{tempdir}/snake_out/report.txt",
        }
        command_lines += list(
            move_multiple_files(expected_output_files, snakemake.output)
        )
        join_and_run_commands(command_lines)


elif command == "agat_sp_manage_functional_annotation.pl":
    # Special case: Multiple optional output files, 3 to 10 files are
    # created by this command depending on the available input.

    with TemporaryDirectory() as tempdir:
        # Build command line
        prefix = f"{tempdir}/snake_out"
        extra += parse_args(snakemake.input)
        extra += f" --output {prefix} "
        command_lines = [f"{command} {extra}"]

        # Make output available on user request
        gff_basename = get_gff_basename(snakemake.input)
        expected_output_files = {
            "gff": f"{prefix}/{gff_basename}",
            "report": f"{prefix}/report.txt",
            "error": f"{prefix}/error.txt",
            "duplicates": f"{prefix}/duplicatedNameFromBlast.txt",
            "cdd": f"{prefix}/CDD.txt",
            "go": f"{prefix}/GO.txt",
            "interpro": f"{prefix}/InterPro.txt",
            "mobidb": f"{prefix}/MobiDBLite.txt",
            "panther": f"{prefix}/PANTHER.txt",
            "superfamily": f"{prefix}/SUPERFAMILY.txt",
        }
        command_lines += list(
            move_multiple_files(expected_output_files, snakemake.output)
        )
        join_and_run_commands(command_lines)

elif command == "agat_sp_statistics.pl":
    # Special case: 1 to 2 files depending on command line and a whole
    # directory based on the content of the input file.

    with TemporaryDirectory() as tempdir:
        # Build command line
        prefix = f"{tempdir}/snake_out"
        extra += parse_args(snakemake.input)
        extra += f" --output {prefix} "

        if snakemake.output.get("yaml"):
            extra += " --yaml "

        if snakemake.output.get("plot"):
            extra += " -p "

        command_lines = [f"{command} {extra}"]

        # Make output available on user request
        expected_output_files = {
            "report": prefix,
            "yaml": f"{prefix}.yaml",
            "plot": f"{prefix}_distribution_plots",
        }
        command_lines += list(
            move_multiple_files(expected_output_files, snakemake.output)
        )
        join_and_run_commands(command_lines)

else:
    # Generic case, will work for most of the agat subcommands.
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    # While subcommnds usully answer the same command line interface,
    # some of them have unexpected changes in argument names.
    # IO arguments will be acquired from snakemake rule IO keys.
    io = {**snakemake.input, **snakemake.output}
    extra += parse_args(io)

    shell("{command} {extra} {log}")
