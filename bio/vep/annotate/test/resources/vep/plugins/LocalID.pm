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

 LocalID

=head1 SYNOPSIS

 mv LocalID.pm ~/.vep/Plugins

 ## first run create database

 # EITHER create from Ensembl variation database
 # VERY slow but includes variant synonyms, if not required see next command
 ./vep -i variant_ids.txt --plugin LocalID,create_db=1 -safe

 # OR create from cache directory
 # faster but does not include synonyms
 # parameter passed to from_cache may be full path to cache e.g. $HOME/.vep/homo_sapiens/88_GRCh38
 # cache may be tabix converted or in default state (http://www.ensembl.org/info/docs/tools/vep/script/vep_cache.html#convert)
 ./vep -i variant_ids.txt --plugin LocalID,create_db=1,from_cache=1 -safe

 # subsequent runs
 ./vep -i variant_ids.txt --plugin LocalID

 # db file can be specified with db=[file]
 # default file name is $HOME/.vep/[species]_[version]_[assembly].variant_ids.sqlite3
 ./vep -i variant_ids.txt --plugin LocalID,db=my_db_file.txt

=head1 DESCRIPTION

 The LocalID plugin allows you to use variant IDs as input without making a database connection.

 Requires sqlite3.
 
 A local sqlite3 database is used to look up variant IDs; this is generated either from Ensembl's
 public database (very slow, but includes synonyms), or from a VEP cache file (faster, excludes
 synonyms).

 NB this plugin is NOT compatible with the ensembl-tools variant_effect_predictor.pl version of VEP.

=cut

package LocalID;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;
use Bio::EnsEMBL::VEP::Parser::ID;
use Bio::EnsEMBL::VEP::Constants;
use Bio::EnsEMBL::VEP::Utils qw(get_compressed_filehandle);


use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);

  my $param_hash = $self->params_to_hash();
  my $config     = $self->{config};
  my $species    = $config->{species} || 'homo_sapiens';
  my $db;

  unless($db = $param_hash->{db}) {
    my $version =
      $config->{db_version} ||
      $config->{cache_version} ||
      $Bio::EnsEMBL::VEP::Constants::VEP_VERSION ||
      'Bio::EnsEMBL::Registry'->software_version ||
      undef;
    my $assembly = $config->{assembly};
    my $dir = $param_hash->{dir} || $config->{dir};

    die("ERROR: Unable to determine software version - if using --offline, add --cache_version [version] or add the ID database name to your --plugin string as \"db=[file]\"\n") unless $version;
    die("ERROR: Unable to determine assembly version - if using --offline, add --assembly [version] or add the ID database name to your --plugin string as \"db=[file]\"\n") unless $assembly;
    $db = sprintf("%s/%s_%i_%s.variant_ids.sqlite3", $dir, $species, $version, $assembly);
  }  

  # create DB?
  $self->create_db($db, $species, $param_hash) if $param_hash->{create_db};

  die("ERROR: DB file $db not found - you need to download or create it first, see documentation in plugin file\n") unless -e $db;

  $self->config->{_localid_db_file} = $db;

  return $self;
}

sub create_db {
  my ($self, $db, $species, $param_hash) = @_;

  # requites sqlite3 command line tool
  die("ERROR: sqlite3 command not found in path\n") unless `which sqlite3` =~ /\/sqlite3/;

  my $config = $self->{config};

  die("ERROR: DB file $db already exists - remove and re-run to overwrite\n") if -e $db;

  print STDERR "## LocalID plugin\n # Creating database of variant IDs - this may take some time\n" unless $config->{quiet};

  my $tmpfile = "$db.tmp$$";
  open my $tmp_handle, ">$tmpfile" or die "ERROR: Unable to write to $tmpfile\n";

  if(my $cache_dir = $param_hash->{from_cache}) {

    # attempt to interpret cache dir from command line opts
    if($cache_dir eq '1') {
      my $version =
        $config->{cache_version} ||
        $config->{db_version} ||
        $Bio::EnsEMBL::VEP::Constants::VEP_VERSION ||
        ($config->{reg} ? $config->{reg}->software_version : undef);
      my $assembly = $config->{assembly};
      my $dir = $config->{dir_cache} || $config->{dir};

      $cache_dir = "$dir\/$species\/$version\_$assembly";
    }

    print STDERR " # attempting to create from $cache_dir\n" unless $config->{quiet};
    $self->_tmp_file_from_cache($cache_dir, $tmp_handle);
  }
  else {
    print STDERR " # attempting to create from variation database for $species\n" unless $config->{quiet};
    $self->_tmp_file_from_var_db($species, $tmp_handle);
  }

  close $tmp_handle;

  # create database
  my $dbh = DBI->connect("dbi:SQLite:dbname=$db","","");
  $dbh->do("CREATE TABLE ids(id, chr, start, end, alleles, strand)");

  # load tmp file into table
  print STDERR " # loading database\n" unless $config->{quiet};
  my $cmd = qq{sqlite3 $db '.import $tmpfile ids'};
  `$cmd 2>&1` and die("ERROR: Failed to import $tmpfile to $db\n");
  unlink($tmpfile);

  # index
  print STDERR " # indexing database\n" unless $config->{quiet};
  $dbh->do("CREATE INDEX id_idx ON ids(id)");

  print STDERR " # successfully built database $db\n" unless $config->{quiet};
}

