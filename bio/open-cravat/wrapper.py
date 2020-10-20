__author__ = "Rick Kim"
__copyright__ = "Copyright 2020, Rick Kim"
__license__ = "GPLv3"

from snakemake.shell import shell
import os
from types import SimpleNamespace
import argparse
import sys


def get_argument_parser_defaults(parser):
    return {
        action.dest: action.default
        for action in parser._actions
        if action.dest != "help"
    }


def get_args(parser, inargs, inkwargs):
    # Combines arguments in various formats.
    inarg_dict = {}
    for inarg in inargs:
        t = type(inarg)
        if t == list:  # ['-t', 'text']
            if inarg[0].endswith(".py"):
                inarg = inarg[1:]
            inarg_dict.update(**vars(parser.parse_args(inarg)))
        elif t == argparse.Namespace:  # already parsed by a parser.
            inarg_dict.update(**vars(inarg))
        elif t == types.SimpleNamespace:
            inarg_dict.update(**vars(inarg))
        elif t == dict:  # {'output_dir': '/rt'}
            inarg_dict.update(inarg)
    inarg_dict.update(inkwargs)
    arg_dict = get_argument_parser_defaults(parser)
    arg_dict.update(inarg_dict)
    args = SimpleNamespace(**arg_dict)
    return args


def install_module(module_name, version):
    cmd = ["oc", "module", "install", "--skip-installed", "-y"]
    if version is not None:
        cmd.extend(["-v", version])
    cmd.append(module_name)
    cmd = " ".join(cmd)
    shell("{cmd} {log}")


cravat_cmd_parser = argparse.ArgumentParser(
    prog="cravat input_file_path_1 input_file_path_2 ...",
    description="Open-CRAVAT genomic variant interpreter. https://github.com/KarchinLab/open-cravat. Use input_file_path arguments before any option or define them in a conf file (option -c).",
    epilog="inputs should be the first option",
)
cravat_cmd_parser.add_argument(
    "-a", nargs="+", dest="annotators", help="annotators to run"
)
cravat_cmd_parser.add_argument(
    "-e", nargs="+", dest="excludes", help="annotators to exclude"
)
cravat_cmd_parser.add_argument("-n", dest="run_name", help="name of cravat run")
cravat_cmd_parser.add_argument(
    "-d", dest="output_dir", default=None, help="directory for output files"
)
cravat_cmd_parser.add_argument(
    "--startat",
    dest="startat",
    choices=[
        "converter",
        "mapper",
        "annotator",
        "aggregator",
        "postaggregator",
        "reporter",
    ],
    default=None,
    help="starts at given stage",
)
cravat_cmd_parser.add_argument(
    "--endat",
    dest="endat",
    choices=[
        "converter",
        "mapper",
        "annotator",
        "aggregator",
        "postaggregator",
        "reporter",
    ],
    default=None,
    help="ends after given stage.",
)
cravat_cmd_parser.add_argument(
    "--skip",
    dest="skip",
    nargs="+",
    choices=[
        "converter",
        "mapper",
        "annotator",
        "aggregator",
        "postaggregator",
        "reporter",
    ],
    default=None,
    help="skips given stage(s).",
)
cravat_cmd_parser.add_argument(
    "-c", dest="conf", default=None, help="path to a conf file"
)
cravat_cmd_parser.add_argument(
    "--cs", dest="confs", default=None, help="configuration string"
)
cravat_cmd_parser.add_argument(
    "-v", dest="verbose", action="store_true", default=False, help="verbose"
)
cravat_cmd_parser.add_argument(
    "-t",
    nargs="+",
    dest="reports",
    choices=(),
    help="report types. If omitted, default one in cravat.yml is used.",
)
cravat_cmd_parser.add_argument(
    "-l",
    "--liftover",
    dest="genome",
    choices=["hg38", "hg19", "hg18"],
    default="hg38",
    help="reference genome of input. CRAVAT will lift over to hg38 if needed.",
)
cravat_cmd_parser.add_argument(
    "-x",
    dest="cleandb",
    action="store_true",
    help="deletes the existing result database and creates a new one.",
)
cravat_cmd_parser.add_argument(
    "--newlog",
    dest="newlog",
    action="store_true",
    default=None,
    help="deletes the existing log file and creates a new one.",
)
cravat_cmd_parser.add_argument(
    "--note",
    dest="note",
    default=None,
    help="note will be written to the run status file (.status.json)",
)
cravat_cmd_parser.add_argument(
    "--mp", dest="mp", default=None, help="number of processes to use to run annotators"
)
cravat_cmd_parser.add_argument(
    "-i",
    "--input-format",
    dest="forcedinputformat",
    default=None,
    help="Force input format",
)
cravat_cmd_parser.add_argument(
    "--temp-files",
    dest="temp_files",
    action="store_true",
    default=False,
    help="Leave temporary files after run is complete.",
)
cravat_cmd_parser.add_argument(
    "--writeadmindb",
    dest="writeadmindb",
    action="store_true",
    default=False,
    help="Write job information to admin db after job completion",
)
cravat_cmd_parser.add_argument(
    "--jobid", dest="jobid", default=None, help="Job ID for server version"
)
cravat_cmd_parser.add_argument(
    "--version",
    dest="show_version",
    action="store_true",
    default=False,
    help="Shows open-cravat version.",
)
cravat_cmd_parser.add_argument(
    "--separatesample",
    dest="separatesample",
    action="store_true",
    default=False,
    help="Separate variant results by sample",
)
cravat_cmd_parser.add_argument(
    "--unique-variants",
    dest="unique_variants",
    action="store_true",
    default=False,
    help=argparse.SUPPRESS,
)
cravat_cmd_parser.add_argument(
    "--primary-transcript",
    dest="primary_transcript",
    nargs="*",
    default=["mane"],
    help='"mane" for MANE transcripts as primary transcripts, or a path to a file of primary transcripts. MANE is default.',
)
cravat_cmd_parser.add_argument(
    "--cleanrun",
    dest="clean_run",
    action="store_true",
    default=False,
    help="Deletes all previous output files for the job and generate new ones.",
)
cravat_cmd_parser.add_argument(
    "--do-not-change-status",
    dest="do_not_change_status",
    action="store_true",
    default=False,
    help="Job status in status.json will not be changed",
)
cravat_cmd_parser.add_argument(
    "--module-option",
    dest="module_option",
    nargs="*",
    help="Module-specific option in module_name.key=value syntax. For example, --module-option vcfreporter.type=separate",
)
cravat_cmd_parser.add_argument(
    "--system-option",
    dest="system_option",
    nargs="*",
    help="System option in key=value syntax. For example, --system-option modules_dir=/home/user/open-cravat/modules",
)
cravat_cmd_parser.add_argument(
    "--silent", dest="silent", action="store_true", default=False, help="Runs silently."
)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
kwargs = {}
args = snakemake.params.get("args", "")
if args != "":
    parsed_args = get_args(cravat_cmd_parser, [args.split()], {})
    for k, v in parsed_args.__dict__.items():
        if v is not None and v != True and v != False:
            kwargs[k] = v
