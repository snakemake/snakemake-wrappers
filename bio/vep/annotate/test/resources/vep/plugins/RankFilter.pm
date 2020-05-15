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

 RankFilter

=head1 SYNOPSIS

 mv RankFilter.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin RankFilter,splice_region_variant

=head1 DESCRIPTION

 A VEP plugin filter that limits output of predictions to those ranked (by Ensembl)
 to be more severe (or at least as severe) as a user specified cutoff. The user can 
 specify either a numerical rank (lower ranks are assumed to be more severe) or an 
 SO term to use as the (inclusive) cutoff on the VEP command line. If a term is not 
 specified the default cutoff term used is 'splice_region_variant' (rank = 8). 
 
 For reference, the table of consequence terms at:

  http://www.ensembl.org/info/docs/variation/index.html#consequence_type_table

 is listed in descending order of severity, so you can refer to this table
 to pick your cutoff.

=cut

package RankFilter;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::Constants qw(%OVERLAP_CONSEQUENCES);

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepFilterPlugin);

sub new {
    my $class = shift;

    # call the superclass constructor

    my $self = $class->SUPER::new(@_);

    # use splice_region_variant as our default cutoff term

    my $term = $self->params->[0] || 'splice_region_variant';

    my $rank;

    if ($term =~ /^\d+$/) {
        
        # we allow the user to specify a numerical rank as 
        # well as a term
        
        $rank = $term;
    }
    elsif (my $oc = $OVERLAP_CONSEQUENCES{$term}) {
        
        # otherwise we look up the rank from the provided
        # SO consequence term

        $rank = $oc->rank;
    }
    else {
        die "Unable to find rank for consequence term: '$term'\n";
    }

    $self->{rank} = $rank;

    return $self;
}

sub feature_types {
    return ['Feature', 'Intergenic'];
}

sub include_line {
    my ($self, $tva) = @_;

    # check all the consequences in turn

    for my $oc (@{ $tva->get_all_OverlapConsequences }) {
        
        # and include this line if the rank of any of the 
        # consequences for this TVA is less than our cutoff 
        # (lower rank is assumed to be more deleterious)

        if ($oc->rank <= $self->{rank}) {
            return 1;
        }
    }

    return 0;
}

1;

