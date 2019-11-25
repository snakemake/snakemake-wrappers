from ftplib import FTP

species = snakemake.params.species.lower()
release = snakemake.params.release
build = snakemake.params.build

suffixes = ""
datatype = snakemake.params.get("datatype", "")
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
            release=release, species=species, datatype=datatype, build=build, suffix=suffix, species_cap=species.capitalize()
        )
        try:
            ftp.size(url)
        except:
            continue
        
        ftp.retrbinary("RETR " + url, out.write)
        success = True

if not success:
    raise ValueError(
        "Requested sequence does not seem to exist on ensembl FTP servers (url {})".format(
            url
        )
    )
