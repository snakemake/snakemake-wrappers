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

        if any(
            yaml.load(open(os.path.join(w, "meta.yaml")), Loader=yaml.BaseLoader).get(
                "blacklisted"
            )
            for w in used_wrappers
        ):
            raise Skipped("wrapper blacklisted")

        testdir = os.path.join(d, "test")
        # pkgdir = os.path.join(d, "pkgs")
        shutil.copytree(os.path.join(wrapper, "test"), testdir)
        # prepare conda package dir
        # os.makedirs(pkgdir)
        # switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + [
            "--wrapper-prefix",
            "file://{}/".format(d),
            "--conda-cleanup-pkgs",
            "--printshellcmds",
            "--show-failed-logs",
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
def test_nonpareil():
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


@skip_if_not_modified
def test_nonpareil_plot():
    run(
        "bio/nonpareil/plot",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "results/a.pdf",
# Test disabled due to bug in nonpareil (#62)
#            "results/a.nomodel.pdf",
        ]
    )


@skip_if_not_modified
def test_indelqual():
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


@skip_if_not_modified
def test_vsearch():
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


@skip_if_not_modified
def test_loglog():
    run(
        "bio/bbtools/loglog",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "logs/se/a.log",
            "logs/pe/a.log",
        ],
    )


@skip_if_not_modified
def test_tadpole():
    run(
        "bio/bbtools/tadpole",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
            "out/correct_se/a.fastq.gz",
            "out/correct_se/a.discarded.fastq.gz",
            "out/correct_pe/a.1.fastq",
            "out/correct_pe/a.2.fastq",
            "out/correct_pe/a.discarded.fastq",
            "out/extend_se/a.fastq.gz",
            "out/extend_se/a.discarded.fastq.gz",
            "out/extend_pe/a.1.fastq",
            "out/extend_pe/a.2.fastq",
            "out/extend_pe/a.discarded.fastq",
        ],
    )


@skip_if_not_modified
def test_seqkit_stats():
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


@skip_if_not_modified
def test_seqkit_rmdup():
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


@skip_if_not_modified
def test_gffread():
    run(
        "bio/gffread",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "transcripts.fa"],
    )


@skip_if_not_modified
def test_seqkit_fx2tab():
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


@skip_if_not_modified
def test_seqkit_grep():
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


@skip_if_not_modified
def test_seqkit_subseq():
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


@skip_if_not_modified
def test_seqkit_seq():
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


@skip_if_not_modified
def test_sickle_pe():
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


@skip_if_not_modified
def test_sickle_se():
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


@skip_if_not_modified
def test_bwa_memx_index():
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


@skip_if_not_modified
def test_bwa_memx_mem():
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


