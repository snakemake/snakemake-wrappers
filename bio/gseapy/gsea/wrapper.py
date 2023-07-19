#coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import gseapy
import pickle
import tempfile

from snakemake.shell import shell

# Building Gene sets object
gmt_path = snakemake.input.get("gmt", [])
gene_sets = snakemake.params.get("gene_sets", [])
if isinstance(gene_sets, str):
    gene_sets = [gene_sets]

if isinstance(gmt_path, list):
    gene_sets += gmt_path
else:
    gene_sets.append(gmt_path)


with tempfile.TemporaryDirectory() as tmpdir:
    outdir = snakemake.params.get("outdir", tmpdir)

    # Running gseapy
    extra = snakemake.params.get("extra", {})
    result = None
    if snakemake.input.get("rank"):
        result = gseapy.prerank(
            rnk=snakemake.input.rank,
            gene_sets=gene_sets,
            outdir=outdir,
            **extra
        )
    elif snakemake.input.get("expr"):
        if snakemake.input.get("cls"):
            result = gseapy.gsea(
                data=snakemake.input.expr,
                gene_sets=gene_sets,
                cls=snakemake.input.cls,
                outdir=outdir,
            **extra
            )
        else:
            result = gseapy.ssgsea(
                data=snakemake.input.expr,
                gene_sets=gene_sets,
                outdir=outdir,
            **extra
            )
    elif snakemake.input.get("gene_list"):
        result = gseapy.enrichr(
            gene_list=snakemake.input.gene_list,
            gene_sets=gene_sets,
            outdir=outdir,
            **extra
        )
    else:
        raise ValueError(
            "Could not decide between GSEApy functions"
        )
    
    shell(f"tree {outdir}")

# if snakemake.output.get("pkl"):
#     with open(snakemake.output.pkl, "wb") as gseapy_stream:
#         pickle.dump(obj=result, file=gseapy_stream, protocol=pickle.HIGHEST_PROTOCOL)