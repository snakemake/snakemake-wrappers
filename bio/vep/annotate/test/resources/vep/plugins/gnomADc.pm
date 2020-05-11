=head1 LICENSE

Copyright 2018 QIMR Berghofer Medical Research Institute

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

 Stephen Kazakoff <Stephen.Kazakoff@qimrberghofer.edu.au>
    
=cut

=head1 NAME

 gnomADc

=head1 SYNOPSIS

 mv gnomADc.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin gnomADc,/path/to/gnomad-public/r2.0.2/coverage/genomes
 ./vep -i variations.vcf --plugin gnomADc,/path/to/gnomad-public/r2.0.2/coverage/exomes

=head1 DESCRIPTION

 A VEP plugin that retrieves gnomAD annotation from either the genome
 or exome coverage files, available here:

 http://gnomad.broadinstitute.org/downloads

 The coverage files must be downloaded and tabix indexed before using this
 plugin:

 > release="2.0.2"

 > genomes="https://storage.googleapis.com/gnomad-public/release/${release}/coverage/genomes"
 > wget -x "${genomes}"/gnomad.genomes.r${release}.chr{{1..22},X}.coverage.txt.gz
 > for i in "${genomes#*//}"/gnomad.genomes.r${release}.chr{{1..22},X}.coverage.txt.gz; do
 >   tabix -s 1 -b 2 -e 2 "${i}"
 > done

 > exomes="https://storage.googleapis.com/gnomad-public/release/${release}/coverage/exomes"
 > wget -x "${exomes}"/gnomad.exomes.r${release}.chr{{1..22},X,Y}.coverage.txt.gz
 > for i in "${exomes#*//}"/gnomad.exomes.r${release}.chr{{1..22},X,Y}.coverage.txt.gz; do
 >   tabix -s 1 -b 2 -e 2 "${i}"
 > done

 The parent directory's basename is used to set the output field prefix. This
 is 'gnomADg' for genomes, 'gnomADe' for exomes, or else just 'gnomAD'.

 If you use this plugin, please see the terms and data information:

 http://gnomad.broadinstitute.org/terms

 The gnomAD coverage files are provided for GRCh37, but if you use GRCh38
 you may like to use the liftover files, available here:

 https://console.cloud.google.com/storage/browser/gnomad-public/release

 You must have the Bio::DB::HTS module or the tabix utility must be installed
 in your path to use this plugin. 


=cut

package gnomADc;

use strict;
use warnings;

use File::Basename;

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  $self->get_user_params();

  my $params = $self->params;

  my $dir = shift @$params;
  die("ERROR: gnomAD directory not specified\n") unless $dir;
  die("ERROR: gnomAD directory not found\n") unless -d $dir;

  # use the parent directory's basename to set a column prefix
  my $base = basename($dir);
  my $prefix = 'gnomAD' . ($base eq 'genomes' || $base eq 'exomes' ? substr($base, 0, 1) : '');

  # add any coverage files to our list of inputs
  opendir (my $fh, $dir) or die $!;
  for (readdir $fh) {
    $self->add_file("$dir/$_") if /\.coverage\.txt\.gz$/;
  }
  closedir $fh;

  my @files = @{ $self->files() };

  die("ERROR: Could not find any $prefix coverage files\n") unless @files;

  $self->{prefix} = $prefix;

  return $self;
}

sub feature_types {
  return ['Feature', 'Intergenic'];
}

sub get_header_info {
  my $self = shift;

  my $prefix = $self->{prefix};
  my %header_info;

  for (qw(mean median)) {
    $header_info{ join('_', $prefix, $_, 'cov') } = "$_ coverage";
  };

  for (qw(1x 5x 10x 15x 20x 25x 30x 50x 100x)) {
    $header_info{ join('_', $prefix, $_, 'cov') } = "Fraction of samples at $_ coverage";
  }

  return \%header_info;
}

sub run {
  my ($self, $vfoa) = @_;

  my $vf = $vfoa->variation_feature;
  my ($vf_start, $vf_end) = ($vf->{start}, $vf->{end});

  $vf_end = $vf_start if $vf_start > $vf_end;

  my @results = @{ $self->get_data($vf->{chr}, $vf_start, $vf_end) };

  return {} unless @results;

  my %sums;

  # sum the values across each position
  for my $result (@results) {
    $sums{$_} += $result->{$_} for keys %$result;
  }

  # take the average of each of the values
  my %avgs = map { $_ => sprintf("%.4f", $sums{$_} / scalar @results) } keys %sums;

  return \%avgs;
}

sub parse_data {
  my ($self, $line) = @_;

  my $prefix = $self->{prefix};
  my ($chr, $pos, @cov) = split /\t/, $line;

  my @keys = map {
    join('_', $prefix, $_, 'cov')
  }
  qw(mean median 1x 5x 10x 15x 20x 25x 30x 50x 100x);

  my %result;

  @result{@keys} = @cov;

  return \%result;
}

sub get_start {
  return $_[1]->{start};
}

sub get_end {
  return $_[1]->{end};
}

1;

