# Wrapper for delly.

## Example:

```
from snakemake.remote import HTTP

HTTP = HTTP.RemoteProvider()

rule delly:
    input:
        ref="genome.fasta",
        samples=expand("mapped/{sample}.bam", sample=config["samples"]),
        indexes=expand("mapped/{sample}.bam.bai", sample=config["samples"]),
        # optional exclude template
        exclude=HTTP.remote("https://github.com/tobiasrausch/delly/raw/master/excludeTemplates/human.hg19.excl.tsv", keep_local=True)
    output:
        "sv/{type,(DEL|DUP|INV|TRA|INS)}.vcf"
    params:
        ""  # optional parameters for delly (except -t, -g)
    log:
        "logs/delly/{type}.log"
    threads: 3
    wrapper:
        "0.0.13/bio/delly"
```
