# Make sure that you set the `truncLen=` option in the rule `dada2_filter_and_trim_pe` according
# to the results of the quality profile checks (after rule `dada2_quality_profile_pe` has finished on all samples).
# If in doubt, check https://benjjneb.github.io/dada2/tutorial.html#inspect-read-quality-profiles

rule all:
    input:
        # In a first run of this meta-wrapper, comment out all other inputs and only keep this one.
        # Looking at the resulting plot, adjust the `truncLen` in rule `dada2_filter_trim_pe` and then
        # rerun with all inputs uncommented.
        expand(
            "reports/dada2/quality-profile/{sample}-quality-profile.png",
            sample=["a","b"]
        ),
        "results/dada2/taxa.RDS"

rule dada2_quality_profile_pe:
    input:
        # FASTQ file without primer sequences
        expand("trimmed/{{sample}}.{orientation}.fastq.gz",orientation=[1,2])
    output:
        "reports/dada2/quality-profile/{sample}-quality-profile.png"
    log:
        "logs/dada2/quality-profile/{sample}-quality-profile-pe.log"
    wrapper:
        "master/bio/dada2/quality-profile"

rule dada2_filter_trim_pe:
    input:
        # Paired-end files without primer sequences
        fwd="trimmed/{sample}.1.fastq.gz",
        rev="trimmed/{sample}.2.fastq.gz"
    output:
        filt="filtered-pe/{sample}.1.fastq.gz",
        filt_rev="filtered-pe/{sample}.2.fastq.gz",
        stats="reports/dada2/filter-trim-pe/{sample}.tsv"
    params:
        # Set the maximum expected errors tolerated in filtered reads
        maxEE=1,
        # Set the number of kept bases in forward and reverse reads
        truncLen=[240,200]
    log:
        "logs/dada2/filter-trim-pe/{sample}.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/filter-trim"

rule dada2_learn_errors:
    input:
    # Quality filtered and trimmed forward FASTQ files (potentially compressed) 
        expand("filtered-pe/{sample}.{{orientation}}.fastq.gz", sample=["a","b"])
    output:
        err="results/dada2/model_{orientation}.RDS",# save the error model
        plot="reports/dada2/errors_{orientation}.png",# plot observed and estimated rates
    params:
        randomize=True
    log:
        "logs/dada2/learn-errors/learn-errors_{orientation}.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/learn-errors"

rule dada2_dereplicate_fastq:
    input:
    # Quality filtered FASTQ file
        "filtered-pe/{fastq}.fastq.gz"
    output:
    # Dereplicated sequences stored as `derep-class` object in a RDS file 
        "uniques/{fastq}.RDS"
    log:
        "logs/dada2/dereplicate-fastq/{fastq}.log"
    wrapper:
        "master/bio/dada2/dereplicate-fastq"

rule dada2_sample_inference:
    input:
    # Dereplicated (aka unique) sequences of the sample
        derep="uniques/{sample}.{orientation}.RDS",
        err="results/dada2/model_{orientation}.RDS" # Error model
    output:
        "denoised/{sample}.{orientation}.RDS" # Inferred sample composition
    log:
        "logs/dada2/sample-inference/{sample}.{orientation}.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/sample-inference"

rule dada2_merge_pairs:
    input:
      dadaF="denoised/{sample}.1.RDS",# Inferred composition
      dadaR="denoised/{sample}.2.RDS",
      derepF="uniques/{sample}.1.RDS",# Dereplicated sequences
      derepR="uniques/{sample}.2.RDS"
    output:
        "merged/{sample}.RDS"
    log:
        "logs/dada2/merge-pairs/{sample}.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/merge-pairs"

rule dada2_make_table_pe:
    input:
    # Merged composition
        expand("merged/{sample}.RDS", sample=['a','b'])
    output:
        "results/dada2/seqTab-pe.RDS"
    params:
        names=['a','b'], # Sample names instead of paths
        orderBy="nsamples" # Change the ordering of samples
    log:
        "logs/dada2/make-table/make-table-pe.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/make-table"

rule dada2_remove_chimeras:
    input:
        "results/dada2/seqTab-pe.RDS" # Sequence table
    output:
        "results/dada2/seqTab.nochimeras.RDS" # Chimera-free sequence table
    log:
        "logs/dada2/remove-chimeras/remove-chimeras.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/remove-chimeras"

rule dada2_collapse_nomismatch:
    input:
        "results/dada2/seqTab.nochimeras.RDS" # Chimera-free sequence table
    output:
        "results/dada2/seqTab.collapsed.RDS"
    log:
        "logs/dada2/collapse-nomismatch/collapse-nomismatch.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/collapse-nomismatch"

rule dada2_assign_taxonomy:
    input:
        seqs="results/dada2/seqTab.collapsed.RDS", # Chimera-free sequence table
        refFasta="resources/example_train_set.fa.gz" # Reference FASTA for taxonomy
    output:
        "results/dada2/taxa.RDS" # Taxonomic assignments
    log:
        "logs/dada2/assign-taxonomy/assign-taxonomy.log"
    threads: 1 # set desired number of threads here
    wrapper:
        "master/bio/dada2/assign-taxonomy"
