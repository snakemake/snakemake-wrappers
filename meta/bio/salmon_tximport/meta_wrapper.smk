rule salmon_decoy_sequences:
    input:
        transcriptome="<transcriptome_sequence>",
        genome="<genome_sequence>",
    output:
        gentrome=temp("<resources>/gentrome.fasta"),
        decoys=temp("<resources>/decoys.txt"),
    threads: 1
    log:
        "<logs>/decoys.log",
    wrapper:
        "v6.0.0/bio/salmon/decoys"


rule salmon_index_gentrome:
    input:
        sequences="<resources>/gentrome.fasta",
        decoys="<resources>/decoys.txt",
    output:
        multiext(
            "<resources>/salmon_gentrome_index/",
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
        "<logs>/salmon/gentrome_index.log",
    threads: 2
    params:
        # optional parameters
        extra="",
    wrapper:
        "v3.5.3/bio/salmon/index"


rule salmon_quant_reads:
    input:
        r1="<reads_r1>",
        r2="<reads_r2>",
        index=multiext(
            "<resources>/salmon_gentrome_index/",
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
        gtf="<genome_annotation>",
    output:
        quant=temp("<results>/pseudo_mapping/<per>/quant.sf"),
        quant_gene=temp("<results>/pseudo_mapping/<per>/quant.genes.sf"),
        lib=temp("<results>/pseudo_mapping/<per>/lib_format_counts.json"),
        aux_info=temp(directory("<results>/pseudo_mapping/<per>/aux_info")),
        cmd_info=temp("<results>/pseudo_mapping/<per>/cmd_info.json"),
        libparams=temp(directory("<results>/pseudo_mapping/<per>/libParams")),
        logs=temp(directory("<results>/pseudo_mapping/<per>/logs")),
    log:
        "<logs>/salmon/<per>.log",
    params:
        # optional parameters
        libtype="A",
        extra="--numBootstraps 32",
    threads: 2
    wrapper:
        "v6.0.0/bio/salmon/quant"


rule tximport:
    input:
        quant=expand(
            "<results>/pseudo_mapping/{sample}/quant.sf",
            sample=["S1", "S2"],
        ),
        lib=expand(
            "<results>/pseudo_mapping/{sample}/lib_format_counts.json",
            sample=["S1", "S2"],
        ),
        aux_info=expand(
            "<results>/pseudo_mapping/{sample}/aux_info",
            sample=["S1", "S2"],
        ),
        cmd_info=expand(
            "<results>/pseudo_mapping/{sample}/cmd_info.json",
            sample=["S1", "S2"],
        ),
        libparams=expand(
            "<results>/pseudo_mapping/{sample}/libParams",
            sample=["S1", "S2"],
        ),
        logs=expand(
            "<results>/pseudo_mapping/{sample}/logs",
            sample=["S1", "S2"],
        ),
        tx_to_gene="<tx_to_gene>",
    output:
        txi="<results>/tximport/SummarizedExperimentObject.RDS",
    params:
        extra="type='salmon'",
    log:
        "<logs>/tximport.log",
    wrapper:
        "v6.0.2/bio/tximport"
