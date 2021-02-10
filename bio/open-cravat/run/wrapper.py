__author__ = "Rick Kim"
__copyright__ = "Copyright 2020, Rick Kim"
__license__ = "GPLv3"

from snakemake.shell import shell
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
inputfiles = []
annotators = []
reporters = []
modules_dir = set()
for v in snakemake.input:
    if os.path.isfile(v):
        inputfiles.append(v)
    elif os.path.isdir(v):
        (module_group_dir, module_name) = os.path.split(v)
        (in_modules_dir, module_group) = os.path.split(module_group_dir)
        modules_dir.add(in_modules_dir)
        if module_group == "annotators":
            annotators.append(module_name)
        elif module_group == "reporters" and module_name.endswith("reporter"):
            reporters.append(module_name[:-8])
if len(modules_dir) > 1:
    print(f'Multiple modules directory detected: {",".join(list(modules_dir))}')
    exit()
cmd = ["oc", "run"]
cmd.extend(inputfiles)
genome = snakemake.params.get("genome", "hg38")
mp = snakemake.threads
cmd.extend(["-l", genome])
cmd.extend(["--mp", str(mp)])
if len(annotators) > 0:
    cmd.append("-a")
    cmd.extend(annotators)
if len(reporters) > 0:
    cmd.append("-t")
    cmd.extend(reporters)
extra = snakemake.params.get("extra", "")
if len(extra) > 0 and type(extra) == str:
    cmd.extend(extra.split(" "))
shell("{cmd} {log}")
