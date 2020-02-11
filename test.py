import subprocess
import os
import tempfile
import shutil
import pytest
import sys

DIFF_ONLY = os.environ.get("DIFF_ONLY", "false") == "true"

if DIFF_ONLY:
    # check if wrapper is modified compared to master
    DIFF_FILES = set(
        subprocess.check_output(["git", "diff", "origin/master", "--name-only"])
        .decode()
        .split("\n")
    )


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

        if DIFF_ONLY and not any(f.startswith(wrapper) for f in DIFF_FILES):
            print(
                "Skipping wrapper {} (not modified).".format(wrapper), file=sys.stderr
            )
            return

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
            logfiles = [
                os.path.join(d, f)
                for d, _, files in os.walk(os.path.join(testdir, "logs"))
                for f in files
            ]
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


def test_arriba():
    run(
        "bio/arriba",
        ["snakemake", "fusions/A.tsv", "fusions/A.discarded.tsv", "--use-conda", "-F"],
    )


def test_art_profiler_illumina():
    run(
        "bio/art/profiler_illumina",
        ["snakemake", "profiles/a.1.txt", "profiles/a.2.txt", "--use-conda", "-F"],
    )


def test_bcftools_index():
    run("bio/bcftools/index", ["snakemake", "a.bcf.csi", "--use-conda", "-F"])


def test_bcftools_concat():
    run("bio/bcftools/concat", ["snakemake", "all.bcf", "--use-conda", "-F"])


def test_bcftools_merge():
    run("bio/bcftools/merge", ["snakemake", "all.bcf", "--use-conda", "-F"])


def test_bcftools_reheader():
    run("bio/bcftools/reheader", ["snakemake", "a.reheader.bcf", "--use-conda", "-F"])


def test_bedtools_intersect():
    run(
        "bio/bedtools/intersect",
        ["snakemake", "A_B.intersected.bed", "--use-conda", "-F"],
    )


def test_bedtools_merge():
    run("bio/bedtools/merge", ["snakemake", "A.merged.bed", "--use-conda", "-F"])


def test_bedtools_slop():
    run("bio/bedtools/slop", ["snakemake", "A.slop.bed", "--use-conda", "-F"])


