rule get_variation_https_protocol:
    output:
        vcf="refs/variation.vcf.gz",
    params:
        species="saccharomyces_cerevisiae",
        release="98",
        build="R64-1-1",
        type="all",
        protocol="https",
    log:
        "logs/get_variation.log",
    cache: "omit-software"  # save space and time with between workflow caching (see docs)
    wrapper:
        "master/bio/reference/ensembl-variation"
