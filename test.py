import subprocess
import os
import tempfile
import shutil
import pytest

def run(wrapper, cmd, check_log=None):
    origdir = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "master", wrapper)
        os.makedirs(dst, exist_ok=True)
        copy = lambda src: shutil.copy(os.path.join(wrapper, src), dst)
        success = False
        for ext in ("py", "R", "Rmd"):
            script = "wrapper." + ext
            if os.path.exists(os.path.join(wrapper, script)):
                copy(script)
                success = True
                break
        assert success, "No wrapper.{py,R,Rmd} found"
        copy("environment.yaml")
        testdir = os.path.join(wrapper, "test")
        # switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + ["--wrapper-prefix", "file://{}/".format(d)]
        subprocess.check_call(["snakemake", "--version"])

        try:
            subprocess.check_call(cmd)
        except Exception as e:
            # go back to original directory
            os.chdir(origdir)
            logfiles = [os.path.join(d, f)
                for d, _, files in os.walk(os.path.join(testdir, "logs"))
                for f in files]
            for path in logfiles:
                with open(path) as f:
                    msg = "###### Logfile: " + path + " ######"
                    print(msg, "\n")
                    print(f.read())
                    print("#" * len(msg))
            if check_log is not None:
                for f in logfiles:
                    check_log(open(f).read())
            else:
                raise e
        finally:
            # go back to original directory
            os.chdir(origdir)


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

def test_epic_peaks():
    run("bio/epic/peaks",
        ["snakemake", "epic/enriched_regions.bed", "--use-conda", "-F"])


def test_fastqc():
    run("bio/fastqc",
        ["snakemake", "qc/fastqc/a.html", "--use-conda", "-F"])


def test_freebayes():
    run("bio/freebayes",
        ["snakemake", "calls/a.vcf", "--use-conda", "-F"])


def test_freebayes_bcf():
    for c in [1, 2]:
        run("bio/freebayes",
            ["snakemake", "--cores", str(c), "calls/a.bcf", "--use-conda", "-F", "-s", "Snakefile_bcf"])

def test_minimap2_aligner():
    run("bio/minimap2/aligner",
        ["snakemake", "aligned/genome_aln.paf", "--use-conda", "-F"])

def test_minimap2_index():
    run("bio/minimap2/index",
        ["snakemake", "genome.mmi", "--use-conda", "-F"])

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

def test_picard_createsequencedictionary():
    run("bio/picard/createsequencedictionary",
        ["snakemake", "genome.dict", "--use-conda", "-F"])

def test_pindel_call():
    run("bio/pindel/call",
        ["snakemake", "pindel/all_D", "--use-conda", "-F"])

def test_pindel_pindel2vcf():
    run("bio/pindel/pindel2vcf",
        ["snakemake", "pindel/all_D.vcf", "--use-conda", "-F"])

def test_pindel_pindel2vcf_multi_input():
    run("bio/pindel/pindel2vcf",
        ["snakemake", "pindel/all.vcf", "--use-conda", "-F"])

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

def test_bcftools_concat():
    run("bio/bcftools/concat",
        ["snakemake", "all.bcf", "--use-conda", "-F"])

def test_bcftools_merge():
    run("bio/bcftools/merge",
        ["snakemake", "all.bcf", "--use-conda", "-F"])

def test_star_align():
    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("bio/star/align/test/index", exist_ok=True)
    try:
        subprocess.check_call("conda env create "
                              "--file bio/star/align/environment.yaml "
                              "-n star-env",
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
    run("bio/star/align",
        ["snakemake", "star/pe/a/Aligned.out.bam", "--use-conda", "-F"])

def test_snpeff():
    run("bio/snpeff",
        ["snakemake", "snpeff/fake_KJ660346.vcf", "--use-conda", "-F"])

def test_snpeff_nostats():
    run("bio/snpeff",
        ["snakemake", "snpeff_nostats/fake_KJ660346.vcf", "--use-conda", "-F", "-s", "Snakefile_nostats"])

def test_trim_galore_pe():
    run("bio/trim_galore/pe",
        ["snakemake", "trimmed/a.1_val_1.fq.gz", "--use-conda", "-F"])

def test_trim_galore_se():
    run("bio/trim_galore/se",
        ["snakemake", "trimmed/a_trimmed.fq.gz", "--use-conda", "-F"])

def test_trimmomatic_pe():
    """Four tests, one per fq-gz combination"""
    run("bio/trimmomatic/pe",
        ["snakemake", "trimmed/a.1.fastq", "--use-conda", "-F",
        "-s", "Snakefile_fq_fq"])
    run("bio/trimmomatic/pe",
        ["snakemake", "trimmed/a.1.fastq.gz", "--use-conda", "-F",
        "-s", "Snakefile_fq_gz"])
    run("bio/trimmomatic/pe",
        ["snakemake", "trimmed/a.1.fastq", "--use-conda", "-F",
        "-s", "Snakefile_gz_fq"])
    run("bio/trimmomatic/pe",
        ["snakemake", "trimmed/a.1.fastq.gz", "--use-conda", "-F",
        "-s", "Snakefile_gz_gz"])

def test_trimmomatic_se():
    """Four tests, one per fq-gz combination"""
    run("bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq", "--use-conda", "-F",
        "-s", "Snakefile_fq_fq"])
    run("bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq.gz", "--use-conda", "-F",
        "-s", "Snakefile_fq_gz"])
    run("bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq", "--use-conda", "-F",
        "-s", "Snakefile_gz_fq"])
    run("bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq.gz", "--use-conda", "-F",
        "-s", "Snakefile_gz_gz"])

