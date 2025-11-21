__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem, get_format


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
mem_mb = get_mem(snakemake, out_unit="MiB")

# Infer output format
in_format = get_format(snakemake.input[0])

# Redundancy summary
redund_sum = snakemake.output.get("redund_sum", "")
if redund_sum:
    extra += f" -o {redund_sum}"

# Redundancy values
redund_val = snakemake.output.get("redund_val", "")
if redund_val:
    extra += f" -a {redund_val}"

# Mate distribution
mate_distr = snakemake.output.get("mate_distr", "")
if mate_distr:
    extra += f" -C {mate_distr}"

# Log
out_log = snakemake.output.get("log", "")
if out_log:
    extra += f" -l {out_log}"


with tempfile.NamedTemporaryFile() as tmp:
    # Uncompress bzip2 input files
    if Path(snakemake.input[0]).suffix == ".bz2":
        in_uncomp = tmp.name
        shell(
            "pbzip2 -p{snakemake.threads} --decompress --stdout {snakemake.input[0]} > {tmp.name}"
        )
    else:
        in_uncomp = snakemake.input[0]

    # Check if input file is empty
    empty = Path(in_uncomp).stat().st_size == 0
    if Path(in_uncomp).suffix == ".gz" and Path(in_uncomp).stat().st_size < 50:
        import gzip

        with gzip.open(in_uncomp, "rt") as f:
            empty = not bool(f.readlines())

    # If empty, provide dummy input file so that program does not crash
    # https://github.com/lmrodriguezr/nonpareil/issues/71
    if empty:
        in_uncomp = tmp.name
        with open(in_uncomp, "wt") as f:
            if in_format == "fasta":
                f.write("\n".join([">dummy1", "N" * 100]))
            elif in_format == "fastq":
                f.write("\n".join(["@dummy1", "N" * 100, "+", "!" * 100]))
            else:
                raise ValueError(f"invalid format: {in_format}")
            f.write("\n")

    shell(
        "nonpareil"
        " -t {snakemake.threads}"
        " -R {mem_mb}"
        " -T {snakemake.params.alg}"
        " -s {in_uncomp}"
        " -f {in_format}"
        " {extra}"
        " {log}"
    )

    if empty and redund_sum:
        with open(redund_sum, "at") as f:
            f.write("\t".join(["0.000000"] + ["0.00000"] * 5) + "\n")
