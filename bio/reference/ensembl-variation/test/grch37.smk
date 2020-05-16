rule get_variation_with_contig_lengths:
    input:
        fai="refs/grch37.fasta.fai"
    output:
        vcf="refs/variation.vcf.gz"
    params:
        species="homo_sapiens",
        release="100",
        build="GRCh37",
        type="all" # one of "all", "somatic", "structural_variation"
    log:
        "logs/get_variation.log"
    wrapper:
        "master/bio/reference/ensembl-variation"
