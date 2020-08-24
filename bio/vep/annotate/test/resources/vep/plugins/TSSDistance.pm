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

 TSSDistance

=head1 SYNOPSIS

 mv TSSDistance.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin TSSDistance

=head1 DESCRIPTION

 A VEP plugin that calculates the distance from the transcription
 start site for upstream variants.

=cut

package TSSDistance;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub get_header_info {
    return {
        TSSDistance => "Distance from the transcription start site"
    };
}

sub feature_types {
    return ['Transcript'];
}

sub variant_feature_types {
    return ['BaseVariationFeature'];
}

sub run {
    my ($self, $tva) = @_;

    my $t = $tva->transcript;
    my $vf = $tva->base_variation_feature;

    my $dist;

    if ($t->strand == 1) {
        $dist = $t->start - $vf->end;
    }
    else {
        $dist = $vf->start - $t->end;
    }

    if ($dist > 0) {
        return {
            TSSDistance => $dist,
        }
    }
    else {
        return {};
    }
}

1;
