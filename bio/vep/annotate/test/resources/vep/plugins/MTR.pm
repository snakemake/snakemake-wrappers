=head1 CONTACT

  Slave Petrovski <slavep@unimelb.edu.au>
  Michael Silk <silkm@student.unimelb.edu.au>

=cut

=head1 NAME

  MTR (Missense Tolerance Ratio)

=head1 SYNOPSIS

  mv MTR.pm ~/.vep/Plugins
  curl -O ftp://mtr-viewer.mdhs.unimelb.edu.au/pub/mtrflatfile_1.0.txt.gz
  curl -O ftp://mtr-viewer.mdhs.unimelb.edu.au/pub/mtrflatfile_1.0.txt.gz.tbi
  perl variant_effect_predictor.pl -i variations.vcf --plugin MTR,mtrflatfile_1.0.txt.gz

=head1 DESCRIPTION

A VEP plugin that retrieves Missense Tolerance Ratio (MTR) scores for
variants from a tabix-indexed flat file.

MTR scores quantify the amount of purifying selection acting
specifically on missense variants in a given window of protein-coding
sequence. It is estimated across a sliding window of 31 codons and uses
observed standing variation data from the WES component of the Exome
Aggregation Consortium Database (ExAC), version 2.0
(http://gnomad.broadinstitute.org).

Please cite the MTR publication alongside the VEP if you use this resource:
http://genome.cshlp.org/content/27/10/1715

The Bio::DB::HTS perl library or tabix utility must be installed in your path
to use this plugin. MTR flat files can be downloaded from:
ftp://mtr-viewer.mdhs.unimelb.edu.au/pub

NB: Data are available for GRCh37 only

=cut

package MTR;

use strict;
use warnings;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;
  my $self = $class->SUPER::new(@_);

  # test tabix
  die "ERROR: tabix does not seem to be in your path\n" unless `which tabix 2>&1` =~ /tabix$/;

  # get MTR file
  my $file = $self->params->[0];
  $self->add_file($file);

  # remote files?
  if($file =~ /tp\:\/\//) {
    my $remote_test = `tabix -f $file 1:1-1 2>&1`;
    if($remote_test && $remote_test !~ /get_local_version/) {
      die "$remote_test\nERROR: Could not find file or index file for remote annotation file $file\n";
    }
  }

  # check files exist
  else {
    die "ERROR: MTR file $file not found\n" unless -e $file;
    die "ERROR: Tabix index file $file\.tbi not found - perhaps you need to create it first?\n" unless -e $file.'.tbi';
  }

  # get headers and store on self
  open HEAD, "tabix -fh $file 1:1-1 2>&1 | ";
  while(<HEAD>) {
    next unless /^\#/;
    chomp;
    $_ =~ s/^\#//;
    $self->{headers} = [split];
  }
  close HEAD;

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub variation_feature_types {
  return ['VariationFeature'];
}

sub get_header_info {
  my $self = shift;
  return {
	  MTR         => 'MTR score',
	  FDR         => 'MTR false discovery rate adjusted binomial exact test.',
	  MTR_centile => 'MTR gene-specific percentile'
	 }
}

sub run {
  my ($self, $tva) = @_;
  my $vf = $tva->variation_feature;

  # get allele, reverse comp if needed
  my $allele = $tva->variation_feature_seq;
  reverse_comp(\$allele) if $vf->{strand} < 0;

  return {} unless $allele =~ /^[ACGT]$/;

  my $tr_id = $tva->transcript->stable_id;

  # data is written by pos, allele, transcript ID (feature)
  # grep lines read in matched on position so that they also are matched on allele and transcript ID
  my ($res) = grep {
    $_->{Genomic_position} eq $vf->{start} &&
    $_->{Genomic_position} eq $vf->{end} &&
    $_->{alt}              eq $allele &&
    $_->{Feature}          eq $tr_id
  } @{$self->get_data($vf->{chr}, $vf->{start}, $vf->{end})};

  # return only the keys defined by get_header_info()
  return $res ? { map {$_ => $res->{$_}} grep {defined($res->{$_}) && $res->{$_} ne '.'} keys %{$self->get_header_info} } : {};
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
  return $_[1]->{'Genomic_position'};
}

sub get_end {
  return $_[1]->{'Genomic_position'};
}

1;
