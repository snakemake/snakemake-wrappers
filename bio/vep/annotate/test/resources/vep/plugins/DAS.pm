=head1 LICENSE
                                                                                                                     
 Copyright (c) 1999-2015 The European Bioinformatics Institute and
 Genome Research Limited.  All rights reserved.                                                                      
                                                                                                                     
 This software is distributed under a modified Apache license.                                                       
 For license details, please see

   http://www.ensembl.org/info/about/code_licence.html                                                               
                                                                                                                     
=head1 CONTACT                                                                                                       

 Ensembl <http://www.ensembl.org/info/about/contact/index.html>
    
=cut

=head1 NAME

 DAS

=head1 SYNOPSIS

 mv DAS.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin DAS,<DAS_server>,<DAS_source>,<proxy>

=head1 DESCRIPTION

 A simple VEP plugin that checks for DAS features overlapping variants. Currently assumes that
 the assemblies match, and doesn't do any smart fetching of chunks of features (i.e. the plugin
 will query the DAS server once for every variant in the input file).

 You can run multiple instances of this plugin at the same time so you can query multiple DAS
 servers and sources. If you are querying multiple sources from the same server it is 
 convenient to store the server name in an environment variable to avoid specifying it
 multiple times, e.g.:

 export DAS="http://somewhere/das"
 ./vep -i variations.vcf --plugin DAS,$DAS,source1 --plugin DAS,$DAS,source2

 Requires the Bio::Das::Lite module from CPAN.

=cut

package DAS;

use strict;
use warnings;

use Bio::Das::Lite;
use Data::Dumper;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub get_header_info {
    my $self = shift;
    return {
        $self->header => $self->{source}." features from DAS server ".$self->{server},
    };
}

sub feature_types {
    return ['Transcript','RegulatoryFeature','MotifFeature','Intergenic'];
}

sub new {
    my $class = shift;
    
    my $self = $class->SUPER::new(@_);

    my ($server, $source, $proxy) = @{ $self->params };

    # strip off any trailing slash from the server URL
    $server =~ s/\/$//;

    $self->{das} = Bio::Das::Lite->new({
        timeout     => 10000,
        dsn         => "$server/$source",
        http_proxy  => $proxy,
    }) || die "Failed to connect to DAS source: $server/$source";

    $self->{source} = $source;
    $self->{server} = $server;

    return $self;
}

sub header {
    my $self = shift;
    return 'DAS_'.$self->{source};
}

sub run {
    my ($self, $vfoa) = @_;

    my $vf = $vfoa->variation_feature;

    my $segment = $vf->seq_region_name .':'.$vf->seq_region_start.','.$vf->seq_region_end;

    # cache the results on the variation feature, making sure the cache key is unique given
    # that there may be multiple DAS plugins running

    my $cache_key = '_vep_das_cache_'.$self->{server}.$self->{source};

    unless (exists $vf->{$cache_key}->{$segment}) {

        $vf->{$cache_key}->{$segment} = [];

        if (my $response = $self->{das}->features($segment)) {
            for my $url (keys %$response) {
                if (ref $response->{$url} eq 'ARRAY') { 
                    for my $feat (@{ $response->{$url} }) {
                        push @{ $vf->{$cache_key}->{$segment} }, $feat->{feature_label}.'('.$feat->{type}.')';
                    }
                }
            }
        }
    }
    
    my $res = join ',', @{ $vf->{$cache_key}->{$segment} };

    return $res ? {$self->header => $res} : {};
}

1;

