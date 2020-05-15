=head1 LICENSE

Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2020] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

=head1 CONTACT

Please email comments or questions to the public Ensembl
developers list at <https://lists.ensembl.org/mailman/listinfo/dev>.

Questions may also be sent to the Ensembl helpdesk at
<https://www.ensembl.org/Help/Contact>.

=cut

=head1 NAME

satMutMPRA

=head1 SYNOPSIS

 mv satMutMPRA.pm ~/.vep/Plugins
 ./vep -i variations.vcf --plugin satMutMPRA,file=/path/to/satMutMPRA_data.gz,cols=col1:col2

=head1 DESCRIPTION

A VEP plugin that retrieves data for variants from a tabix-indexed satMutMPRA file (1-based file).
The saturation mutagenesis-based massively parallel reporter assays (satMutMPRA) measures variant
effects on gene RNA expression for 21 regulatory elements (11 enhancers, 10 promoters).

The 20 disease-associated regulatory elements and one ultraconserved enhancer analysed in different cell lines are the following:
 - ten promoters (of TERT, LDLR, HBB, HBG, HNF4A, MSMB, PKLR, F9, FOXE1 and GP1BB) and
 - ten enhancers (of SORT1, ZRS, BCL11A, IRF4, IRF6, MYC (2x), RET, TCF7L2 and ZFAND3) and
 - one ultraconserved enhancer (UC88).

Please refer to the satMutMPRA web server and Kircher M et al. (2019) paper for more information:
https://mpra.gs.washington.edu/satMutMPRA/
https://www.ncbi.nlm.nih.gov/pubmed/31395865

Parameters can be set using a key=value system:
 file           : required - a tabix indexed file of the satMutMPRA data corresponding to desired assembly.

 pvalue         : p-value threshold  (default: 0.00001)

 cols           : colon delimited list of data types to be returned from the satMutMPRA data
                (default: 'Value', 'P-Value', and 'Element')

 incl_repl       : include replicates (default: off):
                  - full replicate for LDLR promoter (LDLR.2) and SORT1 enhancer (SORT1.2)
                  - a reversed sequence orientation for SORT1 (SORT1-flip)
                  - other conditions: PKLR-48h, ZRSh-13h2, TERT-GAa, TERT-GBM, TERG-GSc

The Bio::DB::HTS perl library or tabix utility must be installed in your path
to use this plugin. The satMutMPRA data file can be downloaded from
https://mpra.gs.washington.edu/satMutMPRA/

