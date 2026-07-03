rule download_ensembl_genome_sequence:
    output:
        temp("<resources>/{species}.{build}.{release}/{build}.ensembl.fasta"),
    params:
        species="{species}",
        build="{build}",
        release="{release}",
        datatype="dna",
    log:
        "<logs>/download_ensembl_genome_sequence/{species}.{build}.{release}.log",
    cache: "omit-software"
    wrapper:
        "v5.10.0/bio/reference/ensembl-sequence"


rule filter_genome_sequence_contigs:
    input:
        fasta="<resources>/{species}.{build}.{release}/{build}.ensembl.fasta",
    output:
        temp("<resources>/{species}.{build}.{release}/{build}.contigs_filtered.fasta"),
    params:
        extra="",
        regions=config.get("contigs", ""),
    log:
        "<logs>/filter_genome_sequence_contigs/{species}.{build}.{release}.log",
    wrapper:
        "v9.4.2/bio/pyfaidx"


rule download_ensembl_genome_annotations:
    output:
        temp("<resources>/{species}.{build}.{release}/{build}.ensembl.gff3"),
    params:
        species="{species}",
        build="{build}",
        release="{release}",
        flavor="",
    log:
        "<logs>/download_ensembl_genome_annotations/{species}.{build}.{release}.log",
    cache: "omit-software"
    wrapper:
        "v9.4.2/bio/reference/ensembl-annotation"


rule fix_known_format_issues_with_ensembl_gff:
    input:
        gff="<resources>/{species}.{build}.{release}/{build}.ensembl.gff3",
    output:
        o=temp("<resources>/{species}.{build}.{release}/{build}.format_fixed.gff3"),
    params:
        command="agat_convert_sp_gxf2gxf.pl",
        extra="",
    log:
        "<logs>/fix_known_format_issues_with_ensembl_gff/{species}.{build}.{release}.log",
    wrapper:
        "v9.6.0/bio/agat"


rule remove_tsl_na_from_gff_annotations:
    input:
        gff="<resources>/{species}.{build}.{release}/{build}.format_fixed.gff3",
    output:
        o=temp("<resources>/{species}.{build}.{release}/{build}.no_tsl_na.gff3"),
    params:
        command="agat_sp_filter_feature_by_attribute_value.pl",
        extra="--attribute 'transcript_support_level' --value '\"NA\"' --test '='",
    log:
        "<logs>/remove_tsl_na_from_gff_annotations/{species}.{build}.{release}.log",
    wrapper:
        "v9.6.0/bio/agat"


rule ensure_annotations_and_sequences_have_same_contigs:
    input:
        gff="<resources>/{species}.{build}.{release}/{build}.no_tsl_na.gff3",
        fasta="<resources>/{species}.{build}.{release}/{build}.contigs_filtered.fasta",
    output:
        o="<resources>/{species}.{build}.{release}/{build}.contigs_filtered.gff3",
    params:
        extra="",
        command="agat_sq_filter_feature_from_fasta.pl",
    log:
        "<logs>/ensure_annotations_and_sequences_have_same_contigs/{species}.{build}.{release}.log",
    wrapper:
        "v9.6.0/bio/agat"


rule compute_genome_wide_statistics:
    input:
        # Avoid useless pyfaidx filter in case user do not want to filter on contigs
        gff=branch(
            condition=config.get("contigs"),
            then="<resources>/{species}.{build}.{release}/{build}.contigs_filtered.gff3",
            otherwise="<resources>/{species}.{build}.{release}/{build}.no_tsl_na.gff3",
        ),
        gs=branch(
            condition=config.get("contigs"),
            then="<resources>/{species}.{build}.{release}/{build}.contigs_filtered.fasta",
            otherwise="<resources>/{species}.{build}.{release}/{build}.ensembl.fasta",
        ),
    output:
        report="<results>/{species}.{build}.{release}/agat_genome_statistics.txt",
        yaml="<results>/{species}.{build}.{release}/agat_genome_statistics.yaml",
        plot=directory(
            "<results>/{species}.{build}.{release}/agat_genome_statistics_plots"
        ),
    log:
        "<logs>/compute_genome_wide_statistics/{species}.{build}.{release}.log",
    params:
        extra="",
        command="agat_sp_statistics.pl",
    wrapper:
        "v9.6.0/bio/agat"
