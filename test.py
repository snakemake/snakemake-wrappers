import subprocess
import os
import tempfile
import shutil

def run(wrapper, cmd):
    origdir = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "master", wrapper)
        os.makedirs(dst, exist_ok=True)
        copy = lambda src: shutil.copy(os.path.join(wrapper, src), dst)
        copy("wrapper.py")
        copy("environment.yaml")
        testdir = os.path.join(wrapper, "test")
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + ["--wrapper-prefix", "file://{}/".format(d)]
        subprocess.check_call(["snakemake", "--version"])
        try:
            subprocess.check_call(cmd)
        finally:
            os.chdir(origdir)
            for d, _, files in os.walk(os.path.join(testdir, "logs")):
                for f in files:
                    path = os.path.join(d, f)
                    with open(path) as f:
                        msg = "###### Logfile: " + path + " ######"
                        print(msg, "\n")
                        print(f.read())
                        print("#" * len(msg))


def test_bowtie2_align():
    run("bio/bowtie2/align",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_mem():
    run("bio/bwa/mem",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_mem_sort_samtools():
    run("bio/bwa/mem",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_samtools"])


def test_bwa_mem_sort_picard():
    run("bio/bwa/mem",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_picard"])


def test_bwa_aln():
    run("bio/bwa/aln",
        ["snakemake", "sai/a.1.sai", "sai/a.2.sai", "--use-conda", "-F"])

def test_bwa_index():
    run("bio/bwa/index",
        ["snakemake", "genome.amb", "genome.ann", "genome.bwt","genome.pac", "genome.sa", "--use-conda", "-F"])

def test_bwa_sampe():
    run("bio/bwa/sampe",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_sampe_sort_samtools():
    run("bio/bwa/sampe",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_samtools"])


def test_bwa_sampe_sort_picard():
    run("bio/bwa/sampe",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_picard"])


def test_bwa_samse():
    run("bio/bwa/samse",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_samse_sort_samtools():
    run("bio/bwa/samse",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_samtools"])


def test_bwa_samse_sort_picard():
    run("bio/bwa/samse",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F",
         "-s", "Snakefile_picard"])


def test_cutadapt_pe():
    run("bio/cutadapt/pe",
        ["snakemake", "trimmed/a.1.fastq", "--use-conda", "-F"])


def test_cutadapt_se():
    run("bio/cutadapt/se",
        ["snakemake", "trimmed/a.fastq", "--use-conda", "-F"])

# TODO epic is too slow for testing. Find a smaller example dataset.
#def test_epic_peaks():
#    run("bio/epic/peaks",
#        ["snakemake", "epic/enriched_regions.bed", "--use-conda", "-F"])


def test_fastqc():
    run("bio/fastqc",
        ["snakemake", "qc/a.html", "--use-conda", "-F"])


def test_freebayes():
    run("bio/freebayes",
        ["snakemake", "calls/a.vcf", "--use-conda", "-F"])


def test_freebayes_bcf():
    for c in [1, 2]:
        run("bio/freebayes",
            ["snakemake", "--cores", str(c), "calls/a.bcf", "--use-conda", "-F", "-s", "Snakefile_bcf"])


def test_multiqc():
    run("bio/multiqc",
        ["snakemake", "qc/multiqc.html", "--use-conda", "-F"])


def test_ngs_disambiguate():
    run("bio/ngs-disambiguate",
        ["snakemake", "disambiguate/s1.graft.ambiguous.bam",
         "--use-conda", "-F"])


def test_picard_collectalignmentsummarymetrics():
    run("bio/picard/collectalignmentsummarymetrics",
        ["snakemake", "stats/a.summary.txt", "--use-conda", "-F"])


def test_picard_collectinsertsizemetrics():
    run("bio/picard/collectinsertsizemetrics",
        ["snakemake", "stats/a.isize.txt", "--use-conda", "-F"])


def test_picard_collecthsmetrics():
    run("bio/picard/collecthsmetrics",
        ["snakemake", "stats/hs_metrics/a.txt", "--use-conda", "-F"])


def test_picard_mergesamfiles():
    run("bio/picard/mergesamfiles",
        ["snakemake", "merged.bam", "--use-conda", "-F"])


def test_picard_sortsam():
    run("bio/picard/sortsam",
        ["snakemake", "sorted/a.bam", "--use-conda", "-F"])


def test_pindel_call():
    run("bio/pindel/call",
        ["snakemake", "pindel/all_D", "--use-conda", "-F"])

def test_pindel_pindel2vcf():
    run("bio/pindel/pindel2vcf",
        ["snakemake", "pindel/all_D.vcf", "--use-conda", "-F"])

def test_samtools_stats():
    run("bio/samtools/stats",
        ["snakemake", "samtools_stats/a.txt", "--use-conda", "-F"])

def test_samtools_sort():
    run("bio/samtools/sort",
        ["snakemake", "mapped/a.sorted.bam", "--use-conda", "-F"])

def test_samtools_index():
    run("bio/samtools/index",
        ["snakemake", "mapped/a.sorted.bam.bai", "--use-conda", "-F"])

def test_samtools_merge():
    run("bio/samtools/merge",
        ["snakemake", "merged.bam", "--use-conda", "-F"])

def test_samtools_view():
    run("bio/samtools/view",
        ["snakemake", "a.bam", "--use-conda", "-F"])

def test_samtools_flagstat():
    run("bio/samtools/flagstat",
        ["snakemake", "mapped/a.bam.flagstat", "--use-conda", "-F"])

def test_star_align():
    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("bio/star/align/test/index", exist_ok=True)
    try:
        subprocess.check_call("conda env create "
                              "--file bio/star/align/environment.yaml "
                              "-p star-env",
                              shell=True,
                              executable="/bin/bash")
        subprocess.check_call("source activate star-env; STAR --genomeDir "
                              "bio/star/align/test/index "
                              "--genomeFastaFiles bio/star/align/test/genome.fasta "
                              "--runMode genomeGenerate",
                              shell=True,
                              executable="/bin/bash")
    finally:
        shutil.rmtree("star-env", ignore_errors=True)

    run("bio/star/align",
        ["snakemake", "star/a/Aligned.out.bam", "--use-conda", "-F"])


def test_trimmomatic_pe():
    run("bio/trimmomatic/pe",
        ["snakemake", "trimmed/a.1.fastq.gz", "--use-conda", "-F"])


def test_trimmomatic_se():
    run("bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq.gz", "--use-conda", "-F"])
