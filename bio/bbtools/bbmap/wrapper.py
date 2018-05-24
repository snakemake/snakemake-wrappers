__author__ = "Silas Kieser"
__copyright__ = "Copyright 2018, Silas Kieser"
__email__ = "silas.kieser@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os

# Extract arguments
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# inputs arguments.

n_files= len(snakemake.input.reads):
if n_files==1:
    input="in={}".format(snakemake.input.reads[0])
elif n_files==2:
    input="in1={0} in2={1}".format(*snakemake.input.reads)
elif n_files==3:
    input="in1={0},{2} in2={1},null".format(*snakemake.input.reads)
else:
    raise ValueError("input.reads must have 1 (single-end); "
                     "2 (paired-end) or ;
                    " 3 (paired-end + singletons) elements")


if hasattr(snakemake.resources,'mem'):
    # java requires 15% overhead
    memory= "-Xmx{java_mem}".format(java_mem=0.85*snakemake.resources.mem )
else:
    memory=""


def to_bbmap_keys(params,ignore_keys=[]):
    """
    transforms a dict to a string with key=value,
    changes booleans to 't' 'f'
    """
    outstring=""

    for key in params:


        if not key in ignore_keys:
            value= params[key]
            if type(balue) is bool:
                value is 't' if value else 'f'

            outstring+=" {}={} ".format(key,value)

    return outstring


params= to_bbmap_keys(snakemake.params,ignore_keys=['sort_bam'])

if hasattr(snakemake.params,'sort_bam') and snakemake.params.sort_bam:
    sort_bam= " bamscript=bs.sh; sh bs.sh "
else:
    sort_bam =""



# output
if len(snakemake.output)==1:
    output="out={}".format(snakemake.output[0])

else:
    output= to_bbmap_keys(snakemake.output,ignore_keys=['unmapped','sam','bam'])

    if hasattr(snakemake.output,'unmapped'):
        n_files= len(snakemake.output.unmapped):
        if n_files==1:
            input="outu={}".format(snakemake.output.unmapped[0])
        elif n_files==2:
            input="outu1={0} outu2={1}".format(*snakemake.output.unmapped)
        elif n_files==3:
            input="outu1={0},{2} outu2={1},null".format(*snakemake.output.unmapped)
        else:
            raise ValueError("output.unmapped must have 1 (single-end); "
                             "2 (paired-end) or ;
                            " 3 (paired-end + singletons) elements")


    if hasattr(snakemake.output,'sam'):
        output="out={}".format(snakemake.output.sam)
    elif hasattr(snakemake.output,'bam'):
            output="out={} ".format(snakemake.output.bam)
    elif not ( hasattr(snakemake.output,'out') or hasattr(snakemake.output,'outm')):
        raise ValueError(
                        "Error: no output file specified"
                        "Specify output as:"
                         "sam='output.sam'"
                         "bam='output.bam'"
                         "or one of 'out', 'outm'"
                        )



shell(
    "bbwrap.sh"
    "ref={snakemake.input.ref}"
    "{input}"
    "{output}"
    "{params}"
    "threads={threads}"
    "overwrite=t"
    "{memory}"
    "{sort_bam}"
    "2> {log}"
       )
