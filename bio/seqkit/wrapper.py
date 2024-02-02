__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


extra_input = " ".join(
    [
        (
            f"--{key.replace('_','-')} {value}"
            if key in ["bed", "gtf"]
            else f"--{key.replace('_','-')}-file {value}"
        )
        for key, value in snakemake.input.items()
    ][1:]
)

extra_output = " ".join(
    [
        (
            f"--{key.replace('_','-')} {value}"
            if key in ["read1", "read2"]
            else f"--{key.replace('_','-')}-file {value}"
        )
        for key, value in snakemake.output.items()
    ][1:]
)


shell(
    "seqkit {snakemake.params.command}"
    " --threads {snakemake.threads}"
    " {extra_input}"
    " {extra_output}"
    " {extra}"
    " --out-file {snakemake.output[0]}"
    " {snakemake.input[0]}"
    " {log}"
)
