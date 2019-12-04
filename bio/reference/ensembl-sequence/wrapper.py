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
build = snakemake.params.build

suffixes = ""
datatype = snakemake.params.get("datatype", "")


def checksum():
    lines = r.getvalue().strip().split("\n")
    for line in lines:
        fields = line.strip().split()
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
            # print("No matching file for CHECKSUM test found")
            continue


if datatype == "dna":
    suffixes = ["dna.primary_assembly.fa.gz", "dna.toplevel.fa.gz"]
elif datatype == "cdna":
    suffixes = ["cdna.all.fa.gz"]
elif datatype == "cds":
    suffixes = ["cds.all.fa.gz"]
elif datatype == "ncrna":
    suffixes = ["ncrna.fa.gz"]
elif datatype == "pep":
    suffixes = ["pep.all.fa.gz"]
else:
    raise ValueError("invalid datatype, must be one of dna, cdna, cds, ncrna, pep")

success = False
with FTP("ftp.ensembl.org") as ftp, open(snakemake.output[0], "wb") as out:
    ftp.login()
    for suffix in suffixes:
        url = "pub/release-{release}/fasta/{species}/{datatype}/{species_cap}.{build}.{suffix}".format(
            release=release,
            species=species,
            datatype=datatype,
            build=build,
            suffix=suffix,
            species_cap=species.capitalize(),
        )
        try:
            ftp.size(url)
        except:
            continue

        ftp.retrbinary("RETR " + url, out.write)
        success = True
        # retrieve CHECKSUMS file
        r = StringIO()
        ftp.retrlines(
            "RETR pub/release-{release}/fasta/{species}/{datatype}/CHECKSUMS".format(
                release=release,
                species=species,
                datatype=datatype
            ),
            lambda s, w=r.write: w(s + '\n'),
        )
        # use StringIO instance for callback, add "\n" because ftplib.retrlines omits newlines

    checksum()

if not success:
    raise ValueError(
        "Requested sequence does not seem to exist on ensembl FTP servers (url {})".format(
            url
        )
    )
