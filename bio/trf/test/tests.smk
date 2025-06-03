# VALIDATIONS RULE 1: Checks with default params if error generated
#################### for invalid file type, that is {sample}.bam.
rule run_trf_invalid_file:
    input:
        sample="demo_data/{sample}.bam",
    output:
        directory("trf_output/{sample}"),
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 2: Checks invalid param e.g delta=20, if error generated
#################### for invalid value or not.
rule run_trf_invalid_param_value:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        pm=20,
        extra="-H",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 3: Checks permissible flags run with valid input file.
#######################################################################
rule run_trf_permissible_flags:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        extra="-H -L29",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 4: Checks permissbile flag types with mistake, run with valid
#################### input file.
rule run_trf_permissible_flag_with_mistake:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        extra=">m",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 5: Checks permissbile optional flag types with mistake,
################### run with valid input file.
rule run_trf_permissible__optional_flag_with_mistake:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        extra="*l20",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 6: Checks permissbile optional flag types with additional
################### flag input style that is -l 20, with space inbetween.
rule run_trf_permissible_flag_with_additional_feature:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        MAtch=2,
        mismatch=3,
        delta=3,
        pm=75,
        pi=20,
        minscore=100,
        maxperiod=500,
        extra="-h -j -m -l=0",
        jump="orange",
        # mismatch=2,
        # extra="-l 20",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 7: Checks impermissible flag types with valid input file.
###########################################################################
rule run_trf_impermissible_flag_types:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    params:
        extra="-g *K )",
    log:
        "logs/{sample}.log",
    wrapper:
        "master/bio/trf"


# VALIDATIONS RULE 8: Checks for run, if not set log directive.
##################################################################
rule run_trf_checks_custom_logging:
    input:
        sample="demo_data/{sample}.fasta",
    output:
        directory("trf_output/{sample}"),
    wrapper:
        "master/bio/trf"
