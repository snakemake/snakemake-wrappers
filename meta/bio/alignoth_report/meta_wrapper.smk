import pandas as pd

checkpoint vembrane_table:
    input:
        "<results>/{sample}.vcf",
    output:
        "<results>/tables/{sample}.tsv"
    log:
        "<logs>/vembrane_table/{sample}.log"
    params:
        expression="INDEX, CHROM, POS, ALT, REF",
        extra=""
    wrapper:
        "master/bio/vembrane/table"


rule alignoth:
    input:
        bam="<results>/mapped/{sample}.bam",
        reference="resources/genome.fa"
        vcf="<results>/{sample}.vcf"
    output:
        directory("<results>/alignoth/{sample}/{index}/")
    params:
        extra=lambda wc: f"--around {get_variant_position(wc)}"
    log:
        "<logs>/alignoth/{sample}.log"
    wrapper:
        "master/bio/alignoth"


rule datavzrd:
    input:
        config="resources/{sample}.datavzrd.yaml",
        overview="<results>/tables/{sample}.tsv",
        plot_tables=lambda wc, input: get_alignoth_tables(wc, input),
    output:
        report(
            directory("<results>/datavzrd-report/{sample}"),
            htmlindex="index.html",
        ),
        # config = "resources/datavzrd/{sample}.rendered_config.yaml"
    params:
        max_index=lambda wc, input: count_variants(wc, input)
    log:
        "<logs>/datavzrd/{sample}.log",
    wrapper:
        "master/utils/datavzrd"


def get_alignoth_tables(wildcards, input):
    count = count_variants(wildcards, input)
    return [f"<results>/alignoth/{{sample}}/{i}/" for i in range(count)]


def count_variants(wildcards, input):
    return sum(1 for _ in open(input.overview, "r"))


def get_variant_position(wildcards):
    df = pd.read_csv(input.overview, sep="\t")
    index = wildcards.index
    return f"{df['CHROM'][index]}:{df['POS'][index]}"
