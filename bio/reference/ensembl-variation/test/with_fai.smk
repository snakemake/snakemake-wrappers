rule get_variation_with_contig_lengths:
    input:
        fai="refs/genome.fasta.fai"
    output:
        vcf="refs/variation.vcf.gz"
    params:
        species="saccharomyces_cerevisiae",
        release="98",
        type="all" # one of "all", "somatic", "structural_variation"
    log:
        "logs/get_variation.log"
    wrapper:
        "master/bio/reference/ensembl-variation"
