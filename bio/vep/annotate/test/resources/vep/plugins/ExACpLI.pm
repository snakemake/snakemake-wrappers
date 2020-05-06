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

 Please email comments or questions to the public Ensembl
 developers list at <http://lists.ensembl.org/mailman/listinfo/dev>.

 Questions may also be sent to the Ensembl help desk at
 <http://www.ensembl.org/Help/Contact>.

=cut

=head1 NAME

ExACpLI - Add ExAC pLI to the VEP output 

=head1 SYNOPSIS

  mv ExACpLI.pm ~/.vep/Plugins
  mv ExACpLI_values.txt ~/.vep/Plugins
  ./vep -i variants.vcf --plugin ExACpLI

=head1 DESCRIPTION


  A VEP plugin that adds the probabililty of a gene being 
  loss-of-function intolerant (pLI) to the VEP output.
  
  Lek et al. (2016) estimated pLI using the expectation-maximization 
  (EM) algorithm and data from 60,706 individuals from 
  ExAC (http://exac.broadinstitute.org/about). The closer pLI is to 1, 
  the more likely the gene is loss-of-function (LoF) intolerant. 
  
  Note: the pLI was calculated using a representative transcript and
  is reported by gene in the plugin.

  The data for the plugin is provided by Kaitlin Samocha and Daniel MacArthur. 
  See https://www.ncbi.nlm.nih.gov/pubmed/27535533 for a description 
  of the dataset and analysis.

  The ExACpLI_values.txt file is found alongside the plugin in the 
  VEP_plugins GitHub repository. The file contains the fields gene and pLI 
  extracted from the file at 
    
    ftp://ftp.broadinstitute.org/pub/ExAC_release/release0.3/functional_gene_constraint/
      fordist_cleaned_exac_r03_march16_z_pli_rec_null_data.txt

  To use another values file, add it as a parameter i.e.

     ./vep -i variants.vcf --plugin ExACpLI,values_file.txt


=cut

package ExACpLI;

use strict;
use warnings;

use DBI;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);
  
  my $file = $self->params->[0];

  if(!$file) {
    my $plugin_dir = $INC{'ExACpLI.pm'};
    $plugin_dir =~ s/ExACpLI\.pm//i;
    $file = $plugin_dir.'/ExACpLI_values.txt';
  }
  
  die("ERROR: ExACpLI values file $file not found\n") unless $file && -e $file;
  
  open my $fh, "<",  $file;
  my %scores;
  
  while(<$fh>) {
    chomp;
    my ($gene, $score) = split;
    next if $score eq 'pLI';
    $scores{lc($gene)} = sprintf("%.2f", $score);
  }
  
  close $fh;
  
  die("ERROR: No scores read from $file\n") unless scalar keys %scores;
  
  $self->{scores} = \%scores;
  
  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    ExACpLI => "ExACpLI value for gene"
  };
}

sub run {
  my $self = shift;
  my $tva = shift;
  
  my $symbol = $tva->transcript->{_gene_symbol} || $tva->transcript->{_gene_hgnc};
  return {} unless $symbol;
  
  return $self->{scores}->{lc($symbol)} ? { ExACpLI => $self->{scores}->{lc($symbol)}} : {};
}

1;

