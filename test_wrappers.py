import difflib
from pathlib import Path
import subprocess
import os
import tempfile
import shutil
import pytest
import sys
import yaml
import filecmp
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


@pytest.fixture
def tmp_test_dir():
    with tempfile.TemporaryDirectory() as d:
        yield d

        # cleanup environments to save disk space
        subprocess.check_call(
            f"for env in `conda env list | grep -P '{d}' | "
            "cut -f1 | tr -d ' '`; do conda env remove --yes --prefix $env; done",
            shell=True,
        )


@pytest.fixture
def run(tmp_test_dir):
    def _run(wrapper, cmd, check_log=None, compare_results_with_expected=None):
        wrapper_dir = Path(wrapper)

        is_meta_wrapper = wrapper.startswith("meta/")

        tmp_test_subdir = Path(tempfile.mkdtemp(dir=tmp_test_dir))
        origdir = os.getcwd()

        meta_path = os.path.join(wrapper, "meta.yaml")
        try:
            with open(meta_path) as f:
                meta = yaml.load(f, Loader=yaml.BaseLoader)
        except Exception:
            raise ValueError(f"Unable to load or parse {meta_path}.")

        if meta.get("blacklisted"):
            pytest.skip("wrapper blacklisted")

        dst = tmp_test_subdir / "master"

        os.symlink(origdir, dst)

        used_wrappers = []
        wrapper_file = "used_wrappers.yaml"
        if os.path.exists(os.path.join(wrapper, wrapper_file)):
            # is meta wrapper
            with open(os.path.join(wrapper, wrapper_file), "r") as wf:
                wf = yaml.load(wf, Loader=yaml.BaseLoader)
                used_wrappers = wf["wrappers"]
        else:
            used_wrappers.append(wrapper)

        if (DIFF_MASTER or DIFF_LAST_COMMIT) and not any(
            any(f.startswith(w) for f in DIFF_FILES)
            for w in chain(used_wrappers, [wrapper])
        ):
            pytest.skip("wrappers not modified")

        testdir = tmp_test_subdir / "test"

        if is_meta_wrapper:
            # make sure that the meta-wrapper is where we expect it
            for path in wrapper_dir.iterdir():
                if path.is_dir():
                    shutil.copytree(path, tmp_test_subdir / path.name)
                else:
                    shutil.copy(path, tmp_test_subdir)
        else:
            shutil.copytree(wrapper_dir / "test", testdir)

        # switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd += [
            "--conda-cleanup-pkgs",
            "--printshellcmds",
            "--show-failed-logs",
        ]
        if not is_meta_wrapper:
            # meta-wrappers define their specific wrapper versions
            cmd += [
                "--wrapper-prefix",
                f"file://{tmp_test_subdir}/",
            ]


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

        try:
            subprocess.check_call(cmd)
            if compare_results_with_expected:
                for generated, expected in compare_results_with_expected.items():
                    if not filecmp.cmp(generated, expected, shallow=False):
                        with open(generated) as genf, open(expected) as expf:
                            gen_lines = genf.readlines()
                            exp_lines = expf.readlines()
                        diff = "".join(
                            difflib.Differ().compare(gen_lines, exp_lines)
                        )
                        raise ValueError(
                            f"Unexpected results: {generated} != {expected}."
                            f"Diff:\n{diff}"
                        )
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
        return tmp_test_subdir

    return _run


def test_aria2c(run):
    run(
        "utils/aria2c",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "results/file.fas.gz",
            "results/file.md5.fas.gz",
            "results/file.md5file.fas.gz",
            "results/file.sha1file.fas.gz",
            "results/file.sha224file.fas.gz",
            "results/file.sha256file.fas.gz",
            "results/file.sha384file.fas.gz",
            "results/file.sha512file.fas.gz",
            "results/file.md5fileH.fas.gz",
        ],
    )


def test_agat(run):
    run(
        "bio/agat",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "agat_config.yaml",
            "agat_levels.yaml",
            "test_agat_convert_bed2gff.gff",
            "test_agat_convert_embl2gff.gff",
            "test_agat_convert_genscan2gff.gff",
            "test_agat_convert_mfannot2gff.gff",
            "test_agat_convert_minimap2_bam2gff_bam.gff",
            "test_agat_convert_minimap2_bam2gff_sam.gff",
            "test_agat_convert_sp_gff2bed.bed",
            "test_agat_convert_sp_gff2gtf.gtf",
            "test_agat_convert_sp_gff2tsv.tsv",
            "test_agat_convert_sp_gff2zff.dna",
            "test_agat_convert_sp_gxf2gxf.gff",
            "test_agat_sp_Prokka_inferNameFromAttributes.gff",
            "test_agat_sp_add_intergenic_regions.gff",
            "test_agat_sp_add_introns.gff",
            "test_agat_sp_add_splice_sites.gff",
            "test_agat_sp_add_start_and_stop.gff",
            "test_agat_sp_alignment_output_style.gff",
            "test_agat_sp_clipN_seqExtremities_and_fixCoordinates.gff",
            "test_agat_sp_compare_two_annotations",
            "test_agat_sp_complement_annotations.gff",
            "test_agat_sp_ensembl_output_style.gff",
            "test_agat_sp_extract_attributes_ID.txt",
            "test_agat_sp_extract_sequences.fasta",
            "test_agat_sp_filter_by_ORF_size_matched.gff",
            "test_agat_sp_filter_by_locus_distance.gff",
            "test_agat_sp_filter_feature_by_attribute_presence.gff",
            "test_agat_sp_filter_feature_by_attribute_value.gff",
            "test_agat_sp_filter_feature_from_keep_list.gff",
            "test_agat_sp_filter_feature_from_kill_list.gff",
            "test_agat_sp_filter_gene_by_intron_numbers.gff",
            "test_agat_sp_filter_gene_by_length.gff",
            "test_agat_sp_filter_incomplete_gene_coding_models.gff",
            "test_agat_sp_filter_record_by_coordinates",
            "test_agat_sp_fix_cds_phases.gff",
            "test_agat_sp_fix_features_locations_duplicated.gff",
            "test_agat_sp_fix_fusion_all.gff",
            "test_agat_sp_fix_longest_ORF_all.gff",
            "test_agat_sp_fix_overlaping_genes.gff",
            "test_agat_sp_fix_small_exon_from_extremities.gff",
            "test_agat_sp_flag_premature_stop_codons.gff",
            "test_agat_sp_flag_short_introns.gff",
            "test_agat_sp_functional_statistics",
            "test_agat_sp_keep_longest_isoform.gff",
            "test_agat_sp_kraken_assess_liftover.gff",
            "test_agat_sp_list_short_introns.gff",
            "test_agat_sp_manage_IDs.gff",
            "test_agat_sp_manage_UTRs_report.txt",
            "test_agat_sp_manage_attributes.gff",
            "test_agat_sp_manage_functional_annotation.gff",
            "test_agat_sp_manage_introns_report.txt",
            "test_agat_sp_merge_annotations.gff",
            "test_agat_sp_move_attributes_within_records.gff",
            "test_agat_sp_prokka_fix_fragmented_gene_annotations",
            "test_agat_sp_sensitivity_specificity.txt",
            "test_agat_sp_separate_by_record_type",
            "test_agat_sp_statistics.txt",
            "test_agat_sq_add_attributes_from_tsv.gff",
            "test_agat_sq_add_hash_tag.gff",
            "test_agat_sq_add_locus_tag.gff",
            "test_agat_sq_filter_feature_from_fasta.gff",
            "test_agat_sq_list_attributes.txt",
            "test_agat_sq_manage_IDs.txt",
            "test_agat_sq_manage_attributes.gff",
            "test_agat_sq_mask.gff",
            "test_agat_sq_remove_redundant_entries.gff",
            "test_agat_sq_repeats_analyzer.gff",
            "test_agat_sq_reverse_complement.gff",
            "test_agat_sq_rfam_analyzer.tsv",
        ],
    )


def test_alignoth(run):
    run(
        "bio/alignoth",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "out/json_plot.vl.json", "out/plot.html", "output-dir/"],
    )

def test_alignoth_report_meta(run):
    run(
        "meta/bio/alignoth_report",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/datavzrd-report/NA12878/",
        ],
    )


def test_miller(run):
    run(
        "utils/miller",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "miller/cat.tsv",
            "miller/summary.tsv",
            "miller/summary.csv",
            "miller/histogram.tsv",
            "miller/join.csv",
            "miller/sample.csv",
            "miller/grep.csv",
            "miller/cut.csv",
            "miller/sort.csv",
            "miller/split_1.csv",
            "miller/split_2.csv",
            "miller/uniq.tsv",
            "miller/pipe.tsv",
        ],
        compare_results_with_expected={
            "miller/cat.tsv": "expected/cat.tsv",
            "miller/summary.tsv": "expected/summary.tsv",
            "miller/summary.csv": "expected/summary.csv",
            "miller/histogram.tsv": "expected/histogram.tsv",
            "miller/join.csv": "expected/join.csv",
            "miller/sample.csv": "expected/sample.csv",
            "miller/grep.csv": "expected/grep.csv",
            "miller/cut.csv": "expected/cut.csv",
            "miller/sort.csv": "expected/sort.csv",
            "miller/split_1.csv": "expected/split_1.csv",
            "miller/split_2.csv": "expected/split_2.csv",
            "miller/uniq.tsv": "expected/uniq.tsv",
            "miller/pipe.tsv": "expected/pipe.tsv",
        },
    )


def test_taxonkit(run):
    run(
        "bio/taxonkit",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "out/list/a.txt",
            "out/list/a.json",
            "out/lineage/a.txt",
            "out/reformat/a.txt",
            "out/name2taxid/a.txt",
            "out/filter/a.txt",
            "out/lca/a.txt",
            "out/create-taxdump/a/taxid.map",
            "out/profile2cami/a.txt",
            "out/cami_filter/a.tsv",
        ],
    )


def test_galah(run):
    run(
        "bio/galah",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results.fas.tsv",
            "results.fas.list",
            "results.fas_list.tsv",
            "results.fas_list.list",
        ],
    )


def test_nonpareil(run):
    run(
        "bio/nonpareil/infer",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/a.fa.npo",
            "results/a.fas.bz2.npo",
            "results/a.fasta.gz.npo",
            "results/a.fq.npo",
            "results/a.fq.bz2.npo",
            "results/a.fastq.gz.npo",
        ],
    )


def test_ngsbits_samplesimilarity(run):
    run(
        "bio/ngsbits/samplesimilarity",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "similarity.tsv",
        ],
    )


def test_nonpareil_plot(run):
    run(
        "bio/nonpareil/plot",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/a.pdf",
            "results/b.pdf",
            "results/c.pdf",
            "results/a.nomodel.pdf",
            "results/b.nomodel.pdf",
            "results/c.nomodel.pdf",
            "results/samples.pdf",
        ],
    )


def test_indelqual(run):
    run(
        "bio/lofreq/indelqual",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/indelqual/a.uindel.bam",
            "out/indelqual/a.dindel.bam",
        ],
    )


def test_vsearch(run):
    run(
        "bio/vsearch",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "out/cluster_fast/a.profile",
            "out/maskfasta/a.fasta",
            "out/fastx_uniques/a.fastq",
            "out/fastx_uniques/a.fastq.gz",
            "out/fastx_uniques/a.fastq.bz2",
            "out/fastq_convert/a.fastq",
        ],
    )


def test_bbtools_pe(run):
    run(
        "bio/bbtools",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
        ],
    )


def test_bbtools_se(run):
    run(
        "bio/bbtools",
        [
            "snakemake",
            "--cores",
            "2",
            "--config",
            "reads_are_paired=False",
            "--use-conda",
            "-F",
        ],
    )


def test_seqkit_stats(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/stats/a.tsv",
        ],
    )


def test_seqkit_rmdup(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/rmdup/name/a.fastq.gz",
        ],
    )
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/rmdup/seq/a.fastq.gz",
        ],
    )


def test_gffread_gtf(run):
    run(
        "bio/gffread",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "transcripts.fa"],
    )


def test_gffread_gff(run):
    run(
        "bio/gffread",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "proteins.fa"],
    )


def test_seqkit_fx2tab(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/fx2tab/a.tsv",
        ],
    )


def test_seqkit_grep(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/grep/name/a.fastq.gz",
        ],
    )
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/grep/seq/a.fastq.gz",
        ],
    )


def test_seqkit_subseq(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/subseq/bed/a.fa.gz",
        ],
    )
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/subseq/gtf/a.fa.gz",
        ],
    )
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/subseq/region/a.fa.gz",
        ],
    )


def test_seqkit_seq(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/seq/a.fa.gz",
        ],
    )


def test_seqkit_common(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/common/a_b.fa.gz",
        ],
    )


def test_seqkit_concat(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/concat/a_b.fa.gz",
        ],
    )


def test_seqkit_split2_part(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/split2/part/a.1-of-2.fas",
            "out/split2/part/a.2-of-2.fas",
        ],
    )


def test_sickle_pe(run):
    run(
        "bio/sickle/pe",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "a.1.fastq",
            "a.2.fastq",
            "a.single.fastq",
        ],
    )


def test_sickle_se(run):
    run(
        "bio/sickle/se",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "a.1.fastq",
        ],
    )


def test_bwameth_mem(run):
    run(
        "bio/bwameth/memx",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "A.mem.bam",
        ],
    )
    run(
        "bio/bwameth/memx",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "A.mem2.bam",
        ],
    )
    run(
        "bio/bwameth/memx",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "A.picard_sort.bam",
        ],
    )
    run(
        "bio/bwameth/memx",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "A.samtools_sort.bam",
        ],
    )


def test_bwameth_index(run):
    run(
        "bio/bwameth/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "genome.fasta.bwameth.c2t.sa",
        ],
    )
    run(
        "bio/bwameth/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "genome.fasta.bwameth.c2t.0123",
        ],
    )


def test_bwa_memx_index(run):
    run(
        "bio/bwa-memx/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "genome.fasta.sa",
        ],
    )
    run(
        "bio/bwa-memx/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "genome.fasta.bwt.2bit.64",
        ],
    )
    run(
        "bio/bwa-memx/index",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "genome.fasta.pos_packed",
        ],
    )


def test_bwa_memx_mem(run):
    run(
        "bio/bwa-memx/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "bwa_memx_test",
        ],
    )


def test_purge_dups_calcuts(run):
    run(
        "bio/purge_dups/calcuts",
        ["snakemake", "--cores", "1", "out/calcuts.cutoffs", "--use-conda", "-F"],
    )


def test_purge_dups_get_seqs(run):
    run(
        "bio/purge_dups/get_seqs",
        ["snakemake", "--cores", "1", "out/get_seqs.hap.fasta", "--use-conda", "-F"],
    )


