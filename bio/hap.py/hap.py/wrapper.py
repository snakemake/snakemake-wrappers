__author__ = "Nathan Olson"
__copyright__ = "This is a U.S. government work and not under copyright protection in the U.S.; foreign copyright protection may apply "
__email__ = "nolson@nist.gov"
__license__ = """
This software was developed by employees of the National Institute of Standards and Technology (NIST), 
an agency of the Federal Government and is being made available as a public service. Pursuant to title 
17 United States Code Section 105, works of NIST employees are not subject to copyright protection in 
the United States.  This software may be subject to foreign copyright.  Permission in the United States 
and in foreign countries, to the extent that NIST may hold copyright, to use, copy, modify, create 
derivative works, and distribute this software and its documentation without fee is hereby granted on 
a non-exclusive basis, provided that this notice and disclaimer of warranty appears in all copies. 

THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, 
INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND FREEDOM FROM INFRINGEMENT, AND ANY 
WARRANTY THAT THE DOCUMENTATION WILL CONFORM TO THE SOFTWARE, OR ANY WARRANTY THAT THE SOFTWARE WILL BE 
ERROR FREE.  IN NO EVENT SHALL NIST BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT, 
INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR IN ANY WAY CONNECTED WITH 
THIS SOFTWARE, WHETHER OR NOT BASED UPON WARRANTY, CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS 
SUSTAINED BY PERSONS OR PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE OUT OF 
THE RESULTS OF, OR USE OF, THE SOFTWARE OR SERVICES PROVIDED HEREUNDER.
"""

from os import path

from snakemake.shell import shell

# Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Optional parameters
engine = snakemake.params.get("engine", "")
if engine:
    engine = "--engine {}".format(engine)

truth_regions = snakemake.input.get("truth_regions", "")
if truth_regions:
    truth_regions = "-f {}".format(truth_regions)

strats = snakemake.input.get("strats", "")
if strats:
    strats = "--stratification {}".format(strats)


shell(
    "(hap.py"
    " --threads {snakemake.threads}"
    " {engine}"
    " -r {snakemake.input.genome}"
    " {extra}"
    " {truth_regions}"
    " {strats}"
    " -o {snakemake.params.prefix}"
    " {snakemake.input.truth}"
    " {snakemake.input.query})"
    " {log}"
)