def test_bowtie2_align():
    run("bio/bowtie2/align", ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_mem():
    run("bio/bwa/mem", ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_mem_sort_samtools():
    run(
        "bio/bwa/mem",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_samtools"],
    )


def test_bwa_mem_sort_picard():
    run(
        "bio/bwa/mem",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_picard"],
    )


def test_bwa_aln():
    run("bio/bwa/aln", ["snakemake", "sai/a.1.sai", "sai/a.2.sai", "--use-conda", "-F"])


def test_bwa_index():
    run(
        "bio/bwa/index",
        [
            "snakemake",
            "genome.amb",
            "genome.ann",
            "genome.bwt",
            "genome.pac",
            "genome.sa",
            "--use-conda",
            "-F",
        ],
    )


def test_bwa_sampe():
    run("bio/bwa/sampe", ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_sampe_sort_samtools():
    run(
        "bio/bwa/sampe",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_samtools"],
    )


def test_bwa_sampe_sort_picard():
    run(
        "bio/bwa/sampe",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_picard"],
    )


def test_bwa_samse():
    run("bio/bwa/samse", ["snakemake", "mapped/a.bam", "--use-conda", "-F"])


def test_bwa_samse_sort_samtools():
    run(
        "bio/bwa/samse",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_samtools"],
    )


def test_bwa_samse_sort_picard():
    run(
        "bio/bwa/samse",
        ["snakemake", "mapped/a.bam", "--use-conda", "-F", "-s", "Snakefile_picard"],
    )


def test_clustalo():
    run("bio/clustalo", ["snakemake", "test.msa.fa", "--use-conda", "-F"])


def test_cutadapt_pe():
    run("bio/cutadapt/pe", ["snakemake", "trimmed/a.1.fastq", "--use-conda", "-F"])


def test_cutadapt_se():
    run("bio/cutadapt/se", ["snakemake", "trimmed/a.fastq", "--use-conda", "-F"])


def test_epic_peaks():
    run(
        "bio/epic/peaks",
        ["snakemake", "epic/enriched_regions.bed", "--use-conda", "-F"],
    )


def test_fastp_pe():
    run(
        "bio/fastp",
        [
            "snakemake",
            "trimmed/pe/a.1.fastq",
            "trimmed/pe/a.2.fastq",
            "report/pe/a.html",
            "report/pe/a.json",
            "--use-conda",
            "-F",
        ],
    )


def test_fastp_pe_wo_trimming():
    run(
        "bio/fastp",
        [
            "snakemake",
            "report/pe_wo_trimming/a.html",
            "report/pe_wo_trimming/a.json",
            "--use-conda",
            "-F",
        ],
    )


def test_fastp_se():
    run(
        "bio/fastp",
        [
            "snakemake",
            "trimmed/se/a.fastq",
            "report/se/a.html",
            "report/se/a.json",
            "--use-conda",
            "-F",
        ],
    )


def test_fastqc():
    run("bio/fastqc", ["snakemake", "qc/fastqc/a.html", "--use-conda", "-F"])


def test_fgbio_annotate():
    run(
        "bio/fgbio/annotatebamwithumis",
        ["snakemake", "mapped/a.annotated.bam", "--use-conda", "-F"],
    )


def test_fgbio_collectduplexseqmetrics():
    run(
        "bio/fgbio/collectduplexseqmetrics",
        [
            "snakemake",
            "stats/a.family_sizes.txt",
            "stats/a.duplex_family_sizes.txt",
            "stats/a.duplex_yield_metrics.txt",
            "stats/a.umi_counts.txt",
            "stats/a.duplex_qc.pdf",
            "stats/a.duplex_umi_counts.txt",
            "--use-conda",
            "-F",
        ],
    )


def test_fgbio_filterconsensusreads():
    run(
        "bio/fgbio/filterconsensusreads",
        ["snakemake", "mapped/a.filtered.bam", "--use-conda", "-F"],
    )


def test_fgbio_group():
    run(
        "bio/fgbio/groupreadsbyumi",
        ["snakemake", "mapped/a.gu.bam", "mapped/a.gu.histo.tsv", "--use-conda", "-F"],
    )


def test_fgbio_set_mate_information():
    run(
        "bio/fgbio/setmateinformation",
        ["snakemake", "mapped/a.mi.bam", "--use-conda", "-F"],
    )


def test_fgbio_call_molecular_consensus_reads():
    run(
        "bio/fgbio/callmolecularconsensusreads",
        ["snakemake", "mapped/a.m3.bam", "--use-conda", "-F"],
    )


def test_filtlong():
    run("bio/filtlong", ["snakemake", "reads.filtered.fastq", "--use-conda", "-F"])


def test_freebayes():
    run("bio/freebayes", ["snakemake", "calls/a.vcf", "--use-conda", "-F"])


def test_freebayes_bcf():
    for c in [1, 2]:
        run(
            "bio/freebayes",
            [
                "snakemake",
                "--cores",
                str(c),
                "calls/a.bcf",
                "--use-conda",
                "-F",
                "-s",
                "Snakefile_bcf",
            ],
        )


def test_happy_prepy():
    run(
        "bio/hap.py/pre.py",
        ["snakemake", "normalized/variants.vcf", "--use-conda", "-F"],
    )


def test_happy_prepy():
    run(
        "bio/hap.py/pre.py",
        ["snakemake", "normalized/variants.vcf", "--use-conda", "-F"],
    )


def test_hisat2_index():
    run("bio/hisat2/index", ["snakemake", "index_genome", "--use-conda", "-F"])


def test_hisat2_align():
    run("bio/hisat2/align", ["snakemake", "mapped/A.bam", "--use-conda", "-F"])


def test_kallisto_index():
    run("bio/kallisto/index", ["snakemake", "transcriptome.idx", "--use-conda", "-F"])


def test_kallisto_quant():
    run("bio/kallisto/quant", ["snakemake", "quant_results_A", "--use-conda", "-F"])


def test_lofreq_call():
    run("bio/lofreq/call", ["snakemake", "calls/a.vcf", "--use-conda", "-F"])


def test_minimap2_aligner():
    run(
        "bio/minimap2/aligner",
        ["snakemake", "aligned/genome_aln.paf", "--use-conda", "-F"],
    )


def test_minimap2_index():
    run("bio/minimap2/index", ["snakemake", "genome.mmi", "--use-conda", "-F"])


def test_multiqc():
    run("bio/multiqc", ["snakemake", "qc/multiqc.html", "--use-conda", "-F"])


def test_nanosimh():
    run(
        "bio/nanosim-h",
        [
            "snakemake",
            "test.simulated.fa",
            "test.simulated.log",
            "test.simulated.errors.txt",
            "--use-conda",
            "-F",
        ],
    )


def test_ngs_disambiguate():
    run(
        "bio/ngs-disambiguate",
        ["snakemake", "disambiguate/s1.graft.ambiguous.bam", "--use-conda", "-F"],
    )


def test_picard_collectalignmentsummarymetrics():
    run(
        "bio/picard/collectalignmentsummarymetrics",
        ["snakemake", "stats/a.summary.txt", "--use-conda", "-F"],
    )


def test_picard_collectinsertsizemetrics():
    run(
        "bio/picard/collectinsertsizemetrics",
        ["snakemake", "stats/a.isize.txt", "--use-conda", "-F"],
    )


def test_picard_collecthsmetrics():
    run(
        "bio/picard/collecthsmetrics",
        ["snakemake", "stats/hs_metrics/a.txt", "--use-conda", "-F"],
    )


def test_picard_mergesamfiles():
    run("bio/picard/mergesamfiles", ["snakemake", "merged.bam", "--use-conda", "-F"])


def test_picard_bam_to_fastq():
    run(
        "bio/picard/samtofastq",
        ["snakemake", "reads/a.R1.fastq", "reads/a.R2.fastq", "--use-conda", "-F"],
    )


def test_picard_sortsam():
    run("bio/picard/sortsam", ["snakemake", "sorted/a.bam", "--use-conda", "-F"])


def test_picard_revertsam():
    run("bio/picard/revertsam", ["snakemake", "revert/a.bam", "--use-conda", "-F"])


def test_picard_createsequencedictionary():
    run(
        "bio/picard/createsequencedictionary",
        ["snakemake", "genome.dict", "--use-conda", "-F"],
    )


def test_pindel_call():
    run("bio/pindel/call", ["snakemake", "pindel/all_D", "--use-conda", "-F"])


def test_pindel_pindel2vcf():
    run("bio/pindel/pindel2vcf", ["snakemake", "pindel/all_D.vcf", "--use-conda", "-F"])


def test_pindel_pindel2vcf_multi_input():
    run("bio/pindel/pindel2vcf", ["snakemake", "pindel/all.vcf", "--use-conda", "-F"])


def test_samtools_fixmate():
    run("bio/samtools/fixmate", ["snakemake", "fixed/a.bam", "--use-conda", "-F"])


def test_pyfastaq_replace_bases():
    run(
        "bio/pyfastaq/replace_bases",
        ["snakemake", "sample1.dna.fa", "--use-conda", "-F"],
    )


def test_samtools_mpileup():
    run(
        "bio/samtools/mpileup",
        ["snakemake", "mpileup/a.mpileup.gz", "--use-conda", "-F"],
    )


def test_samtools_stats():
    run(
        "bio/samtools/stats", ["snakemake", "samtools_stats/a.txt", "--use-conda", "-F"]
    )


def test_samtools_sort():
    run("bio/samtools/sort", ["snakemake", "mapped/a.sorted.bam", "--use-conda", "-F"])


def test_samtools_index():
    run(
        "bio/samtools/index",
        ["snakemake", "mapped/a.sorted.bam.bai", "--use-conda", "-F"],
    )


def test_samtools_merge():
    run("bio/samtools/merge", ["snakemake", "merged.bam", "--use-conda", "-F"])


def test_samtools_view():
    run("bio/samtools/view", ["snakemake", "a.bam", "--use-conda", "-F"])


def test_samtools_flagstat():
    run(
        "bio/samtools/flagstat",
        ["snakemake", "mapped/a.bam.flagstat", "--use-conda", "-F"],
    )


def test_samtools_bam2fq_interleaved():
    run(
        "bio/samtools/bam2fq/interleaved",
        ["snakemake", "reads/a.fq", "--use-conda", "-F"],
    )


def test_samtools_bam2fq_separate():
    run(
        "bio/samtools/bam2fq/separate",
        ["snakemake", "reads/a.1.fq", "--use-conda", "-F"],
    )


def test_samtools_faidx():
    run("bio/samtools/faidx", ["snakemake", "genome.fa.fai", "--use-conda", "-F"])


def test_snpmutator():
    run(
        "bio/snp-mutator",
        [
            "snakemake",
            "test_mutated_1.fasta",
            "test_mutated_2.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_star_align():
    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("bio/star/align/test/index", exist_ok=True)
    try:
        subprocess.check_call(
            "conda env create " "--file bio/star/align/environment.yaml " "-n star-env",
            shell=True,
            executable="/bin/bash",
        )
        subprocess.check_call(
            "source activate star-env; STAR --genomeDir "
            "bio/star/align/test/index "
            "--genomeFastaFiles bio/star/align/test/genome.fasta "
            "--runMode genomeGenerate "
            "--genomeSAindexNbases 8",
            shell=True,
            executable="/bin/bash",
        )
    finally:
        shutil.rmtree("star-env", ignore_errors=True)

    run("bio/star/align", ["snakemake", "star/a/Aligned.out.sam", "--use-conda", "-F"])
    run(
        "bio/star/align",
        ["snakemake", "star/pe/a/Aligned.out.sam", "--use-conda", "-F"],
    )


def test_star_index():
    run("bio/star/index", ["snakemake", "genome", "--use-conda", "-F"])


def test_snpeff():
    run("bio/snpeff", ["snakemake", "snpeff/fake_KJ660346.vcf", "--use-conda", "-F"])


def test_snpeff_nostats():
    run(
        "bio/snpeff",
        [
            "snakemake",
            "snpeff_nostats/fake_KJ660346.vcf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_nostats",
        ],
    )


def test_strelka_germline():
    run("bio/strelka/germline", ["snakemake", "strelka/a", "--use-conda", "-F"])


def test_trim_galore_pe():
    run(
        "bio/trim_galore/pe",
        ["snakemake", "trimmed/a.1_val_1.fq.gz", "--use-conda", "-F"],
    )


def test_trim_galore_se():
    run(
        "bio/trim_galore/se",
        ["snakemake", "trimmed/a_trimmed.fq.gz", "--use-conda", "-F"],
    )


def test_trimmomatic_pe():
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "trimmed/a.1.fastq",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_fq_fq",
        ],
    )
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "trimmed/a.1.fastq.gz",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_fq_gz",
        ],
    )
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "trimmed/a.1.fastq",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_gz_fq",
        ],
    )
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "trimmed/a.1.fastq.gz",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_gz_gz",
        ],
    )
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "trimmed/a.1.fastq.gz",
            "--use-conda",
            "-F",
            "--cores",
            "32",
            "-s",
            "Snakefile_gz_gz",
        ],
    )


