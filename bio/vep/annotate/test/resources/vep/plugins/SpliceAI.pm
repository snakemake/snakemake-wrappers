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

 SpliceAI

=head1 SYNOPSIS

 mv SpliceAI.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin SpliceAI,snv=/path/to/spliceai_snv_.vcf.gz,
 indel=/path/to/spliceai_indel_.vcf.gz

=head1 DESCRIPTION

 A VEP plugin that retrieves pre-calculated annotations from SpliceAI.
 SpliceAI is a deep neural network, developed by Illumina, Inc 
 that predicts splice junctions from an arbitrary pre-mRNA transcript sequence.

 Delta score of a variant, defined as the maximum of (DS_AG, DS_AL, DS_DG, DS_DL), 
 ranges from 0 to 1 and can be interpreted as the probability of the variant being 
 splice-altering. The author-suggested cutoffs are:
   0.2 (high recall)
   0.5 (recommended)
   0.8 (high precision)

 This plugin is available for both GRCh37 and GRCh38.

 More information can be found at:
 https://pypi.org/project/spliceai/

 Please cite the SpliceAI publication alongside VEP if you use this resource:
 https://www.ncbi.nlm.nih.gov/pubmed/30661751

 Running options:
 (Option 1) By default, this plugin appends all scores from SpliceAI files.
 (Option 2) Besides the pre-calculated scores, it can also be specified a score
 cutoff between 0 and 1.

 Output: 
 The output includes the gene symbol, delta scores (DS) and delta positions (DP)
 for acceptor gain (AG), acceptor loss (AL), donor gain (DG), and donor loss (DL).

 For tab and JSON the output contains one header 'SpliceAI_pred' with all
 the delta scores and positions. The format is:
   SYMBOL|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL

 For VCF output the delta scores and positions are stored in different headers.
 The values are 'SpliceAI_pred_xx' being 'xx' the score/position.
   Example: 'SpliceAI_pred_DS_AG' is the delta score for acceptor gain.

 If plugin is run with option 2, the output also contains a flag: 'PASS' if delta score
 passes the cutoff, 'FAIL' otherwise. 

 The following steps are necessary before running this plugin:

 The files with the annotations for all possible substitutions (snv), 1 base insertions 
 and 1-4 base deletions (indel) within genes are available here:
 https://basespace.illumina.com/analyses/194103939/files?projectId=66029966

 GRCh37:
 tabix -p vcf spliceai_scores.raw.snv.hg37.vcf.gz
 tabix -p vcf spliceai_scores.raw.indel.hg37.vcf.gz

 GRCh38:
 tabix -p vcf spliceai_scores.raw.snv.hg38.vcf.gz
 tabix -p vcf spliceai_scores.raw.indel.hg38.vcf.gz

 The plugin can then be run:
 ./vep -i variations.vcf --plugin SpliceAI,snv=/path/to/spliceai_scores.raw.snv.hg38.vcf.gz,
 indel=/path/to/spliceai_scores.raw.indel.hg38.vcf.gz
 ./vep -i variations.vcf --plugin SpliceAI,snv=/path/to/spliceai_scores.raw.snv.hg38.vcf.gz,
 indel=/path/to/spliceai_scores.raw.indel.hg38.vcf.gz,cutoff=0.5


=cut

package SpliceAI;

use strict;
use warnings;
use List::Util qw(max);

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);
use Bio::EnsEMBL::Variation::Utils::Sequence qw(get_matched_variant_alleles);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;
use Bio::EnsEMBL::Variation::VariationFeature;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

my $output_vcf;

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  my $param_hash = $self->params_to_hash();

  die("ERROR: SpliceAI files not provided or not found!\n") unless defined($param_hash->{snv}) && defined($param_hash->{indel}) && -e $param_hash->{snv} && -e $param_hash->{indel};

  $self->add_file($param_hash->{snv});
  $self->add_file($param_hash->{indel});

  if(defined($param_hash->{cutoff})) {
    my $cutoff = $param_hash->{cutoff};
    if($cutoff < 0 || $cutoff > 1) {
      die("ERROR: Cutoff score must be between 0 and 1!\n");
    }
    $self->{cutoff} = $cutoff;
  }

  if($self->{config}->{output_format} eq "vcf") {
    $output_vcf = 1;
  }

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  my $self = shift;

  my %header;

  if($output_vcf) {
    $header{'SpliceAI_pred_SYMBOL'} = 'SpliceAI gene symbol';
    $header{'SpliceAI_pred_DS_AG'} = 'SpliceAI predicted effect on splicing. Delta score for acceptor gain';
    $header{'SpliceAI_pred_DS_AL'} = 'SpliceAI predicted effect on splicing. Delta score for acceptor loss';
    $header{'SpliceAI_pred_DS_DG'} = 'SpliceAI predicted effect on splicing. Delta score for donor gain';
    $header{'SpliceAI_pred_DS_DL'} = 'SpliceAI predicted effect on splicing. Delta score for donor loss';
    $header{'SpliceAI_pred_DP_AG'} = 'SpliceAI predicted effect on splicing. Delta position for acceptor gain';
    $header{'SpliceAI_pred_DP_AL'} = 'SpliceAI predicted effect on splicing. Delta position for acceptor loss';
    $header{'SpliceAI_pred_DP_DG'} = 'SpliceAI predicted effect on splicing. Delta position for donor gain';
    $header{'SpliceAI_pred_DP_DL'} = 'SpliceAI predicted effect on splicing. Delta position for donor loss';
  }

  else {
    $header{'SpliceAI_pred'} = 'SpliceAI predicted effect on splicing. These include delta scores (DS) and delta positions (DP) for acceptor gain (AG), acceptor loss (AL), donor gain (DG), and donor loss (DL). Format: SYMBOL|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL';
  }

  if($self->{cutoff}) {
    $header{'SpliceAI_cutoff'} = 'Flag if delta score pass the cutoff (PASS) or if it does not (FAIL)';
  }

  return \%header;
}

