__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

import pandas as pd
from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")


if len(snakemake.input) > 0:
    # Get hash function
    hash_function = snakemake.params.get(
        "hash_function",
        Path(snakemake.input[0].removesuffix(".gz")).suffix.lstrip(".").lower(),
    )
    # Get hash
    df = pd.read_csv(
        snakemake.input[0],
        sep="  ",
        index_col="file_name",
        header=None,
        names=["checksum", "file_name"],
        engine="python",
    )
    hash = df[df.index.str.endswith(Path(snakemake.params.url).name, na=False)][
        "checksum"
    ].item()
    extra += f" --checksum {hash_function}={hash}"


shell(
    "aria2c --max-concurrent-downloads {snakemake.threads} {extra} --log {snakemake.log} --out {snakemake.output[0]} {snakemake.params.url} > /dev/null"
)
