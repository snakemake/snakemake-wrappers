
rule get_vep_cache_https_protocol:
    output:
        directory("resources/vep/cache"),
    params:
        species="saccharomyces_cerevisiae",
        build="R64-1-1",
        release="98",
        protocol="https",
    log:
        "logs/vep/cache.log",
    cache: "omit-software"  # save space and time with between workflow caching (see docs)
    wrapper:
        "master/bio/vep/cache"