satMutMPRA data can be downloaded for both GRCh38 and GRCh37 from the web server (https://mpra.gs.washington.edu/satMutMPRA/):
'Download' section, select 'GRCh37' or 'GRCh38' for 'Genome release' and 'Download All Elements'.

The file must be processed and indexed by tabix before use by this plugin.

# GRCh38
 > (grep ^Chr GRCh38_ALL.tsv; grep -v ^Chr GRCh38_ALL.tsv | sort -k1,1 -k2,2n ) | bgzip > satMutMPRA_GRCh38_ALL.gz
 > tabix -s 1 -b 2 -e 2 -c C satMutMPRA_GRCh38_ALL.gz

# GRCh37
 > (grep ^Chr GRCh37_ALL.tsv; grep -v ^Chr GRCh37_ALL.tsv | sort -k1,1 -k2,2n ) | bgzip > satMutMPRA_GRCh37_ALL.gz
 > tabix -s 1 -b 2 -e 2 -c C satMutMPRA_GRCh37_ALL.gz


When running the plugin by default 'Value', 'P-Value', and 'Element'
information is returned e.g.

--plugin satMutMPRA,file=/path/to/satMutMPRA_GRCh38_ALL.gz

You may include all columns with ALL; this fetches all data per variant
(e.g. Tags, DNA, RNA, Value, P-Value, Element):

--plugin satMutMPRA,file=/path/to/satMutMPRA_GRCh38_ALL.gz,cols=ALL

You may want to select only a specific subset of information to be
reported, you can do this by specifying the specific columns as parameters to the plugin e.g.

--plugin satMutMPRA,file=/path/to/satMutMPRA_GRCh38_ALL.gz,cols=Tags:DNA

If a requested column is not found, the error message will report the
complete list of available columns in the satMutMPRA file. For a detailed description
of the available information please refer to the manuscript or online web server.

Tabix also allows the data file to be hosted on a remote server. This plugin is
fully compatible with such a setup - simply use the URL of the remote file:

--plugin satMutMPRA,file=http://my.files.com/satMutMPRA.gz

Note that gene locations referred to in satMutMPRA may be out of sync with
those in the latest release of Ensembl; this may lead to discrepancies with
information retrieved from other sources.

=cut

package satMutMPRA;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin;

use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

my @fields_order;

my $out_txt = 1;
my $out_vcf = 0;
my $out_json = 0;
my $char_sep = "|";

my %repl = (
"LDLR.2"=>1, "SORT1.2"=>1,
"SORT1-flip" =>1,
"PKLR-48h" => 1, "ZRSh-13h2" => 1,
"TERT-GAa" =>1, "TERT-GBM" =>1, "TERT-GSc" => 1);

# default config
my %CONFIG = (
  pvalue => 0.00001,
  incl_repl => 0,
);

sub new {
  my $class = shift;

  my $self = $class->SUPER::new(@_);

  $self->expand_left(0);
  $self->expand_right(0);

  my $params_hash = $self->params_to_hash();
  $CONFIG{$_} = $params_hash->{$_} for keys %$params_hash;

  # get satMutMPRA file
  my $file = $CONFIG{file};
  $self->add_file($file);

  # get output format
  $out_vcf  = 1 if ($self->{config}->{output_format} eq "vcf");
  $out_json = 1 if ($self->{config}->{output_format} eq "json");
  $out_txt = 0 if ($out_vcf || $out_json);

  $char_sep = "+" if $out_vcf;

  # get headers
  open HEAD, "tabix -fh $file 1:1-1 2>&1 | ";
  while(<HEAD>) {
    chomp;
    $self->{headers} = [split];
  }
  close HEAD;
  die "ERROR: Could not read headers from $file\n" unless defined($self->{headers}) && scalar @{$self->{headers}};

  # get required columns
  my $i = 0;
  ## allow specific columns to be retrieved from the VCF
  if($params_hash->{cols}){
    my @cols = split/\:/, $params_hash->{cols};
    foreach my $col (@cols){
      next if $col eq ''; # skip if by mistake empty column was present eg. DNA::ALL
      if($col eq 'ALL') {
        $self->{cols} = {map {$_ => $i++}
            @{$self->{headers}}};
        last; #if ALL is used, then the loop will exit after all existing header elements have been selected
      }
      die "ERROR: Column $col not found in header for file $file. Available columns are:\n".join(",", @{$self->{headers}})."\n" unless grep {$_ eq $col} @{$self->{headers}};

      $self->{cols}->{$col} = $i;
      $i++;
    }
  } else { #default columns
    $self->{cols}->{'Value'} = 1;
    $self->{cols}->{'P-Value'} = 2;
    $self->{cols}->{'Element'} = 3;
    $i=3;
  }

  $i += 1; #ensure that $i is higher than the number of selected columns

  # get the order of the output fields into an array, $i is the total number of columns +1
  @fields_order = sort {
    $self->{cols}->{$a}
    <=>
    $self->{cols}->{$b}
  }
  keys %{$self->{cols}};

  return $self;
}

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {
  my $self = shift;

  my $header = 'satMutMPRA data for variation in 21 regulatory features. Format: ';
  $header .= join($char_sep, @fields_order );

  return {
    satMutMPRA => $header,
  }
}

sub run {
  my $self = shift;
  my $tva = shift;

  my $vf = $tva->variation_feature;
  my $ref_allele = $vf->ref_allele_string;
  my %alt_alleles = map {$_ => 1} @{$vf->alt_alleles};

  my ($start, $end) = ($vf->{start}, $vf->{end});
  # adjust coords for insertions
  ($start, $end) = ($vf->{end}, $vf->{start}) if ($vf->{start} > $vf->{end});

  my $data = $self->get_data($vf->{chr}, $start, $end);

  return {} unless $data && scalar @$data;

  my @result =();
  my %result_uniq;
  my @result_str = ();

  foreach my $tmp_data(@{$data}) {
    next unless $tmp_data->{'P-Value'} < $CONFIG{pvalue};
    next unless $ref_allele eq $tmp_data->{'Ref'} && exists($alt_alleles{$tmp_data->{'Alt'}});
    next if (!$CONFIG{incl_repl} && exists ($repl{$tmp_data->{Element}}));

    # get required data
    my %tmp_return =
      map {$_ => $tmp_data->{$_}}
      grep {defined($self->{cols}->{$_})}  # only include selected cols
      keys %$tmp_data;

    # report only unique set of fields
    my $record_line = join(",", values %tmp_return);
    next if defined $result_uniq{$record_line};
    $result_uniq{$record_line} = 1;

    push(@result_str, join($char_sep, @tmp_return{@fields_order}));
    push(@result, \%tmp_return);
  }

  if (scalar @result > 0){
    return {
      satMutMPRA => $self->{config}->{output_format} eq "json" ? \@result : \@result_str
    }
  } else {
    return {};
  }

}

sub parse_data {
  my ($self, $line) = @_;

  my @split = split /\t/, $line;

  # parse data into hash of col names and values
  my %data = map {$self->{headers}->[$_] => $split[$_]} (0..$#{$self->{headers}});

  return \%data;
}

1;
