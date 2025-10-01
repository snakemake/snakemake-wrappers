__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
prior_opt = snakemake.params.get("prior", "")
sample_name = snakemake.params.get("sample_name", "")

# only add --sample-name if a sample name is given
sample_name_opt = f"--sample-name {sample_name}" if sample_name else ""

shell(
    "orthanq call hla --haplotype-calls {snakemake.input.haplotype_calls} "
    " --haplotype-variants {snakemake.input.haplotype_variants} --prior {prior_opt} "
    " --xml {snakemake.input.xml} --output {snakemake.output[0]} {sample_name_opt} {log}"
)
