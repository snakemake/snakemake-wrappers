__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"
__contributor__= "Johannes Köster, Fritjof Lammers"

import sys
sys.stderr = open(snakemake.log[0], "w")

from ftplib import FTP
from io import StringIO
from subprocess import run
from os.path import basename
import csv

species = snakemake.params.species.lower()
release = snakemake.params.release
fmt = snakemake.params.fmt
build = snakemake.params.build


def verify_checksum(reader):
    for fields in csv.reader(reader, sep="\t"):
        cksum = int(fields[0])
        filename = fields[2]
        if filename == basename(snakemake.output[0]):
            cksum_local = int(run(["sum", snakemake.output[0]], capture_output=True).stdout.strip().split()[0])
            if cksum_local == cksum:
                print("CHECKSUM OK: %s" % snakemake.output[0])
                exit(0)
            else:
                print("CHECKSUM FAILED: %s" % snakemake.output[0])
                exit(1)
        else:
            print("No matching file for CHECKSUM test found", file=sys.stderr)
            continue

suffix = ""
if fmt == "gtf":
    suffix = "gtf.gz"
elif fmt == "gff3":
    suffix = "gff3.gz"

with FTP("ftp.ensembl.org") as ftp, open(snakemake.output[0], "wb") as out:
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
    
    checksum_reader = StringIO()
    ftp.retrlines(
        "RETR pub/release-{release}/{fmt}/{species}/CHECKSUMS".format(
            release=release,
            build=build,
            species=species,
            fmt=fmt,
            species_cap=species.capitalize(),
        ),
        lambda s, w=checksum_reader.write: w(s + '\n'),
        # use StringIO instance for callback, add "\n" because ftplib.retrlines omits newlines
    )

    verify_checksum(checksum_reader)
