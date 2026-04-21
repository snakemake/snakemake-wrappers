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
    def _run(
        wrapper,
        cmd=["snakemake"],
        cores=1,
        sdm=["conda"],
        check_log=None,
        compare_results_with_expected=None,
    ):
        wrapper_dir = Path(wrapper)

        is_meta_wrapper = wrapper.startswith("meta/")

        # Check meta.yaml file
        meta_path = wrapper_dir / "meta.yaml"
        try:
            with open(meta_path) as f:
                meta = yaml.load(f, Loader=yaml.BaseLoader)
        except Exception:
            raise ValueError(f"Unable to load or parse {meta_path}.")

        if meta.get("blacklisted"):
            pytest.skip("wrapper blacklisted")

        # Check if wrapper was modified
        if (DIFF_MASTER or DIFF_LAST_COMMIT) and not any(
            f.startswith(wrapper) for f in DIFF_FILES
        ):
            pytest.skip("wrapper not modified")

        # Prepare and copy files to temp test directory
        tmp_test_subdir = Path(tempfile.mkdtemp(dir=tmp_test_dir))
        origdir = Path.cwd()
        dst = tmp_test_subdir / "master"
        os.symlink(origdir, dst)
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

        # Switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd += [
            "--cores",
            str(cores),
            "--conda-cleanup-pkgs",
            "--printshellcmds",
            "--show-failed-logs",
            "--force",
            "--software-deployment-method",
        ] + sdm
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
                        diff = "".join(difflib.Differ().compare(gen_lines, exp_lines))
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
        # Clean up temp folder
        shutil.rmtree(tmp_test_subdir)
        return tmp_test_subdir

    return _run


def test_mmseqs2(run):
    run(
        "bio/mmseqs2/workflows",
        [
            "snakemake",
            "out/search/a.tsv",
            "out/cluster/a_b.cluster.tsv",
            "out/linclust/a_b.cluster.tsv",
            "out/taxonomy/a.lca.tsv",
            "out/rbh/a.tsv",
        ],
        cores=2,
        compare_results_with_expected={
            "out/search/a.tsv": "expected/search/a.tsv",
            "out/cluster/a_b.seqs.fas": "expected/cluster/a_b.seqs.fas",
            "out/cluster/a_b.cluster.tsv": "expected/cluster/a_b.cluster.tsv",
            "out/cluster/a_b.rep_seq.fasta": "expected/cluster/a_b.rep_seq.fasta",
            "out/linclust/a_b.seqs.fas": "expected/linclust/a_b.seqs.fas",
            "out/linclust/a_b.cluster.tsv": "expected/linclust/a_b.cluster.tsv",
            "out/linclust/a_b.rep_seq.fasta": "expected/linclust/a_b.rep_seq.fasta",
            "out/taxonomy/a.lca.tsv": "expected/taxonomy/a.lca.tsv",
            "out/taxonomy/a.report": "expected/taxonomy/a.report",
            "out/taxonomy/a.tophit_aln": "expected/taxonomy/a.tophit_aln",
            "out/taxonomy/a.tophit_report": "expected/taxonomy/a.tophit_report",
            "out/rbh/a.tsv": "expected/rbh/a.tsv",
        },
    )

    run(
        "bio/mmseqs2/db",
        [
            "snakemake",
            "out/databases/a",
            "out/createdb/a",
            "out/createtaxdb/a.done",
        ],
        cores=2,
        compare_results_with_expected={
            "out/databases/a.dbtype": "expected/databases/a.dbtype",
            "out/databases/a_h.dbtype": "expected/databases/a_h.dbtype",
            "out/databases/a.source": "expected/databases/a.source",
            "out/databases/a.version": "expected/databases/a.version",
            "out/createdb/a": "expected/createdb/a",
            "out/createdb/a.dbtype": "expected/createdb/a.dbtype",
            "out/createdb/a_h": "expected/createdb/a_h",
            "out/createdb/a_h.dbtype": "expected/createdb/a_h.dbtype",
            "out/createdb/a_h.index": "expected/createdb/a_h.index",
            "out/createdb/a.index": "expected/createdb/a.index",
            "out/createdb/a.lookup": "expected/createdb/a.lookup",
            "out/createdb/a.source": "expected/createdb/a.source",
        },
    )


