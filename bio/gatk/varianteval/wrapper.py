__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)


vcf = snakemake.input.vcf
if isinstance(vcf, str):
    vcf = "--eval  {}".format(vcf)
else:
    vcf = list(map("--eval {}".format, vcf))

bam = snakemake.input.get("bam", "")
if bam:
    if isinstance(bam, str):
        bam = "--input  {}".format(bam)
    else:
        bam = list(map("--input {}".format, bam))

ref = snakemake.input.get("ref", "")
if ref:
    ref = "--reference " + ref

ref_dict = snakemake.input.get("dict", "")
if ref_dict:
    ref_dict = "--sequence-dictionary " + ref_dict

known = snakemake.input.get("known", "")
if known:
    known = "--dbsnp " + known

comp = snakemake.input.get("comp", "")
if comp:
    if isinstance(comp, str):
        comp = "--comparison  {}".format(comp)
    else:
        comp = list(map("--comparison {}".format, comp))

ped = snakemake.input.get("ped", "")
if ped:
    ped = "--pedigree " + ped


log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "gatk --java-options '{java_opts}' VariantEval "
    "{vcf} "
    "{bam} "
    "{ref} "
    "{ref_dict} "
    "{known} "
    "{ped} "
    "{comp} "
    "{extra} --output {snakemake.output[0]} {log}"
)
