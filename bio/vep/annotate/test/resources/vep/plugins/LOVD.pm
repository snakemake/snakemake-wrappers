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

 LOVD

=head1 SYNOPSIS

 mv LOVD.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin LOVD

=head1 DESCRIPTION

 A VEP plugin that retrieves LOVD variation data from http://www.lovd.nl/.
 
 Please be aware that LOVD is a public resource of curated variants, therefore
 please respect this resource and avoid intensive querying of their databases
 using this plugin, as it will impact the availability of this resource for
 others.

=cut

package LOVD;

use strict;
use warnings;
use LWP::UserAgent;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub version {
    return '2.5';
}

sub feature_types {
    return ['Transcript'];
}

sub get_header_info {
    return {
        LOVD => "LOVD variant ID",
    };
}

sub run {
    my ($self, $tva) = @_;
    
    $self->{has_cache} = 1;

    my %hg_assembly = ( 'grch37' => 'hg19', 'grch38' => 'hg38' );
    my $assembly = lc($self->{config}->{assembly});

    # only works on human
    die("ERROR: LOVD plugin works only on human data") unless $self->{config}->{species} =~ /human|homo/i;
    
    # only work on 2 human assemblies
    die("ERROR: LOVD plugin works only on human assemblies ".join(' and ', keys(%hg_assembly))) unless $hg_assembly{$assembly};

    # get the VF object
    my $vf = $tva->variation_feature;
    return {} unless defined $vf;
    
    # set up a LWP UserAgent
    my $ua = LWP::UserAgent->new;
    $ua->env_proxy;

    my $chr = $vf->{chr};
    $chr =~ s/^chr//;
    
    my $locus = sprintf('chr%s:%s_%s', $chr, $vf->{start}, $vf->{end});
    
    my $data;
    
    # check the cache
    if(!exists($self->{lovd_cache}->{$locus})) {
        
        # construct a LOVD URL
        my $url = sprintf('http://www.lovd.nl/search.php?build=%s&position=%s', $hg_assembly{$assembly}, $locus);
        
        # get the accession (only need the head to get the redirect URL that contains the accession)
        my $response = $ua->get($url);
        
        if($response->is_success) {
            
            # parse the data into a hash
            for(grep {$_ !~ /hg_build/} split /\cJ/, $response->decoded_content) {
                s/\"//g;
                
                my ($build, $pos, $gene, $acc, $dna, $url) = split /\t/;
                
                $data = join(',', $gene, $acc, $dna)
            }
            
            $self->{lovd_cache}->{$locus} = $data;
        }
    }
    else {
        $data = $self->{lovd_cache}->{$locus};
    }
    
    return $data ? { LOVD => $data } : {};
}

1;

