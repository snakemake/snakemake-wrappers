__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
import os.path as path
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
        " {snakemake.wildcards.UUID}"
    )

    for out_path in snakemake.output:
        tmp_path = path.join(tempdir, uuid, path.basename(out_path))
        if not path.exists(tmp_path):
            (root, ext) = os.path.splitext(out_path)
            paths = glob.glob(path.join(tempdir, uuid, ".".join("*", ext)))
            if len(paths) > 1:
                (root, ext2) = os.path.splitext(root)
                paths = glob.glob(path.join(tempdir), uuid, ".".join("*", ext2, ext1))
            if len(paths) == 0:
                ValueError(
                    "{} file extension {} does not match any downloaded file.\n"
                    "Are you sure that UUID {} provides a file of such format?\n".format(
                        out_path, ext1, uuid
                    )
                )
            if len(paths) > 1:
                ValueError(
                    "Found more that one file with extension {}:\n"
                    "{}\n"
                    "Cannot match file {} unambiguously.\n".format(
                        ".".join(ext2, ext1), paths, out_path
                    )
                )
            tmp_path = paths[0]
        shell("mv tmp_path out_path")
