__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from pathlib import Path

from pygadm import Items

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Request data
request = {}
for param in ["name", "admin", "content_level"]:
    value = snakemake.params.get(param, None)
    if value:
        request[param] = value
geo_dataframe = Items(**request)

# GADM uses a WGS84 datum.
geo_dataframe = geo_dataframe.set_crs(4326)

# GeoPandas specifies separate methods for saving files.
# Attempt to grab it using the file extension.
path = snakemake.output.path
save_method = f"to_{Path(path).suffix[1:]}"
if save_method in dir(geo_dataframe):
    getattr(geo_dataframe, save_method)(path)
else:
    geo_dataframe.to_file(path)