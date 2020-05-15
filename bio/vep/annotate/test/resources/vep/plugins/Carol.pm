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

 Carol

=head1 SYNOPSIS

 mv Carol.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin Carol

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that calculates
 the Combined Annotation scoRing toOL (CAROL) score (1) for a missense mutation 
 based on the pre-calculated SIFT (2) and PolyPhen-2 (3) scores from the Ensembl 
 API (4). It adds one new entry class to the VEP's Extra column, CAROL which is
 the calculated CAROL score. Note that this module is a perl reimplementation of 
 the original R script, available at:

 http://www.sanger.ac.uk/resources/software/carol/

 I believe that both versions implement the same algorithm, but if there are any
 discrepancies the R version should be treated as the reference implementation. 
 Bug reports are welcome.

 References:

 (1) Lopes MC, Joyce C, Ritchie GRS, John SL, Cunningham F, Asimit J, Zeggini E. 
     A combined functional annotation score for non-synonymous variants
     Human Heredity (in press)

 (2) Kumar P, Henikoff S, Ng PC.
     Predicting the effects of coding non-synonymous variants on protein function using the SIFT algorithm
     Nature Protocols 4(8):1073-1081 (2009)
     doi:10.1038/nprot.2009.86
 
 (3) Adzhubei IA, Schmidt S, Peshkin L, Ramensky VE, Gerasimova A, Bork P, Kondrashov AS, Sunyaev SR. 
     A method and server for predicting damaging missense mutations
     Nature Methods 7(4):248-249 (2010)
     doi:10.1038/nmeth0410-248
 
 (4) Flicek P, et al.
     Ensembl 2012
     Nucleic Acids Research (2011)
     doi: 10.1093/nar/gkr991

=cut

package Carol;

use strict;
use warnings;

use Math::CDF qw(pnorm qnorm);

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

my $CAROL_CUTOFF = 0.98;

sub version {
    return '2.3';
}

sub feature_types {
    return ['Transcript'];
}

sub get_header_info {
    return {
        CAROL => "Combined Annotation scoRing toOL prediction",
    };
}

sub run {
    my ($self, $tva) = @_;
    
    my $pph_pred    = $tva->polyphen_prediction;
    my $pph_score   = $pph_pred ? ($pph_pred eq 'unknown' ? undef: $tva->polyphen_score) : undef;
    my $sift_score  = $tva->sift_score;

    my ($carol_pred, $carol_score) = compute_carol($pph_score, $sift_score);
    
    my $results = {};

    if (defined $carol_pred) {

        $carol_score = sprintf "%.3f", $carol_score;

        my $result = "$carol_pred($carol_score)";

        if (@{ $self->params } > 0) {
            $result = $carol_pred if ($self->params->[0] =~ /^p/i);
            $result = $carol_score if ($self->params->[0] =~ /^s/i);
        }

        $results = {
            CAROL => $result,
        };
    }
    
    return $results;
}

sub compute_carol {

    my ($pph_score, $sift_score) = @_;
    
    my $carol_score;

    if (defined $pph_score) {
        $pph_score = 0.999 if $pph_score == 1;
        $pph_score = 0.0001 if $pph_score == 0;
    }

    if (defined $sift_score) {
        $sift_score = 1 - $sift_score;
        $sift_score = 0.999 if $sift_score == 1;
        $sift_score = 0.0001 if $sift_score == 0;
    }

    if (defined $pph_score && defined $sift_score) {
        
        my $pph_weight  = log(1/(1-$pph_score));
        my $sift_weight = log(1/(1-$sift_score));
       
        # we take -qnorm, because the R script uses qnorm(..., lower.tail = FALSE)

        my $pph_z   = -qnorm($pph_score);
        my $sift_z  = -qnorm($sift_score);
        
        my $numerator   = ($pph_weight * $pph_z) + ($sift_weight * $sift_z);
        my $denominator = sqrt( ($pph_weight ** 2) + ($sift_weight ** 2) );

        # likewise we take 1 - pnorm

        $carol_score = 1 - pnorm($numerator / $denominator);
    }
    elsif (defined $pph_score) {
        $carol_score = $pph_score;
    }
    else {
        $carol_score = $sift_score;
    }

    if (defined $carol_score) {
        my $carol_pred = $carol_score < $CAROL_CUTOFF ? 'Neutral' : 'Deleterious';
        return ($carol_pred, $carol_score);
    }
    else {
        return undef;
    }
}

1;

