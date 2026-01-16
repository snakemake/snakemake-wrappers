# SAMPLE RULE 1: Minimal usage with all defaults
# When params are omitted, pytrf findstr uses default values:
# - repeats: [12, 7, 5, 4, 4, 4] (standard thresholds for SSR detection)
# - out_format: 'tsv' (tab-separated values)
#
# When output is omitted, results go to stdout, which is redirected
# to the log file. This is useful for quick inspection or piping to other tools.
rule pytrf_findstr_defaults:
    input:
        "demo_data/small_test.fasta",
    # No output specified - results written to stdout (redirected to log)
    # No params specified - uses pytrf default values
    log:
        "logs/small_test_defaults.log",
    wrapper:
        "master/bio/pytrf/findstr"
