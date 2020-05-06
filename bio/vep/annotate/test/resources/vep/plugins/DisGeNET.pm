=head1 LICENSE

Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2020] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

=head1 CONTACT

 Ensembl <http://www.ensembl.org/info/about/contact/index.html>

=cut

=head1 NAME

 DisGeNET

=head1 SYNOPSIS

 mv DisGeNET.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin DisGeNET,file=/path/to/disgenet/data.tsv.gz
 ./vep -i variations.vcf --plugin DisGeNET,file=/path/to/disgenet/data.tsv.gz,disease=1

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 adds Variant-Disease-PMID associations from the DisGeNET database.
 It is available for GRCh38.

 Please cite the DisGeNET publication alongside the VEP if you use this resource:
 https://academic.oup.com/nar/article/48/D1/D845/5611674


 Options are passed to the plugin as key=value pairs:

 file           : Path to DisGENET data file (mandatory).

 disease        : Set value to 1 to include the diseases/phenotype names reporting
                  the Variant-PMID association (optional).

 rsid           : Set value to 1 to include the dbSNP variant Identifier (optional).

 filter_score   : Only reports citations with score greater or equal than input value (optional).

 filter_source  : Only reports citations from input sources (optional).
                  Accepted sources are: UNIPROT, CLINVAR, GWASDB, GWASCAT, BEFREE
                  Separate multiple values with '&'.

 unique         : Only reports unique dbSNP variant Identifiers and diseases/phenotype names (optional)


 Output:
 The output includes: 
  - PMID of the publication reporting the Variant-Disease association (default)
  - DisGENET score for the Variant-Disease association (default)
  - dbSNP variant Identifier (optional)
  - diseases/phenotype names (optional)

 The following steps are necessary before running this plugin:
 This plugin uses file 'all_variant_disease_pmid_associations.tsv.gz'
 File can be downloaded from: https://www.disgenet.org/downloads

 gunzip all_variant_disease_pmid_associations.tsv.gz

 awk '($1 ~ /^snpId/ || $2 ~ /NA/) {next} {print $0 | "sort -k2,2 -k3,3n"}' 
 all_variant_disease_pmid_associations.tsv > all_variant_disease_pmid_associations_sorted.tsv

 bgzip all_variant_disease_pmid_associations_sorted.tsv
 tabix -s 2 -b 3 -e 3 all_variant_disease_pmid_associations_sorted.tsv.gz

 The plugin can then be run as default:
 ./vep -i variations.vcf --plugin DisGeNET,file=all_variant_disease_pmid_associations_sorted.tsv.gz

 or with an option to include optional data or/and filters: 
 ./vep -i variations.vcf --plugin DisGeNET,file=all_variant_disease_pmid_associations_sorted.tsv.gz,
 disease=1
 ./vep -i variations.vcf --plugin DisGeNET,file=all_variant_disease_pmid_associations_sorted.tsv.gz,
 disease=1,filter_source='GWASDB&GWASCAT'

 Of notice: this plugin only matches the chromosome and the position in the
  chromosome, the alleles are not taken into account to append the DisGENET data.
  The rsid is provided (optional) in the output in order to help to filter the relevant data.


=cut
package DisGeNET;

use strict;
use warnings;

use List::MoreUtils qw(uniq);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

my $valid_sources = {
  UNIPROT => 1,
  CLINVAR => 1,
  GWASDB => 1,
  GWASCAT => 1,
  BEFREE => 1
};

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  my $param_hash = $self->params_to_hash();

  die("ERROR: DisGENET file not provided or not found!\n") unless defined($param_hash->{file}) && -e $param_hash->{file};

  $self->add_file($param_hash->{file});

  if(defined($param_hash->{disease})) {
    my $disease = $param_hash->{disease};
    $self->{disease} = $disease;
  }

  if(defined($param_hash->{rsid})) {
    my $rsid = $param_hash->{rsid};
    $self->{rsid} = $rsid;
  }

  if(defined($param_hash->{unique})) {
    my $unique = $param_hash->{unique};
    $self->{unique} = $unique;
  }

  if(defined($param_hash->{filter_score})) {
    my $filter_score = $param_hash->{filter_score};
    if($filter_score < 0 || $filter_score > 1) {
      die("ERROR: Score must be between 0 and 1!\n");
    }
    $self->{filter_score} = $filter_score;
  }

  if(defined($param_hash->{filter_source})) {
    my @sources_filter;
    foreach my $source (split(/[\;\&\|]/, $param_hash->{filter_source})) {
      if (!$valid_sources->{$source}) {
        die "ERROR: $source is not a supported source name. Supported sources are: ", join(', ', keys %$valid_sources), "\n";
      }
      else {
        push @sources_filter, $source;
      }
    }
    if (scalar @sources_filter > 0) {
      $self->{source_to_filter} = \@sources_filter;
    }
  }

  return $self;
}

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {
  my $self = shift;

  my %header;

  $header{'DisGeNET_PMID'} = 'PMID of the publication reporting the Variant-Disease association';
  $header{'DisGeNET_SCORE'} = 'DisGENET score for the Variant-Disease association';

  if($self->{disease}) {
    $header{'DisGeNET_disease'} = 'Name of the disease reporting the Variant-pmid association';
  }
  if($self->{rsid}) {
    $header{'DisGeNET_rsid'} = 'dbSNP variant Identifier';
  }

  return \%header;
}

