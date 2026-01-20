# SAMPLE RULE: Minimal usage with defaults
rule pytrf_findstr_defaults:
    input:
        "demo_data/small_test.fasta",
    output:
        "results/small_test_defaults.tsv",
    log:
        "logs/small_test_defaults.log",
    wrapper:
        "master/bio/pytrf/findstr"
