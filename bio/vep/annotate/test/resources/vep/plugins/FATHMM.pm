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

 FATHMM

=head1 SYNOPSIS

 mv FATHMM.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin FATHMM,"python /path/to/fathmm/fathmm.py"

=head1 DESCRIPTION

 A VEP plugin that gets FATHMM scores and predictions for missense variants.
 
 You will need the fathmm.py script and its dependencies (Python, Python
 MySQLdb). You should create a "config.ini" file in the same directory as the
 fathmm.py script with the database connection options. More information about
 how to set up FATHMM can be found on the FATHMM website at
 https://github.com/HAShihab/fathmm.
 
 A typical installation could consist of:
 
 > wget https://raw.github.com/HAShihab/fathmm/master/cgi-bin/fathmm.py
 > wget http://fathmm.biocompute.org.uk/database/fathmm.v2.3.SQL.gz
 > gunzip fathmm.v2.3.SQL.gz
 > mysql -h[host] -P[port] -u[user] -p[pass] -e"CREATE DATABASE fathmm"
 > mysql -h[host] -P[port] -u[user] -p[pass] -Dfathmm < fathmm.v2.3.SQL
 > echo -e "[DATABASE]\nHOST = [host]\nPORT = [port]\nUSER = [user]\nPASSWD = [pass]\nDB = fathmm\n" > config.ini

=cut

package FATHMM;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);
  
  # get command
  my $command = $self->params->[0];
  
  die 'ERROR: No FATHMM command specified. Specify path to FATHMM with e.g. --plugin FATHMM,"python /path/to/fathmm/fathmm.py"\n' unless defined($command);
  
  die 'ERROR: Your FATHMM command does not look correct; it should looks something like "python /path/to/fathmm/fathmm.py"\n' unless $command =~ /python.+fathmm\.py/;
  
  $self->{command} = $command;
  
  die 'ERROR: Temporary directory '.$self->{config}->{tmpdir}.' not found - specify an existing directory with --tmpdir [dir]\n' unless -d $self->{config}->{tmpdir};
  
  return $self;
}

sub version {
  return 71;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    FATHMM => "FATHMM prediction (score)",
  };
}

sub run {
  my ($self, $tva) = @_;
  
  # only for missense variants
  return {} unless grep {$_->SO_term eq 'missense_variant'} @{$tva->get_all_OverlapConsequences};
  
  # configure command
  my $command      = $self->{command};
  $command        =~ m/(\s.+)\/.+/;
  my $command_dir  = $1;
  
  # configure tmp dir and in/out files for FATHMM
  my $tmp_dir      = $self->{config}->{tmpdir};
  my $tmp_in_file  = $tmp_dir."/fathmm_$$\.in";
  my $tmp_out_file = $tmp_dir."/fatmm_$$\.out";
  
  # get required input data from TVA
  my $protein   = $tva->transcript->{_protein} || $tva->transcript->translation->stable_id;
  my $aa_change = $tva->pep_allele_string;
  my $aa_pos    = $tva->transcript_variation->translation_start;
  $aa_change   =~ s/\//$aa_pos/;
  
  # check we have valid strings
  return {} unless $protein && $aa_change =~ /^[A-Z]\d+[A-Z]$/;
  
  # write input file
  open IN, ">$tmp_in_file" or die "ERROR: Could not write to file $tmp_in_file\n";
  print IN "$protein $aa_change\n";
  close IN;
  
  # run command
  my $fathmm_err = `cd $command_dir; $command $tmp_in_file $tmp_out_file;`;
  
  # read output file
  open OUT, $tmp_out_file or die "ERROR: Could not read from file $tmp_out_file\n";
  
  my ($pred, $score);
  while(<OUT>) {
    next if /^\#/;
    chomp;
    my @data = split;
    ($pred, $score) = ($data[4], $data[5]);
  }
  close OUT;
  
  # delete temporary files
  unlink($tmp_in_file, $tmp_out_file);
  
  return $pred && $score ? {
    FATHMM => "$pred($score)",
  } : {};
}

1;

