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

 Draw

=head1 SYNOPSIS

 mv Draw.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin Draw

=head1 DESCRIPTION

 A VEP plugin that draws pictures of the transcript model showing the
 variant location. Can take five optional paramters:
 
 1) File name stem for images
 2) Image width in pixels (default: 1000px)
 3) Image height in pixels (default: 100px)
 4) Transcript ID - only draw images for this transcript
 5) Variant ID - only draw images for this variant
 
 e.g.
 
 ./vep -i variations.vcf --plugin Draw,myimg,2000,100
 
 Images are written to [file_stem]_[transcript_id]_[variant_id].png
 
 Requires GD library installed to run.

=cut

package Draw;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

# GD libraries for image creating
use GD;
use GD::Polygon;

use Bio::EnsEMBL::Variation::Utils::VariationEffect qw(MAX_DISTANCE_FROM_TRANSCRIPT);

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);


sub new {
    my $class = shift;

    my $self = $class->SUPER::new(@_);
    
    # configure
    my @params = @{$self->params};
    
    $self->{prefix}     = $params[0] || $self->{config}->{output_file};
    $self->{width}      = $params[1] || 1000;
    $self->{height}     = $params[2] || 100;
    $self->{transcript} = $params[3] || undef;
    $self->{variant}    = $params[4] || undef;

    return $self;
}

sub version {
    return '2.4';
}

sub feature_types {
    return ['Transcript'];
}

sub variant_feature_types {
    return ['BaseVariationFeature'];
}

sub get_header_info {
    return {};
}

