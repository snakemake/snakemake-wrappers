__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

tool = snakemake.params.get("tool", "quast")
if tool not in {"quast", "metaquast"}:
    raise ValueError("Invalid params.tool: must be one of 'quast' or 'metaquast'.")

ref = snakemake.input.get("ref", "")
ref_ls = snakemake.input.get("ref_ls", "")
blast_db = snakemake.input.get("blast_db", "")

if ref and ref_ls:
    raise ValueError("Inputs 'ref' and 'ref_ls' are mutually exclusive.")

if tool == "quast" and (ref_ls or blast_db):
    raise ValueError("Inputs 'ref_ls' and 'blast_db' can only be used with metaquast.")

if tool == "quast" and isinstance(ref, list):
    raise ValueError("Input 'ref' must be a single reference when using quast.")

if ref:
    if isinstance(ref, list):
        ref = ",".join(ref)
    ref = f"-r {ref}"
if ref_ls:
    ref_ls = f"--references-list {ref_ls}"
if blast_db:
    blast_db = f"--blast-db {blast_db}"

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
        "{tool} {snakemake.input.fasta} --threads {snakemake.threads} {ref} {ref_ls} {blast_db} {gff} {pe1} {pe2} {pe12} {mp1} {mp2} {mp12} {single} {pacbio} {nanopore} {ref_bam} {ref_sam} {bam} {sam} {sv_bedpe} {extra} -o {tmpdir} {log}"
    )

    fasta_name = Path(snakemake.input.fasta).with_suffix("").name

    output_dir = tmpdir
    if tool == "metaquast":
        output_dir = f"{tmpdir}/combined_reference"

    ### Copy files to final destination
    def save_output(src, dst, wd=Path(".")):
        if not dst:
            return 0
        dest = wd / dst
        shell("cat {src} > {dest}")

    ### Saving OUTPUT files
    # Report files
    for ext in ["html", "pdf", "tex", "txt", "tsv"]:
        save_output(
            f"{output_dir}/report." + ext, snakemake.output.get(f"report_{ext}")
        )
        save_output(
            f"{output_dir}/transposed_report." + ext,
            snakemake.output.get(f"treport_{ext}"),
        )
    # Stats files
    save_output(
        f"{output_dir}/basic_stats/cumulative_plot.pdf",
        snakemake.output.get("stats_cum"),
    )
    save_output(
        f"{output_dir}/basic_stats/GC_content_plot.pdf",
        snakemake.output.get("stats_gc_plot"),
    )
    save_output(
        f"{output_dir}/basic_stats/gc.icarus.txt",
        snakemake.output.get("stats_gc_icarus"),
    )
    save_output(
        f"{output_dir}/basic_stats/{fasta_name}_GC_content_plot.pdf",
        snakemake.output.get("stats_gc_fasta"),
    )
    save_output(
        f"{output_dir}/basic_stats/NGx_plot.pdf", snakemake.output.get("stats_ngx")
    )
    save_output(
        f"{output_dir}/basic_stats/Nx_plot.pdf", snakemake.output.get("stats_nx")
    )
    # Contig reports
    save_output(
        f"{output_dir}/contigs_reports/all_alignments_{fasta_name}.tsv",
        snakemake.output.get("contigs"),
    )
    save_output(
        f"{output_dir}/contigs_reports/contigs_report_{fasta_name}.mis_contigs.info",
        snakemake.output.get("contigs_mis"),
    )
    # Icarus
    save_output(f"{output_dir}/icarus.html", snakemake.output.get("icarus"))
    save_output(
        f"{output_dir}/icarus_viewers/contig_size_viewer.html",
        snakemake.output.get("icarus_viewer"),
    )
