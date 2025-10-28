rule salmon_decoy_sequences:
    input:
        transcriptome="resources/transcriptome.fasta",
        genome="resources/genome.fasta",
    output:
        gentrome=temp("resources/gentrome.fasta"),
        decoys=temp("resources/decoys.txt"),
    threads: 1
    log:
        "decoys.log",
    wrapper:
        "master/bio/salmon/decoys"


rule salmon_index_gentrome:
    input:
        sequences="resources/gentrome.fasta",
        decoys="resources/decoys.txt",
    output:
        multiext(
            "salmon/transcriptome_index/",
            "complete_ref_lens.bin",
            "ctable.bin",
            "ctg_offsets.bin",
            "duplicate_clusters.tsv",
            "info.json",
            "mphf.bin",
            "pos.bin",
            "pre_indexing.log",
            "rank.bin",
            "refAccumLengths.bin",
            "ref_indexing.log",
            "reflengths.bin",
            "refseq.bin",
            "seq.bin",
            "versionInfo.json",
        ),
    cache: True
    log:
        "logs/salmon/transcriptome_index.log",
    threads: 2
    params:
        # optional parameters
        extra="",
    wrapper:
        "master/bio/salmon/index"


rule salmon_quant_reads:
    input:
        r="reads/{sample}.fastq.gz",
        index=multiext(
            "salmon/transcriptome_index/",
            "complete_ref_lens.bin",
            "ctable.bin",
            "ctg_offsets.bin",
            "duplicate_clusters.tsv",
            "info.json",
            "mphf.bin",
            "pos.bin",
            "pre_indexing.log",
            "rank.bin",
            "refAccumLengths.bin",
            "ref_indexing.log",
            "reflengths.bin",
            "refseq.bin",
            "seq.bin",
            "versionInfo.json",
        ),
        gtf="resources/annotation.gtf",
    output:
        quant=temp("pseudo_mapping/{sample}/quant.sf"),
        quant_gene=temp("pseudo_mapping/{sample}/quant.genes.sf"),
        lib=temp("pseudo_mapping/{sample}/lib_format_counts.json"),
        aux_info=temp(directory("pseudo_mapping/{sample}/aux_info")),
        cmd_info=temp("pseudo_mapping/{sample}/cmd_info.json"),
        libparams=temp(directory("pseudo_mapping/{sample}/libParams")),
        logs=temp(directory("pseudo_mapping/{sample}/logs")),
    log:
        "logs/salmon/{sample}.log",
    params:
        # optional parameters
        libtype="A",
        extra="--numBootstraps 32",
    threads: 2
    wrapper:
        "master/bio/salmon/quant"


rule tximport:
    input:
        quant=expand(
            "pseudo_mapping/{sample}/quant.sf", sample=["S1", "S2", "S3", "S4"]
        ),
        lib=expand(
            "pseudo_mapping/{sample}/lib_format_counts.json",
            sample=["S1", "S2", "S3", "S4"],
        ),
        aux_info=expand(
            "pseudo_mapping/{sample}/aux_info", sample=["S1", "S2", "S3", "S4"]
        ),
        cmd_info=expand(
            "pseudo_mapping/{sample}/cmd_info.json", sample=["S1", "S2", "S3", "S4"]
        ),
        libparams=expand(
            "pseudo_mapping/{sample}/libParams", sample=["S1", "S2", "S3", "S4"]
        ),
        logs=expand("pseudo_mapping/{sample}/logs", sample=["S1", "S2", "S3", "S4"]),
        tx_to_gene="resources/tx2gene.tsv",
    output:
        txi="tximport/SummarizedExperimentObject.RDS",
    params:
        extra="type='salmon'",
    log:
        "logs/tximport.log"
    wrapper:
        "master/bio/tximport"
