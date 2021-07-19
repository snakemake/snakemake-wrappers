__author__ = "Graeme Ford"
__copyright__ = "Copyright 2021, Graeme Ford"
__email__ = "graeme.ford@tuks.co.za"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
preloader = snakemake.params.get("preloader", "")

command = [
    "-{key} {value}".format(key=key, value=value)
    for key, value in snakemake.params.iteritems()
    if value is not None
].join(" ")


shell(
    "{preloader} "
    "gatk "
    "--java-options '{java_opts}' "
    "ValidateVariants "
    "{command} "
    "{log}"
)
