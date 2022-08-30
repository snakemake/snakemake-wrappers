__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

meryldb_parents = snakemake.input.get("meryldb_parents", "")


shell(
    "merqury.sh"
    " {snakemake.input.meryldb}"
    " {meryldb_parents}"
    " {snakemake.input.fasta}"
    " out"
    " {log}"
)

meryldb = Path(snakemake.input.meryldb.rstrip("/")).stem

if snakemake.output.get("meryldb_filt"):
    shell("cat {meryldb}.filt > {snakemake.output.meryldb_filt}")
if snakemake.output.get("meryldb_hist"):
    shell("cat {meryldb}.hist > {snakemake.output.meryldb_hist}")
if snakemake.output.get("meryldb_hist_ploidy"):
    shell("cat {meryldb}.hist.ploidy > {snakemake.output.meryldb_hist_ploidy}")

if snakemake.output.get("completeness_stats"):
    shell("cat out.completeness.stats > {snakemake.output.completeness_stats}")
if snakemake.output.get("dist_only_hist"):
    shell("cat out.dist_only.hist > {snakemake.output.dist_only_hist}")
if snakemake.output.get("only_hist"):
    shell("cat out.only.hist > {snakemake.output.only_hist}")
if snakemake.output.get("qv"):
    shell("cat out.qv > {snakemake.output.qv}")

if snakemake.output.get("spectra_asm_hist"):
    shell("cat out.spectra-asm.hist > {snakemake.output.spectra_asm_hist}")
if snakemake.output.get("spectra_asm_ln_png"):
    shell("mv out.spectra-asm.ln.png {snakemake.output.spectra_asm_ln_png}")
if snakemake.output.get("spectra_asm_fl_png"):
    shell("mv out.spectra-asm.fl.png {snakemake.output.spectra_asm_fl_png}")
if snakemake.output.get("spectra_asm_st_png"):
    shell("mv out.spectra-asm.st.png {snakemake.output.spectra_asm_st_png}")

if snakemake.output.get("spectra_cn_hist"):
    shell("cat out.spectra-cn.hist > {snakemake.output.spectra_cn_hist}")
if snakemake.output.get("spectra_cn_ln_png"):
    shell("mv out.spectra-cn.ln.png {snakemake.output.spectra_cn_ln_png}")
if snakemake.output.get("spectra_cn_fl_png"):
    shell("mv out.spectra-cn.fl.png {snakemake.output.spectra_cn_fl_png}")
if snakemake.output.get("spectra_cn_st_png"):
    shell("mv out.spectra-cn.st.png {snakemake.output.spectra_cn_st_png}")

if snakemake.output.get("hapmers_count"):
    shell("cat out.hapmers.count > {snakemake.output.hapmers_count}")
if snakemake.output.get("hapmers_png"):
    shell("mv out.hapmers.blob.png {snakemake.output.hapmers_png}")

if snakemake.output.get("logs"):
    Path(snakemake.output.logs).mkdir(parents=True, exist_ok=True)
    for log in Path("logs").iterdir():
        if log.is_file() and str(log) != str(snakemake.log):
            shell("mv {log} {snakemake.output.logs}/{log.name}")

input_fas = snakemake.input.fasta
if isinstance(input_fas, str):
    input_fas = [input_fas]

for fas in range(1, len(input_fas) + 1):
    prefix = Path(input_fas[fas - 1]).name.removesuffix(".fasta")

    out = snakemake.output.get(f"fas{fas}_only_bed")
    if out:
        shell("cat {prefix}_only.bed > {out}")
    out = snakemake.output.get(f"fas{fas}_only_wig")
    if out:
        shell("cat {prefix}_only.wig > {out}")

    out = snakemake.output.get(f"fas{fas}_only_hist")
    if out:
        shell("cat out.{prefix}.only.hist > {out}")
    out = snakemake.output.get(f"fas{fas}_qv")
    if out:
        shell("cat out.{prefix}.qv > {out}")
    out = snakemake.output.get(f"fas{fas}_spectra_hist")
    if out:
        shell("cat out.{prefix}.spectra-cn.hist > {out}")
    out = snakemake.output.get(f"fas{fas}_spectra_ln_png")
    if out:
        shell("mv out.{prefix}.spectra-cn.ln.png {out}")
    out = snakemake.output.get(f"fas{fas}_spectra_fl_png")
    if out:
        shell("mv out.{prefix}.spectra-cn.fl.png {out}")
    out = snakemake.output.get(f"fas{fas}_spectra_st_png")
    if out:
        shell("mv out.{prefix}.spectra-cn.st.png {out}")
