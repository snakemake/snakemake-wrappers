__author__ = "David Laehnemann, Victoria Sack"
__copyright__ = "Copyright 2018, David Laehnemann, Victoria Sack"
__email__ = "david.laehnemann@hhu.de"
__license__ = "MIT"



from snakemake.shell import shell
import os
import tempfile
import re


# Create temporary directory that will only contain the symbolic link to the
# input file, in order to sanely work with the art_profiler_illumina cli
with tempfile.TemporaryDirectory() as temp_input:
    # ensure that .fastq and .fastq.gz input files work, as well
    filename = os.path.basename(snakemake.input[0] ).replace('.fastq', '.fq')

    # figure out the exact file extension after the above substitution
    ext = re.search("fq(\.gz)?$", filename)
    if ext:
        fq_extension = ext.group(0)
    else:
        raise IOError("Incompatible extension: This art_profiler_illumina "
                    "wrapper requires input files with one of the following "
                    "extensions: fastq, fastq.gz, fq or fq.gz. Please adjust "
                    "your input and the invocation of the wrapper accordingly.")

    os.symlink(
                # snakemake paths are relative, but the symlink needs to be absolute
                os.path.abspath(snakemake.input[0] ),
                # strip temp file name of any infixes, to circumvent art read
                # enumeration magic
                os.path.join(temp_input, "input." + fq_extension)
                )

    # include output folder name in the profile_name command line argument and
    # strip off the file extension, as art will add its own ".txt"
    profile_name = os.path.join( os.path.dirname(snakemake.output[0] ), filename.replace("." + fq_extension, '' ) )

    shell(
        "( art_profiler_illumina {snakemake.params} {profile_name}"
        " {temp_input} {fq_extension} {snakemake.threads} ) 2> {snakemake.log}")
