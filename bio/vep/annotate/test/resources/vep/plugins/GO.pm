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

 GO

=head1 SYNOPSIS

 mv GO.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin GO

=head1 DESCRIPTION

 A VEP plugin that retrieves Gene Ontology terms associated with
 transcripts/translations via the Ensembl API. Requires database connection.
 
=cut

package GO;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);
  
  # connect to DB for offline users
  my $config = $self->{config};
  my $reg = $config->{reg};
  
  if(!defined($self->{config}->{sa})) {
    $reg = 'Bio::EnsEMBL::Registry';
    $reg->load_registry_from_db(
      -host       => $config->{host},
      -user       => $config->{user},
      -pass       => $config->{password},
      -port       => $config->{port},
      -db_version => $config->{db_version},
      -species    => $config->{species} =~ /^[a-z]+\_[a-z]+/i ? $config->{species} : undef,
      -verbose    => $config->{verbose},
      -no_cache   => $config->{no_slice_cache},
    );
  }
  
  return $self;
}

sub version {
  return 73;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return { 'GO' => 'GO terms associated with protein product'};
}

sub run {
  my ($self, $tva) = @_;
  
  my $tr = $tva->transcript->translation;
  return {} unless defined($tr);
  
  my $entries = $tr->get_all_DBEntries('GO');
  
  my $string = join(",", map {$_->display_id.':'.$_->description} @$entries);
  $string =~ s/\s+/\_/g;
  
  return { GO => $string };
}

1;

