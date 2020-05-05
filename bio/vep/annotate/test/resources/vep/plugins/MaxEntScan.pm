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

 MaxEntScan

=head1 SYNOPSIS

 mv MaxEntScan.pm ~/.vep/Plugins
 ./vep -i variants.vcf --plugin MaxEntScan,/path/to/maxentscan/fordownload
 ./vep -i variants.vcf --plugin MaxEntScan,/path/to/maxentscan/fordownload,SWA,NCSS

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 runs MaxEntScan (http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)
 to get splice site predictions.

 The plugin copies most of the code verbatim from the score5.pl and score3.pl
 scripts provided in the MaxEntScan download. To run the plugin you must get and
 unpack the archive from http://genes.mit.edu/burgelab/maxent/download/; the path
 to this unpacked directory is then the param you pass to the --plugin flag.

 The plugin executes the logic from one of the scripts depending on which
 splice region the variant overlaps:

 score5.pl : last 3 bases of exon    --> first 6 bases of intron
 score3.pl : last 20 bases of intron --> first 3 bases of exon

 The plugin reports the reference, alternate and difference (REF - ALT) maximum
 entropy scores.

 If 'SWA' is specified as a command-line argument, a sliding window algorithm
 is applied to subsequences containing the reference and alternate alleles to
 identify k-mers with the highest donor and acceptor splice site scores. To assess
 the impact of variants, reference comparison scores are also provided. For SNVs,
 the comparison scores are derived from sequence in the same frame as the highest
 scoring k-mers containing the alternate allele. For all other variants, the
 comparison scores are derived from the highest scoring k-mers containing the
 reference allele. The difference between the reference comparison and alternate
 scores (SWA_REF_COMP - SWA_ALT) are also provided.

 If 'NCSS' is specified as a command-line argument, scores for the nearest
 upstream and downstream canonical splice sites are also included.

 By default, only scores are reported. Add 'verbose' to the list of command-
 line arguments to include the sequence output associated with those scores.

=cut

package MaxEntScan;

use strict;
use warnings;

use Digest::MD5 qw(md5_hex);

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);
use Bio::EnsEMBL::Variation::Utils::VariationEffect qw(overlap);

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;
use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

# how many seq/score pairs to cache in memory
our $CACHE_SIZE = 50;

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);
  
  # we need sequence, so no offline mode unless we have FASTA
  die("ERROR: cannot function in offline mode without a FASTA file\n") if $self->{config}->{offline} && !$self->{config}->{fasta};

  my $params = $self->params;

  my $dir = shift @$params;
  die("ERROR: MaxEntScan directory not specified\n") unless $dir;
  die("ERROR: MaxEntScan directory not found\n") unless -d $dir;
  $self->{_dir} = $dir;

  ## setup from score5.pl
  $self->{'score5_me2x5'} = $self->score5_makescorematrix($dir.'/me2x5');
  $self->{'score5_seq'}   = $self->score5_makesequencematrix($dir.'/splicemodels/splice5sequences');

  ## setup from score3.pl
  $self->{'score3_metables'} = $self->score3_makemaxentscores;

  my %opts = map { $_ => undef } @$params;

  $self->{'run_SWA'} = 1 if exists $opts{'SWA'};
  $self->{'run_NCSS'} = 1 if exists $opts{'NCSS'};

  $self->{'verbose'} = 1 if exists $opts{'verbose'};

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  my $self = shift;

  my $v = $self->{'verbose'};
  my $headers = $self->get_MES_header_info($v);

  if ($self->{'run_SWA'}) {
    my $swa_headers = $self->get_SWA_header_info($v);
    $headers = {%$headers, %$swa_headers};
  }

  if ($self->{'run_NCSS'}) {
    my $ncss_headers = $self->get_NCSS_header_info($v);
    $headers = {%$headers, %$ncss_headers};
  }

  return $headers;
}

