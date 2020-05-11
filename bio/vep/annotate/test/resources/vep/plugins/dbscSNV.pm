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

 dbscSNV

=head1 SYNOPSIS

  mv dbscSNV.pm ~/.vep/Plugins
  ./vep -i variations.vcf --plugin dbscSNV,/path/to/dbscSNV1.1_GRCh38.txt.gz

=head1 DESCRIPTION

  A VEP plugin that retrieves data for splicing variants from a tabix-indexed
  dbscSNV file.

  Please cite the dbscSNV publication alongside the VEP if you use this resource:
  http://nar.oxfordjournals.org/content/42/22/13534

  The Bio::DB::HTS perl library or tabix utility must be installed in your path
  to use this plugin. The dbscSNV data file can be downloaded from
  https://sites.google.com/site/jpopgen/dbNSFP.

  The file must be processed and indexed by tabix before use by this plugin.
  dbscSNV1.1 has coordinates for both GRCh38 and GRCh37; the file must be
  processed differently according to the assembly you use.

  > wget ftp://dbnsfp:dbnsfp@dbnsfp.softgenetics.com/dbscSNV1.1.zip
  > unzip dbscSNV1.1.zip
  > head -n1 dbscSNV1.1.chr1 > h

  # GRCh38
  > cat dbscSNV1.1.chr* | grep -v ^chr | sort -k5,5 -k6,6n | cat h - | awk '$5 != "."' | bgzip -c > dbscSNV1.1_GRCh38.txt.gz
  > tabix -s 5 -b 6 -e 6 -c c dbscSNV1.1_GRCh38.txt.gz

  # GRCh37
  > cat dbscSNV1.1.chr* | grep -v ^chr | cat h - | bgzip -c > dbscSNV1.1_GRCh37.txt.gz
  > tabix -s 1 -b 2 -e 2 -c c dbscSNV1.1_GRCh37.txt.gz

  Note that in the last command we tell tabix that the header line starts with "c";
  this may change to the default of "#" in future versions of dbscSNV.

  Tabix also allows the data file to be hosted on a remote server. This plugin is
  fully compatible with such a setup - simply use the URL of the remote file:

  --plugin dbscSNV,http://my.files.com/dbscSNV.txt.gz

  Note that transcript sequences referred to in dbscSNV may be out of sync with
  those in the latest release of Ensembl; this may lead to discrepancies with
  scores retrieved from other sources.
 
=cut

package dbscSNV;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);
  
  # get dbNSFP file
  my $file = $self->params->[0];
  $self->add_file($file);

  if(my $assembly = $self->params->[1]) {
    $self->{_param_assembly} = $assembly;
  }
  
  # get headers
  open HEAD, "tabix -fh $file 1:1-1 2>&1 | ";
  while(<HEAD>) {
    chomp;
    $self->{headers} = [split];
  }
  close HEAD;

  # check alt and Ensembl_transcriptid headers
  foreach my $h(qw(alt Ensembl_gene)) {
    die "ERROR: Could not find required column $h in $file\n" unless grep {$_ eq $h} @{$self->{headers}};
  }

  # check we have hg38_pos col, only present in dbscSNV >= 1.1
  if($self->pos_column eq 'hg38_pos') {
    die("ERROR: Could not find hg38_pos column in $file\n") unless grep {$_ eq 'hg38_pos'} @{$self->{headers}};
  }
  
  $self->{cols} = {
    'ada_score' => 1,
    'rf_score'  => 1
  };
  
  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub variation_feature_types {
  return ['VariationFeature'];
}

sub get_header_info {
  return {
    ada_score => 'dbscSNV ADA score',
    rf_score  => 'dbscSNV RF score'
  }
}

sub run {
  my ($self, $tva) = @_;
  
  my $vf = $tva->variation_feature;
  
  return {} unless $vf->{start} eq $vf->{end};
  # return {} unless grep {$_->SO_term =~ /splic/} @{$tva->get_all_OverlapConsequences};
  
  # get allele, reverse comp if needed
  my $allele = $tva->variation_feature_seq;
  reverse_comp(\$allele) if $vf->{strand} < 0;
  
  return {} unless $allele =~ /^[ACGT]$/;
  
  # get gene stable ID
  my $g_id = $tva->transcript->{_gene_stable_id} || $tva->transcript->gene->stable_id;
  
  my $data;
  my $pos_column = $self->pos_column;
  
  foreach my $tmp_data(@{$self->get_data($vf->{chr}, $vf->{start} - 1, $vf->{end})}) {
    # compare allele and transcript
    next unless
      $tmp_data->{$pos_column} == $vf->{start} &&
      defined($tmp_data->{alt}) &&
      $tmp_data->{alt} eq $allele; # &&
      # defined($tmp_data->{Ensembl_gene}) &&
      # $tmp_data->{Ensembl_gene} =~ /$g_id($|;)/;
    
    $data = $tmp_data;
    last;
  }
  
  return {} unless scalar keys %$data;
  
  # get required data
  my %return =
    map {$_ => $data->{$_}}
    grep {$data->{$_} ne '.'}              # ignore missing data
    grep {defined($self->{cols}->{$_})}  # only include selected cols
    keys %$data;
  
  return \%return;
}

sub parse_data {
  my ($self, $line) = @_;

  $line =~ s/\r$//g;

  my @split = split /\t/, $line;
  
  # parse data into hash of col names and values
  my %data = map {$self->{headers}->[$_] => $split[$_]} (0..(scalar @{$self->{headers}} - 1));

  return \%data;
}

sub get_start {  
  return $_[1]->{$_[0]->pos_column};
}

sub get_end {
  return $_[1]->{$_[0]->pos_column};
}

sub pos_column {
  my $self = shift;

  # work out which column to use
  unless(exists($self->{pos_column})) {  
    if(my $assembly = $self->{_param_assembly} || $self->{config}->{assembly}) {
      if($assembly eq 'GRCh37') {
        $self->{pos_column} = 'pos';
      }
      elsif($assembly eq 'GRCh38') {
        $self->{pos_column} = 'hg38_pos';
      }
      else {
        die("ERROR: Assembly \"$assembly\" is not compatible with this plugin\n");
      }
    }
    else {
      die("ERROR: Could not establish which position column to use based on assembly; try setting assembly manually with --assembly\n");
    }
  }

  return $self->{pos_column};
}

1;

