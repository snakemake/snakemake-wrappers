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

  CSN

=head1 SYNOPSIS

  mv CSN.pm ~/.vep/Plugins
  ./vep -i variations.vcf --cache --plugin CSN

=head1 DESCRIPTION

  This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
  reports Clinical Sequencing Nomenclature (CSN) for variants.

  Each notation is given with reference to the transcript identifier;
  specify "--plugin CSN,1" to remove this identifier from the CSN string.

  You may also wish to specify "--no_escape" to prevent the "=" in "p.="
  notations being converted to the URI-escaped equivalent "p.%3D"; doing
  so may break parsers looking for "=" as a KEY=VALUE separator.

  See http://biorxiv.org/content/early/2015/03/21/016808.1

=cut

package CSN;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;
use Bio::EnsEMBL::Variation::DBSQL::TranscriptVariationAdaptor;
use Bio::EnsEMBL::Variation::DBSQL::DBAdaptor;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);
  
  # check config is OK
  
  # FASTA file defined, optimal
  if(!defined($self->{config}->{fasta})) {
    
    # offline mode won't work without FASTA
    die("ERROR: Cannot generate CSN without either a FASTA file (--fasta) or a database connection (--cache or --database)\n") if defined($self->{config}->{offline}) and !defined($self->{config}->{quiet});
    
    # cache mode will work, but DB will be accessed
    warn("WARNING: Database will be accessed using this plugin; use a FASTA file (--fasta) for optimal performance") if defined($self->{config}->{cache}) and !defined($self->{config}->{quiet});
  }
  
  no warnings 'once';
  $Bio::EnsEMBL::Variation::DBSQL::TranscriptVariationAdaptor::DEFAULT_SHIFT_HGVS_VARIANTS_3PRIME = 1;
  no warnings 'once';
  $Bio::EnsEMBL::Variation::DBSQL::DBAdaptor::DEFAULT_SHIFT_HGVS_VARIANTS_3PRIME = 1;
  
  $self->{remove_transcript_ID} = $self->params->[0];
  
  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub variant_feature_types {
  return ['VariationFeature'];
}

sub get_header_info {
  return { CSN => 'Clinical Sequencing Nomenclature'};
}

sub run {
  my ($self, $tva) = @_;
  
  my ($hgvs_c, $hgvs_p) = ($tva->hgvs_transcript || '', $tva->hgvs_protein || '');
  
  return {} unless $hgvs_c;
  
  # trim off transcript/protein ID
  $hgvs_c =~ s/.+\:// if $self->{remove_transcript_ID}; 
  $hgvs_p =~ s/.+\://;
  
  # change Ter to X
  $hgvs_p =~ s/Ter/X/g;
  
  # leave just p.=
  $hgvs_p = 'p.=' if $hgvs_p =~ /p\.\=/;
  
  # escape
  $hgvs_p =~ s/\=/\%3D/g unless $self->{config}->{no_escape};
  
  return { CSN => $hgvs_c.($hgvs_p ? '_'.$hgvs_p : '') };
}

1;
