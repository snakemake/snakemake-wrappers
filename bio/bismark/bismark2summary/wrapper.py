"""Snakemake wrapper to generate summary graphical HTML report from several Bismark text report files."""

# https://github.com/FelixKrueger/Bismark/blob/master/bismark2summary

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
cmds = ["bismark2summary {extra}"]

# basename
bam = snakemake.input.get("bam", None)
if not bam:
    raise ValueError(
        "bismark/bismark2summary: Please specify aligned BAM file path"
        " (one or several) using 'bam=..'"
    )

html = snakemake.output.get("html", None)
txt = snakemake.output.get("txt", None)
if not html or not txt:
    raise ValueError(
        "bismark/bismark2summary: Please specify both 'html=..' and"
        " 'txt=..' paths in output section"
    )

basename, ext = os.path.splitext(html)
if ext.lower() != ".html":
    raise ValueError(
        "bismark/bismark2summary: HTML report file should end"
        " with suffix '.html' but was {} ({})".format(ext, html)
    )

suggested_txt = basename + ".txt"
if suggested_txt != txt:
    raise ValueError(
        "bismark/bismark2summary: Expected '{}' TXT report, "
        "but was: '{}'".format(suggested_txt, txt)
    )

cmds.append("--basename {basename:q}")

# title
title = snakemake.params.get("title", None)
if title:
    cmds.append("--title {title:q}")

cmds.append("{bam}")

# log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmds.append("{log}")

# run shell command:
shell(" ".join(cmds))
