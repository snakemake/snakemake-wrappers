rule test_mashmap_reflist:
    input:
        ref="reference.txt",
        query="reads.fq.gz"
    output:
        "mashmap.out"
    params:
        extra=""
    log:
        "logs/mashmap.log"
    wrapper:
        "master/bio/mashmap"