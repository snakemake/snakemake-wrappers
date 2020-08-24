"""eggNOGmapper annotate hits table."""

__author__ = "Silas Kieser"
__copyright__ = "Copyright 2020, Silas Kieser"
__email__ = "silas.kieser@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


data_base_dir = os.path.dirname(snakemake.input.eggnog_db)

out_extension= '.emapper.annotations'

assert snakemake.output[0].endswith(out_extension), f"expect first outptu file to end with {out_extension}"
output_prefix= snakemake.output[0].replace(out_extension,'')


if hasattr(params,'use_virtual_disk') and params['use_virtual_disk']:


    virtual_disk=snakemake.config.get('virtual_disk','/dev/shm/')
    assert os.path.exists(virtual_disk), "Virtual disk {virtual_disk} doesn't exits"


    shell("cp {snakemake.input.eggnog_db} {virtual_disk}/eggnog.db 2> {log}")

    data_base_dir= virtual_disk


shell(
      " emapper.py --annotate_hits_table"
      " {snakemake.input.seed} "
      " {extra} "
      " -o {output_prefix} "
      " --cpu {snakemake.threads} "
      "--data_dir {data_base_dir} 2> {log}"
      )
