"""Snakemake wrapper for Dammit Annotation"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2019, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

# handle database params
db_dir = snakemake.params.get("database_dir")
db_dir = path.abspath(db_dir)
busco_dbs = snakemake.params.get("busco_dbs", [])
db_extra = snakemake.params.get(
    "db_extra", "--quick"
)  # default so db install is *just* to check installs have already happened

if db_dir:
    db_dir = path.expanduser(db_dir)
    db_cmd = " --database-dir " + db_dir  # if db_dir is not None else ""
else:
    db_cmd = ""

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

busco_dbs = [busco_dbs] if isinstance(busco_dbs, str) else busco_dbs
busco_cmd = (
    " --busco-group " + " --busco-group ".join(busco_dbs)
    if busco_dbs is not None
    else ""
)

# handle annotate params
outdir = path.dirname(snakemake.output[0])
annot_extra = snakemake.params.get("annot_extra", "")

# make informative output dir for *all* dammit output
assembly_name = path.basename(str(snakemake.input.fasta))
dammit_dir = path.join(outdir, assembly_name + ".dammit")
dammit_fasta = path.join(dammit_dir, assembly_name + ".dammit.fasta")
dammit_gff3 = path.join(dammit_dir, assembly_name + ".dammit.gff3")

## Note: databases can be installed using the databases wrapper standalone. In that case, these install cmds
# will just check that databases are properly installed. They will _not_ reinstall.

# databases breaks with multiple threads https://github.com/dib-lab/dammit/issues/140

# run installation of everything *except* busco groups
shell("dammit databases --install {db_cmd} {db_extra} {log}")

# busco groups need to be installed separately
for busco_grp in busco_dbs:
    shell(
        "dammit databases --install {db_cmd} --busco-group {busco_grp} {db_extra} {log}"
    )

# run annotation
shell(
    "dammit annotate {snakemake.input.fasta} {db_cmd} --no-rename --n_threads {snakemake.threads} --output-dir {dammit_dir} {annot_extra} {log}"
)

# cp final dammit annot files to desired location / names
shell("cp {dammit_fasta} {snakemake.output.fasta}")
shell("cp {dammit_gff3} {snakemake.output.gff3}")
