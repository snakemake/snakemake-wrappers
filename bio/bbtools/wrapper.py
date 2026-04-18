__author__ = "Silas Kieser"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

### loging all exceptiuon to log file if available
import sys
import logging, traceback
import warnings

input_keys = ["input", "fastq", "sample", "reads"]
# keys that can be used with 1,2, as suffixes to indicate the paired end reads.
paired_keys = ["in", "out", "outm", "outu", "outmatch"]

single_threaded_scripts = [
    "pileup.sh",
    "summarizescafstats.sh",
    "filterbycoverage.sh.",
    "mergeOTUs.sh",
    "bbest.sh",
    "summarizeseal.sh",
    "bbcountunique.sh",
    "commonkmers.sh",
    "callpeaks.sh",
    "kcompress.sh",
    "stats.sh",
    "statswrapper.sh",
    "fungalrelease.sh",
    "filterbytaxa.sh",
    "gi2taxid.sh",
    "gitable.sh",
    "sortbytaxa.sh",
    "taxonomy.sh",
    "taxtree.sh",
    "reducesilva.sh",
    "synthmda.sh",
    "crosscontaminate.sh",
    "dedupebymapping.sh",
    "randomreads.sh",
    "bbfakereads.sh",
    "gradesam.sh",
    "samtoroc.sh",
    "addadapters.sh",
    "grademerge.sh",
    "printtime.sh",
    "msa.sh",
    "cutprimers.sh",
    "matrixtocolumns.sh",
    "countbarcodes.sh",
    "filterbarcodes.sh",
    "mergebarcodes.sh",
    "removebadbarcodes.sh",
    "demuxbyname.sh",
    "filterbyname.sh",
    "filtersubs.sh",
    "getreads.sh",
    "shred.sh",
    "fuse.sh",
    "shuffle.sh",
    "textfile.sh",
    "countsharedlines.sh",
    "filterlines.sh",
    "makechimeras.sh",
    "phylip2fasta.sh",
    "readlength.sh",
    "reformat.sh",
    "rename.sh",
    "repair.sh",
    "bbsplitpairs.sh",
    "splitnextera.sh",
    "splitsam.sh",
    "testformat.sh",
    "translate6frames.sh",
]

logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__file__)

###################################### Beginning of wrapper ######################################
# global flags to check if input and output are parsed multiple times
parsed_input, parsed_output = False, False

import re
from snakemake_wrapper_utils import java
from snakemake.shell import shell


def get_java_opts(snakemake, java_mem_overhead_factor=0.15) -> str:
    """Obtain mem from params, and handle resource definitions in resources.
    As there was conflicts https://github.com/snakemake/snakemake-wrapper-utils/pull/37
    """

    all_java_opts = java.get_java_opts(snakemake, java_mem_overhead_factor)

    # regex to extract only the "-Xmx" part

    regex = re.compile(r"-Xmx\d+[gGmM]")
    memory_options = regex.findall(all_java_opts)[0]

    logger.debug(f"Memory specification: {memory_options}")

    return memory_options


## Get positional arguments
# TODO: replace with snakemake logging once it is implemented
## Will be implemented in Snakemake https://github.com/snakemake/snakemake/pull/2509
def _get_unnamed_arguments(parameter_list):
    """
    Get unnamed arguments of snakemake.input or snakemake.output.
    Find it as the first key in the parameter_list.

    Run as:
        _get_unnamed_arguments(snakemake.input)

    """
    keys_with_positions = parameter_list._names
    if len(keys_with_positions) == 0:
        # all arguments are unnamed
        return parameter_list

    first_key = next(iter(keys_with_positions.items()))
    n_unnamed_arguments = first_key[1][0]

    logger.debug(f"Found {n_unnamed_arguments} unnamed arguments")
    # as for input arguments either is is a string or a list of strings
    if n_unnamed_arguments == 1:
        return parameter_list[0]
    else:
        return [parameter_list[i] for i in range(n_unnamed_arguments)]


def _parse_in_out(input_or_output, values):
    """
    Parse input or output arguments.

    With global check that is not parsed multiple times.

    """

    if input_or_output == "input":
        key = "in"
        global parsed_input
        already_parsed = parsed_input
    elif input_or_output == "output":
        key = "out"
        global parsed_output
        already_parsed = parsed_output

    else:
        raise Exception("input_or_output should be 'input' or 'output'")

    if already_parsed:
        raise Exception(f"{input_or_output} should be defined only once!")

    parsed_arg = _parse_paired_keys(key, values)
    logger.debug(f"parsed {input_or_output} argument: {parsed_arg}")

    if input_or_output == "input":
        parsed_input = True
    else:
        parsed_output = True

    return parsed_arg


