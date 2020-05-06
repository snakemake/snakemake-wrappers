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

  GXA

=head1 SYNOPSIS

  mv GXA.pm ~/.vep/Plugins
  ./vep -i variations.vcf --cache --plugin GXA

=head1 DESCRIPTION

  This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
  reports data from the Gene Expression Atlas.

  NB: no account is taken for comparing values across experiments; if values
  exist for the same tissue in more than one experiment, the highest value
  is reported.

=cut

package GXA;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);

  die("ERROR: This plugin is currently non-functional due to changes in the Gene Expression Atlas API");
  
  $self->{species} =  $self->{config}->{species};
  $self->{species} =~ s/\_/\%20/;
  
  $self->{url} = 'https://www.ebi.ac.uk/gxa/widgets/heatmap/multiExperiment.tsv?propertyType=bioentity_identifier';
  
  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub variant_feature_types {
  return ['BaseVariationFeature'];
}

sub get_header_info {
  my $self = shift;
  
  if(!exists($self->{_header_info})) {
    
    # get tissues using BRCA2
    my $url = sprintf(
      '%s&species=%s&geneQuery=%s',
      $self->{url},
      $self->{species},
      'BRCA2'
    );
    
    open IN, "curl -s \"$url\" |";
    my @lines = <IN>;
    
    my %headers = ();
    
    while(my $line = shift @lines) {
      next if $line =~ /^#/;
      chomp $line;
      $line =~ s/ /\_/g;
      %headers = map {'GXA_'.$_ => "Tissue expression level in $_ from Gene Expression Atlas"} (split /\t/, $line);
      last;
    }
    
    close IN;
    
    $self->{_header_info} = \%headers;
  };
  
  return $self->{_header_info};
}

sub run {
  my ($self, $tva) = @_;
  
  my $tr = $tva->transcript;
  my $gene_id = $tr->{_gene_stable_id} || $tr->{_gene}->stable_id;
  return {} unless $gene_id;
  
  if(!exists($self->{_cache}) || !exists($self->{_cache}->{$gene_id})) {
    
    my $url = sprintf(
      '%s&species=%s&geneQuery=%s',
      $self->{url},
      $self->{species},
      $gene_id
    );
    
    open IN, "curl -s \"$url\" |";
    
    my $first = 1;
    my (@headers, %data);
    
    while(<IN>) {
      next if /^#/;
      chomp;
            
      if($first) {
        s/ /\_/g;
        @headers = split /\t/, $_;
        $first = 0;
      }
      else {
        my @tmp = split /\t/, $_;
        
        for(my $i=0; $i<=$#headers; $i++) {
          my ($h, $d) = ('GXA_'.$headers[$i], $tmp[$i]);
          next unless defined($d) && $d =~ /^[0-9\.]+$/;
          
          if(exists($data{$h})) {
            $data{$h} = $d if $d > $data{$h};
          }
          else {
            $data{$h} = $d;
          }
        }
      }
    }
    
    close IN;
    
    $self->{_cache}->{$gene_id} = \%data;
  }
  
  return $self->{_cache}->{$gene_id};
}

1;
