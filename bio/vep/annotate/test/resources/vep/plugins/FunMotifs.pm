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

 FunMotifs

=head1 SYNOPSIS

 mv FunMotifs.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin FunMotifs,/path/to/funmotifs/all_tissues.bed.gz,uterus
 ./vep -i variations.vcf --plugin FunMotifs,/path/to/funmotifs/blood.funmotifs_sorted.bed.gz,fscore,dnase_seq
 
 Parameters Required:
 
 [0] : FunMotifs BED file
 [1]+ : List of columns to include within VEP output (e.g. fscore, skin, contactingdomain)
 

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 adds tissue-specific transcription factor motifs from FunMotifs to VEP output.

 Please cite the FunMotifs publication alongside the VEP if you use this resource. 
 The preprint can be found at: https://www.biorxiv.org/content/10.1101/683722v1
 
 FunMotifs files can be downloaded from: http://bioinf.icm.uu.se:3838/funmotifs/
 At the time of writing, all BED files found through this link support GRCh37, 
 however other assemblies are supported by the plugin if an appropriate BED file
 is supplied.

 The tabix utility must be installed in your path to use this plugin.

=cut
package FunMotifs;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);


sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);
  
  die("Insufficient input parameters found for FunMotifs plugin\n") if(scalar(@{$self->params}) < 2);
  
  $self->expand_left(0);
  $self->expand_right(0);

  $self->get_user_params();

  my $file = $self->params->[0];

  ## -s 10000 tells bgzip to only decompress the first 10000 bytes of the file
  ## This should always be sufficient to obtain the headers from the input file
  ## The current header file is approxmiately 800 bytes long    
  my $headers = `bgzip -d -s 10000 $file | head -n 1`;

  if ($headers){
    my @array = split(/\t/,$headers);
    my @new_array = grep(s/\s*$//g, @array);
    $self->{headers} = \@new_array;
  }
  else{
    warn('Unable to find header information within ' . $file);
  }

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return { FunMotifs => 'Annotated Transcription Factor Motifs'};
}

sub run {
  my ($self, $tva) = @_;
  my $params = $self->params;
  
  if(scalar(@{$self->params}) < 1){
    return $self;
  }
  
  my $output_prefix = 'FM';
  
  my $vf = $tva->variation_feature;  
  my $end = $vf->{end};
  my $start = $vf->{start};
  ($start, $end) = ($end, $start) if $start > $end;
  my ($res) = @{$self->get_data($vf->{chr}, $start, $end)};

  shift @{$params} if ($params->[0] =~ /.gz/i); #Removes filename
  
  my %col_head_hash = map { $_ => 1 } @{$self->{headers}};
  my $col_head_hashref = \%col_head_hash;
  my $output_hash = {};

  foreach my $para(@$params)
  {
      $output_hash->{$output_prefix . $para} = $res->{$para} if ($col_head_hashref->{$para} && defined($res->{$para}));
  } 

  return $output_hash;
}

sub parse_data {
  my ($self, $line) = @_;
  my %output_hash;
  @output_hash{@{$self->{headers}}} = split(/\t/,$line);
  return \%output_hash;
}


sub get_start {
  return $_[1]->{start};
}

sub get_end {
  return $_[1]->{end};
}

1;
