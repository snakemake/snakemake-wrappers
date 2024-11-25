# coding: utf-8

"""Snakemake wrapper for NGS-Checkmate"""

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os.path import isdir, basename


def make_list_file_for_bam_vcf(paths, output):
    """
    Build a list file from a list of paths
    as described at:
    https://github.com/parklab/NGSCheckMate?tab=readme-ov-file#input-file-list-format

    Parameters:
    paths   list[str]: List of paths to VCF/BAM files
    output  str      : Path to temporary output list file
    """
    with open(output, "w") as outstream:
        outstream.write("\n".join(paths))


def make_list_file_for_fastq(paths, output, is_paired):
    """
    Build a list file from a list of paths
    as described at:
    https://github.com/parklab/NGSCheckMate?tab=readme-ov-file#input-file-list-format

    Parameters:
    paths       list[str]: List of paths to FastQ files
    output      str      : Path to temporary output file
    is_paired   bool     : True if reads are paired, else False
    """
    with open(output, "w") as outstream:
        if is_paired:
            r1_paths = paths[::2]
            r2_paths = paths[1::2]
            names = [basename(fq) for fq in r1_paths]
            lines = [
                "\t".join([r1, r2, name])
                for r1, r2, name in zip(r1_paths, r2_paths, names)
            ]
        else:
            names = [basename(fq) for fq in paths]
            lines = ["\t".join([path, name]) for path, name in zip(paths, names)]

        outstream.write("\n".join(lines))


log = snakemake.log_fmt_shell(
    stdout=True,
    stderr=True,
    append=True,
)
extra = snakemake.params.get("extra", "")

launcher = "ncm.py"

# Pattern file is expected for FastQ files only
pattern = snakemake.input.get("pattern", "")
bed = snakemake.input.get("bed", "")
if bed:
    extra += f" --bedfile {bed} "

with TemporaryDirectory() as tempdir:
    samples = snakemake.input.get("samples")
    list_file = f"{tempdir}/list_file.txt"
    if samples:
        if len(samples) == 1:
            samples = [str(samples)]
        else:
            samples = list(map(str, samples))

        if all(sample.lower().endswith((".bam", "sam")) for sample in samples):
            extra += f" --BAM --bedfile {snakemake.input.bed} "
            make_list_file_for_bam_vcf(paths=samples, output=list_file)
        elif all(
            sample.lower().endswith((".vcf", ".bcf", ".vcf.gz")) for sample in samples
        ):
            extra += f"--VCF --bedfile {snakemake.input.bed} "
            make_list_file_for_bam_vcf(paths=samples, output=list_file)
        elif all(
            sample.lower().endswith((".fastq", ".fq", ".fastq.gz", ".fq.fq"))
            for sample in samples
        ):
            launcher = "ncm_fastq.py"
            extra += f" --pt {snakemake.input.pattern} "
            make_list_file_for_fastq(
                paths=samples,
                output=list_file,
                is_paired=snakemake.params.get("paired", True),
            )

            # Only ncm_fastq.py handles multithreading
            extra += f" --maxthread {snakemake.threads} "
        else:
            raise ValueError("Mixed BAM/VCF/Fastq. Please provide only one file type.")

    list_file = snakemake.input.get("list_file", list_file)
    extra += f" --list {list_file} "

    cmd = (
        f"export NCM_REF='{snakemake.input.fasta}' && "
        f"{launcher} {extra} --outdir {tempdir} "
        f"-N snake_out {log} "
    )
    shell("echo '{cmd}' {log}")
    shell(cmd)

    shell("tree -srhf {tempdir} {log} ")

    pdf = snakemake.output.get("pdf")
    if pdf:
        # Warning: A PDF file is produced only when more that one sample is provided
        shell("mv --verbose {tempdir}/snake_out.pdf {pdf} {log}")

    matched = snakemake.output.get("match")
    if matched:
        shell("mv --verbose {tempdir}/snake_out_matched.txt {matched} {log}")

    txt = snakemake.output.get("txt")
    if txt:
        shell("mv --verbose {tempdir}/snake_out_all.txt {txt} {log}")

    matrix = snakemake.output.get("matrix")
    if matrix:
        shell("mv --verbose {tempdir}/snake_out_output_corr_matrix.txt {matrix} {log}")

    rscript = snakemake.output.get("r")
    if rscript:
        shell("mv --verbose {tempdir}/r_script.r {rscript} {log}")

    out_list_file = snakemake.output.get("list_file")
    if out_list_file:
        shell("mv --verbose {list_file} {out_list_file} {log}")
