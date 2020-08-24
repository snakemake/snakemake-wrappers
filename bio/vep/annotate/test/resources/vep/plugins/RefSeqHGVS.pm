=head1 NAME

 RefSeqHGVS -- provide RefSeq-based HGVS tags for VEP output

=head1 SYNOPSIS

 cp RefSeqHGVS.pm ~/.vep/Plugins/ (or elsewhere in PERL5LIB)
 perl variant_effect_predictor.pl -i variations.vcf --plugin RefSeqHGVS

 Output:
 Variant lines with the following addtiional tags:
     HGVSc-RefSeq=NM_198156.2:c.403delA;HGVSp-RefSeq=NP_937799.1:p.Arg135GlyfsX26

=head1 DESCRIPTION

 RefSeqHGVS is a plugin for Ensembl's Variant Effect Predictor that
 provides variant annotatoins in HGVS format [1] using RefSeq accessions
 (typically NM and NP).  It provides the analog to VEP's HGVSc and HGVSp
 annotations, which use Ensembl ENST and ENSP accessions.  This module
 relies RefSeq data in the OtherFeatures database.

 Converting ENST HGVS tags to RefSeq tags is confounded subtle differences
 between exon structures for the same CDS.  The plugin is intended to be
 conservative by requiring exact matches of both CDS and exon structure
 when converting variants.

 [1] http://www.hgvs.org/mutnomen/

=head1 BUGS AND LIMITATIONS

=over

=item * RefSeq transcripts limited to those in the OtherFeatures database. 

Archived RefSeq transcripts are not available.

=item * Discrepancies between RefSeq and GRCh37

 Approximately 20% of RefSeqs differ from the GRCh37 due to substitution
 (16.2%), insertion/deletion (3.5%), or both (1.2%) differences. [1]
 Variants are annotated by difference with respect to the genome, not the
 RefSeq transcript.

 [1] MU2A--reconciling the genome and transcriptome to determine the
 effects of base substitutions.
﻿Garla, V., Kong, Y., Szpakowski, S., & Krauthammer, M. (2011). 
 Bioinformatics, 27(3), 416-8. doi:10.1093/bioinformatics/btq658
 https://www.ncbi.nlm.nih.gov/pubmed/21149339

=item * Conservative selection of equivalent RefSeq transcripts.

Only NM transcripts which are exactly identical to the ENST transcript in
both CDS and exon structure are used.  In the future, this might be
relaxed to exclude only regions of mismatch.  Currently, this implies that
HGVS tags are not constructued when the RefSeq differs from the reference
geneome.

=back

=head1 CONTACT

 Reece Hart <reecehart@gmail.com>

=head1 LICENSE

 This code and all rights to it are hereby donated to EnsEMBL project by
 Reece Hart and Locus Development.

 Copyright (c) 1999-2011 The European Bioinformatics Institute and
 Genome Research Limited.  All rights reserved.

 This software is distributed under a modified Apache license.
 For license details, please see

   http://www.ensembl.org/info/about/code_licence.html

=cut


package RefSeqHGVS;

use strict;
use warnings;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

use Data::Dumper;

my %mt_cache;								# cache of ENST -> NM mappings

sub version {
  return '2.3';
}

sub new {
  my $class = shift;
  my $self = $class->SUPER::new(@_);
  my $reg = 'Bio::EnsEMBL::Registry';

  $self->{ofsa} = $reg->get_adaptor('Human', 'otherfeatures', 'Slice')
	or die "Failed to create transcript adaptor in human otherfeatures database\n";
  $self->{ofta} = $reg->get_adaptor('Human', 'otherfeatures', 'Transcript')
	or die "Failed to create transcript adaptor in human otherfeatures database\n";

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub variant_feature_types {
  return ['VariationFeature'];
}

sub get_header_info {
  return {
	'HGVSc-RefSeq' => "HGVSc using RefSeq transcripts accessions",
	'HGVSp-RefSeq' => "HGVSp using RefSeq protein accessions",
  };
}

sub run {
  my ($self, $tva) = @_;
  my $t = $tva->transcript;
  my %rv;

  my $ofsa = $self->{ofsa};
  my $ofta = $self->{ofta};

  # mappabale_transcripts have identical CDS and exon structure
  my @mappable_transcripts = $self->get_mappable_transcripts($t);
  my @transcript_acs = map { $_->display_id() } @mappable_transcripts;
  my @protein_acs = grep {defined $_} map { $_->translation()->display_id() } @mappable_transcripts;

  # substitute accessions for those in mappable transcripts/proteins
  my @hgvsc_rs;
  if (defined (my $hgvsc = $tva->hgvs_coding())) {
	@hgvsc_rs = map {__subst_hgvs_ac($hgvsc ,$_)} @transcript_acs;
  }
  my @hgvsp_rs;
  if (defined (my $hgvsp = $tva->hgvs_protein())) {
	@hgvsp_rs = map {__subst_hgvs_ac($hgvsp,$_)} @protein_acs;
  }

  $rv{'HGVSc-RefSeq'} = join(';',@hgvsc_rs) if @hgvsc_rs;
  $rv{'HGVSp-RefSeq'} = join(';',@hgvsp_rs) if @hgvsp_rs;
  return \%rv;
}


sub get_mappable_transcripts {
  my ($self,$t) = @_;
  my $key = $t->display_id();
  if (not exists $mt_cache{$key}) {
	@{$mt_cache{$key}} = $self->_get_mappable_transcripts($t);
  }
  return @{$mt_cache{$key}};
}


############################################################################
## internal methods
sub _get_mappable_transcripts {
  my ($self,$t) = @_;
  my $cds_seq = $t->translateable_seq();
  my $exon_structure = __tx_exon_str($t);

  # cds_seq is empty for pseudogenes; no mapping possible
  return () if ($cds_seq eq '');

  # get overlapping transcripts from other features
  my @tx = @{ $self->{ofta}->fetch_all_by_Slice($t->feature_Slice()) };

  # limit to NMs with standard-format
  @tx = grep { $_->display_id() =~ m/^NM_\d+\.\d+$/ } @tx;

  # limit to transcripts with same CDS
  @tx = grep { $_->translateable_seq() eq $cds_seq } @tx;

  # limit to transcripts with identical chromosomal exon structure
  @tx = grep { __tx_exon_str($_->transform('chromosome')) eq $exon_structure } @tx;

  return @tx;
}


############################################################################
## function (not methods)

sub __tx_exon_str {
  my $t = shift;
  return join(',', map {sprintf('[%s,%s]', $_->start(), $_->end())} 
				@{ $t->get_all_translateable_Exons() } );
}

sub __subst_hgvs_ac {
  my ($hgvs,$ac) = @_;
  $hgvs =~ s/^[^:]+:/$ac:/;
  return $hgvs;
}

sub __uniq {
  return keys %{{ map {$_=>1} @_ }};
}


1;