sub _tmp_file_from_cache {
  my ($self, $cache_dir, $tmp_handle) = @_;
  my $config = $self->{config};

  die("ERROR: Cache dir $cache_dir not found or not a directory\n") unless -d $cache_dir;

  # read info
  open INFO, $cache_dir.'/info.txt' or die("ERROR: No info.txt file found in $cache_dir\n");

  my %cols;
  while(<INFO>) {
    next unless /^variation_cols/;
    chomp;
    my @tmp_cols = split(',', (split("\t", $_))[1]);
    $cols{$tmp_cols[$_]} = $_ for 0..$#tmp_cols;
    last;
  }
  close INFO;

  # get all chromosome dirs
  opendir DIR, $cache_dir or die("ERROR: Could not read dir $cache_dir\n");
  my @chrs = grep {-d $cache_dir.'/'.$_ && !/^\./} readdir DIR;
  closedir DIR;

  foreach my $chr(@chrs) {
    opendir CHR, $cache_dir.'/'.$chr;
    my @all_files = grep {/var/ && !/\.(tb|cs)i$/} readdir CHR;
    closedir CHR;

    my @files = grep {/all_vars/} @all_files;
    @files = @all_files unless @files;

    foreach my $file(@files) {
      my $fh = get_compressed_filehandle($cache_dir.'/'.$chr.'/'.$file, 1);

      my $delim;

      while(<$fh>) {
        unless($delim) {
          $delim = /\t/ ? "\t" : " ";
        }

        chomp;
        my @split = map {($_ || '') eq '.' ? undef : $_} split($delim);

        # id, chr, start, end, alleles, strand
        print $tmp_handle join("|",
          $split[$cols{variation_name}],
          $chr,
          $split[$cols{start}],
          $split[$cols{end}] || $split[$cols{start}],
          $split[$cols{allele_string}] || '',
          $split[$cols{strand}] || 1,
        )."\n";
      }

      close $fh;
    }
  }
}

sub _tmp_file_from_var_db {
  my ($self, $species, $tmp_handle) = @_;
  my $config = $self->{config};

  my $var_dbc = Bio::EnsEMBL::Registry->get_adaptor($species, 'variation', 'variation')->db->dbc;

  my $mysql = $var_dbc->prepare(qq{
    SELECT v.name, s.name, vf.seq_region_start, vf.seq_region_end, vf.allele_string, vf.seq_region_strand
    FROM variation v, variation_feature vf, seq_region s
    WHERE v.variation_id = vf.variation_id
    AND vf.seq_region_id = s.seq_region_id
  }, {mysql_use_result => 1});

  my ($i, $c, $s, $e, $a, $d);
  $mysql->execute();
  $mysql->bind_columns(\$i, \$c, \$s, \$e, \$a, \$d);
  print $tmp_handle join("|", ($i, $c, $s, $e, $a, $d))."\n" while $mysql->fetch();
  $mysql->finish();

  # do synonyms
  print STDERR "Processing synonyms\n" unless $config->{quiet};
  $mysql = $var_dbc->prepare(qq{
    SELECT v.name, s.name, vf.seq_region_start, vf.seq_region_end, vf.allele_string, vf.seq_region_strand
    FROM variation_synonym v, variation_feature vf, seq_region s
    WHERE v.variation_id = vf.variation_id
    AND vf.seq_region_id = s.seq_region_id
  }, {mysql_use_result => 1});

  $mysql->execute();
  $mysql->bind_columns(\$i, \$c, \$s, \$e, \$a, \$d);
  print $tmp_handle join("|", ($i, $c, $s, $e, $a, $d))."\n" while $mysql->fetch();
  $mysql->finish();
}

sub run {
  return {};
}

1;




###########################################
### Redefine methods in existing module ###
###########################################

package Bio::EnsEMBL::VEP::Parser::ID;

no warnings qw(redefine);
sub new {
  my $caller = shift;
  my $class = ref($caller) || $caller;
  
  my $self = $class->SUPER::new(@_);

  return $self;
}

sub create_VariationFeatures {
  my $self = shift;

  my $parser = $self->parser;
  $parser->next();

  $self->skip_empty_lines();

  return [] unless $parser->{record};

  $self->line_number($self->line_number + 1);

  my $id = $parser->get_value;

  # remove whitespace
  $id =~ s/\s+//g;

  my $db  = $self->id_db;
  my $sth = $self->{_id_sth} ||= $db->prepare("SELECT chr, start, end, alleles, strand FROM ids WHERE id = ?");
  my $ad  = $self->{_var_ad} ||= $self->get_adaptor('variation', 'VariationFeature');

  my @vfs;
  my ($c, $s, $e, $a, $d);
  $sth->execute($id);
  $sth->bind_columns(\$c, \$s, \$e, \$a, \$d);

  push @vfs, Bio::EnsEMBL::Variation::VariationFeature->new_fast({
    start          => $s,
    end            => $e,
    allele_string  => $a,
    strand         => $d,
    map_weight     => 1,
    adaptor        => $ad,
    variation_name => $id,
    chr            => $c,
  }) while $sth->fetch;

  $sth->finish();

  unless(@vfs) {
    $self->warning_msg("WARNING: No mappings found for variant \'$id\'");
    return $self->create_VariationFeatures();
  }

  return $self->post_process_vfs(\@vfs);
}

sub id_db {
  my $self = shift;

  unless(exists($self->{_id_db})) {
    throw("ERROR: ID database not defined or detected - possible plugin compile failure\n") unless my $db = $self->config->{_params}->{_localid_db_file};
    throw("ERROR: ID database file $db not found - you need to download or create it first, see documentation in plugin file\n") unless -e $db;
    $self->{_id_db} = DBI->connect("dbi:SQLite:dbname=$db","","");
  }

  return $self->{_id_db};
}

1;
