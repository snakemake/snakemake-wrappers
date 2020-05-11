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

  HGVSReferenceBase

=head1 SYNOPSIS

  mv HGVSReferenceBase.pm ~/.vep/Plugins
  ./vep -i variations.vcf --cache --hgvs --plugin HGVSReferenceBase

=head1 DESCRIPTION

  This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
  reports the reference base for the variant, as used in the longer form.
  of HGVS. To be used with --hgvs option.

=cut


package HGVSReferenceBase;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;
use Bio::EnsEMBL::Variation::DBSQL::TranscriptVariationAdaptor;
use Bio::EnsEMBL::Variation::DBSQL::DBAdaptor;
use Bio::EnsEMBL::Variation::TranscriptVariationAllele;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);


sub feature_types {
  return ['Transcript'];
}

sub variant_feature_types {
  return ['VariationFeature'];
}

sub get_header_info {
  my $self = shift;
  
  return {
    'HGVS_ref' => 'Reference base as may be reported in HGVS transcript level notation',
  };
}

sub run {
  my ($self, $tva) = @_;

  # check var class, this is only useful for  deletions 
  # or duplications -  a subset of insertions
  return {} unless $tva->variation_feature->var_class() =~ /del|ins/;

  return $tva->hgvs_transcript_reference() ? {'HGVS_ref' => $tva->hgvs_transcript_reference()} : {};

}

1;