def test_trimmomatic_se():
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq", "--use-conda", "-F", "-s", "Snakefile_fq_fq"],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "trimmed/a.fastq.gz",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_fq_gz",
        ],
    )
    run(
        "bio/trimmomatic/se",
        ["snakemake", "trimmed/a.fastq", "--use-conda", "-F", "-s", "Snakefile_gz_fq"],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "trimmed/a.fastq.gz",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_gz_gz",
        ],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "trimmed/a.fastq.gz",
            "--use-conda",
            "-F",
            "--cores",
            "32",
            "-s",
            "Snakefile_gz_gz",
        ],
    )


def test_rubic():
    run("bio/rubic", ["snakemake", "BRCA/gains.txt", "--use-conda", "-F"])


def test_delly():
    run("bio/delly", ["snakemake", "sv/calls.bcf", "--use-conda", "-F"])


def test_jannovar():
    env_file = "bio/jannovar/environment.yaml"
    env = ".envs/jannovar"
    subprocess.run(
        f"conda env create -f {env_file} --prefix {env}", shell=True, executable="bash"
    )
    subprocess.run(
        f"source activate {env}; jannovar download -d hg19/ucsc",
        shell=True,
        executable="bash",
    )
    shutil.move("data/hg19_ucsc.ser", "bio/jannovar/test")
    run(
        "bio/jannovar",
        ["snakemake", "jannovar/pedigree_vars.vcf.gz", "--use-conda", "-F"],
    )


