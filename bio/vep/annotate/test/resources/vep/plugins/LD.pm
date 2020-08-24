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

 LD

=head1 SYNOPSIS

 mv LD.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin LD,1000GENOMES:phase_3:CEU,0.8
 ./vep -i variations.vcf --plugin LD,'populations=1000GENOMES:phase_3:CEU&1000GENOMES:phase_3:PUR&1000GENOMES:phase_3:STU',0.8


=head1 DESCRIPTION

 This is a plugin for the Ensembl Variant Effect Predictor (VEP) that
 finds variants in linkage disequilibrium with any overlapping existing 
 variants from the Ensembl variation databases. You can configure the 
 population used to calculate the r2 value, and the r2 cutoff used by 
 passing arguments to the plugin via the VEP command line (separated 
 by commas). This plugin adds a single new entry to the Extra column 
 with a comma-separated list of linked variant IDs and the associated 
 r2 values, e.g.:

   LinkedVariants=rs123:0.879,rs234:0.943

 If no arguments are supplied, the default population used is the CEU
 sample from the 1000 Genomes Project phase 3, and the default r2
 cutoff used is 0.8.

 WARNING: Calculating LD is a relatively slow procedure, so this will 
 slow VEP down considerably when running on large numbers of
 variants. Consider running vep followed by filter_vep to get a smaller
 input set:

   ./vep -i input.vcf -cache -vcf -o input_vep.vcf
   ./filter_vep -i input_vep.vcf -filter "Consequence is missense_variant" > input_vep_filtered.vcf
   ./vep -i input_vep_filtered.vcf -cache -plugin LD

=cut

=head1 INSTALLATION

 LD calculation requires additional installation steps.

 The JSON perl library is required; see VEP's installation instructions
 for guidance: http://www.ensembl.org/info/docs/tools/vep/script/vep_download.html#additional

 A binary from the ensembl-variation git repository must be compiled and either
 added to your PATH or specified on the command line. In the ensembl-vep
 directory:

   export HTSLIB_DIR=${PWD}/htslib
   git clone https://github.com/Ensembl/ensembl-variation
   cd ensembl-variation/C_code
   make

 You may EITHER add this path to your PATH environment variable (add this line
 to your $HOME/.bashrc to make the change permanent):

   export PATH=${PATH}:${PWD}

 OR you may specify the full path to the ld_vcf binary on the vep command line:

   ./vep -i variations.vcf --plugin LD,1000GENOMES:phase_3:CEU,0.8,$PWD/ensembl-variation/C_code/ld_vcf

=cut

=head1 DATA

 By default genotype data to calculate LD is retrieved from tabix-indexed
 VCF files hosted on Ensembl's FTP servers. It is possible to download this
 data to your local machine and have the LD plugin read genotype data from
 there instead, giving faster performance and reducing network traffic.

 These commands show how to get the data files for GRCh38.

   mkdir variation_genotype
   cd variation_genotype
   lftp -e "mget ALL.chr*.phase3_shapeit2_mvncall_integrated_v3plus_nounphased.rsID.genotypes.GRCh38_dbSNP.vcf.gz*" ftp://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_genotype/
   cd ..

 For GRCh37 replace the lftp command with:

   lftp -e "mget ALL.chr*.phase3_shapeit2_mvncall_integrated_v3plus_nounphased.rsID.genotypes.vcf.gz*" ftp://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh37/variation_genotype/

 We must now modify the JSON configuration file used to find the data. Starting
 in the ensembl-vep directory:

   perl -pi -e "s|ftp://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38|$PWD|" Bio/EnsEMBL/Variation/DBSQL/vcf_config.json

 Or for GRCh37:

   perl -pi -e "s|ftp://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh37|$PWD|" Bio/EnsEMBL/Variation/DBSQL/vcf_config.json 

=cut

