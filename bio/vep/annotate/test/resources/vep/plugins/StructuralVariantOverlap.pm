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

 StructuralVariantOverlap

=head1 SYNOPSIS

 mv StructuralVariantOverlap.pm ~/.vep/Plugins
 ./vep -i structvariants.vcf --plugin StructuralVariantOverlap,file=gnomad_v2_sv.sites.vcf.gz

=head1 DESCRIPTION

 A VEP plugin that retrieves information from overlapping structural variants.

 Parameters can be set using a key=value system:

 file           : required - a VCF file of reference data. 

 overlap        : percentage overlap between SVs (default: 80)
 reciprocal     : calculate reciprocal overlap, options:  0 or 1. (default: 0)
                  (overlap is expressed as % of input SV by default)

 cols           : colon delimited list of data types to return from the INFO fields (only AF by default)

 same_type      : 1/0 only report SV of the same type (eg deletions for deletions, off by default)

 distance       : the distance the ends of the overlapping SVs should be within.

 match_type     : only report reference SV which lie within or completely surround the input SV
                  options: within, surrounding

 label          : annotation label that will appear in the output (default: "SV_overlap")
                  Example- input: label=mydata, output: mydata_name=refSV,mydata_PC=80,mydata_AF=0.05

Example reference data

1000 Genomes Project:
ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/integrated_sv_map/ALL.wgs.mergedSV.v8.20130502.svs.genotypes.vcf.gz

gnomAD::
https://storage.googleapis.com/gnomad-public/papers/2019-sv/gnomad_v2_sv.sites.vcf.gz


 Example:

  ./vep -i structvariants.vcf --plugin StructuralVariantOverlap,file=gnomad_v2_sv.sites.vcf.gz


=cut


package StructuralVariantOverlap;

use strict;
use warnings;

use Bio::EnsEMBL::Variation::Utils::VEP qw(parse_line);
use base qw(Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin);

sub new {
  my $class = shift;
  my $self = $class->SUPER::new(@_);
  
  ## check tabix is available
  die "ERROR: tabix does not seem to be in your path\n" unless `which tabix 2>&1` =~ /tabix$/;

  my $params_hash = $self->params_to_hash();

  ## get/check annotation file
  die "ERROR: file of annotations needed\n" unless $params_hash->{file};
  die "ERROR: file $params_hash->{file} not found\n" unless -e $params_hash->{file};
  die "ERROR: Tabix index file $params_hash->{file}\.tbi not found\n" 
    unless -e $params_hash->{file}.'.tbi';

  $self->{file} = $params_hash->{file};


  ## get/set optional parameters
  die "ERROR: StructuralVariantOverlap match type : ". $params_hash->{match_type} . "not recognised . Select within or surrounding\n"
    if defined  $params_hash->{match_type} && $params_hash->{match_type} !~/^within$|^surrounding$/;

  $self->{distance}   = $params_hash->{distance} ? $params_hash->{distance} : undef;
  $self->{match_type} = $params_hash->{match_type} ? $params_hash->{match_type} : undef ;
  $self->{required_percent_olap} = $params_hash->{percentage} ? $params_hash->{percentage} : 80;
  $self->{same_type}  = $params_hash->{same_type} ? $params_hash->{same_type} : 0 ;
  $self->{label}  = $params_hash->{label} ? $params_hash->{label} : "SV_overlap";
  $self->{reciprocal}  = $params_hash->{reciprocal} ? $params_hash->{reciprocal} : 0;


  ## allow specific columns to be rerieved from the VCF
  if($params_hash->{cols}){
    my @cols = split/\:/, $params_hash->{cols};
    foreach my $col (@cols){
      $self->{cols}->{$col} = 1;
    }
  }
  return $self;
}

sub variant_feature_types {
    return ['BaseVariationFeature'];
}

sub feature_types {
  return ['Feature','Intergenic'];
}

sub get_header_info {

  my $self = shift;

  return $self->{header_info} if exists($self->{header_info});

  my $desc;
  ## if any specific columns were requested; add them
  if( scalar(keys %{$self->{cols}}) > 0 ){
    $desc = $self->get_header_desc();
  }

  my $overlap_definition = $self->{reciprocal} == 1 ?
                           "minimum reciprocal overlap as a percent" :
                           "percent of input SV covered by reference SV";

  my %headers = ( $self->{label}."_name" => "name of overlapping SV",
                  $self->{label}."_AF"   => "frequency of overlapping SV",
                  $self->{label}."_PC"   => $overlap_definition,
                );

  ## add any specifically requested headers
  foreach my $info (keys %{$self->{cols}}){
    $headers{$self->{label} ."_". $info} = $desc->{$info};
  } 

  return \%headers;
}

