rule bowtie2_build:
    input:
        ref="<genome_sequence>",
    output:
        multiext(
            "<resources>/bowtie_index/genome",
            ".1.bt2",
            ".2.bt2",
            ".3.bt2",
            ".4.bt2",
            ".rev.1.bt2",
            ".rev.2.bt2",
        ),
    log:
        "<logs>/bowtie2_build/build.log",
    params:
        extra="",
    threads: 8
    wrapper:
        "v3.11.0/bio/bowtie2/build"


rule bowtie2_alignment:
    input:
        sample=["<reads_r1>", "<reads_r2>"],
        idx=multiext(
            "<resources>/bowtie_index/genome",
            ".1.bt2",
            ".2.bt2",
            ".3.bt2",
            ".4.bt2",
            ".rev.1.bt2",
            ".rev.2.bt2",
        ),
    output:
        temp("<results>/mapped/{sample}.bam"),
    log:
        "<logs>/bowtie2/{sample}.log",
    params:
        extra=(
            " --rg-id {sample} "
            "--rg 'SM:{sample} LB:FakeLib PU:FakePU.1.{sample} PL:ILLUMINA' "
        ),
    threads: 8
    wrapper:
        "v7.6.0/bio/bowtie2/align"


rule sambamba_sort:
    input:
        "<results>/mapped/{sample}.bam",
    output:
        temp("<results>/mapped/{sample}.sorted.bam"),
    params:
        "",
    log:
        "<logs>/sambamba-sort/{sample}.log",
    threads: 8
    wrapper:
        "v3.11.0/bio/sambamba/sort"


rule sambamba_view:
    input:
        "<results>/mapped/{sample}.sorted.bam",
    output:
        temp("<results>/mapped/{sample}.filtered.bam"),
    params:
        extra=(
            " --format 'bam' "
            "--filter 'mapping_quality >= 30 and not (unmapped or mate_is_unmapped)' "
        ),
    log:
        "logs/sambamba-view/{sample}.log",
    threads: 8
    wrapper:
        "v6.1.0/bio/sambamba/view"


rule sambamba_markdup:
    input:
        "<results>/mapped/{sample}.filtered.bam",
    output:
        "<results>/mapped/{sample}.rmdup.bam",
    params:
        extra=" --remove-duplicates ",  # optional parameters
    log:
        "<logs>/sambamba-markdup/{sample}.log",
    threads: 8
    wrapper:
        "v6.1.0/bio/sambamba/markdup"


rule sambamba_index:
    input:
        "<results>/mapped/{sample}.rmdup.bam",
    output:
        "<results>/mapped/{sample}.rmdup.bam.bai",
    params:
        extra="",
    log:
        "<logs>/sambamba-index/{sample}.log",
    threads: 8
    wrapper:
        "v6.1.0/bio/sambamba/index"