def test_aria2c(run):
    run(
        "utils/aria2c",
        [
            "snakemake",
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
        cores=2,
    )


def test_agat(run):
    run(
        "bio/agat",
        [
            "snakemake",
            "out/agat_config.yaml",
            "out/agat_levels.yaml",
            "out/test_agat_convert_bed2gff.gff",
            "out/test_agat_convert_embl2gff.gff",
            "out/test_agat_convert_genscan2gff.gff",
            "out/test_agat_convert_mfannot2gff.gff",
            "out/test_agat_convert_minimap2_bam2gff_bam.gff",
            "out/test_agat_convert_minimap2_bam2gff_sam.gff",
            "out/test_agat_convert_sp_gff2bed.bed",
            "out/test_agat_convert_sp_gff2gtf.gtf",
            "out/test_agat_convert_sp_gff2tsv.tsv",
            "out/test_agat_convert_sp_gff2zff.dna",
            "out/test_agat_convert_sp_gxf2gxf.gff",
            "out/test_agat_sp_prokka_infer_name_from_attributes.gff",
            "out/test_agat_sp_add_intergenic_regions.gff",
            "out/test_agat_sp_add_introns.gff",
            "out/test_agat_sp_add_splice_sites.gff",
            "out/test_agat_sp_add_start_and_stop.gff",
            "out/test_agat_sp_alignment_output_style.gff",
            "out/test_agat_sp_clipN_seqExtremities_and_fixCoordinates.gff",
            "out/test_agat_sp_compare_two_annotations",
            "out/test_agat_sp_complement_annotations.gff",
            "out/test_agat_sp_ensembl_output_style.gff",
            "out/test_agat_sp_extract_attributes_ID.txt",
            "out/test_agat_sp_extract_sequences.fasta",
            "out/test_agat_sp_filter_by_ORF_size_matched.gff",
            "out/test_agat_sp_filter_by_locus_distance.gff",
            "out/test_agat_sp_filter_feature_by_attribute_presence.gff",
            "out/test_agat_sp_filter_feature_by_attribute_value.gff",
            "out/test_agat_sp_filter_feature_from_keep_list.gff",
            "out/test_agat_sp_filter_feature_from_kill_list.gff",
            "out/test_agat_sp_filter_gene_by_intron_numbers.gff",
            "out/test_agat_sp_filter_gene_by_length.gff",
            "out/test_agat_sp_filter_incomplete_gene_coding_models.gff",
            "out/test_agat_sp_filter_record_by_coordinates",
            "out/test_agat_sp_fix_cds_phases.gff",
            "out/test_agat_sp_fix_features_locations_duplicated.gff",
            "out/test_agat_sp_fix_fusion_all.gff",
            "out/test_agat_sp_fix_longest_ORF_all.gff",
            "out/test_agat_sp_fix_overlaping_genes.gff",
            "out/test_agat_sp_fix_small_exon_from_extremities.gff",
            "out/test_agat_sp_flag_premature_stop_codons.gff",
            "out/test_agat_sp_flag_short_introns.gff",
            "out/test_agat_sp_functional_statistics",
            "out/test_agat_sp_keep_longest_isoform.gff",
            "out/test_agat_sp_kraken_assess_liftover.gff",
            "out/test_agat_sp_list_short_introns.gff",
            "out/test_agat_sp_manage_IDs.gff",
            "out/test_agat_sp_manage_UTRs_report.txt",
            "out/test_agat_sp_manage_attributes.gff",
            "out/test_agat_sp_manage_functional_annotation.gff",
            "out/test_agat_sp_manage_introns_report.txt",
            "out/test_agat_sp_merge_annotations.gff",
            "out/test_agat_sp_move_attributes_within_records.gff",
            "out/test_agat_sp_prokka_fix_fragmented_gene_annotations",
            "out/test_agat_sp_sensitivity_specificity.txt",
            "out/test_agat_sp_separate_by_record_type",
            "out/test_agat_sp_statistics.txt",
            "out/test_agat_sq_add_attributes_from_tsv.gff",
            "out/test_agat_sq_add_hash_tag.gff",
            "out/test_agat_sq_add_locus_tag.gff",
            "out/test_agat_sq_filter_feature_from_fasta.gff",
            "out/test_agat_sq_list_attributes.txt",
            "out/test_agat_sq_manage_IDs.txt",
            "out/test_agat_sq_manage_attributes.gff",
            "out/test_agat_sq_mask.gff",
            "out/test_agat_sq_remove_redundant_entries.gff",
            "out/test_agat_sq_repeats_analyzer.gff",
            "out/test_agat_sq_reverse_complement.gff",
            "out/test_agat_sq_rfam_analyzer.tsv",
        ],
    )


def test_alignoth(run):
    run(
        "bio/alignoth",
        [
            "snakemake",
            "out/json_plot.vl.json",
            "out/plot.html",
            "output-dir/",
        ],
    )


def test_meta_alignoth_report(run):
    run(
        "meta/bio/alignoth_report",
        [
            "snakemake",
            "results/datavzrd-report/NA12878/",
        ],
    )


def test_miller(run):
    run(
        "utils/miller",
        [
            "snakemake",
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
        cores=2,
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


def test_jq(run):
    run(
        "utils/jq",
        [
            "snakemake",
            "out/sum.json",
        ],
        compare_results_with_expected={
            "out/sum.json": "expected/sum.json",
        },
    )


def test_taxonkit(run):
    run(
        "bio/taxonkit",
        [
            "snakemake",
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
            "results/a.fa.npo",
            "results/a.fas.bz2.npo",
            "results/a.fasta.gz.npo",
            "results/a.fq.npo",
            "results/a.fq.bz2.npo",
            "results/a.fastq.gz.npo",
            "results/empty.fq.bz2.npo",
            "results/empty.fq.gz.npo",
            "results/empty.fq.npo",
        ],
        compare_results_with_expected={
            "results/a.fa.log": "expected/a.fa.log",
            "results/a.fa.npc": "expected/a.fa.npc",
            "results/a.fas.bz2.npc": "expected/a.fas.bz2.npc",
            "results/a.fasta.gz.npc": "expected/a.fasta.gz.npc",
            "results/a.fq.log": "expected/a.fq.log",
            "results/a.fq.npc": "expected/a.fq.npc",
            "results/a.fq.bz2.npc": "expected/a.fq.bz2.npc",
            "results/a.fastq.gz.npc": "expected/a.fastq.gz.npc",
            "results/empty.fq.bz2.npa": "expected/empty.fq.bz2.npa",
            "results/empty.fq.bz2.npc": "expected/empty.fq.bz2.npc",
            "results/empty.fq.bz2.npo": "expected/empty.fq.bz2.npo",
            "results/empty.fq.gz.npa": "expected/empty.fq.gz.npa",
            "results/empty.fq.gz.npc": "expected/empty.fq.gz.npc",
            "results/empty.fq.gz.npo": "expected/empty.fq.gz.npo",
            "results/empty.fq.npa": "expected/empty.fq.npa",
            "results/empty.fq.npc": "expected/empty.fq.npc",
            "results/empty.fq.npo": "expected/empty.fq.npo",
        },
    )


def test_nonpareil_plot(run):
    run(
        "bio/nonpareil/plot",
        [
            "snakemake",
            "results/a.pdf",
            "results/b.pdf",
            "results/c.pdf",
            "results/d.pdf",
            "results/a.nomodel.pdf",
            "results/b.nomodel.pdf",
            "results/c.nomodel.pdf",
            "results/d.nomodel.pdf",
            "results/samples.pdf",
        ],
    )


def test_lofreq_call(run):
    run(
        "bio/lofreq/call",
        ["snakemake", "calls/a.vcf"],
    )


def test_lofreq_indelqual(run):
    run(
        "bio/lofreq/indelqual",
        [
            "snakemake",
            "out/indelqual/a.uindel.bam",
            "out/indelqual/a.dindel.bam",
        ],
        cores=2,
    )


def test_vsearch(run):
    run(
        "bio/vsearch",
        [
            "snakemake",
            "out/cluster_fast/a.profile",
            "out/maskfasta/a.fasta",
            "out/fastx_uniques/a.fastq",
            "out/fastx_uniques/a.fastq.gz",
            "out/fastx_uniques/a.fastq.bz2",
            "out/fastq_convert/a.fastq",
            "out/derep_fulllength/a.fasta",
            "out/derep_prefix/a.fasta",
        ],
    )


def test_swarm(run):
    run(
        "bio/swarm",
        [
            "snakemake",
            "out/a.seeds.fas",
            "out/a.gz.seeds.fas",
            "out/a.bz2.seeds.fas",
        ],
        cores=2,
    )


def test_bbtools(run):
    run(
        "bio/bbtools",
        [
            "snakemake",
        ],
        cores=2,
    )

    run(
        "bio/bbtools",
        [
            "snakemake",
            "--config",
            "reads_are_paired=False",
        ],
        cores=2,
    )


def test_gffread(run):
    run(
        "bio/gffread",
        [
            "snakemake",
            "transcripts.fa",
            "proteins.fa",
        ],
    )


def test_seqkit(run):
    run(
        "bio/seqkit",
        [
            "snakemake",
            "out/stats/a.tsv",
            "out/rmdup/name/a.fastq.gz",
            "out/rmdup/seq/a.fastq.gz",
            "out/fx2tab/a.tsv",
            "out/grep/name/a.fastq.gz",
            "out/grep/seq/a.fastq.gz",
            "out/subseq/bed/a.fa.gz",
            "out/subseq/gtf/a.fa.gz",
            "out/subseq/region/a.fa.gz",
            "out/seq/a.fa.gz",
            "out/common/a_b.fa.gz",
            "out/concat/a_b.fa.gz",
            "out/split2/part/a.1-of-2.fas",
            "out/split2/part/a.2-of-2.fas",
        ],
        cores=2,
    )


def test_sickle_pe(run):
    run(
        "bio/sickle/pe",
        [
            "snakemake",
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
            "a.1.fastq",
        ],
    )


def test_bwameth_memx(run):
    run(
        "bio/bwameth/memx",
        [
            "snakemake",
            "A.mem.bam",
            "A.mem2.bam",
            "AB_pe.mem.bam",
            "A.picard_sort.bam",
            "A.samtools_sort.bam",
        ],
        cores=2,
    )


def test_bwameth_index(run):
    run(
        "bio/bwameth/index",
        [
            "snakemake",
            "genome.fasta.bwameth.c2t.sa",
            "genome.fasta.bwameth.c2t.0123",
        ],
    )


def test_bwa_memx_index(run):
    run(
        "bio/bwa-memx/index",
        [
            "snakemake",
            "genome.fasta.sa",
            "genome.fasta.bwt.2bit.64",
            "genome.fasta.pos_packed",
        ],
    )


def test_bwa_memx_mem(run):
    run(
        "bio/bwa-memx/mem",
        [
            "snakemake",
            "bwa_memx_test",
        ],
    )


def test_purge_dups_calcuts(run):
    run(
        "bio/purge_dups/calcuts",
        ["snakemake", "out/calcuts.cutoffs"],
    )


def test_purge_dups_get_seqs(run):
    run(
        "bio/purge_dups/get_seqs",
        ["snakemake", "out/get_seqs.hap.fasta"],
    )


def test_purge_dups_ngscstat(run):
    run(
        "bio/purge_dups/ngscstat",
        ["snakemake", "out/ngscstat.cov"],
    )


def test_purge_dups_pbcstat(run):
    run(
        "bio/purge_dups/pbcstat",
        ["snakemake", "out/pbcstat.cov"],
    )


def test_purge_dups(run):
    run(
        "bio/purge_dups/purge_dups",
        ["snakemake", "out/purge_dups.bed"],
    )


def test_purge_dups_split_fa(run):
    run(
        "bio/purge_dups/split_fa",
        ["snakemake", "out/genome.split"],
    )


def test_quast(run):
    run(
        "bio/quast",
        ["snakemake", "a/treport.tsv"],
    )


def test_gfatools(run):
    run(
        "bio/gfatools",
        [
            "snakemake",
            "a.stat",
            "a.fas",
            "a.bed",
            "a.blacklist",
            "a.bubble",
            "a.asm",
            "a.sql",
        ],
    )


def test_hifiasm(run):
    run(
        "bio/hifiasm",
        ["snakemake", "hifiasm/a.a_ctg.gfa"],
        cores=2,
    )


def meryl_count(run):
    run(
        "bio/meryl/count",
        ["snakemake", "genome"],
        cores=2,
    )


def meryl_sets(run):
    run(
        "bio/meryl/sets",
        [
            "snakemake",
            "genome_union",
            "genome_intersect",
            "genome_subtract",
            "genome_difference",
        ],
    )


def meryl_stats(run):
    run(
        "bio/meryl/stats",
        ["snakemake", "genome.stats"],
    )


def test_genomescope(run):
    run(
        "bio/genomescope",
        ["snakemake", "a/model.txt"],
    )


def test_bellerophon(run):
    run(
        "bio/bellerophon",
        ["snakemake", "out.sam", "out.bam"],
        cores=2,
    )


def test_pretext_map(run):
    run(
        "bio/pretext/map",
        ["snakemake", "map.pretext"],
    )


def test_pretext_snapshot(run):
    run(
        "bio/pretext/snapshot",
        [
            "snakemake",
            "full_map.png",
            "full_map.jpg",
        ],
    )


def test_pretext_graph(run):
    run(
        "bio/pretext/graph",
        ["snakemake", "a.pretext"],
    )


def test_salsa2(run):
    run(
        "bio/salsa2",
        ["snakemake", "out/a.agp"],
    )


def test_merqury(run):
    run(
        "bio/merqury",
        [
            "snakemake",
            "results/haploid/out.qv",
            "results/diploid/out.qv",
        ],
    )


def test_mashmap(run):
    run("bio/mashmap", ["snakemake", "mashmap.out"], cores=2)

    run(
        "bio/mashmap",
        [
            "snakemake",
            "mashmap.out",
            "-s",
            "Snakefile_reflist.smk",
        ],
        cores=2,
    )


def test_liftoff(run):
    run(
        "bio/liftoff",
        [
            "snakemake",
            "genome_annotation_genome.gff3",
        ],
    )


def test_biobambam2_bamsormadup(run):
    run(
        "bio/biobambam2/bamsormadup",
        ["snakemake", "dedup/a.bam"],
    )


def test_bustools_text(run):
    run(
        "bio/bustools/text",
        ["snakemake", "file.tsv", "file2.tsv"],
    )


def test_bustools_count(run):
    run(
        "bio/bustools/count",
        ["snakemake", "buscount.mtx"],
    )


def test_bustools_sort(run):
    run(
        "bio/bustools/sort",
        ["snakemake", "sorted.bus"],
    )


def test_open_cravat_run(run):
    run(
        "bio/open-cravat/run",
        ["snakemake"],
    )


def test_open_cravat_module(run):
    run(
        "bio/open-cravat/module",
        ["snakemake"],
    )


def test_vcf2maf(run):
    run(
        "bio/vcf2maf/vcf2maf",
        [
            "snakemake",
            "small.maf",
        ],
    )


def test_vcf2vcf(run):
    run(
        "bio/vcf2maf/vcf2vcf",
        [
            "snakemake",
            "corrected.vcf",
        ],
    )


def test_meta_varscan2_snpeff(run):
    run(
        "meta/bio/varscan2_snpeff",
        [
            "snakemake",
            "snpeff/annotated.vcf",
        ],
    )


def test_meta_salmon_tximport(run):
    run(
        "meta/bio/salmon_tximport",
        [
            "snakemake",
            "tximport/SummarizedExperimentObject.RDS",
        ],
        cores=2,
    )


def test_meta_dada2_se(run):
    run(
        "meta/bio/dada2_se",
        [
            "snakemake",
        ],
    )


def test_meta_dada2_pe(run):
    run(
        "meta/bio/dada2_pe",
        [
            "snakemake",
            "results/dada2/taxa.RDS",
            "reports/dada2/quality-profile/a-quality-profile.png",
            "reports/dada2/quality-profile/b-quality-profile.png",
        ],
    )


def test_adapterremoval(run):
    run(
        "bio/adapterremoval",
        [
            "snakemake",
            "trimmed/pe/a_R1.fastq.gz",
            "trimmed/pe/a_R2.fastq.gz",
            "trimmed/pe/a.singleton.fastq.gz",
            "trimmed/pe/a.collapsed.fastq.gz",
            "trimmed/pe/a.collapsed_trunc.fastq.gz",
            "trimmed/pe/a.discarded.fastq.gz",
            "stats/pe/a.settings",
            "trimmed/se/a.fastq.gz",
            "trimmed/se/a.discarded.fastq.gz",
            "stats/se/a.settings",
        ],
    )


def test_mapdamage2(run):
    run(
        "bio/mapdamage2",
        [
            "snakemake",
            "results/rescale/a.bam",
            "results/all/a.bam",
        ],
    )


def test_microphaser_normal(run):
    run(
        "bio/microphaser/normal",
        ["snakemake", "out/a.fasta"],
    )


def test_microphaser_somatic(run):
    run(
        "bio/microphaser/somatic",
        ["snakemake", "out/a.info.tsv"],
    )


def test_microphaser_build_reference(run):
    run(
        "bio/microphaser/build_reference",
        ["snakemake", "out/peptides.bin"],
    )


def test_microphaser_filter(run):
    run(
        "bio/microphaser/filter",
        ["snakemake", "out/peptides.wt.fasta"],
    )


def test_dada2_quality_profile(run):
    run(
        "bio/dada2/quality-profile",
        [
            "snakemake",
            "reports/dada2/quality-profile/a-quality-profile.png",
            "reports/dada2/quality-profile/a.1-quality-profile.png",
        ],
    )


def test_dada2_filter_trim(run):
    run(
        "bio/dada2/filter-trim",
        [
            "snakemake",
            "filtered-se/a.1.fastq.gz",
            "filtered-pe/a.1.fastq.gz",
        ],
    )


def test_dada2_dereplicate_fastq(run):
    run(
        "bio/dada2/dereplicate-fastq",
        ["snakemake", "uniques/a.1.RDS"],
    )


def test_dada2_learn_errors(run):
    run(
        "bio/dada2/learn-errors",
        ["snakemake", "results/dada2/model_1.RDS"],
    )


def test_dada2_sample_inference(run):
    run(
        "bio/dada2/sample-inference",
        ["snakemake", "denoised/a.1.RDS"],
    )


def test_dada2_merge_pairs(run):
    run(
        "bio/dada2/merge-pairs",
        ["snakemake", "merged/a.RDS"],
    )


def test_dada2_make_table(run):
    run(
        "bio/dada2/make-table",
        [
            "snakemake",
            "results/dada2/seqTab-se.RDS",
            "results/dada2/seqTab-pe.RDS",
        ],
    )


def test_dada2_remove_chimeras(run):
    run(
        "bio/dada2/remove-chimeras",
        ["snakemake", "results/dada2/seqTab.nochim.RDS"],
    )


def test_dada2_collapse_nomismatch(run):
    run(
        "bio/dada2/collapse-nomismatch",
        [
            "snakemake",
            "results/dada2/seqTab.collapsed.RDS",
        ],
    )


def test_dada2_assign_taxonomy(run):
    run(
        "bio/dada2/assign-taxonomy",
        ["snakemake", "results/dada2/taxa.RDS"],
    )


def test_dada2_assign_species(run):
    run(
        "bio/dada2/assign-species",
        [
            "snakemake",
            "results/dada2/genus-species-taxa.RDS",
        ],
    )


def test_dada2_add_species(run):
    run(
        "bio/dada2/add-species",
        ["snakemake", "results/dada2/taxa-sp.RDS"],
    )


def test_datavzrd(run):
    run(
        "utils/datavzrd",
        ["snakemake", "results/datavzrd-report/A"],
    )


def test_deseq2_deseqdataset(run):
    run(
        "bio/deseq2/deseqdataset",
        [
            "snakemake",
            "dds_htseq.RDS",
            "dds_minimal.RDS",
            "dds_txi.RDS",
            "dds_se.RDS",
            "dds_rmatrix.RDS",
            "dds_matrix.RDS",
        ],
    )


def test_deseq2_wald(run):
    run(
        "bio/deseq2/wald",
        [
            "snakemake",
            "dge_normal.tsv",
            "dge_ashr.tsv",
            "dge_apeglm.tsv",
            "dge_2f.tsv",
            "dge_1s.tsv",
        ],
    )


def test_meta_arriba_star(run):
    run(
        "meta/bio/star_arriba",
        ["snakemake", "results/arriba/a.fusions.tsv"],
    )


def test_csvtk(run):
    run(
        "utils/csvtk",
        [
            "snakemake",
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
    run(
        "utils/xsv",
        [
            "snakemake",
            "xsv/split/0.csv",
            "xsv/table.txt",
            "xsv/stats.txt",
            "xsv/split",
            "xsv/sort.csv",
            "xsv/slice.csv",
            "xsv/select.csv",
            "xsv/search.csv",
            "xsv/sample.csv",
            "xsv/join.csv",
            "xsv/input.csv",
            "table.csv.idx",
            "xsv/headers_all.csv",
            "xsv/headers.csv",
            "xsv/frequency.csv",
            "xsv/fmt.tsv",
            "xsv/flatten.csv",
            "xsv/fixlength.csv",
            "xsv/count_csv.csv",
            "xsv/count_tsv.csv",
            "xsv/catrows.csv",
            "xsv/catcols.csv",
        ],
    )


def test_meta_bwa_mapping(run):
    run(
        "meta/bio/bwa_mapping",
        [
            "snakemake",
            "results/mapped/a.bam.bai",
        ],
    )


def test_cnvkit_batch(run):
    run(
        "bio/cnvkit/batch",
        [
            "snakemake",
            "cnvkit/reference.cnn",
            "cnvkit/a.antitargetcoverage.cnn",
            "cnvkit/a.bintest.cns",
            "cnvkit/a.cnr",
            "cnvkit/a.cns",
            "cnvkit/a.call.cns",
            "cnvkit/a.targetcoverage.cnn",
        ],
    )


def test_cnvkit_call(run):
    run(
        "bio/cnvkit/call",
        [
            "snakemake",
            "test.call.cns",
        ],
    )


def test_cnvkit_diagram(run):
    run(
        "bio/cnvkit/diagram",
        [
            "snakemake",
            "test.cns.pdf",
            "test.cnr.pdf",
            "test.cnn.pdf",
            "test.cnscnr.pdf",
        ],
    )


def test_cnvkit_antitarget(run):
    run(
        "bio/cnvkit/antitarget",
        [
            "snakemake",
            "test.antitarget.bed",
        ],
    )


def test_cnvkit_target(run):
    run(
        "bio/cnvkit/target",
        [
            "snakemake",
            "test.target.bed",
        ],
    )


def test_cnvkit_export(run):
    run(
        "bio/cnvkit/export",
        [
            "snakemake",
            "test.cns.seg",
            "test.cns.vcf",
            "test.cns.vcf.gz",
            "test.cns.cdt",
            "test.cns.jtv",
        ],
    )


def test_enhanced_volcano(run):
    run(
        "bio/enhancedvolcano",
        [
            "snakemake",
            "volcano_tsv.png",
            "volcano_csv.svg",
            "volcano_rds.svg",
        ],
    )


def test_goleft_indexcov(run):
    run(
        "bio/goleft/indexcov",
        ["snakemake"],
    )


def test_gridss_call(run):
    run(
        "bio/gridss/call",
        [
            "snakemake",
            "--show-failed-logs",
            "vcf/group.vcf",
        ],
    )


def test_gridss_assemble(run):
    run(
        "bio/gridss/assemble",
        [
            "snakemake",
            "--show-failed-logs",
            "assembly/group.bam",
        ],
    )


def test_gridss_preprocess(run):
    run(
        "bio/gridss/preprocess",
        [
            "snakemake",
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
            "call/A-bounds.txt",
            "call/A-genotype.txt",
            "call/A-unplaced.txt",
        ],
    )


def test_strling_merge(run):
    run(
        "bio/strling/merge",
        ["snakemake", "merged/group-bounds.txt"],
    )


def test_strling_extract(run):
    run(
        "bio/strling/extract",
        ["snakemake", "extract/A.bin"],
    )


def test_strling_index(run):
    run(
        "bio/strling/index",
        [
            "snakemake",
            "reference/genome.fasta.str",
            "reference/genome.fasta.fai",
        ],
    )


def test_vembrane_filter(run):
    run(
        "bio/vembrane/filter",
        ["snakemake", "filtered/out.vcf"],
    )


def test_vembrane_table(run):
    run(
        "bio/vembrane/table",
        ["snakemake", "table/out.tsv"],
    )


def test_shovill(run):
    run(
        "bio/shovill",
        [
            "snakemake",
            "assembly/input.spades.assembly.fa",
            "assembly/input.spades.contigs.fa",
        ],
    )


def test_prinseq_plus_plus(run):
    run(
        "bio/prinseq-plus-plus",
        [
            "snakemake",
            "results/a.fq",
            "results/a.fq.gz",
            "results/a.fasta",
            "results/a.fas.gz",
            "results/a.R1.fq.gz",
        ],
    )


def test_seqtk(run):
    run(
        "bio/seqtk",
        [
            "snakemake",
            "results/fq2fas/a.fasta",
            "results/convBQ/a.fasta",
            "results/subseq_list/a.fq.gz",
            "results/mergepe/a.fastq.gz",
            "results/sample_se/a.fastq.gz",
            "results/sample_pe/a.1.fastq.gz",
            "results/sample_pe/a.2.fastq.gz",
        ],
    )


def test_sequali(run):
    run(
        "bio/sequali",
        [
            "snakemake",
            "report/se/a.html",
            "report/se/a.json",
            "report/se/a.adapter.html",
            "report/se/a.adapter.json",
            "report/pe/a.images.html",
            "report/pe/a.images.json",
            "report/pe/a.zip",
        ],
    )


def test_arriba(run):
    run(
        "bio/arriba",
        [
            "snakemake",
            "fusions/A.tsv",
            "fusions/A.discarded.tsv",
            "fusions/A.with_sv.tsv",
            "fusions/A.with_sv.discarded.tsv",
        ],
    )


def test_art_profiler_illumina(run):
    run(
        "bio/art/profiler_illumina",
        [
            "snakemake",
            "profiles/a.1.txt",
            "profiles/a.2.txt",
        ],
    )


def test_pyroe_idtoname(run):
    run(
        "bio/pyroe/idtoname",
        [
            "snakemake",
            "id2name.gtf.tsv",
            "id2name.gff3.tsv",
        ],
    )


def test_pyroe_makesplicedunspliced(run):
    run(
        "bio/pyroe/makeunspliceunspliced/",
        [
            "snakemake",
            "spliceu.fa",
        ],
    )


def test_pyroe_makesplicedintronic(run):
    run(
        "bio/pyroe/makesplicedintronic",
        [
            "snakemake",
            "splici_full/spliced_intronic_sequences.fasta",
        ],
    )


def test_bcftools_filter(run):
    run(
        "bio/bcftools/filter",
        [
            "snakemake",
            "a.filter_sample.vcf",
            "a.filter.vcf",
            "a.filter.vcf.gz",
            "a.filter.bcf",
            "a.filter.uncompressed.bcf",
        ],
    )


def test_bcftools_sort(run):
    run(
        "bio/bcftools/sort",
        ["snakemake", "a.sorted.bcf"],
    )


def test_bcftools_call(run):
    run(
        "bio/bcftools/call",
        ["snakemake", "a.calls.bcf"],
    )


def test_bcftools_index(run):
    run(
        "bio/bcftools/index",
        ["snakemake", "a.bcf.csi"],
    )


def test_bcftools_concat(run):
    run(
        "bio/bcftools/concat",
        ["snakemake", "all.bcf"],
    )


def test_bcftools_merge(run):
    run(
        "bio/bcftools/merge",
        ["snakemake", "all.bcf"],
    )


def test_bcftools_mpileup(run):
    run(
        "bio/bcftools/mpileup",
        ["snakemake", "pileups/a.pileup.bcf"],
    )


def test_bcftools_reheader(run):
    run(
        "bio/bcftools/reheader",
        [
            "snakemake",
            "a.reheader.bcf",
            "a.reheader_map.bcf",
        ],
    )


def test_bcftools_stats(run):
    run(
        "bio/bcftools/stats",
        ["snakemake", "a.bcf.stats.txt"],
    )


def test_bcftools_norm(run):
    run(
        "bio/bcftools/norm",
        ["snakemake", "a.norm.vcf"],
    )


def test_bcftools_view(run):
    run(
        "bio/bcftools/view",
        [
            "snakemake",
            "a.view.vcf",
            "a.view.vcf.gz",
            "a.view.bcf",
            "a.view.uncompressed.bcf",
        ],
    )


def test_bedtools_bamtobed(run):
    run(
        "bio/bedtools/bamtobed",
        ["snakemake", "a.bed", "a.bed.gz"],
    )


def test_bedtools_genomecov(run):
    run(
        "bio/bedtools/genomecov",
        [
            "snakemake",
            "genomecov_bam/a.genomecov",
            "genomecov_bed/a.genomecov",
        ],
    )


def test_bedtools_complement(run):
    run(
        "bio/bedtools/complement",
        [
            "snakemake",
            "results/bed-complement/a.complement.bed",
            "results/bed-complement/a.complement.bed.gz",
            "results/vcf-complement/a.complement.vcf",
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
            "results/bed-sorted/a.sorted.bed",
            "results/bed-sorted/a.sorted_by_file.bed",
            "results/vcf-sorted/a.sorted_by_file.vcf",
        ],
    )


def test_bedtools_split(run):
    run(
        "bio/bedtools/split",
        [
            "snakemake",
            "results/a.1-of-2.bed",
            "results/a.2-of-2.bed",
        ],
    )


def test_bedtools_intersect(run):
    run(
        "bio/bedtools/intersect",
        [
            "snakemake",
            "A_B.intersected.bed",
            "A_B.intersected.bed.gz",
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
            "A.merged.bed",
            "AB.merged.bed",
        ],
    )


def test_bedtools_slop(run):
    run(
        "bio/bedtools/slop",
        ["snakemake", "A.slop.bed"],
    )


def test_bgzip(run):
    run("bio/bgzip", ["snakemake", "test.vcf.gz"])


def test_blast_makeblastdb(run):
    run(
        "bio/blast/makeblastdb",
        [
            "snakemake",
            "results/genome.fasta.ndb",
            "results/genome.fasta.nhr",
            "results/genome.fasta.nin",
            "results/genome.fasta.not",
            "results/genome.fasta.nsq",
            "results/genome.fasta.ntf",
            "results/genome.fasta.nto",
            "results/protein.fasta.pdb",
            "results/protein.fasta.phr",
            "results/protein.fasta.pin",
            "results/protein.fasta.pot",
            "results/protein.fasta.psq",
            "results/protein.fasta.ptf",
            "results/protein.fasta.pto",
        ],
    )


def test_blast_blastn(run):
    run(
        "bio/blast/blastn",
        ["snakemake", "a.blast.txt"],
    )


def test_bowtie2_align(run):
    run(
        "bio/bowtie2/align",
        [
            "snakemake",
            "mapped_idx/a.cram",
            "mapped_idx/a.bam",
            "mapped/a.bam",
            "mapped_se_gz/a.bam",
        ],
        cores=2,
    )


def test_bowtie2_build(run):
    run(
        "bio/bowtie2/build",
        [
            "snakemake",
            "genome.1.bt2",
            "genome.1.bt2l",
        ],
    )


def test_samshee(run):
    run(
        "bio/samshee",
        [
            "snakemake",
            "samples.json",
            "samples.csv",
            "samples_schema.json",
        ],
    )


def test_bwa_mem(run):
    run(
        "bio/bwa/mem",
        ["snakemake", "mapped/a.bam"],
    )

    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "mapped/a.bam",
            "mapped_with_index_bai/a.bam",
            "mapped_with_index_bai/a.bam.bai",
            "mapped_with_index_csi/a.bam",
            "mapped_with_index_csi/a.bam.csi",
            "-s",
            "Snakefile_samtools",
        ],
    )

    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_fgbio",
        ],
    )

    run(
        "bio/bwa/mem",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_bwa_aln(run):
    run(
        "bio/bwa/aln",
        [
            "snakemake",
            "sai/a.1.sai",
            "sai/a.2.sai",
        ],
    )


def test_bwa_index(run):
    run(
        "bio/bwa/index",
        [
            "snakemake",
            "genome.bwtsw.amb",
            "genome.bwtsw.ann",
            "genome.bwtsw.bwt",
            "genome.bwtsw.pac",
            "genome.bwtsw.sa",
            "genome.is.amb",
            "genome.is.ann",
            "genome.is.bwt",
            "genome.is.pac",
            "genome.is.sa",
            "genome.rb2.amb",
            "genome.rb2.ann",
            "genome.rb2.bwt",
            "genome.rb2.pac",
            "genome.rb2.sa",
        ],
    )


def test_bwa_samxe(run):
    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "mapped/a.se.sam",
            "mapped/a.pe.sam",
            "mapped/a.se.bam",
            "mapped/a.pe.bam",
        ],
    )

    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "mapped/a.se.samtools_sort.bam",
            "mapped/a.se.samtools_sort.sam",
            "mapped/a.pe.samtools_sort.bam",
            "mapped/a.pe.samtools_sort.sam",
            "-s",
            "Snakefile_samtools",
        ],
    )

    run(
        "bio/bwa/samxe",
        [
            "snakemake",
            "mapped/a.se.picard_sort.sam",
            "mapped/a.pe.picard_sort.sam",
            "mapped/a.se.picard_sort.bam",
            "mapped/a.pe.picard_sort.bam",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_bwa_sampe(run):
    run(
        "bio/bwa/sampe",
        ["snakemake", "mapped/a.bam"],
    )

    run(
        "bio/bwa/sampe",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_samtools",
        ],
    )

    run(
        "bio/bwa/sampe",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_bwa_samse(run):
    run(
        "bio/bwa/samse",
        ["snakemake", "mapped/a.bam"],
    )

    run(
        "bio/bwa/samse",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_samtools",
        ],
    )

    run(
        "bio/bwa/samse",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_bwa_mem_samblaster(run):
    run(
        "bio/bwa/mem-samblaster",
        ["snakemake", "mapped/a.bam"],
    )


def test_bwa_meme(run):
    run(
        "bio/bwa-meme/mem",
        [
            "snakemake",
            "bwa_meme_test",
        ],
    )


def test_bwa_mem2_mem(run):
    run(
        "bio/bwa-mem2/mem",
        ["snakemake", "mapped/a.bam"],
        cores=2,
    )
    run(
        "bio/bwa-mem2/mem",
        ["snakemake", "mapped/a.sam"],
        cores=2,
    )

    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_samtools",
        ],
        cores=2,
    )

    run(
        "bio/bwa-mem2/mem",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_picard",
        ],
        cores=2,
    )


