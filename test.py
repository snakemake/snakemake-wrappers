import subprocess
import os
import tempfile
import shutil
import pytest
import sys
import yaml
from itertools import chain

DIFF_MASTER = os.environ.get("DIFF_MASTER", "false") == "true"
DIFF_LAST_COMMIT = os.environ.get("DIFF_LAST_COMMIT", "false") == "true"

if DIFF_MASTER or DIFF_LAST_COMMIT:
    compare = "HEAD^" if DIFF_LAST_COMMIT else "origin/master"

    # check if wrapper is modified compared to master
    DIFF_FILES = set(
        subprocess.check_output(["git", "diff", compare, "--name-only"])
        .decode()
        .split("\n")
    )

CONTAINERIZED = os.environ.get("CONTAINERIZED", "false") == "true"


class Skipped(Exception):
    pass


skip_if_not_modified = pytest.mark.xfail(raises=Skipped)


def run(wrapper, cmd, check_log=None):
    origdir = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "master")
        os.makedirs(dst, exist_ok=True)
        copy = lambda pth, src: shutil.copy(
            os.path.join(pth, src), os.path.join(dst, pth)
        )

        used_wrappers = []
        wrapper_file = "used_wrappers.yaml"
        if os.path.exists(os.path.join(wrapper, wrapper_file)):
            # is meta wrapper
            with open(os.path.join(wrapper, wrapper_file), "r") as wf:
                wf = yaml.load(wf, Loader=yaml.BaseLoader)
                used_wrappers = wf["wrappers"]
        else:
            used_wrappers.append(wrapper)

        for w in used_wrappers:
            success = False
            for ext in ("py", "R", "Rmd"):
                script = "wrapper." + ext
                if os.path.exists(os.path.join(w, script)):
                    os.makedirs(os.path.join(dst, w), exist_ok=True)
                    copy(w, script)
                    success = True
                    break
            assert success, "No wrapper script found for {}".format(w)
            copy(w, "environment.yaml")

        if (DIFF_MASTER or DIFF_LAST_COMMIT) and not any(
            any(f.startswith(w) for f in DIFF_FILES)
            for w in chain(used_wrappers, [wrapper])
        ):
            raise Skipped("wrappers not modified")

        testdir = os.path.join(d, "test")
        # pkgdir = os.path.join(d, "pkgs")
        shutil.copytree(os.path.join(wrapper, "test"), testdir)
        # prepare conda package dir
        # os.makedirs(pkgdir)
        # switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + ["--wrapper-prefix", "file://{}/".format(d), "--conda-cleanup-pkgs"]

        if CONTAINERIZED:
            # run snakemake in container
            cmd = [
                "sudo",
                "docker",
                "run",
                "-it",
                "-v",
                "{}:{}".format(os.getcwd(), "/workdir"),
                "snakemake/snakemake",
                " ".join(cmd),
            ]

        # env = dict(os.environ)
        # env["CONDA_PKGS_DIRS"] = pkgdir
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
            # cleanup environments to save disk space
            subprocess.check_call(
                "for env in `conda env list | grep -P '\.snakemake/conda' | "
                "cut -f1 | tr -d ' '`; do conda env remove --prefix $env; done",
                shell=True,
            )
            # go back to original directory
            os.chdir(origdir)


@skip_if_not_modified
def test_open_cravat_run():
    run(
        "bio/open-cravat/run",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


@skip_if_not_modified
def test_open_cravat_module():
    run(
        "bio/open-cravat/module",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


@skip_if_not_modified
def test_dada2_se_meta():
    run(
        "meta/bio/dada2_se",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
        ],
    )


@skip_if_not_modified
def test_adapterremoval_pe_collapse_singletons():
    run(
        "bio/adapterremoval",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "trimmed/pe_collapse/a_R1.fastq.gz",
            "trimmed/pe_collapse/a_R2.fastq.gz",
            "trimmed/pe_collapse/a.fastq.gz",
            "trimmed/pe_collapse/a.discarded.fastq.gz",
            "stats/pe_collapse/a.settings",
        ],
    )


@skip_if_not_modified
def test_adapterremoval_pe():
    run(
        "bio/adapterremoval",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "trimmed/pe/a_R1.fastq.gz",
            "trimmed/pe/a_R2.fastq.gz",
            "trimmed/pe/a.singleton.fastq.gz",
            "trimmed/pe/a.collapsed.fastq.gz",
            "trimmed/pe/a.collapsed_trunc.fastq.gz",
            "trimmed/pe/a.discarded.fastq.gz",
            "stats/pe/a.settings",
        ],
    )


@skip_if_not_modified
def test_adapterremoval_se():
    run(
        "bio/adapterremoval",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "trimmed/se/a.fastq.gz",
            "trimmed/se/a.discarded.fastq.gz",
            "stats/se/a.settings",
        ],
    )


@skip_if_not_modified
def test_dada2_pe_meta():
    run(
        "meta/bio/dada2_pe",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/dada2/taxa.RDS",
            "reports/dada2/quality-profile/a-quality-profile.png",
            "reports/dada2/quality-profile/b-quality-profile.png",
        ],
    )


@skip_if_not_modified
def test_mapdamage2():
    run(
        "bio/mapdamage2",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/a/Runtime_log.txt",
        ],
    )