def test_cairosvg():
    run("utils/cairosvg", ["snakemake", "pca.pdf", "--use-conda", "-F"])


def test_trinity():
    run(
        "bio/trinity",
        ["snakemake", "trinity_out_dir/Trinity.fasta", "--use-conda", "-F"],
    )


def test_salmon_index():
    run(
        "bio/salmon/index",
        ["snakemake", "salmon/transcriptome_index", "--use-conda", "-F"],
    )


def test_salmon_quant():
    run(
        "bio/salmon/quant",
        ["snakemake", "salmon/a/quant.sf", "--use-conda", "-F", "-s", "Snakefile"],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/a_se_x_transcriptome/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_se",
        ],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/ab_pe_x_transcriptome/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_pe_multi",
        ],
    )


def test_sourmash_compute():
    run(
        "bio/sourmash/compute/",
        ["snakemake", "transcriptome.sig", "--use-conda", "-F", "-s", "Snakefile"],
    )
    run(
        "bio/sourmash/compute/",
        ["snakemake", "reads.sig", "--use-conda", "-F", "-s", "Snakefile"],
    )


@pytest.mark.skip(reason="test hangs, skipping so we can see gatk test results")
def test_busco():
    run(
        "bio/busco",
        ["snakemake", "txome_busco/full_table_txome_busco.tsv", "--use-conda", "-F"],
    )


