######################################################
# Snakefile for testing extra rules of pytrf wrapper
######################################################


rule pytrf_findgtr:
    input:
        seq="demo_data/{sample}.fasta",
    output:
        "results/{sample}_findgtr.tsv",
    log:
        "logs/{sample}.log",
    params:
        subcommand="findgtr",
        extra="-m 3 -r 1",  # min-motif=3, min-repeat=1
    wrapper:
        "master/bio/pytrf"


rule pytrf_findatr:
    input:
        seq="demo_data/{sample}.fasta",
    output:
        "results/{sample}_findatr.tsv",
    log:
        "logs/{sample}.log",
    params:
        subcommand="findatr",
        extra="-m 3 -M 10",  # min-motif-size=3, max-motif-size=10
    wrapper:
        "master/bio/pytrf"


rule pytrf_extract:
    input:
        seq="demo_data/small_test_extract.fasta",  # sequence fasta
        repeat="demo_data/small_test_extract.tsv",  # repeat file from findstr/findgtr/findatr
    output:
        "results/small_test_extract.tsv",
    log:
        "logs/small_test_extract.log",
    params:
        subcommand="extract",
        extra="-l 150",  # flank-length=150
    wrapper:
        "master/bio/pytrf"