def test_ngscheckmate_makesnvpattern(run):
    run(
        "bio/ngscheckmate/makesnvpattern",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "genome.pt"],
    )


def test_purge_dups_ngscstat(run):
    run(
        "bio/purge_dups/ngscstat",
        ["snakemake", "--cores", "1", "out/ngscstat.cov", "--use-conda", "-F"],
    )


def test_purge_dups_pbcstat(run):
    run(
        "bio/purge_dups/pbcstat",
        ["snakemake", "--cores", "1", "out/pbcstat.cov", "--use-conda", "-F"],
    )


def test_purge_dups_purge_dups(run):
    run(
        "bio/purge_dups/purge_dups",
        ["snakemake", "--cores", "1", "out/purge_dups.bed", "--use-conda", "-F"],
    )


def test_purge_dups_split_fa(run):
    run(
        "bio/purge_dups/split_fa",
        ["snakemake", "--cores", "1", "out/genome.split", "--use-conda", "-F"],
    )


def test_quast(run):
    run(
        "bio/quast",
        ["snakemake", "--cores", "1", "a/treport.tsv", "--use-conda", "-F"],
    )


def test_gfatools(run):
    run("bio/gfatools", ["snakemake", "--cores", "1", "a.stat", "--use-conda", "-F"])

    run("bio/gfatools", ["snakemake", "--cores", "1", "a.fas", "--use-conda", "-F"])

    run("bio/gfatools", ["snakemake", "--cores", "1", "a.bed", "--use-conda", "-F"])

    run(
        "bio/gfatools",
        ["snakemake", "--cores", "1", "a.blacklist", "--use-conda", "-F"],
    )

    run("bio/gfatools", ["snakemake", "--cores", "1", "a.bubble", "--use-conda", "-F"])

    run("bio/gfatools", ["snakemake", "--cores", "1", "a.asm", "--use-conda", "-F"])

    run("bio/gfatools", ["snakemake", "--cores", "1", "a.sql", "--use-conda", "-F"])


def test_hifiasm(run):
    run(
        "bio/hifiasm",
        ["snakemake", "--cores", "2", "hifiasm/a.a_ctg.gfa", "--use-conda", "-F"],
    )


def meryl_count(run):
    run(
        "bio/meryl/count",
        ["snakemake", "--cores", "2", "genome", "--use-conda", "-F"],
    )


def meryl_sets(run):
    run(
        "bio/meryl/sets",
        ["snakemake", "--cores", "1", "genome_union", "--use-conda", "-F"],
    )

    run(
        "bio/meryl/sets",
        ["snakemake", "--cores", "1", "genome_intersect", "--use-conda", "-F"],
    )

    run(
        "bio/meryl/sets",
        ["snakemake", "--cores", "1", "genome_subtract", "--use-conda", "-F"],
    )

    run(
        "bio/meryl/sets",
        ["snakemake", "--cores", "1", "genome_difference", "--use-conda", "-F"],
    )


def meryl_union(run):
    run(
        "bio/meryl/stats",
        ["snakemake", "--cores", "1", "genome.stats", "--use-conda", "-F"],
    )


def test_genomescope(run):
    run(
        "bio/genomescope",
        ["snakemake", "--cores", "1", "a/model.txt", "--use-conda", "-F"],
    )


def test_bellerophon(run):
    run(
        "bio/bellerophon",
        ["snakemake", "--cores", "2", "out.sam", "--use-conda", "-F"],
    )

    run(
        "bio/bellerophon",
        ["snakemake", "--cores", "2", "out.bam", "--use-conda", "-F"],
    )


def test_pretext_map(run):
    run(
        "bio/pretext/map",
        ["snakemake", "--cores", "1", "map.pretext", "--use-conda", "-F"],
    )


def test_pretext_snapshot(run):
    run(
        "bio/pretext/snapshot",
        ["snakemake", "--cores", "1", "full_map.png", "--use-conda", "-F"],
    )

    run(
        "bio/pretext/snapshot",
        ["snakemake", "--cores", "1", "full_map.jpg", "--use-conda", "-F"],
    )


def test_pretext_graph(run):
    run(
        "bio/pretext/graph",
        ["snakemake", "--cores", "1", "a.pretext", "--use-conda", "-F"],
    )


def test_salsa2(run):
    run(
        "bio/salsa2",
        ["snakemake", "--cores", "1", "out/a.agp", "--use-conda", "-F"],
    )


def test_merqury_haploid(run):
    run(
        "bio/merqury",
        ["snakemake", "--cores", "1", "results/haploid/out.qv", "--use-conda", "-F"],
    )


def test_merqury_diploid(run):
    run(
        "bio/merqury",
        ["snakemake", "--cores", "1", "results/diploid/out.qv", "--use-conda", "-F"],
    )


def test_mashmap(run):
    run(
        "bio/mashmap", ["snakemake", "--cores", "2", "mashmap.out", "--use-conda", "-F"]
    )

    run(
        "bio/mashmap",
        [
            "snakemake",
            "--cores",
            "2",
            "mashmap.out",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_reflist.smk",
        ],
    )


def test_rbt_csvreport(run):
    run(
        "bio/rbt/csvreport",
        ["snakemake", "--cores", "1", "qc_data", "--use-conda", "-F"],
    )


def test_liftoff(run):
    run(
        "bio/liftoff",
        [
            "snakemake",
            "--cores",
            "1",
            "genome_annotation_genome.gff3",
            "--use-conda",
            "-F",
        ],
    )


def test_biobambam2_bamsormadup(run):
    run(
        "bio/biobambam2/bamsormadup",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


def test_bustools_text(run):
    run(
        "bio/bustools/text",
        ["snakemake", "--cores", "1", "file.tsv", "--use-conda", "-F"],
    )
    run(
        "bio/bustools/text",
        ["snakemake", "--cores", "1", "file2.tsv", "--use-conda", "-F"],
    )


def test_open_cravat_run(run):
    run(
        "bio/open-cravat/run",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


def test_bustools_count(run):
    run(
        "bio/bustools/count",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "buscount.mtx"],
    )


def test_bustools_sort(run):
    run(
        "bio/bustools/sort",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "sorted.bus"],
    )


def test_open_cravat_module(run):
    run(
        "bio/open-cravat/module",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


def test_vcf2maf_vcf2vcf(run):
    run(
        "bio/vcf2maf/vcf2vcf",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "corrected.vcf",
        ],
    )


def test_varscan2_snpeff_meta(run):
    run(
        "meta/bio/varscan2_snpeff",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "snpeff/annotated.vcf",
        ],
    )


def test_vcf2maf(run):
    run(
        "bio/vcf2maf/vcf2maf",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "small.maf",
        ],
    )


def test_salmon_tximport_meta(run):
    run(
        "meta/bio/salmon_tximport",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "tximport/SummarizedExperimentObject.RDS",
        ],
    )


def test_dada2_se_meta(run):
    run(
        "meta/bio/dada2_se",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
        ],
    )


def test_adapterremoval_pe(run):
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


def test_adapterremoval_se(run):
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


def test_dada2_pe_meta(run):
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


def test_mapdamage2(run):
    run(
        "bio/mapdamage2",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/rescale/a.bam",
            "results/all/a.bam",
        ],
    )


def test_microphaser_normal(run):
    run(
        "bio/microphaser/normal",
        ["snakemake", "--cores", "1", "out/a.fasta", "--use-conda", "-F"],
    )


def test_microphaser_somatic(run):
    run(
        "bio/microphaser/somatic",
        ["snakemake", "--cores", "1", "out/a.info.tsv", "--use-conda", "-F"],
    )


def test_microphaser_build_reference(run):
    run(
        "bio/microphaser/build_reference",
        ["snakemake", "--cores", "1", "out/peptides.bin", "--use-conda", "-F"],
    )


def test_microphaser_filter(run):
    run(
        "bio/microphaser/filter",
        ["snakemake", "--cores", "1", "out/peptides.wt.fasta", "--use-conda", "-F"],
    )


def test_dada2_quality_profile_se(run):
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


def test_dada2_quality_profile_pe(run):
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


def test_dada2_filter_trim_se(run):
    run(
        "bio/dada2/filter-trim",
        ["snakemake", "--cores", "1", "filtered-se/a.1.fastq.gz", "--use-conda", "-F"],
    )


def test_dada2_filter_trim_pe(run):
    run(
        "bio/dada2/filter-trim",
        ["snakemake", "--cores", "1", "filtered-pe/a.1.fastq.gz", "--use-conda", "-F"],
    )


def test_dada2_dereplicate_fastq(run):
    run(
        "bio/dada2/dereplicate-fastq",
        ["snakemake", "--cores", "1", "--use-conda", "uniques/a.1.RDS"],
    )


def test_dada2_learn_errors(run):
    run(
        "bio/dada2/learn-errors",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/model_1.RDS"],
    )


def test_dada2_sample_inference(run):
    run(
        "bio/dada2/sample-inference",
        ["snakemake", "--cores", "1", "--use-conda", "denoised/a.1.RDS"],
    )


def test_dada2_merge_pairs(run):
    run(
        "bio/dada2/merge-pairs",
        ["snakemake", "--cores", "1", "--use-conda", "merged/a.RDS", "-F"],
    )


def test_dada2_make_table_se(run):
    run(
        "bio/dada2/make-table",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab-se.RDS"],
    )


def test_dada2_make_table_pe(run):
    run(
        "bio/dada2/make-table",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab-pe.RDS"],
    )


def test_dada2_remove_chimeras(run):
    run(
        "bio/dada2/remove-chimeras",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/seqTab.nochim.RDS"],
    )


def test_dada2_collapse_nomismatch(run):
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


def test_dada2_assign_taxonomy(run):
    run(
        "bio/dada2/assign-taxonomy",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/taxa.RDS"],
    )


def test_dada2_assign_species(run):
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


def test_dada2_add_species(run):
    run(
        "bio/dada2/add-species",
        ["snakemake", "--cores", "1", "--use-conda", "results/dada2/taxa-sp.RDS"],
    )


def test_datavzrd(run):
    run(
        "utils/datavzrd",
        ["snakemake", "--cores", "1", "--use-conda", "results/datavzrd-report/A"],
    )


def test_deseq2_deseqdataset(run):
    # from HTSeqcount / Featurecount
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_htseq.RDS"],
    )

    # DDS import
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_minimal.RDS"],
    )

    # txi import
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_txi.RDS"],
    )

    # SE import
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_se.RDS"],
    )

    # R matrix import
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_rmatrix.RDS"],
    )

    # text matrix import
    run(
        "bio/deseq2/deseqdataset",
        ["snakemake", "--cores", "1", "--use-conda", "dds_matrix.RDS"],
    )


def test_deseq2_wald(run):
    run(
        "bio/deseq2/wald",
        ["snakemake", "--cores", "1", "--use-conda", "dge_normal.tsv"],
    )

    run("bio/deseq2/wald", ["snakemake", "--cores", "1", "--use-conda", "dge_ashr.tsv"])

    run(
        "bio/deseq2/wald",
        ["snakemake", "--cores", "1", "--use-conda", "dge_apeglm.tsv"],
    )

    run("bio/deseq2/wald", ["snakemake", "--cores", "1", "--use-conda", "dge_2f.tsv"])

    run("bio/deseq2/wald", ["snakemake", "--cores", "1", "--use-conda", "dge_1s.tsv"])


def test_arriba_star_meta(run):
    run(
        "meta/bio/star_arriba",
        ["snakemake", "results/arriba/a.fusions.tsv", "--cores", "1", "--sdm", "conda"],
    )


def test_csvtk(run):
    run(
        "utils/csvtk",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "csvtk/cat.csv",
            "csvtk/summary_tsv.csv",
            "csvtk/summary_csv.csv",
            "csvtk/frequency.csv",
            "csvtk/headers.csv",
            "csvtk/join.csv",
            "csvtk/sample.csv",
            "csvtk/grep.csv",
            "csvtk/cut.csv",
            "csvtk/sort.csv",
            "csvtk/split",
            "csvtk/stats.txt",
            "csvtk/uniq.txt",
        ],
        compare_results_with_expected={
            "csvtk/cat.csv": "expected/cat.csv",
            "csvtk/summary_tsv.csv": "expected/summary_tsv.csv",
            "csvtk/summary_csv.csv": "expected/summary_csv.csv",
            "csvtk/frequency.csv": "expected/frequency.csv",
            "csvtk/headers.csv": "csvtk/headers.csv",
            "csvtk/join.csv": "expected/join.csv",
            "csvtk/sample.csv": "expected/sample.csv",
            "csvtk/grep.csv": "expected/grep.csv",
            "csvtk/cut.csv": "expected/cut.csv",
            "csvtk/sort.csv": "expected/sort.csv",
            "csvtk/split/table-ENSG02.csv": "expected/split/table-ENSG02.csv",
            "csvtk/split/table-ENSG01.csv": "expected/split/table-ENSG01.csv",
            "csvtk/stats.txt": "expected/stats.txt",
            "csvtk/uniq.txt": "expected/uniq.txt",
        },
    )


def test_xsv(run):
    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/split/0.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/table.txt"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/stats.txt"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/split"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/sort.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/slice.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/select.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/search.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/sample.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/join.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/input.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "table.csv.idx"])

    run(
        "utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/headers_all.csv"]
    )

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/headers.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/frequency.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/fmt.tsv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/flatten.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/fixlength.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/count_csv.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/count_tsv.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/catrows.csv"])

    run("utils/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv/catcols.csv"])


def test_bwa_mapping_meta(run):
    run(
        "meta/bio/bwa_mapping",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "results/mapped/a.bam.bai",
        ],
    )


def test_cnvkit_batch_create_reference(run):
    run(
        "bio/cnvkit/batch",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "cnvkit/reference.cnn",
        ],
    )


def test_cnvkit_call(run):
    run(
        "bio/cnvkit/call",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.call.cns",
        ],
    )


def test_cnvkit_diagram(run):
    run(
        "bio/cnvkit/diagram",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.pdf",
        ],
    )
    run(
        "bio/cnvkit/diagram",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cnr.pdf",
        ],
    )
    run(
        "bio/cnvkit/diagram",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cnn.pdf",
        ],
    )
    run(
        "bio/cnvkit/diagram",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cnscnr.pdf",
        ],
    )


def test_cnvkit_antitarget(run):
    run(
        "bio/cnvkit/antitarget",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.antitarget.bed",
        ],
    )


def test_cnvkit_batch(run):
    run(
        "bio/cnvkit/batch",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "cnvkit/a.antitargetcoverage.cnn",
            "cnvkit/a.bintest.cns",
            "cnvkit/a.cnr",
            "cnvkit/a.cns",
            "cnvkit/a.call.cns",
            "cnvkit/a.targetcoverage.cnn",
        ],
    )


def test_cnvkit_target(run):
    run(
        "bio/cnvkit/target",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.target.bed",
        ],
    )


