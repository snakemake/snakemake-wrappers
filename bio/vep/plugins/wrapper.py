__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import sys
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile
from tempfile import NamedTemporaryFile

if snakemake.log:
    sys.stderr = open(snakemake.log[0], "w")

outdir = Path(snakemake.output[0])
outdir.mkdir()

with NamedTemporaryFile() as tmp:
    urlretrieve(
        "https://github.com/Ensembl/VEP_plugins/archive/release/{release}.zip".format(
            release=snakemake.params.release
        ),
        tmp.name,
    )

    with ZipFile(tmp.name) as f:
        for member in f.infolist():
            memberpath = Path(member.filename)
            if len(memberpath.parts) == 1:
                # skip root dir
                continue
            targetpath = outdir / memberpath.relative_to(memberpath.parts[0])
            if member.is_dir():
                targetpath.mkdir()
            else:
                with open(targetpath, "wb") as out:
                    out.write(f.read(member.filename))