def test_bwa_mem2_index(run):
    run(
        "bio/bwa-mem2/index",
        [
            "snakemake",
            "genome.fasta.amb",
            "genome.fasta.ann",
            "genome.fasta.0123",
            "genome.fasta.bwt.2bit.64",
            "genome.fasta.pac",
        ],
    )


def test_bwa_mem2_mem_samblaster(run):
    run(
        "bio/bwa-mem2/mem-samblaster",
        ["snakemake", "mapped/a.bam"],
    )


def test_dragmap_build(run):
    run(
        "bio/dragmap/build",
        ["snakemake", "genome/hash_table.cfg"],
    )


def test_dragmap_align(run):
    run(
        "bio/dragmap/align",
        ["snakemake", "mapped/a.bam"],
    )

    run(
        "bio/dragmap/align",
        [
            "snakemake",
            "mapped/a.bam",
            "mapped_with_index/a.bam",
            "mapped_with_index/a.bam.csi",
            "-s",
            "Snakefile_samtools",
        ],
    )

    run(
        "bio/dragmap/align",
        [
            "snakemake",
            "mapped/a.bam",
            "-s",
            "Snakefile_picard",
        ],
    )


def test_chopper(run):
    run(
        "bio/chopper",
        [
            "snakemake",
            "treated/filter.fastq",
            "treated/filter.fastq.gz",
            "treated/contam.fastq",
        ],
        compare_results_with_expected={
            "treated/filter.fastq": "expected/filter.fastq",
            "treated/contam.fastq": "expected/contam.fastq",
        },
    )


