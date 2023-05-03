__author__ = "Silas Kieser"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

### loging all exceptiuon to log file if available
import sys
import logging, traceback


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
            if hasattr(key, log):
                stderr_file = log[key]

        for key in ["stdout", "out"]:
            if hasattr(key, log):
                stdout_file = log[key]

        if (stderr_file is None) or (stderr_file is None):
            warnings.warn(
                "Cannot infer which logfile is stderr and which is stdout, Logging stderr and stdout to the same file"
            )
            return None, log[0]

        else:
            return stdout_file, stderr_file


def multiple_log_fmt_shell(snakemake, append_stderr=False, append_stdout=False):
    """
    Format shell command for logging to stdout and stderr files.
    """

    from snakemake.script import _log_shell_redirect

    stderr_file, stdout_file = infer_stdout_and_stderr(snakemake.log)

    if stdout_file is None:
        return snakemake.log_fmt_shell(append=append_stdout)
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
    level=logging.INFO,
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

##############################################################
## helper functions they should go in snakemake_wrapper_utils


# global flags to check if input and output are parsed multiple times
parsed_input, parsed_output = False, False


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
        parsed_arg = f" in1={values[0]} in2={values[1]} "

    else:
        # multiple files
        logger.error(
            "More than 2 files provided, this case cannot be parsed unambigously! I parse it as a comma seperated list of files."
        )

        parsed_arg = f" {key}=" + ",".join(values)

    logger.info(f"parsed {input_or_output} argument: {parsed_arg}")

    if input_or_output == "input":
        parsed_input = True
    else:
        parsed_output = True

    return parsed_arg


def __parse_bbtools_keywords(
    command,
    extra="",
    input_keys=["input", "fastq", "sample"],
    output_keys=["out", "output"],
    ignore_keys=["flag"],
    **kwargs,
):
    """
    Parse rule input, output and params into a bbmap command.

    Run as.
        parse_bbmap(
        **snakemake.input, **snakemake.params, **snakemake.output

    Special params:
        'command' in params to define the bbmap command
        input_keys: list of keywords that are parsed as input
        output_keys: list of keywords that are parsed as output
        ignore_keys: list of keywords that are ignored
        extra: extra arguments that are added to the command

    """

    # add extra arguments  at the beginning

    logger.info(f"extra arguments at the begginging: {extra} ")
    command += f" {extra} "

    for k in kwargs:
        if k in ignore_keys:
            logger.info(f"{k} argument detected, This is not passed to the bbtool.")
            pass

        # INPUT
        if k in input_keys:
            logger.info(f"{k} argument detected, parsing it as input.")
            command += _parse_bbmap_in_out("input", kwargs[k])

        # OUTPUT
        if k in output_keys:
            logger.info(f"{k} argument detected, parsing it as output.")
            command += _parse_bbmap_in_out("output", kwargs[k])

        else:
            # bool conversions
            if type(kwargs[k]) == bool:
                kwargs[k] = "t" if kwargs[k] else "f"

            # if list
            if isinstance(kwargs[k], list):
                kwargs[k] = ",".join(kwargs[k])

            command += f" {k}={kwargs[k]} "

    return command


def __check_for_duplicated_keywords(snakemake):
    input_keys = snakemake.input.keys()
    output_keys = snakemake.output.keys()
    params_keys = snakemake.params.keys()

    all_keys = input_keys + output_keys + params_keys

    if len(all_keys) != len(set(all_keys)):
        raise Exception("Duplicated keywords in input, output or params")


def parse_bbmap(snakemake):
    from snakemake_wrapper_utils.java import get_java_opts

    java_opts = get_java_opts(snakemake)
    # log = snakemake.log_fmt_shell(stdout=True, stderr=True,append=True)
    log = multiple_log_fmt_shell(snakemake, append_stderr=True)

    if not hasattr(snakemake.params, "command"):
        raise Exception("params needs 'command' argument")

    ## keywords
    __check_for_duplicated_keywords(snakemake)

    command = parse_bbmap(**snakemake.input, **snakemake.params, **snakemake.output)
    command += f" {java_opts} t={snakemake.threads} {log}"


######################################
## beginn of wrapper


from snakemake.shell import shell


command = parse_bbmap(snakemake)
logger.info(f"run command:\n\n\t{command}\n")

shell(command)
