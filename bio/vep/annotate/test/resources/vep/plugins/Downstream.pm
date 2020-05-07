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

 Downstream

=head1 SYNOPSIS

 mv Downstream.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin Downstream

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 predicts the downstream effects of a frameshift variant on the protein
 sequence of a transcript. It provides the predicted downstream protein
 sequence (including any amino acids overlapped by the variant itself),
 and the change in length relative to the reference protein.
 
 Note that changes in splicing are not predicted - only the existing
 translateable (i.e. spliced) sequence is used as a source of
 translation. Any variants with a splice site consequence type are
 ignored.

 If VEP is run in offline mode using the flag --offline, a FASTA file is required.
 See: https://www.ensembl.org/info/docs/tools/vep/script/vep_cache.html#fasta
 Sequence may be incomplete without a FASTA file or database connection.

=cut

package Downstream;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;
use POSIX qw(ceil);

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub version {
    return '2.3';
}

sub feature_types {
    return ['Transcript'];
}

sub variant_feature_types {
    return ['VariationFeature'];
}

sub get_header_info {
    return {
        DownstreamProtein   => "Predicted downstream translation for frameshift mutations",
        ProteinLengthChange => "Predicted change in protein product length",
    };
}

sub run {
    my ($self, $tva) = @_;
    
    my @ocs = @{$tva->get_all_OverlapConsequences};
    
    if(grep {$_->SO_term eq 'frameshift_variant'} @ocs) {
        
        # can't do it for splice sites
        return {} if grep {$_->SO_term =~ /splice/} @ocs;
        
        my $tv = $tva->transcript_variation;
        my $tr = $tv->transcript;
        my $cds_seq = defined($tr->{_variation_effect_feature_cache}) ? $tr->{_variation_effect_feature_cache}->{translateable_seq} : $tr->translateable_seq;
        
        # get the sequence to translate
        my ($low_pos, $high_pos) = sort {$a <=> $b} ($tv->cds_start, $tv->cds_end);
        my $is_insertion         = $tv->cds_start > $tv->cds_end ? 1 : 0;
        my $last_complete_codon  = (ceil($low_pos / 3) - 1) * 3;
        my $before_var_seq       = substr $cds_seq, $last_complete_codon, $low_pos - $last_complete_codon - ($is_insertion ? 0 : 1);
        my $after_var_seq        = substr $cds_seq, $high_pos - ($is_insertion ? 1 : 0);
        my $to_translate         = $before_var_seq.$tva->feature_seq.$after_var_seq;
        my $three_prime_utr_seq  = $tr->three_prime_utr->seq() if ($tr->three_prime_utr);
        $to_translate            = $to_translate.$three_prime_utr_seq if ($three_prime_utr_seq);
        $to_translate            =~ s/\-//g;
        
        # create a bioperl object
        my $codon_seq = Bio::Seq->new(
          -seq      => $to_translate,
          -moltype  => 'dna',
          -alphabet => 'dna'
        );
        
        # get codon table
        my $codon_table;
        if(defined($tr->{_variation_effect_feature_cache})) {
            $codon_table = $tr->{_variation_effect_feature_cache}->{codon_table} || 1;
        }
        else {
            my ($attrib) = @{$tr->slice->get_all_Attributes('codon_table')};
            $codon_table = $attrib ? $attrib->value || 1 : 1;
        }
        
        # translate
        my $new_pep = $codon_seq->translate(undef, undef, undef, $codon_table)->seq();
        $new_pep =~ s/\*.*//;
        
        # compare lengths
        my $translation = defined($tr->{_variation_effect_feature_cache}) && defined($tr->{_variation_effect_feature_cache}->{peptide}) ? $tr->{_variation_effect_feature_cache}->{peptide} : $tr->translation->seq;
        my $new_length = ($tv->translation_start < $tv->translation_end ? $tv->translation_start : $tv->translation_end) + length($new_pep);
        
        return {
            DownstreamProtein   => $new_pep,
            ProteinLengthChange => $new_length - length($translation),
        };
    }

    return {};
}

1;

