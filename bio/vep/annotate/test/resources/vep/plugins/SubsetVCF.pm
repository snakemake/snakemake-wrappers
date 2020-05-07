=head1 NAME

 SubsetVCF

=head1 DESCRIPTION

 A VEP plugin to retrieve overlapping records from a given VCF file.
 Values for POS, ID, and ALT, are retrieved as well as values for any requested
 INFO field. Additionally, the allele number of the matching ALT is returned.

 Though similar to using '--custom', this plugin returns all ALTs for a given
 POS, as well as all associated INFO values.

 By default, only VCF records with a filter value of "PASS" are returned, 
 however this behaviour can be changed via the 'filter' option.

 Parameters:
    name: short name added used as a prefix (required)
    file: path to tabix-index vcf file (required)
  filter: only consider variants marked as 'PASS', 1 or 0 (default, 1)
  fields: info fields to be returned (default, not used)
            '%' can delimit multiple fields
            '*' can be used as a wildcard 

 Returns:
  <name>_POS: POS field from VCF
  <name>_REF: REF field from VCF (minimised)
  <name>_ALT: ALT field from VCF (minimised)
  <name>_alt_index: Index of matching variant (zero-based)
  <name>_<field>: List of requested info values

=head1 SYNOPSIS

 ./vep -i variations.vcf --plugin SubsetVCF,file=filepath.vcf.gz,name=myvfc,fields=AC*%AN*

=head1 CONTACT
	
	Joseph A. Prinz <jp102@duke.edu>

=head1 LICENSE

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
			http://www.apache.org/licenses/LICENSE-2.0
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

=cut

package SubsetVCF;

use strict;
use warnings;

use Storable qw(dclone);
use Data::Dumper;

use Bio::EnsEMBL::Utils::Sequence qw(reverse_comp);
use Bio::EnsEMBL::Variation::Utils::Sequence qw(get_matched_variant_alleles);
use Bio::EnsEMBL::Variation::Utils::VEP qw(parse_line get_all_consequences);
use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;
use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub simple_vf {
  my ($vf, $params) = @_;
  my @alleles = split /\//, $vf->{allele_string};
  my $ref = shift @alleles;

  my @line;
  if (ref $vf->{_line} ne "ARRAY") {
    @line = split /\t/, $vf->{_line};
  } else {
    @line = @{$vf->{_line}};
  }

  # Use a particular allele if requested
  @alleles = ($params->{allele}) if $params->{allele};
  
  # Reverse comp if needed
  if ($vf->{strand} < 0) {
    @alleles = map { reverse_comp($_) } @alleles;
    $ref = reverse_comp($ref);
    $vf->{strand} = 1;
  }

  # Return values
  my $ret = {
      chr    => $vf->{chr},
      pos    => $vf->{start},
      start  => $vf->{start},
      end    => $vf->{end},
      strand => $vf->{strand},
      alts   => [@alleles],
      line   => [@line],
      ref    => $ref};

  # If filter is true, only return $ret if filter eq "PASS"
  return $params->{filter} && $line[6] ne "PASS" ? {} : $ret;
}

sub parse_info {
  my ($line, $valid_fields) = @_;
  my %ret;
  for my $dat (split /;/, $line->[7]) {
    my ($field, $val) = split /=/, $dat;
    if (grep { $field eq $_ } @$valid_fields) {
      $ret{$field} = [split /,/, $val];
    }
  }
  return \%ret;
}

sub new {
  my $class = shift;
  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);
  $self->get_user_params();

  # Get params and ensure a minumum number of parameters
  my $params = $self->params_to_hash();
  die "ERROR: no value for 'file' specified" if !$params->{file};
  die "ERROR: no value for 'name' specified" if !$params->{name};

  # Defaults
  $params->{filter} = 1 if !$params->{filter};

  # Add file via parameter hash
  $self->add_file($params->{file});
  $self->{filter} = $params->{filter};
  $self->{name} = $params->{name};

  if ($params->{fields}) {
    # Mung filter to turn AC*%AN* into AC[^,]+|AN[^,]+
    $params->{fields} =~ s/%/|/g;
    $params->{fields} =~ s/\*/[^,]*/g;

    # Get input file headers
    my %fields;
    my $info_regex = "^##INFO=<ID=($params->{fields}),.*Description=\"([^\"]+).*";
    open HEAD, "tabix -fh $params->{file} 1:1-1 2>&1 | ";
    while(my $line = <HEAD>) {
      next unless $line =~ $info_regex;
      $fields{$1} = $2;
    }
    die "Could not find any valid info fields" if not %fields;
    $self->{fields} = \%fields;
    $self->{valid_fields} = [keys %fields];
  }
  return $self;
}

sub feature_types {
  return ['Feature', 'Intergenic'];
}

sub get_header_info {
  my $self = shift;
  my %ret;

  # Add fields if requested
  if ($self->{fields}) {
    while (my ($field, $desc) = each %{$self->{fields}}) {
      $ret{"$self->{name}_$field"} = $desc;
    }
  }

  $ret{"$self->{name}_ID"} = "Original ID";
  $ret{"$self->{name}_POS"} = "Original POS";
  $ret{"$self->{name}_REF"} = "Original refrance allele";
  $ret{"$self->{name}_ALT"} = "Original alternatives as they appear in the VCF file";
  $ret{"$self->{name}_alt_index"} = "Index of matching alternative (zero-based)";
  return \%ret;
}

sub parse_data {
  my ($self, $line) = @_;
  my ($vf) = @{parse_line({format => 'vcf', minimal => 1}, $line)};
  return simple_vf($vf, {filter => $self->{filter}});
}

sub run {
  my ($self, $tva) = @_;
  my $vf = simple_vf($tva->variation_feature, {allele => $tva->{variation_feature_seq}});
  
  # Zero-indexing start for tabix and adding 1 to end for VEP indels
  my @data = @{$self->get_data($vf->{chr}, ($vf->{start} - 1), ($vf->{end} + 1))};

  my (%ret, $found_vf, @matches);
  for my $dat (@data) {
    next unless %$dat;
    @matches = @{get_matched_variant_alleles($vf, $dat)};
    if (@matches) {
      $found_vf = dclone $dat;
      last;
    }
  }

  if (@matches) {
    # Return the index of matching found alleles
    my @found_alts = map { $_->{b_index} } @matches;

    # Parse info fields if needed
    if ($self->{fields}) {
      my %found_fields = %{parse_info($found_vf->{line}, $self->{valid_fields})};
      while (my ($field, $val) = each %found_fields) {
        $ret{"$self->{name}_$field"} = [@$val];
      }
    }

    $ret{"$self->{name}_ID"} = $found_vf->{line}->[2];
    $ret{"$self->{name}_POS"} = $found_vf->{pos};
    $ret{"$self->{name}_POS"} = $found_vf->{pos};
    $ret{"$self->{name}_REF"} = $found_vf->{ref};
    $ret{"$self->{name}_ALT"} = $found_vf->{alts};
    $ret{"$self->{name}_alt_index"} = [@found_alts]; 
  }
  return \%ret;
}

1;
