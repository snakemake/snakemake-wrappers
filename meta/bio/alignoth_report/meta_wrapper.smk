import pandas as pd

checkpoint vembrane_table:
    input:
        "<results>/{sample}.vcf.gz",
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
        reference="resources/genome.fa",
        vcf="<results>/{sample}.vcf.gz",
        csi="<results>/{sample}.vcf.gz.csi",
        overview="<results>/tables/{sample}.tsv"
    output:
        directory("<results>/alignoth/{sample}/{index}/")
    params:
        extra=lambda wc, input: f"--around {get_variant_position(wc, input)}"
    log:
        "<logs>/alignoth/{sample}_{index}.log"
    wrapper:
        "master/bio/alignoth"


rule datavzrd:
    input:
        config=workflow.source_path("resources/template.datavzrd.yaml"),
        overview="<results>/tables/{sample}.tsv",
        plot_tables=lambda wc: get_alignoth_tables(wc, "results")
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
        "master/utils/datavzrd"


def get_alignoth_tables(wildcards, results_dir):
    count = count_variants(wildcards)
    l = [f"{results_dir}/alignoth/{{sample}}/{i}/" for i in range(count)]
    return l


def count_variants(wildcards):
    return sum(1 for _ in open(checkpoints.vembrane_table.get(sample=wildcards.sample).output[0], "r")) - 1


def get_variant_position(wildcards, input):
    df = pd.read_csv(input.overview, sep="\t")
    row = int(wildcards.index)
    chrom = df.iloc[row]["CHROM"]
    pos = df.iloc[row]["POS"]
    print(f"Row {row}: {chrom}:{pos}")
    return f"{chrom}:{pos}"