def test_cnvkit_export(run):
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.seg",
        ],
    )
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.vcf",
        ],
    )
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.vcf.gz",
        ],
    )
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.cdt",
        ],
    )
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "test.cns.jtv",
        ],
    )


def test_enhanced_volcano(run):
    run(
        "bio/enhancedvolcano",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "volcano_tsv.png",
        ],
    )

    run(
        "bio/enhancedvolcano",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "volcano_csv.svg",
        ],
    )

    run(
        "bio/enhancedvolcano",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "volcano_rds.svg",
        ],
    )


def test_goleft_indexcov(run):
    run(
        "bio/goleft/indexcov",
        ["snakemake", "--cores", "1", "--use-conda", "-Fp"],
    )


def test_gridss_call(run):
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


def test_gridss_assemble(run):
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


def test_gridss_preprocess(run):
    run(
        "bio/gridss/preprocess",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "--show-failed-logs",
            "working_dir/A.bam.gridss.working/A.bam.cigar_metrics",
            "working_dir/A.bam.gridss.working/A.bam.computesamtags.changes.tsv",
            "working_dir/A.bam.gridss.working/A.bam.coverage.blacklist.bed",
            "working_dir/A.bam.gridss.working/A.bam.idsv_metrics",
            "working_dir/A.bam.gridss.working/A.bam.insert_size_histogram.pdf",
            "working_dir/A.bam.gridss.working/A.bam.insert_size_metrics",
            "working_dir/A.bam.gridss.working/A.bam.mapq_metrics",
            "working_dir/A.bam.gridss.working/A.bam.sv.bam",
            "working_dir/A.bam.gridss.working/A.bam.sv.bam.csi",
            "working_dir/A.bam.gridss.working/A.bam.tag_metrics",
        ],
    )


def test_gridss_setupreference(run):
    run(
        "bio/gridss/setupreference",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "--show-failed-logs",
            "reference/genome.fasta.amb",
            "reference/genome.fasta.ann",
            "reference/genome.fasta.bwt",
            "reference/genome.fasta.dict",
            "reference/genome.fasta.fai",
            "reference/genome.fasta.pac",
            "reference/genome.fasta.sa",
        ],
    )


def test_strling_call(run):
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


def test_strling_merge(run):
    run(
        "bio/strling/merge",
        ["snakemake", "--cores", "1", "--use-conda", "merged/group-bounds.txt"],
    )


def test_strling_extract(run):
    run(
        "bio/strling/extract",
        ["snakemake", "--cores", "1", "--use-conda", "extract/A.bin"],
    )


def test_strling_index(run):
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


def test_vembrane_filter(run):
    run(
        "bio/vembrane/filter",
        ["snakemake", "--cores", "1", "--use-conda", "filtered/out.vcf"],
    )


def test_vembrane_table(run):
    run(
        "bio/vembrane/table",
        ["snakemake", "--cores", "1", "--use-conda", "table/out.tsv"],
    )


def test_shovill(run):
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


def test_prinseq_plus_plus(run):
    run(
        "bio/prinseq-plus-plus",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/a.fq"],
    )

    run(
        "bio/prinseq-plus-plus",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/a.fq.gz"],
    )

    run(
        "bio/prinseq-plus-plus",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/a.fasta"],
    )

    run(
        "bio/prinseq-plus-plus",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/a.fas.gz"],
    )

    run(
        "bio/prinseq-plus-plus",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/a.R1.fq.gz"],
    )


def test_seqtk(run):
    run(
        "bio/seqtk",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/fq2fas/a.fasta"],
    )

    run(
        "bio/seqtk",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/convBQ/a.fasta"],
    )

    run(
        "bio/seqtk",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/subseq_list/a.fq.gz",
        ],
    )

    run(
        "bio/seqtk",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/mergepe/a.fastq.gz",
        ],
    )

    run(
        "bio/seqtk",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/sample_se/a.fastq.gz",
        ],
    )

    run(
        "bio/seqtk",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/sample_pe/a.1.fastq.gz",
            "results/sample_pe/a.2.fastq.gz",
        ],
    )


def test_arriba(run):
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


def test_art_profiler_illumina(run):
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


def test_pyroe_id_to_name(run):
    run(
        "bio/pyroe/idtoname",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "id2name.gtf.tsv"],
    )
    run(
        "bio/pyroe/idtoname",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "id2name.gff3.tsv"],
    )


def test_pyroe_makesplicedunspliced(run):
    run(
        "bio/pyroe/makeunspliceunspliced/",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "spliceu.fa",
        ],
    )


def test_pyroe_makesplicedintronic(run):
    run(
        "bio/pyroe/makesplicedintronic",
        [
            "snakemake",
            "--cores",
            "1",
            "splici_full/spliced_intronic_sequences.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_bcftools_filter_sample(run):
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter_sample.vcf", "--use-conda", "-F"],
    )


def test_bcftools_filter_vcf(run):
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf", "--use-conda", "-F"],
    )


def test_bcftools_filter_vcf_gz(run):
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf.gz", "--use-conda", "-F"],
    )


def test_bcftools_filter_bcf(run):
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.bcf", "--use-conda", "-F"],
    )


def test_bcftools_filter_uncompressed_bcf(run):
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.uncompressed.bcf", "--use-conda", "-F"],
    )


def test_bcftools_sort(run):
    run(
        "bio/bcftools/sort",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.sorted.bcf"],
    )


def test_bcftools_call(run):
    run(
        "bio/bcftools/call",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.calls.bcf"],
    )


def test_bcftools_index(run):
    run(
        "bio/bcftools/index",
        ["snakemake", "--cores", "1", "a.bcf.csi", "--use-conda", "-F"],
    )


def test_bcftools_concat(run):
    run(
        "bio/bcftools/concat",
        ["snakemake", "--cores", "1", "all.bcf", "--use-conda", "-F"],
    )


def test_bcftools_merge(run):
    run(
        "bio/bcftools/merge",
        ["snakemake", "--cores", "1", "all.bcf", "--use-conda", "-F"],
    )


def test_bcftools_mpileup(run):
    run(
        "bio/bcftools/mpileup",
        ["snakemake", "--cores", "1", "pileups/a.pileup.bcf", "--use-conda", "-F"],
    )


def test_bcftools_reheader(run):
    run(
        "bio/bcftools/reheader",
        ["snakemake", "--cores", "1", "a.reheader.bcf", "--use-conda", "-F"],
    )
    run(
        "bio/bcftools/reheader",
        ["snakemake", "--cores", "1", "a.reheader_map.bcf", "--use-conda", "-F"],
    )


def test_bcftools_stats(run):
    run(
        "bio/bcftools/stats",
        ["snakemake", "--cores", "1", "a.bcf.stats.txt", "--use-conda", "-F"],
    )


def test_bcftools_norm(run):
    run(
        "bio/bcftools/norm",
        ["snakemake", "--cores", "1", "a.norm.vcf", "--use-conda", "-F"],
    )


def test_bcftools_view_vcf(run):
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.vcf", "--use-conda", "-F"],
    )


def test_bcftools_view_vcf_gz(run):
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.vcf.gz", "--use-conda", "-F"],
    )


def test_bcftools_view_bcf(run):
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.bcf", "--use-conda", "-F"],
    )


def test_bcftools_view_uncompressed_bcf(run):
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.uncompressed.bcf", "--use-conda", "-F"],
    )


def test_bedtools_bamtobed(run):
    run(
        "bio/bedtools/bamtobed",
        ["snakemake", "--cores", "1", "a.bed", "a.bed.gz", "--use-conda", "-F"],
    )


def test_bedtools_genomecoveragebed(run):
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


def test_bedtools_complement(run):
    run(
        "bio/bedtools/complement",
        [
            "snakemake",
            "--cores",
            "1",
            "results/bed-complement/a.complement.bed",
            "results/bed-complement/a.complement.bed.gz",
            "results/vcf-complement/a.complement.vcf",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "results/bed-complement/a.complement.bed": "expected/bed-complement/a.complement.bed",
            # "results/bed-complement/a.complement.bed.gz": "expected/bed-complement/a.complement.bed.gz",  # Disabled since filecmp does not work with gzip files
            "results/vcf-complement/a.complement.vcf": "expected/vcf-complement/a.complement.vcf",
        },
    )


def test_bedtools_sort(run):
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


def test_bedtools_split(run):
    run(
        "bio/bedtools/split",
        [
            "snakemake",
            "--cores",
            "1",
            "results/a.1-of-2.bed",
            "results/a.2-of-2.bed",
            "--use-conda",
            "-F",
        ],
    )


def test_bedtools_intersect(run):
    run(
        "bio/bedtools/intersect",
        [
            "snakemake",
            "--cores",
            "1",
            "A_B.intersected.bed",
            "A_B.intersected.bed.gz",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "A_B.intersected.bed": "expected/A_B.intersected.bed",
            # "A_B.intersected.bed.gz": "expected/A_B.intersected.bed.gz",  # Disabled since filecmp does not work with gzip files
        },
    )


def test_bedtools_merge(run):
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


def test_bedtools_merge_multi(run):
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


def test_bedtools_slop(run):
    run(
        "bio/bedtools/slop",
        ["snakemake", "--cores", "1", "A.slop.bed", "--use-conda", "-F"],
    )


def test_bgzip(run):
    run("bio/bgzip", ["snakemake", "--cores", "1", "test.vcf.gz", "--use-conda", "-F"])


def test_blast_makeblastdb_nucleotide(run):
    run(
        "bio/blast/makeblastdb",
        [
            "snakemake",
            "--cores",
            "1",
            "results/genome.fasta.ndb",
            "results/genome.fasta.nhr",
            "results/genome.fasta.nin",
            "results/genome.fasta.not",
            "results/genome.fasta.nsq",
            "results/genome.fasta.ntf",
            "results/genome.fasta.nto",
            "--use-conda",
            "-F",
        ],
    )


def test_blast_makeblastdb_protein(run):
    run(
        "bio/blast/makeblastdb",
        [
            "snakemake",
            "--cores",
            "1",
            "results/protein.fasta.pdb",
            "results/protein.fasta.phr",
            "results/protein.fasta.pin",
            "results/protein.fasta.pot",
            "results/protein.fasta.psq",
            "results/protein.fasta.ptf",
            "results/protein.fasta.pto",
            "--use-conda",
            "-F",
        ],
    )


def test_blast_blastn(run):
    run(
        "bio/blast/blastn",
        ["snakemake", "--cores", "1", "a.blast.txt", "--use-conda", "-F"],
    )


def test_bowtie2_align(run):
    run(
        "bio/bowtie2/align",
        ["snakemake", "--cores", "2", "mapped_idx/a.cram", "--use-conda", "-F"],
    )

    run(
        "bio/bowtie2/align",
        ["snakemake", "--cores", "2", "mapped_idx/a.bam", "--use-conda", "-F"],
    )

    run(
        "bio/bowtie2/align",
        ["snakemake", "--cores", "2", "mapped/a.bam", "--use-conda", "-F"],
    )

    run(
        "bio/bowtie2/align",
        ["snakemake", "--cores", "2", "mapped_se_gz/a.bam", "--use-conda", "-F"],
    )


def test_bowtie2_build(run):
    run(
        "bio/bowtie2/build",
        ["snakemake", "--cores", "1", "genome.1.bt2", "--use-conda", "-F"],
    )


def test_bowtie2_build_large(run):
    run(
        "bio/bowtie2/build",
        ["snakemake", "--cores", "1", "genome.1.bt2l", "--use-conda", "-F"],
    )


def test_bwa_mem(run):
    run(
        "bio/bwa/mem",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_samshee(run):
    run(
        "bio/samshee",
        ["snakemake", "--cores", "1", "samples.json", "--use-conda", "-F"],
    )
    run(
        "bio/samshee",
        ["snakemake", "--cores", "1", "samples.csv", "--use-conda", "-F"],
    )
    run(
        "bio/samshee",
        ["snakemake", "--cores", "1", "samples_schema.json", "--use-conda", "-F"],
    )


def test_bwa_mem_sort_samtools(run):
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


def test_bwa_mem_sort_samtools_write_index(run):
    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped_with_index_csi/a.bam",
            "mapped_with_index_csi/a.bam.csi",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )
    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped_with_index_bai/a.bam",
            "mapped_with_index_bai/a.bam.bai",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


def test_bwa_mem_sort_fgbio(run):
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
            "Snakefile_fgbio",
        ],
    )


def test_bwa_mem_sort_picard(run):
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


def test_bwa_aln(run):
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


def test_bwa_index(run):
    run(
        "bio/bwa/index",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.bwtsw.amb",
            "genome.bwtsw.ann",
            "genome.bwtsw.bwt",
            "genome.bwtsw.pac",
            "genome.bwtsw.sa",
            "--use-conda",
            "-F",
        ],
    )

    run(
        "bio/bwa/index",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.is.amb",
            "genome.is.ann",
            "genome.is.bwt",
            "genome.is.pac",
            "genome.is.sa",
            "--use-conda",
            "-F",
        ],
    )

    run(
        "bio/bwa/index",
        [
            "snakemake",
            "--cores",
            "1",
            "genome.rb2.amb",
            "genome.rb2.ann",
            "genome.rb2.bwt",
            "genome.rb2.pac",
            "genome.rb2.sa",
            "--use-conda",
            "-F",
        ],
    )


def test_bwa_samxe_sam_se(run):
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.se.sam", "--use-conda", "-F"],
    )


def test_bwa_samxe_sam_pe(run):
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.pe.sam", "--use-conda", "-F"],
    )


def test_bwa_samxe_bam_se(run):
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.se.bam", "--use-conda", "-F"],
    )


def test_bwa_samxe_bam_pe(run):
    run(
        "bio/bwa/samxe",
        ["snakemake", "--cores", "1", "mapped/a.pe.bam", "--use-conda", "-F"],
    )


def test_bwa_samxe_sam_se_sort_samtools(run):
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


def test_bwa_samxe_sam_pe_sort_samtools(run):
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


def test_bwa_samxe_bam_se_sort_samtools(run):
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


def test_bwa_samxe_bam_pe_sort_samtools(run):
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


def test_bwa_samxe_sam_se_sort_picard(run):
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


def test_bwa_samxe_sam_pe_sort_picard(run):
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


def test_bwa_samxe_bam_se_sort_picard(run):
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


def test_bwa_samxe_bam_pe_sort_picard(run):
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


