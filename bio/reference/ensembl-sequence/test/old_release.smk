rule get_genome:
    output:
        "refs/genome.fasta"
    params:
        species="saccharomyces_cerevisiae",
        datatype="dna",
        build="R64-1-1",
        release="75"
    log:
        "logs/get_genome.log"
    wrapper:
        "master/bio/reference/ensembl-sequence"

rule get_chromosome:
    output:
        "refs/old_release.chr1.fasta"
    params:
        species="saccharomyces_cerevisiae",
        datatype="dna",
        build="R64-1-1",
        release="101",
        chromosome="I"
    log:
        "logs/get_genome.log"
    wrapper:
        "master/bio/reference/ensembl-sequence"