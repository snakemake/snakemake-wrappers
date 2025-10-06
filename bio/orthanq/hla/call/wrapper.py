__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

#for HLA typing of normal samples, use diploid, for virus quantification, use uniform.
prior_opt = snakemake.params.get("prior", "")

#in case the preprocessed BCF contains multi sample records, use --sample-name
extra = snakemake.params.get("extra", "")

shell(
    "orthanq call hla --haplotype-calls {snakemake.input.haplotype_calls} "
    " --haplotype-variants {snakemake.input.haplotype_variants} --prior {prior_opt} "
    " --xml {snakemake.input.xml} --output {snakemake.output[0]} {extra} {log}"
)