def test_bwa_sampe(run):
    run(
        "bio/bwa/sampe",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_bwa_sampe_sort_samtools(run):
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


def test_bwa_sampe_sort_picard(run):
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


def test_bwa_samse(run):
    run(
        "bio/bwa/samse",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_bwa_samse_sort_samtools(run):
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


def test_bwa_samse_sort_picard(run):
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


def test_bwa_mem2_mem(run):
    run(
        "bio/bwa-mem2/mem",
        ["snakemake", "--cores", "2", "mapped/a.bam", "--use-conda", "-F"],
    )
    run(
        "bio/bwa-mem2/mem",
        ["snakemake", "--cores", "2", "mapped/a.sam", "--use-conda", "-F"],
    )


def test_bwa_mem2_sort_samtools(run):
    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "--cores",
            "2",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


def test_bwa_meme(run):
    run(
        "bio/bwa-meme/mem",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "bwa_meme_test",
        ],
    )


def test_bwa_mem2_sort_picard(run):
    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "--cores",
            "2",
            "mapped/a.bam",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_bwa_mem2_index(run):
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
            "genome.fasta.pac",
            "--use-conda",
            "-F",
        ],
    )


def test_dragmap_build(run):
    run(
        "bio/dragmap/build",
        ["snakemake", "--cores", "1", "genome/hash_table.cfg", "--use-conda", "-F"],
    )


def test_dragmap_align(run):
    run(
        "bio/dragmap/align",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_dragmap_align_sort_samtools(run):
    run(
        "bio/dragmap/align",
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


def test_dragmap_align_sort_samtools_write_index(run):
    run(
        "bio/dragmap/align",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped_with_index/a.bam",
            "mapped_with_index/a.bam.csi",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_samtools",
        ],
    )


def test_dragmap_align_sort_picard(run):
    run(
        "bio/dragmap/align",
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


def test_clustalo(run):
    run(
        "bio/clustalo",
        ["snakemake", "--cores", "1", "test.msa.fa", "--use-conda", "-F"],
    )


def test_cnv_facets(run):
    run(
        "bio/cnv_facets",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "CNV_bam.vcf.gz"],
    )
    run(
        "bio/cnv_facets",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "CNV_pileup.vcf.gz"],
    )


def test_coolpuppy(run):
    run(
        "bio/coolpuppy",
        ["snakemake", "--cores", "1", "CN_1000000.clpy", "--use-conda", "-F"],
    )


def test_cooltools_insulation(run):
    run(
        "bio/cooltools/insulation",
        ["snakemake", "--cores", "1", "CN_1000000.insulation.tsv", "--use-conda", "-F"],
    )


def test_cooltools_expected_cis(run):
    run(
        "bio/cooltools/expected_cis",
        [
            "snakemake",
            "--cores",
            "1",
            "CN_1000000.cis.expected.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_cooltools_expected_trans(run):
    run(
        "bio/cooltools/expected_trans",
        [
            "snakemake",
            "--cores",
            "1",
            "CN_1000000.trans.expected.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_cooltools_eigs_cis(run):
    run(
        "bio/cooltools/eigs_cis",
        [
            "snakemake",
            "--cores",
            "1",
            "CN_1000000.cis.vecs.tsv",
            "CN_1000000.cis.lam.tsv",
            "CN_1000000.cis.bw",
            "--use-conda",
            "-F",
        ],
    )


def test_cooltools_eigs_trans(run):
    run(
        "bio/cooltools/eigs_trans",
        [
            "snakemake",
            "--cores",
            "1",
            "CN_1000000.trans.vecs.tsv",
            "CN_1000000.trans.lam.tsv",
            "CN_1000000.trans.bw",
            "--use-conda",
            "-F",
        ],
    )


def test_cooltools_saddle(run):
    run(
        "bio/cooltools/saddle",
        ["snakemake", "--cores", "1", "CN_1000000.saddledump.npz", "--use-conda", "-F"],
    )


def test_cooltools_pileup(run):
    run(
        "bio/cooltools/pileup",
        ["snakemake", "--cores", "1", "CN_1000000.pileup.npz", "--use-conda", "-F"],
    )


def test_cooltools_dots(run):
    run(
        "bio/cooltools/dots",
        ["snakemake", "--cores", "1", "HFF_10000.dots.bedpe", "--use-conda", "-F"],
    )


def test_cooltools_genome_binnify(run):
    run(
        "bio/cooltools/genome/binnify",
        ["snakemake", "--cores", "1", "hg38_1000000_bins.bed", "--use-conda", "-F"],
    )


def test_cooltools_genome_gc(run):
    run(
        "bio/cooltools/genome/gc",
        ["snakemake", "--cores", "1", "gc_100000.tsv", "--use-conda", "-F"],
    )


def test_cutadapt_pe(run):
    run(
        "bio/cutadapt/pe",
        ["snakemake", "--cores", "1", "trimmed/a.1.fastq", "--use-conda", "-F"],
    )


def test_cutadapt_se(run):
    run(
        "bio/cutadapt/se",
        ["snakemake", "--cores", "1", "trimmed/a.fastq", "--use-conda", "-F"],
    )


def test_deeptools_computematrix(run):
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


def test_deeptools_plotcorrelation(run):
    run(
        "bio/deeptools/plotcorrelation",
        ["snakemake", "--cores", "1", "bins.svg", "--use-conda", "-F"],
    )


def test_deeptools_bamcoverage(run):
    run(
        "bio/deeptools/bamcoverage",
        [
            "snakemake",
            "--cores",
            "1",
            "a.coverage.bw",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_bampe_fragmentsize(run):
    # Test basic functionality
    run(
        "bio/deeptools/bampefragmentsize",
        ["snakemake", "--cores", "1", "results/histogram.png", "--use-conda", "-F"],
    )
    # Test with multiple BAMs and custom labels
    run(
        "bio/deeptools/bampefragmentsize",
        [
            "snakemake",
            "--cores",
            "1",
            "results/histogram.png",
            "--config",
            "labels='sample1,sample2'",
            "--use-conda",
            "-F",
        ],
    )
    # Test with blacklist
    run(
        "bio/deeptools/bampefragmentsize",
        [
            "snakemake",
            "--cores",
            "1",
            "results/histogram.png",
            "--config",
            "blacklist='regions.bed'",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_multibigwigsummary(run):
    run(
        "bio/deeptools/multibigwigsummary",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "bins.npz",
        ],
    )
    run(
        "bio/deeptools/multibigwigsummary",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "bed.npz",
        ],
    )


def test_deeptools_bamcoverage_eff(run):
    run(
        "bio/deeptools/bamcoverage",
        [
            "snakemake",
            "--cores",
            "1",
            "a.coverage_code.bw",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_bamcoverage_no_params(run):
    run(
        "bio/deeptools/bamcoverage",
        [
            "snakemake",
            "--cores",
            "1",
            "a.coverage_no_params.bw",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_alignmentsieve(run):
    run(
        "bio/deeptools/alignmentsieve",
        [
            "snakemake",
            "--cores",
            "1",
            "filtered.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_plot_pca(run):
    run(
        "bio/deeptools/plotpca",
        [
            "snakemake",
            "--cores",
            "1",
            "pca.svg",
            "--use-conda",
            "-F",
        ],
    )


def test_deeptools_plotheatmap(run):
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


def test_deeptools_plotfingerprint(run):
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


def test_deeptools_plotprofile(run):
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


def test_deeptools_plotcoverage(run):
    run(
        "bio/deeptools/plotcoverage",
        [
            "snakemake",
            "--cores",
            "1",
            "coverage.png",
            "--use-conda",
            "-F",
        ],
    )


def test_deepvariant(run):
    run(
        "bio/deepvariant",
        ["snakemake", "--cores", "1", "calls/a.vcf.gz", "--use-conda", "-F"],
    )


def test_deepvariant_gvcf(run):
    run(
        "bio/deepvariant",
        [
            "snakemake",
            "--cores",
            "1",
            "gvcf_calls/a.vcf.gz",
            "gvcf_calls/a.g.vcf.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_epic_peaks(run):
    run(
        "bio/epic/peaks",
        ["snakemake", "--cores", "1", "epic/enriched_regions.bed", "--use-conda", "-F"],
    )


def test_fastp_pe(run):
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


def test_fastp_pe_wo_trimming(run):
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


def test_fastp_se(run):
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


def test_fastqc(run):
    run(
        "bio/fastqc",
        ["snakemake", "--cores", "1", "qc/fastqc/a.html", "--use-conda", "-F"],
    )


def test_fastq_screen(run):
    run(
        "bio/fastq_screen",
        ["snakemake", "--cores", "1", "qc/a.fastq_screen.txt", "--use-conda", "-F"],
    )
    run(
        "bio/fastq_screen",
        [
            "snakemake",
            "--cores",
            "1",
            "qc/a.fastq_screen_conf.txt",
            "--use-conda",
            "-F",
        ],
    )
    run(
        "bio/fastq_screen",
        [
            "snakemake",
            "--cores",
            "1",
            "qc/a.fastq_screen_nopng.txt",
            "--use-conda",
            "-F",
        ],
    )


def test_fasttree(run):
    run(
        "bio/fasttree",
        ["snakemake", "--cores", "1", "test-proteins.nwk", "--use-conda", "-F"],
    )


def test_fgbio_annotate(run):
    run(
        "bio/fgbio/annotatebamwithumis",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a.annotated.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_fgbio_annotate_two_umi_fastqs(run):
    run(
        "bio/fgbio/annotatebamwithumis",
        [
            "snakemake",
            "--cores",
            "1",
            "mapped/a-a.annotated.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_fgbio_collectduplexseqmetrics(run):
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


def test_fgbio_filterconsensusreads(run):
    run(
        "bio/fgbio/filterconsensusreads",
        ["snakemake", "--cores", "1", "mapped/a.filtered.bam", "--use-conda", "-F"],
    )


def test_fgbio_group(run):
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


def test_fgbio_set_mate_information(run):
    run(
        "bio/fgbio/setmateinformation",
        ["snakemake", "--cores", "1", "mapped/a.mi.bam", "--use-conda", "-F"],
    )


def test_fgbio_call_molecular_consensus_reads(run):
    run(
        "bio/fgbio/callmolecularconsensusreads",
        ["snakemake", "--cores", "1", "mapped/a.m3.bam", "--use-conda", "-F"],
    )


def test_filtlong(run):
    run(
        "bio/filtlong",
        ["snakemake", "--cores", "1", "reads.filtered.fastq", "--use-conda", "-F"],
    )


def test_freebayes(run):
    run(
        "bio/freebayes",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


def test_freebayes_bcf(run):
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
            ],
        )


def test_freebayes_bed(run):
    for c in [1, 2]:
        run(
            "bio/freebayes",
            [
                "snakemake",
                "--cores",
                str(c),
                "calls/a.vcf.gz",
                "--use-conda",
                "-F",
            ],
        )


def test_gdc_api_bam_slicing(run):
    def check_log(log):
        assert "error" in log and "token" in log

    run(
        "bio/gdc-api/bam-slicing",
        ["snakemake", "--cores", "1", "raw/testing_sample.bam", "--use-conda", "-F"],
        check_log=check_log,
    )


def test_gdc_download(run):
    run(
        "bio/gdc-client/download",
        ["snakemake", "--cores", "1", "raw/testing_sample.maf.gz", "--use-conda", "-F"],
    )


def test_happy_prepy(run):
    run(
        "bio/hap.py/pre.py",
        ["snakemake", "--cores", "1", "normalized/variants.vcf", "--use-conda", "-F"],
    )


def test_happy_prepy(run):
    run(
        "bio/hap.py/pre.py",
        [
            "snakemake",
            "--cores",
            "1",
            "normalized/variants.vcf.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_hisat2_index(run):
    run(
        "bio/hisat2/index",
        [
            "snakemake",
            "--cores",
            "1",
            *[f"hisat2_index/genome.{i}.ht2" for i in range(1, 9)],
            *[f"hisat2_index/genome.{i}.ht2l" for i in range(1, 9)],
            "--use-conda",
            "-F",
        ],
    )


def test_hisat2_align(run):
    run(
        "bio/hisat2/align",
        ["snakemake", "--cores", "1", "mapped/A.bam", "--use-conda", "-F"],
    )


def test_homer_mergePeaks(run):
    run(
        "bio/homer/mergePeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "merged/a_b.peaks"],
    )


def test_homer_getDifferentialPeaks(run):
    run(
        "bio/homer/getDifferentialPeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a_diffPeaks.txt"],
    )


def test_homer_findPeaks(run):
    run(
        "bio/homer/findPeaks",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a_peaks.txt"],
    )


def test_homer_makeTagDirectory(run):
    run(
        "bio/homer/makeTagDirectory",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "tagDir/a"],
    )


def test_immunedeconv(run):
    run(
        "bio/immunedeconv",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "deconv.csv"],
    )


def test_jellyfish_count(run):
    run(
        "bio/jellyfish/count",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.jf"],
    )


def test_jellyfish_dump(run):
    run(
        "bio/jellyfish/dump",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.dump"],
    )


def test_jellyfish_histo(run):
    run(
        "bio/jellyfish/histo",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.histo"],
    )


def test_jellyfish_merge(run):
    run(
        "bio/jellyfish/merge",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "ab.jf"],
    )


def test_homer_annotatePeaks(run):
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


def test_kallisto_index(run):
    run(
        "bio/kallisto/index",
        ["snakemake", "--cores", "1", "transcriptome.idx", "--use-conda", "-F"],
    )


def test_kallisto_quant(run):
    run(
        "bio/kallisto/quant",
        ["snakemake", "--cores", "1", "quant_results_A", "--use-conda", "-F"],
    )


def test_lofreq_call(run):
    run(
        "bio/lofreq/call",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


def test_macs2_callpeak(run):
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


def test_minimap2_aligner_paf(run):
    run(
        "bio/minimap2/aligner",
        ["snakemake", "--cores", "1", "aligned/genome_aln.paf", "--use-conda", "-F"],
    )


def test_minimap2_aligner_sam(run):
    run(
        "bio/minimap2/aligner",
        ["snakemake", "--cores", "1", "aligned/genome_aln.sam", "--use-conda", "-F"],
    )


def test_minimap2_aligner_sam_sorted(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.sorted.sam",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_aligner_bam_sorted(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.sorted.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_aligner_ubam_paf(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.ubam.paf",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_aligner_ubam_sam(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.ubam.sam",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_aligner_ubam_sam_sorted(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.sorted.ubam.sam",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_aligner_ubam_bam_sorted(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned/genome_aln.sorted.ubam.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_minimap2_index(run):
    run(
        "bio/minimap2/index",
        ["snakemake", "--cores", "1", "genome.mmi", "--use-conda", "-F"],
    )


def test_mtnucratiocalculator(run):
    run(
        "bio/mtnucratio",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ratio.txt"],
    )


def test_mosdepth(run):
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_bed/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_by_threshold/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_quantize_precision/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_cram/a.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


def test_multiqc(run):
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc.html", "--use-conda", "-F"],
    )


def test_multiqc_a(run):
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc.a.html", "--use-conda", "-F"],
    )


def test_multiqc_config(run):
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc.config.html", "--use-conda", "-F"],
    )


def test_muscle_super5(run):
    run(
        "bio/muscle",
        ["snakemake", "--cores", "2", "test-proteins.super5.fas", "--use-conda", "-F"],
    )


def test_muscle_fas(run):
    run(
        "bio/muscle",
        ["snakemake", "--cores", "2", "test-proteins.fas", "--use-conda", "-F"],
    )


def test_nanosim_genome(run):
    run(
        "bio/nanosim/simulator",
        [
            "snakemake",
            "--cores",
            "1",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_reads.fq",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_errors.txt",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_reads.unaligned.fq",
            "--use-conda",
            "-F",
        ],
    )


def test_nanosim_transcriptome(run):
    run(
        "bio/nanosim/simulator",
        [
            "snakemake",
            "--cores",
            "1",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated.fq",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated.errors.txt",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated_reads.unaligned.fq",
            "--use-conda",
            "-F",
        ],
    )


def test_nanosim_metagenome(run):
    run(
        "bio/nanosim/simulator",
        [
            "snakemake",
            "--cores",
            "1",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.abundances.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.dna_type_list.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.reference_genomes_list.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/simulated/sample_x.simulated_errors.txt",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/simulated/sample_x.simulated_reads.fa",
            "--use-conda",
            "-F",
        ],
    )


def test_ngsbits_sampleancestry(run):
    run(
        "bio/ngsbits/sampleancestry",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "ancestry.tsv",
        ],
    )


def test_ngsderive(run):
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.readlen.tsv"],
    )
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.instrument.tsv"],
    )
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.strandedness.tsv"],
    )
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.encoding.tsv"],
    )
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.junctions.tsv"],
    )
    run(
        "bio/ngsderive",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "junctions/A.rg.bam.junctions.tsv",
        ],
    )
    run(
        "bio/ngsderive",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.endedness.tsv"],
    )


def test_ngs_disambiguate(run):
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


def test_optitype(run):
    run(
        "bio/optitype",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "optitype/a_result.tsv"],
    )


def test_pandora_index(run):
    run(
        "bio/pandora/index",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "rpsL/prg.fa.k15.w14.idx"],
    )


def test_pcaexplorer_pcaplot(run):
    run(
        "bio/pcaexplorer/pcaplot",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "pca.svg"],
    )


def test_picard_addorreplacegroups(run):
    run(
        "bio/picard/addorreplacereadgroups",
        ["snakemake", "--cores", "1", "fixed-rg/a.bam", "--use-conda", "-F"],
    )


def test_picard_markduplicates_bam(run):
    run(
        "bio/picard/markduplicates",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


def test_picard_markduplicateswithmatecigar_bam(run):
    run(
        "bio/picard/markduplicates",
        [
            "snakemake",
            "--cores",
            "1",
            "dedup/a.matecigar.bam",
            "dedup/a.matecigar.bai",
            "--use-conda",
            "-F",
        ],
    )


def test_picard_markduplicates_sam(run):
    run(
        "bio/picard/markduplicates",
        ["snakemake", "--cores", "1", "dedup/a.sam", "--use-conda", "-F"],
    )


def test_picard_markduplicates_cram(run):
    run(
        "bio/picard/markduplicates",
        [
            "snakemake",
            "--cores",
            "1",
            "dedup/a.cram",
            "dedup/a.cram.crai",
            "--use-conda",
            "-F",
        ],
    )


def test_picard_collectalignmentsummarymetrics(run):
    run(
        "bio/picard/collectalignmentsummarymetrics",
        ["snakemake", "--cores", "1", "stats/a.summary.txt", "--use-conda", "-F"],
    )


def test_picard_collectinsertsizemetrics(run):
    run(
        "bio/picard/collectinsertsizemetrics",
        ["snakemake", "--cores", "1", "stats/a.isize.txt", "--use-conda", "-F"],
    )


def test_picard_bedtointervallist(run):
    run(
        "bio/picard/bedtointervallist",
        ["snakemake", "--cores", "1", "a.interval_list", "--use-conda", "-F"],
    )


def test_picard_collecthsmetrics(run):
    run(
        "bio/picard/collecthsmetrics",
        ["snakemake", "--cores", "1", "stats/hs_metrics/a.txt", "--use-conda", "-F"],
    )


def test_picard_collectmultiplemetrics(run):
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


def test_picard_mergesamfiles(run):
    run(
        "bio/picard/mergesamfiles",
        ["snakemake", "--cores", "1", "merged.bam", "--use-conda", "-F"],
    )


def test_picard_collecttargettedpcemetrics(run):
    run(
        "bio/picard/collecttargetedpcrmetrics/",
        ["snakemake", "--cores", "1", "stats/a.pcr.txt", "--use-conda", "-F"],
    )


def test_picard_bam_to_fastq(run):
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


def test_picard_sortsam(run):
    run(
        "bio/picard/sortsam",
        ["snakemake", "--cores", "1", "sorted/a.bam", "--use-conda", "-F"],
    )


def test_picard_revertsam(run):
    run(
        "bio/picard/revertsam",
        ["snakemake", "--cores", "1", "revert/a.bam", "--use-conda", "-F"],
    )


def test_picard_createsequencedictionary(run):
    run(
        "bio/picard/createsequencedictionary",
        ["snakemake", "--cores", "1", "genome.dict", "--use-conda", "-F"],
    )


def test_pindel_call(run):
    run(
        "bio/pindel/call",
        [
            "snakemake",
            "--cores",
            "1",
            "pindel/all_D",
            "--use-conda",
            "-F",
        ],
    )


def test_pindel_call_include(run):
    def check_log(log):
        assert "Looking at chromosome 1 bases 1000 to 10000" in log

    run(
        "bio/pindel/call",
        [
            "snakemake",
            "--cores",
            "1",
            "pindel/all_included_D",
            "--use-conda",
            "-F",
        ],
        check_log=check_log,
    )


def test_pindel_call_exclude(run):
    def check_log(log):
        assert "Looking at chromosome 1 bases 1 to 1000" in log

    run(
        "bio/pindel/call",
        [
            "snakemake",
            "--cores",
            "1",
            "pindel/all_excluded_D",
            "--use-conda",
            "-F",
        ],
    )


def test_pindel_pindel2vcf(run):
    run(
        "bio/pindel/pindel2vcf",
        ["snakemake", "--cores", "1", "pindel/all_D.vcf", "--use-conda", "-F"],
    )


def test_pindel_pindel2vcf_multi_input(run):
    run(
        "bio/pindel/pindel2vcf",
        ["snakemake", "--cores", "1", "pindel/all.vcf", "--use-conda", "-F"],
    )


def test_preseq_lc_extrap(run):
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


def test_prosolo_calling(run):
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


def test_prosolo_fdr(run):
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


def test_razers3(run):
    run(
        "bio/razers3",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "mapped/a.bam"],
    )


def test_rebaler(run):
    run("bio/rebaler", ["snakemake", "--cores", "1", "--use-conda", "sample1.asm.fa"])


def test_sambamba_flagstats(run):
    run(
        "bio/sambamba/flagstat",
        ["snakemake", "--cores", "1", "mapped/A.stats.txt", "--use-conda", "-F"],
    )


def test_sambamba_sort(run):
    run(
        "bio/sambamba/sort",
        ["snakemake", "--cores", "1", "mapped/A.sorted.bam", "--use-conda", "-F"],
    )


def test_sambamba_index(run):
    run(
        "bio/sambamba/index",
        ["snakemake", "--cores", "1", "mapped/A.sorted.bam.bai", "--use-conda", "-F"],
    )


def test_sambamba_merge(run):
    run(
        "bio/sambamba/merge",
        ["snakemake", "--cores", "1", "mapped/A.merged.bam", "--use-conda", "-F"],
    )


def test_sambamba_view(run):
    run(
        "bio/sambamba/view",
        ["snakemake", "--cores", "1", "mapped/A.filtered.bam", "--use-conda", "-F"],
    )


def test_sambamba_slice(run):
    run(
        "bio/sambamba/slice",
        ["snakemake", "--cores", "1", "mapped/A.region.bam", "--use-conda", "-F"],
    )


def test_sambamba_markdup(run):
    run(
        "bio/sambamba/markdup",
        ["snakemake", "--cores", "1", "mapped/A.rmdup.bam", "--use-conda", "-F"],
    )


def test_samtools_calmd(run):
    run(
        "bio/samtools/calmd",
        ["snakemake", "--cores", "1", "a.calmd.bam", "--use-conda", "-F"],
    )


def test_samtools_collate(run):
    run(
        "bio/samtools/collate",
        ["snakemake", "--cores", "1", "a.collated.bam", "--use-conda", "-F"],
    )


def test_samtools_fixmate(run):
    run(
        "bio/samtools/fixmate",
        ["snakemake", "--cores", "1", "fixed/a.bam", "--use-conda", "-F"],
    )


def test_pyfaidx(run):
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "retrieved.fasta", "--use-conda", "-F"],
    )
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "retrieved.chrom", "--use-conda", "-F"],
    )
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "retrieved.bed", "--use-conda", "-F"],
    )
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "sequence.fasta.fai", "--use-conda", "-F"],
    )
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "regions.fa", "--use-conda", "-F"],
    )
    run(
        "bio/pyfaidx",
        ["snakemake", "--cores", "1", "list_regions.fa", "--use-conda", "-F"],
    )


