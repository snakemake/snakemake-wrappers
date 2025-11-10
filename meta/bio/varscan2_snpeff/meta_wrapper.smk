rule get_genome_fasta:
    output:
        "genome.fasta",
    log:
        "logs/get_genome_fasta.log",
    params:
        species="saccharomyces_cerevisiae",
        datatype="dna",
        build="R64-1-1",
        release="105",
    threads: 1
    wrapper:
        "v5.10.0/bio/reference/ensembl-sequence"


rule samtools_mpileup:
    input:
        bam=expand(
            "{sample}.sorted.bam",
            sample=("a", "b"),
        ),
        ref="genome.fasta",
    output:
        "samtools/mpileup.gz",
    log:
        "logs/samtools_mpileup.log",
    params:
        extra="--count-orphans",
    threads: 1
    wrapper:
        "v7.3.0/bio/samtools/mpileup"


rule varscan2_somatic:
    input:
        mpileup="samtools/mpileup.gz",
    output:
        snp="varscan2/snp.vcf",
        indel="varscan2/indel.vcf",
    log:
        "logs/varscan2_somatic.log",
    params:
        extra="--strand-filter 1",
    threads: 1
    wrapper:
        "v7.0.0/bio/varscan/somatic"


rule snpeff_download:
    output:
        directory("resources/snpeff/{ref}"),
    log:
        "logs/snpeff_download.{ref}.log",
    params:
        reference=lambda w: w.ref,
    threads: 1
    wrapper:
        "v7.0.0/bio/snpeff/download"


rule snpeff_annotate:
    input:
        calls="varscan2/snp.vcf",
        db="resources/snpeff/R64-1-1.105",
    output:
        calls="snpeff/annotated.vcf",
        stats="snpeff/annotated.html",
        csvstats="snpeff/annotated.csv",
    log:
        "logs/snpeff_annotate.log",
    params:
        extra="-nodownload -noLog",
    threads: 1
    wrapper:
        "v7.0.0/bio/snpeff/annotate"
