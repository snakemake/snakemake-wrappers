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

 Mastermind

=head1 SYNOPSIS

 mv Mastermind.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin Mastermind,/path/to/data.vcf.gz
 ./vep -i variations.vcf --plugin Mastermind,/path/to/data.vcf.gz,1

=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 uses the Mastermind Genomic Search Engine (https://www.genomenon.com/mastermind)
 to report variants that have clinical evidence cited in the medical literature. 
 It is available for both GRCh37 and GRCh38.

 Running options:
 (Option 1) By default, this plugin matches the citation data with the specific mutation.
 (Option 2) It can be run with the flag '1' to return the citations for all mutations/transcripts.   

 Output: 
 The output includes three unique counts 'MMCNT1, MMCNT2, MMCNT3' and one identifier 'MMID3'
 to be used to build an URL which shows all articles from MMCNT3.

 'MMCNT1' is the count of Mastermind articles with cDNA matches for a specific variant;
 'MMCNT2' is the count of Mastermind articles with variants either explicitly matching at
 the cDNA level or given only at protein level;
 'MMCNT3' is the count of Mastermind articles including other DNA-level variants resulting
 in the same amino acid change;
 'MMID3' is the Mastermind variant identifier(s), as gene:key, for MMCNT3;

 To build the URL, substitute the 'gene:key' in the following link with the value from MMID3:
 https://mastermind.genomenon.com/detail?disease=all%20diseases&gene=gene&mutation=gene:key
  
 More information can be found at: https://www.genomenon.com/cvr/


 The following steps are necessary before running this plugin:
 
 Download and Registry (free): 
 https://www.genomenon.com/cvr/ 
 
 GRCh37 VCF:
 unzip mastermind_cited_variants_reference-XXXX.XX.XX-grch37-vcf.zip
 bgzip mastermind_cited_variants_reference-XXXX.XX.XX-GRCh37-vcf
 tabix -p vcf mastermind_cited_variants_reference-XXXX.XX.XX.GRCh37-vcf.gz

 GRCh38 VCF:
 unzip mastermind_cited_variants_reference-XXXX.XX.XX-grch38-vcf.zip
 bgzip mastermind_cited_variants_reference-XXXX.XX.XX-GRCh38-vcf
 tabix -p vcf mastermind_cited_variants_reference-XXXX.XX.XX.GRCh38-vcf.gz
  
 
 The plugin can then be run as default (Option 1):
 ./vep -i variations.vcf --plugin Mastermind,/path/to/mastermind_cited_variants_reference-XXXX.XX.XX.GRChXX-vcf.gz

 or with an option to not filter by mutations (Option 2): 
 ./vep -i variations.vcf --plugin Mastermind,/path/to/mastermind_cited_variants_reference-XXXX.XX.XX.GRChXX-vcf.gz,1 


 Note: While running this plugin as default, i.e. filtering by mutation, if a variant doesn't affect 
       the protein sequence, the citation data can be appended to a transcript with different consequence.
 Example
  VEP: upstream_gene_variant
  Mastermind: intronic
  VEP output: var_1|1:154173185-154173187|C|ENSG00000143549|ENST00000368545|Transcript|upstream_gene_variant|
    -|-|-|-|-|-|IMPACT=MODIFIER;DISTANCE=508;STRAND=-1;Mastermind_MMID3=TPM3:E62int;Mastermind_counts=1|1|1;


=cut

package Mastermind;

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

  $self->get_user_params();

  die("ERROR: Mastermind input file not specified or found!\n") unless defined($self->params->[0]) && -e $self->params->[0];

  $self->{file} = $self->params->[0];

  if(defined($self->params->[1])) {
    $self->{mutation_off} = $self->params->[1];
  }

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {

  return{
     'Mastermind_counts'  => 'Mastermind number of citations in the medical literature. Output includes three unique counts: MMCNT1|MMCNT2|MMCNT3. MMCNT1 - Count of Mastermind articles with cDNA matches for this specific variant; MMCNT2 - Count of Mastermind articles with variants either explicitly matching at the cDNA level or given only at protein level; MMCNT3 - Count of Mastermind articles including other DNA-level variants resulting in the same amino acid change.',
     'Mastermind_MMID3'  => 'Mastermind MMID3 variant identifier(s), as gene:key, for MMCNT3.',
  };

}

sub run {
  my ($self, $tva) = @_;

  my $vf = $tva->variation_feature;
  my $tv = $tva->transcript_variation;
  my $chr = $vf->{chr};

  my $chr_syn;
  my @new_chr_array;
  my $new_chr;

  $self->parse_chromosome_synonyms($self->config->{'synonyms'}) if $self->config->{cache} && (not defined($self->{config}->{_chromosome_synonyms}));

  if(defined($self->{syn_cache}->{$chr})) {
    $new_chr = $self->{syn_cache}->{$chr};
  }
  else {
    if($self->config->{database}) {
      my $srs_adaptor = $vf->slice->adaptor->db->get_SeqRegionSynonymAdaptor();
      $chr_syn = $srs_adaptor->get_synonyms( $vf->slice->get_seq_region_id($vf->slice) );
      @new_chr_array = map {$_->{name}} (grep {$_->{name} =~ 'NC_'} @{$chr_syn});
    }
    elsif($self->config->{cache}) {
      $chr_syn = $self->config->{_chromosome_synonyms}->{($vf->{chr})};
      @new_chr_array = grep(/NC_/, keys %{$chr_syn});
      if (! @new_chr_array && ($vf->{chr} =~ /^chr/)) {
        my $tmp_chr = $vf->{chr};
        $tmp_chr =~ s/^chr//i;
        $chr_syn = $self->config->{_chromosome_synonyms}->{$tmp_chr};
        @new_chr_array = grep(/NC_/, keys %{$chr_syn});
      }
    }

    return {} unless scalar(@new_chr_array);
    $new_chr = shift(@new_chr_array);
    $self->{syn_cache}->{$chr} = $new_chr;
  }

  my $ref_allele;
  my $alt_allele;

  # convert to vcf format to compare the alleles
  if($vf->allele_string =~ /-/) {
    my $convert_to_vcf = $vf->to_VCF_record;
    $ref_allele = ${$convert_to_vcf}[3];
    $alt_allele = ${$convert_to_vcf}[4];
  }
  else { 
    my @alleles = split /\//, $vf->allele_string;
    $ref_allele = shift @alleles;
    $alt_allele = shift @alleles;
  }

  my $end = $vf->{end};
  my $start = $vf->{start};
  ($start, $end) = ($end, $start) if $start > $end;

  my @data = @{$self->get_data($new_chr, $start, $end)} if(defined $new_chr);

  return {} unless(@data);

  my $result_data;

  foreach my $data_value (@data) {

    if($data_value->{data}) {
      my $ref_allele_comp = $ref_allele;
      my $alt_allele_comp = $alt_allele;
      reverse_comp(\$ref_allele_comp);
      reverse_comp(\$alt_allele_comp);

      # Ref and alt alleles from mastermind file
      my $mm_ref = $data_value->{ref};
      my $mm_alt = $data_value->{alt};

      if( ($ref_allele eq $mm_ref && $alt_allele eq $mm_alt) || ($ref_allele_comp eq $mm_ref && $alt_allele_comp eq $mm_alt) ) {

        # Only checks the genomic location - appends data for all transcripts
        if($self->{mutation_off}){
          $result_data = $data_value->{result};
          next;
        }

        # checks by mutation
        my $peptide_start = defined($tv->translation_start) ? $tv->translation_start : undef;
        my $peptide_end = defined($tv->translation_end) ? $tv->translation_end : undef;
        my $aa_alterations = $data_value->{aa};
        my $aa_string = $tv->pep_allele_string;
        my $is_intron = $tv->intron_number();
        my $has_cdna = $tv->cdna_start();
        my $is_5utr = $tv->_five_prime_utr();
        my $is_3utr = $tv->_three_prime_utr();

        foreach my $aa_alteration (@$aa_alterations) {

          # checks if citation refers to an UTR variant
          if($data_value->{is_utr} == 1 && !defined($is_intron) && defined($has_cdna) && (defined($is_5utr) || defined($is_3utr))) {
            $result_data = $data_value->{result};
          }
          # checks if it is a frameshift or nonsense
          elsif($data_value->{is_fs} == 1 && $aa_string =~ /X/) {
            $result_data = $data_value->{result};
          }
          elsif($data_value->{is_other} == 1 && !defined($has_cdna)) {
            $result_data = $data_value->{result};
          }

          # If mastermind aa change is UTR then skips aa verification
          next unless $aa_alteration !~ /UTR/;

          # If there's a protein alteration then it only adds citations for the exact alteration cited
          if(defined($aa_alteration) && defined($peptide_start) && defined($peptide_end) && ($peptide_start == $aa_alteration || $peptide_end == $aa_alteration)) {
            $result_data = $data_value->{result};
          }
        }
      }

    }

  }

  my $result = defined($result_data) ? $result_data : {};

  return $result;
}

# Parse data from mastermind file
sub parse_data {
  my ($self, $line) = @_;

  my ($chr, $start, $id, $ref, $alt, $x, $xx, $data) = split /\t/, $line;

  my ($mmcnt1, $mmcnt2, $mmcnt3, $mmid3);
  my @data_splited = split /;/, $data;
  foreach my $value (@data_splited){
    $mmcnt1 = $value if $value =~ /MMCNT1/;
    $mmcnt2 = $value if $value =~ /MMCNT2/;
    $mmcnt3 = $value if $value =~ /MMCNT3/;
    $mmid3  = $value if $value =~ /MMID3/;
  }

  my $mm_data = $mmcnt1 . ';' . $mmcnt2 . ';' . $mmcnt3 . ';' . $mmid3;

  # Frameshift or nonsense
  my $is_fs = 0;
  # UTR 
  my $is_utr = 0;
  # Intronic or splice
  my $is_other = 0;

  if($mmid3 =~ /fs|([0-9]+X)/) {
    $is_fs = 1;
  }
  elsif($mmid3 =~ /UTR/) {
    $is_utr = 1;
  }
  elsif($mmid3 =~ /sa|sd|int/) {
    $is_other = 1;
  }

  $mmcnt1 =~ s/MMCNT1=//;
  $mmcnt2 =~ s/MMCNT2=//;
  $mmcnt3 =~ s/MMCNT3=//;
  $mmid3  =~ s/MMID3=//;

  my %mm_hash;
  $mm_hash{'Mastermind_counts'} = $mmcnt1.'|'.$mmcnt2.'|'.$mmcnt3;
  $mm_hash{'Mastermind_MMID3'} = $mmid3;

  my @aa_alterations = split /,/, $mmid3;

  foreach my $aa_alteration (@aa_alterations) {
    $aa_alteration =~ s/.*\:[A-Za-z]+//;
    $aa_alteration =~ s/[A-Za-z]+|\*//;
  }

  return {
    chr    => $chr,
    start  => $start,
    ref    => $ref,
    alt    => $alt,
    aa     => \@aa_alterations,
    data   => $mm_data,
    result => \%mm_hash,
    is_fs  => $is_fs,
    is_utr => $is_utr,
    is_other => $is_other,
  };
}

sub parse_chromosome_synonyms {
  my $self = shift;
  my $file = shift;

  if($file) {
    open INPUT, $file or throw("ERROR: Could not read synonyms file $file: $!");

    my $synonyms = $self->config->{_chromosome_synonyms} ||= {};

    while(<INPUT>) {
      chomp;
      my @split = split(/\s+/, $_);

      my $ref = shift @split;

      foreach my $syn(@split) {
        $synonyms->{$ref}->{$syn} = 1;
        $synonyms->{$syn}->{$ref} = 1;
      }
    }

    close INPUT;
  }

  return $self->config->{_chromosome_synonyms} ||= {};
}

1;
