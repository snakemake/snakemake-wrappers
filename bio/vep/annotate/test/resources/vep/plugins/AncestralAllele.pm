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

 AncestralAllele

=head1 SYNOPSIS

 mv AncestralAllele.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin AncestralAllele,homo_sapiens_ancestor_GRCh38_e86.fa.gz

=head1 DESCRIPTION

 A VEP plugin that retrieves ancestral allele sequences from a FASTA file.

 Ensembl produces FASTA file dumps of the ancestral sequences of key species.
 They are available from ftp://ftp.ensembl.org/pub/current_fasta/ancestral_alleles/

 For optimal retrieval speed, you should pre-process the FASTA files into a single
 bgzipped file that can be accessed via Bio::DB::HTS::Faidx (installed by VEP's
 INSTALL.pl):

 wget ftp://ftp.ensembl.org/pub/release-90/fasta/ancestral_alleles/homo_sapiens_ancestor_GRCh38_e86.tar.gz
 tar xfz homo_sapiens_ancestor_GRCh38_e86.tar.gz
 cat homo_sapiens_ancestor_GRCh38_e86/*.fa | bgzip -c > homo_sapiens_ancestor_GRCh38_e86.fa.gz
 rm -rf homo_sapiens_ancestor_GRCh38_e86/ homo_sapiens_ancestor_GRCh38_e86.tar.gz
 ./vep -i variations.vcf --plugin AncestralAllele,homo_sapiens_ancestor_GRCh38_e86.fa.gz

 The plugin is also compatible with Bio::DB::Fasta and an uncompressed FASTA file.

 Note the first time you run the plugin with a newly generated FASTA file it will
 spend some time indexing the file. DO NOT INTERRUPT THIS PROCESS, particularly
 if you do not have Bio::DB::HTS installed.

 Special cases:
   "-" represents an insertion
   "?" indicates the chromosome could not be looked up in the FASTA

=cut

package AncestralAllele;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

our $CAN_USE_FAIDX;
our $DEBUG = 0;

BEGIN {
  if (eval { require Bio::DB::HTS::Faidx; 1 }) {
    $CAN_USE_FAIDX = 1;
  }
}

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);

  # get file
  my $fasta_file = $self->params->[0] || "";
  die("ERROR: Ancestral FASTA file $fasta_file not provided or found\n") unless $fasta_file && -e $fasta_file;
  $self->fasta_file($fasta_file);

  # get type of index we're creating/using
  my $type = $fasta_file =~ /\.gz$/ ? 'Bio::DB::HTS::Faidx' : 'Bio::DB::Fasta';
  die("ERROR: Bio::DB::HTS required to access compressed FASTA file $fasta_file\n") if $type eq 'Bio::DB::HTS::Faidx' && !$CAN_USE_FAIDX;
  $self->index_type($type);

  # init DB here so indexing doesn't happen at some point in the middle of VEP run
  $self->fasta_db;

  return $self;
}

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {
  return { AA => 'Ancestral allele from '.$_[0]->fasta_file }
}

sub run {
  my ($self, $tva) = @_;
  
  my $vf = $tva->variation_feature;

  my ($start, $end) = ($vf->{start}, $vf->{end});

  # cache AA on VF, prevents repeat lookups for multiple TVAs
  if(!exists($vf->{_vep_plugin_AncestralAllele})) {

    # insertion
    return { AA => $vf->{_vep_plugin_AncestralAllele} = '-' } if $start > $end;

    my $sr_name = $self->get_sr_name($vf->{chr});

    # chr not in FASTA
    return { AA => $vf->{_vep_plugin_AncestralAllele} = '?' } unless $sr_name;

    my $fasta_db = $self->fasta_db;
    my $type = $self->index_type;
    my ($seq, $length);

    if($type eq 'Bio::DB::HTS::Faidx') {
      my $location_string = $sr_name.":".$start."-".$end ;
      ($seq, $length) = $fasta_db->get_sequence($location_string);
    }
    elsif($type eq 'Bio::DB::Fasta') {
      $seq = $fasta_db->seq($sr_name, $start => $end);
    }
    else {
      throw("ERROR: Don't know how to fetch sequence from a ".ref($fasta_db)."\n");
    }

    reverse_comp(\$seq) if $vf->{strand} < 0;

    $vf->{_vep_plugin_AncestralAllele} = $seq;
  }

  return { AA => $vf->{_vep_plugin_AncestralAllele} };
}

# getter/setter for fasta file path
sub fasta_file {
  my $self = shift;
  $self->{_fasta_file} = shift if @_;
  return $self->{_fasta_file};
}

# getter/setter for fasta index type
sub index_type {
  my $self = shift;
  $self->{_index_type} = shift if @_;
  return $self->{_index_type};
}

## CRIBBED FROM Bio::EnsEMBL::Variation::Utils::FastaSequence
## MOVE THIS CODE TO SHARED UTILS SPACE?
# creates the FASTA DB object
# returns either a Bio::DB::Fasta or a Bio::DB::HTS::Faidx
# uses a lock file to avoid partial indexes getting used
sub fasta_db {
  my $self = shift;

  # if we've forked we need to re-connect
  # but make sure we only do this once per fork
  my $prev_pid = $self->{_prev_pid} ||= $$;
  if($prev_pid ne $$) {
    delete $self->{_fasta_db};
    $self->{_prev_pid} = $$;
  }

  if(!exists($self->{_fasta_db})) {
    my $fasta = $self->fasta_file;
    my $type = $self->index_type;

    # check lock file
    my $lock_file = $fasta;
    $lock_file .= -d $fasta ? '/.vep.lock' : '.vep.lock';

    # lock file exists, indexing failed
    if(-e $lock_file) {
      print STDERR "Lock file found, removing to allow re-indexing\n" if $DEBUG;
      for(qw(.fai .index .gzi /directory.index /directory.fai .vep.lock)) {
        unlink($fasta.$_) if -e $fasta.$_;
      }
    }

    my $index_exists = 0;

    for my $fn(map {$fasta.$_} qw(.fai .index .gzi /directory.index /directory.fai)) {
      if(-e $fn) {
        $index_exists = 1;
        last;
      }
    }

    # create lock file
    unless($index_exists) {
      open LOCK, ">$lock_file" or throw("ERROR: Could not write to FASTA lock file $lock_file\n");
      print LOCK "1\n";
      close LOCK;
      print STDERR "Indexing $fasta\n" if $DEBUG;
    }

    # run indexing
    my $fasta_db;
    if($type eq 'Bio::DB::HTS::Faidx' && $CAN_USE_FAIDX) {
      $fasta_db = Bio::DB::HTS::Faidx->new($fasta);
    }
    elsif(!$type || $type eq 'Bio::DB::Fasta') {
      $fasta_db = Bio::DB::Fasta->new($fasta);
    }
    else {
      throw("ERROR: Don't know how to index with type $type\n");
    }
    print STDERR "Finished indexing\n" if $DEBUG;

    throw("ERROR: Unable to create FASTA DB\n") unless $fasta_db;

    # remove lock file
    unlink($lock_file) unless $index_exists;

    $self->{_fasta_db} = $fasta_db;
  }

  return $self->{_fasta_db};
}

# gets seq region name as it appears in the FASTA
# the file contains names like "ANCESTOR_for_chromosome:GRCh38:10:1:133797422:1"
# so want to map from "10" or "chr10" to "ANCESTOR_for_chromosome:GRCh38:10:1:133797422:1"
sub get_sr_name {
  my $self = shift;
  my $sr_name = shift;
  my $new_sr_name = $sr_name;

  my $map = $self->fasta_name_map;
  my $fasta_db = $self->fasta_db;

  unless($map->{$sr_name}) {
    foreach my $alt(
      $sr_name =~ /^chr/i ? (substr($sr_name, 3)) : ('chr'.$sr_name, 'CHR'.$sr_name)
    ) {
      if($map->{$alt}) {
        print STDERR "USING SYNONYM $alt FOR $sr_name\n" if $DEBUG;
        $new_sr_name = $alt;
        last;
      }
    }
  }

  return $map->{$new_sr_name} || undef;
}

sub fasta_name_map {
  my ($self, $chr) = @_;

  if(!exists($self->{_name_map})) {
    my $fasta_db = $self->fasta_db;

    my %map = map {(split(':', $_))[2] => $_}
      $fasta_db->isa('Bio::DB::Fasta') ?
      (grep {$_ !~ /^\_\_/} $fasta_db->get_all_primary_ids) :
      ($fasta_db->get_all_sequence_ids);

    $self->{_name_map} = \%map;
  }

  return $self->{_name_map};
}

1;