def test_clustalo(run):
    run(
        "bio/clustalo",
        ["snakemake", "test.msa.fa"],
    )


def test_cnv_facets(run):
    run(
        "bio/cnv_facets",
        [
            "snakemake",
            "CNV_bam.vcf.gz",
            "CNV_pileup.vcf.gz",
        ],
    )


def test_coolpuppy(run):
    run(
        "bio/coolpuppy",
        ["snakemake", "CN_1000000.clpy"],
    )


def test_cooltools_insulation(run):
    run(
        "bio/cooltools/insulation",
        ["snakemake", "CN_1000000.insulation.tsv"],
    )


def test_cooltools_expected_cis(run):
    run(
        "bio/cooltools/expected_cis",
        [
            "snakemake",
            "CN_1000000.cis.expected.tsv",
        ],
    )


def test_cooltools_expected_trans(run):
    run(
        "bio/cooltools/expected_trans",
        [
            "snakemake",
            "CN_1000000.trans.expected.tsv",
        ],
    )


def test_cooltools_eigs_cis(run):
    run(
        "bio/cooltools/eigs_cis",
        [
            "snakemake",
            "CN_1000000.cis.vecs.tsv",
            "CN_1000000.cis.lam.tsv",
            "CN_1000000.cis.bw",
        ],
    )


def test_cooltools_eigs_trans(run):
    run(
        "bio/cooltools/eigs_trans",
        [
            "snakemake",
            "CN_1000000.trans.vecs.tsv",
            "CN_1000000.trans.lam.tsv",
            "CN_1000000.trans.bw",
        ],
    )


def test_cooltools_saddle(run):
    run(
        "bio/cooltools/saddle",
        ["snakemake", "CN_1000000.saddledump.npz"],
    )


def test_cooltools_pileup(run):
    run(
        "bio/cooltools/pileup",
        ["snakemake", "CN_1000000.pileup.npz"],
    )


def test_cooltools_dots(run):
    run(
        "bio/cooltools/dots",
        ["snakemake", "HFF_10000.dots.bedpe"],
    )


def test_cooltools_genome_binnify(run):
    run(
        "bio/cooltools/genome/binnify",
        ["snakemake", "hg38_1000000_bins.bed"],
    )


def test_cooltools_genome_gc(run):
    run(
        "bio/cooltools/genome/gc",
        ["snakemake", "gc_100000.tsv"],
    )


def test_cutadapt_pe(run):
    run(
        "bio/cutadapt/pe",
        ["snakemake", "trimmed/a.1.fastq"],
    )


def test_cutadapt_se(run):
    run(
        "bio/cutadapt/se",
        ["snakemake", "trimmed/a.fastq"],
    )


def test_deeptools_computematrix(run):
    run(
        "bio/deeptools/computematrix",
        [
            "snakemake",
            "matrix_files/matrix.gz",
            "matrix_files/matrix.tab",
            "matrix_files/matrix.bed",
        ],
    )


def test_deeptools_plotcorrelation(run):
    run(
        "bio/deeptools/plotcorrelation",
        ["snakemake", "bins.svg"],
    )


def test_deeptools_bampe_fragmentsize(run):
    # Test basic functionality
    run(
        "bio/deeptools/bampefragmentsize",
        ["snakemake", "results/histogram.png"],
    )
    # Test with multiple BAMs and custom labels
    run(
        "bio/deeptools/bampefragmentsize",
        [
            "snakemake",
            "results/histogram.png",
            "--config",
            "labels='sample1,sample2'",
        ],
    )
    # Test with blacklist
    run(
        "bio/deeptools/bampefragmentsize",
        [
            "snakemake",
            "results/histogram.png",
            "--config",
            "blacklist='regions.bed'",
        ],
    )


def test_deeptools_multibigwigsummary(run):
    run(
        "bio/deeptools/multibigwigsummary",
        [
            "snakemake",
            "bins.npz",
            "bed.npz",
        ],
    )


def test_deeptools_bamcoverage(run):
    run(
        "bio/deeptools/bamcoverage",
        [
            "snakemake",
            "a.coverage.bw",
            "a.coverage_code.bw",
            "a.coverage_no_params.bw",
        ],
    )


def test_deeptools_alignmentsieve(run):
    run(
        "bio/deeptools/alignmentsieve",
        [
            "snakemake",
            "filtered.bam",
        ],
    )


def test_deeptools_plotpca(run):
    run(
        "bio/deeptools/plotpca",
        [
            "snakemake",
            "pca.svg",
        ],
    )


def test_deeptools_plotheatmap(run):
    run(
        "bio/deeptools/plotheatmap",
        [
            "snakemake",
            "plot_heatmap/heatmap.png",
            "plot_heatmap/heatmap_regions.bed",
            "plot_heatmap/heatmap_matrix.tab",
        ],
    )


def test_deeptools_plotfingerprint(run):
    run(
        "bio/deeptools/plotfingerprint",
        [
            "snakemake",
            "plot_fingerprint/plot_fingerprint.png",
            "plot_fingerprint/raw_counts.tab",
            "plot_fingerprint/qc_metrics.txt",
        ],
    )


def test_deeptools_plotprofile(run):
    run(
        "bio/deeptools/plotprofile",
        [
            "snakemake",
            "plot_profile/plot.png",
            "plot_profile/regions.bed",
            "plot_profile/data.tab",
        ],
    )


def test_deeptools_plotcoverage(run):
    run(
        "bio/deeptools/plotcoverage",
        [
            "snakemake",
            "coverage.png",
        ],
    )


def test_deepvariant(run):
    run(
        "bio/deepvariant",
        [
            "snakemake",
            "calls/a.vcf.gz",
            "gvcf_calls/a.vcf.gz",
            "gvcf_calls/a.g.vcf.gz",
        ],
    )


def test_epic_peaks(run):
    run(
        "bio/epic/peaks",
        ["snakemake", "epic/enriched_regions.bed"],
    )


def test_falco(run):
    run(
        "bio/falco",
        ["snakemake", "qc/falco/a.html"],
    )


def test_fastp(run):
    run(
        "bio/fastp",
        [
            "snakemake",
            "trimmed/se/a.fastq",
            "report/se/a.html",
            "report/se/a.json",
            "trimmed/pe/a.1.fastq",
            "trimmed/pe/a.2.fastq",
            "report/pe/a.html",
            "report/pe/a.json",
            "report/pe_wo_trimming/a.html",
            "report/pe_wo_trimming/a.json",
        ],
    )


def test_fastqc(run):
    run(
        "bio/fastqc",
        ["snakemake", "qc/fastqc/a.html"],
    )


def test_fastq_screen(run):
    run(
        "bio/fastq_screen",
        [
            "snakemake",
            "qc/a.fastq_screen.txt",
            "qc/a.fastq_screen_conf.txt",
            "qc/a.fastq_screen_nopng.txt",
        ],
    )


def test_fasttree(run):
    run(
        "bio/fasttree",
        ["snakemake", "test-proteins.nwk"],
    )


def test_fgbio_annotatebamwithumis(run):
    run(
        "bio/fgbio/annotatebamwithumis",
        [
            "snakemake",
            "mapped/a.annotated.bam",
            "mapped/a-a.annotated.bam",
        ],
    )


def test_fgbio_collectduplexseqmetrics(run):
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
        ],
    )


def test_fgbio_filterconsensusreads(run):
    run(
        "bio/fgbio/filterconsensusreads",
        ["snakemake", "mapped/a.filtered.bam"],
    )


def test_fgbio_groupreadsbyumi(run):
    run(
        "bio/fgbio/groupreadsbyumi",
        [
            "snakemake",
            "mapped/a.gu.bam",
            "mapped/a.gu.histo.tsv",
        ],
    )


def test_fgbio_setmateinformation(run):
    run(
        "bio/fgbio/setmateinformation",
        ["snakemake", "mapped/a.mi.bam"],
    )


def test_fgbio_callmolecularconsensusreads(run):
    run(
        "bio/fgbio/callmolecularconsensusreads",
        ["snakemake", "mapped/a.m3.bam"],
    )


def test_filtlong(run):
    run(
        "bio/filtlong",
        ["snakemake", "reads.filtered.fastq"],
    )


def test_freebayes(run):
    for c in [1, 2]:
        run(
            "bio/freebayes",
            [
                "snakemake",
                "calls/a.bcf",
                "calls/a.vcf",
                "calls/a.vcf.gz",
            ],
            cores=c,
        )


def test_gdc_api_bam_slicing(run):
    def check_log(log):
        assert "error" in log and "token" in log

    run(
        "bio/gdc-api/bam-slicing",
        ["snakemake", "raw/testing_sample.bam"],
        check_log=check_log,
    )


def test_gdc_client_download(run):
    run(
        "bio/gdc-client/download",
        ["snakemake", "raw/testing_sample.maf.gz"],
    )


def test_happy_prepy(run):
    run(
        "bio/hap.py/pre.py",
        [
            "snakemake",
            "normalized/variants.vcf",
            "normalized/variants.vcf.gz",
        ],
    )


def test_hisat2_index(run):
    run(
        "bio/hisat2/index",
        [
            "snakemake",
            *[f"hisat2_index/genome.{i}.ht2" for i in range(1, 9)],
            *[f"hisat2_index/genome.{i}.ht2l" for i in range(1, 9)],
        ],
    )


def test_hisat2_align(run):
    run(
        "bio/hisat2/align",
        ["snakemake", "mapped/A.bam"],
    )


def test_homer_mergepeaks(run):
    run(
        "bio/homer/mergePeaks",
        ["snakemake", "merged/a_b.peaks"],
    )


def test_homer_getdifferentialpeaks(run):
    run(
        "bio/homer/getDifferentialPeaks",
        ["snakemake", "a_diffPeaks.txt"],
    )


def test_homer_findpeaks(run):
    run(
        "bio/homer/findPeaks",
        ["snakemake", "a_peaks.txt"],
    )


def test_homer_maketagdirectory(run):
    run(
        "bio/homer/makeTagDirectory",
        ["snakemake", "tagDir/a"],
    )


def test_homer_annotatepeaks(run):
    run(
        "bio/homer/annotatePeaks",
        [
            "snakemake",
            "a_annot.txt",
            "a.count.matrix.txt",
            "a.ratio.matrix.txt",
            "a.logPvalue.matrix.txt",
            "a.stats.txt",
            "a_motif.fasta",
            "a_motif.bed",
            "a_motif.logic",
        ],
    )


def test_immunedeconv(run):
    run(
        "bio/immunedeconv",
        ["snakemake", "deconv.csv"],
    )


def test_jellyfish_count(run):
    run(
        "bio/jellyfish/count",
        ["snakemake", "a.jf"],
        cores=2,
    )


def test_jellyfish_dump(run):
    run(
        "bio/jellyfish/dump",
        ["snakemake", "a.dump"],
        cores=2,
    )


def test_jellyfish_histo(run):
    run(
        "bio/jellyfish/histo",
        ["snakemake", "a.histo"],
        cores=2,
    )


def test_jellyfish_merge(run):
    run(
        "bio/jellyfish/merge",
        ["snakemake", "ab.jf"],
        cores=2,
    )


def test_kallisto_index(run):
    run(
        "bio/kallisto/index",
        ["snakemake", "transcriptome.idx"],
    )


def test_kallisto_quant(run):
    run(
        "bio/kallisto/quant",
        ["snakemake", "quant_results_A"],
    )


def test_macs2_callpeak(run):
    run(
        "bio/macs2/callpeak",
        [
            "snakemake",
            "callpeak/basename_peaks.xls",
            "callpeak/basename_peaks.narrowPeak",
            "callpeak/basename_summits.bed",
            "callpeak_options/basename_peaks.xls",
            "callpeak_options/basename_peaks.broadPeak",
            "callpeak_options/basename_peaks.gappedPeak",
            "callpeak_options/basename_treat_pileup.bdg",
            "callpeak_options/basename_control_lambda.bdg",
        ],
    )


