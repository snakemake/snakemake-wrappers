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

 ReferenceQuality

=head1 SYNOPSIS

 mv ReferenceQuality.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin ReferenceQuality,/path/to/data.gff3.gz

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 reports on the quality of the reference genome using GRC data at the location of your variants.
 More information can be found at: https://www.ncbi.nlm.nih.gov/grc/human/issues

 The following steps are necessary before running this plugin:
 
 GRCh38:
 
 Download
 ftp://ftp.ncbi.nlm.nih.gov/pub/grc/human/GRC/GRCh38/MISC/annotated_clone_assembly_problems_GCF_000001405.38.gff3
 ftp://ftp.ncbi.nlm.nih.gov/pub/grc/human/GRC/Issue_Mapping/GRCh38.p12_issues.gff3
 
 cat annotated_clone_assembly_problems_GCF_000001405.38.gff3 GRCh38.p12_issues.gff3 > GRCh38_quality_mergedfile.gff3
 sort -k 1,1 -k 4,4n -k 5,5n GRCh38_quality_mergedfile.gff3 > sorted_GRCh38_quality_mergedfile.gff3
 bgzip sorted_GRCh38_quality_mergedfile.gff3
 tabix -p gff sorted_GRCh38_quality_mergedfile.gff3.gz

 The plugin can then be run with:
 ./vep -i variations.vcf --plugin ReferenceQuality,sorted_GRCh38_quality_mergedfile.gff3.gz
  
 GRCh37:
 
 Download
 ftp://ftp.ncbi.nlm.nih.gov/pub/grc/human/GRC/GRCh37/MISC/annotated_clone_assembly_problems_GCF_000001405.25.gff3
 ftp://ftp.ncbi.nlm.nih.gov/pub/grc/human/GRC/Issue_Mapping/GRCh37.p13_issues.gff3
 
 cat annotated_clone_assembly_problems_GCF_000001405.25.gff3 GRCh37.p13_issues.gff3 > GRCh37_quality_mergedfile.gff3
 sort -k 1,1 -k 4,4n -k 5,5n GRCh37_quality_mergedfile.gff3 > sorted_GRCh37_quality_mergedfile.gff3
 bgzip sorted_GRCh37_quality_mergedfile.gff3
 tabix -p gff sorted_GRCh37_quality_mergedfile.gff3.gz
 
 The plugin can then be run with:
 ./vep -i variations.vcf --plugin ReferenceQuality,sorted_GRCh37_quality_mergedfile.gff3.gz
 
 

 The tabix utility must be installed in your path to use this plugin.

=cut

package ReferenceQuality;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  $self->get_user_params();
    

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return { ReferenceQuality => 'Indicates quality of reference genome at input position - https://www.ncbi.nlm.nih.gov/grc/human/issues'};
}

sub run {
  my ($self, $tva) = @_;
    
  my $vf = $tva->variation_feature;
  my $allele = $tva->variation_feature_seq;
  my $chr = $vf->{chr};

  my $chr_syn;
  my @new_chr_array;
  my $new_chr;
  
  $self->parse_chromosome_synonyms($self->config->{'synonyms'}) if $self->config->{cache} && (not defined($self->{config}->{_chromosome_synonyms}));
  
  if(defined($self->{syn_cache}->{$chr}))
  {
    $new_chr = $self->{syn_cache}->{$chr};
  }
  else
  {
    #The NC_ chromosome synonym is found differently if we have database access
    if($self->config->{database})
    {
      my $srs_adaptor = $vf->slice->adaptor->db->get_SeqRegionSynonymAdaptor();
      $chr_syn = $srs_adaptor->get_synonyms( $vf->slice->get_seq_region_id($vf->slice) );
      @new_chr_array = map {$_->{name}} (grep {$_->{name} =~ 'NC_'} @{$chr_syn});
    }
    elsif($self->config->{cache})
    {
      $chr_syn = $self->config->{_chromosome_synonyms}->{($vf->{chr})};
      @new_chr_array = grep(/NC_/, keys %{$chr_syn});
      if (! @new_chr_array && ($vf->{chr} =~ /^chr/)) {
        my $tmp_chr = $vf->{chr};
        $tmp_chr =~ s/^chr//i;
        $chr_syn = $self->config->{_chromosome_synonyms}->{$tmp_chr};
        @new_chr_array = grep(/NC_/, keys %{$chr_syn});
      }
    }

    return {} unless scalar(@new_chr_array);
    $new_chr = shift(@new_chr_array);
    $self->{syn_cache}->{$chr} = $new_chr;
  }
  my $end = $vf->{end};
  my $start = $vf->{start};
  ($start, $end) = ($end, $start) if $start > $end;
  
  my @data = @{$self->get_data($new_chr, $start, $end)};

  #In case of multiple issue reports, we combine the output hashes
  my $combined_result_hash = {};
  my $counter = 1;
  foreach my $result (@data)
  {
    if($result->{result}){
      my $single_result_hash = {split /[;=]/, $result->{result}};
      if ((not defined($single_result_hash->{status})) || (defined($single_result_hash->{status}) && $single_result_hash->{status} ne 'Resolved'))
      {
        delete($single_result_hash->{chr});
        delete($single_result_hash->{status});
        delete($single_result_hash->{affectVersion});
        delete($single_result_hash->{fixVersion});
        $single_result_hash = {map { +"ReferenceQuality_Issue$counter\_$_" => $single_result_hash->{$_} } keys %$single_result_hash};
        $combined_result_hash = {%$combined_result_hash, %$single_result_hash};
        $counter++;
      }
    }
  }
  
  return $combined_result_hash unless $self->config->{vcf} || $self->config->{tab};
  
  #If VCF or Tab format, combine into one string
  my @sorted_keys = sort(keys %{$combined_result_hash});
  my $single_result_string = "";
  my $separator = "~";
  foreach my $key (@sorted_keys){
    $single_result_string .= $key . "=" .$combined_result_hash->{$key} . $separator;
  }
  chop($single_result_string);
  return { "ReferenceQuality" => $single_result_string};
}

sub parse_data {
  my ($self, $line) = @_;

  my ($c, $grc, $feat, $s, $e, $n, $str, $n2, $note) = split /\t/, $line;

  return {
    start => $s,
    end => $e,
    result => $note,
  };
}

sub get_start {
  return $_[1]->{start};
}

sub get_end {
  return $_[1]->{end};
}

sub parse_chromosome_synonyms {
  my $self = shift;
  my $file = shift;

  if($file) {
    open IN, $file or throw("ERROR: Could not read synonyms file $file: $!");

    my $synonyms = $self->config->{_chromosome_synonyms} ||= {};

    while(<IN>) {
      chomp;
      my @split = split(/\s+/, $_);

      my $ref = shift @split;

      foreach my $syn(@split) {
        $synonyms->{$ref}->{$syn} = 1;
        $synonyms->{$syn}->{$ref} = 1;
      }
    }

    close IN;
  }

  return $self->config->{_chromosome_synonyms} ||= {};
}

1;
