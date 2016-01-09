[![Snakemake](https://img.shields.io/badge/snakemake-≥3.5.0-brightgreen.svg?style=flat-square)](https://bitbucket.org/johanneskoester/snakemake)

# The Snakemake Wrapper Repository

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular command line tools 
from [Snakemake](https://bitbucket.org/johanneskoester/snakemake) rules and workflows.

## Structure

Wrappers can be found under

```
<discipline>/<name>/
```

The general strategy is to include these into your workflow via the [wrapper](https://bitbucket.org/snakemake/snakemake/wiki/Documentation#markdown-header-external-wrapper) directive. Examples can be found in the READMEs located in the wrapper subdirectories.

## Contribute

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* provide a README.md describing the usage and purpose,
* define author with email address and a license,
* follow the python [style guide](http://legacy.python.org/dev/peps/pep-0008),
* use 4 spaces for indentation.