def test_minimap2_aligner(run):
    run(
        "bio/minimap2/aligner",
        [
            "snakemake",
            "aligned/genome_aln.paf",
            "aligned/genome_aln.sam",
            "aligned/genome_aln.sorted.sam",
            "aligned/genome_aln.sorted.bam",
            "aligned/genome_aln.ubam.paf",
            "aligned/genome_aln.ubam.sam",
            "aligned/genome_aln.sorted.ubam.sam",
            "aligned/genome_aln.sorted.ubam.bam",
        ],
    )


def test_minimap2_index(run):
    run(
        "bio/minimap2/index",
        ["snakemake", "genome.mmi"],
    )


def test_mtnucratio(run):
    run(
        "bio/mtnucratio",
        ["snakemake", "ratio.txt"],
    )


def test_mosdepth(run):
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "mosdepth/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_bed/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_by_threshold/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_quantize_precision/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "mosdepth_cram/a.mosdepth.summary.txt",
        ],
        cores=4,
    )


def test_multiqc(run):
    run(
        "bio/multiqc",
        [
            "snakemake",
            "qc/multiqc.html",
            "qc/multiqc.a.html",
            "qc/multiqc.config.html",
        ],
    )


def test_muscle(run):
    run(
        "bio/muscle",
        [
            "snakemake",
            "test-proteins.super5.fas",
            "test-proteins.fas",
        ],
        cores=2,
    )


def test_nanosim(run):
    run(
        "bio/nanosim/simulator",
        [
            "snakemake",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_reads.fq",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_errors.txt",
            "results/nanosim/genome/brca2/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.simulated_reads.unaligned.fq",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated.fq",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated.errors.txt",
            "results/nanosim/transcriptome/brca2/human_NA12878_cDNA-rel2_guppy_v3.2.2.simulated_reads.unaligned.fq",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.abundances.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.dna_type_list.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/config/sample_x.reference_genomes_list.tsv",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/simulated/sample_x.simulated_errors.txt",
            "results/nanosim/metagenome/brca2/metagenome_ERR3152366_Log_v3.2.2/simulated/sample_x.simulated_reads.fa",
        ],
    )


def test_ngsbits_samplesimilarity(run):
    run(
        "bio/ngsbits/samplesimilarity",
        [
            "snakemake",
            "similarity.tsv",
        ],
    )


def test_ngsbits_sampleancestry(run):
    run(
        "bio/ngsbits/sampleancestry",
        [
            "snakemake",
            "ancestry.tsv",
        ],
    )


def test_ngsderive(run):
    run(
        "bio/ngsderive",
        [
            "snakemake",
            "A.readlen.tsv",
            "A.instrument.tsv",
            "A.strandedness.tsv",
            "A.encoding.tsv",
            "A.junctions.tsv",
            "junctions/A.rg.bam.junctions.tsv",
            "A.endedness.tsv",
        ],
    )


def test_ngs_disambiguate(run):
    run(
        "bio/ngs-disambiguate",
        [
            "snakemake",
            "disambiguate/s1.graft.ambiguous.bam",
        ],
    )


def test_optitype(run):
    run(
        "bio/optitype",
        ["snakemake", "optitype/a_result.tsv"],
    )


def test_pandora_index(run):
    run(
        "bio/pandora/index",
        ["snakemake", "rpsL/prg.fa.k15.w14.idx"],
    )


def test_pcaexplorer_pcaplot(run):
    run(
        "bio/pcaexplorer/pcaplot",
        ["snakemake", "pca.svg"],
    )


def test_picard_addorreplacegroups(run):
    run(
        "bio/picard/addorreplacereadgroups",
        ["snakemake", "fixed-rg/a.bam"],
    )


def test_picard_markduplicates(run):
    run(
        "bio/picard/markduplicates",
        [
            "snakemake",
            "dedup/a.bam",
            "dedup/a.sam",
            "dedup/a.cram",
            "dedup/a.cram.crai",
            "dedup/a.matecigar.bam",
            "dedup/a.matecigar.bai",
        ],
    )


def test_picard_collectalignmentsummarymetrics(run):
    run(
        "bio/picard/collectalignmentsummarymetrics",
        ["snakemake", "stats/a.summary.txt"],
    )


def test_picard_collectinsertsizemetrics(run):
    run(
        "bio/picard/collectinsertsizemetrics",
        ["snakemake", "stats/a.isize.txt"],
    )


def test_picard_bedtointervallist(run):
    run(
        "bio/picard/bedtointervallist",
        ["snakemake", "a.interval_list"],
    )


def test_picard_collecthsmetrics(run):
    run(
        "bio/picard/collecthsmetrics",
        ["snakemake", "stats/hs_metrics/a.txt"],
    )


def test_picard_collectmultiplemetrics(run):
    run(
        "bio/picard/collectmultiplemetrics",
        [
            "snakemake",
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
        ],
    )


def test_picard_mergesamfiles(run):
    run(
        "bio/picard/mergesamfiles",
        ["snakemake", "merged.bam"],
    )


def test_picard_collecttargetedpcrmetrics(run):
    run(
        "bio/picard/collecttargetedpcrmetrics/",
        ["snakemake", "stats/a.pcr.txt"],
    )


def test_picard_samtofastq(run):
    run(
        "bio/picard/samtofastq",
        [
            "snakemake",
            "reads/a.R1.fastq",
            "reads/a.R2.fastq",
        ],
    )


def test_picard_sortsam(run):
    run(
        "bio/picard/sortsam",
        ["snakemake", "sorted/a.bam"],
    )


def test_picard_revertsam(run):
    run(
        "bio/picard/revertsam",
        ["snakemake", "revert/a.bam"],
    )


def test_picard_createsequencedictionary(run):
    run(
        "bio/picard/createsequencedictionary",
        ["snakemake", "genome.dict"],
    )


def test_picard_mergevcfs(run):
    run(
        "bio/picard/mergevcfs",
        ["snakemake", "snvs.vcf"],
    )


def test_picard_collectrnaseqmetrics(run):
    run(
        "bio/picard/collectrnaseqmetrics",
        ["snakemake"],
    )


def test_picard_collectgcbiasmetrics(run):
    run(
        "bio/picard/collectgcbiasmetrics",
        ["snakemake"],
    )


def test_pindel_call(run):
    def check_log(log):
        assert "Looking at chromosome 1 bases 1000 to 10000" in log

    run(
        "bio/pindel/call",
        [
            "snakemake",
            "pindel/all_D",
            "pindel/all_included_D",
            "pindel/all_excluded_D",
        ],
        check_log=check_log,
    )


def test_pindel_pindel2vcf(run):
    run(
        "bio/pindel/pindel2vcf",
        [
            "snakemake",
            "pindel/all_D.vcf",
            "pindel/all.vcf",
        ],
    )


def test_preseq_lc_extrap(run):
    run(
        "bio/preseq/lc_extrap",
        [
            "snakemake",
            "test_bam/a.lc_extrap",
            "test_bed/a.lc_extrap",
        ],
    )


def test_prosolo_single_cell_bulk(run):
    run(
        "bio/prosolo/single-cell-bulk",
        [
            "snakemake",
            "variant_calling/single_cell.bulk.prosolo.bcf",
        ],
    )


def test_prosolo_control_fdr(run):
    run(
        "bio/prosolo/control-fdr",
        [
            "snakemake",
            "fdr_control/single_cell.bulk.prosolo.fdr.bcf",
        ],
    )


def test_razers3(run):
    run(
        "bio/razers3",
        ["snakemake", "mapped/a.bam"],
    )


def test_rebaler(run):
    run("bio/rebaler", ["snakemake", "sample1.asm.fa"])


def test_sambamba_flagstat(run):
    run(
        "bio/sambamba/flagstat",
        ["snakemake", "mapped/A.stats.txt"],
    )


def test_sambamba_sort(run):
    run(
        "bio/sambamba/sort",
        ["snakemake", "mapped/A.sorted.bam"],
    )


def test_sambamba_index(run):
    run(
        "bio/sambamba/index",
        ["snakemake", "mapped/A.sorted.bam.bai"],
    )


def test_sambamba_merge(run):
    run(
        "bio/sambamba/merge",
        ["snakemake", "mapped/A.merged.bam"],
    )


def test_sambamba_view(run):
    run(
        "bio/sambamba/view",
        ["snakemake", "mapped/A.filtered.bam"],
    )


def test_sambamba_slice(run):
    run(
        "bio/sambamba/slice",
        ["snakemake", "mapped/A.region.bam"],
    )


def test_sambamba_markdup(run):
    run(
        "bio/sambamba/markdup",
        ["snakemake", "mapped/A.rmdup.bam"],
    )


def test_pyfaidx(run):
    run(
        "bio/pyfaidx",
        [
            "snakemake",
            "retrieved.fasta",
            "retrieved.chrom",
            "retrieved.bed",
            "sequence.fasta.fai",
            "regions.fa",
            "list_regions.fa",
        ],
    )


def test_pyfastaq_replace_bases(run):
    run(
        "bio/pyfastaq/replace_bases",
        ["snakemake", "sample1.dna.fa"],
    )


def test_samtools_calmd(run):
    run(
        "bio/samtools/calmd",
        ["snakemake", "a.calmd.bam"],
    )


def test_samtools_collate(run):
    run(
        "bio/samtools/collate",
        ["snakemake", "a.collated.bam"],
    )


def test_samtools_fixmate(run):
    run(
        "bio/samtools/fixmate",
        ["snakemake", "fixed/a.bam"],
    )


def test_samtools_depth(run):
    run(
        "bio/samtools/depth",
        ["snakemake", "depth.txt"],
    )


def test_samtools_mpileup(run):
    run(
        "bio/samtools/mpileup",
        ["snakemake", "mpileup/a.mpileup.gz"],
    )


def test_samtools_mpileup(run):
    run(
        "bio/samtools/markdup",
        ["snakemake", "a.markdup.bam"],
    )


def test_samtools_stats(run):
    run(
        "bio/samtools/stats",
        ["snakemake", "samtools_stats/a.txt"],
    )


def test_samtools_sort(run):
    run(
        "bio/samtools/sort",
        ["snakemake", "mapped/a.sorted.bam"],
    )


def test_samtools_index(run):
    run(
        "bio/samtools/index",
        ["snakemake", "mapped/a.sorted.bam.bai"],
    )


def test_samtools_merge(run):
    run(
        "bio/samtools/merge",
        ["snakemake", "merged.bam"],
    )


def test_samtools_view(run):
    run("bio/samtools/view", ["snakemake", "a.bam"])


def test_samtools_fastx(run):
    run(
        "bio/samtools/fastx",
        ["snakemake", "a.fasta"],
    )


def test_samtools_flagstat(run):
    run(
        "bio/samtools/flagstat",
        ["snakemake", "mapped/a.bam.flagstat"],
    )


def test_samtools_idxstats(run):
    run(
        "bio/samtools/idxstats",
        [
            "snakemake",
            "mapped/a.sorted.bam.idxstats",
        ],
    )


def test_samtools_fastq_interleaved(run):
    run(
        "bio/samtools/fastq/interleaved",
        ["snakemake", "reads/a.fq"],
    )


def test_samtools_fastq_separate(run):
    run(
        "bio/samtools/fastq/separate",
        ["snakemake", "reads/a.1.fq"],
    )


def test_samtools_faidx(run):
    run(
        "bio/samtools/faidx",
        [
            "snakemake",
            "out/genome.fa.fai",
            "out/genome.named.fa.fai",
            "out/genome.fas.bgz.fai",
            "out/genome.fas.bgz.gzi",
            "out/genome.region_file.fas",
            "out/genome.region_array.fas",
            "out/genome.region_bgzip.fas",
        ],
    )


def test_bamtools_filter(run):
    run(
        "bio/bamtools/filter",
        ["snakemake", "filtered/a.bam"],
    )


def test_bamtools_filter_json(run):
    run(
        "bio/bamtools/filter_json",
        ["snakemake", "filtered/a.bam"],
    )


def test_bamtools_split(run):
    run(
        "bio/bamtools/split",
        ["snakemake", "mapped/a.REF_xx.bam"],
    )


def test_bamtools_stats(run):
    run(
        "bio/bamtools/stats",
        ["snakemake", "a.bamstats"],
    )


