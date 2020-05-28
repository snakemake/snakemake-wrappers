__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# extract arguments
params = ""
extra_limits = ""
tags = snakemake.params.get("tags")
min_size = snakemake.params.get("min_size")
max_size = snakemake.params.get("max_size")
min_length = snakemake.params.get("min_length")
max_length = snakemake.params.get("max_length")
additional_params = snakemake.params.get("additional_params")

if tags and tags is not None:
    params = params + " " + " ".join(map('-tag "{}"'.format, tags))

if min_size and min_size is not None:
    params = params + ' -insertSize ">=' + min_size + '"'
    if max_size and max_size is not None:
        extra_limits = extra_limits + ' -insertSize "<=' + max_size + '"'
else:
    if max_size and max_size is not None:
        params = params + ' -insertSize "<=' + max_size + '"'

if min_length and min_length is not None:
    params = params + ' -length ">=' + min_length + '"'
    if max_length and max_length is not None:
        extra_limits = extra_limits + ' -length "<=' + max_length + '"'
else:
    if max_length and max_length is not None:
        params = params + ' -length "<=' + max_length + '"'

if additional_params and additional_params is not None:
    params = params + " " + additional_params

if extra_limits:
    params = params + " | bamtools filter" + extra_limits

shell(
    "(bamtools filter"
    " -in {snakemake.input[0]}" + params + " -out {snakemake.output[0]}) {log}"
)
