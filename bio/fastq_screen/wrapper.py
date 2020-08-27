import os
import re
import tempfile

__author__ = "Ryan Dale"
__copyright__ = "Copyright 2016, Ryan Dale"
__email__ = "dalerr@niddk.nih.gov"
__license__ = "MIT"

_config = snakemake.params["fastq_screen_config"]

subset = snakemake.params.get("subset", 100000)
aligner = snakemake.params.get("aligner", "bowtie2")
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

# snakemake.params.fastq_screen_config can be either a dict or a string. If
# string, interpret as a filename pointing to the fastq_screen config file.
# Otherwise, create a new tempfile out of the contents of the dict:
if isinstance(_config, dict):
    tmp = tempfile.NamedTemporaryFile(delete=False).name
    with open(tmp, "w") as fout:
        for label, indexes in _config["database"].items():
            for aligner, index in indexes.items():
                fout.write(
                    "\t".join(["DATABASE", label, index, aligner.upper()]) + "\n"
                )
        for aligner, path in _config["aligner_paths"].items():
            fout.write("\t".join([aligner.upper(), path]) + "\n")
    config_file = tmp
else:
    config_file = _config

# fastq_screen hard-codes filenames according to this prefix. We will send
# hard-coded output to a temp dir, and then move them later.
prefix = re.split(".fastq|.fq|.txt|.seq", os.path.basename(snakemake.input[0]))[0]

tempdir = tempfile.mkdtemp()

os.system(
    "fastq_screen --outdir %s "
    "--force "
    "--aligner %s "
    "--conf %s "
    "--subset %s "
    "--threads %s "
    "%s "
    "%s "
    "%s"
    % (
        tempdir,
        aligner,
        config_file,
        subset,
        snakemake.threads,
        extra,
        snakemake.input[0],
        log,
    )
)


# Move output to the filenames specified by the rule
os.system("mv %s/%s_screen.txt %s" % (tempdir, prefix, snakemake.output.txt))
os.system("mv %s/%s_screen.png %s" % (tempdir, prefix, snakemake.output.png))

# Clean up temp
os.system("rm -r %s" % tempdir)
if isinstance(_config, dict):
    os.system("rm %s" % tmp)