def test_snpmutator(run):
    run(
        "bio/snp-mutator",
        [
            "snakemake",
            "test_mutated_1.fasta",
            "test_mutated_2.fasta",
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
        [
            "snakemake",
            "star/se/a/se_aligned.bam",
            "star/pe/a/pe_aligned.sam",
        ],
    )


def test_star_index(run):
    run("bio/star/index", ["snakemake", "genome"])


def test_ngscheckmate_makesnvpattern(run):
    run(
        "bio/ngscheckmate/makesnvpattern",
        ["snakemake", "genome.pt"],
    )


def test_ngscheckmate_ncm(run):
    run(
        "bio/ngscheckmate/ncm",
        [
            "snakemake",
            "bam_matrix.txt",
            "vcf_matrix.txt",
            "fastq_matched.txt",
            "fastq_paired_matched.txt",
        ],
    )


def test_snpeff_annotate(run):
    run(
        "bio/snpeff/annotate",
        [
            "snakemake",
            "snpeff/fake_KJ660346.vcf",
            "snpeff_nostats/fake_KJ660346.vcf",
        ],
    )


def test_snpeff_download(run):
    run(
        "bio/snpeff/download",
        [
            "snakemake",
            "resources/snpeff/ebola_zaire",
        ],
    )


def test_strelka_germline(run):
    run(
        "bio/strelka/germline",
        ["snakemake", "strelka/a.vcf.gz"],
    )


def test_strelka_somatic(run):
    run(
        "bio/strelka/somatic",
        ["snakemake", "a_vcf", "-j 2"],
    )


def test_subread_featurecounts(run):
    run(
        "bio/subread/featurecounts",
        [
            "snakemake",
            "results/a.featureCounts",
            "results/a.featureCounts.summary",
            "results/a.featureCounts.jcounts",
        ],
    )


def test_trim_galore_pe(run):
    run(
        "bio/trim_galore/pe",
        [
            "snakemake",
            "trimmed/a_R1.fq.gz",
            "trimmed/a_R2.fastq",
        ],
    )


def test_trim_galore_se(run):
    run(
        "bio/trim_galore/se",
        [
            "snakemake",
            "trimmed/a_trimmed.fq.gz",
            "trimmed/a_trimmed.fastq",
        ],
    )


def test_trimmomatic(run):
    """Four tests, one per fq-gz combination"""
    run(
        "bio/trimmomatic",
        [
            "snakemake",
            "trimmed/se/fq_fq/a.1.fastq",
            "trimmed/se/gz_fq/a.1.fastq",
            "trimmed/se/fq_gz/a.1.fastq.gz",
            "trimmed/se/gz_gz/a.1.fastq.gz",
            "trimmed/pe/fq_fq/a.1.fastq",
            "trimmed/pe/gz_fq/a.1.fastq",
            "trimmed/pe/fq_gz/a.1.fastq.gz",
            "trimmed/pe/gz_gz/a.1.fastq.gz",
        ],
        cores=10,
    )


def test_rasusa(run):
    run(
        "bio/rasusa",
        ["snakemake", "a.subsampled.r1.fq"],
    )


def test_rubic(run):
    run(
        "bio/rubic",
        ["snakemake", "out/BRCA/gains.txt"],
    )


def test_delly(run):
    run(
        "bio/delly",
        [
            "snakemake",
            "sv/calls.bcf",
            "sv/calls.vcf.gz",
        ],
    )


def test_manta(run):
    run(
        "bio/manta",
        ["snakemake", "results/out.bcf"],
        cores=2,
    )


def test_jannovar(run):
    run(
        "bio/jannovar",
        [
            "snakemake",
            "jannovar/pedigree_vars.vcf.gz",
        ],
    )


def test_cairosvg(run):
    run("utils/cairosvg", ["snakemake", "pca.pdf"])


def test_trinity(run):
    run(
        "bio/trinity",
        [
            "snakemake",
            "trinity_out_dir.Trinity.fasta",
        ],
    )


def test_salmon_decoys(run):
    run(
        "bio/salmon/decoys",
        ["snakemake", "gentrome.fasta.gz"],
        cores=2,
    )


def test_salmon_index(run):
    run(
        "bio/salmon/index",
        [
            "snakemake",
            "salmon/transcriptome_index/complete_ref_lens.bin",
        ],
    )

    run(
        "bio/salmon/index",
        [
            "snakemake",
            "salmon/transcriptome_index/",
            "-s",
            "Snakefile_dir",
        ],
    )


def test_salmon_quant(run):
    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/a/quant.sf",
            "-s",
            "Snakefile",
        ],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/a/quant.sf",
            "-s",
            "Snakefile_index_list",
        ],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/a_se_x_transcriptome/quant.sf",
            "-s",
            "Snakefile_se",
        ],
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/a_se_x_transcriptome/quant.sf",
            "-s",
            "Snakefile_se_bz2",
        ],
        cores=2,
    )

    run(
        "bio/salmon/quant",
        [
            "snakemake",
            "salmon/ab_pe_x_transcriptome/quant.sf",
            "-s",
            "Snakefile_pe_multi",
        ],
    )


def test_gseapy_gsea(run):
    run(
        "bio/gseapy/gsea",
        [
            "snakemake",
            "KEGG_2016",
            "gsea.results.csv",
            "ssgsea.results.csv",
            "prerank_results_dir",
        ],
    )


def test_sexdeterrmine(run):
    run(
        "bio/sexdeterrmine",
        ["snakemake", "results.tsv"],
    )


def test_sourmash_compute(run):
    run(
        "bio/sourmash/compute/",
        [
            "snakemake",
            "transcriptome.sig",
            "reads.sig",
        ],
    )


def test_busco(run):
    run(
        "bio/busco",
        [
            "snakemake",
            "txome_busco/short_summary.json",
        ],
    )


def test_vcftools_filter(run):
    run(
        "bio/vcftools/filter",
        ["snakemake", "sample.filtered.vcf"],
    )


def test_gatk_callcopyrationsegments(run):
    run(
        "bio/gatk/callcopyratiosegments",
        ["snakemake", "a.called.seg"],
    )


def test_gatk_calculatecontamination(run):
    run(
        "bio/gatk/calculatecontamination",
        ["snakemake", "contamination.table"],
    )


def test_gatk_scatterintervalsbyns(run):
    run(
        "bio/gatk/scatterintervalsbyns",
        ["snakemake", "genome.intervals"],
    )


def test_gatk_splitintervals(run):
    run(
        "bio/gatk/splitintervals",
        ["snakemake", "out/genome.00.bed"],
    )


def test_gatk_printreadsspark(run):
    run(
        "bio/gatk/printreadsspark",
        ["snakemake", "a.bam"],
    )


def test_gatk_markduplicatesspark(run):
    run(
        "bio/gatk/markduplicatesspark",
        ["snakemake", "dedup/a.bam"],
    )


def test_gatk_intervallisttobed(run):
    run(
        "bio/gatk/intervallisttobed",
        ["snakemake", "genome.bed"],
    )


def test_gatk_estimatelibrarycomplexity(run):
    run(
        "bio/gatk/estimatelibrarycomplexity",
        ["snakemake", "a.metrics"],
    )


def test_gatk_baserecalibrator(run):
    run(
        "bio/gatk/baserecalibrator",
        ["snakemake", "recal/a.grp"],
    )


def test_gatk_baserecalibratorspark(run):
    run(
        "bio/gatk/baserecalibratorspark",
        ["snakemake", "recal/a.grp"],
    )


def test_gatk_collectreadcounts(run):
    run(
        "bio/gatk/collectreadcounts",
        ["snakemake", "a.counts.hdf5"],
    )


def test_gatk_collectalleliccounts(run):
    run(
        "bio/gatk/collectalleliccounts",
        ["snakemake", "a.counts.tsv"],
    )


def test_gatk_applybqsr(run):
    run(
        "bio/gatk/applybqsr",
        [
            "snakemake",
            "recal/a.bam",
            "recal/a.cram",
            "recal/a.embed.cram",
        ],
    )


def test_gatk_applybqsrspark(run):
    run(
        "bio/gatk/applybqsrspark",
        [
            "snakemake",
            "recal/a.bam",
            "recal/a.cram",
        ],
    )


def test_gatk_denoisereadcounts(run):
    run(
        "bio/gatk/denoisereadcounts",
        [
            "snakemake",
            "a.standardizedCR.tsv",
            "a.denoisedCR.tsv",
        ],
    )


def test_gatk_haplotypecaller(run):
    run(
        "bio/gatk/haplotypecaller",
        [
            "snakemake",
            "calls/a.vcf",
            "calls/a.g.vcf",
        ],
    )


def test_gatk_modelsegments(run):
    run(
        "bio/gatk/modelsegments",
        ["snakemake", "a.den.modelFinal.seg"],
    )


def test_gatk_variantrecalibrator(run):
    def check_log(log):
        assert "USAGE" not in log

    run(
        "bio/gatk/variantrecalibrator",
        [
            "snakemake",
            "calls/all.recal.vcf",
        ],
        check_log=check_log,
    )


def test_gatk_variantstotable(run):
    run(
        "bio/gatk/variantstotable",
        ["snakemake", "calls/snvs.tab"],
    )


def test_gatk_filtermutectcalls(run):
    run(
        "bio/gatk/filtermutectcalls",
        [
            "snakemake",
            "calls/snvs.mutect.filtered.vcf",
            "calls/snvs.mutect.filtered.b.vcf",
        ],
    )


def test_gatk_selectvariants(run):
    run(
        "bio/gatk/selectvariants",
        ["snakemake", "calls/snvs.vcf"],
    )


def test_gatk_variantannotator(run):
    run(
        "bio/gatk/variantannotator",
        ["snakemake", "snvs.annot.vcf"],
    )


def test_gatk_variantfiltration(run):
    run(
        "bio/gatk/variantfiltration",
        ["snakemake", "calls/snvs.filtered.vcf"],
    )


def test_gatk_varianteval(run):
    run(
        "bio/gatk/varianteval",
        ["snakemake", "snvs.varianteval.grp"],
    )


def test_gatk_genotypegvcfs(run):
    run(
        "bio/gatk/genotypegvcfs",
        ["snakemake", "calls/all.vcf"],
    )


def test_gatk_genomicsdbimport(run):
    run(
        "bio/gatk/genomicsdbimport",
        ["snakemake", "db"],
    )


def test_gatk_combinegvcfs(run):
    run(
        "bio/gatk/combinegvcfs",
        ["snakemake", "calls/all.g.vcf"],
    )


def test_gatk_splitncigarreads(run):
    run(
        "bio/gatk/splitncigarreads",
        ["snakemake", "split/a.bam"],
    )


def test_gatk_cleansam(run):
    run(
        "bio/gatk/cleansam",
        ["snakemake", "a.clean.bam"],
    )

    run(
        "bio/gatk/mutect",
        [
            "snakemake",
            "variant/a.vcf",
            "variant_complete/a.vcf",
            "variant_list/a_b.vcf",
            "variant_bam/a.vcf",
            "variant_bam/a.bam",
        ],
    )


def test_gatk_learnreadorientationmodel(run):
    run(
        "bio/gatk/learnreadorientationmodel",
        ["snakemake"],
    )


def test_gatk_leftalignandtrimvariants(run):
    run(
        "bio/gatk/leftalignandtrimvariants",
        [
            "snakemake",
            "calls/split_multiallelics.vcf",
        ],
    )


def test_gatk_getpileupsummaries(run):
    run(
        "bio/gatk/getpileupsummaries",
        ["snakemake", "summaries.table"],
    )


def test_gatk_depthofcoverage(run):
    run(
        "bio/gatk/depthofcoverage",
        [
            "snakemake",
            "depth/a",
            "depth/a.sample_cumulative_coverage_counts",
            "depth/a.sample_cumulative_coverage_proportions",
            "depth/a.sample_interval_statistics",
            "depth/a.sample_interval_summary",
            "depth/a.sample_statistics",
            "depth/a.sample_summary",
        ],
    )


def test_gatk_applyvqsr(run):
    run(
        "bio/gatk/applyvqsr",
        ["snakemake", "test.snp_recal.vcf"],
    )


def test_gatk3_realignertargetcreator(run):
    run(
        "bio/gatk3/realignertargetcreator",
        ["snakemake", "a.intervals"],
    )


def test_gatk3_indelrealigner(run):
    run(
        "bio/gatk3/indelrealigner",
        ["snakemake", "a.realigned.bam"],
    )


def test_gatk3_baserecalibrator(run):
    run(
        "bio/gatk3/baserecalibrator",
        ["snakemake", "a.recal_data_table"],
    )


def test_gatk3_printreads(run):
    run(
        "bio/gatk3/printreads",
        ["snakemake", "a.bqsr.bam"],
    )


def test_igv_reports(run):
    run(
        "bio/igv-reports",
        ["snakemake", "igv-report.html"],
    )


def test_vardict(run):
    run(
        "bio/vardict",
        [
            "snakemake",
            "vcf/a.s.vcf",
            "vcf/a.tn.vcf",
        ],
    )


def test_varscan_mpileup2indel(run):
    run(
        "bio/varscan/mpileup2indel",
        ["snakemake", "vcf/a.vcf"],
    )


def test_varscan_mpileup2snp(run):
    run(
        "bio/varscan/mpileup2snp",
        ["snakemake", "vcf/a.vcf"],
    )


def test_varscan_somatic(run):
    run(
        "bio/varscan/somatic",
        [
            "snakemake",
            "single_mpileup/vcf/a.snp.vcf",
            "dual_mpileup/vcf/a.snp.vcf",
        ],
    )


def test_umis_bamtag(run):
    run(
        "bio/umis/bamtag",
        ["snakemake", "data/a.annotated.bam"],
    )


def test_transdecoder_longorfs(run):
    run(
        "bio/transdecoder/longorfs",
        [
            "snakemake",
            "test.fa.transdecoder_dir/longest_orfs.pep",
        ],
    )


def test_transdecoder_predict(run):
    run(
        "bio/transdecoder/predict",
        ["snakemake", "test.fa.transdecoder.gff3"],
    )


