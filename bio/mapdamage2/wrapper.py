__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

# Input BAM fle
in_bam = snakemake.input.get("bam", "")
if in_bam:
    in_bam = f"--input {in_bam}"

# Output
out_plot = any([in_tag.startswith("plot_") for in_tag, _ in snakemake.output.items()])
out_stats = any([in_tag.startswith("stats_") for in_tag, _ in snakemake.output.items()])
out_bam = snakemake.output.get("bam", "")
if out_bam:
    out_bam = f"--rescale --rescale-out {out_bam}"

# Check if only tpye of output is specified
# https://stackoverflow.com/questions/16801322/how-can-i-check-that-a-list-has-one-and-only-one-truthy-value
i = iter([out_plot, out_stats, out_bam])
if any(i) and not any(i):
    if out_plot:
        extra += " --no-stats"
    elif out_stats:
        extra += " --stats-only"
    elif out_bam:
        extra += " --rescale-only"
    else:
        raise ValueError("unexpected error.")


with tempfile.TemporaryDirectory() as tmpdir:
    fnames_tmp = {
        "GtoA3p": "3pGtoA_freq.txt",
        "CtoT5p": "5pCtoT_freq.txt",
        "dnacomp": "dnacomp.txt",
        "lg_dist": "lgdistribution.txt",
        "misinc": "misincorporation.txt",
        "plot_misinc": "Fragmisincorporation_plot.pdf",
        "plot_len": "Length_plot.pdf",
        "log": "Runtime_log.txt",
        "stats_ref": "dnacomp_genome.csv",
        "stats_prob": "Stats_out_MCMC_correct_prob.csv",
        "stats_hist": "Stats_out_MCMC_hist.pdf",
        "stats_iter": "Stats_out_MCMC_iter.csv",
        "stats_summ": "Stats_out_MCMC_iter_summ_stat.csv",
        "stats_plot_freq": "Stats_out_MCMC_post_pred.pdf",
        "stats_plot_trace": "Stats_out_MCMC_trace.pdf",
    }

    # Symlink input files to temp (to use as results) folder
    for in_tag, fname_tmp in snakemake.input.items():
        if in_tag not in ["bam", "ref"]:
            (Path(tmpdir) / fnames_tmp[in_tag]).symlink_to(Path(fname_tmp).resolve())

    shell(
        "mapDamage"
        " {in_bam}"
        " --reference {snakemake.input.ref}"
        " --folder {tmpdir}"
        " {out_bam}"
        " {extra}"
        " {log}"
    )

    for in_tag, fname_tmp in fnames_tmp.items():
        fname_dest = snakemake.output.get(in_tag)
        if fname_dest:
            shell("cp --verbose {tmpdir}/{fname_tmp} {fname_dest} {log}")
