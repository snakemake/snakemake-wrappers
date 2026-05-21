__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
import os.path as path
from tempfile import TemporaryDirectory
import glob

extra = snakemake.params.get("extra", "")
uuid = snakemake.params.uuid
assert str(uuid).strip(), "You need to provide a GDC UUID via the 'uuid' in 'params'."

# Input
token = snakemake.input.get("gdc_token", "")
if token:
    token = f"--token-file {token}"

with TemporaryDirectory() as tempdir:
    shell(
        "gdc-client download"
        " {token}"
        " {extra}"
        " -n {snakemake.threads} "
        " --log-file {snakemake.log} "
        " --dir {tempdir}"
        " {snakemake.params.uuid}"
    )

    for out_path in snakemake.output:
        tmp_path = path.join(tempdir, uuid, path.basename(out_path))
        if not path.exists(tmp_path):
            root, ext1 = path.splitext(out_path)
            paths = glob.glob(path.join(tempdir, uuid, f"*{ext1}"))
            if len(paths) > 1:
                root, ext2 = path.splitext(root)
                paths = glob.glob(path.join(tempdir, uuid, f"*{ext2}{ext1}"))
            assert len(paths) > 0, f"File '{out_path}' extension ({ext1}) does not match any downloaded file. Are you sure that UUID {uuid} provides a file of such format?"
            assert len(paths) == 1, f"Cannot match requested output file {out_path} unambiguously. Found more than one downloaded file with extension '{ext1}{ext2}': {paths}."
            tmp_path = paths[0]
        shell("mv {tmp_path} {out_path}")
