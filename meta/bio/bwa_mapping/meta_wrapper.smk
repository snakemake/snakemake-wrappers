rule bwa_index:
    input:
        "<genome_sequence>",
    output:
        idx=multiext("<resources>/bwa_index/genome", ".amb", ".ann", ".bwt", ".pac", ".sa"),
    log:
        "<logs>/bwa_index.log",
    wrapper:
        "v5.10.0/bio/bwa/index"


rule bwa_mem:
    input:
        reads=["<reads_r1>", "<reads_r2>"],
        idx=multiext("<resources>/bwa_index/genome", ".amb", ".ann", ".bwt", ".pac", ".sa"),
    output:
        "<results>/mapped/{sample}.bam"
    log:
        "<logs>/bwa_mem/{sample}.log"
    params:
        extra=r"-R '@RG\tID:{sample}\tSM:{sample}'",
        sort="samtools",          # Can be 'none', 'samtools' or 'picard'.
        sort_order="coordinate",  # Can be 'queryname' or 'coordinate'.
        sort_extra=""             # Extra args for samtools/picard.
    threads: 8
    wrapper:
        "v7.6.0/bio/bwa/mem"


rule samtools_index:
    input:
        "<results>/mapped/{sample}.bam"
    output:
        "<results>/mapped/{sample}.bam.bai"
    log:
        "<logs>/samtools_index/{sample}.log"
    params:
        "" # optional params string
    wrapper:
        "v7.3.0/bio/samtools/index"