def test_pyfastaq_replace_bases(run):
    run(
        "bio/pyfastaq/replace_bases",
        ["snakemake", "--cores", "1", "sample1.dna.fa", "--use-conda", "-F"],
    )


def test_samtools_depth(run):
    run(
        "bio/samtools/depth",
        ["snakemake", "--cores", "1", "depth.txt", "--use-conda", "-F"],
    )


def test_samtools_mpileup(run):
    run(
        "bio/samtools/mpileup",
        ["snakemake", "--cores", "1", "mpileup/a.mpileup.gz", "--use-conda", "-F"],
    )


def test_samtools_mpileup(run):
    run(
        "bio/samtools/markdup",
        ["snakemake", "--cores", "1", "a.markdup.bam", "--use-conda", "-F"],
    )


def test_samtools_stats(run):
    run(
        "bio/samtools/stats",
        ["snakemake", "--cores", "1", "samtools_stats/a.txt", "--use-conda", "-F"],
    )


def test_samtools_sort(run):
    run(
        "bio/samtools/sort",
        ["snakemake", "--cores", "1", "mapped/a.sorted.bam", "--use-conda", "-F"],
    )


def test_samtools_index(run):
    run(
        "bio/samtools/index",
        ["snakemake", "--cores", "1", "mapped/a.sorted.bam.bai", "--use-conda", "-F"],
    )


def test_samtools_merge(run):
    run(
        "bio/samtools/merge",
        ["snakemake", "--cores", "1", "merged.bam", "--use-conda", "-F"],
    )


def test_samtools_view(run):
    run(
        "bio/samtools/view", ["snakemake", "--cores", "1", "a.bam", "--use-conda", "-F"]
    )


def test_samtools_fastx(run):
    run(
        "bio/samtools/fastx",
        ["snakemake", "--cores", "1", "a.fasta", "--use-conda", "-F"],
    )


def test_samtools_flagstat(run):
    run(
        "bio/samtools/flagstat",
        ["snakemake", "--cores", "1", "mapped/a.bam.flagstat", "--use-conda", "-F"],
    )


def test_samtools_idxstats(run):
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


def test_samtools_fastq_interleaved(run):
    run(
        "bio/samtools/fastq/interleaved",
        ["snakemake", "--cores", "1", "reads/a.fq", "--use-conda", "-F"],
    )


def test_samtools_fastq_separate(run):
    run(
        "bio/samtools/fastq/separate",
        ["snakemake", "--cores", "1", "reads/a.1.fq", "--use-conda", "-F"],
    )


def test_samtools_faidx(run):
    run(
        "bio/samtools/faidx",
        [
            "snakemake",
            "--cores",
            "1",
            "out/genome.fa.fai",
            "out/genome.named.fa.fai",
            "out/genome.fas.bgz.fai",
            "out/genome.fas.bgz.gzi",
            "out/genome.region_file.fas",
            "out/genome.region_array.fas",
            "out/genome.region_bgzip.fas",
            "--use-conda",
            "-F",
        ],
    )


def test_bamtools_filter(run):
    run(
        "bio/bamtools/filter",
        ["snakemake", "--cores", "1", "filtered/a.bam", "--use-conda", "-F"],
    )


def test_bamtools_filter_json(run):
    run(
        "bio/bamtools/filter_json",
        ["snakemake", "--cores", "1", "filtered/a.bam", "--use-conda", "-F"],
    )


def test_bamtools_split(run):
    run(
        "bio/bamtools/split",
        ["snakemake", "--cores", "1", "mapped/a.REF_xx.bam", "--use-conda", "-F"],
    )


def test_bamtools_stats(run):
    run(
        "bio/bamtools/stats",
        ["snakemake", "--cores", "1", "a.bamstats", "--use-conda", "-F"],
    )


def test_snpmutator(run):
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


def test_star_align(run):
    # generate index on the fly, because it is huge regardless of genome size
    os.makedirs("bio/star/align/test/index", exist_ok=True)
    try:
        subprocess.check_call(
            "mamba env create --file bio/star/align/environment.yaml -n star-env",
            shell=True,
        )
        subprocess.check_call(
            "bash -l -c 'source $(dirname $(dirname $(which mamba)))/bin/activate star-env; STAR --genomeDir "
            "bio/star/align/test/index "
            "--genomeFastaFiles bio/star/align/test/genome.fasta "
            "--runMode genomeGenerate "
            "--genomeSAindexNbases 8'",
            shell=True,
        )
    finally:
        shutil.rmtree("star-env", ignore_errors=True)

    run(
        "bio/star/align",
        ["snakemake", "--cores", "1", "star/se/a/se_aligned.bam", "--use-conda", "-F"],
    )
    run(
        "bio/star/align",
        ["snakemake", "--cores", "1", "star/pe/a/pe_aligned.sam", "--use-conda", "-F"],
    )


def test_ngscheckmate_ncm(run):
    run(
        "bio/ngscheckmate/ncm",
        ["snakemake", "--cores", "1", "bam_matrix.txt", "--use-conda", "-F"],
    )
    run(
        "bio/ngscheckmate/ncm",
        ["snakemake", "--cores", "1", "vcf_matrix.txt", "--use-conda", "-F"],
    )
    run(
        "bio/ngscheckmate/ncm",
        ["snakemake", "--cores", "1", "fastq_matched.txt", "--use-conda", "-F"],
    )
    run(
        "bio/ngscheckmate/ncm",
        ["snakemake", "--cores", "1", "fastq_paired_matched.txt", "--use-conda", "-F"],
    )


def test_star_index(run):
    run("bio/star/index", ["snakemake", "--cores", "1", "genome", "--use-conda", "-F"])


