import subprocess
import os

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))
    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("index", exist_ok=True)
    subprocess.check_call(["STAR", "--genomeDir", "index", "--genomeFastaFiles", "genome.fasta", "--runMode", "genomeGenerate"])

def test():
    subprocess.check_call(["snakemake", "star/a/Aligned.out.bam", "--use-conda", "-F"])
