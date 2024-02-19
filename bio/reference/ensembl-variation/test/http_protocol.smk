rule get_variation_http_protocol:
    output:
        vcf="refs/variation.vcf.gz",
    params:
        species="saccharomyces_cerevisiae",
        release="98",
        build="R64-1-1",
        type="all",
        protocol="http"
    log:
        "logs/get_variation.log",
    wrapper:
        "master/bio/reference/ensembl-variation"