@skip_if_not_modified
def test_dada2_quality_profile_se():
    run(
        "bio/dada2/quality-profile",
        [
            "snakemake",
            "--cores",
            "1",
            "reports/dada2/quality-profile/a-quality-profile.png",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_dada2_quality_profile_pe():
    run(
        "bio/dada2/quality-profile",
        [
            "snakemake",
            "--cores",
            "1",
            "reports/dada2/quality-profile/a.1-quality-profile.png",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_dada2_filter_trim_se():
    run(
        "bio/dada2/filter-trim",
        ["snakemake", "--cores", "1", "filtered-se/a.1.fastq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_dada2_filter_trim_pe():
    run(
        "bio/dada2/filter-trim",
        ["snakemake", "--cores", "1", "filtered-pe/a.1.fastq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_dada2_dereplicate_fastq():
    run(
        "bio/dada2/dereplicate-fastq",
        ["snakemake", "--cores", "1", "--use-conda", "uniques/a.1.RDS"],
    )


@skip_if_not_modified
def test_dada2_learn_errors():
    run(
        "bio/dada2/learn-errors",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/model_1.RDS"],
    )


@skip_if_not_modified
def test_dada2_sample_inference():
    run(
        "bio/dada2/sample-inference",
        ["snakemake", "--cores", "1", "--use-conda", "denoised/a.1.RDS"],
    )


@skip_if_not_modified
def test_dada2_merge_pairs():
    run(
        "bio/dada2/merge-pairs",
        ["snakemake", "--cores", "1", "--use-conda", "merged/a.RDS", "-F"],
    )


@skip_if_not_modified
def test_dada2_make_table_se():
    run(
        "bio/dada2/make-table",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab-se.RDS"],
    )


@skip_if_not_modified
def test_dada2_make_table_pe():
    run(
        "bio/dada2/make-table",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab-pe.RDS"],
    )


@skip_if_not_modified
def test_dada2_remove_chimeras():
    run(
        "bio/dada2/remove-chimeras",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab.nochim.RDS"],
    )


@skip_if_not_modified
def test_dada2_collapse_nomismatch():
    run(
        "bio/dada2/collapse-nomismatch",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/dada2/seqTab.collapsed.RDS",
        ],
    )


@skip_if_not_modified
def test_dada2_assign_taxonomy():
    run(
        "bio/dada2/assign-taxonomy",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/taxa.RDS"],
    )


@skip_if_not_modified
def test_dada2_assign_species():
    run(
        "bio/dada2/assign-species",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/dada2/genus-species-taxa.RDS",
        ],
    )


@skip_if_not_modified
def test_dada2_add_species():
    run(
        "bio/dada2/add-species",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/taxa-sp.RDS"],
    )


@skip_if_not_modified
def test_arriba_star_meta():
    run(
        "meta/bio/star_arriba",
        ["snakemake", "--cores", "1", "--use-conda", "results/arriba/a.fusions.tsv"],
    )


@skip_if_not_modified
def test_bwa_mapping_meta():
    run(
        "meta/bio/bwa_mapping",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "mapped/a.bam.bai",
        ],
    )


@skip_if_not_modified
def test_gridss_call():
    run(
        "bio/gridss/call",
        [
            "snakemake",
            "--show-failed-logs",
            "--cores",
            "1",
            "--use-conda",
            "vcf/group.vcf",
        ],
    )


@skip_if_not_modified
def test_gridss_assemble():
    run(
        "bio/gridss/assemble",
        [
            "snakemake",
            "--show-failed-logs",
            "--cores",
            "1",
            "--use-conda",
            "assembly/group.bam",
        ],
    )


@skip_if_not_modified
def test_gridss_preprocess():
    run(
        "bio/gridss/preprocess",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "--show-failed-logs",
            "working_dir/A.bam.gridss.working/A.bam.cigar_metrics",
            "working_dir/A.bam.gridss.working/A.bam.coverage.blacklist.bed",
            "working_dir/A.bam.gridss.working/A.bam.idsv_metrics",
            "working_dir/A.bam.gridss.working/A.bam.insert_size_histogram.pdf",
            "working_dir/A.bam.gridss.working/A.bam.insert_size_metrics",
            "working_dir/A.bam.gridss.working/A.bam.mapq_metrics",
            "working_dir/A.bam.gridss.working/A.bam.sv.bam",
            "working_dir/A.bam.gridss.working/A.bam.sv.bam.bai",
            "working_dir/A.bam.gridss.working/A.bam.sv_metrics",
            "working_dir/A.bam.gridss.working/A.bam.tag_metrics",
        ],
    )


@skip_if_not_modified
def test_gridss_setupreference():
    run(
        "bio/gridss/setupreference",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "--show-failed-logs",
            "reference/genome.fasta.gridsscache",
            "reference/genome.fasta.img",
        ],
    )


@skip_if_not_modified
def test_strling_call():
    run(
        "bio/strling/call",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "call/A-bounds.txt",
            "call/A-genotype.txt",
            "call/A-unplaced.txt",
        ],
    )


@skip_if_not_modified
def test_strling_merge():
    run(
        "bio/strling/merge",
        ["snakemake", "--cores", "1", "--use-conda", "merged/group-bounds.txt"],
    )


@skip_if_not_modified
def test_strling_extract():
    run(
        "bio/strling/extract",
        ["snakemake", "--cores", "1", "--use-conda", "extract/A.bin"],
    )


@skip_if_not_modified
def test_strling_index():
    run(
        "bio/strling/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "reference/genome.fasta.str",
            "reference/genome.fasta.fai",
        ],
    )


@skip_if_not_modified
def test_vembrane_filter():
    run(
        "bio/vembrane/filter",
        ["snakemake", "--cores", "1", "--use-conda", "filtered/out.vcf"],
    )


@skip_if_not_modified
def test_vembrane_table():
    run(
        "bio/vembrane/table",
        ["snakemake", "--cores", "1", "--use-conda", "table/out.tsv"],
    )


@skip_if_not_modified
def test_shovill():
    run(
        "bio/shovill",
        [
            "snakemake",
            "assembly/input.spades.assembly.fa",
            "assembly/input.spades.contigs.fa",
            "--cores",
            "1",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_seqtk_subsample_se():
    run(
        "bio/seqtk/subsample/se",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.subsampled.fastq.gz"],
    )


@skip_if_not_modified
def test_seqtk_subsample_pe():
    run(
        "bio/seqtk/subsample/pe",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "a.1.subsampled.fastq.gz",
            "a.2.subsampled.fastq.gz",
        ],
    )


@skip_if_not_modified
def test_arriba():
    run(
        "bio/arriba",
        [
            "snakemake",
            "--cores",
            "1",
            "fusions/A.tsv",
            "fusions/A.discarded.tsv",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_art_profiler_illumina():
    run(
        "bio/art/profiler_illumina",
        [
            "snakemake",
            "--cores",
            "1",
            "profiles/a.1.txt",
            "profiles/a.2.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bcftools_filter_vcf():
    run("bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf", "--use-conda", "-F"])


@skip_if_not_modified
def test_bcftools_filter_vcf_gz():
    run("bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf.gz", "--use-conda", "-F"])


@skip_if_not_modified
def test_bcftools_filter_bcf():
    run("bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.bcf", "--use-conda", "-F"])


@skip_if_not_modified
def test_bcftools_filter_bcf_gz():
    run("bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.bcf.gz", "--use-conda", "-F"])


@skip_if_not_modified
def test_bcftools_sort():
    run(
        "bio/bcftools/sort",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.sorted.bcf"],
    )


@skip_if_not_modified
def test_bcftools_call():
    run(
        "bio/bcftools/call",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.calls.bcf"],
    )


@skip_if_not_modified
def test_bcftools_index():
    run(
        "bio/bcftools/index",
        ["snakemake", "--cores", "1", "a.bcf.csi", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_concat():
    run(
        "bio/bcftools/concat",
        ["snakemake", "--cores", "1", "all.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_merge():
    run(
        "bio/bcftools/merge",
        ["snakemake", "--cores", "1", "all.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_mpileup():
    run(
        "bio/bcftools/mpileup",
        ["snakemake", "--cores", "1", "pileups/a.pileup.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_reheader():
    run(
        "bio/bcftools/reheader",
        ["snakemake", "--cores", "1", "a.reheader.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_view():
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.vcf"],
    )


@skip_if_not_modified
def test_bedtools_genomecoveragebed():
    run(
        "bio/bedtools/genomecov",
        [
            "snakemake",
            "--cores",
            "1",
            "genomecov_bam/a.genomecov",
            "genomecov_bed/a.genomecov",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bedtools_complement():
    run(
        "bio/bedtools/complement",
        [
            "snakemake",
            "--cores",
            "1",
            "results/bed-complement/a.complement.bed",
            "results/vcf-complement/a.complement.vcf",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bedtools_sort():
    run(
        "bio/bedtools/sort",
        [
            "snakemake",
            "--cores",
            "1",
            "results/bed-sorted/a.sorted.bed",
            "results/bed-sorted/a.sorted_by_file.bed",
            "results/vcf-sorted/a.sorted_by_file.vcf",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bedtools_intersect():
    run(
        "bio/bedtools/intersect",
        ["snakemake", "--cores", "1", "A_B.intersected.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bedtools_merge():
    run(
        "bio/bedtools/merge",
        [
            "snakemake",
            "--cores",
            "1",
            "A.merged.bed",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile",
        ],
    )


@skip_if_not_modified
def test_bedtools_merge_multi():
    run(
        "bio/bedtools/merge",
        [
            "snakemake",
            "--cores",
            "1",
            "AB.merged.bed",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_multi",
        ],
    )


@skip_if_not_modified
def test_bedtools_slop():
    run(
        "bio/bedtools/slop",
        ["snakemake", "--cores", "1", "A.slop.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bowtie2_align():
    run(
        "bio/bowtie2/align",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bowtie2_build():
    run(
        "bio/bowtie2/build",
        ["snakemake", "--cores", "1", "genome.1.bt2", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_mem():
    run(
        "bio/bwa/mem",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_mem_sort_samtools():
    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_mem_sort_picard():
    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_aln():
    run(
        "bio/bwa/aln",
        [
            "snakemake",
            "--cores",
            "1",
            "sai/a.1.sai",
            "sai/a.2.sai",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bwa_index():
    run(
        "bio/bwa/index",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.amb",
            "genome.ann",
            "genome.bwt",
            "genome.pac",
            "genome.sa",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_se():
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.se.sam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_pe():
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.pe.sam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_se():
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.se.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_pe():
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.pe.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_se_sort_samtools():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.se.samtools_sort.sam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_pe_sort_samtools():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.pe.samtools_sort.sam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_se_sort_samtools():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.se.samtools_sort.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_pe_sort_samtools():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.pe.samtools_sort.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_se_sort_picard():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.se.picard_sort.sam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_sam_pe_sort_picard():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.pe.picard_sort.sam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_se_sort_picard():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.se.picard_sort.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_samxe_bam_pe_sort_picard():
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.pe.picard_sort.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_sampe():
    run(
        "bio/bwa/sampe",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_sampe_sort_samtools():
    run(
        "bio/bwa/sampe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_sampe_sort_picard():
    run(
        "bio/bwa/sampe",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_samse():
    run(
        "bio/bwa/samse",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_samse_sort_samtools():
    run(
        "bio/bwa/samse",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_samse_sort_picard():
    run(
        "bio/bwa/samse",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_mem2_mem():
    run(
        "bio/bwa-mem2/mem",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_mem2_sort_samtools():
    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


@skip_if_not_modified
def test_bwa_mem2_sort_picard():
    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


@skip_if_not_modified
def test_bwa_mem2_index():
    run(
        "bio/bwa-mem2/index",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.fasta.amb",
            "genome.fasta.ann",
            "genome.fasta.0123",
            "genome.fasta.bwt.2bit.64",
            "genome.fasta.bwt.8bit.32",
            "genome.fasta.pac",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_clustalo():
    run(
        "bio/clustalo",
        ["snakemake", "--cores", "1", "test.msa.fa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cutadapt_pe():
    run(
        "bio/cutadapt/pe",
        ["snakemake", "--cores", "1", "trimmed/a.1.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cutadapt_se():
    run(
        "bio/cutadapt/se",
        ["snakemake", "--cores", "1", "trimmed/a.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_deeptools_computematrix():
    run(
        "bio/deeptools/computematrix",
        [
            "snakemake",
            "--cores",
            "1",
            "matrix_files/matrix.gz",
            "matrix_files/matrix.tab",
            "matrix_files/matrix.bed",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_deeptools_plotheatmap():
    run(
        "bio/deeptools/plotheatmap",
        [
            "snakemake",
            "--cores",
            "1",
            "plot_heatmap/heatmap.png",
            "plot_heatmap/heatmap_regions.bed",
            "plot_heatmap/heatmap_matrix.tab",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_deeptools_plotfingerprint():
    run(
        "bio/deeptools/plotfingerprint",
        [
            "snakemake",
            "--cores",
            "1",
            "plot_fingerprint/plot_fingerprint.png",
            "plot_fingerprint/raw_counts.tab",
            "plot_fingerprint/qc_metrics.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_deeptools_plotprofile():
    run(
        "bio/deeptools/plotprofile",
        [
            "snakemake",
            "--cores",
            "1",
            "plot_profile/plot.png",
            "plot_profile/regions.bed",
            "plot_profile/data.tab",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_deepvariant():
    run(
        "bio/deepvariant",
        ["snakemake", "--cores", "1", "calls/a.vcf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_epic_peaks():
    run(
        "bio/epic/peaks",
        ["snakemake", "--cores", "1", "epic/enriched_regions.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fastp_pe():
    run(
        "bio/fastp",
        [
            "snakemake",
            "--cores",
            "1",
            "trimmed/pe/a.1.fastq",
            "trimmed/pe/a.2.fastq",
            "report/pe/a.html",
            "report/pe/a.json",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_fastp_pe_wo_trimming():
    run(
        "bio/fastp",
        [
            "snakemake",
            "--cores",
            "1",
            "report/pe_wo_trimming/a.html",
            "report/pe_wo_trimming/a.json",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_fastp_se():
    run(
        "bio/fastp",
        [
            "snakemake",
            "--cores",
            "1",
            "trimmed/se/a.fastq",
            "report/se/a.html",
            "report/se/a.json",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_fastqc():
    run(
        "bio/fastqc",
        ["snakemake", "--cores", "1", "qc/fastqc/a.html", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fastq_screen():
    run(
        "bio/fastq_screen",
        ["snakemake", "--cores", "1", "qc/a.fastq_screen.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fgbio_annotate():
    run(
        "bio/fgbio/annotatebamwithumis",
        ["snakemake", "--cores", "1", "mapped/a.annotated.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fgbio_collectduplexseqmetrics():
    run(
        "bio/fgbio/collectduplexseqmetrics",
        [
            "snakemake",
            "--cores",
            "1",
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


@skip_if_not_modified
def test_fgbio_filterconsensusreads():
    run(
        "bio/fgbio/filterconsensusreads",
        ["snakemake", "--cores", "1", "mapped/a.filtered.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fgbio_group():
    run(
        "bio/fgbio/groupreadsbyumi",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.gu.bam",
            "mapped/a.gu.histo.tsv",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_fgbio_set_mate_information():
    run(
        "bio/fgbio/setmateinformation",
        ["snakemake", "--cores", "1", "mapped/a.mi.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fgbio_call_molecular_consensus_reads():
    run(
        "bio/fgbio/callmolecularconsensusreads",
        ["snakemake", "--cores", "1", "mapped/a.m3.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_filtlong():
    run(
        "bio/filtlong",
        ["snakemake", "--cores", "1", "reads.filtered.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_freebayes():
    run(
        "bio/freebayes",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
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


@skip_if_not_modified
def test_freebayes_bed():
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
                "Snakefile_bed",
            ],
        )


@skip_if_not_modified
def test_gdc_api_bam_slicing():
    def check_log(log):
        assert "error" in log and "token" in log

    run(
        "bio/gdc-api/bam-slicing",
        ["snakemake", "--cores", "1", "raw/testing_sample.bam", "--use-conda", "-F"],
        check_log=check_log,
    )


@skip_if_not_modified
def test_gdc_download():
    run(
        "bio/gdc-client/download",
        ["snakemake", "--cores", "1", "raw/testing_sample.maf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_happy_prepy():
    run(
        "bio/hap.py/pre.py",
        ["snakemake", "--cores", "1", "normalized/variants.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_happy_prepy():
    run(
        "bio/hap.py/pre.py",
        ["snakemake", "--cores", "1", "normalized/variants.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_hisat2_index():
    run(
        "bio/hisat2/index",
        ["snakemake", "--cores", "1", "index_genome", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_hisat2_align():
    run(
        "bio/hisat2/align",
        ["snakemake", "--cores", "1", "mapped/A.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_homer_mergePeaks():
    run(
        "bio/homer/mergePeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "merged/a_b.peaks"],
    )


@skip_if_not_modified
def test_homer_getDifferentialPeaks():
    run(
        "bio/homer/getDifferentialPeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a_diffPeaks.txt"],
    )


@skip_if_not_modified
def test_homer_findPeaks():
    run(
        "bio/homer/findPeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a_peaks.txt"],
    )


@skip_if_not_modified
def test_homer_makeTagDirectory():
    run(
        "bio/homer/makeTagDirectory",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "tagDir/a"],
    )


@skip_if_not_modified
def test_homer_annotatePeaks():
    run(
        "bio/homer/annotatePeaks",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "a_annot.txt",
            "a.count.matrix.txt",
            "a.ratio.matrix.txt",
            "a.logPvalue.matrix.txt",
            "a.stats.txt",
            "a_motif.fasta",
            "a_motif.bed",
            "a_motif.logic",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_kallisto_index():
    run(
        "bio/kallisto/index",
        ["snakemake", "--cores", "1", "transcriptome.idx", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_kallisto_quant():
    run(
        "bio/kallisto/quant",
        ["snakemake", "--cores", "1", "quant_results_A", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_lofreq_call():
    run(
        "bio/lofreq/call",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_macs2_callpeak():
    run(
        "bio/macs2/callpeak",
        [
            "snakemake",
            "--cores",
            "1",
            "callpeak/basename_peaks.xls",
            "callpeak/basename_peaks.narrowPeak",
            "callpeak/basename_summits.bed",
            "callpeak_options/basename_peaks.xls",
            "callpeak_options/basename_peaks.broadPeak",
            "callpeak_options/basename_peaks.gappedPeak",
            "callpeak_options/basename_treat_pileup.bdg",
            "callpeak_options/basename_control_lambda.bdg",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_minimap2_aligner():
    run(
        "bio/minimap2/aligner",
        ["snakemake", "--cores", "1", "aligned/genome_aln.paf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_minimap2_index():
    run(
        "bio/minimap2/index",
        ["snakemake", "--cores", "1", "genome.mmi", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_multiqc():
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc.html", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_nanosimh():
    run(
        "bio/nanosim-h",
        [
            "snakemake",
            "--cores",
            "1",
            "test.simulated.fa",
            "test.simulated.log",
            "test.simulated.errors.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_ngs_disambiguate():
    run(
        "bio/ngs-disambiguate",
        [
            "snakemake",
            "--cores",
            "1",
            "disambiguate/s1.graft.ambiguous.bam",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_optitype():
    run(
        "bio/optitype",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "optitype/a_result.tsv"],
    )


@skip_if_not_modified
def test_picard_addorreplacegroups():
    run(
        "bio/picard/addorreplacereadgroups",
        ["snakemake", "--cores", "1", "fixed-rg/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_markduplicates():
    run(
        "bio/picard/markduplicates",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_markduplicateswithmatecigar():
    run(
        "bio/picard/markduplicateswithmatecigar",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_collectalignmentsummarymetrics():
    run(
        "bio/picard/collectalignmentsummarymetrics",
        ["snakemake", "--cores", "1", "stats/a.summary.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_collectinsertsizemetrics():
    run(
        "bio/picard/collectinsertsizemetrics",
        ["snakemake", "--cores", "1", "stats/a.isize.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_bedtointervallist():
    run(
        "bio/picard/bedtointervallist",
        ["snakemake", "--cores", "1", "a.interval_list", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_collecthsmetrics():
    run(
        "bio/picard/collecthsmetrics",
        ["snakemake", "--cores", "1", "stats/hs_metrics/a.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_collectmultiplemetrics():
    run(
        "bio/picard/collectmultiplemetrics",
        [
            "snakemake",
            "--cores",
            "1",
            "stats/a.alignment_summary_metrics",
            "stats/a.insert_size_metrics",
            "stats/a.insert_size_histogram.pdf",
            "stats/a.quality_distribution_metrics",
            "stats/a.quality_distribution.pdf",
            "stats/a.quality_by_cycle_metrics",
            "stats/a.quality_by_cycle.pdf",
            "stats/a.base_distribution_by_cycle_metrics",
            "stats/a.base_distribution_by_cycle.pdf",
            "stats/a.gc_bias.detail_metrics",
            "stats/a.gc_bias.summary_metrics",
            "stats/a.gc_bias.pdf",
            "stats/a.rna_metrics",
            "stats/a.bait_bias_detail_metrics",
            "stats/a.bait_bias_summary_metrics",
            "stats/a.error_summary_metrics",
            "stats/a.pre_adapter_detail_metrics",
            "stats/a.pre_adapter_summary_metrics",
            "stats/a.quality_yield_metrics",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_picard_mergesamfiles():
    run(
        "bio/picard/mergesamfiles",
        ["snakemake", "--cores", "1", "merged.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_collecttargettedpcemetrics():
    run(
        "bio/picard/collecttargetedpcrmetrics/",
        ["snakemake", "--cores", "1", "stats/a.pcr.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_bam_to_fastq():
    run(
        "bio/picard/samtofastq",
        [
            "snakemake",
            "--cores",
            "1",
            "reads/a.R1.fastq",
            "reads/a.R2.fastq",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_picard_sortsam():
    run(
        "bio/picard/sortsam",
        ["snakemake", "--cores", "1", "sorted/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_revertsam():
    run(
        "bio/picard/revertsam",
        ["snakemake", "--cores", "1", "revert/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_createsequencedictionary():
    run(
        "bio/picard/createsequencedictionary",
        ["snakemake", "--cores", "1", "genome.dict", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pindel_call():
    run(
        "bio/pindel/call",
        ["snakemake", "--cores", "1", "pindel/all_D", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pindel_pindel2vcf():
    run(
        "bio/pindel/pindel2vcf",
        ["snakemake", "--cores", "1", "pindel/all_D.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pindel_pindel2vcf_multi_input():
    run(
        "bio/pindel/pindel2vcf",
        ["snakemake", "--cores", "1", "pindel/all.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_preseq_lc_extrap():
    run(
        "bio/preseq/lc_extrap",
        [
            "snakemake",
            "--cores",
            "1",
            "test_bam/a.lc_extrap",
            "test_bed/a.lc_extrap",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_prosolo_calling():
    run(
        "bio/prosolo/single-cell-bulk",
        [
            "snakemake",
            "--cores",
            "1",
            "variant_calling/single_cell.bulk.prosolo.bcf",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_prosolo_fdr():
    run(
        "bio/prosolo/control-fdr",
        [
            "snakemake",
            "--cores",
            "1",
            "fdr_control/single_cell.bulk.prosolo.fdr.bcf",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_razers3():
    run(
        "bio/razers3",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "mapped/a.bam"],
    )


@skip_if_not_modified
def test_rebaler():
    run("bio/rebaler", ["snakemake", "--cores", "1", "--use-conda", "sample1.asm.fa"])


@skip_if_not_modified
def test_sambamba_flagstats():
    run(
        "bio/sambamba/flagstat",
        ["snakemake", "--cores", "1", "mapped/A.stats.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_sort():
    run(
        "bio/sambamba/sort",
        ["snakemake", "--cores", "1", "mapped/A.sorted.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_index():
    run(
        "bio/sambamba/index",
        ["snakemake", "--cores", "1", "mapped/A.sorted.bam.bai", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_merge():
    run(
        "bio/sambamba/merge",
        ["snakemake", "--cores", "1", "mapped/A.merged.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_view():
    run(
        "bio/sambamba/view", ["snakemake", "--cores", "1", "mapped/A.filtered.bam", "--use-conda", "-F"]
    )


@skip_if_not_modified
def test_sambamba_slice():
    run(
        "bio/sambamba/slice", ["snakemake", "--cores", "1", "mapped/A.region.bam", "--use-conda", "-F"]
    )


@skip_if_not_modified
def test_sambamba_markdup():
    run(
        "bio/sambamba/markdup", ["snakemake", "--cores", "1", "mapped/A.rmdup.bam", "--use-conda", "-F"]
    )


@skip_if_not_modified
def test_samtools_calmd():
    run(
        "bio/samtools/calmd",
        ["snakemake", "--cores", "1", "a.calmd.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_fixmate():
    run(
        "bio/samtools/fixmate",
        ["snakemake", "--cores", "1", "fixed/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pyfastaq_replace_bases():
    run(
        "bio/pyfastaq/replace_bases",
        ["snakemake", "--cores", "1", "sample1.dna.fa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_depth():
    run(
        "bio/samtools/depth",
        ["snakemake", "--cores", "1", "depth.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_mpileup():
    run(
        "bio/samtools/mpileup",
        ["snakemake", "--cores", "1", "mpileup/a.mpileup.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_stats():
    run(
        "bio/samtools/stats",
        ["snakemake", "--cores", "1", "samtools_stats/a.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_sort():
    run(
        "bio/samtools/sort",
        ["snakemake", "--cores", "1", "mapped/a.sorted.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_index():
    run(
        "bio/samtools/index",
        ["snakemake", "--cores", "1", "mapped/a.sorted.bam.bai", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_merge():
    run(
        "bio/samtools/merge",
        ["snakemake", "--cores", "1", "merged.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_view():
    run(
        "bio/samtools/view", ["snakemake", "--cores", "1", "a.bam", "--use-conda", "-F"]
    )


@skip_if_not_modified
def test_samtools_flagstat():
    run(
        "bio/samtools/flagstat",
        ["snakemake", "--cores", "1", "mapped/a.bam.flagstat", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_idxstats():
    run(
        "bio/samtools/idxstats",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.sorted.bam.idxstats",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_samtools_bam2fq_interleaved():
    run(
        "bio/samtools/bam2fq/interleaved",
        ["snakemake", "--cores", "1", "reads/a.fq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_bam2fq_separate():
    run(
        "bio/samtools/bam2fq/separate",
        ["snakemake", "--cores", "1", "reads/a.1.fq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_faidx():
    run(
        "bio/samtools/faidx",
        ["snakemake", "--cores", "1", "genome.fa.fai", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bamtools_filter():
    run(
        "bio/bamtools/filter",
        ["snakemake", "--cores", "1", "filtered/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bamtools_filter_json():
    run(
        "bio/bamtools/filter_json",
        ["snakemake", "--cores", "1", "filtered/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bamtools_split():
    run(
        "bio/bamtools/split",
        ["snakemake", "--cores", "1", "mapped/a.REF_xx.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bamtools_stats():
    run(
        "bio/bamtools/stats",
        ["snakemake", "--cores", "1", "a.bamstats", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpmutator():
    run(
        "bio/snp-mutator",
        [
            "snakemake",
            "--cores",
            "1",
            "test_mutated_1.fasta",
            "test_mutated_2.fasta",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
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

    run(
        "bio/star/align",
        ["snakemake", "--cores", "1", "star/a/Aligned.out.sam", "--use-conda", "-F"],
    )
    run(
        "bio/star/align",
        ["snakemake", "--cores", "1", "star/pe/a/Aligned.out.sam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_star_index():
    run("bio/star/index", ["snakemake", "--cores", "1", "genome", "--use-conda", "-F"])


@skip_if_not_modified
def test_snpeff_annotate():
    run(
        "bio/snpeff/annotate",
        ["snakemake", "--cores", "1", "snpeff/fake_KJ660346.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpeff_download():
    run(
        "bio/snpeff/download",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/snpeff/ebola_zaire",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_snpeff_nostats():
    run(
        "bio/snpeff/annotate",
        [
            "snakemake",
            "--cores",
            "1",
            "snpeff_nostats/fake_KJ660346.vcf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_nostats",
        ],
    )


@skip_if_not_modified
def test_strelka_germline():
    run(
        "bio/strelka/germline",
        ["snakemake", "--cores", "1", "strelka/a", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_subread_featurecounts():
    run(
        "bio/subread/featurecounts",
        [
            "snakemake",
            "--cores",
            "1",
            "results/a.featureCounts",
            "results/a.featureCounts.summary",
            "results/a.featureCounts.jcounts",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_trim_galore_pe():
    run(
        "bio/trim_galore/pe",
        ["snakemake", "--cores", "1", "trimmed/a.1_val_1.fq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_trim_galore_se():
    run(
        "bio/trim_galore/se",
        ["snakemake", "--cores", "1", "trimmed/a_trimmed.fq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_trimmomatic_pe():
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic/pe",
        [
            "snakemake",
            "--cores",
            "1",
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
            "--cores",
            "1",
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
            "--cores",
            "1",
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
            "--cores",
            "1",
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
            "--cores",
            "1",
            "trimmed/a.1.fastq.gz",
            "--use-conda",
            "-F",
            "--cores",
            "32",
            "-s",
            "Snakefile_gz_gz",
        ],
    )


@skip_if_not_modified
def test_trimmomatic_se():
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "--cores",
            "1",
            "trimmed/a.fastq",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_fq_fq",
        ],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "--cores",
            "1",
            "trimmed/a.fastq.gz",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_fq_gz",
        ],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "--cores",
            "1",
            "trimmed/a.fastq",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_gz_fq",
        ],
    )
    run(
        "bio/trimmomatic/se",
        [
            "snakemake",
            "--cores",
            "1",
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
            "--cores",
            "1",
            "trimmed/a.fastq.gz",
            "--use-conda",
            "-F",
            "--cores",
            "32",
            "-s",
            "Snakefile_gz_gz",
        ],
    )


@skip_if_not_modified
def test_rasusa():
    run(
        "bio/rasusa",
        ["snakemake", "--cores", "1", "--use-conda", "a.subsampled.r1.fq"],
    )


@skip_if_not_modified
def test_rubic():
    run(
        "bio/rubic",
        ["snakemake", "--cores", "1", "BRCA/gains.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_delly():
    run("bio/delly", ["snakemake", "--cores", "1", "sv/calls.bcf", "--use-conda", "-F"])


@skip_if_not_modified
def test_jannovar():
    run(
        "bio/jannovar",
        [
            "snakemake",
            "--cores",
            "1",
            "jannovar/pedigree_vars.vcf.gz",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_cairosvg():
    run("utils/cairosvg", ["snakemake", "--cores", "1", "pca.pdf", "--use-conda", "-F"])


@skip_if_not_modified
def test_trinity():
    run(
        "bio/trinity",
        [
            "snakemake",
            "--cores",
            "1",
            "trinity_out_dir/Trinity.fasta",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_salmon_index():
    run(
        "bio/salmon/index",
        [
            "snakemake",
            "--cores",
            "1",
            "salmon/transcriptome_index",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_salmon_quant():
    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "--cores",
            "1",
            "salmon/a/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile",
        ],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "--cores",
            "1",
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
            "--cores",
            "1",
            "salmon/ab_pe_x_transcriptome/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_pe_multi",
        ],
    )


@skip_if_not_modified
def test_sourmash_compute():
    run(
        "bio/sourmash/compute/",
        [
            "snakemake",
            "--cores",
            "1",
            "transcriptome.sig",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile",
        ],
    )
    run(
        "bio/sourmash/compute/",
        [
            "snakemake",
            "--cores",
            "1",
            "reads.sig",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile",
        ],
    )


@pytest.mark.skip(reason="test hangs, skipping so we can see gatk test results")
@skip_if_not_modified
def test_busco():
    run(
        "bio/busco",
        [
            "snakemake",
            "--cores",
            "1",
            "txome_busco/full_table_txome_busco.tsv",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_vcftoolsfilter():
    run(
        "bio/vcftools/filter",
        ["snakemake", "--cores", "1", "sample.filtered.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_markduplicatesspark():
    run(
        "bio/gatk/markduplicatesspark",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_baserecalibrator():
    run(
        "bio/gatk/baserecalibrator",
        ["snakemake", "--cores", "1", "recal/a.grp", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_baserecalibratorspark():
    run(
        "bio/gatk/baserecalibratorspark",
        ["snakemake", "--cores", "1", "recal/a.grp", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_applybqsr():
    run(
        "bio/gatk/applybqsr",
        ["snakemake", "--cores", "1", "recal/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_haplotypecaller():
    run(
        "bio/gatk/haplotypecaller",
        ["snakemake", "--cores", "1", "calls/a.g.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_variantrecalibrator():
    def check_log(log):
        assert "USAGE" not in log

    run(
        "bio/gatk/variantrecalibrator",
        [
            "snakemake",
            "--cores",
            "1",
            "-s",
            "test.smk",
            "calls/all.recal.vcf",
            "--use-conda",
            "-F",
        ],
        check_log=check_log,
    )


@skip_if_not_modified
def test_gatk_filtermutectcalls():
    run(
        "bio/gatk/filtermutectcalls",
        ["snakemake", "--cores", "1", "calls/snvs.mutect.filtered.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_selectvariants():
    run(
        "bio/gatk/selectvariants",
        ["snakemake", "--cores", "1", "calls/snvs.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_variantfiltration():
    run(
        "bio/gatk/variantfiltration",
        ["snakemake", "--cores", "1", "calls/snvs.filtered.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_varianteval():
    run(
        "bio/gatk/varianteval",
        ["snakemake", "--cores", "1", "snvs.varianteval.grp", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_genotypegvcfs():
    run(
        "bio/gatk/genotypegvcfs",
        ["snakemake", "--cores", "1", "calls/all.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_genomicsdbimport():
    run(
        "bio/gatk/genomicsdbimport",
        ["snakemake", "--cores", "1", "db", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_combinegvcfs():
    run(
        "bio/gatk/combinegvcfs",
        ["snakemake", "--cores", "1", "calls/all.g.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_splitncigarreads():
    run(
        "bio/gatk/splitncigarreads",
        ["snakemake", "--cores", "1", "split/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_mergevcfs():
    run(
        "bio/picard/mergevcfs",
        ["snakemake", "--cores", "1", "snvs.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_igv_reports():
    run(
        "bio/igv-reports",
        ["snakemake", "--cores", "1", "igv-report.html", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_strelka_somatic():
    run(
        "bio/strelka/somatic",
        ["snakemake", "--cores", "1", "a_vcf", "--use-conda", "-F", "-j 2"],
    )


@skip_if_not_modified
def test_gatk_mutect():
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_mutect_bam():
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant_bam/a.vcf", "variant_bam/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vardict_single_mode():
    run(
        "bio/vardict",
        ["snakemake", "--cores", "1", "vcf/a.s.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vardict_paired_mode():
    run(
        "bio/vardict",
        ["snakemake", "--cores", "1", "vcf/a.tn.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_varscan_mpileup2indel():
    run(
        "bio/varscan/mpileup2indel",
        ["snakemake", "--cores", "1", "vcf/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_varscan_mpileup2snp():
    run(
        "bio/varscan/mpileup2snp",
        ["snakemake", "--cores", "1", "vcf/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_varscan_somatic():
    run(
        "bio/varscan/somatic",
        ["snakemake", "--cores", "1", "vcf/a.snp.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_umis_bamtag():
    run(
        "bio/umis/bamtag",
        ["snakemake", "--cores", "1", "data/a.annotated.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_transdecoder_longorfs():
    run(
        "bio/transdecoder/longorfs",
        [
            "snakemake",
            "--cores",
            "1",
            "test.fa.transdecoder_dir/longest_orfs.pep",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_transdecoder_predict():
    run(
        "bio/transdecoder/predict",
        ["snakemake", "--cores", "1", "test.fa.transdecoder.gff3", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_lastdb_nucl():
    run(
        "bio/last/lastdb",
        ["snakemake", "--cores", "1", "test-transcript.fa.prj", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_lastdb_prot():
    run(
        "bio/last/lastdb",
        ["snakemake", "--cores", "1", "test-protein.fa.prj", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_lastal_nucl():
    run(
        "bio/last/lastal",
        ["snakemake", "--cores", "1", "test-transcript.maf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_lastal_prot():
    run(
        "bio/last/lastal",
        ["snakemake", "--cores", "1", "test-tr-x-prot.maf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pear():
    run(
        "bio/pear",
        [
            "snakemake",
            "--cores",
            "1",
            "pear/reads_pear_assembled.fq.gz",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_plass_paired():
    run(
        "bio/plass",
        ["snakemake", "--cores", "1", "plass/prot.fasta", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_plass_single():
    run(
        "bio/plass",
        ["snakemake", "--cores", "1", "plass/prot_single.fasta", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_refgenie():
    try:
        shutil.copytree("bio/refgenie/test/genome_folder", "/tmp/genome_folder")
    except FileExistsError:
        # no worries, the directory is already there
        pass
    os.environ["REFGENIE"] = "/tmp/genome_folder/genome_config.yaml"
    run("bio/refgenie", ["snakemake", "--cores", "1", "--use-conda", "-F"])


@skip_if_not_modified
def test_hmmbuild():
    run(
        "bio/hmmer/hmmbuild",
        ["snakemake", "--cores", "1", "test-profile.hmm", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_hmmpress():
    run(
        "bio/hmmer/hmmpress",
        ["snakemake", "--cores", "1", "test-profile.hmm.h3f", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_hmmscan():
    run(
        "bio/hmmer/hmmscan",
        ["snakemake", "--cores", "1", "test-prot-tbl.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_hmmsearch():
    run(
        "bio/hmmer/hmmsearch",
        ["snakemake", "--cores", "1", "test-prot-tbl.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_paladin_index():
    run(
        "bio/paladin/index",
        ["snakemake", "--cores", "1", "index/prot.fasta.bwt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_paladin_prepare():
    run(
        "bio/paladin/prepare",
        ["snakemake", "--cores", "1", "uniprot_sprot.fasta.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_paladin_align():
    run(
        "bio/paladin/align",
        ["snakemake", "--cores", "1", "paladin_mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ucsc_bedgraphtobigwig():
    run(
        "bio/ucsc/bedGraphToBigWig",
        ["snakemake", "--cores", "1", "a.bw", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ucsc_fatotwobit():
    run(
        "bio/ucsc/faToTwoBit",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.2bit",
            "genome_gz.2bit",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_ucsc_twobitinfo():
    run(
        "bio/ucsc/twoBitInfo",
        ["snakemake", "--cores", "1", "genome.chrom.sizes", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ucsc_twobittofa():
    run(
        "bio/ucsc/twoBitToFa",
        ["snakemake", "--cores", "1", "genome.fa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_sequence():
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_sequence_old_release():
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "-s", "old_release.smk", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_sequence_chromosome():
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "refs/chr1.fasta", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_sequence_chromosome_old_release():
    run(
        "bio/reference/ensembl-sequence",
        [
            "snakemake",
            "-s",
            "old_release.smk",
            "--cores",
            "1",
            "refs/old_release.chr1.fasta",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_ensembl_annotation():
    run(
        "bio/reference/ensembl-annotation",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_variation():
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_variation_old_release():
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "old_release.smk", "--cores", "1", "--use-conda", "-F"],
    )


@pytest.mark.skip(reason="needs too much time")
@skip_if_not_modified
def test_ensembl_variation_grch37():
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "grch37.smk", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_variation_with_contig_lengths():
    run(
        "bio/reference/ensembl-variation",
        [
            "snakemake",
            "--cores",
            "1",
            "--snakefile",
            "with_fai.smk",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_infernal_cmpress():
    run(
        "bio/infernal/cmpress",
        [
            "snakemake",
            "--cores",
            "1",
            "test-covariance-model.cm.i1f",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_infernal_cmscan():
    run(
        "bio/infernal/cmscan",
        ["snakemake", "--cores", "1", "tr-infernal-tblout.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bismark_genome_preparation():
    run(
        "bio/bismark/bismark_genome_preparation",
        [
            "snakemake",
            "--cores",
            "1",
            "indexes/genome/Bisulfite_Genome",
            "indexes/genome_gz/Bisulfite_Genome",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_genome_bam2nuc():
    run(
        "bio/bismark/bam2nuc",
        [
            "snakemake",
            "--cores",
            "1",
            "indexes/genome/genomic_nucleotide_frequencies.txt",
            "bams/b_genome.nucleotide_stats.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_bismark():
    run(
        "bio/bismark/bismark",
        [
            "snakemake",
            "--cores",
            "1",
            "bams/a_genome_pe.bam",
            "bams/b_genome.bam",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_deduplicate_bismark():
    run(
        "bio/bismark/deduplicate_bismark",
        [
            "snakemake",
            "--cores",
            "1",
            "bams/a_genome_pe.deduplicated.bam",
            "bams/b_genome.deduplicated.bam",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_bismark_methylation_extractor():
    run(
        "bio/bismark/bismark_methylation_extractor",
        [
            "snakemake",
            "--cores",
            "1",
            "meth_cpg/a_genome_pe.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.bismark.cov.gz",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_bismark2report():
    run(
        "bio/bismark/bismark2report",
        [
            "snakemake",
            "--cores",
            "1",
            "qc/meth/a_genome.bismark2report.html",
            "qc/meth/b_genome.bismark2report.html",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_bismark2summary():
    run(
        "bio/bismark/bismark2summary",
        [
            "snakemake",
            "--cores",
            "1",
            "qc/experiment.bismark2summary.html",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bismark_bismark2bedgraph():
    run(
        "bio/bismark/bismark2bedGraph",
        [
            "snakemake",
            "--cores",
            "1",
            "meth_cpg/a_genome_pe.deduplicated_CpG.bismark.cov.gz",
            "meth_non_cpg/a_genome_pe.deduplicated_non_cpg.bismark.cov.gz",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_tabix():
    run(
        "bio/tabix",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "test.vcf.gz.tbi"],
    )


@skip_if_not_modified
def test_msisensor_scan():
    run(
        "bio/msisensor/scan",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "microsat.list"],
    )


@skip_if_not_modified
def test_msisensor_msi():
    run(
        "bio/msisensor/msi",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "example.msi"],
    )


@skip_if_not_modified
def test_tximport():
    run("bio/tximport", ["snakemake", "--cores", "1", "txi.RDS", "--use-conda", "-F"])


@skip_if_not_modified
def test_fasterq_dump():
    run(
        "bio/sra-tools/fasterq-dump",
        ["snakemake", "--cores", "1", "data/ERR267986.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_mem_samblaster():
    run(
        "bio/bwa/mem-samblaster",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bwa_mem2_samblaster():
    run(
        "bio/bwa-mem2/mem-samblaster",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpsift_genesets():
    run(
        "bio/snpsift/genesets",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpsift_vartype():
    run(
        "bio/snpsift/varType",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpsift_gwascat():
    run(
        "bio/snpsift/gwascat",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ptrimmer_se():
    run(
        "bio/ptrimmer",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ptrimmer_se"],
    )


@skip_if_not_modified
def test_ptrimmer_pe():
    run(
        "bio/ptrimmer",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ptrimmer_pe"],
    )


@skip_if_not_modified
def test_vep_cache():
    run(
        "bio/vep/cache",
        ["snakemake", "--cores", "1", "resources/vep/cache", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vep_plugins():
    run(
        "bio/vep/plugins",
        ["snakemake", "--cores", "1", "resources/vep/plugins", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vep_annotate():
    run(
        "bio/vep/annotate",
        ["snakemake", "--cores", "1", "variants.annotated.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_genomepy():
    # download dm3 genome (relatively small, +/- 250 mb)
    run(
        "bio/genomepy",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "dm3/dm3.fa"],
    )


@skip_if_not_modified
def test_chm_eval_sample():
    run(
        "bio/benchmark/chm-eval-sample",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_chm_eval_kit():
    run(
        "bio/benchmark/chm-eval-kit", ["snakemake", "--cores", "1", "--use-conda", "-F"]
    )


@skip_if_not_modified
def test_chm_eval_eval():
    run(
        "bio/benchmark/chm-eval",
        ["snakemake", "--cores", "1", "--use-conda", "chm-eval/calls.summary"],
    )


@skip_if_not_modified
def test_snpsift_dbnsfp():
    run(
        "bio/snpsift/dbnsfp",
        ["snakemake", "--cores", "1", "out.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_snpsift_annotate():
    run(
        "bio/snpsift/annotate",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )

@skip_if_not_modified
def test_unicycler():
    run(
        "bio/unicycler",
        [
            "snakemake",
            "--cores",
            "1",
            "result/reads/assembly.fasta",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_vg_construct():
    run(
        "bio/vg/construct",
        ["snakemake", "--cores", "1", "graph/c.vg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_merge():
    run(
        "bio/vg/merge",
        ["snakemake", "--cores", "1", "graph/wg.vg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_ids():
    run(
        "bio/vg/ids",
        ["snakemake", "--cores", "1", "graph/c_mod.vg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_index_gcsa():
    run(
        "bio/vg/index/gcsa",
        ["snakemake", "--cores", "1", "index/wg.gcsa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_index_xg():
    run(
        "bio/vg/index/xg",
        ["snakemake", "--cores", "1", "index/x.xg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_kmers():
    run(
        "bio/vg/kmers",
        ["snakemake", "--cores", "1", "kmers/c.kmers", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_prune():
    run(
        "bio/vg/prune",
        ["snakemake", "--cores", "1", "graph/c.pruned.vg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_vg_sim():
    run("bio/vg/sim", ["snakemake", "--cores", "1", "reads/x.seq", "--use-conda", "-F"])


@skip_if_not_modified
def test_wgsim():
    run(
        "bio/wgsim",
        ["snakemake", "--cores", "1", "reads/1.fq", "reads/2.fq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_diamond_blastx():
    run(
        "bio/diamond/makedb",
        ["snakemake", "--cores", "1", "foo.dmnd", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_diamond_blastx():
    run(
        "bio/diamond/blastx",
        ["snakemake", "--cores", "1", "foo.tsv.gz", "--use-conda", "-F"],
    )
