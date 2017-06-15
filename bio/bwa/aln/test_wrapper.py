import subprocess
import os

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))

def test():
    subprocess.check_call(["snakemake", "sai/a.1.sai",
                           "sai/a.2.sai", "--use-conda", "-F"])