## read descriptions from requested info fields from reference VCF
sub get_header_desc {

  my $self = shift;

  my %desc;

  (open my $in, "tabix -f -h ".$self->{file}." 1:1-1 |")||die "Failed to read headers from " . $self->{file} . "\n" ;

  my @lines = <$in>;

  while(my $line = shift @lines) {

    next unless $line =~/INFO/;

    my @det = split/\,|\>|\</, $line;
    my $key;

    foreach my $d(@det){
      if($d =~/ID/){
        $key = (split/\=/, $d)[1];
      }
      elsif($d=~/Description/){
        $d =~ s/Description\=//;
        $desc{$key} = $d;
      }
    }
  }
  close $in;

  return \%desc;

}

sub run {
  my ($self, $bvfoa) = @_;

  $self->get_header_info();

  my $svf = $bvfoa->base_variation_feature;

  ## don't annotate breakends with overlapping SV data
  return {} if $svf->class_SO_term() eq 'BND';

  ## read & filter reference VCF  
  my $overlaps = $self->get_data($svf);

  return {} unless $overlaps && scalar @$overlaps;

  my %save;
  ## loop through overlapping SVs extracting required info
  foreach my $osv(@{$overlaps}){

    ## collect output types
    push @{$save{$self->{label}."_name"}}, $osv->variation_name();
    push @{$save{$self->{label}."_PC"}}, $osv->{_overlap_found};

    my %info;
    ## if any specific columns were requested; add them
    my $info = (split/\s+/,$osv->{_line})[7];
    my @attribs = split/\;/, $info;
    foreach my $att(@attribs){
      my($key, $val) = split/\=/, $att;
      $info{$key} = $val;
    }

    if(scalar (keys %{$self->{cols}}) > 0){
      foreach my $info (keys %{$self->{cols}}){
        push @{$save{$self->{label} . "_" . $info}},  $info{$info};
      }
    }
    else{
      ## add allele frequency as a default if available
      push @{$save{$self->{label}."_AF"}}, defined  $info{AF} ?  $info{AF} : undef;
    }
  }
  ## format
  my %output;
  foreach my $t( keys %save){
    $output{$t} = join(",", @{$save{$t}});
  }
  return \%output;
}

## read annotation file & apply filters

sub get_data{

  my ($self, $svf) = @_;

  my $start = $svf->{start};
  my $end   = $svf->{end};

  my $length = $end - $start +1;

  ## no useful overlap can be calculated if there is no start/end available
  return unless $length >0;

  my @overlaps;

  ## adjust coords for tabix
  my $s  = $start - 1;
  my $pos_string = sprintf("%s:%i-%i", $svf->seq_region_name, $s, $end);
  
  (open my $in, "tabix  ".$self->{file}." $pos_string |")||die "Failed to read headers from " . $self->{file} . "\n" ;
 
  while(<$in>) {

    my $olap_svs = parse_line({format => 'vcf'}, $_);

    foreach my $olap_sv (@{$olap_svs}){

      ## skip breakends - hard to interpret here
      next if $olap_sv->class_SO_term() eq 'BND';

      ## match on SV class if required 
      ## confounded by different descriptions for the same event
      next if $olap_sv->class_SO_term() ne $svf->class_SO_term() &&  $self->{same_type}  ==1;


      if( defined $self->{match_type}){
        ## check reference SV within input SV if required 
        next if $self->{match_type} eq "within" && ($start > $olap_sv->{start} ||  $end < $olap_sv->{end});

        ## check reference SV surrounded by input SV if required 
        next if $self->{match_type} eq "surrounding" && ($start < $olap_sv->{start} ||  $end > $olap_sv->{end});
      }

      ## check overlap is long enough
      my $overlap_found; ## % overlap
      if( $self->{required_percent_olap} > 0){

        my @overlap_start = sort { $a <=> $b } ($start, $olap_sv->start());
        my @overlap_end   = sort { $a <=> $b } ($end, $olap_sv->end());

        $overlap_found = 100 * (1+ $overlap_end[0]  - $overlap_start[1])/ $length;

        ## overlap as percentage of input SV
        next unless $overlap_found  > $self->{required_percent_olap};

        if ($self->{reciprocal} ==1){
          ## check bi-directional overlap - percentage of ref SV covered
          my $ref_sv_length = $olap_sv->end - $olap_sv->start +1;
          my $ref_overlap_found = 100 * (1+ $overlap_end[0]  - $overlap_start[1])/ $ref_sv_length;

          next unless $ref_overlap_found > $self->{required_percent_olap};
          ## report minimum overlap if checking bidirectionally
          $overlap_found = $ref_overlap_found if $ref_overlap_found < $overlap_found;
        }
      }


      ## check breakpoint ends are within required distance
      if (defined $self->{distance}){
        next unless abs($start - $olap_sv->{start}) < $self->{distance};
        next unless abs($end - $olap_sv->{end}) < $self->{distance};
      }

      ## cache overlap on object
      $olap_sv->{_overlap_found} = $overlap_found;
      push @overlaps, $olap_sv;
    }
  }

  return \@overlaps;
}


1;

