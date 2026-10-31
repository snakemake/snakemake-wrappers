__author__ = "Luca Celebrano"
__copyright__ = "Copyright 2026, Luca Celebrano"
__email__ = "l.celebrano@studenti.unina.it"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
if "--pattern" in extra:
    raise ValueError("Specify pattern via params.pattern, not extra.")

pattern = snakemake.params["pattern"]
normalized_pattern = pattern.lower().replace("-", "").strip()
if "micropapillary" in normalized_pattern:
    raise ValueError(
        "The 'micropapillary' pattern is temporarily unsupported in "
        "spatial-continuum 1.0.2 due to upstream matching order."
    )
tp53 = snakemake.params.get("tp53", "wt")
rb1 = snakemake.params.get("rb1", "wt")
stroma = snakemake.params.get("stroma", "moderate")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "cri-calc"
    " --pattern '{pattern}'"
    " --tp53 '{tp53}'"
    " --rb1 '{rb1}'"
    " --stroma '{stroma}'"
    " {extra}"
    " > {snakemake.output.report:q}"
    " {log}"
)