sub get_MES_header_info {
  my ($self, $verbose) = @_;

  my $headers = {
    MaxEntScan_ref => "MaxEntScan reference sequence score",
    MaxEntScan_alt => "MaxEntScan alternate sequence score",
    MaxEntScan_diff => "MaxEntScan score difference",
  };

  if ($verbose) {

    $headers->{'MaxEntScan_ref_seq'} = "MaxEntScan reference sequence";
    $headers->{'MaxEntScan_alt_seq'} = "MaxEntScan alternate sequence";
  }

  return $headers;
}

sub get_SWA_header_info {
  my ($self, $verbose) = @_;

  my $headers = {
    "MES-SWA_donor_ref" => "Highest splice donor reference sequence score",
    "MES-SWA_donor_alt" => "Highest splice donor alternate sequence score",
    "MES-SWA_donor_ref_comp" => "Donor reference comparison sequence score",
    "MES-SWA_donor_diff" => "Difference between the donor reference comparison and alternate sequence scores",

    "MES-SWA_acceptor_ref" => "Highest splice acceptor reference sequence score",
    "MES-SWA_acceptor_alt" => "Highest splice acceptor alternate sequence score",
    "MES-SWA_acceptor_ref_comp" => "Acceptor reference comparison sequence score",
    "MES-SWA_acceptor_diff" => "Difference between the acceptor reference comparison and alternate sequence scores",
  };

  if ($verbose) {

    $headers->{'MES-SWA_donor_ref_seq'} = "Highest splice donor reference sequence";
    $headers->{'MES-SWA_donor_ref_frame'} = "Position of the highest splice donor reference sequence";
    $headers->{'MES-SWA_donor_ref_context'} = "Selected donor sequence context containing the reference allele";
    $headers->{'MES-SWA_donor_alt_seq'} = "Highest splice donor alternate sequence";
    $headers->{'MES-SWA_donor_alt_frame'} = "Position of the highest splice donor alternate sequence";
    $headers->{'MES-SWA_donor_alt_context'} = "Selected donor sequence context containing the alternate allele";
    $headers->{'MES-SWA_donor_ref_comp_seq'} = "Donor reference comparison sequence";

    $headers->{'MES-SWA_acceptor_ref_seq'} = "Highest splice acceptor reference sequence";
    $headers->{'MES-SWA_acceptor_ref_frame'} = "Position of the highest splice acceptor reference sequence";
    $headers->{'MES-SWA_acceptor_ref_context'} = "Selected acceptor sequence context containing the reference allele";
    $headers->{'MES-SWA_acceptor_alt_seq'} = "Highest splice acceptor alternate sequence";
    $headers->{'MES-SWA_acceptor_alt_frame'} = "Position of the highest splice acceptor alternate sequence";
    $headers->{'MES-SWA_acceptor_alt_context'} = "Selected acceptor sequence context containing the alternate allele";
    $headers->{'MES-SWA_acceptor_ref_comp_seq'} = "Acceptor reference comparison sequence";
  }

  return $headers;
}

sub get_NCSS_header_info {
  my ($self, $verbose) = @_;

  my $headers = {
    "MES-NCSS_upstream_acceptor" => "Nearest upstream canonical splice acceptor sequence score",
    "MES-NCSS_upstream_donor" => "Nearest upstream canonical splice donor sequence score",

    "MES-NCSS_downstream_acceptor" => "Nearest downstream canonical splice acceptor sequence score",
    "MES-NCSS_downstream_donor" => "Nearest downstream canonical splice donor sequence score",
  };

  if ($verbose) {

    $headers->{'MES-NCSS_upstream_acceptor_seq'} = "Nearest upstream canonical splice acceptor sequence";
    $headers->{'MES-NCSS_upstream_donor_seq'} = "Nearest upstream canonical splice donor sequence";

    $headers->{'MES-NCSS_downstream_acceptor_seq'} = "Nearest downstream canonical splice acceptor sequence";
    $headers->{'MES-NCSS_downstream_donor_seq'} = "Nearest downstream canonical splice donor sequence";
  }

  return $headers;
}