def test_last_lastdb(run):
    run(
        "bio/last/lastdb",
        [
            "snakemake",
            "test-transcript.fa.prj",
            "test-protein.fa.prj",
        ],
    )


def test_last_lastal(run):
    run(
        "bio/last/lastal",
        [
            "snakemake",
            "test-transcript.maf",
            "test-tr-x-prot.maf",
        ],
    )


def test_pear(run):
    run(
        "bio/pear",
        [
            "snakemake",
            "pear/reads_pear_assembled.fq.gz",
        ],
    )


def test_plass(run):
    run(
        "bio/plass",
        [
            "snakemake",
            "plass/prot.fasta",
            "plass/prot_single.fasta",
        ],
    )


def test_refgenie(run):
    try:
        shutil.copytree("bio/refgenie/test/genome_folder", "/tmp/genome_folder")
    except FileExistsError:
        # no worries, the directory is already there
        pass
    os.environ["REFGENIE"] = "/tmp/genome_folder/genome_config.yaml"
    run("bio/refgenie", ["snakemake"])


def test_hmmer_hmmbuild(run):
    run(
        "bio/hmmer/hmmbuild",
        ["snakemake", "test-profile.hmm"],
    )


def test_hmmer_hmmpress(run):
    run(
        "bio/hmmer/hmmpress",
        ["snakemake", "test-profile.hmm.h3f"],
    )


def test_hmmer_hmmscan(run):
    run(
        "bio/hmmer/hmmscan",
        ["snakemake", "test-prot-tbl.txt"],
    )


def test_hmmer_hmmsearch(run):
    run(
        "bio/hmmer/hmmsearch",
        ["snakemake", "test-prot-tbl.txt"],
    )


def test_hmmer_jackhmmer(run):
    run(
        "bio/hmmer/jackhmmer",
        ["snakemake", "test-prot-tbl.txt"],
    )


def test_paladin_index(run):
    run(
        "bio/paladin/index",
        ["snakemake", "index/prot.fasta.bwt"],
    )


def test_paladin_prepare(run):
    run(
        "bio/paladin/prepare",
        ["snakemake", "uniprot_sprot.fasta.gz"],
    )


def test_paladin_align(run):
    run(
        "bio/paladin/align",
        ["snakemake", "paladin_mapped/a.bam"],
    )


def test_ucsc_bedgraphtobigwig(run):
    run(
        "bio/ucsc/bedGraphToBigWig",
        ["snakemake", "a.bw"],
    )


def test_ucsc_genepredtobed(run):
    run(
        "bio/ucsc/genePredToBed",
        ["snakemake", "annotation.bed"],
    )


def test_ucsc_fatotwobit(run):
    run(
        "bio/ucsc/faToTwoBit",
        [
            "snakemake",
            "genome.2bit",
            "genome_gz.2bit",
        ],
    )


def test_ucsc_twobitinfo(run):
    run(
        "bio/ucsc/twoBitInfo",
        ["snakemake", "genome.chrom.sizes"],
    )


def test_ucsc_twobittofa(run):
    run(
        "bio/ucsc/twoBitToFa",
        ["snakemake", "genome.fa"],
    )


def test_ucsc_gtftogenepred(run):
    run(
        "bio/ucsc/gtfToGenePred",
        [
            "snakemake",
            "annotation.genePred",
            "annotation.PicardCollectRnaSeqMetrics.genePred",
        ],
    )


def test_entrez_efetch(run):
    run(
        "bio/entrez/efetch",
        ["snakemake"],
    )


def test_ensembl_sequence(run):
    run(
        "bio/reference/ensembl-sequence",
        [
            "snakemake",
            "refs/genome.fasta",
            "refs/genome.fa.gz",
            "refs/chr2.fasta",
            "refs/chr6_and_chr1.fasta",
            "refs/chr6_and_chr1.fa.gz",
        ],
        compare_results_with_expected={
            "refs/chr6_and_chr1.fasta": "expected/chr6_and_chr1.fasta",
            "refs/chr6_and_chr1.fa.gz": "expected/chr6_and_chr1.fa.gz",
        },
    )

    run(
        "bio/reference/ensembl-sequence",
        [
            "snakemake",
            "-s",
            "old_release.smk",
            "refs/genome.fasta",
            "refs/old_release.chr1.fasta",
        ],
    )


def test_ensembl_annotation(run):
    run(
        "bio/reference/ensembl-annotation",
        [
            "snakemake",
            "refs/annotation.gtf",
            "refs/annotation.gtf.gz",
            "resources/regulatory_features.gff",
            "resources/regulatory_features.gff3.gz",
        ],
    )


def test_ensembl_regulation(run):
    run(
        "bio/reference/ensembl-regulation",
        [
            "snakemake",
            "resources/regulatory_features.mouse.gff.gz",
        ],
    )


def test_ensembl_biomart_table(run):
    run(
        "bio/reference/ensembl-biomart-table",
        [
            "snakemake",
            "resources/ensembl_transcripts_to_genes_mapping.tsv.gz",
            "resources/ensembl_transcripts_to_genes_mapping.parquet.gz",
        ],
    )


def test_ensembl_mysql_table(run):
    run(
        "bio/reference/ensembl-mysql-table",
        [
            "snakemake",
            "resources/ensembl_repeat_annotations.tsv.gz",
            "resources/ensembl_regulatory_annotations.parquet.gz",
        ],
    )


def test_ensembl_variation(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake"],
    )

    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "old_release.smk"],
    )

    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "chrom_wise.smk"],
    )

    run(
        "bio/reference/ensembl-variation",
        [
            "snakemake",
            "--snakefile",
            "with_fai.smk",
        ],
    )


@pytest.mark.skip(reason="needs too much time")
def test_ensembl_variation_grch37(run):
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "grch37.smk"],
    )


def test_ega_fetch(run):
    run(
        "bio/ega/fetch",
        ["snakemake", "data/EGAF00007243774.cram"],
    )


def test_infernal_cmpress(run):
    run(
        "bio/infernal/cmpress",
        [
            "snakemake",
            "test-covariance-model.cm.i1f",
        ],
    )


def test_infernal_cmscan(run):
    run(
        "bio/infernal/cmscan",
        ["snakemake", "tr-infernal-tblout.txt"],
    )


def test_methyldackel_extract(run):
    run(
        "bio/methyldackel/extract",
        [
            "snakemake",
            "cpg.meth.bg",
            "cpg.count.bg",
            "cpg.logit.bg",
            "report.tsv",
        ],
    )


def test_bismark_genome_preparation(run):
    run(
        "bio/bismark/bismark_genome_preparation",
        [
            "snakemake",
            "resources/genome/bismark",
            "resources/genome_gz/bismark",
        ],
        cores=2,
        compare_results_with_expected={
            "resources/genome/bismark/Bisulfite_Genome/GA_conversion/genome_mfa.GA_conversion.fa": "expected/genome/bismark/Bisulfite_Genome/genome_mfa.GA_conversion.fa",
            "resources/genome_gz/bismark/Bisulfite_Genome/CT_conversion/genome_mfa.CT_conversion.fa": "expected/genome_gz/bismark/Bisulfite_Genome/genome_mfa.CT_conversion.fa",
        },
    )


def test_bismark_bam2nuc(run):
    run(
        "bio/bismark/bam2nuc",
        [
            "snakemake",
            "indexes/genome/genomic_nucleotide_frequencies.txt",
            "bams/b_genome.nucleotide_stats.txt",
        ],
    )


def test_bismark(run):
    run(
        "bio/bismark/bismark",
        [
            "snakemake",
            "results/bismark/a_genome_pe.bam",
            "results/bismark/b_genome.cram",
        ],
        compare_results_with_expected={
            "results/bismark/b_genome.nucleotide_stats.txt": "expected/b_genome.nucleotide_stats.txt",
        },
    )


def test_bismark_deduplicate(run):
    run(
        "bio/bismark/deduplicate_bismark",
        [
            "snakemake",
            "bams/a_pe.deduplicated.bam",
            "bams/b.deduplicated.bam",
        ],
    )


def test_bismark_methylation_extractor(run):
    run(
        "bio/bismark/bismark_methylation_extractor",
        [
            "snakemake",
            "meth_cpg/a_genome_pe.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.deduplicated.bismark.cov.gz",
            "meth_cpg/b_genome.bismark.cov.gz",
        ],
    )


def test_bismark_bismark2report(run):
    run(
        "bio/bismark/bismark2report",
        [
            "snakemake",
            "qc/meth/a_genome.bismark2report.html",
            "qc/meth/b_genome.bismark2report.html",
        ],
    )


def test_bismark_bismark2summary(run):
    run(
        "bio/bismark/bismark2summary",
        [
            "snakemake",
            "qc/experiment.bismark2summary.html",
        ],
    )


def test_bismark_bismark2bedgraph(run):
    run(
        "bio/bismark/bismark2bedGraph",
        [
            "snakemake",
            "meth_cpg/a_genome_pe.deduplicated_CpG.bismark.cov.gz",
            "meth_non_cpg/a_genome_pe.deduplicated_non_cpg.bismark.cov.gz",
        ],
    )


def test_tabix_index(run):
    run(
        "bio/tabix/index",
        ["snakemake", "test.vcf.gz.tbi"],
    )


def test_tabix_query(run):
    run(
        "bio/tabix/query",
        ["snakemake", "A.output.bed"],
    )


def test_msisensor_msi(run):
    run(
        "bio/msisensor/msi",
        ["snakemake", "example.msi"],
    )


def test_msisensor_scan(run):
    run(
        "bio/msisensor/scan",
        ["snakemake", "microsat.list"],
    )


def test_tximport(run):
    run("bio/tximport", ["snakemake", "txi.RDS"])


def test_sra_tools_fasterq_dump(run):
    run(
        "bio/sra-tools/fasterq-dump",
        [
            "snakemake",
            "data/se/SRR14133989.fastq",
            "data/se/SRR14133989.fastq.gz",
            "data/se/SRR14133989.fastq.bz2",
            "data/pe/SRR14133829_1.fastq",
            "data/pe/SRR14133829_1.fastq.gz",
            "data/pe/SRR14133829_1.fastq.bz2",
        ],
    )


def test_snpsift_genesets(run):
    run(
        "bio/snpsift/genesets",
        ["snakemake", "annotated/out.vcf"],
    )


def test_snpsift_vartype(run):
    run(
        "bio/snpsift/varType",
        ["snakemake", "annotated/out.vcf"],
    )


def test_snpsift_gwascat(run):
    run(
        "bio/snpsift/gwascat",
        ["snakemake", "annotated/out.vcf"],
    )


def test_snpsift_dbnsfp(run):
    run(
        "bio/snpsift/dbnsfp",
        ["snakemake", "out.vcf"],
    )


def test_snpsift_annotate(run):
    run(
        "bio/snpsift/annotate",
        ["snakemake", "annotated/out.vcf"],
    )


def test_ptrimmer(run):
    run(
        "bio/ptrimmer",
        [
            "snakemake",
            "ptrimmer_se",
            "ptrimmer_pe",
        ],
    )


def test_vep_cache(run):
    run(
        "bio/vep/cache",
        [
            "snakemake",
            "resources/vep/cache",
            "resources/vep/indexed_cache",
            "resources/vep/cache_ebi",
        ],
    )


def test_vep_plugins(run):
    run(
        "bio/vep/plugins",
        ["snakemake", "resources/vep/plugins"],
    )


def test_vep_annotate(run):
    run(
        "bio/vep/annotate",
        [
            "snakemake",
            "variants.annotated.bcf",
            "--verbose",
        ],
    )


def test_genefuse(run):
    run(
        "bio/genefuse",
        [
            "snakemake",
            "a_fusions.txt",
            "a_genefuse_report.html",
        ],
    )


def test_genomepy(run):
    # download dm3 genome (relatively small, +/- 250 mb)
    run(
        "bio/genomepy",
        ["snakemake", "dm3/dm3.fa"],
    )


def test_chm_eval_sample(run):
    run(
        "bio/benchmark/chm-eval-sample",
        ["snakemake"],
    )


def test_chm_eval_kit(run):
    run("bio/benchmark/chm-eval-kit", ["snakemake"])


def test_chm_eval_eval(run):
    run(
        "bio/benchmark/chm-eval",
        ["snakemake", "chm-eval/calls.summary"],
    )


def test_unicycler(run):
    run(
        "bio/unicycler",
        [
            "snakemake",
            "result/reads/assembly.fasta",
        ],
    )


def test_vg_autoindex(run):
    run(
        "bio/vg/autoindex",
        [
            "snakemake",
            "resources/genome.dist",
            "resources/genome.xg",
        ],
    )


def test_vg_construct(run):
    run(
        "bio/vg/construct",
        ["snakemake", "graph/c.vg"],
    )


def test_vg_giraffe(run):
    run(
        "bio/vg/giraffe",
        ["snakemake", "mapped/a.bam"],
    )


def test_vg_merge(run):
    run(
        "bio/vg/merge",
        ["snakemake", "graph/wg.vg"],
    )


def test_vg_ids(run):
    run(
        "bio/vg/ids",
        ["snakemake", "graph/c_mod.vg"],
    )


