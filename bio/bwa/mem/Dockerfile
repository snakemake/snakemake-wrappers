FROM snakemake/snakemake
# docker build -t snakemake-wrappers/bwa/mem
# How to test from test folder:
# snakemake --cores 1 mapped/a.bam --use-conda -F -s Snakefile_samtools
MAINTAINER Johannes Köster <johannes.koester@tu-dortmund.de>
ADD . /tmp/repo
WORKDIR /tmp/repo
RUN /bin/bash -c "source activate snakemake && \
    conda env update --file /tmp/repo/environment.yaml --prune"