def _parse_paired_keys(key, values):
    """
    Some keys in bbtools can be used with 1,2, as suffixes to indicate the paired end reads.

    Single files are parsed as:

        in=values

    Two files are parsed as:

        in1=values[0] in2=values[1]

    More than two files are parsed as:

        in=values[0],values[1],values[2],...

    the same applies to output arguments (out=).

    """
    if len(values) == 1 or isinstance(values, str):
        # single input file
        parsed_arg = f" {key}={values} "

    elif len(values) == 2:
        parsed_arg = f" {key}1={values[0]} {key}2={values[1]} "

    else:
        # multiple files
        warnings.warn(
            "More than 2 files provided, this case cannot be parsed unambigously! I parse it as a comma seperated list of files."
        )

        parsed_arg = f" {key}=" + ",".join(values)

    logger.debug(f"parsed {key} argument: {parsed_arg}")
    return parsed_arg


def _parse_keywords_for_bbtool(parameter_list, section):
    """
    Parse rule input, output and params into a bbmap command.

    Run as.
        _parse_keywords_for_bbtool(
        snakemake.input,"input")


    """

    logger.debug(f"Parse {section} section of snamemake rule into bbmap command")

    if section == "params":
        ignore_keys = ["command", "extra"]
    else:
        ignore_keys = ["flag"]

    # command to be build
    command = ""

    logger.debug(f"parameter_list: {parameter_list}")

    ## unnamed arguments
    unnamed_arguments = _get_unnamed_arguments(parameter_list)

    if len(unnamed_arguments) > 0:
        assert section in ["input", "output"]
        logger.debug(f"Found unnamed arguments. parse them as {section}")

        command += _parse_in_out(section, unnamed_arguments)

    # parameters with keywords
    # transform to dict
    parameter_list = dict(parameter_list)

    for k in parameter_list.keys():
        logger.debug(f"Parse keyword: {k}")
        if k in ignore_keys:
            logger.debug(f"{k} argument detected, This is not passed to the bbtool.")
            pass

        # INPUT keys
        elif (k in input_keys) and (section == "input"):
            command += _parse_in_out(section, values=parameter_list[k])

        ## OUTPUT keys that can be paired
        elif k in paired_keys:
            if k == "out":
                command += _parse_in_out(section, values=parameter_list[k])
            # Other keys that can be paired, e.g. outm
            else:
                command += _parse_paired_keys(k, parameter_list[k])

        # other keys
        else:
            # bool conversions
            if type(parameter_list[k]) == bool:
                parameter_list[k] = "t" if parameter_list[k] else "f"

            # collapse list
            if isinstance(parameter_list[k], list):
                parameter_list[k] = ",".join(parameter_list[k])

            parsed = f" {k}={parameter_list[k]} "

            logger.debug(f"parsed argument: {parsed}")
            command += parsed

    return command


def __check_for_duplicated_keywords(snakemake):
    input_keys = list(snakemake.input.keys())
    output_keys = list(snakemake.output.keys())
    params_keys = list(snakemake.params.keys())

    all_keys = input_keys + output_keys + params_keys

    if len(all_keys) != len(set(all_keys)):
        raise Exception("Duplicated keywords in input, output or params")


def parse_bbtool(snakemake):
    """
    Assembles the bbtools wrapper shell command from Snakemake inputs, outputs, params, and runtime settings.

    Validates that `snakemake.params.command` is present and is a single-word string without any whitespace, ending with ".sh".
    Adds `snakemake.params.extra`, if present, asserting it is a string.
    Parses inputs, outputs, and params into bbtools-style arguments, appends thread and Java memory options, adds the "-eoom" flag, and includes shell log redirections.

    Returns:
        command (str): The fully assembled command string ready to be executed in the shell.

    Raises:
        Exception: If `snakemake.params.command` is not provided.
        AssertionError: If `command` or `extra` have invalid types or formats.
    """

    java_opts = get_java_opts(snakemake, java_mem_overhead_factor=0.15)
    extra = snakemake.params.get("extra", "")

    ## keywords
    __check_for_duplicated_keywords(snakemake)

    # Add threads if not in single threaded scripts
    threads = snakemake.threads
    if snakemake.params.command in single_threaded_scripts:
        if snakemake.threads > 3:
            logger.warning(
                f"{snakemake.params.command} will only use 1-3 threads, but you specified {snakemake.threads} threads. Threads will be capped at 3."
            )
            threads = 3

    input = _parse_keywords_for_bbtool(snakemake.input, "input")
    params = _parse_keywords_for_bbtool(snakemake.params, "params")
    output = _parse_keywords_for_bbtool(snakemake.output, "output")

    return f"{snakemake.params.command} {java_opts} -eoom threads={threads} {input} {params} {extra} {output}"


command = parse_bbtool(snakemake)
logger.debug(f"run command:\n\n\t{command}\n")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("{command} {log}")
