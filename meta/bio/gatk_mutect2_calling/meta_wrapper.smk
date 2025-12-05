rule create_dict:
    input:
        "<genome_sequence>",
    output:
        "<genome_dict>",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "<logs>/picard/create_dict.log",
    params:
        extra="",
    wrapper:
        "v7.6.0/bio/picard/createsequencedictionary"


rule samtools_index:
    input:
        "<genome_sequence>",
    output:
        "<genome_sequence_index>",
    log:
        "<logs>/genome_index.log",
    params:
        extra="",  # optional params string
    wrapper:
        "v7.6.0/bio/samtools/faidx"


rule picard_replace_read_groups:
    input:
        "<bam_file>",
    output:
        "<results>/picard/<per>.bam",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "<logs>/picard/replace_rg/<per>.log",
    params:
        # Required for GATK
        extra="--RGLB lib1 --RGPL illumina --RGPU {sample} --RGSM {sample}",
    wrapper:
        "v7.6.0/bio/picard/addorreplacereadgroups"


rule sambamba_index_picard_bam:
    input:
        "<results>/picard/<per>.bam",
    output:
        "<results>/picard/<per>.bam.bai",
    threads: 1
    log:
        "<logs>/sambamba/index/<per>.log",
    params:
        extra="",
    wrapper:
        "v6.1.0/bio/sambamba/index"


rule mutect2_call:
    input:
        fasta="<genome_sequence>",
        fasta_dict="<genome_dict>",
        fasta_fai="<genome_sequence_index>",
        map="<results>/picard/<per>.bam",
        map_idx="<results>/picard/<per>.bam.bai",
        intervals="<bed_intervals>",
    output:
        vcf="<results>/variant/<per>.vcf",
        bam="<results>/variant/<per>.bam",
        f1r2="<results>/counts/<per>.f1r2.tar.gz",
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra=" --tumor-sample {sample} ",
    log:
        "<logs>/mutect/<per>.log",
    wrapper:
        "v7.6.0/bio/gatk/mutect"


rule gatk_get_pileup_summaries:
    input:
        bam="<results>/picard/<per>.bam",
        bai="<results>/picard/<per>.bam.bai",
        variants="<known_variants>",
        variants_tbi="<known_variants_tbi>",
        intervals="<bed_intervals>",
    output:
        temp("<results>/summaries/<per>.table"),
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra="",
    log:
        "<logs>/summary/<per>.log",
    wrapper:
        "v7.6.0/bio/gatk/getpileupsummaries"


rule gatk_calculate_contamination:
    input:
        tumor="<results>/summaries/<per>.table",
    output:
        temp("<results>/contamination/<per>.pileups.table"),
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "<logs>/contamination/<per>.log",
    params:
        extra="",
    wrapper:
        "v7.6.0/bio/gatk/calculatecontamination"


rule gatk_learn_read_orientation_model:
    input:
        f1r2="<results>/counts/<per>.f1r2.tar.gz",
    output:
        temp("<results>/artifacts_prior/<per>.tar.gz"),
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra="",
    log:
        "<logs>/learnreadorientationbias/<per>.log",
    wrapper:
        "v7.6.0/bio/gatk/learnreadorientationmodel"


rule filter_mutect_calls:
    input:
        vcf="<results>/variant/<per>.vcf",
        ref="<genome_sequence>",
        ref_dict="<genome_dict>",
        ref_fai="<genome_sequence_index>",
        bam="<results>/picard/<per>.bam",
        bam_bai="<results>/picard/<per>.bam.bai",
        contamination="<results>/contamination/<per>.pileups.table",
        f1r2="<results>/artifacts_prior/<per>.tar.gz",
    output:
        vcf="<results>/variant/<per>.filtered.vcf.gz",
        vcf_idx="<results>/variant/<per>.filtered.vcf.gz.tbi",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "<logs>/gatk/filter/<per>.log",
    params:
        extra="--create-output-variant-index --min-median-mapping-quality 35 --max-alt-allele-count 3",
        java_opts="",
    wrapper:
        "v7.6.0/bio/gatk/filtermutectcalls"
