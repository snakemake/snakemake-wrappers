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

 LoFtool

=head1 SYNOPSIS

  mv LoFtool.pm ~/.vep/Plugins
  mv LoFtool_scores.txt ~/.vep/Plugins
  ./vep -i variants.vcf --plugin LoFtool

=head1 DESCRIPTION

  Add LoFtool scores to the VEP output.

  LoFtool provides a rank of genic intolerance and consequent
  susceptibility to disease based on the ratio of Loss-of-function (LoF)
  to synonymous mutations for each gene in 60,706 individuals from ExAC,
  adjusting for the gene de novo mutation rate and evolutionary protein
  conservation. The lower the LoFtool gene score percentile the most
  intolerant is the gene to functional variation. For more details please see
  (Fadista J et al. 2017), PMID:27563026.
  The authors would like to thank the Exome Aggregation Consortium and
  the groups that provided exome variant data for comparison. A full
  list of contributing groups can be found at http://exac.broadinstitute.org/about.

  The LoFtool_scores.txt file is found alongside the plugin in the
  VEP_plugins GitHub repo.

  To use another scores file, add it as a parameter i.e.

  ./vep -i variants.vcf --plugin LoFtool,scores_file.txt

=cut

package LoFtool;

use strict;
use warnings;

use DBI;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);
  
  my $file = $self->params->[0];

  if(!$file) {
    my $plugin_dir = $INC{'LoFtool.pm'};
    $plugin_dir =~ s/LoFtool\.pm//i;
    $file = $plugin_dir.'/LoFtool_scores.txt';
  }
  
  die("ERROR: LoFtool scores file $file not found\n") unless $file && -e $file;
  
  open IN, $file;
  my %scores;
  
  while(<IN>) {
    chomp;
    my ($gene, $score) = split;
    next if !defined($score) || $score eq 'LoFtool_percentile';
    $scores{lc($gene)} = sprintf("%g", $score);
  }
  
  close IN;
  
  die("ERROR: No scores read from $file\n") unless scalar keys %scores;
  
  $self->{scores} = \%scores;
  
  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    LoFtool => "LoFtool score for gene"
  };
}

sub run {
  my $self = shift;
  my $tva = shift;
  
  my $symbol = $tva->transcript->{_gene_symbol} || $tva->transcript->{_gene_hgnc};
  return {} unless $symbol;
  
  return $self->{scores}->{lc($symbol)} ? { LoFtool => $self->{scores}->{lc($symbol)}} : {};
}

1;