def test_vcftoolsfilter():
    run(
        "bio/vcftools/filter", ["snakemake", "sample.filtered.vcf", "--use-conda", "-F"]
    )


def test_gatk_baserecalibrator():
    run("bio/gatk/baserecalibrator", ["snakemake", "recal/a.bam", "--use-conda", "-F"])


def test_gatk_haplotypecaller():
    run("bio/gatk/haplotypecaller", ["snakemake", "calls/a.g.vcf", "--use-conda", "-F"])


def test_gatk_variantrecalibrator():
    def check_log(log):
        assert "USAGE" not in log

    run(
        "bio/gatk/variantrecalibrator",
        ["snakemake", "-s", "test.smk", "calls/all.recal.vcf", "--use-conda", "-F"],
        check_log=check_log,
    )


def test_gatk_selectvariants():
    run("bio/gatk/selectvariants", ["snakemake", "calls/snvs.vcf", "--use-conda", "-F"])


def test_gatk_variantfiltration():
    run(
        "bio/gatk/variantfiltration",
        ["snakemake", "calls/snvs.filtered.vcf", "--use-conda", "-F"],
    )


def test_gatk_genotypegvcfs():
    run("bio/gatk/genotypegvcfs", ["snakemake", "calls/all.vcf", "--use-conda", "-F"])


# this GATK tool does not work with our test data so far... Error is unclear.
# def test_gatk_genomicsdbimport():
#    run("bio/gatk/genomicsdbimport", ["snakemake", "genomicsdb/ref", "--use-conda", "-F"])


def test_gatk_combinegvcfs():
    run("bio/gatk/combinegvcfs", ["snakemake", "calls/all.g.vcf", "--use-conda", "-F"])


def test_gatk_splitncigarreads():
    run("bio/gatk/splitncigarreads", ["snakemake", "split/a.bam", "--use-conda", "-F"])


def test_picard_mergevcfs():
    run("bio/picard/mergevcfs", ["snakemake", "snvs.vcf", "--use-conda", "-F"])


def test_igv_reports():
    run("bio/igv-reports", ["snakemake", "igv-report.html", "--use-conda", "-F"])


