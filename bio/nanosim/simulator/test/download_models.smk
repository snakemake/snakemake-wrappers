rule download_nanosim_genome_model:
    output:
        model=multiext(
            "resources/human_NA12878_DNA_FAB49712_guppy/training",
            "_aligned_reads.pkl",
            "_aligned_region.pkl",
            "_chimeric_info",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_gap_length.pkl",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_match_markov_model",
            "_model_profile",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_unaligned_length.pkl",
        ),
    shell:
        "cd resources/; "
        "wget https://github.com/bcgsc/NanoSim/raw/master/pre-trained_models/human_NA12878_DNA_FAB49712_guppy.tar.gz; "
        "tar xzf human_NA12878_DNA_FAB49712_guppy.tar.gz; "


rule download_nanosim_transcriptome_model:
    output:
        model=multiext(
            "resources/human_NA12878_cDNA_Bham1_albacore/training",
            "_added_intron_final.gff3",
            "_aligned_reads.pkl",
            "_aligned_region_2d.pkl",
            "_aligned_region.pkl",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_IR_markov_model",
            "_match_markov_model",
            "_model_profile",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_unaligned_length.pkl",
        ),
    shell:
        "cd resources/; "
        "wget https://github.com/bcgsc/NanoSim/raw/master/pre-trained_models/human_NA12878_cDNA_Bham1_albacore.tar.gz; "
        "tar xzf human_NA12878_cDNA_Bham1_albacore.tar.gz; "


rule download_nanosim_metagenome_model:
    output:
        model=multiext(
            "resources/metagenome_ERR3152364_Even/training",
            "_aligned_reads.pkl",
            "_aligned_region.pkl",
            "_chimeric_info",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_gap_length.pkl",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_match_markov_model",
            "_model_profile",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_unaligned_length.pkl",
        ),
    shell:
        "cd resources/; "
        "wget https://github.com/bcgsc/NanoSim/raw/master/pre-trained_models/metagenome_ERR3152364_Even.tar.gz; "
        "tar xzf metagenome_ERR3152364_Even.tar.gz; "
