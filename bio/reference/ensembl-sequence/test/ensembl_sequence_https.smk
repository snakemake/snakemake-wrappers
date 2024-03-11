rule get_genome_http_protocol:
    output:
        "refs/genome.fasta",
    params:
        species="saccharomyces_cerevisiae",
        datatype="dna",
        build="R64-1-1",
        release="98",
        protocol="http",
    log:
        "logs/get_genome.log",
    cache: "omit-software"  # save space and time with between workflow caching (see docs)
    wrapper:
        "master/bio/reference/ensembl-sequence"
