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

 MPC

=head1 SYNOPSIS

 mv MPC.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin MPC,fordist_constraint_official_mpc_values.txt.gz

=head1 DESCRIPTION

 A VEP plugin that retrieves MPC scores for variants from a tabix-indexed MPC data file.

 MPC is a missense deleteriousness metric based on the analysis of genic regions
 depleted of missense mutations in the Exome Agggregation Consortium (ExAC) data.

 The MPC score is the product of work by Kaitlin Samocha (ks20@sanger.ac.uk).
 Publication currently in pre-print: Samocha et al bioRxiv 2017 (TBD)
 
 The MPC score file is available to download from:

 ftp://ftp.broadinstitute.org/pub/ExAC_release/release1/regional_missense_constraint/

 The data are currently mapped to GRCh37 only. Not all transcripts are included; see
 README in the above directory for exclusion criteria.
 
=cut

package MPC;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

my %INCLUDE_SO = map {$_ => 1} qw(missense_variant stop_lost stop_gained start_lost);

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
  return { MPC => 'MPC score' };
}

sub run {
  my ($self, $tva) = @_;
  
  # only for missense variants
  return {} unless grep {$INCLUDE_SO{$_->SO_term}} @{$tva->get_all_OverlapConsequences};
  
  my $vf = $tva->variation_feature;
  
  return {} unless $vf->{start} eq $vf->{end};
  
  # get allele, reverse comp if needed
  my $allele = $tva->variation_feature_seq;
  reverse_comp(\$allele) if $vf->{strand} < 0;
  
  return {} unless $allele =~ /^[ACGT]$/;
  
  # get transcript stable ID
  my $tr_id = $tva->transcript->stable_id;

  my ($res) = grep {
    $_->{pos} == $vf->{start} &&
    $_->{alt} eq $allele &&
    $_->{tr}  eq $tr_id
  } @{$self->get_data($vf->{chr}, $vf->{start}, $vf->{end})};

  return $res ? { MPC => $res->{MPC} } : {};
}

sub parse_data {
  my ($self, $line) = @_;

  my @split = split /\t/, $line;

  return {
    pos => $split[1],
    alt => $split[3],
    tr  => $split[5],
    MPC => $split[-1],
  };
}

sub get_start {
  return $_[1]->{pos};
}

sub get_end {
  return $_[1]->{pos};
}

1;
