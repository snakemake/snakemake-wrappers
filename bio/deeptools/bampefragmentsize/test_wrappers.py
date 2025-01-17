import subprocess

def run(command, args):
    subprocess.run([command] + args, check=True)

def test_bampe_fragmentsize():
    run(
        "bio/deeptools/bampefragmentsize",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.bam", "b.bam"],
    )
