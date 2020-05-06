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

 CCDSFilter

=head1 SYNOPSIS

 mv CCDSFilter.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin CCDSFilter

=head1 DESCRIPTION

 A simple VEP filter plugin that limits output to variants that
 fall in transcripts which have CCDS coding sequences.

=cut

package CCDSFilter;

use strict;
use warnings;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepFilterPlugin);

sub feature_types {
    return ['Transcript'];
}

sub include_line {
    my ($self, $tva) = @_;

    my $t = $tva->transcript;

    my @entries = grep {$_->database eq 'CCDS'} @{$t->get_all_DBEntries};
   
    return scalar @entries;
}

1;

