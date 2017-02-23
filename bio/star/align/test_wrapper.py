import subprocess
import os
import shutil

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))

    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("index", exist_ok=True)
    subprocess.check_call("conda env create --file ../environment.yaml -p star-env", shell=True)
    subprocess.check_call("source activate star; STAR --genomeDir index --genomeFastaFiles genome.fasta --runMode genomeGenerate", shell=True)
    shutil.rmtree(".star-env", ignore_errors=True)

def test():
    subprocess.check_call(["snakemake", "star/a/Aligned.out.bam", "--use-conda", "-F"])