@skip_if_not_modified
def test_purge_dups_calcuts():
    run(
        "bio/purge_dups/calcuts",
        ["snakemake", "--cores", "1", "out/calcuts.cutoffs", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_purge_dups_get_seqs():
    run(
        "bio/purge_dups/get_seqs",
        ["snakemake", "--cores", "1", "out/get_seqs.hap.fasta", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_purge_dups_ngscstat():
    run(
        "bio/purge_dups/ngscstat",
        ["snakemake", "--cores", "1", "out/ngscstat.cov", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_purge_dups_pbcstat():
    run(
        "bio/purge_dups/pbcstat",
        ["snakemake", "--cores", "1", "out/pbcstat.cov", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_purge_dups_purge_dups():
    run(
        "bio/purge_dups/purge_dups",
        ["snakemake", "--cores", "1", "out/purge_dups.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_purge_dups_split_fa():
    run(
        "bio/purge_dups/split_fa",
        ["snakemake", "--cores", "1", "out/genome.split", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_quast():
    run(
        "bio/quast",
        ["snakemake", "--cores", "1", "a/quast.log", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gfatools():
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


@skip_if_not_modified
def test_hifiasm():
    run(
        "bio/hifiasm",
        ["snakemake", "--cores", "2", "hifiasm/a.a_ctg.gfa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def meryl_count():
    run(
        "bio/meryl/count",
        ["snakemake", "--cores", "2", "genome", "--use-conda", "-F"],
    )


@skip_if_not_modified
def meryl_sets():
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


@skip_if_not_modified
def meryl_union():
    run(
        "bio/meryl/stats",
        ["snakemake", "--cores", "1", "genome.stats", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_genomescope():
    run(
        "bio/genomescope",
        ["snakemake", "--cores", "1", "a/model.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bellerophon():
    run(
        "bio/bellerophon",
        ["snakemake", "--cores", "2", "out.sam", "--use-conda", "-F"],
    )

    run(
        "bio/bellerophon",
        ["snakemake", "--cores", "2", "out.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pretext_map():
    run(
        "bio/pretext/map",
        ["snakemake", "--cores", "1", "map.pretext", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pretext_snapshot():
    run(
        "bio/pretext/snapshot",
        ["snakemake", "--cores", "1", "full_map.png", "--use-conda", "-F"],
    )

    run(
        "bio/pretext/snapshot",
        ["snakemake", "--cores", "1", "full_map.jpg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_pretext_graph():
    run(
        "bio/pretext/graph",
        ["snakemake", "--cores", "1", "a.pretext", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_salsa2():
    run(
        "bio/salsa2",
        ["snakemake", "--cores", "1", "out/a.agp", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_merqury_haploid():
    run(
        "bio/merqury",
        ["snakemake", "--cores", "1", "results/haploid/out.qv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_merqury_diploid():
    run(
        "bio/merqury",
        ["snakemake", "--cores", "1", "results/diploid/out.qv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_mashmap():
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


@skip_if_not_modified
def test_rbt_csvreport():
    run(
        "bio/rbt/csvreport",
        ["snakemake", "--cores", "1", "qc_data", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_liftoff():
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


@skip_if_not_modified
def test_biobambam2_bamsormadup():
    run(
        "bio/biobambam2/bamsormadup",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bustools_text():
    run(
        "bio/bustools/text",
        ["snakemake", "--cores", "1", "file.tsv", "--use-conda", "-F"],
    )
    run(
        "bio/bustools/text",
        ["snakemake", "--cores", "1", "file2.tsv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_open_cravat_run():
    run(
        "bio/open-cravat/run",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


@skip_if_not_modified
def test_bustools_count():
    run(
        "bio/bustools/count",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "buscount.mtx"],
    )


@skip_if_not_modified
def test_bustools_sort():
    run(
        "bio/bustools/sort",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "sorted.bus"],
    )


@skip_if_not_modified
def test_open_cravat_module():
    run(
        "bio/open-cravat/module",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


@skip_if_not_modified
def test_salmon_tximport_meta():
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
def test_microphaser_normal():
    run(
        "bio/microphaser/normal",
        ["snakemake", "--cores", "1", "out/a.fasta", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_microphaser_somatic():
    run(
        "bio/microphaser/somatic",
        ["snakemake", "--cores", "1", "out/a.info.tsv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_microphaser_build_reference():
    run(
        "bio/microphaser/build_reference",
        ["snakemake", "--cores", "1", "out/peptides.bin", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_microphaser_filter():
    run(
        "bio/microphaser/filter",
        ["snakemake", "--cores", "1", "out/peptides.wt.fasta", "--use-conda", "-F"],
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
def test_deseq2_deseqdataset():
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


@skip_if_not_modified
def test_deseq2_wald():
    run(
        "bio/deseq2/wald",
        ["snakemake", "--cores", "1", "--use-conda", "dge.tsv"]
    )


@skip_if_not_modified
def test_arriba_star_meta():
    run(
        "meta/bio/star_arriba",
        ["snakemake", "--cores", "1", "--use-conda", "results/arriba/a.fusions.tsv"],
    )


@skip_if_not_modified
def test_xsv():
    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_split/0.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_table.txt"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_stats.txt"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_split"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_sort.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_slice.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_select.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_search.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_sample.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_join.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_input.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "table.csv.idx"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_headers_all.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_headers.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_frequency.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_fmt.tsv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_flatten.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_fixlength.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_count.csv"])

    run(
        "bio/xsv",
        ["snakemake", "--cores", "1", "--use-conda", "xsv_count.tsv_as_input.csv"],
    )

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_catrows.csv"])

    run("bio/xsv", ["snakemake", "--cores", "1", "--use-conda", "xsv_catcols.csv"])


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
            "reference/genome.fasta.amb",
            "reference/genome.fasta.ann",
            "reference/genome.fasta.bwt",
            "reference/genome.fasta.dict",
            "reference/genome.fasta.fai",
            "reference/genome.fasta.pac",
            "reference/genome.fasta.sa",
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
def test_seqtk_seq():
    run(
        "bio/seqtk/seq",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "a.fasta"],
    )


@skip_if_not_modified
def test_seqtk_mergepe():
    run(
        "bio/seqtk/mergepe",
        [
            "snakemake",
            "--cores",
            "1",
            "--use-conda",
            "-F",
            "a.merged.fastq.gz",
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
def test_pyroe_id_to_name():
    run(
        "bio/pyroe/idtoname",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "id2name.gtf.tsv"],
    )
    run(
        "bio/pyroe/idtoname",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "id2name.gff3.tsv"],
    )


@skip_if_not_modified
def test_pyroe_makesplicedunspliced():
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


@skip_if_not_modified
def test_pyroe_makesplicedintronic():
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


@skip_if_not_modified
def test_bcftools_filter_sample():
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter_sample.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_filter_vcf():
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_filter_vcf_gz():
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.vcf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_filter_bcf():
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_filter_uncompressed_bcf():
    run(
        "bio/bcftools/filter",
        ["snakemake", "--cores", "1", "a.filter.uncompressed.bcf", "--use-conda", "-F"],
    )


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
def test_bcftools_stats():
    run(
        "bio/bcftools/stats",
        ["snakemake", "--cores", "1", "a.bcf.stats.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_norm():
    run(
        "bio/bcftools/norm",
        ["snakemake", "--cores", "1", "a.norm.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_view_vcf():
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_view_vcf_gz():
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.vcf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_view_bcf():
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bcftools_view_uncompressed_bcf():
    run(
        "bio/bcftools/view",
        ["snakemake", "--cores", "1", "a.view.uncompressed.bcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bedtools_bamtobed():
    run(
        "bio/bedtools/bamtobed",
        ["snakemake", "--cores", "1", "a.bed", "--use-conda", "-F"],
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
def test_bgzip():
    run("bio/bgzip", ["snakemake", "--cores", "1", "test.vcf.gz", "--use-conda", "-F"])


@skip_if_not_modified
def test_blast_makeblastdb_nucleotide():
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


@skip_if_not_modified
def test_blast_makeblastdb_protein():
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


@skip_if_not_modified
def test_blast_blastn():
    run(
        "bio/blast/blastn",
        ["snakemake", "--cores", "1", "a.blast.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bowtie2_align():
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


@skip_if_not_modified
def test_bowtie2_build():
    run(
        "bio/bowtie2/build",
        ["snakemake", "--cores", "1", "genome.1.bt2", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bowtie2_build_large():
    run(
        "bio/bowtie2/build",
        ["snakemake", "--cores", "1", "genome.1.bt2l", "--use-conda", "-F"],
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
def test_bwa_mem_sort_samtools_write_index():
    run(
        "bio/bwa/mem",
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
def test_bwa_meme():
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
            "genome.fasta.pac",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_dragmap_build():
    run(
        "bio/dragmap/build",
        ["snakemake", "--cores", "1", "genome/hash_table.cfg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_dragmap_align():
    run(
        "bio/dragmap/align",
        ["snakemake", "--cores", "1", "mapped/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_dragmap_align_sort_samtools():
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


@skip_if_not_modified
def test_dragmap_align_sort_samtools_write_index():
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


@skip_if_not_modified
def test_dragmap_align_sort_picard():
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


@skip_if_not_modified
def test_clustalo():
    run(
        "bio/clustalo",
        ["snakemake", "--cores", "1", "test.msa.fa", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_coolpuppy():
    run(
        "bio/coolpuppy",
        ["snakemake", "--cores", "1", "CN_1000000.clpy", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_insulation():
    run(
        "bio/cooltools/insulation",
        ["snakemake", "--cores", "1", "CN_1000000.insulation.tsv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_expected_cis():
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


@skip_if_not_modified
def test_cooltools_expected_trans():
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


@skip_if_not_modified
def test_cooltools_eigs_cis():
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


@skip_if_not_modified
def test_cooltools_eigs_trans():
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


@skip_if_not_modified
def test_cooltools_saddle():
    run(
        "bio/cooltools/saddle",
        ["snakemake", "--cores", "1", "CN_1000000.saddledump.npz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_pileup():
    run(
        "bio/cooltools/pileup",
        ["snakemake", "--cores", "1", "CN_1000000.pileup.npz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_dots():
    run(
        "bio/cooltools/dots",
        ["snakemake", "--cores", "1", "HFF_10000.dots.bedpe", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_genome_binnify():
    run(
        "bio/cooltools/genome/binnify",
        ["snakemake", "--cores", "1", "hg38_1000000_bins.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_cooltools_genome_gc():
    run(
        "bio/cooltools/genome/gc",
        ["snakemake", "--cores", "1", "gc_100000.tsv", "--use-conda", "-F"],
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
def test_deeptools_bamcoverage():
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


@skip_if_not_modified
def test_deeptools_alignmentsieve():
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
def test_deeptools_plotcoverage():
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


@skip_if_not_modified
def test_deepvariant():
    run(
        "bio/deepvariant",
        ["snakemake", "--cores", "1", "calls/a.vcf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_deepvariant_gvcf():
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


@skip_if_not_modified
def test_epic_peaks():
    run(
        "bio/epic/peaks",
        ["snakemake", "--cores", "1", "epic/enriched_regions.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bbduk_pe():
    run(
        "bio/bbtools/bbduk",
        ["snakemake", "--cores", "1", "trimmed/pe/a.stats.txt", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_bbduk_se():
    run(
        "bio/bbtools/bbduk",
        ["snakemake", "--cores", "1", "trimmed/se/a.stats.txt", "--use-conda", "-F"],
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
def test_fasttree():
    run(
        "bio/fasttree",
        ["snakemake", "--cores", "1", "test-proteins.nwk", "--use-conda", "-F"],
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
                "calls/a.vcf.gz",
                "--use-conda",
                "-F",
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
        [
            "snakemake",
            "--cores",
            "1",
            "normalized/variants.vcf.gz",
            "--use-conda",
            "-F",
        ],
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
def test_jellyfish_count():
    run(
        "bio/jellyfish/count",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.jf"],
    )


@skip_if_not_modified
def test_jellyfish_dump():
    run(
        "bio/jellyfish/dump",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.dump"],
    )


@skip_if_not_modified
def test_jellyfish_histo():
    run(
        "bio/jellyfish/histo",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "a.histo"],
    )


@skip_if_not_modified
def test_jellyfish_merge():
    run(
        "bio/jellyfish/merge",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "ab.jf"],
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
def test_minimap2_aligner_paf():
    run(
        "bio/minimap2/aligner",
        ["snakemake", "--cores", "1", "aligned/genome_aln.paf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_minimap2_aligner_sam():
    run(
        "bio/minimap2/aligner",
        ["snakemake", "--cores", "1", "aligned/genome_aln.sam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_minimap2_aligner_sam_sorted():
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


@skip_if_not_modified
def test_minimap2_aligner_bam_sorted():
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


@skip_if_not_modified
def test_minimap2_index():
    run(
        "bio/minimap2/index",
        ["snakemake", "--cores", "1", "genome.mmi", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_mosdepth():
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_mosdepth_bed():
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth_bed/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_mosdepth_by_threshold():
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth_by_threshold/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_mosdepth_quantize_precision():
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth_quantize_precision/m54075_180905_225130.ccs.ecoliK12_pbi_March2013.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_mosdepth_cram():
    run(
        "bio/mosdepth",
        [
            "snakemake",
            "--cores",
            "4",
            "mosdepth_cram/a.mosdepth.summary.txt",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_multiqc():
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc.html", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_multiqc_a():
    run(
        "bio/multiqc",
        ["snakemake", "--cores", "1", "qc/multiqc_a.html", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_muscle_super5():
    run(
        "bio/muscle",
        ["snakemake", "--cores", "2", "test-proteins.super5.fas", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_muscle_fas():
    run(
        "bio/muscle",
        ["snakemake", "--cores", "2", "test-proteins.fas", "--use-conda", "-F"],
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
def test_pandora_index():
    run(
        "bio/pandora/index",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "rpsL/prg.fa.k15.w14.idx"],
    )


@skip_if_not_modified
def test_picard_addorreplacegroups():
    run(
        "bio/picard/addorreplacereadgroups",
        ["snakemake", "--cores", "1", "fixed-rg/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_markduplicates_bam():
    run(
        "bio/picard/markduplicates",
        ["snakemake", "--cores", "1", "dedup_bam/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_markduplicateswithmatecigar_bam():
    run(
        "bio/picard/markduplicates",
        [
            "snakemake",
            "--cores",
            "1",
            "dedup_bam/a.matecigar.bam",
            "dedup_bam/a.mcigar.bai",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_picard_markduplicates_sam():
    run(
        "bio/picard/markduplicates",
        ["snakemake", "--cores", "1", "dedup_sam/a.sam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_picard_markduplicates_cram():
    run(
        "bio/picard/markduplicates",
        [
            "snakemake",
            "--cores",
            "1",
            "dedup_cram/a.cram",
            "dedup_cram/a.cram.crai",
            "--use-conda",
            "-F",
        ],
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
        [
            "snakemake",
            "--cores",
            "1",
            "pindel/all_D",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_pindel_call_include():
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


@skip_if_not_modified
def test_pindel_call_exclude():
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
        "bio/sambamba/view",
        ["snakemake", "--cores", "1", "mapped/A.filtered.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_slice():
    run(
        "bio/sambamba/slice",
        ["snakemake", "--cores", "1", "mapped/A.region.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_sambamba_markdup():
    run(
        "bio/sambamba/markdup",
        ["snakemake", "--cores", "1", "mapped/A.rmdup.bam", "--use-conda", "-F"],
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
def test_samtools_fastx():
    run(
        "bio/samtools/fastx",
        ["snakemake", "--cores", "1", "a.fasta", "--use-conda", "-F"],
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
def test_samtools_fastq_interleaved():
    run(
        "bio/samtools/fastq/interleaved",
        ["snakemake", "--cores", "1", "reads/a.fq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_samtools_fastq_separate():
    run(
        "bio/samtools/fastq/separate",
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


@skip_if_not_modified
def test_star_index():
    run("bio/star/index", ["snakemake", "--cores", "1", "genome", "--use-conda", "-F"])


@skip_if_not_modified
def test_snpeff_annotate():
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
def test_strelka_germline():
    run(
        "bio/strelka/germline",
        ["snakemake", "--cores", "1", "strelka/a.vcf.gz", "--use-conda", "-F"],
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
        ["snakemake", "--cores", "1", "trimmed/a_R1.fq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_trim_galore_pe_uncompressed():
    run(
        "bio/trim_galore/pe",
        ["snakemake", "--cores", "1", "trimmed/a_R2.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_trim_galore_se():
    run(
        "bio/trim_galore/se",
        ["snakemake", "--cores", "1", "trimmed/a_trimmed.fq.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_trim_galore_se_uncompressed():
    run(
        "bio/trim_galore/se",
        ["snakemake", "--cores", "1", "trimmed/a_trimmed.fastq", "--use-conda", "-F"],
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
def test_delly():
    run(
        "bio/delly",
        ["snakemake", "--cores", "1", "sv/calls.vcf.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_manta():
    run(
        "bio/manta",
        ["snakemake", "--cores", "2", "results/out.bcf", "--use-conda", "-F"],
    )


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
            "trinity_out_dir.Trinity.fasta",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_salmon_decoys():
    run(
        "bio/salmon/decoys",
        ["snakemake", "--cores", "2", "--use-conda", "-F", "gentrome.fasta.gz"],
    )


@skip_if_not_modified
def test_salmon_index():
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


@skip_if_not_modified
def test_busco():
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


@skip_if_not_modified
def test_vcftoolsfilter():
    run(
        "bio/vcftools/filter",
        ["snakemake", "--cores", "1", "sample.filtered.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_callcopyrationsegments():
    run(
        "bio/gatk/callcopyratiosegments",
        ["snakemake", "--cores", "1", "a.called.seg", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_scatterintervalsbyns():
    run(
        "bio/gatk/scatterintervalsbyns",
        ["snakemake", "--cores", "1", "genome.intervals", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_splitintervals():
    run(
        "bio/gatk/splitintervals",
        ["snakemake", "--cores", "1", "out/genome.00.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_printreadsspark():
    run(
        "bio/gatk/printreadsspark",
        ["snakemake", "--cores", "1", "a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_markduplicatesspark():
    run(
        "bio/gatk/markduplicatesspark",
        ["snakemake", "--cores", "1", "dedup/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_intervallisttobed():
    run(
        "bio/gatk/intervallisttobed",
        ["snakemake", "--cores", "1", "genome.bed", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_estimatelibrarycomplexity():
    run(
        "bio/gatk/estimatelibrarycomplexity",
        ["snakemake", "--cores", "1", "a.metrics", "--use-conda", "-F"],
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
def test_gatk_collectreadcounts():
    run(
        "bio/gatk/collectreadcounts",
        ["snakemake", "--cores", "1", "a.counts.hdf5", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_collectalleliccounts():
    run(
        "bio/gatk/collectalleliccounts",
        ["snakemake", "--cores", "1", "a.counts.tsv", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_applybqsr():
    run(
        "bio/gatk/applybqsr",
        ["snakemake", "--cores", "1", "recal/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_applybqsr_cram():
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


@skip_if_not_modified
def test_gatk_applybqsrspark():
    run(
        "bio/gatk/applybqsrspark",
        ["snakemake", "--cores", "1", "recal/a.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_applybqsrspark_cram():
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


@skip_if_not_modified
def test_gatk_denoisereadcounts():
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


@skip_if_not_modified
def test_gatk_haplotypecaller_vcf():
    run(
        "bio/gatk/haplotypecaller",
        ["snakemake", "--cores", "1", "calls/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_haplotypecaller_gvcf():
    run(
        "bio/gatk/haplotypecaller",
        ["snakemake", "--cores", "1", "calls/a.g.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_modelsegments():
    run(
        "bio/gatk/modelsegments",
        ["snakemake", "--cores", "1", "a.den.modelFinal.seg", "--use-conda", "-F"],
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
            "calls/all.recal.vcf",
            "--use-conda",
            "-F",
        ],
        check_log=check_log,
    )


@skip_if_not_modified
def test_gatk_variantstotable():
    run(
        "bio/gatk/variantstotable",
        ["snakemake", "--cores", "1", "calls/snvs.tab", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_filtermutectcalls():
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


@skip_if_not_modified
def test_gatk_selectvariants():
    run(
        "bio/gatk/selectvariants",
        ["snakemake", "--cores", "1", "calls/snvs.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_variantannotator():
    run(
        "bio/gatk/variantannotator",
        ["snakemake", "--cores", "1", "snvs.annot.vcf", "--use-conda", "-F"],
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
def test_gatk_cleansam():
    run(
        "bio/gatk/cleansam",
        ["snakemake", "--cores", "1", "a.clean.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk3_realignertargetcreator():
    run(
        "bio/gatk3/realignertargetcreator",
        ["snakemake", "--cores", "1", "a.intervals", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk3_indelrealigner():
    run(
        "bio/gatk3/indelrealigner",
        ["snakemake", "--cores", "1", "a.realigned.bam", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk3_baserecalibrator():
    run(
        "bio/gatk3/baserecalibrator",
        ["snakemake", "--cores", "1", "a.recal_data_table", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk3_printreads():
    run(
        "bio/gatk3/printreads",
        ["snakemake", "--cores", "1", "a.bqsr.bam", "--use-conda", "-F"],
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
    run(
        "bio/gatk/mutect",
        ["snakemake", "--cores", "1", "variant_complete/a.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_learn_read_orientation():
    run(
        "bio/gatk/learnreadorientationmodel",
        ["snakemake", "--cores", "1", "--use-conda"],
    )


@skip_if_not_modified
def test_gatk_leftalignandtrimvariants():
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


@skip_if_not_modified
def test_gatk_getpileupsummaries():
    run(
        "bio/gatk/getpileupsummaries",
        ["snakemake", "--cores", "1", "summaries.table", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gatk_mutect_bam():
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


@skip_if_not_modified
def test_gatk_depth_of_coverage():
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
def test_ensembl_annotation_gtf():
    run(
        "bio/reference/ensembl-annotation",
        ["snakemake", "--cores", "1", "refs/annotation.gtf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_ensembl_annotation_gtf_gz():
    run(
        "bio/reference/ensembl-annotation",
        ["snakemake", "--cores", "1", "refs/annotation.gtf.gz", "--use-conda", "-F"],
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
def test_ensembl_variation_chromosome():
    run(
        "bio/reference/ensembl-variation",
        ["snakemake", "-s", "chrom_wise.smk", "--cores", "1", "--use-conda", "-F"],
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
            "bams/a_pe.deduplicated.bam",
            "bams/b.deduplicated.bam",
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
def test_tabix_index():
    run(
        "bio/tabix/index",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "test.vcf.gz.tbi"],
    )


@skip_if_not_modified
def test_tabix_query():
    run(
        "bio/tabix/query",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "A.output.bed"],
    )


# TODO msisensor fails with a segfault, skip tests for now
# @skip_if_not_modified
# def test_msisensor_scan():
#     run(
#         "bio/msisensor/scan",
#         ["snakemake", "--cores", "1", "--use-conda", "-F", "microsat.list"],
#     )


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
def test_fasterq_dump_se():
    run(
        "bio/sra-tools/fasterq-dump",
        ["snakemake", "--cores", "1", "data/se/SRR14133989.fastq", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_fasterq_dump_se_gz():
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


@skip_if_not_modified
def test_fasterq_dump_se_bz2():
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


@skip_if_not_modified
def test_fasterq_dump_pe():
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


@skip_if_not_modified
def test_fasterq_dump_pe_gz():
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


@skip_if_not_modified
def test_fasterq_dump_pe_bz2():
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


@skip_if_not_modified
def test_genefuse():
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
def test_diamond_makedb():
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


@skip_if_not_modified
def test_diamond_blastp():
    run(
        "bio/diamond/blastp",
        ["snakemake", "--cores", "1", "test-protein.tsv.gz", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_applyvqsr():
    run(
        "bio/gatk/applyvqsr",
        ["snakemake", "--cores", "1", "test.snp_recal.vcf", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_nextflow():
    run(
        "utils/nextflow",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "--show-failed-logs"],
    )


@skip_if_not_modified
def test_qualimaprnaseq():
    run(
        "bio/qualimap/rnaseq",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_qualimapbamqc():
    run(
        "bio/qualimap/bamqc",
        ["snakemake", "--cores", "1", "qc/a", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_collectrnaseqmetrics():
    run(
        "bio/picard/collectrnaseqmetrics",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gtftogenepred():
    run(
        "bio/ucsc/gtfToGenePred",
        ["snakemake", "--cores", "1", "annotation.genePred", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_gtftogenepred_picard_collectrnaseqmetrics():
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


@skip_if_not_modified
def test_collectgcbiasmetrics():
    run(
        "bio/picard/collectgcbiasmetrics",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_rsem_calculate_expression():
    run(
        "bio/rsem/calculate-expression",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )

    run(
        "bio/rsem/calculate-expression",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "-s", "Snakefile_fastq"],
    )


@skip_if_not_modified
def test_rsem_prepare_reference():
    run(
        "bio/rsem/prepare-reference",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_generate_data_matrix():
    run(
        "bio/rsem/generate-data-matrix",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_metaspades():
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


@skip_if_not_modified
def test_verifybamid2():
    run(
        "bio/verifybamid/verifybamid2",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_collapse_reads_to_fragments_bam():
    run(
        "bio/rbt/collapse_reads_to_fragments-bam",
        ["snakemake", "--cores", "1", "--use-conda", "-F"],
    )


@skip_if_not_modified
def test_calc_consensus_reads():
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


@skip_if_not_modified
def test_bazam_interleaved():
    run(
        "bio/bazam",
        ["snakemake", "--cores", "1", "--use-conda", "-F", "results/reads/a.fastq.gz"],
    )


@skip_if_not_modified
def test_bazam_separated():
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

@skip_if_not_modified
def test_ragtag_correction():
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


@skip_if_not_modified
def test_ragtag_patch():
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


@skip_if_not_modified
def test_ragtag_scaffold():
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


@skip_if_not_modified
def test_ragtag_merge():
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

@skip_if_not_modified
def test_barrnap():
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
