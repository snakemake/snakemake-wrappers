[![Snakemake](https://img.shields.io/badge/snakemake-≥3.5.5-brightgreen.svg?style=flat-square)](https://bitbucket.org/johanneskoester/snakemake)

# The Snakemake Wrapper Repository

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular command line tools
from [Snakemake](https://bitbucket.org/johanneskoester/snakemake) rules and workflows.

## Usage

Wrappers can be found under

```
<discipline>/<name>/
```

in this repository.
The general strategy is to include these into your workflow via the [wrapper](https://bitbucket.org/snakemake/snakemake/wiki/Documentation#markdown-header-wrappers) directive, e.g.
```
#!python

rule samtools_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    params:
        "-m 4G"
    threads: 8
    wrapper:
        "0.2.0/bio/samtools/sort"
```
Here, Snakemake will automatically download the corresponding wrapper from https://bitbucket.org/snakemake/snakemake-wrappers/src/0.0.8/bio/samtools_sort/wrapper.py. Thereby, 0.0.8 can be replaced with the version tag you want to use, or a commit id (see [here](https://bitbucket.org/snakemake/snakemake-wrappers/commits/)). This ensures reproducibility since changes in the wrapper implementation won't be propagated automatically to your workflow. Alternatively, e.g., for development, the wrapper directive can also point to full URLs, including the local ``file://``.
Examples for each wrapper can be found in the READMEs located in the wrapper subdirectories.

Each wrapper defines required software packages and versions via a ``requirements.txt`` file in the same directory.
In the future, Snakemake will automatically install the required packages before job execution via https://anaconda.org.

## Contribute

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* provide a README.md describing the usage and purpose,
* provide a requirements.txt which lists all required software packages (the packages shall be available via https://anaconda.org),
* define author with email address and a license,
* follow the python [style guide](http://legacy.python.org/dev/peps/pep-0008),
* use 4 spaces for indentation.