package LD;

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {
  my $self = shift;
  my $header = {};
  my $population_count = scalar @{$self->{populations}};  
  foreach my $population (@{$self->{populations}}) {
    my $population_name = $population->name;
    my $key = ($population_count > 1) ? "LinkedVariants_$population_name" : "LinkedVariants"; 
    $header->{$key} = "Variants in LD (r2 >= ".$self->{r2_cutoff}.
      ") with overlapping existing variants from the $population_name population"; 
  }
  return $header;
}

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  if ($self->config->{offline}) {
    warn "Warning: a connection to the database is required to calculate LD\n";
  }

  my $reg = 'Bio::EnsEMBL::Registry';

  # turn on the check for existing variants

  $self->config->{check_existing} = 1;

  # fetch our population

  my ($pop_name, $r2_cutoff, $ld_binary) = @{ $self->params };

  # set some defaults

  $pop_name ||= '1000GENOMES:phase_3:CEU';

  my @pop_names = ();
  if ($pop_name =~ /^populations=/) {
    $pop_name =~ s/populations=//;  
    my %unique_populations = map { $_ => 1 } split('&', $pop_name);
    push @pop_names, keys %unique_populations;
  } else {
    push @pop_names, $pop_name;
  }


  $r2_cutoff = 0.8 unless defined $r2_cutoff;

  my $pop_adap = $reg->get_adaptor('human', 'variation', 'population')
    || die "Failed to get population adaptor\n";

  $pop_adap->db->use_vcf(1);
  my $valid_pops = $pop_adap->fetch_all_vcf_Populations();

  my @populations = ();
  foreach my $pop_name (@pop_names) {
    my ($pop) = grep {$_->name eq $pop_name} @$valid_pops;
    die "Invalid population '$pop_name'; valid populations are:\n".join(", ", map {$_->name} @$valid_pops)."\n" unless $pop;
    push @populations, $pop;
  }

  $self->{populations} = \@populations;
  $self->{r2_cutoff} = $r2_cutoff;
  
  # prefetch the necessary adaptors
  
  my $ld_adap = $reg->get_adaptor('human', 'variation', 'ldfeaturecontainer')
    || die "Failed to get LD adaptor\n";
  $ld_adap->db->use_vcf(1);
  my $var_adap = $reg->get_adaptor('human', 'variation', 'variation')
    || die "Failed to get variation adaptor\n";
    
  my $var_feat_adap = $reg->get_adaptor('human', 'variation', 'variationfeature')
    || die "Failed to get variation feature adaptor\n";

  if($ld_binary) {
    die("Specified LD binary \"$ld_binary\" does not exist\n") unless -e $ld_binary;
    $Bio::EnsEMBL::Variation::DBSQL::LDFeatureContainerAdaptor::VCF_BINARY_FILE = $ld_binary;
  }
   
  $self->{ld_adap} = $ld_adap;
  $self->{var_adap} = $var_adap;
  $self->{var_feat_adap} = $var_feat_adap;

  return $self;
}

sub run {
  my ($self, $vfoa, $line_hash) = @_;

  # fetch the existing variants from the line hash
  return {} unless $line_hash->{Existing_variation};

  my @vars = ref($line_hash->{Existing_variation}) eq 'ARRAY' ? @{$line_hash->{Existing_variation}} : split(',', $line_hash->{Existing_variation});
  my @ld_results = ();
  for my $var (@vars) {
    # check cache
    my $res;
    if($self->{cache}) {
      ($res) = grep {$_->{var} eq $var} @{$self->{cache}};
    }
    unless($res) {
      my $all_ld_variants_by_population = {};
      if (my $v = $self->{var_adap}->fetch_by_name($var)) {
        for my $vf (@{ $self->{var_feat_adap}->fetch_all_by_Variation($v) }) {

          # we're only interested in variation features that overlap our variant
          my $vep_input_vf = $vfoa->variation_feature;
          
          my $vep_input_alt_allele = shift @{$vep_input_vf->alt_alleles};
          if ($vf->seq_region_name eq $vep_input_vf->seq_region_name && grep {$vep_input_alt_allele eq $_} @{$vf->alt_alleles} ) {

            foreach my $population (@{$self->{populations}}) {
              my @this_linked;
              # fetch an LD feature container for this variation feature and our preconfigured population
              if (my $ldfc = $self->{ld_adap}->fetch_by_VariationFeature($vf, $population)) {
              
                # loop over all the linked variants
                # we pass 1 to get_all_ld_values() so that it doesn't lazy load
                # VariationFeature objects - we only need the name here anyway
                for my $result (@{ $ldfc->get_all_ld_values(1) }) {
                  # apply our r2 cutoff
                  if ($result->{r2} >= $self->{r2_cutoff}) {
                    my $v1 = $result->{variation_name1};
                    my $v2 = $result->{variation_name2};
                    # I'm not sure which of these are the query variant, so just check the names
                    my $linked = $v1 eq $var ? $v2 : $v1;
                    push @this_linked, sprintf("%s:%.3f", $linked, $result->{r2});
                  }
                }
              }
              $all_ld_variants_by_population->{$population->name} = \@this_linked if (scalar @this_linked);
            }
          }
          if (scalar keys %$all_ld_variants_by_population) {
            # cache it
            $res = {
              var => $var,
              linked => $all_ld_variants_by_population,
            };
            push @ld_results, $res;
            push @{$self->{cache}}, $res;
            shift @{$self->{cache}} while scalar @{$self->{cache}} > 50;
          }
        }
      }
    } else { # end unless 
      push @ld_results, $res;
    }
    last if (scalar @ld_results);
  } # end foreach variation
  if (scalar @ld_results) {
    my $res = $ld_results[0];
    my $results = {};
    my $population_count = scalar keys %{$res->{linked}};  
    foreach my $population_name (keys %{$res->{linked}}) {
      my @linked_variants = @{$res->{linked}->{$population_name}};
      my $key = ($population_count > 1) ? "LinkedVariants_$population_name" : "LinkedVariants"; 
      $results->{$key} = join(',', @linked_variants);
    }
    return $results;
  }
  return {};
}

1;

