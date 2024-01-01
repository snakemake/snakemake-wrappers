# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import glob
import gseapy
import logging
import shutil

from tempfile import TemporaryDirectory


def mouve_output_files(method, tempdir):
    """
    Move the predictable output files individually
    and let the rest be in an additional directory
    """
    log = snakemake.log.get("gseapy")
    if log:
        logging.info(f"Moving gseapy logs to {log}")
        shutil.move(
            # The logging file contains a timestamp
            # there is only one logging file
            glob.glob(f"{tempdir}/gseapy.{method}.*.log")[0],
            log,
        )

    if method != "enrichr":
        # `enrichr` method does not produce gmt files
        gmt = snakemake.output.get("gmt")
        if gmt:
            logging.info(f"Moving gseapy GMT to {gmt}")
            shutil.move(f"{tempdir}/gene_sets.gmt", gmt)

        # `enrichr` method does not produce any csv
        csv = snakemake.output.get("csv")
        if csv:
            logging.info(f"Moving gseapy CSV to {csv}")
            if method == "gsea":
                shutil.move(f"{tempdir}/gseapy.phenotype.{method}.report.csv", csv)
            else:
                shutil.move(f"{tempdir}/gseapy.gene_set.{method}.report.csv", csv)

        # Only produced with pre-ranking method.
        # File names depend on gseapy results and are not predictable
        prerank_dir = snakemake.output.get("prerank")
        if method == "prerank" and prerank_dir:
            logging.info(f"Moving gseapy pre-rank results to {prerank_dir}")
            shutil.move(f"{tempdir}/{method}/", prerank_dir)

    # Only produced with enrichr method.
    # File names depend on gseapy results and are not predictable
    else:
        # Since logging file has already been moved, only
        # PDF/TXT results remains
        enrichr_dir = snakemake.output.get("enrichr_dir")
        if enrichr_dir:
            logging.info(f"Moving gseapy-biomart enrichr to {enrichr_dir}")
            shutil.move(f"{tempdir}/", enrichr_dir)


class TooManyThreadsRequested(Exception):
    def __init__(self):
        super().__init__("This subcommand uses only one threads.")


# Building Gene sets object
gmt_path = snakemake.input.get("gmt", [])
gene_sets = snakemake.params.get("gene_sets", [])
if isinstance(gene_sets, str):
    gene_sets = [gene_sets]

if isinstance(gmt_path, list):
    gene_sets += gmt_path
else:
    gene_sets.append(gmt_path)

extra = snakemake.params.get("extra", {})

# Running gseapy
result = None

with TemporaryDirectory() as tempdir:
    if snakemake.input.get("rank"):
        print("Using Pre-rank method")
        result = gseapy.prerank(
            rnk=snakemake.input.rank,
            gene_sets=gene_sets,
            outdir=tempdir,
            threads=snakemake.threads,
            **extra,
        )
        mouve_output_files(method="prerank", tempdir=tempdir)

    elif snakemake.input.get("expr"):
        if snakemake.input.get("cls"):
            print("Using GSEA method")
            result = gseapy.gsea(
                data=snakemake.input.expr,
                gene_sets=gene_sets,
                cls=snakemake.input.cls,
                threads=snakemake.threads,
                outdir=tempdir,
                **extra,
            )
            mouve_output_files(method="gsea", tempdir=tempdir)
        else:
            if snakemake.threads > 1:
                raise TooManyThreadsRequested()

            print("Using Single-Sample GSEA method")
            result = gseapy.ssgsea(
                data=snakemake.input.expr, gene_sets=gene_sets, outdir=tempdir, **extra
            )
            mouve_output_files(method="ssgsea", tempdir=tempdir)
    elif snakemake.input.get("gene_list"):
        if snakemake.threads > 1:
            raise TooManyThreadsRequested()

        print("Using Biomart EnrichR method")
        result = gseapy.enrichr(
            gene_list=snakemake.input.gene_list,
            gene_sets=gene_sets,
            outdir=tempdir,
            **extra,
        )
        mouve_output_files(method="enrichr", tempdir=tempdir)
    else:
        raise ValueError("Could not decide between GSEApy functions")
