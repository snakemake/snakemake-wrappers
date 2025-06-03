# VALIDATIONS RULE 1: Checks if error generated with missing param
#################### value.
rule run_trf_with_missing_param_value:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        match=2,
        mismatch=7,
        delta=7,
        pm=80,
        maxperiod=500,
        extra="-f -d -m",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 2: Checks other permissible flags apart from
####################  recommended ones.with valid input file.
rule run_trf_permissible_flags:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        match=2,
        mismatch=7,
        delta=7,
        pm=80,
        pi=10,
        minscore=50,
        maxperiod=500,
        extra="-H -L29",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 3: Gracefully runs for partial
##################### or all upper caps, although conventionally
##################### not recommended.
rule run_trf_basic_uppercase:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    log:
        "logs/{sample}.log",
    params:
        MATCH=2,
        mismatch=7,
        deltA=7,
        PM=80,
        Pi=10,
        minscore=50,
        maxperiod=500,
        eXtra="-f -d -m",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 4: Gracefully runs for not set log directive,
##################### although not recommended option and commenting
##################### to avoid linter conflicts.
# rule run_trf_checks_without_log_directive:
#     input:
#         sample="demo_data/{sample}.fasta",
#     output:
#         directory("trf_output/{sample}"),
#     params:
#         match=2,
#         mismatch=7,
#         delta=7,
#         pm=80,
#         pi=10,
#         minscore=50,
#         maxperiod=500,
#     wrapper:
#         "master/bio/trf"