sub run {
  my ($self, $tva) = @_;

  my $vf = $tva->variation_feature;

  my $chr = $vf->{chr};

  my $end = $vf->{end};
  my $start = $vf->{start};
  ($start, $end) = ($end, $start) if $start > $end;

  my @data = @{$self->get_data($chr, $start, $end)};

  return {} unless(@data);

  my %hash;
  my @result_pmid;
  my @result_score;
  my @result_rsid;
  my %unique_values;
  my @diseases;
  my %unique_diseases;

  foreach my $data_value (@data) {
    my $pmid = $data_value->{pmid};
    my $rsid = $data_value->{rsid};
    my $score = $data_value->{score};
    my $source = $data_value->{source};

    if($self->{filter_score}) {
      next if($score < $self->{filter_score});
    }

    if($self->{source_to_filter}) {
      my $sources_aux = $self->{source_to_filter};
      my $check = check_source($sources_aux, $source);
      next if(!$check);
    }

    # Some publications are duplicated - same publications from different sources are in different rows
    # Check if pmid and rsid are not returned more than once
    if(!$unique_values{$pmid.':'.$rsid}++) {
      push @result_pmid, $pmid;
      push @result_score, $score;
      if($self->{rsid}) {
        push @result_rsid, $rsid;
      }
    }

    if($self->{disease}) {
      my $disease_name = $data_value->{diseaseName};
      if($self->{unique}) {
        if(!$unique_diseases{$disease_name}++) {
          push @diseases, $disease_name;
        }
      }
      else{
        push @diseases, $disease_name;
      }
    }
  }

  $hash{'DisGeNET_PMID'} = join(',', @result_pmid);
  $hash{'DisGeNET_SCORE'} = join(',', @result_score);

  if($self->{disease}) {
    $hash{'DisGeNET_disease'} = join(',', @diseases);
  }

  if($self->{rsid}) {
    if($self->{unique}) {
      my @u_result_rsid = uniq @result_rsid;
      $hash{'DisGeNET_rsid'} = join(',', @u_result_rsid);
    }
    else {
      $hash{'DisGeNET_rsid'} = join(',', @result_rsid);
    }
  }

  return scalar @result_pmid > 0 ? \%hash : {};
}

sub parse_data {
  my ($self, $line) = @_;

  # Data in file is: 
  # 'snpId, chromosome, position, DSI, DPI, diseaseId, diseaseName, diseaseType, diseaseClass,
  # diseaseSemanticType, score, EI, YearInitial, YearFinal, pmid, source'

  my @all_data = split /\t/, $line;

  # Delete commas from phenotype/disease description
  my $disease = $all_data[6];
  if($disease =~ /,/) {
    $disease =~ s/,//g;
  }

  return {
      rsid => $all_data[0],
      diseaseName => $disease,
      score => $all_data[10],
      pmid => $all_data[14],
      source => $all_data[15]
  };
}

sub get_start {
  return $_[1]->{start};
}

sub get_end {
  return $_[1]->{end};
}

sub check_source {
  my $input_sources = shift;
  my $var_source = shift;

  my $result = 0;

  my %hash_sources = map { $_ => 1 } @$input_sources;

  if(exists($hash_sources{$var_source})) {
    $result = 1;
  }

  return $result;
}

1;
