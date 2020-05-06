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

 miRNA

=head1 SYNOPSIS

 mv miRNA.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin miRNA

=head1 DESCRIPTION

 A VEP plugin that determines where in the secondary structure of a miRNA a
 variant falls.
 
=cut

package miRNA;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  my $self = shift;
  return {
    miRNA => 'SO term for miRNA component containing the variant'
  }
}

sub run {
  my ($self, $tva) = @_;
  
  my $tv = $tva->transcript_variation;
  my $tr = $tva->transcript;
  
  # obviously this only works for *RNA transcripts
  return {} unless $tr->biotype =~ /RNA/;
  
  # and it only works if the TV falls in the cDNA
  return {} unless $tv->cdna_start && $tv->cdna_end;
  
  # get attribute if already cached
  my ($attrib) = @{$tr->get_all_Attributes('ncRNA')};
  
  # bit of a cheat to get attrib if ncRNA attribute hasn't been cached
  if(!$attrib && defined($self->{config}->{ta})) {
    delete $tr->{attributes};
    $tr->{adaptor} = $self->{config}->{ta};
    ($attrib) = @{$tr->get_all_Attributes('ncRNA')};
  }
  
  return {} unless $attrib;
  
  # split out string to get coords and structure string
  my ($start, $end, $struct) = split /\s+|\:/, $attrib->value;
  return {} unless $struct && $struct =~ /[\(\.\)]+/;
  
  # variant not in given structure?
  return { miRNA => 'None' } unless $tv->cdna_start <= $end && $tv->cdna_end >= $start;
  
  # parse out structure
  my @struct;
  while($struct =~ m/([\.\(\)])([0-9]+)?/g) {
    my $num = $2 || 1;
    push @struct, $1 for(1..$num);
  }
  
  # get struct element types overlapped by variant
  my %chars;
  for my $pos($tv->cdna_start..$tv->cdna_end) {
    $pos -= $start;
    next if $pos < 0 or $pos > scalar @struct;
    $chars{$struct[$pos]} = 1;
  }
  
  # map element types to SO terms
  my %map = (
    '(' => 'miRNA_stem',
    ')' => 'miRNA_stem',
    '.' => 'miRNA_loop'
  );
  
  return {
    miRNA => join(",", sort map {$map{$_}} keys %chars)
  };
}

1;