sub run {
  my ($self, $tva) = @_;
  my $vf = $tva->variation_feature;
  my $chr = $vf->{chr};

  my $end = $vf->{end};
  my $start = $vf->{start};
  ($start, $end) = ($end, $start) if $start > $end;

  my @data = @{$self->get_data($chr, $start, $end)} if(defined $chr);

  return {} unless(@data);

  my $result_data = '';
  my $result_flag;

  foreach my $data_value (@data) {

    my $ref_allele;
    my $alt_allele;

    # get alt allele
    my $allele = $tva->variation_feature_seq;
    reverse_comp(\$allele) if $vf->{strand} < 0;
    my $new_allele_string = $vf->ref_allele_string.'/'.$allele;

    if($vf->ref_allele_string =~ /-/) {

      # convert to vcf format to compare the alt alleles
      my $vf_2 = Bio::EnsEMBL::Variation::VariationFeature->new
        (-start => $start,
         -end => $end,
         -strand => $vf->{strand},
         -allele_string => $new_allele_string
        );
      my $convert_to_vcf = $vf_2->to_VCF_record;
      $ref_allele = ${$convert_to_vcf}[3];
      $alt_allele = ${$convert_to_vcf}[4];
    }
    else {
      $ref_allele = $vf->ref_allele_string;
      $alt_allele = $allele;
    }

    my $matches = get_matched_variant_alleles(
      {
        ref    => $ref_allele,
        alts   => [$alt_allele],
        pos    => $start,
        strand => $vf->strand
      },
      {
       ref  => $data_value->{ref},
       alts => [$data_value->{alt}],
       pos  => $data_value->{start},
      }
    );
    if (@$matches) {

      my %hash;

      if($output_vcf) {
        my @data_values = split /\|/, $data_value->{result};
        $hash{'SpliceAI_pred_SYMBOL'} = $data_values[0];
        $hash{'SpliceAI_pred_DS_AG'} = $data_values[1];
        $hash{'SpliceAI_pred_DS_AL'} = $data_values[2];
        $hash{'SpliceAI_pred_DS_DG'} = $data_values[3];
        $hash{'SpliceAI_pred_DS_DL'} = $data_values[4];
        $hash{'SpliceAI_pred_DP_AG'} = $data_values[5];
        $hash{'SpliceAI_pred_DP_AL'} = $data_values[6];
        $hash{'SpliceAI_pred_DP_DG'} = $data_values[7];
        $hash{'SpliceAI_pred_DP_DL'} = $data_values[8];
      }

      else {
        $hash{'SpliceAI_pred'} = $data_value->{result};
      }

      # Add a flag if cutoff is used
      if($self->{cutoff}) {
        if($data_value->{info} >= $self->{cutoff}) {
          $result_flag = 'PASS';
        }
        else {
          $result_flag = 'FAIL';
        }
        $hash{'SpliceAI_cutoff'} = $result_flag;
      }

      return \%hash;
    }
  }

  return {};
}

# Parse data from SpliceAI file
sub parse_data {
  my ($self, $line) = @_;

  my ($chr, $start, $id, $ref, $alt, $qual, $filter, $info) = split /\t/, $line;

  $info =~ s/SpliceAI=//;
  my @info_splited = split (qr/\|/,$info, 2);
  my $allele = $info_splited[0];
  my $data = $info_splited[1];

  my $max_score;
  if($self->{cutoff}){
    my @scores = split (qr/\|/,$data);
    my @scores_list = @scores[1..4];
    $max_score = max(@scores_list);
  }

  return {
    chr    => $chr,
    start  => $start,
    ref    => $ref,
    alt    => $alt,
    info   => $max_score,
    result => $data,
  };
}

1;