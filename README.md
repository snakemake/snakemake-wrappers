[![Snakemake](https://img.shields.io/badge/snakemake-≥3.5.0-brightgreen.svg?style=flat-square)](https://bitbucket.org/johanneskoester/snakemake)

# The Snakemake Wrapper Repository

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular command line tools 
from [Snakemake](https://bitbucket.org/johanneskoester/snakemake) rules and workflows.
**This repository is experimental and subject to unannounced changes.**

## Structure

Wrappers can be found under

```
<discipline>/<subject>/<name>.py
```

The general strategy is to include these into your workflow via the [script](https://bitbucket.org/snakemake/snakemake/wiki/Documentation#markdown-header-external-scripts) directive.
This can also happen via https urls (in this case make sure, that you trust the source).

## Contribute

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* start with a docstring describing the usage and purpose,
* define author with email address and a license,
* follow the python [style guide](http://legacy.python.org/dev/peps/pep-0008),
* use 4 spaces for indentation.