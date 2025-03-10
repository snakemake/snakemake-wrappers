__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from pathlib import Path

from pygadm import Items

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

request = {}
for param in ["name", "admin", "content_level"]:
    value = snakemake.params.get(param, None)
    if value:
        request[param] = value

geo_dataframe = Items(**request)

path = Path(snakemake.output.path)

geo_dataframe.to_file(path)


