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

 Condel

=head1 SYNOPSIS

 mv Condel.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin Condel,/path/to/config/Condel/config,b

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that calculates
 the Consensus Deleteriousness (Condel) score (1) for a missense mutation 
 based on the pre-calculated SIFT (2) and PolyPhen-2 (3) scores from the Ensembl 
 API (4). It adds one new entry class to the VEP's Extra column, Condel which is
 the calculated Condel score. This version of Condel was developed by the Biomedical Genomics Group 
 of the Universitat Pompeu Fabra, at the Barcelona Biomedical Research Park and available at
 (http://bg.upf.edu/condel) until April 2014. The code in this plugin is based on a script provided by this 
 group and slightly reformatted to fit into the Ensembl API.

 The plugin takes 3 command line arguments, the first is the path to a Condel 
 configuration directory which contains cutoffs and the distribution files etc., 
 the second is either "s", "p", or "b" to output the Condel score, prediction or 
 both (the default is both), and the third argument is either 1 or 2 to use the 
 original version of Condel (1), or the newer version (2) - 2 is the default and 
 is recommended to avoid false positive predictions from Condel in some 
 circumstances.

 An example Condel configuration file and a set of distribution files can be found 
 in the config/Condel directory in this repository. You should edit the 
 config/Condel/config/condel_SP.conf file and set the 'condel.dir' parameter to
 the full path to the location of the config/Condel directory on your system.

 References:

 (1) Gonzalez-Perez A, Lopez-Bigas N. 
     Improving the assessment of the outcome of non-synonymous SNVs with a Consensus deleteriousness score (Condel)
     Am J Hum Genet 88(4):440-449 (2011)
     doi:10.1016/j.ajhg.2011.03.004

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

package Condel;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub version {
    return '2.4';
}

sub feature_types {
    return ['Transcript'];
}

sub get_header_info {
    return {
        Condel => "Consensus deleteriousness score for an amino acid substitution based on SIFT and PolyPhen-2",
    };
}

sub new {
    my $class = shift;
    
    my $self = $class->SUPER::new(@_);

    # parse the config file and distribution files 

    my $config_dir = $self->params->[0];
    $self->{output} = $self->params->[1] || 'b';
    $self->{version} = $self->params->[2] || 2;

    # find config dir
    unless($config_dir && -d $config_dir) {
        $config_dir = $INC{'Condel.pm'};
        $config_dir =~ s/Condel\.pm/config\/Condel\/config/;
        die "ERROR: Unable to find Condel config path\n" unless -d $config_dir;
    }
    
    my $config_file = "$config_dir/condel_SP.conf";

    open(CONF, "<$config_file") || die "Could not open $config_file";

    my @conf = <CONF>;
    
    my $safe_conf = 0;
    
    for (my $i = 0; $i < @conf; $i++){
        if ($conf[$i] =~ /condel\.dir=\'(\S+)\'/){
            $self->{config}->{'condel.dir'} = $1;

            # user has not edited config, attempt to get correct dir
            if($self->{config}->{'condel.dir'} eq 'path/to/config/Condel/') {
                my $dir = $INC{'Condel.pm'};
                $dir =~ s/Condel\.pm/config\/Condel/;
                $self->{config}->{'condel.dir'} = $dir;
            }
            $safe_conf++ if -d $self->{config}->{'condel.dir'};
        }
        elsif ($conf[$i] =~ /(cutoff\.HumVar\.\w+)=\'(\S+)\'/){
            $self->{config}->{$1} = $2;
            $safe_conf++;
        }
        elsif ($conf[$i] =~ /(max\.HumVar\.\w+)=\'(\S+)\'/){
            $self->{config}->{$1} = $2;
            $safe_conf++;
        }
    }

    if ($safe_conf < 3){
        die "Malformed config file!!!\n\n";
    }

    open(SIFT, $self->{config}->{'condel.dir'}."/methdist/sift.data");
    my @sift = <SIFT>;
    close SIFT;

    for (my $i = 0; $i < @sift; $i++){
        if ($sift[$i] =~ /(\S+)\s+(\S+)\s+(\S+)/){
            $self->{sift}->{tp}->{$1} = $2;
            $self->{sift}->{tn}->{$1} = $3;
        }
    }

    open(POLYPHEN, $self->{config}->{'condel.dir'}."/methdist/polyphen.data");
    my @polyphen = <POLYPHEN>;
    close POLYPHEN;

    for (my $i = 0; $i < @polyphen; $i++){
        if ($polyphen[$i] =~ /(\S+)\s+(\S+)\s+(\S+)/){
            $self->{polyphen}->{tp}->{$1} = $2;
            $self->{polyphen}->{tn}->{$1} = $3;
        }
    }

    return $self;
}

sub run {
    my ($self, $tva) = @_;
    
    my $pph_score   = $tva->polyphen_score;
    my $pph_pred    = $tva->polyphen_prediction;
    my $sift_score  = $tva->sift_score;

    my $results = {};

    if (defined $pph_score && defined $sift_score && $pph_pred ne 'unknown') {

        my ($condel_pred, $condel_score) = $self->compute_condel($sift_score, $pph_score);

        $condel_score = sprintf "%.3f", $condel_score;
            
        my $output = "$condel_pred($condel_score)";
        
        $output = $condel_pred if ($self->{output} =~ /^p/);
        $output = $condel_score if ($self->{output} =~ /^s/);

        $results = {
            Condel => $output,
        };
    }

    return $results;
}

sub compute_condel {

    my ($self, $sift_score, $polyphen_score) = @_;

    my $USE_V2 = $self->{version} == 2;

    my $class;
    
    my $base = 0;
    my $int_score = 0;

    $sift_score     = sprintf("%.3f", $sift_score);
    $polyphen_score = sprintf("%.3f", $polyphen_score);
    
    if ($sift_score <= $self->{config}->{'cutoff.HumVar.sift'}){
        $int_score += sprintf("%.3f", (1 - $sift_score/$self->{config}->{'max.HumVar.sift'})*(1-$self->{sift}->{tn}->{$sift_score}));
        $base += $USE_V2 ? 1 : 1-$self->{sift}->{tn}->{$sift_score};
    }
    else {
        $int_score += sprintf("%.3f", (1 - $sift_score/$self->{config}->{'max.HumVar.sift'})*(1-$self->{sift}->{tp}->{$sift_score}));
        $base += $USE_V2 ? 1 : 1-$self->{sift}->{tp}->{$sift_score};
    }
    
    if ($polyphen_score >= $self->{config}->{'cutoff.HumVar.polyphen'}){
        $int_score += sprintf("%.3f", $polyphen_score/$self->{config}->{'max.HumVar.polyphen'}*(1-$self->{polyphen}->{tn}->{$polyphen_score}));
        $base += $USE_V2 ? 1 : 1-$self->{polyphen}->{tn}->{$polyphen_score};
    }
    else {
        $int_score += sprintf("%.3f", $polyphen_score/$self->{config}->{'max.HumVar.polyphen'}*(1-$self->{polyphen}->{tp}->{$polyphen_score}));
        $base += $USE_V2 ? 1 : 1-$self->{polyphen}->{tp}->{$polyphen_score};
    }

    if ($base == 0){
        $int_score = -1;
        $class = 'not_computable_was';
    }
    else {
        $int_score = sprintf("%.3f", $int_score/$base);
    }

    if ($int_score >= 0.469){
        $class = 'deleterious';
    }
    elsif ($int_score >= 0 && $int_score < 0.469) {
        $class = 'neutral';
    }

    # if the user wants an array, return the class and score, otherwise just return the class
        
    return ($class, $int_score);
}

1;
