__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

tool = snakemake.params.get("tool", "ngsngs")
assert tool in ["ngsngs", "LenConvert", "MisConvert", "MetaMisConvert", "RandRef", "RandVar", "QualConvert", "VCFtoBED", "RemoveCodon"], "invalid tool specified"

threads = f"--threads {snakemake.threads}" if tool == "ngsngs" else ""

input = f"--input {snakemake.input[0]}" if len(snakemake.input) else ""

output = ",".join([str(value) for key, value in snakemake.output.items() if key != "pos"])
output_extra = " ".join([f"--{key} {value}" for key, value in snakemake.output.items() if key == "pos"])


shell("{tool} {threads} {input} {extra} --output {output} {output_extra} {log}")