def test_strelka_somatic():
    run("bio/strelka/somatic", ["snakemake", "a_vcf", "--use-conda", "-F", "-j 2"])


def test_gatk_mutect():
    run("bio/gatk/mutect", ["snakemake", "variant/a.vcf", "--use-conda", "-F"])


def test_varscan_mpileup2indel():
    run("bio/varscan/mpileup2indel", ["snakemake", "vcf/a.vcf", "--use-conda", "-F"])


def test_varscan_mpileup2snp():
    run("bio/varscan/mpileup2snp", ["snakemake", "vcf/a.vcf", "--use-conda", "-F"])


def test_varscan_mpileup2snp():
    run("bio/varscan/somatic", ["snakemake", "vcf/a.snp.vcf", "--use-conda", "-F"])


def test_umis_bamtag():
    run("bio/umis/bamtag", ["snakemake", "data/a.annotated.bam", "--use-conda", "-F"])


def test_transdecoder_longorfs():
    run(
        "bio/transdecoder/longorfs",
        ["snakemake", "test.fa.transdecoder_dir/longest_orfs.pep", "--use-conda", "-F"],
    )


def test_transdecoder_predict():
    run(
        "bio/transdecoder/predict",
        ["snakemake", "test.fa.transdecoder.gff3", "--use-conda", "-F"],
    )


def test_lastdb_nucl():
    run("bio/last/lastdb", ["snakemake", "test-transcript.fa.prj", "--use-conda", "-F"])


def test_lastdb_prot():
    run("bio/last/lastdb", ["snakemake", "test-protein.fa.prj", "--use-conda", "-F"])


def test_lastal_nucl():
    run("bio/last/lastal", ["snakemake", "test-transcript.maf", "--use-conda", "-F"])


def test_lastal_prot():
    run("bio/last/lastal", ["snakemake", "test-tr-x-prot.maf", "--use-conda", "-F"])


def test_pear():
    run(
        "bio/pear",
        ["snakemake", "pear/reads_pear_assembled.fq.gz", "--use-conda", "-F"],
    )


def test_plass_paired():
    run("bio/plass", ["snakemake", "plass/prot.fasta", "--use-conda", "-F"])


def test_plass_single():
    run("bio/plass", ["snakemake", "plass/prot_single.fasta", "--use-conda", "-F"])


def test_refgenie():
    try:
        shutil.copytree("bio/refgenie/test/genome_folder", "/tmp/genome_folder")
    except FileExistsError:
        # no worries, the directory is already there
        pass
    os.environ["REFGENIE"] = "/tmp/genome_folder/genome_config.yaml"
    run("bio/refgenie", ["snakemake", "--use-conda", "-F"])


def test_hmmbuild():
    run("bio/hmmer/hmmbuild", ["snakemake", "test-profile.hmm", "--use-conda", "-F"])


def test_hmmpress():
    run(
        "bio/hmmer/hmmpress", ["snakemake", "test-profile.hmm.h3f", "--use-conda", "-F"]
    )


def test_hmmscan():
    run("bio/hmmer/hmmscan", ["snakemake", "test-prot-tbl.txt", "--use-conda", "-F"])


def test_hmmsearch():
    run("bio/hmmer/hmmsearch", ["snakemake", "test-prot-tbl.txt", "--use-conda", "-F"])


def test_paladin_index():
    run("bio/paladin/index", ["snakemake", "index/prot.fasta.bwt", "--use-conda", "-F"])


def test_paladin_prepare():
    run(
        "bio/paladin/prepare",
        ["snakemake", "uniprot_sprot.fasta.gz", "--use-conda", "-F"],
    )


def test_paladin_align():
    run("bio/paladin/align", ["snakemake", "paladin_mapped/a.bam", "--use-conda", "-F"])


def test_ucsc_bedgraphtobigwig():
    run("bio/ucsc/bedGraphToBigWig", ["snakemake", "a.bw", "--use-conda", "-F"])


def test_ucsc_fatotwobit():
    run(
        "bio/ucsc/faToTwoBit",
        ["snakemake", "genome.2bit", "genome_gz.2bit", "--use-conda", "-F"],
    )


