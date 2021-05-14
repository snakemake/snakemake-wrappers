__author__ = "Felix Mölder"
__copyright__ = "Copyright 2021, Felix Mölder"
__email__ = "felix.moelder@uni-due.de"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

tmp_dir = tempfile.mkdtemp()
sample_name = "-s {params.sample_report}" if params.get("sample_report", None) else ""
extra = snakemake.params.get("extra", "")
result_dir = snakemake.output[0].rsplit("/", 2)[0]
shell("cp -r {result_dir} {tmp_dir}")

shell("debarcer plot -d {tmp_dir} {sample_name} {extra}")

shell("mv {os.path.join(tmp_dir, 'Figures/')} {os.path.join(result_dir, 'Figures/')}")
shell("mv {tmp_dir}/Report/debarcer_report.html {snakemake.output[0]}")