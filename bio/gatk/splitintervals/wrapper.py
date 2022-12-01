__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

n_out_files = len(snakemake.output)
assert n_out_files > 1, "you need to specify more than 2 output files!"

prefix = Path(os.path.commonprefix(snakemake.output))
suffix = os.path.commonprefix([file[::-1] for file in snakemake.output])[::-1]
chunk_labels = [
    out.removeprefix(str(prefix)).removesuffix(suffix) for out in snakemake.output
]
assert all(
    [chunk_label.isnumeric() for chunk_label in chunk_labels]
), "all chunk labels have to be numeric!"
len_chunk_labels = set([len(chunk_label) for chunk_label in chunk_labels])
assert len(len_chunk_labels) == 1, "all chunk labels must have the same length!"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' SplitIntervals"
        " --intervals {snakemake.input.intervals}"
        " --reference {snakemake.input.ref}"
        " --scatter-count {n_out_files}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {prefix.parent}"
        " --interval-file-prefix {prefix.name:q}"
        " --interval-file-num-digits {len_chunk_labels}"
        " --extension {suffix:q}"
        " {log}"
    )
