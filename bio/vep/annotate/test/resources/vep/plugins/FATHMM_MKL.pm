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

 FATHMM_MKL

=head1 SYNOPSIS

 mv FATHMM_MKL.pm ~/.vep/Plugins
 ./vep -i input.vcf --plugin FATHMM_MKL,fathmm-MKL_Current.tab.gz

=head1 DESCRIPTION

 A VEP plugin that retrieves FATHMM-MKL scores for variants from a tabix-indexed
 FATHMM-MKL data file.
 
 See https://github.com/HAShihab/fathmm-MKL for details.

 NB: The currently available data file is for GRCh37 only.
 
=cut

package FATHMM_MKL;

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

  return $self;
}

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {
  my $self = shift;
  return {
    FATHMM_MKL_C => 'FATHMM-MKL coding score',
    FATHMM_MKL_NC => 'FATHMM-MKL non-coding score',
  }
}

sub run {
  my ($self, $tva) = @_;
  
  my $vf = $tva->variation_feature;

  return {} unless $vf->{start} eq $vf->{end};
  
  # get allele, reverse comp if needed
  my $allele = $tva->variation_feature_seq;
  reverse_comp(\$allele) if $vf->{strand} < 0;
  
  return {} unless $allele =~ /^[ACGT]$/;
  
  # adjust coords, file is BED-like (but not 0-indexed, go figure...)
  my ($s, $e) = ($vf->{start}, $vf->{end} + 1);
  
  foreach my $data(@{$self->get_data($vf->{chr}, $s, $e)}) {
    if($data->{start} == $s && $allele eq $data->{alt}) {
      return $data->{result};
    }
  }

  return {};
}

sub parse_data {
  my ($self, $line) = @_;

  my ($c, $s, $e, $ref, $alt, $nc_score, $nc_groups, $c_score, $c_groups) = split /\t/, $line;

  return {
    start => $s,
    end => $e - 1,
    alt => $alt,
    result => {
      FATHMM_MKL_C  => $c_score,
      FATHMM_MKL_NC => $nc_score,
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

