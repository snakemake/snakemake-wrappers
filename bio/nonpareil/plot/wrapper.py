__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.NamedTemporaryFile() as tmp:

    for output in snakemake.output:
        ext = Path(output).suffix.lstrip(".")
        if ext in ["json", "tsv", "pdf"]:
            if ext == "json":
                extra += f" --{ext} {tmp.name}"
            else:
                extra += f" --{ext} {output}"

    shell("NonpareilCurves.R {extra} {snakemake.input} {log}")

    # Fix JSON output file
    # https://github.com/lmrodriguezr/nonpareil/issues/70
    json_out = snakemake.output.get("json")
    if json_out:
        import json
        import numpy as np

        with open(tmp.name, "rt") as json_f:
            json_data = json.load(json_f)
            for key, val in json_data.items():
                val["x.adj"] = [np.nan if x == "NaN" else x for x in val["x.adj"]]
        with open(json_out, "wt") as json_f:
            json.dump(json_data, json_f, indent=4)
