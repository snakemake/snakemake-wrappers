__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
import tempfile
from pathlib import Path
from snakemake.shell import shell

meryldb_parents = snakemake.input.get("meryldb_parents", "")
out_prefix = "out"
log_tmp = "__LOG__.tmp"


with tempfile.TemporaryDirectory() as tmpdir:
    cwd = Path.cwd()
    # Create symlinks for input files
    for input in snakemake.input:
        src = Path(input)
        dst = Path(tmpdir) / input
        src = Path(os.path.relpath(src.resolve(), dst.resolve().parent))
        dst.symlink_to(src)
    os.chdir(tmpdir)

    shell(
        "merqury.sh"
        " {snakemake.input.meryldb}"
        " {meryldb_parents}"
        " {snakemake.input.fasta}"
        " {out_prefix}"
        " > {log_tmp} 2>&1"
    )

    if snakemake.log.get("std"):
        out = cwd / str(snakemake.log.std)
        shell("mv {log_tmp} {out}")
    if snakemake.log.get("spectra_cn"):
        out = cwd / str(snakemake.log.spectra_cn)
        shell("mv logs/{out_prefix}.spectra-cn.log {out}")

    meryldb = Path(snakemake.input.meryldb.rstrip("/")).stem
    if snakemake.output.get("meryldb_filt"):
        out = cwd / snakemake.output.meryldb_filt
        shell("cat {meryldb}.filt > {out}")
    if snakemake.output.get("meryldb_hist"):
        out = cwd / snakemake.output.meryldb_hist
        shell("cat {meryldb}.hist > {out}")
    if snakemake.output.get("meryldb_hist_ploidy"):
        out = cwd / snakemake.output.meryldb_hist_ploidy
        shell("cat {meryldb}.hist.ploidy > {out}")

    if snakemake.output.get("completeness_stats"):
        out = cwd / snakemake.output.completeness_stats
        shell("cat {out_prefix}.completeness.stats > {out}")
    if snakemake.output.get("dist_only_hist"):
        out = cwd / snakemake.output.dist_only_hist
        shell("cat {out_prefix}.dist_only.hist > {out}")
    if snakemake.output.get("only_hist"):
        out = cwd / snakemake.output.only_hist
        shell("cat {out_prefix}.only.hist > {out}")
    if snakemake.output.get("qv"):
        out = cwd / snakemake.output.qv
        shell("cat {out_prefix}.qv > {out}")

    if snakemake.output.get("spectra_asm_hist"):
        out = cwd / snakemake.output.spectra_asm_hist
        shell("cat {out_prefix}.spectra-asm.hist > {out}")
    if snakemake.output.get("spectra_asm_ln_png"):
        out = cwd / snakemake.output.spectra_asm_ln_png
        shell("mv {out_prefix}.spectra-asm.ln.png {out}")
    if snakemake.output.get("spectra_asm_fl_png"):
        out = cwd / snakemake.output.spectra_asm_fl_png
        shell("mv {out_prefix}.spectra-asm.fl.png {out}")
    if snakemake.output.get("spectra_asm_st_png"):
        out = cwd / snakemake.output.spectra_asm_st_png
        shell("mv {out_prefix}.spectra-asm.st.png {out}")

    if snakemake.output.get("spectra_cn_hist"):
        out = cwd / snakemake.output.spectra_cn_hist
        shell("cat {out_prefix}.spectra-cn.hist > {out}")
    if snakemake.output.get("spectra_cn_ln_png"):
        out = cwd / snakemake.output.spectra_cn_ln_png
        shell("mv {out_prefix}.spectra-cn.ln.png {out}")
    if snakemake.output.get("spectra_cn_fl_png"):
        out = cwd / snakemake.output.spectra_cn_fl_png
        shell("mv {out_prefix}.spectra-cn.fl.png {out}")
    if snakemake.output.get("spectra_cn_st_png"):
        out = cwd / snakemake.output.spectra_cn_st_png
        shell("mv {out_prefix}.spectra-cn.st.png {out}")

    if snakemake.output.get("hapmers_count"):
        out = cwd / snakemake.output.hapmers_count
        shell("cat {out_prefix}.hapmers.count > {out}")
    if snakemake.output.get("hapmers_png"):
        out = cwd / snakemake.output.hapmers_png
        shell("mv {out_prefix}.hapmers.blob.png {out}")

    input_fas = snakemake.input.fasta
    if isinstance(input_fas, str):
        input_fas = [input_fas]

    for fas in range(1, len(input_fas) + 1):
        prefix = Path(input_fas[fas - 1]).name.removesuffix(".fasta")

        out = snakemake.output.get(f"fas{fas}_only_bed")
        if out:
            out = cwd / out
            shell("cat {prefix}_only.bed > {out}")
        out = snakemake.output.get(f"fas{fas}_only_wig")
        if out:
            out = cwd / out
            shell("cat {prefix}_only.wig > {out}")

        out = snakemake.output.get(f"fas{fas}_only_hist")
        if out:
            out = cwd / out
            shell("cat {out_prefix}.{prefix}.only.hist > {out}")
        out = snakemake.output.get(f"fas{fas}_qv")
        if out:
            out = cwd / out
            shell("cat {out_prefix}.{prefix}.qv > {out}")
        out = snakemake.output.get(f"fas{fas}_spectra_hist")
        if out:
            out = cwd / out
            shell("cat {out_prefix}.{prefix}.spectra-cn.hist > {out}")
        out = snakemake.output.get(f"fas{fas}_spectra_ln_png")
        if out:
            out = cwd / out
            shell("mv {out_prefix}.{prefix}.spectra-cn.ln.png {out}")
        out = snakemake.output.get(f"fas{fas}_spectra_fl_png")
        if out:
            out = cwd / out
            shell("mv {out_prefix}.{prefix}.spectra-cn.fl.png {out}")
        out = snakemake.output.get(f"fas{fas}_spectra_st_png")
        if out:
            out = cwd / out
            shell("mv {out_prefix}.{prefix}.spectra-cn.st.png {out}")
