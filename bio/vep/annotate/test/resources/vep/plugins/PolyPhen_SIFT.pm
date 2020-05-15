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

 PolyPhen_SIFT

=head1 SYNOPSIS

 mv PolyPhen_SIFT.pm ~/.vep/Plugins
 ./vep -i variations.vcf -cache --plugin PolyPhen_SIFT

=head1 DESCRIPTION

 A VEP plugin that retrieves PolyPhen and SIFT predictions from a
 locally constructed sqlite database. It can be used when your main
 source of VEP transcript annotation (e.g. a GFF file or GFF-based cache)
 does not contain these predictions.

 You must either download or create a sqlite database of the predictions.
 You may point to the file by adding db=[file] as a parameter:

 --plugin PolyPhen_SIFT,db=[file]

 Human predictions (assembly-independent) are available here:

 https://dl.dropboxusercontent.com/u/12936195/homo_sapiens.PolyPhen_SIFT.db

 (Please note the download location of this file may change)

 Place this file in $HOME/.vep to have the plugin find it automatically.
 You may change this directory by adding dir=[dir] as a parameter:

 --plugin PolyPhen_SIFT,dir=[dir]

 To create the database, you must have an active database connection
 (i.e. not using --offline) and add create_db=1 as a parameter:

 --plugin PolyPhen_SIFT,create_db=1

 *** NB: this will take some time!!! ***

 By default the file is created as:

 ${HOME}/.vep/[species].PolyPhen_SIFT.db
 
=cut

package PolyPhen_SIFT;

use strict;
use warnings;
use DBI;
use Digest::MD5 qw(md5_hex);
use Bio::EnsEMBL::Variation::ProteinFunctionPredictionMatrix;

use Bio::EnsEMBL::Variation::Utils::BaseVepPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepPlugin);

sub new {
  my $class = shift;
  
  my $self = $class->SUPER::new(@_);

  my $param_hash = $self->params_to_hash();

  my $species = $self->config->{species} || 'homo_sapiens';
  my $dir = $param_hash->{dir} || $self->{config}->{dir};
  my $db = $param_hash->{db} || $dir.'/'.$species.'.PolyPhen_SIFT.db';

  # create DB?
  if($param_hash->{create_db}) {
    die("ERROR: DB file $db already exists - remove and re-run to overwrite\n") if -e $db;

    $self->{dbh} = DBI->connect("dbi:SQLite:dbname=$db","","");
    $self->{dbh}->do("CREATE TABLE predictions(md5, analysis, matrix)");

    my $sth = $self->{dbh}->prepare("INSERT INTO predictions VALUES(?, ?, ?)");

    my $mysql = Bio::EnsEMBL::Registry->get_adaptor($species, 'variation', 'variation')->db->dbc->prepare(qq{
      SELECT m.translation_md5, a.value, p.prediction_matrix
      FROM translation_md5 m, attrib a, protein_function_predictions p
      WHERE m.translation_md5_id = p.translation_md5_id
      AND p.analysis_attrib_id = a.attrib_id
    }, {mysql_use_result => 1});

    my ($md5, $attrib, $matrix);
    $mysql->execute();
    $mysql->bind_columns(\$md5, \$attrib, \$matrix);
    $sth->execute($md5, $attrib, $matrix) while $mysql->fetch();
    $sth->finish();
    $mysql->finish();

    $self->{dbh}->do("CREATE INDEX md5_idx ON predictions(md5)");
  }

  die("ERROR: DB file $db not found - you need to download or create it first, see documentation in plugin file\n") unless -e $db;

  $self->{initial_pid} = $$;
  $self->{db_file} = $db;

  $self->{dbh} ||= DBI->connect("dbi:SQLite:dbname=$db","","");
  $self->{get_sth} = $self->{dbh}->prepare("SELECT md5, analysis, matrix FROM predictions WHERE md5 = ?");

  return $self;
}

sub feature_types {
  return ['Transcript'];
}

