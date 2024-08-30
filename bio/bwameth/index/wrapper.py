# coding: utf-8

"""Snakemake wrapper for BWA-Meth index"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

import os
import os.path

from tempfile import TemporaryDirectory
from snakemake import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

# Automatic detection of aligner based on one output file
subcommand = "index"
if any(str(outfile).endswith(".0123"):
       subcommand = "index-mem2"

with TemporaryDirectory() as tempdir:
    # Create symlink to avoid bwa-meth index to be written next to the input reference file
    ref_basename = os.path.basename(snakemake.input[0])
    used_reference = os.path.join(tempdir, ref_basename)
    os.symlink(os.path.abspath(snakemake.input[0]), os.path.join(tempdir, ref_basename))

    # Find user-defined reference directory
    prefix = os.path.commonprefix([os.path.abspath(f) for f in snakemake.output])
    out_dir = os.path.dirname(prefix)

    # Run bwameth index command
    shell("bwameth.py {subcommand} {used_reference} {log}")

    # Return index file to user where they expect them
    os.unlink(used_reference)
    shell("mv -v {used_reference}.bwameth.c2t* {out_dir} {log}")
