__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    # Configure Manta
    "configManta.py --bam {snakemake.input.samples} --referenceFasta {snakemake.input.ref} --runDir {snakemake.outdir} {log}; "
    # Run Manta
    "{snakemake.outdir}/runWorkflow.py --mode local --jobs {snakemake.threads} --memGb {snakemake.resources.mem_gb} {log}; "
)
