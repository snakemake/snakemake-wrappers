__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
import os.path as path
from tempfile import TemporaryDirectory
import glob

uuid = snakemake.params.get("uuid", "")
if uuid == "":
    raise ValueError("You need to provide a GDC UUID via the 'uuid' in 'params'.")

extra = snakemake.params.get("extra", "")
token = snakemake.params.get("gdc_token", "")
if token != "":
    token = "--token-file {}".format(token)

with TemporaryDirectory() as tempdir:
    shell(
        "gdc-client download"
        " {token}"
        " {extra}"
        " -n {snakemake.threads} "
        " --log-file {snakemake.log} "
        " --dir {tempdir}"
        " {uuid}"
    )

    for out_path in snakemake.output:
        tmp_path = path.join(tempdir, uuid, path.basename(out_path))
        if not path.exists(tmp_path):
            (root, ext1) = path.splitext(out_path)
            paths = glob.glob(path.join(tempdir, uuid, "*" + ext1))
            if len(paths) > 1:
                (root, ext2) = path.splitext(root)
                paths = glob.glob(path.join(tempdir, uuid, "*" + ext2 + ext1))
            if len(paths) == 0:
                raise ValueError(
                    "{} file extension {} does not match any downloaded file.\n"
                    "Are you sure that UUID {} provides a file of such format?\n".format(
                        out_path, ext1, uuid
                    )
                )
            if len(paths) > 1:
                raise ValueError(
                    "Found more than one downloaded file with extension '{}':\n"
                    "{}\n"
                    "Cannot match requested output file {} unambiguously.\n".format(
                        ext2 + ext1, paths, out_path
                    )
                )
            tmp_path = paths[0]
        shell("mv {tmp_path} {out_path}")
