__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smed"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


panel_of_normal = ""
if snakemake.input.get("pon", None):
    panel_of_normal = "--count-panel-of-normals {snakemake.input.pon}"


gc_intervals = ""
if snakemake.input.get("gc_interval", None):
    gc_intervals = "--annotated-intervals {snakemake.input.gc_interval}"

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' DenoiseReadCounts"
        " -I {snakemake.input.hdf5} "
        " {panel_of_normal}"
        " {gc_intervals}"
        " --standardized-copy-ratios {snakemake.output.std_copy_ratio}"
        " --denoised-copy-ratios {snakemake.output.denoised_copy_ratio}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )
