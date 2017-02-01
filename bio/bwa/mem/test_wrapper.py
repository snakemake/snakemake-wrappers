import subprocess
import os

def setup_module():
    workdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test")
    os.chdir(workdir)

def test():
    subprocess.check_call(["snakemake", "mapped/a.bam", "--use-conda", "-F"])