def test_snpeff_annotate(run):
    run(
        "bio/snpeff/annotate",
        [
            "snakemake",
            "--cores",
            "1",
            "snpeff/fake_KJ660346.vcf",
            "snpeff_nostats/fake_KJ660346.vcf",
            "--use-conda",
            "-F",
        ],
    )


def test_snpeff_download(run):
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


def test_strelka_germline(run):
    run(
        "bio/strelka/germline",
        ["snakemake", "--cores", "1", "strelka/a.vcf.gz", "--use-conda", "-F"],
    )


def test_subread_featurecounts(run):
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


def test_trim_galore_pe(run):
    run(
        "bio/trim_galore/pe",
        ["snakemake", "--cores", "1", "trimmed/a_R1.fq.gz", "--use-conda", "-F"],
    )


def test_trim_galore_pe_uncompressed(run):
    run(
        "bio/trim_galore/pe",
        ["snakemake", "--cores", "1", "trimmed/a_R2.fastq", "--use-conda", "-F"],
    )


def test_trim_galore_se(run):
    run(
        "bio/trim_galore/se",
        ["snakemake", "--cores", "1", "trimmed/a_trimmed.fq.gz", "--use-conda", "-F"],
    )


def test_trim_galore_se_uncompressed(run):
    run(
        "bio/trim_galore/se",
        ["snakemake", "--cores", "1", "trimmed/a_trimmed.fastq", "--use-conda", "-F"],
    )


def test_trimmomatic_pe(run):
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic",
        [
            "snakemake",
            "--cores",
            "10",
            "trimmed/se/fq_fq/a.1.fastq",
            "trimmed/se/gz_fq/a.1.fastq",
            "trimmed/se/fq_gz/a.1.fastq.gz",
            "trimmed/se/gz_gz/a.1.fastq.gz",
            "trimmed/pe/fq_fq/a.1.fastq",
            "trimmed/pe/gz_fq/a.1.fastq",
            "trimmed/pe/fq_gz/a.1.fastq.gz",
            "trimmed/pe/gz_gz/a.1.fastq.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_rasusa(run):
    run(
        "bio/rasusa",
        ["snakemake", "--cores", "1", "--use-conda", "a.subsampled.r1.fq"],
    )


def test_rubic(run):
    run(
        "bio/rubic",
        ["snakemake", "--cores", "1", "out/BRCA/gains.txt", "--use-conda", "-F"],
    )


def test_delly(run):
    run("bio/delly", ["snakemake", "--cores", "1", "sv/calls.bcf", "--use-conda", "-F"])


def test_delly(run):
    run(
        "bio/delly",
        ["snakemake", "--cores", "1", "sv/calls.vcf.gz", "--use-conda", "-F"],
    )


def test_manta(run):
    run(
        "bio/manta",
        ["snakemake", "--cores", "2", "results/out.bcf", "--use-conda", "-F"],
    )


def test_jannovar(run):
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


def test_cairosvg(run):
    run("utils/cairosvg", ["snakemake", "--cores", "1", "pca.pdf", "--use-conda", "-F"])


def test_trinity(run):
    run(
        "bio/trinity",
        [
            "snakemake",
            "--cores",
            "1",
            "trinity_out_dir.Trinity.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_salmon_decoys(run):
    run(
        "bio/salmon/decoys",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "gentrome.fasta.gz"],
    )


def test_salmon_index(run):
    run(
        "bio/salmon/index",
        [
            "snakemake",
            "--cores",
            "1",
            "salmon/transcriptome_index/complete_ref_lens.bin",
            "--use-conda",
            "-F",
        ],
    )

    run(
        "bio/salmon/index",
        [
            "snakemake",
            "--cores",
            "1",
            "salmon/transcriptome_index/",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_dir",
        ],
    )


def test_salmon_quant(run):
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
            "salmon/a/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_index_list",
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
            "2",
            "salmon/a_se_x_transcriptome/quant.sf",
            "--use-conda",
            "-F",
            "-s",
            "Snakefile_se_bz2",
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


def test_gseapy_gsea(run):
    run(
        "bio/gseapy/gsea",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "KEGG_2016"],
    )

    run(
        "bio/gseapy/gsea",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "gsea.results.csv"],
    )

    run(
        "bio/gseapy/gsea",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ssgsea.results.csv"],
    )

    run(
        "bio/gseapy/gsea",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "prerank_results_dir"],
    )


def test_sexdeterrmine(run):
    run(
        "bio/sexdeterrmine",
        ["snakemake", "--cores", "1", "results.tsv", "-F", "--use-conda"],
    )


def test_sourmash_compute(run):
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


def test_busco(run):
    run(
        "bio/busco",
        [
            "snakemake",
            "--cores",
            "1",
            "txome_busco/short_summary.json",
            "--use-conda",
            "-F",
        ],
    )


def test_vcftoolsfilter(run):
    run(
        "bio/vcftools/filter",
        ["snakemake", "--cores", "1", "sample.filtered.vcf", "--use-conda", "-F"],
    )


def test_gatk_callcopyrationsegments(run):
    run(
        "bio/gatk/callcopyratiosegments",
        ["snakemake", "--cores", "1", "a.called.seg", "--use-conda", "-F"],
    )


def test_gatk_calculatecontamination(run):
    run(
        "bio/gatk/calculatecontamination",
        ["snakemake", "--cores", "1", "contamination.table", "--use-conda", "-F"],
    )


def test_gatk_scatterintervalsbyns(run):
    run(
        "bio/gatk/scatterintervalsbyns",
        ["snakemake", "--cores", "1", "genome.intervals", "--use-conda", "-F"],
    )


def test_gatk_splitintervals(run):
    run(
        "bio/gatk/splitintervals",
        ["snakemake", "--cores", "1", "out/genome.00.bed", "--use-conda", "-F"],
    )


def test_gatk_printreadsspark(run):
    run(
        "bio/gatk/printreadsspark",
        ["snakemake", "--cores", "1", "a.bam", "--use-conda", "-F"],
    )


