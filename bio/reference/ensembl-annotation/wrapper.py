from ftplib import FTP

species = snakemake.params.species.lower()
release = snakemake.params.release
fmt = snakemake.params.fmt
build = snakemake.params.build

suffix = ""
if fmt == "gtf":
    suffix = "gtf.gz"
elif fmt == "gff3":
    suffix = "gff3.gz"


with FTP("ftp.ensembl.org") as ftp, open(snakemake.output[0], "wb") as out:
    ftp.login()
    ftp.retrbinary(
        "STOR pub/release-{release}/{fmt}/{species}/{species.capitalize()}.{build}.{release}.{suffix}".format(
            release=release,
            build=build
            species=species,
            fmt=fmt
        ),
        out.write,
    )
