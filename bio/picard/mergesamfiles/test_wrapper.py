import subprocess
import os

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))

def test():
    subprocess.check_call(["snakemake", "merged.bam", "--use-conda", "-F"])
