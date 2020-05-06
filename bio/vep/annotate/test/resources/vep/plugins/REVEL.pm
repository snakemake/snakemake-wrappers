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

 REVEL

=head1 SYNOPSIS

 mv REVEL.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin REVEL,/path/to/revel/data.tsv.gz

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 adds the REVEL score for missense variants to VEP output.

 Please cite the REVEL publication alongside the VEP if you use this resource:
 https://www.ncbi.nlm.nih.gov/pubmed/27666373
 
 REVEL scores can be downloaded from: https://sites.google.com/site/revelgenomics/downloads
 and can be tabix-processed by:
 
 cat revel_all_chromosomes.csv | tr "," "\t" > tabbed_revel.tsv
 sed '1s/.*/#&/' tabbed_revel.tsv > new_tabbed_revel.tsv
 bgzip new_tabbed_revel.tsv
 tabix -f -s 1 -b 2 -e 2 new_tabbed_revel.tsv.gz

 The tabix utility must be installed in your path to use this plugin.

=cut
package REVEL;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  $self->get_user_params();

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return { REVEL => 'Rare Exome Variant Ensemble Learner '};
}

sub run {
  my ($self, $tva) = @_;
  # only for missense variants
  return {} unless grep {$_->SO_term eq 'missense_variant'} @{$tva->get_all_OverlapConsequences};

  my $vf = $tva->variation_feature;
  my $allele = $tva->variation_feature_seq;
  my ($res) = grep {
    $_->{alt}   eq $allele &&
    $_->{start} eq $vf->{start} &&
    $_->{end}   eq $vf->{end} &&
    $_->{altaa} eq $tva->peptide
  } @{$self->get_data($vf->{chr}, $vf->{start}, $vf->{end})};

  return $res ? $res->{result} : {};
}

sub parse_data {
  my ($self, $line) = @_;

  my ($c, $s, $ref, $alt, $refaa, $altaa, $revel_value) = split /\t/, $line;

  return {
    alt => $alt,
    start => $s,
    end => $s,
    altaa => $altaa,
    result => {
      REVEL   => $revel_value,
    }
  };
}

sub get_start {
  return $_[1]->{start};
}

sub get_end {
  return $_[1]->{end};
}

1;
