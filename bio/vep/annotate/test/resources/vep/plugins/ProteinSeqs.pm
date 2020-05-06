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

 ProteinSeqs

=head1 SYNOPSIS

 mv ProteinSeqs.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin ProteinSeqs,reference.fa,mutated.fa

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 prints out the reference and mutated protein sequences of any
 proteins found with non-synonymous mutations in the input file. 

 You should supply the name of file where you want to store the
 reference protein sequences as the first argument, and a file to
 store the mutated sequences as the second argument.

 Note that, for simplicity, where stop codons are gained the plugin 
 simply substitutes a '*' into the sequence and does not truncate the 
 protein. Where a stop codon is lost any new amino acids encoded by the 
 mutation are appended to the sequence, but the plugin does not attempt 
 to translate until the next downstream stop codon. Also, the protein
 sequence resulting from each mutation is printed separately, no attempt
 is made to apply multiple mutations to the same protein.

=cut

package ProteinSeqs;

use strict;
use warnings;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub version {
    return '2.4';
}

sub feature_types {
    return ['Transcript'];
}

sub new {
    my $class = shift;

    my $self = $class->SUPER::new(@_);

    if($self->{config}->{fork}) {
      print STDERR "WARNING: Plugin ProteinSeqs is disabling forking\n" unless $self->{config}->{quiet};
      delete($self->{config}->{fork});
    }

    # use some default file names if none are supplied

    my $ref_file = $self->params->[0] || 'reference.fa';
    my $mut_file = $self->params->[1] || 'mutated.fa';

    open $self->{ref_file}, ">$ref_file" or die "Failed to open $ref_file";
    open $self->{mut_file}, ">$mut_file" or die "Failed to open $mut_file";

    return $self;
}

sub run {
    my ($self, $tva) = @_;

    # check if we have a mutant amino acid, if not there isn't much we can do!

    if (my $mut_aa = $tva->peptide) {
        
	return {} if !defined($tva->hgvs_protein);
        
	# get the peptide coordinates
	
	my $tl_start = $tva->transcript_variation->translation_start;
        my $tl_end = $tva->transcript_variation->translation_end;

        # and our reference sequence

        my $ref_seq = $tva->transcript_variation->_peptide;

        # splice the mutant peptide sequence into the reference sequence

        my $mut_seq = $ref_seq;

        substr($mut_seq, $tl_start-1, $tl_end - $tl_start + 1) = $mut_aa;

        # print out our reference and mutant sequences

        my $translation_id = $tva->transcript->translation->stable_id;
        
        # only print the reference sequence if we haven't printed it yet

        $self->print_fasta($ref_seq, $translation_id, $self->{ref_file})
            unless $self->{printed_ref}->{$translation_id}++;

        # we always print the mutated sequence as each mutation may have
        # a different consequence
        
        $self->print_fasta($mut_seq, $tva->hgvs_protein, $self->{mut_file});
    }

    # return an empty hashref because we don't want to add 
    # anything to the VEP output file

    return {};
}

sub print_fasta {
    my ($self, $peptide, $id, $fh) = @_;

    # break the sequence into 80 characters per line
    
    $peptide =~ s/(.{80})/$1\n/g;
    
    # get rid of any trailing newline
    
    chomp $peptide;

    # print the sequence

    print $fh ">$id\n$peptide\n";
}

sub STORABLE_freeze {
    my ($self, $cloning) = @_;
    return if $cloning;
    
    close $self->{ref_file};
    close $self->{mut_file};
    
    delete $self->{ref_file};
    delete $self->{ref_file};
}

sub STORABLE_thaw {
    my ($self, $cloning) = @_;
    return if $cloning;

    my $ref_file = $self->params->[0] || 'reference.fa';
    my $mut_file = $self->params->[1] || 'mutated.fa';

    open $self->{ref_file}, ">>$ref_file" or die "Failed to open $ref_file";
    open $self->{mut_file}, ">>$mut_file" or die "Failed to open $mut_file";
}

1;
