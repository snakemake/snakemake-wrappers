import pandas as pd

checkpoint vembrane_table:
    input:
        "<results>/{sample}.bcf",
    output:
        "<results>/tables/{sample}.tsv"
    log:
        "<logs>/vembrane_table/{sample}.log"
    params:
        expression="INDEX, CHROM, POS, ALT, REF",
        extra=""
    wrapper:
        "v7.6.1/bio/vembrane/table"


rule alignoth:
    input:
        bam="<results>/mapped/{sample}.bam",
        reference="resources/genome.fa",
        vcf="<results>/{sample}.bcf",
        idx="<results>/{sample}.bcf.csi",
        overview="<results>/tables/{sample}.tsv"
    output:
        directory("<results>/alignoth/{sample}/{index}/")
    params:
        extra=lambda wc, input: f"--around-vcf-record {wc.index} -f tsv"
    log:
        "<logs>/alignoth/{sample}_{index}.log"
    wrapper:
        "v7.9.0/bio/alignoth"


rule datavzrd:
    input:
        config=workflow.source_path("resources/template.datavzrd.yaml"),
        overview="<results>/tables/{sample}.tsv",
        plot_tables=lambda wc: get_alignoth_tables(wc, "<results>")
    output:
        report(
            directory("<results>/datavzrd-report/{sample}"),
            htmlindex="index.html",
        ),
        # config = "resources/datavzrd/{sample}.rendered_config.yaml"
    params:
        max_index=lambda wc: count_variants(wc)
    log:
        "<logs>/datavzrd/{sample}.log",
    wrapper:
        "v7.9.0/utils/datavzrd"


def get_alignoth_tables(wildcards, results_dir):
    count = count_variants(wildcards)
    return [f"{results_dir}/alignoth/{{sample}}/{i}/" for i in range(count)]


def count_variants(wildcards):
    return sum(1 for _ in open(checkpoints.vembrane_table.get(sample=wildcards.sample).output[0], "r")) - 1
