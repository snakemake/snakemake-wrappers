__author__ = "Rick Kim"
__copyright__ = "Copyright 2020, Rick Kim"
__license__ = "GPLv3"

from snakemake.shell import shell
import cravat
import re
import pathlib
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
onames = []
for o in snakemake.output:
    onames.append(o)
if type(onames) == str:
    onames = [onames]
elif type(onames) == list:
    onames = onames
else:
    onames = [str(onames)]
for oname in onames:
    if os.path.exists(oname):
        continue
    [o2, module_name] = os.path.split(oname)
    [modules_dir, module_type] = os.path.split(o2)
    module_type = module_type[:-1]
    modules_dir_cur = cravat.admin_util.get_modules_dir()
    if modules_dir_cur != modules_dir:
        cravat.admin_util.set_modules_dir(modules_dir)
    cmd = ["oc", "module", "install", module_name, "-y"]
    cmd = " ".join(cmd)
    shell("{cmd} {log}")