def test_ucsc_twobitinfo():
    run("bio/ucsc/twoBitInfo", ["snakemake", "genome.chrom.sizes", "--use-conda", "-F"])


def test_ucsc_twobittofa():
    run("bio/ucsc/twoBitToFa", ["snakemake", "genome.fa", "--use-conda", "-F"])


def test_ensembl_sequence():
    run("bio/reference/ensembl-sequence", ["snakemake", "--use-conda", "-F"])


def test_ensembl_annotation():
    run("bio/reference/ensembl-annotation", ["snakemake", "--use-conda", "-F"])


def test_ensembl_variation():
    run("bio/reference/ensembl-variation", ["snakemake", "--use-conda", "-F"])


def test_ensembl_variation_with_contig_lengths():
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "--snakefile", "with_fai.smk", "--use-conda", "-F"],
    )


def test_infernal_cmpress():
    run(
        "bio/infernal/cmpress",
        ["snakemake", "test-covariance-model.cm.i1f", "--use-conda", "-F"],
    )


def test_infernal_cmscan():
    run(
        "bio/infernal/cmscan",
        ["snakemake", "tr-infernal-tblout.txt", "--use-conda", "-F"],
    )


def test_bismark_genome_preparation():
    run(
        "bio/bismark/bismark_genome_preparation",
        [
            "snakemake",
            "indexes/genome/Bisulfite_Genome",
            "indexes/genome_gz/Bisulfite_Genome",
            "--use-conda",
            "-F",
        ],
    )


def test_bismark_genome_bam2nuc():
    run(
        "bio/bismark/bam2nuc",
        [
            "snakemake",
            "indexes/genome/genomic_nucleotide_frequencies.txt",
            "bams/b_genome.nucleotide_stats.txt",
            "--use-conda",
            "-F",
        ],
    )


def test_bismark_bismark():
    run(
        "bio/bismark/bismark",
        ["snakemake", "bams/a_genome_pe.bam", "bams/b_genome.bam", "--use-conda", "-F"],
    )


def test_bismark_deduplicate_bismark():
    run(
        "bio/bismark/deduplicate_bismark",
        [
            "snakemake",
            "bams/a_genome_pe.deduplicated.bam",
            "bams/b_genome.deduplicated.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_bismark_bismark_methylation_extractor():
    run(
        "bio/bismark/bismark_methylation_extractor",
        [
            "snakemake",
            "meth_cpg/a_genome_pe.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.bismark.cov.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_bismark_bismark2report():
    run(
        "bio/bismark/bismark2report",
        [
            "snakemake",
            "qc/meth/a_genome.bismark2report.html",
            "qc/meth/b_genome.bismark2report.html",
            "--use-conda",
            "-F",
        ],
    )


def test_bismark_bismark2summary():
    run(
        "bio/bismark/bismark2summary",
        ["snakemake", "qc/experiment.bismark2summary.html", "--use-conda", "-F"],
    )


def test_bismark_bismark2bedgraph():
    run(
        "bio/bismark/bismark2bedGraph",
        [
            "snakemake",
            "meth_cpg/a_genome_pe.deduplicated_CpG.bismark.cov.gz",
            "meth_non_cpg/a_genome_pe.deduplicated_non_cpg.bismark.cov.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_tabix():
    run("bio/tabix", ["snakemake", "--use-conda", "-F", "test.vcf.gz.tbi"])


def test_msisensor_scan():
    run("bio/msisensor/scan", ["snakemake", "--use-conda", "-F", "microsat.list"])


def test_msisensor_msi():
    run("bio/msisensor/msi", ["snakemake", "--use-conda", "-F", "example.msi"])


def test_tximport():
    run("bio/tximport", ["snakemake", "txi.RDS", "--use-conda", "-F"])


def test_fasterq_dump():
    run(
        "bio/sra-tools/fasterq-dump",
        ["snakemake", "data/ERR267986.fastq", "--use-conda", "-F"],
    )


def test_bwa_mem_samblaster():
    run("bio/bwa/mem-samblaster", ["snakemake", "mapped/a.bam", "--use-conda", "-F"])
