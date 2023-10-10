__author__ = "Silas Kieser"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

### loging all exceptiuon to log file if available
import sys
import logging, traceback


input_keys = ["input", "fastq", "sample", "reads"]
output_keys = ["out", "output"]
ignore_keys = [
    "flag",
    # are parsed seperately
    "extra",
    "command",
]

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


def infer_stdout_and_stderr(log) -> tuple:
    """
    If multiple log files are provided, try to infer which one is for stderr.

    If only one log file is provided, or inference fails, return None for stdout_file


    Returns
    -------
    tuple
        stdout_file, stderr_file


    """
    import warnings

    if len(log) == 0:
        return None, None

    elif len(log) == 1:
        return None, log[0]

    else:
        # infer stdout and stderr file
        for key in ["stderr", "err"]:
            if hasattr(log, key):
                stderr_file = log[key]

        for key in ["stdout", "out"]:
            if hasattr(log, key):
                stdout_file = log[key]

        if (stderr_file is None) or (stderr_file is None):
            warnings.warn(
                "Cannot infer which logfile is stderr and which is stdout, Logging stderr and stdout to the same file"
            )
            return None, log[0]

        else:
            return stdout_file, stderr_file


def multiple_log_fmt_shell(snakemake, append_stderr=False, append_stdout=False) -> str:
    """
    Format shell command for logging to stdout and stderr files.
    """

    from snakemake.script import _log_shell_redirect

    stdout_file, stderr_file = infer_stdout_and_stderr(snakemake.log)

    if stdout_file is None:
        # log both to the same file
        return snakemake.log_fmt_shell(
            append=append_stderr or append_stdout, stdout=True, stderr=True
        )
    else:
        # sucessfully inferred und stderr and stdout file

        shell_log_fmt = (
            _log_shell_redirect(
                stderr_file, stdout=False, stderr=True, append=append_stderr
            )
            + " "
            + _log_shell_redirect(
                stdout_file, stdout=True, stderr=False, append=append_stdout
            )
        )

        return shell_log_fmt


try:
    _, logfile = infer_stdout_and_stderr(snakemake.log)

    # clear stderr file
    open(logfile, "w").close()

except:
    print("No log file provided, logging to stdout")
    logfile = None

logging.basicConfig(
    filename=logfile,
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error(
        "".join(
            [
                "Uncaught exception: ",
                *traceback.format_exception(exc_type, exc_value, exc_traceback),
            ]
        )
    )


# Install exception handler
sys.excepthook = handle_exception

logger = logging.getLogger(__file__)

###################################### Beginning of logging ######################################


# global flags to check if input and output are parsed multiple times
parsed_input, parsed_output = False, False

import warnings
from snakemake_wrapper_utils.java import get_java_opts


def _parse_bbmap_in_out(input_or_output, values):
    """
    Parse input or output arguments.

    Single files are parsed as:

        in=values

    Two files are parsed as:

        in1=values[0] in2=values[1]

    More than two files are parsed as:

        in=values[0],values[1],values[2],...

    the same applies to output arguments (out=).

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

    logger.info(f"parsed {input_or_output} argument: {parsed_arg}")

    if input_or_output == "input":
        parsed_input = True
    else:
        parsed_output = True

    return parsed_arg


def __parse_keywords_for_bbtool(parameter_list, section):
    """
    Parse rule input, output and params into a bbmap command.

    Run as.
        __parse_keywords_for_bbtool(
        snakemake.input,"input")


    """

    logger.info(f"Parse {section} section of snamemake rule into bbmap command")

    if section == "input":
        special_keys = input_keys
    elif section == "output":
        special_keys = output_keys
    elif section == "params":
        special_keys = []
    else:
        raise Exception("section should be 'input', 'output' or 'params'")

    # command to be build
    command = ""

    keys = list(parameter_list.keys())

    logger.debug(f"parameter_list: {parameter_list}")

    # get number of unnamed arguments as the position of the first named argument
    keys_with_positions = parameter_list._names
    first_key = next(iter(keys_with_positions.items()))
    n_unnamed_arguments = first_key[1][0]

    if n_unnamed_arguments > 0:
        assert section in ["input", "output"]
        logger.info(
            f"Found {n_unnamed_arguments} unnamed arguments. parse them as {section}"
        )

        command += _parse_bbmap_in_out(
            section, [parameter_list[i] for i in range(n_unnamed_arguments)]
        )

    # transform to dict
    parameter_list = dict(parameter_list)

    for k in keys:
        logger.info(f"Parse keyword: {k}")
        if k in ignore_keys:
            logger.info(f"{k} argument detected, This is not passed to the bbtool.")
            pass

        # INPUT/OUTPUT
        elif k in special_keys:
            assert section in ["input", "output"]
            logger.info(f"Parsing it as {section}.")
            command += _parse_bbmap_in_out(section, parameter_list[k])

        else:
            # bool conversions
            if type(parameter_list[k]) == bool:
                parameter_list[k] = "t" if parameter_list[k] else "f"

            # collapse list
            if isinstance(parameter_list[k], list):
                parameter_list[k] = ",".join(parameter_list[k])

            parsed = f" {k}={parameter_list[k]} "

            logger.info(f"parsed argument: {parsed}")
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
    ## keywords
    __check_for_duplicated_keywords(snakemake)

    if not hasattr(snakemake.params, "command"):
        raise Exception("params needs 'command' parameter")
    else:
        command = snakemake.params.command
        assert type(command) == str, "command should be a string"
        assert len(command.split()) == 1, "command should not contain spaces"
        assert command.endswith(".sh"), "command should end with .sh"

        command_with_parameters = command
        logger.info(f"command is: {command_with_parameters}")

        # add extra arguments  at the beginning
        if hasattr(snakemake.params, "extra"):
            extra = snakemake.params.extra
            assert type(extra) == str, "extra should be a string"
            logger.info(f"extra arguments: {extra} ")
            command_with_parameters += f" {extra} "

    command_with_parameters += __parse_keywords_for_bbtool(snakemake.input, "input")
    command_with_parameters += __parse_keywords_for_bbtool(snakemake.output, "output")
    command_with_parameters += __parse_keywords_for_bbtool(snakemake.params, "params")

    # Add threads if not in single threaded scripts
    if command in single_threaded_scripts:
        if snakemake.threads > 3:
            logger.warning(
                f"Shell script {shell_script} will only use 1-3 threads, but you specify {snakemake.threads} threads. I ignore the threads argument."
            )
    else:
        command_with_parameters += f" threads={snakemake.threads} "

    # memory
    java_opts = get_java_opts(snakemake)

    # log
    log = multiple_log_fmt_shell(snakemake, append_stderr=True)

    command_with_parameters += f" {java_opts} {log}"

    return command_with_parameters


######################################
## beginn of wrapper


from snakemake.shell import shell


command = parse_bbtool(snakemake)
logger.info(f"run command:\n\n\t{command}\n")

shell(command)
