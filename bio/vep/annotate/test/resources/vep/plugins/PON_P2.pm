=head1 NAME
 PON_P2
 
=head1 SYNOPSIS
 mv PON_P2.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin PON_P2,/path/to/python/script/ponp2.py,hg37
 
=head1 CONTACT
Abhishek Niroula <abhishek.niroula@med.lu.se>
Mauno Vihinen <mauno.vihinen@med.lu.se>

=head1 DESCRIPTION
 This plugin for Ensembl Variant Effect Predictor (VEP) computes the predictions of PON-P2
 for amino acid substitutions in human proteins. PON-P2 is developed and maintained by
 Protein Structure and Bioinformatics Group at Lund University and is available at 
 http://structure.bmc.lu.se/PON-P2/.
 
 To run this plugin, you will require a python script and its dependencies (Python,
 python suds). The python file can be downloaded from http://structure.bmc.lu.se/PON-P2/vep.html/
 and the complete path to this file must be supplied while using this plugin.

=cut

package PON_P2;


use strict;
use warnings;


use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);
use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);


sub feature_types {
	return ['Transcript'];
}


sub get_header_info {
	return {
		PON_P2 => "PON-P2 prediction and score for amino acid substitutions"
	};
}


sub new {
	my $class = shift;
	my $self = $class->SUPER::new(@_);
	# get parameters
	my $command = $self->params->[0];
	my $Hg = $self->params->[1];
	die 'ERROR: Path to python script not specified! Specify path to python script e.g. --plugin PON_P2,/path/to/python/client/for/ponp2.py,[hg37/hg38]\n' unless defined($command);
	die 'ERROR: Reference genome not specified! Specify the reference genome after the path to python file e.g. --plugin PON_P2,/path/to/python/client/for/ponp2.py,[hg37/hg38]\n' unless defined($command);
	die "ERROR: Wrong reference genome specified! It should be either 'hg37' or 'hg38'\n" unless ($Hg ~~ ["hg37","hg38"]);
	die 'ERROR: Incorrect path to ponp2.py\n' unless -e $command;
	$self->{command} = $command;
	$self->{Hg} = $Hg;
	return $self;
}


sub run {
	my ($self, $tva) = @_;

	# only for missense variants
	return {} unless grep {$_->SO_term eq 'missense_variant'} @{$tva->get_all_OverlapConsequences};

	## Now get the variation features
	my $vf=$tva -> variation_feature;

	## If not snp return
	return {} unless $vf->{start} eq $vf->{end};

	## get allele, reverse comp if needed
	my $allele = $tva -> variation_feature_seq;
	my $Variation = $tva -> hgvs_genomic;
	my ($Chr, $Pos, $Alt) = (split /:g.|>/, $Variation)[0,1,2];
	my $Position = substr $Pos, 0, -1;
	my $Ref = substr $Pos, -1;
	
	## Check for single nucleotide substitution
	return {} unless $Ref =~ /^[ACGT]$/;
	return {} unless $Alt =~ /^[ACGT]$/;

	my $command = $self -> {command};
	my $Hg = $self -> {Hg};
	my $V = $Chr."_".$Position."_".$Ref."_".$Alt;;

	## Call pon-p2 python script here
	my $ponp2Res = `python $command $V $Hg` or return {};
	$ponp2Res =~ s/\R//g;

	my ($pred, $prob) =split /\t/, $ponp2Res;

	## Can PON-P2 predict?
	return {} if $pred eq "cannot";

	## Return predictions
	return $pred && $prob ? {
		PON_P2 => "$pred($prob)",
	} : {};
}

1;
