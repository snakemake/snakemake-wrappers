__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
tmp_root = snakemake.params.get("tmp_root", None)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory(dir=tmp_root) as tmp_dir:
    shell(
        """
        (TMPDIR={tmp_dir}; \
        pbmm2 align --num-threads {snakemake.threads} \
            --preset {snakemake.params.preset} \
            --sample {snakemake.params.sample} \
            --log-level {snakemake.params.loglevel} \
            {extra} \
            {snakemake.input.reference} \
            {snakemake.input.query} \
            {snakemake.output.bam}) {log}
        """
    )
