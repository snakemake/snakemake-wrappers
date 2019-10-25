"""Snakemake wrapper for Dammit Databases"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2019, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

# handle database params
db_dir = snakemake.params.get("db_dir")
db_dir = path.abspath(db_dir)
busco_dbs = snakemake.params.get("busco_dbs", [])
db_extra = snakemake.params.get("db_extra", "")
db_only = snakemake.params.get('db_install_only', False)

if db_dir:
    db_dir = path.expanduser(db_dir)
    db_cmd = ' --database-dir ' + db_dir
else:
    db_cmd = ""

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

busco_dbs = [busco_dbs] if isinstance(busco_dbs, str) else busco_dbs
busco_cmd = ' --busco-group ' + ' --busco-group '.join(busco_dbs) if busco_dbs is not None else ""

# databases breaks with multiple threads https://github.com/dib-lab/dammit/issues/140
# only a single busco group can be installed at once: https://github.com/dib-lab/dammit/issues/141

# run installation of everything *except* busco groups
shell("dammit databases --install {db_cmd} {db_extra} {log}") #--n_threads {snakemake.threads}

# busco groups need to be installed separately
for busco_grp in busco_dbs:
    shell("dammit databases --install {db_cmd} --busco-group {busco_grp} {db_extra} {log}")

