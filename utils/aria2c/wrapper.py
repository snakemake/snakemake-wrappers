__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

for hash_function, digest in snakemake.params.items():
    if hash_function in [
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "md5",
        "adler32",
    ]:
        if hash_function.startswith("sha"):
            hash_function = hash_function.replace("sha", "sha-")
        extra += f" --checksum {hash_function}={digest}"
        break

shell(
    "aria2c"
    " --max-concurrent-downloads {snakemake.threads}"
    " {extra}"
    " --log {snakemake.log}"
    " --out {snakemake.output[0]}"
    " {snakemake.params.url}"
    " > /dev/null"
)
