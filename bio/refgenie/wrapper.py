__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import refgenconf
from refgenconf.exceptions import RefgenconfError

genome = snakemake.params.genome
asset = snakemake.params.asset
tag = snakemake.params.tag

conf_path = os.environ["REFGENIE"]

# BUG If there are multiple concurrent refgenie commands, this will fail due to
# unable to acquire lock of the config file.
try:
    rgc = refgenconf.RefGenConf(conf_path, writable=True)
except RefgenconfError:
    # Read lock timeouts on the config file can occur when multiple refgenie commands are run concurrently.
    rgc = refgenconf.RefGenConf(
        conf_path, writable=True, skip_read_lock=True, genome_exact=False
    )
# pull asset if necessary
gat, archive_data, server_url = rgc.pull(
    genome, asset, tag, force=False, force_large=snakemake.params.get("force_large", False)
)

for seek_key, out in snakemake.output.items():
    path = rgc.seek(genome, asset, tag_name=tag, seek_key=seek_key, strict_exists=True)
    os.symlink(path, out)
