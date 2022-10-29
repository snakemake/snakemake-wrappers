rule bwa_meme_test:
    input:
        "mapped/a.cram",
        "mapped/a.picard.cram",


rule L2_PARAMETERS_extract:
    input:
        "genome.fasta.suffixarray_uint64_L2_PARAMETERS.gz",
    output:
        temp("genome.fasta.suffixarray_uint64_L2_PARAMETERS"),
    conda:
        "gzip.yaml"
    log:
        "log/extract.l2.log",
    shell:
        "zcat {input} > {output} 2> {log}"


rule bwa_meme_mem_picard:
    input:
        reads=["reads/{sample}.1.fastq", "reads/{sample}.2.fastq"],
        reference="genome.fasta",
        idx=multiext(
            "genome.fasta",
            ".0123",
            ".amb",
            ".ann",
            ".pac",
            ".pos_packed",
            ".suffixarray_uint64",
            ".suffixarray_uint64_L0_PARAMETERS",
            ".suffixarray_uint64_L1_PARAMETERS",
            ".suffixarray_uint64_L2_PARAMETERS",
        ),
    output:
        "mapped/{sample}.picard.cram",
    log:
        "logs/bwa_meme/{sample}.log",
    params:
        extra=r"-R '@RG\tID:{sample}\tSM:{sample}' -M",
        sort="picard",
        sort_order="coordinate",
        sort_extra="",
        dedup="mark",
        dedup_extra="-M",
        exceed_thread_limit=True,
        embed_ref=True,
    threads: 8
    wrapper:
        "master/bio/bwa-meme/mem"
