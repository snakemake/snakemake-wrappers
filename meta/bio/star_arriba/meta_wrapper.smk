rule star_index:
    input:
        fasta="<genome_sequence>",
        gtf="<genome_annotation>",
    output:
        directory("<resources>/star_genome"),
    threads: 4
    params:
        sjdbOverhang=100,
        extra="--genomeSAindexNbases 2",
    log:
        "<logs>/star_index_genome.log",
    cache: True  # mark as eligible for between workflow caching
    wrapper:
        "v3.3.7/bio/star/index"


rule star_align:
    input:
        # use a list for multiple fastq files for one sample
        # usually technical replicates across lanes/flowcells
        fq1="<reads_r1>",
        fq2="<reads_r2>",  #optional
        idx="<resources>/star_genome",
        annotation="<genome_annotation>",
    output:
        # see STAR manual for additional output files
        aln="<results>/star/<per>/Aligned.out.bam",
        reads_per_gene="<results>/star/<per>/ReadsPerGene.out.tab",
    log:
        "<logs>/star/<per>.log",
    params:
        # specific parameters to work well with arriba
        extra=lambda wc, input: (
            f"--quantMode GeneCounts --sjdbGTFfile {input.annotation}"
            " --outSAMtype BAM Unsorted --chimSegmentMin 10 --chimOutType WithinBAM SoftClip"
            " --chimJunctionOverhangMin 10 --chimScoreMin 1 --chimScoreDropMax 30 --chimScoreJunctionNonGTAG 0"
            " --chimScoreSeparation 1 --alignSJstitchMismatchNmax 5 -1 5 5 --chimSegmentReadGapMax 3"
        ),
    threads: 12
    wrapper:
        "v3.3.7/bio/star/align"


rule arriba:
    input:
        bam=rules.star_align.output.aln,
        genome="<genome_sequence>",
        annotation="<genome_annotation>",
        # optional: # A custom tsv containing identified artifacts, such as read-through fusions of neighbouring genes.
        # default blacklists are selected via blacklist parameter
        # see https://arriba.readthedocs.io/en/latest/input-files/#blacklist
        custom_blacklist=[],
    output:
        fusions="<results>/arriba/<per>.fusions.tsv",
        discarded="<results>/arriba/<per>.fusions.discarded.tsv",
    params:
        # required if blacklist or known_fusions is set
        genome_build="GRCh38",
        default_blacklist=False,
        default_known_fusions=True,
        extra="",
    log:
        "<logs>/arriba/<per>.log",
    threads: 1
    wrapper:
        "v7.3.0/bio/arriba"
