__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
import tempfile
from pathlib import Path
from snakemake.shell import shell


out_prefix = "out"

with tempfile.TemporaryDirectory() as tmpdir:
    cwd = Path.cwd()
    # MerylDBs
    meryldb = Path(snakemake.input.meryldb).resolve()
    meryldb_parents = snakemake.input.get("meryldb_parents", "")
    if meryldb_parents:
        meryldb_parents = Path(meryldb_parents).resolve()
    # FASTA
    fasta = snakemake.input.fasta
    if isinstance(fasta, str):
        fasta = [fasta]
    fasta = [Path(f).resolve() for f in fasta]
    # LOG
    log = snakemake.log.get("std")
    if log:
        log = f"> {Path(log).resolve()} 2>&1"
    os.chdir(tmpdir)

    shell(
        "merqury.sh"
        " {meryldb}"
        " {meryldb_parents}"
        " {fasta}"
        " {out_prefix}"
        " {log}"
    )

    ### Copy files to final destination
    def save_output(src, dst):
        if not dst:
            return 0
        shell("cat {src} > {dst}")

    ### Saving LOG files
    for type in ["spectra_cn"]:
        save_output(
            f"logs/{out_prefix}." + type.replace("_", "-") + ".log",
            cwd / snakemake.log.get(type),
        )

    ### Saving OUTPUT files
    # EXT: replace all "_" with "."
    meryldb = Path(snakemake.input.meryldb.rstrip("/")).stem
    for type in ["filt", "hist", "hist_ploidy"]:
        save_output(
            f"{meryldb}." + type.replace("_", "."), cwd / snakemake.output.get(type)
        )

    # EXT: replace last "_" with "."
    for type in [
        "completeness_stats",
        "dist_only_hist",
        "only_hist",
        "qv",
        "hapmers_count",
        "hapmers_blob_png",
    ]:
        save_output(
            f"{out_prefix}." + type[::-1].replace("_", ".", 1)[::-1],
            cwd / snakemake.output.get(type),
        )

    # EXT: replace first "_" with "-", and remaining with "."
    for type in [
        "spectra_asm_hist",
        "spectra_asm_ln_png",
        "spectra_asm_fl_png",
        "spectra_asm_st_png",
        "spectra_cn_hist",
        "spectra_cn_ln_png",
        "spectra_cn_fl_png",
        "spectra_cn_st_png",
    ]:
        save_output(
            f"{out_prefix}." + type.replace("_", ".").replace(".", "-", 1),
            cwd / snakemake.output.get(type),
        )

    input_fas = snakemake.input.fasta
    if isinstance(input_fas, str):
        input_fas = [input_fas]

    for fas in range(1, len(input_fas) + 1):
        prefix = Path(input_fas[fas - 1]).name.removesuffix(".fasta")

        # EXT: remove everything until first "_" and replace last "_" with "."
        for type in [f"fas{fas}_only_bed", f"fas{fas}_only_wig"]:
            save_output(
                prefix + type[type.find("_") :][::-1].replace("_", ".", 1)[::-1],
                cwd / snakemake.output.get(type),
            )

        # EXT: remove everything until first "_" and replace all "_" with "."
        for type in [f"fas{fas}_only_hist", f"fas{fas}_qv"]:
            save_output(
                f"{out_prefix}.{prefix}" + type[type.find("_") :].replace("_", "."),
                cwd / snakemake.output.get(type),
            )

        # EXT: remove everything until first "_", replace first "_" with "-", and remaining with "."
        for type in [
            f"fas{fas}_spectra_cn_hist",
            f"fas{fas}_spectra_cn_ln_png",
            f"fas{fas}_spectra_cn_fl_png",
            f"fas{fas}_spectra_cn_st_png",
        ]:
            save_output(
                f"{out_prefix}.{prefix}."
                + type[type.find("_") + 1 :].replace("_", ".").replace(".", "-", 1),
                cwd / snakemake.output.get(type),
            )