sub get_header_info {
  return {
    PolyPhen_humdiv_score => 'PolyPhen humdiv score from PolyPhen_SIFT plugin',
    PolyPhen_humdiv_pred  => 'PolyPhen humdiv prediction from PolyPhen_SIFT plugin',
    PolyPhen_humvar_score => 'PolyPhen humvar score from PolyPhen_SIFT plugin',
    PolyPhen_humvar_pred  => 'PolyPhen humvar prediction from PolyPhen_SIFT plugin',
    SIFT_score            => 'SIFT score from PolyPhen_SIFT plugin',
    SIFT_pred             => 'SIFT prediction from PolyPhen_SIFT plugin',
  };
}

sub run {
  my ($self, $tva) = @_;
  
  # only for missense variants
  return {} unless grep {$_->SO_term eq 'missense_variant'} @{$tva->get_all_OverlapConsequences};

  my $tr = $tva->transcript;
  my $tr_vep_cache = $tr->{_variation_effect_feature_cache} ||= {};

  ## if predictions are not available for both tools in the cache, look in the SQLite database
  unless(exists($tr_vep_cache->{protein_function_predictions}) &&
     $tva->sift_prediction() && $tva->polyphen_prediction()
   ){

    # get peptide
    unless($tr_vep_cache->{peptide}) {
      my $translation = $tr->translate;
      return {} unless $translation;
      $tr_vep_cache->{peptide} = $translation->seq;
    }

    # get data, indexed on md5 of peptide sequence
    my $md5 = md5_hex($tr_vep_cache->{peptide});

    my $data = $self->fetch_from_cache($md5);

    unless($data) {

      # forked, reconnect to DB
      if($$ != $self->{initial_pid}) {
        $self->{dbh} = DBI->connect("dbi:SQLite:dbname=".$self->{db_file},"","");
        $self->{get_sth} = $self->{dbh}->prepare("SELECT md5, analysis, matrix FROM predictions WHERE md5 = ?");

        # set this so only do once per fork
        $self->{initial_pid} = $$;
      }

      $self->{get_sth}->execute($md5);

      $data = {};

      while(my $arrayref = $self->{get_sth}->fetchrow_arrayref) {
        my $analysis = $arrayref->[1];
        my ($super_analysis, $sub_analysis) = split('_', $arrayref->[1]);

        $data->{$analysis} = Bio::EnsEMBL::Variation::ProteinFunctionPredictionMatrix->new(
          -translation_md5    => $arrayref->[0],
          -analysis           => $super_analysis,
          -sub_analysis       => $sub_analysis,
          -matrix             => $arrayref->[2]
        );
      }

      $self->add_to_cache($md5, $data);
    }

    $tr_vep_cache->{protein_function_predictions} = $data;
  }

  my $return = {};

  foreach my $tool_string(qw(SIFT PolyPhen_humdiv PolyPhen_humvar)) {
    my ($tool, $analysis) = split('_', $tool_string);
    my $lc_tool = lc($tool);

    my $pred_meth  = $lc_tool.'_prediction';
    my $score_meth = $lc_tool.'_score';

    my $pred = $tva->$pred_meth($analysis);

    if($pred) {
      $pred =~ s/\s+/\_/g;
      $pred =~ s/\_\-\_/\_/g;
      $return->{$tool_string.'_pred'} = $pred;

      my $score = $tva->$score_meth($analysis);
      $return->{$tool_string.'_score'} = $score if defined($score);
    }
  }

  return $return;
}

sub fetch_from_cache {
  my $self = shift;
  my $md5 = shift;

  my $cache = $self->{_cache} ||= [];

  my ($data) = map {$_->{data}} grep {$_->{md5} eq $md5} @$cache;
  return $data;
}

sub add_to_cache {
  my $self = shift;
  my $md5 = shift;
  my $data = shift;

  my $cache = $self->{_cache} ||= [];
  push @$cache, {md5 => $md5, data => $data};

  shift @$cache while scalar @$cache > 50;
}

1;