def test_vg_index_gcsa(run):
    run(
        "bio/vg/index/gcsa",
        ["snakemake", "index/wg.gcsa"],
    )


def test_vg_index_xg(run):
    run(
        "bio/vg/index/xg",
        ["snakemake", "index/x.xg"],
    )


def test_vg_kmers(run):
    run(
        "bio/vg/kmers",
        ["snakemake", "kmers/c.kmers"],
    )


def test_vg_prune(run):
    run(
        "bio/vg/prune",
        ["snakemake", "graph/c.pruned.vg"],
    )


def test_vg_sim(run):
    run("bio/vg/sim", ["snakemake", "reads/x.seq"])


def test_wgsim(run):
    run(
        "bio/wgsim",
        ["snakemake", "reads/1.fq", "reads/2.fq"],
    )


def test_diamond_makedb(run):
    run(
        "bio/diamond/makedb",
        ["snakemake", "foo.dmnd"],
    )


def test_diamond_blastx(run):
    run(
        "bio/diamond/blastx",
        ["snakemake", "foo.tsv.gz"],
    )


def test_diamond_blastp(run):
    run(
        "bio/diamond/blastp",
        ["snakemake", "test-protein.tsv.gz"],
    )


def test_nextflow(run):
    run(
        "utils/nextflow",
        ["snakemake", "--show-failed-logs"],
    )


def test_qualimap_rnaseq(run):
    run(
        "bio/qualimap/rnaseq",
        ["snakemake"],
    )


def test_qualimap_bamqc(run):
    run(
        "bio/qualimap/bamqc",
        ["snakemake", "qc/a"],
    )


def test_rsem_calculate_expression(run):
    run(
        "bio/rsem/calculate-expression",
        ["snakemake"],
    )

    run(
        "bio/rsem/calculate-expression",
        ["snakemake", "-s", "Snakefile_fastq"],
    )


def test_rsem_prepare_reference(run):
    run(
        "bio/rsem/prepare-reference",
        ["snakemake"],
    )


def test_rsem_generate_data_matrix(run):
    run(
        "bio/rsem/generate-data-matrix",
        ["snakemake"],
    )


def test_rseqc_inner_distance(run):
    run(
        "bio/rseqc/inner_distance",
        ["snakemake", "a.pdf"],
    )


def test_rseqc_infer_experiment(run):
    run(
        "bio/rseqc/infer_experiment",
        ["snakemake", "a.experiment.txt"],
    )


def test_rseqc_bam_stat(run):
    run(
        "bio/rseqc/bam_stat",
        ["snakemake", "a.stats"],
    )


def test_rseqc_read_gc(run):
    run(
        "bio/rseqc/read_gc",
        ["snakemake"],
    )


def test_rseqc_read_duplication(run):
    run(
        "bio/rseqc/read_duplication",
        ["snakemake"],
    )


def test_rseqc_read_distribution(run):
    run(
        "bio/rseqc/read_distribution",
        ["snakemake"],
    )


def test_spades_metaspades(run):
    run(
        "bio/spades/metaspades",
        [
            "snakemake",
            "run_metaspades",
            "--resources",
            "mem_mem=1000",
            "time=15",
            "--show-failed-logs",
        ],
        cores=2,
    )


def test_megahit(run):
    run(
        "bio/megahit",
        [
            "snakemake",
        ],
        cores=2,
    )


def test_verifybamid2(run):
    run(
        "bio/verifybamid/verifybamid2",
        ["snakemake"],
    )


def test_rbt_csvreport(run):
    run(
        "bio/rbt/csvreport",
        ["snakemake", "qc_data"],
    )


def test_rbt_collapse_reads_to_fragments(run):
    run(
        "bio/rbt/collapse_reads_to_fragments-bam",
        ["snakemake"],
    )


def test_meta_gatk_mutect2_calling(run):
    run(
        "meta/bio/gatk_mutect2_calling",
        [
            "snakemake",
            "results/variant/Sample1.filtered.vcf.gz.tbi",
        ],
        cores=2,
    )


def test_meta_calc_consensus_reads(run):
    run(
        "meta/bio/calc_consensus_reads/",
        [
            "snakemake",
            "results/consensus/sampleA.bam",
        ],
    )


def test_meta_bowtie2_sambamba(run):
    run(
        "meta/bio/bowtie2_sambamba",
        [
            "snakemake",
            "results/mapped/Sample1.rmdup.bam.bai",
        ],
        cores=2,
    )


def test_bazam(run):
    run(
        "bio/bazam",
        [
            "snakemake",
            "results/reads/a.fastq.gz",
            "results/reads/a.r1.fastq.gz",
        ],
    )


def test_ragtag_correction(run):
    run(
        "bio/ragtag/correction",
        [
            "snakemake",
            "query_corrected_reference/ragtag.correct.fasta",
        ],
    )


def test_ragtag_patch(run):
    run(
        "bio/ragtag/patch",
        [
            "snakemake",
            "query_reference.fasta",
        ],
    )


def test_ragtag_scaffold(run):
    run(
        "bio/ragtag/scaffold",
        [
            "snakemake",
            "query_scaffold_reference/ragtag.scaffold.fasta",
        ],
    )


def test_ragtag_merge(run):
    run(
        "bio/ragtag/merge",
        [
            "snakemake",
            "asm_merged.fasta",
        ],
    )


def test_barrnap(run):
    run(
        "bio/barrnap",
        [
            "snakemake",
            "mitochondria.gff",
        ],
    )


def test_encode_fastq_downloader(run):
    run(
        "bio/encode_fastq_downloader",
        ["snakemake", "ENCFF140TJA.fastq.gz"],
    )


def test_whatshap_haplotag(run):
    run(
        "bio/whatshap/haplotag",
        [
            "snakemake",
            "alignment.phased.bam",
        ],
    )


def test_sortmerna(run):
    run(
        "bio/sortmerna",
        [
            "snakemake",
            "aligned_1.fastq.gz",
            "unpaired.fastq",
        ],
    )


def test_tmb_pyeffgenomesize(run):
    run(
        "bio/tmb/pyeffgenomesize",
        [
            "snakemake",
            "minimal.txt",
            "complete.txt",
        ],
    )


def test_tmb_pytmb(run):
    run(
        "bio/tmb/pytmb",
        ["snakemake"],
    )


def test_root_hadd(run):
    run(
        "phys/root/hadd",
        ["snakemake"],
        cores=2,
    )


def test_root_define_columns(run):
    run(
        "phys/root/define_columns",
        ["snakemake"],
        cores=2,
    )


def test_root_filter(run):
    run(
        "phys/root/filter",
        [
            "snakemake",
            "ntuple0_str_output.root",
            "ntuple0_list_output.root",
            "ntuple0_dict_output.root",
        ],
        cores=2,
    )


def test_root_rootcp(run):
    run(
        "phys/root/rootcp",
        ["snakemake"],
        cores=2,
    )


def test_emu_abundance(run):
    run(
        "bio/emu/abundance",
        [
            "snakemake",
            "sample_rel-abundance.tsv",
            "sample_emu_alignments.sam",
            "sample_unclassified.fas",
            "sample_unmapped.fas",
            "short_read_rel-abundance_paired.tsv",
            "short_read_emu_alignments_paired.sam",
            "short_read_unclassified_paired.fq",
            "short_read_unmapped_paired.fq",
        ],
    )


def test_emu_collapse_taxonomy(run):
    run(
        "bio/emu/collapse-taxonomy",
        [
            "snakemake",
            "full_length_rel-abundance_collapsed.tsv",
        ],
    )


def test_emu_combine_output(run):
    run(
        "bio/emu/combine-outputs",
        [
            "snakemake",
            "combined_abundances.tsv",
            "counts.tsv",
            "taxonomy.tsv",
        ],
    )


def test_toulligqc(run):
    run(
        "bio/toulligqc",
        [
            "snakemake",
            "toulligqc_sequencing_summary/report.html",
            "toulligqc_bam/report.html",
            "toulligqc_fastq/report.html",
        ],
    )


def test_varlociraptor_estimate_alignment_properties(run):
    run(
        "bio/varlociraptor/estimate-alignment-properties",
        [
            "snakemake",
            "results/alignment-properties/NA12878.json",
            "--sdm",
            "conda",
        ],
    )


def test_varlociraptor_preprocess_variants(run):
    run(
        "bio/varlociraptor/preprocess-variants",
        [
            "snakemake",
            "results/observations/NA12878.bcf",
            "--sdm",
            "conda",
        ],
    )


def test_varlociraptor_call_variants(run):
    run(
        "bio/varlociraptor/call-variants",
        [
            "snakemake",
            "results/variant-calls/dummy-group.bcf",
            "--sdm",
            "conda",
        ],
    )


def test_varlociraptor_control_fdr(run):
    run(
        "bio/varlociraptor/control-fdr",
        [
            "snakemake",
            "results/variant-calls/dummy-group.fdr-controlled.bcf",
            "--sdm",
            "conda",
        ],
    )


def test_overturemaps_download(run):
    run(
        "geo/overturemaps/download",
        [
            "snakemake",
            "results/division_boundary.parquet",
        ],
        cores=2,
    )


def test_pygadm_item(run):
    run(
        "geo/pygadm/item",
        ["snakemake", "results/mexico.parquet"],
        cores=2,
    )


def test_trf(run):
    run(
        "bio/trf",
        [
            "snakemake",
            "trf_output/small_test",
            "--allowed-rules",
            "run_trf_basic",
        ],
    )

    with pytest.raises(subprocess.CalledProcessError):
        run(
            "bio/trf",
            [
                "snakemake",
                "trf_output/small_test",
                "--allowed-rules",
                "run_trf_with_missing_param_value",
            ],
        )

    run(
        "bio/trf",
        [
            "snakemake",
            "trf_output/small_test",
            "--allowed-rules",
            "run_trf_permissible_flags",
        ],
    )

    run(
        "bio/trf",
        [
            "snakemake",
            "trf_output/small_test",
            "--allowed-rules",
            "run_trf_basic_uppercase",
        ],
    )


def test_mehari_download_transcript_db(run):
    run(
        "bio/mehari/download-transcript-db",
        [
            "snakemake",
            "resources/mehari/dbs/transcripts.bin.zst",
        ],
    )


def test_mehari_download_clinvar_db(run):
    run(
        "bio/mehari/download-clinvar-db",
        [
            "snakemake",
            "resources/mehari/dbs/clinvar/sv",
        ],
    )


def test_mehari_annotate_seqvars(run):
    run(
        "bio/mehari/annotate-seqvars",
        [
            "snakemake",
            "resources/MT-ND2.annotated.bcf",
            "--verbose",
        ],
    )


def test_rasterio_clip(run):
    run(
        "geo/rasterio/clip",
        [
            "snakemake",
            "results/montenegro.tiff",
            "results/switzerland.tiff",
            "results/puerto_vallarta_small.tiff",
        ],
        cores=2,
    )


def test_orthanq(run):
    run(
        "bio/orthanq",
        [
            "snakemake",
            "out/candidates",
            "out/candidates.vcf",
            # "out/preprocess_hla.bcf",
            "out/preprocess_virus.bcf",
            "out/calls_hla",
            "out/calls_virus",
        ],
    )


def test_mofa2_training(run):
    run(
        "bio/mofa2/training",
        ["snakemake", "data.hdf5"],
    )


def test_mofa2_plotting(run):
    run("bio/mofa2/plotting", ["snakemake"])


def test_go_yq(run):
    run(
        "utils/go-yq",
        [
            "snakemake",
            "concat.yaml",
            "updated.yaml",
            "evaluated.yaml",
            "foo_bar.yml",
            "table.json",
        ],
    )


def test_pytrf(run):
    run(
        "bio/pytrf",
        [
            "snakemake",
            "--cores",
            "1",
            "results/small_test_findstr.csv",
            "results/small_test_findstr_defaults.tsv",
            "results/small_test_findgtr.tsv",
            "results/small_test_findatr.tsv",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "results/small_test_findstr.csv": "expected/findstr_basic.csv",
            "results/small_test_findgtr.tsv": "expected/findgtr_basic.tsv",
            "results/small_test_findatr.tsv": "expected/findatr_basic.tsv",
        },
    )


@pytest.mark.skip(
    reason="PyTRF extract command has a delimiter bug (see https://github.com/lmdu/pytrf/issues/6)"
)
def test_pytrf_extract(run):
    run(
        "bio/pytrf",
        [
            "snakemake",
            "--cores",
            "1",
            "results/small_test_extract.tsv",
            "--use-conda",
            "-F",
        ],
        compare_results_with_expected={
            "results/small_test_extract.tsv": "expected/extract_basic.tsv",
        },
    )


def test_jasminesv(run):
    run("bio/jasminesv", ["snakemake"])


def test_genometools(run):
    run(
        "bio/genometools/gff3",
        ["snakemake", "example.revised.gff3"],
    )

    run(
        "bio/genometools/gff3validator",
        ["snakemake", "example.validated.flag"],
    )


def test_pbmarkdup(run):
    run(
        "bio/pbmarkdup",
        ["snakemake",
        "pbmarkdup1.fastq.gz",
        "pbmarkdup2.fastq.gz",
        "pbmarkdup3.fastq.gz",
        "dedup.fastq.gz",
        ],
    )
