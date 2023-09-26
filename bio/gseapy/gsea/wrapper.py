# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import gseapy
import logging


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
print(extra)
print(gene_sets)

# Running gseapy
result = None
if snakemake.input.get("rank"):
    print("Using Pre-rank method")
    result = gseapy.prerank(
        rnk=snakemake.input.rank,
        gene_sets=gene_sets,
        outdir=str(snakemake.output),
        threads=snakemake.threads,
        **extra
    )
elif snakemake.input.get("expr"):
    if snakemake.input.get("cls"):
        print("Using GSEA method")
        result = gseapy.gsea(
            data=snakemake.input.expr,
            gene_sets=gene_sets,
            cls=snakemake.input.cls,
            threads=snakemake.threads,
            outdir=str(snakemake.output),
            **extra
        )
    else:
        if snakemake.threads > 1:
            raise TooManyThreadsRequested()

        print("Using Single-Sample GSEA method")
        result = gseapy.ssgsea(
            data=snakemake.input.expr,
            gene_sets=gene_sets,
            outdir=str(snakemake.output),
            **extra
        )
elif snakemake.input.get("gene_list"):
    if snakemake.threads > 1:
        raise TooManyThreadsRequested()

    print("Using Biomart EnrichR method")
    result = gseapy.enrichr(
        gene_list=snakemake.input.gene_list,
        gene_sets=gene_sets,
        outdir=str(snakemake.output),
        **extra
    )
else:
    raise ValueError("Could not decide between GSEApy functions")
