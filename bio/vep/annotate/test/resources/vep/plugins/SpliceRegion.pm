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

 Ensembl <dev@ensembl.org>
  
=cut

=head1 NAME

 SpliceRegion

=head1 SYNOPSIS

 mv SpliceRegion.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin SpliceRegion
 
 To only show the additional consequence extended_intronic_splice_region_variant, use: 
 ./vep -i variations.vcf --plugin SpliceRegion,Extended

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 provides more granular predictions of splicing effects.

 Three additional terms may be added:

 # splice_donor_5th_base_variant : variant falls in the 5th base after the splice donor junction (5' end of intron)

             v
 ...EEEEEIIIIIIIIII...

 (E = exon, I = intron, v = variant location)

 # splice_donor_region_variant : variant falls in region between 3rd and 6th base after splice junction (5' end of intron)

           vv vvv
 ...EEEEEIIIIIIIIII...

 # splice_polypyrimidine_tract_variant : variant falls in polypyrimidine tract at 3' end of intron, between 17 and 3 bases from the end

      vvvvvvvvvvvvvvv
 ...IIIIIIIIIIIIIIIIIIIIEEEEE...


=cut

package SpliceRegion;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::VariationEffect qw(overlap);
use Bio::EnsEMBL::Variation::Utils::Constants qw(%OVERLAP_CONSEQUENCES);

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

my %TERM_RANK = (
  splice_donor_5th_base_variant => 1,
  splice_donor_region_variant => 2,
  splice_polypyrimidine_tract_variant => 3,
  extended_intronic_splice_region_variant_5prime => 4,
  extended_intronic_splice_region_variant_3prime => 5,
);

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    SpliceRegion => "SpliceRegion predictions",
  };
}

sub run {
  my ($self, $tva) = @_;

  my $vf = $tva->variation_feature;
  my ($vf_start, $vf_end) = ($vf->{start}, $vf->{end});

  my $is_insertion = 0;
  if($vf_start > $vf_end) {
    ($vf_start, $vf_end) = ($vf_end, $vf_start);
    $is_insertion = 1;
  }

  my $tv = $tva->transcript_variation;
  my $tr = $tv->transcript;
  my $vf_tr_seq = $tva->feature_seq;

  # define some variables depending on transcript strand
  my ($strand_mod, $donor_coord, $acc_coord);
  if($tr->strand > 0) {
    $strand_mod = 1;
    $donor_coord = 'start';
    $acc_coord = 'end';
  }
  else {
    $strand_mod = -1;
    $donor_coord = 'end';
    $acc_coord = 'start';
  }

  my %results;

  my @terms;
  my $extended_flag = lc($self->params->[0] || "") eq 'extended';
  for my $intron(@{$tv->_overlapped_introns($vf_start, $vf_end)}) {

    # define terms to check for and their regions
    @terms = (
      {
        term => 'splice_donor_5th_base_variant',
        region => [$intron->{$donor_coord} + (4 * $strand_mod), $intron->{$donor_coord} + (4 * $strand_mod)]
      },
      {
        term => 'splice_donor_region_variant',
        region => [$intron->{$donor_coord} + (2 * $strand_mod), $intron->{$donor_coord} + (5 * $strand_mod)]
      },
      {
        term => 'splice_polypyrimidine_tract_variant',
        region => [$intron->{$acc_coord} + (-16 * $strand_mod), $intron->{$acc_coord} + (-2 * $strand_mod)],
        # allele_specific_mod => {
        #   A => '_to_purine',
        #   G => '_to_purine',
        # }
      },
    ) unless $extended_flag;
    
    @terms = (
      {
        term => 'extended_intronic_splice_region_variant_5prime',
        region => [$intron->{$donor_coord}, $intron->{$donor_coord} + (9 * $strand_mod)]
      },
      {
        term => 'extended_intronic_splice_region_variant_3prime',
        region => [$intron->{$acc_coord} + (-9 * $strand_mod), $intron->{$acc_coord} ],
        # allele_specific_mod => {
        #   A => '_to_purine',
        #   G => '_to_purine',
        # }
      },
    ) if $extended_flag;
    

    foreach my $term_hash(@terms) {
      my $pass = overlap($vf_start, $vf_end, sort {$a <=> $b} @{$term_hash->{region}});
      if($pass) {
        my $term = $term_hash->{term};
        $term = 'extended_intronic_splice_region_variant' if $extended_flag;

        # if(my $allele_specific_mods = $term_hash->{allele_specific_mod}) {
        #   $term .= $allele_specific_mods->{$vf_tr_seq} || '';
        # }

        $results{$term}++;
        last;
      }
    }
  }

  return {} unless %results;

  return { SpliceRegion => [sort {$TERM_RANK{$a} <=> $TERM_RANK{$b}} keys %results]};
}

1;

