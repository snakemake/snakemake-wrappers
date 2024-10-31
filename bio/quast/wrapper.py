__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"-r {ref}"

gff = snakemake.input.get("gff", "")
if gff:
    gff = f"--features {gff}"

pe1 = snakemake.input.get("pe1", "")
if pe1:
    pe1 = f"--pe1 {pe1}"
pe2 = snakemake.input.get("pe2", "")
if pe2:
    pe2 = f"--pe2 {pe2}"
pe12 = snakemake.input.get("pe12", "")
if pe12:
    pe12 = f"--pe12 {pe12}"
mp1 = snakemake.input.get("mp1", "")
if mp1:
    mp1 = f"--mp1 {mp1}"
mp2 = snakemake.input.get("mp2", "")
if mp2:
    mp2 = f"--mp2 {mp2}"
mp12 = snakemake.input.get("mp12", "")
if mp12:
    mp12 = f"--mp12 {mp12}"
single = snakemake.input.get("single", "")
if single:
    single = f"--single {single}"
pacbio = snakemake.input.get("pacbio", "")
if pacbio:
    pacbio = f"--pacbio {pacbio}"
nanopore = snakemake.input.get("nanopore", "")
if nanopore:
    nanopore = f"--nanopore {nanopore}"
ref_bam = snakemake.input.get("ref_bam", "")
if ref_bam:
    ref_bam = f"--ref-bam {ref_bam}"
ref_sam = snakemake.input.get("ref_sam", "")
if ref_sam:
    ref_sam = f"--ref-sam {ref_sam}"
bam = snakemake.input.get("bam", "")
if bam:
    if isinstance(bam, list):
        bam = ",".join(bam)
    bam = f"--bam {bam}"
sam = snakemake.input.get("sam", "")
if sam:
    if isinstance(sam, list):
        sam = ",".join(sam)
    sam = f"--sam {sam}"
sv_bedpe = snakemake.input.get("sv_bedpe", "")
if sv_bedpe:
    sv_bedpe = f"--sv-bedpe {sv_bedpe}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "quast --threads {snakemake.threads} {ref} {gff} {pe1} {pe2} {pe12} {mp1} {mp2} {mp12} {single} {pacbio} {nanopore} {ref_bam} {ref_sam} {bam} {sam} {sv_bedpe} {extra} -o {tmpdir} {snakemake.input.fasta} {log}"
    )

    fasta_name = Path(snakemake.input.fasta).with_suffix("").name

    ### Copy files to final destination
    def save_output(src, dst, wd=Path(".")):
        if not dst:
            return 0
        dest = wd / dst
        shell("cat {src} > {dest}")

    ### Saving OUTPUT files
    # Report files
    for ext in ["html", "pdf", "tex", "txt", "tsv"]:
        save_output(f"{tmpdir}/report." + ext, snakemake.output.get(f"report_{ext}"))
        save_output(
            f"{tmpdir}/transposed_report." + ext, snakemake.output.get(f"treport_{ext}")
        )
    # Stats files
    save_output(
        f"{tmpdir}/basic_stats/cumulative_plot.pdf", snakemake.output.get("stats_cum")
    )
    save_output(
        f"{tmpdir}/basic_stats/GC_content_plot.pdf",
        snakemake.output.get("stats_gc_plot"),
    )
    save_output(
        f"{tmpdir}/basic_stats/gc.icarus.txt", snakemake.output.get("stats_gc_icarus")
    )
    save_output(
        f"{tmpdir}/basic_stats/{fasta_name}_GC_content_plot.pdf",
        snakemake.output.get("stats_gc_fasta"),
    )
    save_output(f"{tmpdir}/basic_stats/NGx_plot.pdf", snakemake.output.get("stats_ngx"))
    save_output(f"{tmpdir}/basic_stats/Nx_plot.pdf", snakemake.output.get("stats_nx"))
    # Contig reports
    save_output(
        f"{tmpdir}/contigs_reports/all_alignments_{fasta_name}.tsv",
        snakemake.output.get("contigs"),
    )
    save_output(
        f"{tmpdir}/contigs_reports/contigs_report_{fasta_name}.mis_contigs.info",
        snakemake.output.get("contigs_mis"),
    )
    # Icarus
    save_output(f"{tmpdir}/icarus.html", snakemake.output.get("icarus"))
    save_output(
        f"{tmpdir}/icarus_viewers/contig_size_viewer.html",
        snakemake.output.get("icarus_viewer"),
    )