sub run {
  my ($self, $tva) = @_;

  my $seq_headers = $self->get_MES_header_info();
  my $results = $self->run_MES($tva);

  if ($self->{'run_SWA'}) {
    my $swa_seq_headers = $self->get_SWA_header_info();
    $seq_headers = {%$seq_headers, %$swa_seq_headers};
    my $swa_results = $self->run_SWA($tva);
    $results = {%$results, %$swa_results};
  }

  if ($self->{'run_NCSS'}) {
    my $ncss_seq_headers = $self->get_NCSS_header_info();
    $seq_headers = {%$seq_headers, %$ncss_seq_headers};
    my $ncss_results = $self->run_NCSS($tva);
    $results = {%$results, %$ncss_results};
  }

  my %data;

  # add the scores
  my @scores = grep { exists $results->{$_} } keys %$seq_headers;
  @data{@scores} = map { sprintf('%.3f', $_) } @{$results}{@scores};

  if ($self->{'verbose'}) {
    # add any remaining results
    my @non_scores = grep { ! exists $data{$_} } keys %$results;
    @data{@non_scores} = @{$results}{@non_scores};
  }

  return \%data;
}

sub run_MES {
  my ($self, $tva) = @_;

  my $vf = $tva->variation_feature;
  return {} unless $vf->{start} == $vf->{end} && $tva->feature_seq =~ /^[ACGT]$/;

  my $tv = $tva->transcript_variation;
  my $tr = $tva->transcript;
  my $tr_strand = $tr->strand;
  my ($vf_start, $vf_end) = ($vf->start, $vf->end);

  # use _overlapped_introns() method from BaseTranscriptVariation
  # this will use an interval tree if available for superfast lookup of overlapping introns
  # we have to expand the search space around $vf because we're looking for the splice region not the intron per se
  foreach my $intron(@{$tv->_overlapped_introns($vf_start - 21, $vf_end + 21)}) {
    
    # get coords depending on strand
    # MaxEntScan does different predictions for 5 and 3 prime
    # and we need to feed it different bits of sequence for each
    #
    # 5prime, 3 bases of exon, 6 bases of intron:
    # ===------
    #
    # 3prime, 20 bases of intron, 3 bases of exon
    # --------------------===

    my ($five_start, $five_end, $three_start, $three_end);

    if($tr_strand > 0) {
      ($five_start, $five_end)   = ($intron->start - 3, $intron->start + 5);
      ($three_start, $three_end) = ($intron->end - 19, $intron->end + 3);
    }

    else {
      ($five_start, $five_end)   = ($intron->end - 5, $intron->end + 3);
      ($three_start, $three_end) = ($intron->start - 3, $intron->start + 19);
    }

    if(overlap($vf->start, $vf->end, $five_start, $five_end)) {
      my ($ref_seq, $alt_seq) = @{$self->get_seqs($tva, $five_start, $five_end)};

      return {} unless defined($ref_seq) && $ref_seq =~ /^[ACGT]+$/;
      return {} unless defined($alt_seq) && $alt_seq =~ /^[ACGT]+$/;

      my $ref_score = $self->score5($ref_seq);
      my $alt_score = $self->score5($alt_seq);

      return {
        MaxEntScan_ref => $ref_score,
        MaxEntScan_ref_seq => $ref_seq,
        MaxEntScan_alt => $alt_score,
        MaxEntScan_alt_seq => $alt_seq,
        MaxEntScan_diff => $ref_score - $alt_score,
      }
    }

    if(overlap($vf->start, $vf->end, $three_start, $three_end)) {
      my ($ref_seq, $alt_seq) = @{$self->get_seqs($tva, $three_start, $three_end)};

      return {} unless defined($ref_seq) && $ref_seq =~ /^[ACGT]+$/;
      return {} unless defined($alt_seq) && $alt_seq =~ /^[ACGT]+$/;

      my $ref_score = $self->score3($ref_seq);
      my $alt_score = $self->score3($alt_seq);

      return {
        MaxEntScan_ref => $ref_score,
        MaxEntScan_ref_seq => $ref_seq,
        MaxEntScan_alt => $alt_score,
        MaxEntScan_alt_seq => $alt_seq,
        MaxEntScan_diff => $ref_score - $alt_score,
      }
    }
  }

  return {};
}

