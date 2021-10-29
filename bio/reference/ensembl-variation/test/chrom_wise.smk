rule get_variation:
    output:
        vcf="refs/variation.vcf.gz"
    params:
        species="homo_sapiens",
        release="104",
        build="GRCh38",
        type="all", # one of "all", "somatic", "structural_variation"
        chromosome="21",
    log:
        "logs/get_variation.log"
    wrapper:
        "master/bio/reference/ensembl-variation"
