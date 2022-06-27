rule test_mashmap_reflist:
    input:
        ref="reference.txt",
        query="read.fasta.gz",
    output:
        "mashmap.out",
    params:
        extra="-s 500 --pi 99",
    log:
        "logs/mashmap.log",
    wrapper:
        "master/bio/mashmap"
