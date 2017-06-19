import subprocess
import os

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))

def test_sort_none():
    subprocess.check_call(["snakemake", "mapped/a.bam", "--config",
                           "sort=none", "--use-conda", "-F"])

def test_sort_samtools():
    subprocess.check_call(["snakemake", "mapped/a.bam", "--config",
                           "sort=samtools", "--use-conda", "-F"])

def test_sort_picard():
    subprocess.check_call(["snakemake", "mapped/a.bam", "--config",
                           "sort=picard", "--use-conda", "-F"])