@pytest.mark.skip(reason="known fail")
def test_rubic():
    run("bio/rubic",
        ["snakemake", "BRCA/gains.txt", "--use-conda", "-F"])

def test_delly():
    run("bio/delly", ["snakemake", "sv/calls.bcf", "--use-conda", "-F"])

def test_jannovar():
    run("bio/jannovar", ["snakemake", "jannovar/pedigree_vars.vcf.gz", "--use-conda", "-F"])

def test_cairosvg():
    run("utils/cairosvg", ["snakemake", "pca.pdf", "--use-conda", "-F"])

def test_trinity():
    run("bio/trinity",
        ["snakemake", "trinity_out_dir/Trinity.fasta", "--use-conda", "-F"])

@pytest.mark.skip(reason="known fail")
def test_salmon_index():
    run("bio/salmon/index",
        ["snakemake", "salmon/transcriptome_index", "--use-conda", "-F"])

def test_salmon_quant():
    run("bio/salmon/quant",
        ["snakemake", "salmon/a/quant.sf",
        "--use-conda", "-F", "-s", "Snakefile"])

    run("bio/salmon/quant",
        ["snakemake", "salmon/a_se_x_transcriptome/quant.sf",
        "--use-conda", "-F","-s", "Snakefile_se"])

    run("bio/salmon/quant",
        ["snakemake", "salmon/ab_pe_x_transcriptome/quant.sf",
        "--use-conda", "-F", "-s", "Snakefile_pe_multi"])

def test_sourmash_compute():
    run("bio/sourmash/compute/",
        ["snakemake","transcriptome.sig",
         "--use-conda","-F","-s","Snakefile"])
    run("bio/sourmash/compute/",
        ["snakemake","reads.sig",
         "--use-conda","-F","-s","Snakefile"])

@pytest.mark.skip(reason="test hangs, skipping so we can see gatk test results")
def test_busco():
    run("bio/busco",
        ["snakemake", "txome_busco/full_table_txome_busco.tsv",
        "--use-conda", "-F"])

def test_vcftoolsfilter():
    run("bio/vcftools/filter", ["snakemake", "sample.filtered.vcf", "--use-conda", "-F"])

def test_gatk_baserecalibrator():
    run("bio/gatk/baserecalibrator", ["snakemake", "recal/a.bam", "--use-conda", "-F"])

def test_gatk_haplotypecaller():
    run("bio/gatk/haplotypecaller", ["snakemake", "calls/a.g.vcf", "--use-conda", "-F"])

def test_gatk_variantrecalibrator():
    def check_log(log):
        assert "USAGE" not in log

    run("bio/gatk/variantrecalibrator",
        ["snakemake", "-s", "test.smk", "calls/all.recal.vcf", "--use-conda", "-F"],
        check_log=check_log)

def test_gatk_selectvariants():
    run("bio/gatk/selectvariants", ["snakemake", "calls/snvs.vcf", "--use-conda", "-F"])

def test_gatk_variantfiltration():
    run("bio/gatk/variantfiltration", ["snakemake", "calls/snvs.filtered.vcf", "--use-conda", "-F"])

def test_gatk_genotypegvcfs():
    run("bio/gatk/genotypegvcfs", ["snakemake", "calls/all.vcf", "--use-conda", "-F"])

# this GATK tool does not work with our test data so far... Error is unclear.
#def test_gatk_genomicsdbimport():
#    run("bio/gatk/genomicsdbimport", ["snakemake", "genomicsdb/ref", "--use-conda", "-F"])

def test_gatk_combinegvcfs():
    run("bio/gatk/combinegvcfs", ["snakemake", "calls/all.g.vcf", "--use-conda", "-F"])


def test_picard_mergevcfs():
    run("bio/picard/mergevcfs", ["snakemake", "snvs.vcf", "--use-conda", "-F"])
