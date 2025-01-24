__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smed"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


input_copy_ratio_seg = snakemake.input.copy_ratio_seg

called_copy_ratio_seg = snakemake.output.called_copy_ratio_seg

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    outputfile_call = os.path.join(tmpdir, "temp.seq")
    outputfile_igv = os.path.join(tmpdir, "temp.igv.seg")
    shell(
        "gatk --java-options '{java_opts}' CallCopyRatioSegments"
        " -I {input_copy_ratio_seg}"
        " -O {outputfile_call}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )
    shell("cp {outputfile_call} {called_copy_ratio_seg}")
    if snakemake.output.get("igv_seg", None):
        shell("cp {outputfile_igv} {snakemake.output.igv_seg}")
