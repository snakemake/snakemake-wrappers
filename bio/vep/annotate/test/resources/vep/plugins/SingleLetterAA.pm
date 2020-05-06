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

 SingleLetterAA

=head1 SYNOPSIS

 mv SingleLetterAA.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin SingleLetterAA

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 returns a HGVSp string with single amino acid letter codes

=cut
package SingleLetterAA;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return { HGVSp => 'Altered to provide HGVSp with single amino acid letter codes '};
}

sub run {
  my ($self, $tva) = @_;
  
  my $vf = $tva->variation_feature;
  my $tva_tv = $tva->base_variation_feature_overlap;
  my $hgvs_full_string = $tva->hgvs_protein();

  return {} unless defined($hgvs_full_string);

  my $hgvs_notation;
  $hgvs_notation->{start}   = $tva_tv->translation_start();
  $hgvs_notation->{end}     = $tva_tv->translation_end();  
  $hgvs_notation->{alt} = $tva->peptide;
  $hgvs_notation->{ref} = $tva_tv->get_reference_TranscriptVariationAllele->peptide;    

  my @hgvs_array = split(':', $hgvs_full_string);
  $hgvs_notation->{ref_name} = $hgvs_array[0];
  $hgvs_notation->{'numbering'} = 'p';

  $hgvs_notation = $tva->_get_hgvs_protein_type($hgvs_notation);
  my $separator = ':p.';
  my @split =  split(/$separator/, $tva->_get_hgvs_protein_format($hgvs_notation));
  if (scalar(@split) == 2)
  {
    $split[1] =~ s/Ter|X/*/g;
    return {
        HGVSp  => $split[0] . $separator . $split[1],
    };
  }
  #else something has gone wrong and our HGVSp string doesn't contain :p.
  return {};
}

1;
