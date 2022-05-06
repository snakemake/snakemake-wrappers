__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os
from tempfile import TemporaryDirectory
from shutil import copyfile

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
svd_mu = snakemake.input.get("svd_mu", "")
if svd_mu:
    svd_prefix = os.path.splitext(svd_mu)[0]
    for suffix in ("bed", "UD", "V"):
        fn = f"{svd_prefix}.{suffix}"
        if not os.path.isfile(fn):
            raise Exception(f"Failed to find required input {fn}.")
else:
    genome_build = snakemake.params.get("genome_build", "38")
    if genome_build not in ("37", "38"):
        raise Exception(
            f"No svd_prefix given and improper {genome_build=} "
            f"given.  Valid choices are 37,38."
        )
    verifybamid2_found = False
    for path in os.getenv("PATH").split(os.path.pathsep):
        path_to_verifybamid2 = os.path.join(path, "verifybamid2")
        if os.path.isfile(path_to_verifybamid2):
            verifybamid2_found = True
            resources_directory = os.path.join(
                os.path.dirname(os.path.realpath(path_to_verifybamid2)), "resource"
            )
            svd_prefix = os.path.join(
                resources_directory, f"1000g.phase3.100k.b{genome_build}.vcf.gz.dat"
            )
            break
    if not verifybamid2_found:
        raise Exception("Failed to find verifybamid2 location.")


def move_file(src, dst):
    "this function will move `fn` while respecting ACLs in the target directory"
    copyfile(src, dst)
    os.remove(src)


# verifybamid2 outputs results to result.selfSM and result.Ancestry in the working directory,
# so to avoid collisions we have to run it from a temporary directory and fix the paths
# to inputs, outputs, and the log file
ref_path = os.path.abspath(snakemake.input.ref)
svd_prefix = os.path.abspath(svd_prefix)
bam_path = os.path.abspath(snakemake.input.bam)
selfsm_path = os.path.abspath(snakemake.output.selfsm)
ancestry_path = os.path.abspath(snakemake.output.ancestry)
if snakemake.log:
    snakemake.log[0] = os.path.abspath(snakemake.log[0])
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
with TemporaryDirectory() as tmp_dir:
    os.chdir(tmp_dir)
    shell(
        "verifybamid2 --SVDPrefix {svd_prefix} "
        "--Reference {ref_path} --BamFile {bam_path} {extra} "
        "--NumThread {snakemake.threads} {log}"
    )
    move_file("result.selfSM", selfsm_path)
    move_file("result.Ancestry", ancestry_path)
