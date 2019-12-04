__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from ftplib import FTP
from io import StringIO
from subprocess import run
from os.path import basename

species = snakemake.params.species.lower()
release = snakemake.params.release
fmt = snakemake.params.fmt
build = snakemake.params.build


def parse_checksums():
    lines = r.getvalue().strip().split("\n")
    for line in lines:
        fields = line.split()
        yield {
            "cksum": int(fields[0]),
            "blksize": int(fields[1]),
            "filename": fields[2]
        }


suffix = ""
if fmt == "gtf":
    suffix = "gtf.gz"
elif fmt == "gff3":
    suffix = "gff3.gz"

r = StringIO()

with FTP("ftp.ensembl.org") as ftp, open(snakemake.output[0], "wb") as out:
    print("starting download: pub/release-{release}/{fmt}/{species}/{species_cap}.{build}.{release}.{suffix}".format(
        release=release,
        build=build,
        species=species,
        fmt=fmt,
        species_cap=species.capitalize(),
        suffix=suffix,
    ))
    ftp.login()
    ftp.retrbinary(
        "RETR pub/release-{release}/{fmt}/{species}/{species_cap}.{build}.{release}.{suffix}".format(
            release=release,
            build=build,
            species=species,
            fmt=fmt,
            species_cap=species.capitalize(),
            suffix=suffix,
        ),
        out.write,
    )
    ftp.retrlines(
        "RETR pub/release-{release}/{fmt}/{species}/CHECKSUMS".format(
            release=release,
            build=build,
            species=species,
            fmt=fmt,
            species_cap=species.capitalize(),
            suffix=suffix,
        ),
        lambda s, w=r.write: w(s + '\n'),
        # use StringIO instance for callback, add "\n" because ftplib.retrlines omits newlines
    )

for elem in parse_checksums():
    if elem["filename"] == basename(snakemake.output[0]):
        cksum_remote = elem["cksum"]
        cksum_local = int(run(["sum", snakemake.output[0]], capture_output=True).stdout.strip().split()[0])
        print(cksum_remote)
        print(cksum_local)
        if cksum_local == cksum_remote:
            print("CHECKSUM OK: %s" % snakemake.output[0])
            exit(0)
        else:
            print("CHECKSUM FAILED: %s" % snakemake.output[0])
            exit(1)
    else:
        print("No matching file for CHECKSUM test found")
        continue