sub run_SWA {
  my ($self, $tva) = @_;

  my $vf = $tva->variation_feature;

  my %results;

  # get the donor reference and alternate sequence contexts
  my ($donor_ref_context, $donor_alt_context) = @{$self->get_seqs($tva, $vf->start - 8, $vf->end + 8)};

  if (defined($donor_ref_context)) {
    $results{'MES-SWA_donor_ref_context'} = $donor_ref_context;

    if ($donor_ref_context  =~ /^[ACGT]+$/) {
      my ($seq, $frame, $score) = @{$self->get_max_donor($donor_ref_context)};
      $results{'MES-SWA_donor_ref_seq'} = $seq;
      $results{'MES-SWA_donor_ref_frame'} = $frame;
      $results{'MES-SWA_donor_ref'} = $score;
    }
  }

  if (defined($donor_alt_context)) {
    $results{'MES-SWA_donor_alt_context'} = $donor_alt_context;

    if ($donor_alt_context  =~ /^[ACGT]+$/) {
      my ($seq, $frame, $score) = @{$self->get_max_donor($donor_alt_context)};
      $results{'MES-SWA_donor_alt_seq'} = $seq;
      $results{'MES-SWA_donor_alt_frame'} = $frame;
      $results{'MES-SWA_donor_alt'} = $score;

      if (defined(my $ref_comp_seq = $results{'MES-SWA_donor_ref_seq'})) {

        if ($vf->{start} == $vf->{end} && $tva->feature_seq =~ /^[ACGT]$/) {
          # for SNVs, compare to the same frame as the highest scoring ALT k-mer
          $ref_comp_seq = substr($donor_ref_context, $frame - 1, 9);
        }

        $results{'MES-SWA_donor_ref_comp_seq'} = $ref_comp_seq;
        $results{'MES-SWA_donor_ref_comp'} = $self->score5($ref_comp_seq);

        $results{'MES-SWA_donor_diff'} = $results{'MES-SWA_donor_ref_comp'} - $score;
      }
    }
  }

  # get the acceptor reference and alternate sequence contexts
  my ($acceptor_ref_context, $acceptor_alt_context) = @{$self->get_seqs($tva, $vf->start - 22, $vf->end + 22)};

  if (defined($acceptor_ref_context)) {
    $results{'MES-SWA_acceptor_ref_context'} = $acceptor_ref_context;

    if ($acceptor_ref_context  =~ /^[ACGT]+$/) {
      my ($seq, $frame, $score) = @{$self->get_max_acceptor($acceptor_ref_context)};
      $results{'MES-SWA_acceptor_ref_seq'} = $seq;
      $results{'MES-SWA_acceptor_ref_frame'} = $frame;
      $results{'MES-SWA_acceptor_ref'} = $score;
    }
  }

  if (defined($acceptor_alt_context)) {
    $results{'MES-SWA_acceptor_alt_context'} = $acceptor_alt_context;

    if ($acceptor_alt_context  =~ /^[ACGT]+$/) {
      my ($seq, $frame, $score) = @{$self->get_max_acceptor($acceptor_alt_context)};
      $results{'MES-SWA_acceptor_alt_seq'} = $seq;
      $results{'MES-SWA_acceptor_alt_frame'} = $frame;
      $results{'MES-SWA_acceptor_alt'} = $score;

      if (defined(my $ref_comp_seq = $results{'MES-SWA_acceptor_ref_seq'})) {

        if ($vf->{start} == $vf->{end} && $tva->feature_seq =~ /^[ACGT]$/) {
          # for SNVs, compare to the same frame as the highest scoring ALT k-mer
          $ref_comp_seq = substr($acceptor_ref_context, $frame - 1, 23);
        }

        $results{'MES-SWA_acceptor_ref_comp_seq'} = $ref_comp_seq;
        $results{'MES-SWA_acceptor_ref_comp'} = $self->score3($ref_comp_seq);

        $results{'MES-SWA_acceptor_diff'} = $results{'MES-SWA_acceptor_ref_comp'} - $score;
      }
    }
  }

  return \%results;
}

