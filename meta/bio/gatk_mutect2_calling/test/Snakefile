rule create_dict:
    input:
        "genome.fasta",
    output:
        "genome.dict",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "logs/picard/create_dict.log",
    params:
        extra="",
    wrapper:
        "master/bio/picard/createsequencedictionary"


rule samtools_index:
    input:
        "genome.fasta",
    output:
        "genome.fasta.fai",
    log:
        "logs/genome_index.log",
    params:
        extra="",  # optional params string
    wrapper:
        "master/bio/samtools/faidx"


rule picard_replace_read_groups:
    input:
        "mapped/{sample}.bam",
    output:
        "picard/{sample}.bam",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "logs/picard/replace_rg/{sample}.log",
    params:
        # Required for GATK
        extra="--RGLB lib1 --RGPL illumina --RGPU {sample} --RGSM {sample}",
    wrapper:
        "master/bio/picard/addorreplacereadgroups"


rule sambamba_index_picard_bam:
    input:
        "picard/{sample}.bam",
    output:
        "picard/{sample}.bam.bai",
    threads: 1
    log:
        "logs/sambamba/index/{sample}.log",
    params:
        extra="",
    wrapper:
        "master/bio/sambamba/index"


rule mutect2_call:
    input:
        fasta="genome.fasta",
        fasta_dict="genome.dict",
        fasta_fai="genome.fasta.fai",
        map="picard/{sample}.bam",
        map_idx="picard/{sample}.bam.bai",
        intervals="regions.bed",
    output:
        vcf="variant/{sample}.vcf",
        bam="variant/{sample}.bam",
        f1r2="counts/{sample}.f1r2.tar.gz",
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra=" --tumor-sample {sample} ",
    log:
        "logs/mutect/{sample}.log",
    wrapper:
        "master/bio/gatk/mutect"


rule gatk_get_pileup_summaries:
    input:
        bam="picard/{sample}.bam",
        bai_bai="picard/{sample}.bam.bai",
        variants="known.vcf.gz",
        variants_tbi="known.vcf.gz.tbi",
        intervals="regions.bed",
    output:
        temp("summaries/{sample}.table"),
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra="",
    log:
        "logs/summary/{sample}.log",
    wrapper:
        "master/bio/gatk/getpileupsummaries"


rule gatk_calculate_contamination:
    input:
        tumor="summaries/{sample}.table",
    output:
        temp("contamination/{sample}.pileups.table"),
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "logs/contamination/{sample}.log",
    params:
        extra="",
    wrapper:
        "master/bio/gatk/calculatecontamination"


rule gatk_learn_read_orientation_model:
    input:
        f1r2="counts/{sample}.f1r2.tar.gz",
    output:
        temp("artifacts_prior/{sample}.tar.gz"),
    threads: 1
    resources:
        mem_mb=1024,
    params:
        extra="",
    log:
        "logs/learnreadorientationbias/{sample}.log",
    wrapper:
        "master/bio/gatk/learnreadorientationmodel"


rule filter_mutect_calls:
    input:
        vcf="variant/{sample}.vcf",
        ref="genome.fasta",
        ref_dict="genome.dict",
        ref_fai="genome.fasta.fai",
        bam="picard/{sample}.bam",
        bam_bai="picard/{sample}.bam.bai",
        contamination="contamination/{sample}.pileups.table",
        f1r2="artifacts_prior/{sample}.tar.gz",
    output:
        vcf="variant/{sample}.filtered.vcf.gz",
        vcf_idx="variant/{sample}.filtered.vcf.gz.tbi",
    threads: 1
    resources:
        mem_mb=1024,
    log:
        "logs/gatk/filter/{sample}.log",
    params:
        extra="--create-output-variant-index --min-median-mapping-quality 35 --max-alt-allele-count 3",
        java_opts="",
    wrapper:
        "master/bio/gatk/filtermutectcalls"