sub run {
    my ($self, $tva) = @_;
    
    my $main_tr = $tva->feature;
    my $vf = $tva->base_variation_feature;
    
    return {} if defined($self->{transcript}) && $main_tr->stable_id ne $self->{transcript};
    return {} if defined($self->{variant}) && $vf->variation_name ne $self->{variant};
    
    # if we're showing a gene fusion, get 
    my $second_tr = $tva->{_fusion_transcripts}->[0] if grep {$_->SO_term =~ /gene_fusion/} @{$tva->get_all_OverlapConsequences};
    
    # set up scales etc
    my $width    = $main_tr->feature_Slice->length + (2 * MAX_DISTANCE_FROM_TRANSCRIPT);
    my $tr_start = $main_tr->start - MAX_DISTANCE_FROM_TRANSCRIPT;
    my $tr_end   = $main_tr->end + MAX_DISTANCE_FROM_TRANSCRIPT;
    
    if(defined($second_tr)) {
        $width    = (max(($main_tr->end, $second_tr->end)) - min(($main_tr->start, $second_tr->start))) + 1 + (2 * MAX_DISTANCE_FROM_TRANSCRIPT);
        $tr_start = min(($main_tr->start, $second_tr->start)) - MAX_DISTANCE_FROM_TRANSCRIPT;
        $tr_end   = max(($main_tr->end, $second_tr->end)) + MAX_DISTANCE_FROM_TRANSCRIPT;
    }
    
    my $x_scale  = ($self->{width} - 20)  / $width;
    my $y_scale  = ($self->{height} - 30) / 100;
    my $x_off    = 10;
    my $y_off    = 20;
    
    # create GD image object
    my $img = GD::Image->new($self->{width}, $self->{height});
    
    # set up some colours
    my %colours = (
        white      => $img->colorAllocate(255,255,255),
        black      => $img->colorAllocate(0,0,0),
        grey       => $img->colorAllocate(200,200,200),
        darkgrey   => $img->colorAllocate(150,150,150),
        vlightgrey => $img->colorAllocate(235,235,235),
        blue       => $img->colorAllocate(0,0,200),
        lightblue  => $img->colorAllocate(200,200,255),
        red        => $img->colorAllocate(200,0,0),
        lightred   => $img->colorAllocate(255,200,200),
        green      => $img->colorAllocate(0,200,0),
        lightgreen => $img->colorAllocate(220,255,220),
        yellow     => $img->colorAllocate(236,164,26),
        purple     => $img->colorAllocate(195,50,212),  
    );
    
    # scale bar
    my $zero_string = '0' x (length(int(100 / $x_scale)) - 1);
    my $bases_per_bar = '1'.$zero_string;
    
    my $start = int($tr_start / $bases_per_bar) * $bases_per_bar;
    my $end = (int($tr_start / $bases_per_bar) + 1) * $bases_per_bar;
    my $colour = 0;
    
    while($start < $tr_end) {
        my $method = $colour ? 'rectangle' : 'filledRectangle';
        
        $img->$method(
            $x_off + (($start - $tr_start) * $x_scale),
            $self->{height} - 15,
            $x_off + (($end - $tr_start) * $x_scale),
            $self->{height} - 10,
            $colours{grey},
        );
        
        # tick and label
        if($start =~ /(5|0)$zero_string$/) {
            my $string = $start;
            1 while $string =~ s/^(-?\d+)(\d\d\d)/$1,$2/;
            
            $img->string(
                gdTinyFont,
                $x_off + (($start - $tr_start) * $x_scale) + 2,
                $self->{height} - 8,
                $string,
                $colours{black}
            );
            
            $img->line(
                $x_off + (($start - $tr_start) * $x_scale),
                $self->{height} - 15,
                $x_off + (($start - $tr_start) * $x_scale),
                $self->{height},
                $start =~ /5$zero_string$/ ? $colours{grey} : $colours{black}
            );
            
            $img->dashedLine(
                $x_off + (($start - $tr_start) * $x_scale),
                0,
                $x_off + (($start - $tr_start) * $x_scale),
                $self->{height} - 15,
                $start =~ /5$zero_string$/ ? $colours{vlightgrey} : $colours{grey}
            )
        }
        
        $colour = 1 - $colour;
        $start += $bases_per_bar;
        $end += $bases_per_bar;
    }
    
    # render transcripts
    foreach my $tr($main_tr, $second_tr) {
        next unless defined($tr);
        
        # render introns
        foreach my $intron(@{$tr->get_all_Introns}) {
            $img->line(
                $x_off + (($intron->start - $tr_start) * $x_scale),
                $y_off + (20 * $y_scale),
                $x_off + (((($intron->start + $intron->end) / 2) - $tr_start) * $x_scale),
                $y_off + (10 * $y_scale),
                $colours{lightblue}
            );
            
            $img->line(
                $x_off + (((($intron->start + $intron->end) / 2) - $tr_start) * $x_scale),
                $y_off + (10 * $y_scale),
                $x_off + (($intron->end - $tr_start) * $x_scale),
                $y_off + (20 * $y_scale),
                $colours{lightblue}
            );
        }
        
        # render exons
        foreach my $exon(@{$tr->get_all_Exons}) {
            
            # non-coding part
            $img->rectangle(
                $x_off + (($exon->start - $tr_start) * $x_scale),
                $y_off + (10 * $y_scale),
                $x_off + (($exon->end - $tr_start) * $x_scale),
                $y_off + (30 * $y_scale),
                $colours{lightblue}
            );
            
            # coding part
            $img->filledRectangle(
                $x_off + (($exon->coding_region_start($tr) - $tr_start) * $x_scale),
                $y_off + (0 * $y_scale),
                $x_off + (($exon->coding_region_end($tr) - $tr_start) * $x_scale),
                $y_off + (40 * $y_scale),
                $colours{blue}
            ) if defined $exon->coding_region_start($tr) && defined $exon->coding_region_end($tr);
        }
        
        # add transcript direction indicator
        if($tr->strand == 1) {
            
            # vertical line
            $img->line(
                $x_off + (($tr->start - $tr_start) * $x_scale),
                $y_off + (-5 * $y_scale),
                $x_off + (($tr->start - $tr_start) * $x_scale),
                $y_off + (20 * $y_scale),
                $colours{lightblue},
            );
            
            # horizontal line
            $img->line(
                $x_off + (($tr->start - $tr_start) * $x_scale),
                $y_off + (-5 * $y_scale),
                $x_off + (($tr->start - $tr_start) * $x_scale) + 20,
                $y_off + (-5 * $y_scale),
                $colours{lightblue},
            );
            
            # top arrow part
            $img->line(
                $x_off + (($tr->start - $tr_start) * $x_scale) + 17,
                $y_off + (-8 * $y_scale),
                $x_off + (($tr->start - $tr_start) * $x_scale) + 20,
                $y_off + (-5 * $y_scale),
                $colours{lightblue},
            );
            
            # bottom arrow part
            $img->line(
                $x_off + (($tr->start - $tr_start) * $x_scale) + 17,
                $y_off + (-1 * $y_scale),
                $x_off + (($tr->start - $tr_start) * $x_scale) + 20,
                $y_off + (-5 * $y_scale),
                $colours{lightblue},
            );
            
            # label
            $img->string(gdTinyFont, $x_off + (($tr->start - $tr_start) * $x_scale) + 25, $y_off + (-12 * $y_scale), $tr->stable_id, $colours{blue});
        }
        
        else {        
            
            # vertical line
            $img->line(
                $x_off + (($tr->end - $tr_start) * $x_scale),
                $y_off + (20 * $y_scale),
                $x_off + (($tr->end - $tr_start) * $x_scale),
                $y_off + (47 * $y_scale),
                $colours{lightblue},
            );
            
            # horizontal line
            $img->line(
                $x_off + (($tr->end - $tr_start) * $x_scale),
                $y_off + (47 * $y_scale),
                $x_off + (($tr->end - $tr_start) * $x_scale) - 20,
                $y_off + (47 * $y_scale),
                $colours{lightblue},
            );
            
            # top arrow part
            $img->line(
                $x_off + (($tr->end - $tr_start) * $x_scale) - 17,
                $y_off + (50 * $y_scale),
                $x_off + (($tr->end - $tr_start) * $x_scale) - 20,
                $y_off + (47 * $y_scale),
                $colours{lightblue},
            );
            
            # bottom arrow part
            $img->line(
                $x_off + (($tr->end - $tr_start) * $x_scale) - 17,
                $y_off + (43 * $y_scale),
                $x_off + (($tr->end - $tr_start) * $x_scale) - 20,
                $y_off + (47 * $y_scale),
                $colours{lightblue},
            );
            
            # label
            $img->string(gdTinyFont, $x_off + (($tr->end - $tr_start) * $x_scale) - 100, $y_off + (43 * $y_scale), $tr->stable_id, $colours{blue});
        }
    }
    
    # render variant
    my $var_colour = 'green';
    
    if($vf->class_SO_term =~ /deletion/) {
        $var_colour = 'red';
    }
    
    $img->filledRectangle(
        $x_off + (($vf->start - $tr_start) * $x_scale),
        $y_off + (60 * $y_scale),
        $x_off + (($vf->end - $tr_start) * $x_scale),
        $y_off + (70 * $y_scale),
        $colours{$var_colour},
    );
    
    # variant label
    $img->string(
        gdTinyFont,
        $x_off + (($vf->start - $tr_start) * $x_scale),
        $y_off + (75 * $y_scale),
        $vf->variation_name,
        $colours{$var_colour}
    );
    
    my $vname = $vf->variation_name;
    $vname =~ s/\//\_/g;
    my $file = $self->{prefix}."_".$main_tr->stable_id."_".(defined($second_tr) ? $second_tr->stable_id."_" : "").$vname."\.png";
    
    # check we're allowed to write to it
    if(!defined($self->{config}->{force_overwrite}) && -e $file) {
        die "ERROR: Image file $file already exists - choose a different file name stem or use --force_overwrite\n";
        return;
    }
    
    open IM, ">$file" or die "ERROR: Could not write to file $file\n";
    binmode IM;
    print IM $img->png;
    close IM;
    
    return {};
}

sub max {
    return (sort {$a <=> $b} @_)[-1];
}

sub min {
    return (sort {$a <=> $b} @_)[0];
}

1;

