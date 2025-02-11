rule download_nanosim_genome_model:
    output:
        model=multiext(
            "resources/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1/training",
            "_aligned_reads.pkl",
            "_aligned_region.pkl",
            "_base_qualities_model_parameters.tsv",
            "_chimeric_info",
            "_del.hist",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_gap_length.pkl",
            "_hp_lengths_model_parameters.tsv",
            "_hp_lengths.tsv",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_ins.hist",
            "_match.hist",
            "_match_markov_model",
            "_mis.hist",
            "_model_profile",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_unaligned_length.pkl",
        ),
    conda: "envs/download.yaml"
    log: "logs/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1/training_download.log",
    shell:
        "cd resources/; "
        "wget https://github.com/bcgsc/NanoSim/raw/refs/heads/master/pre-trained_models/human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.tar.gz; "
        "tar xzf human_giab_hg002_sub1M_kitv14_dorado_v3.2.1.tar.gz; "


rule download_nanosim_transcriptome_model:
    output:
        model=multiext(
            "resources/human_NA12878_cDNA-rel2_guppy_v3.2.2/training",
            "_added_intron_final.gff3",
            "_aligned_reads.pkl",
            "_aligned_region_2d.pkl",
            "_aligned_region.pkl",
            "_base_qualities_model_parameters.tsv",
            "_del.hist",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_hp_lengths_model_parameters.tsv",
            "_hp_lengths.tsv",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_ins.hist",
            "_IR_info",
            "_IR_markov_model",
            "_match.hist",
            "_match_markov_model",
            "_mis.hist",
            "_model_profile",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_transcriptome_alnm_processed.maf",
            "_transcriptome_chimeric_info",
            "_transcriptome_gap_length.pkl",
            "_transcriptome_primary.out",
            "_unaligned_length.pkl",
        ),
    conda: "envs/download.yaml"
    log: "logs/human_NA12878_cDNA-rel2_guppy_v3.2.2/training_download.log",
    shell:
        "cd resources/; "
        "wget https://zenodo.org/records/14042983/files/human_NA12878_cDNA-rel2_guppy_v3.2.2.tar.gz?download=1; "
        "tar xzf human_NA12878_cDNA-rel2_guppy_v3.2.2.tar.gz; "


rule download_nanosim_metagenome_model:
    output:
        model=multiext(
            "resources/metagenome_ERR3152366_Log_v3.2.2/training",
            "_aligned_reads.pkl",
            "_aligned_region.pkl",
            "_base_qualities_model_parameters.tsv",
            "_chimeric_info",
            "_del.hist",
            "_error_markov_model",
            "_error_rate.tsv",
            "_first_match.hist",
            "_gap_length.pkl",
            "_ht_length.pkl",
            "_ht_ratio.pkl",
            "_ins.hist",
            "_match.hist",
            "_match_markov_model",
            "_mis.hist",
            "_model_profile",
            "_quantification.tsv",
            "_reads_alignment_rate",
            "_strandness_rate",
            "_unaligned_length.pkl",
        ),
    conda: "envs/download.yaml"
    log: "logs/metagenome_ERR3152366_Log_v3.2.2/training_download.log",
    shell:
        "cd resources/; "
        "wget https://github.com/bcgsc/NanoSim/raw/refs/heads/master/pre-trained_models/metagenome_ERR3152366_Log_v3.2.2.tar.gz; "
        "tar xzf metagenome_ERR3152366_Log_v3.2.2.tar.gz; "
