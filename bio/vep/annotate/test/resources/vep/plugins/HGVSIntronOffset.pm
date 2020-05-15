=head1 LICENSE

Copyright 2018 QIMR Berghofer Medical Research Institute

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

 Stephen Kazakoff <Stephen.Kazakoff@qimrberghofer.edu.au>
    
=cut

=head1 NAME

 HGVSIntronOffset

=head1 SYNOPSIS

 mv HGVSIntronOffset.pm ~/.vep/Plugins
 ./vep -i variants.vcf --hgvs --plugin HGVSIntronOffset

=head1 DESCRIPTION

 A VEP plugin for the Ensembl Variant Effect Predictor (VEP) that returns
 HGVS intron start and end offsets. To be used with --hgvs option.

=cut

package HGVSIntronOffset;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    HGVS_IntronStartOffset => "HGVS intron start offset",
    HGVS_IntronEndOffset => "HGVS intron end offset",
  };
}

sub run {
  my ($self, $tva) = @_;

  return {} unless $tva->hgvs_transcript;

  my $start_offset = $tva->hgvs_intron_start_offset;
  my $end_offset = $tva->hgvs_intron_end_offset;

  return {} unless defined($start_offset) && defined($end_offset);

  return {
    HGVS_IntronStartOffset => $start_offset,
    HGVS_IntronEndOffset => $end_offset,
  };
}

1;
