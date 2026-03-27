__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import refgenconf

conf_path = os.environ["REFGENIE"]

rgc = refgenconf.RefGenConf.from_yaml_file(conf_path, writable=True)

# pull asset if necessary
gat, archive_data, server_url = rgc.pull(
    snakemake.params.genome, snakemake.params.asset, snakemake.params.tag, force=False
)

for seek_key, out in snakemake.output.items():
    path = rgc.seek(
        snakemake.params.genome,
        snakemake.params.asset,
        tag_name=snakemake.params.tag,
        seek_key=seek_key,
        strict_exists=True,
    )
    os.symlink(path, out)