sub run_NCSS {
  my ($self, $tva) = @_;

  my $tv = $tva->transcript_variation;
  my $tr = $tva->transcript;

  my %results;

  if ($tv->intron_number) {

    my ($intron_numbers, $total_introns) = split(/\//, $tv->intron_number);
    my $intron_number = (split(/-/, $intron_numbers))[0];

    my $introns = $tr->get_all_Introns;

    my $intron_idx = $intron_number - 1;
    my $intron = $introns->[$intron_idx];

    if (defined(my $seq = $self->get_donor_seq_from_intron($intron))) {
      $results{'MES-NCSS_upstream_donor_seq'} = $seq;
      $results{'MES-NCSS_upstream_donor'} = $self->score5($seq) if $seq =~ /^[ACGT]+$/;
    }

    if (defined(my $seq = $self->get_acceptor_seq_from_intron($intron))) {
      $results{'MES-NCSS_downstream_acceptor_seq'} = $seq;
      $results{'MES-NCSS_downstream_acceptor'} = $self->score3($seq) if $seq =~ /^[ACGT]+$/;
    }

    # don't calculate an upstream acceptor score if the intron is the first in the transcript
    unless ($intron_number == 1) {
      my $upstream_intron = $introns->[$intron_idx - 1];

      if (defined(my $seq = $self->get_acceptor_seq_from_intron($upstream_intron))) {
        $results{'MES-NCSS_upstream_acceptor_seq'} = $seq;
        $results{'MES-NCSS_upstream_acceptor'} = $self->score3($seq) if $seq =~ /^[ACGT]+$/;
      }
    }

    # don't calculate a downstream donor score if the intron is the last in the transcript
    unless ($intron_number == $total_introns) {
      my $downstream_intron = $introns->[$intron_idx + 1];

      if (defined(my $seq = $self->get_donor_seq_from_intron($downstream_intron))) {
        $results{'MES-NCSS_downstream_donor_seq'} = $seq;
        $results{'MES-NCSS_downstream_donor'} = $self->score5($seq) if $seq =~ /^[ACGT]+$/;
      }
    }
  }

  elsif ($tv->exon_number) {

    my ($exon_numbers, $total_exons) = split(/\//, $tv->exon_number);
    my $exon_number = (split(/-/, $exon_numbers))[0];

    my $exons = $tr->get_all_Exons;

    my $exon_idx = $exon_number - 1;
    my $exon = $exons->[$exon_idx];

    # don't calculate upstream scores if the exon is the first in the transcript
    unless ($exon_number == 1) {
      my $upstream_exon = $exons->[$exon_idx - 1];

      if (defined(my $seq = $self->get_donor_seq_from_exon($upstream_exon))) {
        $results{'MES-NCSS_upstream_donor_seq'} = $seq;
        $results{'MES-NCSS_upstream_donor'} = $self->score5($seq) if $seq =~ /^[ACGT]+$/;
      }

      if (defined(my $seq = $self->get_acceptor_seq_from_exon($exon))) {
        $results{'MES-NCSS_upstream_acceptor_seq'} = $seq;
        $results{'MES-NCSS_upstream_acceptor'} = $self->score3($seq) if $seq =~ /^[ACGT]+$/;
      }
    }

    # don't calculate downstream scores if the exon is the last exon in the transcript
    unless ($exon_number == $total_exons) {
      my $downstream_exon = $exons->[$exon_idx + 1];

      if (defined(my $seq = $self->get_donor_seq_from_exon($exon))) {
        $results{'MES-NCSS_downstream_donor_seq'} = $seq;
        $results{'MES-NCSS_downstream_donor'} = $self->score5($seq) if $seq =~ /^[ACGT]+$/;
      }

      if (defined(my $seq = $self->get_acceptor_seq_from_exon($downstream_exon))) {
        $results{'MES-NCSS_downstream_acceptor_seq'} = $seq;
        $results{'MES-NCSS_downstream_acceptor'} = $self->score3($seq) if $seq =~ /^[ACGT]+$/;
      }
    }
  }

  return \%results;
}


## Sliding window approach methods
##################################

sub get_max_donor {
  my ($self, $sequence) = @_;

  my ($seq, $frame, $max);
  my @kmers = @{$self->sliding_window($sequence, 9)};

  for my $i (0 .. $#kmers) {
    my $kmer = $kmers[$i];
    my $score = $self->score5($kmer);
    if(!$max || $score > $max) {
      $seq = $kmer;
      $frame = $i + 1;
      $max = $score;
    }
  }
  return [$seq, $frame, $max];
}

sub get_max_acceptor {
  my ($self, $sequence) = @_;

  my ($seq, $frame, $max);
  my @kmers = @{$self->sliding_window($sequence, 23)};

  for my $i (0 .. $#kmers) {
    my $kmer = $kmers[$i];
    my $score = $self->score3($kmer);
    if(!$max || $score > $max) {
      $seq = $kmer;
      $frame = $i + 1;
      $max = $score;
    }
  }
  return [$seq, $frame, $max];
}

sub sliding_window {
  my ($self, $sequence, $winsize) = @_;
  my @seqs;
  for (my $i = 1; $i <= length($sequence) - $winsize + 1; $i++) {
    push @seqs, substr($sequence, $i - 1, $winsize);
  }
  return \@seqs;
}


## Nearest canonical splice site methods
########################################

sub get_donor_seq_from_exon {
  my ($self, $exon) = @_;

  my ($start, $end);

  if ($exon->strand > 0) {
    ($start, $end) = ($exon->end - 2, $exon->end + 6);
  }
  else {
    ($start, $end) = ($exon->start - 6, $exon->start + 2);
  }

  my $slice = $exon->slice()->sub_Slice($start, $end, $exon->strand);
  my $seq = $slice->seq() if defined($slice);

  return $seq;
}

sub get_acceptor_seq_from_exon {
  my ($self, $exon) = @_;

  my ($start, $end);

  if ($exon->strand > 0) {
    ($start, $end) = ($exon->start - 20, $exon->start + 2);
  }
  else {
    ($start, $end) = ($exon->end - 2, $exon->end + 20);
  }

  my $slice = $exon->slice()->sub_Slice($start, $end, $exon->strand);
  my $seq = $slice->seq() if defined($slice);

  return $seq;
}

sub get_donor_seq_from_intron {
  my ($self, $intron) = @_;

  my ($start, $end);

  if ($intron->strand > 0) {
    ($start, $end) = ($intron->start - 3, $intron->start + 5);
  }
  else {
    ($start, $end) = ($intron->end - 5, $intron->end + 3);
  }

  my $slice = $intron->slice()->sub_Slice($start, $end, $intron->strand);
  my $seq = $slice->seq() if defined($slice);

  return $seq;
}

sub get_acceptor_seq_from_intron {
  my ($self, $intron) = @_;

  my ($start, $end);

  if ($intron->strand > 0) {
    ($start, $end) = ($intron->end - 19, $intron->end + 3);
  }
  else {
    ($start, $end) = ($intron->start - 3, $intron->start + 19);
  }

  my $slice = $intron->slice()->sub_Slice($start, $end, $intron->strand);
  my $seq = $slice->seq() if defined($slice);

  return $seq;
}


## Common methods
#################

sub get_seqs {
  my ($self, $tva, $start, $end) = @_;
  my $vf = $tva->variation_feature;

  my $tr_strand = $tva->transcript->strand;

  my $ref_slice = $vf->{slice}->sub_Slice($start, $end, $tr_strand);

  my ($ref_seq, $alt_seq);

  if (defined $ref_slice) {

    $ref_seq = $alt_seq = $ref_slice->seq();

    my $substr_start = $tr_strand > 0 ? $vf->{start} - $start : $end - $vf->{end};
    my $feature_seq = $tva->seq_length > 0 ? $tva->feature_seq : '';

    substr($alt_seq, $substr_start, ($vf->{end} - $vf->{start}) + 1) = $feature_seq;
  }

  return [$ref_seq, $alt_seq];
}

sub score5 {
  my $self = shift;
  my $seq = shift;
  my $hex = md5_hex($seq);

  # check cache
  if($self->{cache}) {
    my ($res) = grep {$_->{hex} eq $hex} @{$self->{cache}->{score5}};

    return $res->{score} if $res; 
  }

  my $a = $self->score5_scoreconsensus($seq);
  die("ERROR: No score5_scoreconsensus\n") unless defined($a);

  my $b = $self->score5_getrest($seq);
  die("ERROR: No score5_getrest\n") unless defined($b);

  my $c = $self->{'score5_seq'}->{$b};
  die("ERROR: No score5_seq for $b\n") unless defined($c);

  my $d = $self->{'score5_me2x5'}->{$c};
  die("ERROR: No score5_me2x5 for $c\n") unless defined($d);

  my $score = $self->log2($a * $d);

  # cache it
  push @{$self->{cache}->{score5}}, { hex => $hex, score => $score };
  shift @{$self->{cache}->{score5}} while scalar @{$self->{cache}->{score5}} > $CACHE_SIZE;

  return $score;
}

sub score3 {
  my $self = shift;
  my $seq = shift;
  my $hex = md5_hex($seq);

  # check cache
  if($self->{cache}) {
    my ($res) = grep {$_->{hex} eq $hex} @{$self->{cache}->{score3}};

    return $res->{score} if $res; 
  }

  my $a = $self->score3_scoreconsensus($seq);
  die("ERROR: No score3_scoreconsensus\n") unless defined($a);

  my $b = $self->score3_getrest($seq);
  die("ERROR: No score3_getrest\n") unless defined($b);

  my $c = $self->score3_maxentscore($b, $self->{'score3_metables'});
  die("ERROR: No score3_maxentscore for $b\n") unless defined($c);

  my $score = $self->log2($a * $c);

  # cache it
  push @{$self->{cache}->{score3}}, { hex => $hex, score => $score };
  shift @{$self->{cache}->{score3}} while scalar @{$self->{cache}->{score3}} > $CACHE_SIZE;

  return $score;
}


## methods copied from score5.pl
################################

sub score5_makesequencematrix {
  my $self = shift;
  my $file = shift;
  my %matrix;
  my $n=0;
  open(SCOREF, $file) || die "Can't open $file!\n";
  while(<SCOREF>) { 
    chomp;
    $_=~ s/\s//;
    $matrix{$_} = $n;
    $n++;
  }
  close(SCOREF);
  return \%matrix;
}

sub score5_makescorematrix {
  my $self = shift;
  my $file = shift;
  my %matrix;
  my $n=0;
  open(SCOREF, $file) || die "Can't open $file!\n";
  while(<SCOREF>) { 
    chomp;
    $_=~ s/\s//;
    $matrix{$n} = $_;
    $n++;
  }
  close(SCOREF);
  return \%matrix;
}

sub score5_getrest {
  my $self = shift;
  my $seq = shift;
  my @seqa = split(//,uc($seq));
  return $seqa[0].$seqa[1].$seqa[2].$seqa[5].$seqa[6].$seqa[7].$seqa[8];
}

sub score5_scoreconsensus {
  my $self = shift;
  my $seq = shift;
  my @seqa = split(//,uc($seq));
  my %bgd; 
  $bgd{'A'} = 0.27; 
  $bgd{'C'} = 0.23; 
  $bgd{'G'} = 0.23; 
  $bgd{'T'} = 0.27;  
  my %cons1;
  $cons1{'A'} = 0.004;
  $cons1{'C'} = 0.0032;
  $cons1{'G'} = 0.9896;
  $cons1{'T'} = 0.0032;
  my %cons2;
  $cons2{'A'} = 0.0034; 
  $cons2{'C'} = 0.0039; 
  $cons2{'G'} = 0.0042; 
  $cons2{'T'} = 0.9884;
  my $addscore = $cons1{$seqa[3]}*$cons2{$seqa[4]}/($bgd{$seqa[3]}*$bgd{$seqa[4]}); 
  return $addscore;
}

sub log2 {
  my ($self, $val) = @_;
  return log($val)/log(2);
}


## methods copied from score3.pl
################################

sub score3_hashseq {
  #returns hash of sequence in base 4
  # $self->score3_hashseq('CAGAAGT') returns 4619
  my $self = shift;
  my $seq = shift;
  $seq = uc($seq);
  $seq =~ tr/ACGT/0123/;
  my @seqa = split(//,$seq);
  my $sum = 0;
  my $len = length($seq);
  my @four = (1,4,16,64,256,1024,4096,16384);
  my $i=0;
  while ($i<$len) {
    $sum+= $seqa[$i] * $four[$len - $i -1] ;
    $i++;
  }
  return $sum;
}

sub score3_makemaxentscores {
  my $self = shift;
  my $dir = $self->{'_dir'}."/splicemodels/";
  my @list = ('me2x3acc1','me2x3acc2','me2x3acc3','me2x3acc4',
    'me2x3acc5','me2x3acc6','me2x3acc7','me2x3acc8','me2x3acc9');
  my @metables;
  my $num = 0 ;
  foreach my $file (@list) {
    my $n = 0;
    open (SCOREF,"<".$dir.$file) || die "Can't open $file!\n";
    while(<SCOREF>) {
      chomp;
      $_=~ s/\s//;
      $metables[$num]{$n} = $_;
      $n++;
    }
    close(SCOREF);
    #print STDERR $file."\t".$num."\t".$n."\n";
    $num++;
  }
  return \@metables;
}

sub score3_maxentscore {
  my $self = shift;
  my $seq = shift;
  my $table_ref = shift;
  my @metables = @$table_ref;
  my @sc;
  $sc[0] = $metables[0]{$self->score3_hashseq(substr($seq,0,7))};
  $sc[1] = $metables[1]{$self->score3_hashseq(substr($seq,7,7))};
  $sc[2] = $metables[2]{$self->score3_hashseq(substr($seq,14,7))};
  $sc[3] = $metables[3]{$self->score3_hashseq(substr($seq,4,7))};
  $sc[4] = $metables[4]{$self->score3_hashseq(substr($seq,11,7))};
  $sc[5] = $metables[5]{$self->score3_hashseq(substr($seq,4,3))};
  $sc[6] = $metables[6]{$self->score3_hashseq(substr($seq,7,4))};
  $sc[7] = $metables[7]{$self->score3_hashseq(substr($seq,11,3))};
  $sc[8] = $metables[8]{$self->score3_hashseq(substr($seq,14,4))};
  my $finalscore = $sc[0] * $sc[1] * $sc[2] * $sc[3] * $sc[4] / ($sc[5] * $sc[6] * $sc[7] * $sc[8]);
  return $finalscore;
}

sub score3_getrest {
  my $self = shift;
  my $seq = shift;
  my $seq_noconsensus = substr($seq,0,18).substr($seq,20,3);
  return $seq_noconsensus;
}

sub score3_scoreconsensus {
  my $self = shift;
  my $seq = shift;
  my @seqa = split(//,uc($seq));
  my %bgd; 
  $bgd{'A'} = 0.27; 
  $bgd{'C'} = 0.23; 
  $bgd{'G'} = 0.23; 
  $bgd{'T'} = 0.27;  
  my %cons1;
  $cons1{'A'} = 0.9903;
  $cons1{'C'} = 0.0032;
  $cons1{'G'} = 0.0034;
  $cons1{'T'} = 0.0030;
  my %cons2;
  $cons2{'A'} = 0.0027; 
  $cons2{'C'} = 0.0037; 
  $cons2{'G'} = 0.9905; 
  $cons2{'T'} = 0.0030;
  my $addscore = $cons1{$seqa[18]} * $cons2{$seqa[19]}/ ($bgd{$seqa[18]} * $bgd{$seqa[19]}); 
  return $addscore;
}

1;

