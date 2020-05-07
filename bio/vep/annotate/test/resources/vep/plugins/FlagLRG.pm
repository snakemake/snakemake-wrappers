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

 FlagLRG

=head1 SYNOPSIS

 mv FlagLRG.pm ~/.vep/Plugins
 ./vep -i variants.vcf --plugin FlagLRG,/path/to/list_LRGs_transcripts_xrefs.txt

=head1 DESCRIPTION

 A VEP plugin that retrieves the LRG ID matching either the RefSeq or Ensembl
 transcript IDs. You can obtain the 'list_LRGs_transcripts_xrefs.txt' using:

 > wget ftp://ftp.ebi.ac.uk/pub/databases/lrgex/list_LRGs_transcripts_xrefs.txt

=cut

package FlagLRG;

use strict;
use warnings;

use Text::CSV;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);


sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  my $params = $self->params;

  my $file = shift @$params;

  die("ERROR: FlagLRG $file not found\n") unless $file && -e $file;

  open(my $fh, $file) or die $!;

  chomp(my $header_line = <$fh>);
  $header_line =~ s/^#\s*//;

  chomp(my $column_names = <$fh>);
  $column_names =~ s/^#\s*//;

  my $tsv = Text::CSV->new({ binary => 1, auto_diag => 1, sep_char => "\t" });

  $tsv->parse($column_names);
  $tsv->column_names($tsv->fields);

  while (my $href = $tsv->getline_hr($fh)) {

    my $lrg_tr = $href->{'LRG'} . $href->{'LRG_TRANSCRIPT'};

    my $refseq_tr = $href->{'REFSEQ_TRANSCRIPT'};
    my $ensembl_tr = $href->{'ENSEMBL_TRANSCRIPT'};

    $self->{cache}{$refseq_tr} = $lrg_tr unless $refseq_tr eq '-';
    $self->{cache}{$ensembl_tr} = $lrg_tr unless $ensembl_tr eq '-';
  }

  close $fh;

  $self->{header_line} = $header_line;

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  my $self = shift;

  return {
    FlagLRG => $self->{header_line},
  };
}

sub run {
  my ($self, $tva) = @_;

  my $tr = $tva->transcript;
  my $tr_id = $tr->stable_id;

  $tr_id .= '.'.$tr->version unless $tr_id =~ /\.\d+$/; 

  if (defined(my $lrg_tr = $self->{cache}{$tr_id})) {

    return { FlagLRG => $lrg_tr };
  }

  return {};
}

1;