def test_gatk_markduplicatesspark(run):
    run(
        "bio/gatk/markduplicatesspark",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


def test_gatk_intervallisttobed(run):
    run(
        "bio/gatk/intervallisttobed",
        ["snakemake", "--cores", "1", "genome.bed", "--use-conda", "-F"],
    )


def test_gatk_estimatelibrarycomplexity(run):
    run(
        "bio/gatk/estimatelibrarycomplexity",
        ["snakemake", "--cores", "1", "a.metrics", "--use-conda", "-F"],
    )


def test_gatk_baserecalibrator(run):
    run(
        "bio/gatk/baserecalibrator",
        ["snakemake", "--cores", "1", "recal/a.grp", "--use-conda", "-F"],
    )


def test_gatk_baserecalibratorspark(run):
    run(
        "bio/gatk/baserecalibratorspark",
        ["snakemake", "--cores", "1", "recal/a.grp", "--use-conda", "-F"],
    )


def test_gatk_collectreadcounts(run):
    run(
        "bio/gatk/collectreadcounts",
        ["snakemake", "--cores", "1", "a.counts.hdf5", "--use-conda", "-F"],
    )


def test_gatk_collectalleliccounts(run):
    run(
        "bio/gatk/collectalleliccounts",
        ["snakemake", "--cores", "1", "a.counts.tsv", "--use-conda", "-F"],
    )


def test_gatk_applybqsr(run):
    run(
        "bio/gatk/applybqsr",
        ["snakemake", "--cores", "1", "recal/a.bam", "--use-conda", "-F"],
    )


def test_gatk_applybqsr_cram(run):
    run(
        "bio/gatk/applybqsr",
        [
            "snakemake",
            "-s",
            "Snakefile_cram",
            "--cores",
            "1",
            "recal/a.cram",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_applybqsrspark(run):
    run(
        "bio/gatk/applybqsrspark",
        ["snakemake", "--cores", "1", "recal/a.bam", "--use-conda", "-F"],
    )


def test_gatk_applybqsrspark_cram(run):
    run(
        "bio/gatk/applybqsrspark",
        [
            "snakemake",
            "-s",
            "Snakefile_cram",
            "--cores",
            "1",
            "recal/a.cram",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_denoisereadcounts(run):
    run(
        "bio/gatk/denoisereadcounts",
        [
            "snakemake",
            "--cores",
            "1",
            "a.standardizedCR.tsv",
            "a.denoisedCR.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_haplotypecaller_vcf(run):
    run(
        "bio/gatk/haplotypecaller",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


def test_gatk_haplotypecaller_gvcf(run):
    run(
        "bio/gatk/haplotypecaller",
        ["snakemake", "--cores", "1", "calls/a.g.vcf", "--use-conda", "-F"],
    )


def test_gatk_modelsegments(run):
    run(
        "bio/gatk/modelsegments",
        ["snakemake", "--cores", "1", "a.den.modelFinal.seg", "--use-conda", "-F"],
    )


def test_gatk_variantrecalibrator(run):
    def check_log(log):
        assert "USAGE" not in log

    run(
        "bio/gatk/variantrecalibrator",
        [
            "snakemake",
            "--cores",
            "1",
            "calls/all.recal.vcf",
            "--use-conda",
            "-F",
        ],
        check_log=check_log,
    )


def test_gatk_variantstotable(run):
    run(
        "bio/gatk/variantstotable",
        ["snakemake", "--cores", "1", "calls/snvs.tab", "--use-conda", "-F"],
    )


def test_gatk_filtermutectcalls(run):
    run(
        "bio/gatk/filtermutectcalls",
        [
            "snakemake",
            "--cores",
            "1",
            "calls/snvs.mutect.filtered.vcf",
            "--use-conda",
            "-F",
        ],
    )

    run(
        "bio/gatk/filtermutectcalls",
        [
            "snakemake",
            "--cores",
            "1",
            "calls/snvs.mutect.filtered.b.vcf",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_selectvariants(run):
    run(
        "bio/gatk/selectvariants",
        ["snakemake", "--cores", "1", "calls/snvs.vcf", "--use-conda", "-F"],
    )


def test_gatk_variantannotator(run):
    run(
        "bio/gatk/variantannotator",
        ["snakemake", "--cores", "1", "snvs.annot.vcf", "--use-conda", "-F"],
    )


def test_gatk_variantfiltration(run):
    run(
        "bio/gatk/variantfiltration",
        ["snakemake", "--cores", "1", "calls/snvs.filtered.vcf", "--use-conda", "-F"],
    )


def test_gatk_varianteval(run):
    run(
        "bio/gatk/varianteval",
        ["snakemake", "--cores", "1", "snvs.varianteval.grp", "--use-conda", "-F"],
    )


def test_gatk_genotypegvcfs(run):
    run(
        "bio/gatk/genotypegvcfs",
        ["snakemake", "--cores", "1", "calls/all.vcf", "--use-conda", "-F"],
    )


def test_gatk_genomicsdbimport(run):
    run(
        "bio/gatk/genomicsdbimport",
        ["snakemake", "--cores", "1", "db", "--use-conda", "-F"],
    )


def test_gatk_combinegvcfs(run):
    run(
        "bio/gatk/combinegvcfs",
        ["snakemake", "--cores", "1", "calls/all.g.vcf", "--use-conda", "-F"],
    )


def test_gatk_splitncigarreads(run):
    run(
        "bio/gatk/splitncigarreads",
        ["snakemake", "--cores", "1", "split/a.bam", "--use-conda", "-F"],
    )


def test_gatk_cleansam(run):
    run(
        "bio/gatk/cleansam",
        ["snakemake", "--cores", "1", "a.clean.bam", "--use-conda", "-F"],
    )


def test_gatk3_realignertargetcreator(run):
    run(
        "bio/gatk3/realignertargetcreator",
        ["snakemake", "--cores", "1", "a.intervals", "--use-conda", "-F"],
    )


def test_gatk3_indelrealigner(run):
    run(
        "bio/gatk3/indelrealigner",
        ["snakemake", "--cores", "1", "a.realigned.bam", "--use-conda", "-F"],
    )


def test_gatk3_baserecalibrator(run):
    run(
        "bio/gatk3/baserecalibrator",
        ["snakemake", "--cores", "1", "a.recal_data_table", "--use-conda", "-F"],
    )


def test_gatk3_printreads(run):
    run(
        "bio/gatk3/printreads",
        ["snakemake", "--cores", "1", "a.bqsr.bam", "--use-conda", "-F"],
    )


def test_picard_mergevcfs(run):
    run(
        "bio/picard/mergevcfs",
        ["snakemake", "--cores", "1", "snvs.vcf", "--use-conda", "-F"],
    )


def test_igv_reports(run):
    run(
        "bio/igv-reports",
        ["snakemake", "--cores", "1", "igv-report.html", "--use-conda", "-F"],
    )


def test_strelka_somatic(run):
    run(
        "bio/strelka/somatic",
        ["snakemake", "--cores", "1", "a_vcf", "--use-conda", "-F", "-j 2"],
    )


def test_gatk_mutect(run):
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant/a.vcf", "--use-conda", "-F"],
    )
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant_complete/a.vcf", "--use-conda", "-F"],
    )
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant_list/a_b.vcf", "--use-conda", "-F"],
    )


def test_gatk_learn_read_orientation(run):
    run(
        "bio/gatk/learnreadorientationmodel",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


def test_gatk_leftalignandtrimvariants(run):
    run(
        "bio/gatk/leftalignandtrimvariants",
        [
            "snakemake",
            "--cores",
            "1",
            "calls/split_multiallelics.vcf",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_getpileupsummaries(run):
    run(
        "bio/gatk/getpileupsummaries",
        ["snakemake", "--cores", "1", "summaries.table", "--use-conda", "-F"],
    )


def test_gatk_mutect_bam(run):
    run(
        "bio/gatk/mutect",
        [
            "snakemake",
            "--cores",
            "1",
            "variant_bam/a.vcf",
            "variant_bam/a.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_gatk_depth_of_coverage(run):
    run(
        "bio/gatk/depthofcoverage",
        [
            "snakemake",
            "--cores",
            "1",
            "depth/a",
            "depth/a.sample_cumulative_coverage_counts",
            "depth/a.sample_cumulative_coverage_proportions",
            "depth/a.sample_interval_statistics",
            "depth/a.sample_interval_summary",
            "depth/a.sample_statistics",
            "depth/a.sample_summary",
            "--use-conda",
            "-F",
        ],
    )


def test_vardict_single_mode(run):
    run(
        "bio/vardict",
        ["snakemake", "--cores", "1", "vcf/a.s.vcf", "--use-conda", "-F"],
    )


def test_vardict_paired_mode(run):
    run(
        "bio/vardict",
        ["snakemake", "--cores", "1", "vcf/a.tn.vcf", "--use-conda", "-F"],
    )


def test_varscan_mpileup2indel(run):
    run(
        "bio/varscan/mpileup2indel",
        ["snakemake", "--cores", "1", "vcf/a.vcf", "--use-conda", "-F"],
    )


def test_varscan_mpileup2snp(run):
    run(
        "bio/varscan/mpileup2snp",
        ["snakemake", "--cores", "1", "vcf/a.vcf", "--use-conda", "-F"],
    )


def test_varscan_somatic(run):
    run(
        "bio/varscan/somatic",
        [
            "snakemake",
            "--cores",
            "1",
            "single_mpileup/vcf/a.snp.vcf",
            "dual_mpileup/vcf/a.snp.vcf",
            "--use-conda",
            "-F",
        ],
    )


def test_umis_bamtag(run):
    run(
        "bio/umis/bamtag",
        ["snakemake", "--cores", "1", "data/a.annotated.bam", "--use-conda", "-F"],
    )


def test_transdecoder_longorfs(run):
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


def test_transdecoder_predict(run):
    run(
        "bio/transdecoder/predict",
        ["snakemake", "--cores", "1", "test.fa.transdecoder.gff3", "--use-conda", "-F"],
    )


def test_lastdb_nucl(run):
    run(
        "bio/last/lastdb",
        ["snakemake", "--cores", "1", "test-transcript.fa.prj", "--use-conda", "-F"],
    )


def test_lastdb_prot(run):
    run(
        "bio/last/lastdb",
        ["snakemake", "--cores", "1", "test-protein.fa.prj", "--use-conda", "-F"],
    )


def test_lastal_nucl(run):
    run(
        "bio/last/lastal",
        ["snakemake", "--cores", "1", "test-transcript.maf", "--use-conda", "-F"],
    )


def test_lastal_prot(run):
    run(
        "bio/last/lastal",
        ["snakemake", "--cores", "1", "test-tr-x-prot.maf", "--use-conda", "-F"],
    )


def test_pear(run):
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


def test_plass_paired(run):
    run(
        "bio/plass",
        ["snakemake", "--cores", "1", "plass/prot.fasta", "--use-conda", "-F"],
    )


def test_plass_single(run):
    run(
        "bio/plass",
        ["snakemake", "--cores", "1", "plass/prot_single.fasta", "--use-conda", "-F"],
    )


def test_refgenie(run):
    try:
        shutil.copytree("bio/refgenie/test/genome_folder", "/tmp/genome_folder")
    except FileExistsError:
        # no worries, the directory is already there
        pass
    os.environ["REFGENIE"] = "/tmp/genome_folder/genome_config.yaml"
    run("bio/refgenie", ["snakemake", "--cores", "1", "--use-conda", "-F"])


def test_hmmbuild(run):
    run(
        "bio/hmmer/hmmbuild",
        ["snakemake", "--cores", "1", "test-profile.hmm", "--use-conda", "-F"],
    )


def test_hmmpress(run):
    run(
        "bio/hmmer/hmmpress",
        ["snakemake", "--cores", "1", "test-profile.hmm.h3f", "--use-conda", "-F"],
    )


def test_hmmscan(run):
    run(
        "bio/hmmer/hmmscan",
        ["snakemake", "--cores", "1", "test-prot-tbl.txt", "--use-conda", "-F"],
    )


def test_hmmsearch(run):
    run(
        "bio/hmmer/hmmsearch",
        ["snakemake", "--cores", "1", "test-prot-tbl.txt", "--use-conda", "-F"],
    )


def test_jackhmmer(run):
    run(
        "bio/hmmer/jackhmmer",
        ["snakemake", "--cores", "1", "test-prot-tbl.txt", "--use-conda", "-F"],
    )


def test_paladin_index(run):
    run(
        "bio/paladin/index",
        ["snakemake", "--cores", "1", "index/prot.fasta.bwt", "--use-conda", "-F"],
    )


def test_paladin_prepare(run):
    run(
        "bio/paladin/prepare",
        ["snakemake", "--cores", "1", "uniprot_sprot.fasta.gz", "--use-conda", "-F"],
    )


def test_paladin_align(run):
    run(
        "bio/paladin/align",
        ["snakemake", "--cores", "1", "paladin_mapped/a.bam", "--use-conda", "-F"],
    )


def test_ucsc_bedgraphtobigwig(run):
    run(
        "bio/ucsc/bedGraphToBigWig",
        ["snakemake", "--cores", "1", "a.bw", "--use-conda", "-F"],
    )


def test_ucsc_genepredtobed(run):
    run(
        "bio/ucsc/genePredToBed",
        ["snakemake", "--cores", "1", "annotation.bed", "--use-conda", "-F"],
    )


def test_ucsc_fatotwobit(run):
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


def test_ucsc_twobitinfo(run):
    run(
        "bio/ucsc/twoBitInfo",
        ["snakemake", "--cores", "1", "genome.chrom.sizes", "--use-conda", "-F"],
    )


def test_ucsc_twobittofa(run):
    run(
        "bio/ucsc/twoBitToFa",
        ["snakemake", "--cores", "1", "genome.fa", "--use-conda", "-F"],
    )


def test_entrez_efetch(run):
    run(
        "bio/entrez/efetch",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_sequence(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_sequence_old_release(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "-s", "old_release.smk", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_sequence_gzipped(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "refs/genome.fa.gz", "--use-conda", "-F"],
    )


def test_ensembl_sequence_chromosome(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "refs/chr2.fasta", "--use-conda", "-F"],
    )


def test_ensembl_sequence_multiple_chromosomes(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "refs/chr6_and_chr1.fasta", "--use-conda", "-F"],
        compare_results_with_expected={
            "refs/chr6_and_chr1.fasta": "expected/chr6_and_chr1.fasta"
        },
    )


def test_ensembl_sequence_multiple_chromosomes_gzipped(run):
    run(
        "bio/reference/ensembl-sequence",
        ["snakemake", "--cores", "1", "refs/chr6_and_chr1.fa.gz", "--use-conda", "-F"],
        compare_results_with_expected={
            "refs/chr6_and_chr1.fa.gz": "expected/chr6_and_chr1.fa.gz"
        },
    )


def test_ensembl_sequence_chromosome_old_release(run):
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


def test_ensembl_annotation_gtf(run):
    run(
        "bio/reference/ensembl-annotation",
        ["snakemake", "--cores", "1", "refs/annotation.gtf", "--use-conda", "-F"],
    )


def test_ensembl_annotation_gtf_gz(run):
    run(
        "bio/reference/ensembl-annotation",
        ["snakemake", "--cores", "1", "refs/annotation.gtf.gz", "--use-conda", "-F"],
    )


def test_ensembl_regulatory_gff3_gz(run):
    run(
        "bio/reference/ensembl-regulation",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/regulatory_features.gff3.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_regulatory_features_grch37_gff(run):
    run(
        "bio/reference/ensembl-regulation",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/regulatory_features.gff",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_regulatory_features_mouse_gff_gz(run):
    run(
        "bio/reference/ensembl-regulation",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/regulatory_features.mouse.gff.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_transcripts_to_genes_mapping(run):
    run(
        "bio/reference/ensembl-biomart-table",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/ensembl_transcripts_to_genes_mapping.tsv.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_transcripts_to_genes_mapping_parquet(run):
    run(
        "bio/reference/ensembl-biomart-table",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/ensembl_transcripts_to_genes_mapping.parquet.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_mysql_create_repeat_annotations(run):
    run(
        "bio/reference/ensembl-mysql-table",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/ensembl_repeat_annotations.tsv.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_mysql_create_regulatory_annotations_parquet(run):
    run(
        "bio/reference/ensembl-mysql-table",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/ensembl_regulatory_annotations.parquet.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_ensembl_variation(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_variation_old_release(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "old_release.smk", "--cores", "1", "--use-conda", "-F"],
    )


@pytest.mark.skip(reason="needs too much time")
def test_ensembl_variation_grch37(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "grch37.smk", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_variation_chromosome(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "chrom_wise.smk", "--cores", "1", "--use-conda", "-F"],
    )


def test_ensembl_variation_with_contig_lengths(run):
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


def test_ega_fetch(run):
    run(
        "bio/ega/fetch",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "data/EGAF00007243774.cram"],
    )


def test_infernal_cmpress(run):
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


def test_infernal_cmscan(run):
    run(
        "bio/infernal/cmscan",
        ["snakemake", "--cores", "1", "tr-infernal-tblout.txt", "--use-conda", "-F"],
    )


def test_bismark_genome_preparation(run):
    run(
        "bio/bismark/bismark_genome_preparation",
        [
            "snakemake",
            "--cores",
            "2",
            "resources/genome/bismark",
            "resources/genome_gz/bismark",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "resources/genome/bismark/Bisulfite_Genome/GA_conversion/genome_mfa.GA_conversion.fa": "expected/genome/bismark/Bisulfite_Genome/genome_mfa.GA_conversion.fa",
            "resources/genome_gz/bismark/Bisulfite_Genome/CT_conversion/genome_mfa.CT_conversion.fa": "expected/genome_gz/bismark/Bisulfite_Genome/genome_mfa.CT_conversion.fa",
        },
    )


def test_bismark_genome_bam2nuc(run):
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


def test_bismark_bismark(run):
    run(
        "bio/bismark/bismark",
        [
            "snakemake",
            "--cores",
            "1",
            "results/bismark/a_genome_pe.bam",
            "results/bismark/b_genome.cram",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "results/bismark/b_genome.nucleotide_stats.txt": "expected/b_genome.nucleotide_stats.txt",
        },
    )


def test_bismark_deduplicate_bismark(run):
    run(
        "bio/bismark/deduplicate_bismark",
        [
            "snakemake",
            "--cores",
            "1",
            "bams/a_pe.deduplicated.bam",
            "bams/b.deduplicated.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_methyldackel_extract(run):
    run(
        "bio/methyldackel/extract",
        ["snakemake", "--cores", "1", "-F", "--use-conda", "cpg.meth.bg"],
    )

    run(
        "bio/methyldackel/extract",
        ["snakemake", "--cores", "1", "-F", "--use-conda", "cpg.count.bg"],
    )

    run(
        "bio/methyldackel/extract",
        ["snakemake", "--cores", "1", "-F", "--use-conda", "cpg.logit.bg"],
    )

    run(
        "bio/methyldackel/extract",
        ["snakemake", "--cores", "1", "-F", "--use-conda", "report.tsv"],
    )


def test_bismark_bismark_methylation_extractor(run):
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


def test_bismark_bismark2report(run):
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


def test_bismark_bismark2summary(run):
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


def test_bismark_bismark2bedgraph(run):
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


def test_tabix_index(run):
    run(
        "bio/tabix/index",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "test.vcf.gz.tbi"],
    )


def test_tabix_query(run):
    run(
        "bio/tabix/query",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.output.bed"],
    )


# TODO msisensor fails with a segfault, skip tests for now
#
# def test_msisensor_scan(run):
#     run(
#         "bio/msisensor/scan",
#         ["snakemake", "--cores", "1", "--use-conda", "-F", "microsat.list"],
#     )


def test_msisensor_msi(run):
    run(
        "bio/msisensor/msi",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "example.msi"],
    )


def test_tximport(run):
    run("bio/tximport", ["snakemake", "--cores", "1", "txi.RDS", "--use-conda", "-F"])


def test_fasterq_dump_se(run):
    run(
        "bio/sra-tools/fasterq-dump",
        ["snakemake", "--cores", "1", "data/se/SRR14133989.fastq", "--use-conda", "-F"],
    )


def test_fasterq_dump_se_gz(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "--cores",
            "1",
            "data/se/SRR14133989.fastq.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_fasterq_dump_se_bz2(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "--cores",
            "1",
            "data/se/SRR14133989.fastq.bz2",
            "--use-conda",
            "-F",
        ],
    )


def test_fasterq_dump_pe(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "--cores",
            "1",
            "data/pe/SRR14133829_1.fastq",
            "--use-conda",
            "-F",
        ],
    )


def test_fasterq_dump_pe_gz(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "--cores",
            "1",
            "data/pe/SRR14133829_1.fastq.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_fasterq_dump_pe_bz2(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "--cores",
            "1",
            "data/pe/SRR14133829_1.fastq.bz2",
            "--use-conda",
            "-F",
        ],
    )


def test_bwa_mem_samblaster(run):
    run(
        "bio/bwa/mem-samblaster",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_bwa_mem2_samblaster(run):
    run(
        "bio/bwa-mem2/mem-samblaster",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_snpsift_genesets(run):
    run(
        "bio/snpsift/genesets",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


def test_snpsift_vartype(run):
    run(
        "bio/snpsift/varType",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


def test_snpsift_gwascat(run):
    run(
        "bio/snpsift/gwascat",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


def test_ptrimmer_se(run):
    run(
        "bio/ptrimmer",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ptrimmer_se"],
    )


def test_ptrimmer_pe(run):
    run(
        "bio/ptrimmer",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ptrimmer_pe"],
    )


def test_vep_cache(run):
    run(
        "bio/vep/cache",
        ["snakemake", "--cores", "1", "resources/vep/cache", "--use-conda", "-F"],
    )

    run(
        "bio/vep/cache",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/vep/indexed_cache",
            "--use-conda",
            "-F",
        ],
    )

    run(
        "bio/vep/cache",
        ["snakemake", "--cores", "1", "resources/vep/cache_ebi", "--use-conda", "-F"],
    )


def test_vep_plugins(run):
    run(
        "bio/vep/plugins",
        ["snakemake", "--cores", "1", "resources/vep/plugins", "--use-conda", "-F"],
    )


def test_vep_annotate(run):
    run(
        "bio/vep/annotate",
        [
            "snakemake",
            "--cores",
            "1",
            "variants.annotated.bcf",
            "--use-conda",
            "-F",
            "--verbose",
        ],
    )


def test_genefuse(run):
    run(
        "bio/genefuse",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "a_fusions.txt",
            "a_genefuse_report.html",
        ],
    )


def test_genomepy(run):
    # download dm3 genome (relatively small, +/- 250 mb)
    run(
        "bio/genomepy",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "dm3/dm3.fa"],
    )


def test_chm_eval_sample(run):
    run(
        "bio/benchmark/chm-eval-sample",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_chm_eval_kit(run):
    run(
        "bio/benchmark/chm-eval-kit", ["snakemake", "--cores", "1", "--use-conda", "-F"]
    )


def test_chm_eval_eval(run):
    run(
        "bio/benchmark/chm-eval",
        ["snakemake", "--cores", "1", "--use-conda", "chm-eval/calls.summary"],
    )


def test_snpsift_dbnsfp(run):
    run(
        "bio/snpsift/dbnsfp",
        ["snakemake", "--cores", "1", "out.vcf", "--use-conda", "-F"],
    )


def test_snpsift_annotate(run):
    run(
        "bio/snpsift/annotate",
        ["snakemake", "--cores", "1", "annotated/out.vcf", "--use-conda", "-F"],
    )


def test_unicycler(run):
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


def test_vg_autoindex_giraffe(run):
    run(
        "bio/vg/autoindex",
        ["snakemake", "--cores", "1", "resources/genome.dist", "--use-conda", "-F"],
    )


def test_vg_autoindex_map(run):
    run(
        "bio/vg/autoindex",
        ["snakemake", "--cores", "1", "resources/genome.xg", "--use-conda", "-F"],
    )


def test_vg_construct(run):
    run(
        "bio/vg/construct",
        ["snakemake", "--cores", "1", "graph/c.vg", "--use-conda", "-F"],
    )


def test_vg_giraffe(run):
    run(
        "bio/vg/giraffe",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


def test_vg_merge(run):
    run(
        "bio/vg/merge",
        ["snakemake", "--cores", "1", "graph/wg.vg", "--use-conda", "-F"],
    )


def test_vg_ids(run):
    run(
        "bio/vg/ids",
        ["snakemake", "--cores", "1", "graph/c_mod.vg", "--use-conda", "-F"],
    )


def test_vg_index_gcsa(run):
    run(
        "bio/vg/index/gcsa",
        ["snakemake", "--cores", "1", "index/wg.gcsa", "--use-conda", "-F"],
    )


def test_vg_index_xg(run):
    run(
        "bio/vg/index/xg",
        ["snakemake", "--cores", "1", "index/x.xg", "--use-conda", "-F"],
    )


def test_vg_kmers(run):
    run(
        "bio/vg/kmers",
        ["snakemake", "--cores", "1", "kmers/c.kmers", "--use-conda", "-F"],
    )


def test_vg_prune(run):
    run(
        "bio/vg/prune",
        ["snakemake", "--cores", "1", "graph/c.pruned.vg", "--use-conda", "-F"],
    )


def test_vg_sim(run):
    run("bio/vg/sim", ["snakemake", "--cores", "1", "reads/x.seq", "--use-conda", "-F"])


def test_wgsim(run):
    run(
        "bio/wgsim",
        ["snakemake", "--cores", "1", "reads/1.fq", "reads/2.fq", "--use-conda", "-F"],
    )


def test_diamond_makedb(run):
    run(
        "bio/diamond/makedb",
        ["snakemake", "--cores", "1", "foo.dmnd", "--use-conda", "-F"],
    )


def test_diamond_blastx(run):
    run(
        "bio/diamond/blastx",
        ["snakemake", "--cores", "1", "foo.tsv.gz", "--use-conda", "-F"],
    )


def test_diamond_blastp(run):
    run(
        "bio/diamond/blastp",
        ["snakemake", "--cores", "1", "test-protein.tsv.gz", "--use-conda", "-F"],
    )


def test_applyvqsr(run):
    run(
        "bio/gatk/applyvqsr",
        ["snakemake", "--cores", "1", "test.snp_recal.vcf", "--use-conda", "-F"],
    )


def test_nextflow(run):
    run(
        "utils/nextflow",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "--show-failed-logs"],
    )


def test_qualimaprnaseq(run):
    run(
        "bio/qualimap/rnaseq",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_qualimapbamqc(run):
    run(
        "bio/qualimap/bamqc",
        ["snakemake", "--cores", "1", "qc/a", "--use-conda", "-F"],
    )


def test_collectrnaseqmetrics(run):
    run(
        "bio/picard/collectrnaseqmetrics",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_gtftogenepred(run):
    run(
        "bio/ucsc/gtfToGenePred",
        ["snakemake", "--cores", "1", "annotation.genePred", "--use-conda", "-F"],
    )


def test_gtftogenepred_picard_collectrnaseqmetrics(run):
    run(
        "bio/ucsc/gtfToGenePred",
        [
            "snakemake",
            "--cores",
            "1",
            "annotation.PicardCollectRnaSeqMetrics.genePred",
            "--use-conda",
            "-F",
        ],
    )


def test_collectgcbiasmetrics(run):
    run(
        "bio/picard/collectgcbiasmetrics",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_rsem_calculate_expression(run):
    run(
        "bio/rsem/calculate-expression",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )

    run(
        "bio/rsem/calculate-expression",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "-s", "Snakefile_fastq"],
    )


def test_rsem_prepare_reference(run):
    run(
        "bio/rsem/prepare-reference",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_generate_data_matrix(run):
    run(
        "bio/rsem/generate-data-matrix",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_rseqc_inner_distance(run):
    run(
        "bio/rseqc/inner_distance",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.pdf"],
    )


def test_rseqc_infer_experiment(run):
    run(
        "bio/rseqc/infer_experiment",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.experiment.txt"],
    )


def test_rseqc_bam_stat(run):
    run(
        "bio/rseqc/bam_stat",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.stats"],
    )


def test_rseqc_read_gc(run):
    run(
        "bio/rseqc/read_gc",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_rseqc_read_duplication(run):
    run(
        "bio/rseqc/read_duplication",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_rseqc_read_distribution(run):
    run(
        "bio/rseqc/read_distribution",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_metaspades(run):
    run(
        "bio/spades/metaspades",
        [
            "snakemake",
            "run_metaspades",
            "--cores",
            "2",
            "--use-conda",
            "--resources",
            "mem_mem=1000",
            "time=15",
            "--show-failed-logs",
            "-F",
        ],
    )


def test_megahit(run):
    run(
        "bio/megahit",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
        ],
    )


def test_verifybamid2(run):
    run(
        "bio/verifybamid/verifybamid2",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_collapse_reads_to_fragments_bam(run):
    run(
        "bio/rbt/collapse_reads_to_fragments-bam",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_gatk_mutect2_calling_meta(run):
    run(
        "meta/bio/gatk_mutect2_calling",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "variant/Sample1.filtered.vcf.gz.tbi",
        ],
    )


def test_calc_consensus_reads(run):
    run(
        "meta/bio/calc_consensus_reads/",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/consensus/sampleA.bam",
        ],
    )


def test_bowtie2_sambamba_meta(run):
    run(
        "meta/bio/bowtie2_sambamba",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "results/mapped/Sample1.rmdup.bam.bai",
        ],
    )


def test_bazam_interleaved(run):
    run(
        "bio/bazam",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/reads/a.fastq.gz"],
    )


def test_bazam_separated(run):
    run(
        "bio/bazam",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/reads/a.r1.fastq.gz",
        ],
    )


def test_ragtag_correction(run):
    run(
        "bio/ragtag/correction",
        [
            "snakemake",
            "--cores",
            "1",
            "query_corrected_reference/ragtag.correct.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_ragtag_patch(run):
    run(
        "bio/ragtag/patch",
        [
            "snakemake",
            "--cores",
            "1",
            "query_reference.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_ragtag_scaffold(run):
    run(
        "bio/ragtag/scaffold",
        [
            "snakemake",
            "--cores",
            "1",
            "query_scaffold_reference/ragtag.scaffold.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_ragtag_merge(run):
    run(
        "bio/ragtag/merge",
        [
            "snakemake",
            "--cores",
            "1",
            "asm_merged.fasta",
            "--use-conda",
            "-F",
        ],
    )


def test_barrnap(run):
    run(
        "bio/barrnap",
        [
            "snakemake",
            "--cores",
            "1",
            "mitochondria.gff",
            "--use-conda",
            "-F",
        ],
    )


def test_encode_fastq_downloader(run):
    run(
        "bio/encode_fastq_downloader",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "ENCFF140TJA.fastq.gz"],
    )


def test_whatshap_haplotag(run):
    run(
        "bio/whatshap/haplotag",
        [
            "snakemake",
            "--cores",
            "1",
            "alignment.phased.bam",
            "--use-conda",
            "-F",
        ],
    )


def test_sortmerna_pe(run):
    run(
        "bio/sortmerna",
        [
            "snakemake",
            "--cores",
            "1",
            "aligned_1.fastq.gz",
            "--use-conda",
            "-F",
        ],
    )


def test_sortmerna_se(run):
    run(
        "bio/sortmerna",
        [
            "snakemake",
            "--cores",
            "1",
            "unpaired.fastq",
            "--use-conda",
            "-F",
        ],
    )


def test_tmb_pyeffgenomesize(run):
    run(
        "bio/tmb/pyeffgenomesize",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "minimal.txt"],
    )
    run(
        "bio/tmb/pyeffgenomesize",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "complete.txt"],
    )


def test_tmb_pytmb(run):
    run(
        "bio/tmb/pytmb",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


def test_root_hadd(run):
    run(
        "phys/root/hadd",
        ["snakemake", "--cores", "2", "--use-conda", "-F"],
    )


def test_root_define_columns(run):
    run(
        "phys/root/define_columns",
        ["snakemake", "--cores", "2", "--use-conda", "-F"],
    )


def test_root_filter_str(run):
    run(
        "phys/root/filter",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "ntuple0_str_output.root"],
    )


def test_root_filter_list(run):
    run(
        "phys/root/filter",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "ntuple0_list_output.root"],
    )


def test_root_filter_dict(run):
    run(
        "phys/root/filter",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "ntuple0_dict_output.root"],
    )


def test_root_rootcp(run):
    run(
        "phys/root/rootcp",
        ["snakemake", "--cores", "2", "--use-conda", "-F"],
    )


def test_emu_abundance(run):
    run(
        "bio/emu/abundance",
        [
            "snakemake",
            "--cores",
            "1",
            "sample_rel-abundance.tsv",
            "sample_emu_alignments.sam",
            "sample_unclassified.fas",
            "sample_unmapped.fas",
            "--use-conda",
            "-F",
        ],
    )


def test_emu_abundance_paired(run):
    run(
        "bio/emu/abundance",
        [
            "snakemake",
            "--cores",
            "1",
            "short_read_rel-abundance_paired.tsv",
            "short_read_emu_alignments_paired.sam",
            "short_read_unclassified_paired.fq",
            "short_read_unmapped_paired.fq",
            "--use-conda",
            "-F",
        ],
    )


def test_emu_collapse_taxonomy(run):
    run(
        "bio/emu/collapse-taxonomy",
        [
            "snakemake",
            "--cores",
            "1",
            "full_length_rel-abundance_collapsed.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_emu_combine_output(run):
    run(
        "bio/emu/combine-outputs",
        [
            "snakemake",
            "--cores",
            "1",
            "combined_abundances.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_emu_combine_output_split(run):
    run(
        "bio/emu/combine-outputs",
        [
            "snakemake",
            "--cores",
            "1",
            "counts.tsv",
            "taxonomy.tsv",
            "--use-conda",
            "-F",
        ],
    )


def test_toulligqc_sequencing_summary(run):
    run(
        "bio/toulligqc",
        [
            "snakemake",
            "--cores",
            "1",
            "toulligqc_sequencing_summary/report.html",
            "--use-conda",
            "-F",
        ],
    )


def test_toulligqc_bam(run):
    run(
        "bio/toulligqc",
        ["snakemake", "--cores", "1", "toulligqc_bam/report.html", "--use-conda", "-F"],
    )


def test_toulligqc_fastq(run):
    run(
        "bio/toulligqc",
        [
            "snakemake",
            "--cores",
            "1",
            "toulligqc_fastq/report.html",
            "--use-conda",
            "-F",
        ],
    )


def test_varlociraptor_alignment_properties(run):
    run(
        "bio/varlociraptor/estimate-alignment-properties",
        [
            "snakemake",
            "--cores",
            "1",
            "results/alignment-properties/NA12878.json",
            "--sdm",
            "conda",
            "-F",
        ],
    )


def test_varlociraptor_preprocess_variants(run):
    run(
        "bio/varlociraptor/preprocess-variants",
        [
            "snakemake",
            "--cores",
            "1",
            "results/observations/NA12878.bcf",
            "--sdm",
            "conda",
            "-F",
        ],
    )


def test_varlociraptor_call_variants(run):
    run(
        "bio/varlociraptor/call-variants",
        [
            "snakemake",
            "--cores",
            "1",
            "results/variant-calls/dummy-group.bcf",
            "--sdm",
            "conda",
            "-F",
        ],
    )


def test_varlociraptor_control_fdr(run):
    run(
        "bio/varlociraptor/control-fdr",
        [
            "snakemake",
            "--cores",
            "1",
            "results/variant-calls/dummy-group.fdr-controlled.bcf",
            "--sdm",
            "conda",
            "-F",
        ],
    )


def test_overturemaps_download(run):
    run(
        "geo/overturemaps/download",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "results/division_boundary.parquet",
        ],
    )


def test_pygadm_item(run):
    run(
        "geo/pygadm/item",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "results/mexico.parquet"],
    )


def test_trf_basic_recommended_params(run):
    run(
        "bio/trf",
        [
            "snakemake",
            "--cores",
            "1",
            "trf_output/small_test",
            "--use-conda",
            "--allowed-rules",
            "run_trf_basic",
        ],
    )


def test_trf_with_invalid_param_value(run):
    with pytest.raises(subprocess.CalledProcessError):
        run(
            "bio/trf",
            [
                "snakemake",
                "--cores",
                "1",
                "trf_output/small_test",
                "--use-conda",
                "--allowed-rules",
                "run_trf_with_missing_param_value",
            ],
        )


def test_trf_with_permissible_flags(run):
    run(
        "bio/trf",
        [
            "snakemake",
            "--cores",
            "1",
            "trf_output/small_test",
            "--use-conda",
            "--allowed-rules",
            "run_trf_permissible_flags",
        ],
    )


def test_trf_basic_with_uppercase_params(run):
    run(
        "bio/trf",
        [
            "snakemake",
            "--cores",
            "1",
            "trf_output/small_test",
            "--use-conda",
            "--allowed-rules",
            "run_trf_basic_uppercase",
        ],
    )


def test_mehari_download_transcript_db(run):
    run(
        "bio/mehari/download-transcript-db",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/mehari/dbs/transcripts.bin.zst",
            "--use-conda",
            "-F",
        ],
    )


def test_mehari_download_clinvar_db_sv(run):
    run(
        "bio/mehari/download-clinvar-db",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/mehari/dbs/clinvar/sv",
            "--use-conda",
            "-F",
        ],
    )


def test_mehari_annotate_seqvars(run):
    run(
        "bio/mehari/annotate-seqvars",
        [
            "snakemake",
            "--cores",
            "1",
            "resources/MT-ND2.annotated.bcf",
            "--use-conda",
            "-F",
            "--verbose",
        ],
    )


def test_rasterio_clip_geotiff(run):
    run(
        "geo/rasterio/clip",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "results/montenegro.tiff",
            "results/switzerland.tiff",
            "results/puerto_vallarta_small.tiff",
        ],
    )


def test_orthanq(run):
    run(
        "bio/orthanq",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "out/candidates",
            "out/candidates.vcf",
#             "out/preprocess_hla.bcf",
            "out/preprocess_virus.bcf",
            "out/calls_hla",
            "out/calls_virus",
        ],
    )
