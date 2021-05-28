### Description

<!--Add a description of your PR here-->

### QC
<!-- Make sure that you can tick the boxes below. -->

For all wrappers added by this PR, I made sure that

* [ ] there is a test case which covers any introduced changes,
* [ ] `input:` and `output:` file paths in the resulting rule can be changed arbitrarily,
* [ ] all `environment.yaml` specifications follow [the respective best practices](https://stackoverflow.com/a/64594513/2352071),
* [ ] wherever possible, command line arguments are inferred and set automatically (e.g. based on file extensions in `input:` or `output:`),
* [ ] all fields of the example rules in the `Snakefile`s and their entries are explained via comments (`input:`/`output:`/`params:` etc.),
* [ ] `stderr` and/or `stdout` are logged correctly (`log:`), depending on the wrapped tool,
* [ ] the `meta.yaml` contains a link to the documentation of the respective tool or command,
* [ ] `Snakefile`s pass the linting (`snakemake --lint`),
* [ ] `Snakefile`s are formatted with [snakefmt](https://github.com/snakemake/snakefmt),
* [ ] Python wrapper scripts are formatted with [black](https://black.readthedocs.io).