for k, v in snakemake.params.items():
    if k == "args":
        continue
    else:
        kwargs[k] = v
if "annotators" not in kwargs:
    print("No annotator was given. Exiting.")
    sys.exit()
if "reports" not in kwargs:
    print("No report type was given. Exiting.")
    sys.exit()

# Install modules
if kwargs["annotators"] is not None and len(kwargs["annotators"]) > 0:
    for i in range(len(kwargs["annotators"])):
        mv = kwargs["annotators"][i]
        if "=" in mv:
            module_name, version = mv.split("=")
            install_module_name = module_name
        else:
            module_name = mv
            install_module_name = module_name
            version = None
        install_module(install_module_name, version)
        kwargs["annotators"][i] = module_name
if kwargs["reports"] is not None and len(kwargs["reports"]) > 0:
    for i in range(len(kwargs["reports"])):
        mv = kwargs["reports"][i]
        if "=" in mv:
            module_name, version = mv.split("=")
            install_module_name = module_name + "reporter"
        else:
            module_name = mv
            install_module_name = module_name + "reporter"
            version = None
        install_module(install_module_name, version)
        kwargs["reports"][i] = module_name

# inputs
cmd = ["oc", "run"]
cmd.extend(list(snakemake.input))

# build arguments
actions = cravat_cmd_parser._action_groups[0]._actions
action_dests = [v.dest for v in actions]
for i in range(len(action_dests)):
    dest = action_dests[i]
    if dest in kwargs:
        action = actions[i]
        option_string = action.option_strings[0]
        cmd.append(option_string)
        option_value = kwargs[dest]
        if type(option_value) == list:
            cmd.extend(option_value)
        else:
            cmd.append(option_value)
cmd = " ".join(cmd)
shell("{cmd} {log}")
