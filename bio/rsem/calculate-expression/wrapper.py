__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


import os

from snakemake.shell import shell

bam = snakemake.input.get("bam", "")
fq_one = snakemake.input.get("fq_one", "")
fq_two = snakemake.input.get("fq_two", "")
if bam:
    if fq_one:
        raise Exception("Only input.bam or input.fq_one expected, got both.")
    input_bam = " --bam"
    input_string = bam
    paired_end = snakemake.params.get("paired-end", False)
else:
    input_bam = ""
    if fq_one:
        input_bam = False
        if isinstance(fq_one, list):
            num_fq_one = len(fq_one)
            input_string = ",".join(fq_one)
        else:
            num_fq_one = 1
            input_string = fq_one
        if fq_two:
            paired_end = True
            if isinstance(fq_two, list):
                num_fq_two = len(fq_two)
                if num_fq_one != num_fq_two:
                    raise Exception(
                        "Got {} R1 FASTQs, {} R2 FASTQs.".format(num_fq_one, num_fq_two)
                    )
            else:
                fq_two = [fq_two]
            input_string += " " + ",".join(fq_two)
        else:
            paired_end = False
    else:
        raise Exception("Expected input.bam or input.fq_one, got neither.")

if paired_end:
    paired_end_string = "--paired-end"
else:
    paired_end_string = ""

genes_results = snakemake.output.genes_results
if genes_results.endswith(".genes.results"):
    output_prefix = genes_results[: -len(".genes.results")]
else:
    raise Exception(
        "output.genes_results file name malformed "
        "(rsem will append .genes.results suffix)"
    )
if not snakemake.output.isoforms_results.endswith(".isoforms.results"):
    raise Exception(
        "output.isoforms_results file name malformed "
        "(rsem will append .isoforms.results suffix)"
    )

reference_prefix = os.path.splitext(snakemake.input.reference)[0]

extra = snakemake.params.get("extra", "")
threads = snakemake.threads
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "rsem-calculate-expression --num-threads {snakemake.threads} {extra} "
    "{paired_end_string} {input_bam} {input_string} "
    "{reference_prefix} {output_prefix} "
    "{log}"
)
