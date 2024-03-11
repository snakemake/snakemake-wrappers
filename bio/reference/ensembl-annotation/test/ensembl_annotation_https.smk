rule get_annotation_https_protocol_gz:
    output:
        "refs/annotation.gtf.gz",
    params:
        species="homo_sapiens",
        release="105",
        build="GRCh37",
        flavor="",
        protocol="https",
    log:
        "logs/get_annotation.log",
    cache: "omit-software"  # save space and time with between workflow caching (see docs)
    wrapper:
        "master/bio/reference/ensembl-annotation"
