def get_alignoth_tables(wildcards, results_dir):
    count = count_variants(wildcards)
    return [f"{results_dir}/alignoth/{{sample}}/{i}/" for i in range(count)]


def count_variants(wildcards):
    return sum(1 for _ in open(checkpoints.vembrane_table.get(sample=wildcards.sample).output[0], "r")) - 1


checkpoint vembrane_table:
    input:
        "<results>/{sample}.bcf",
    output:
        "<results>/tables/{sample}.tsv"
    log:
        "<logs>/vembrane_table/{sample}.log"
    params:
        expression="INDEX, CHROM, POS, REF, ALT",
        extra=""
    wrapper:
        "v7.6.1/bio/vembrane/table"


rule alignoth:
    input:
        bam="<results>/mapped/{sample}.bam",
        bam_idx="<results>/mapped/{sample}.bam.bai",
        reference="resources/genome.fa",
        reference_idx="resources/genome.fa.fai",
        vcf="<results>/{sample}.bcf",
        vcf_idx="<results>/{sample}.bcf.csi",
        overview="<results>/tables/{sample}.tsv"
    output:
        directory("<results>/alignoth/{sample}/{index}/")
    params:
        extra=lambda wc, input: f"--around-vcf-record {wc.index} -f tsv"
    log:
        "<logs>/alignoth/{sample}_{index}.log"
    wrapper:
        "v8.0.1/bio/alignoth"


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
        "v7.9.1/utils/datavzrd"
