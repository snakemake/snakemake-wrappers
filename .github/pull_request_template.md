<!-- Ensure that the PR title follows conventional commit style (<type>: <description>)-->
<!-- Possible types are here: https://github.com/commitizen/conventional-commit-types/blob/master/index.json -->

<!-- Add a description of your PR here-->

### QC
<!-- Make sure that you can tick the boxes below. -->

* [ ] I confirm that:

For all wrappers added by this PR, 

* there is a test case which covers any introduced changes,
* `input:` and `output:` file paths in the resulting rule can be changed arbitrarily,
* either the wrapper can only use a single core, or the example rule contains a `threads: x` statement with `x` being a reasonable default,
* rule names in the test case are in [snake_case](https://en.wikipedia.org/wiki/Snake_case) and somehow tell what the rule is about or match the tools purpose or name (e.g., `map_reads` for a step that maps reads),
* all `environment.yaml` specifications follow [the respective best practices](https://stackoverflow.com/a/64594513/2352071),
* the `environment.yaml` pinning has been updated by running `snakedeploy pin-conda-envs environment.yaml` on a linux machine,
* wherever possible, command line arguments are inferred and set automatically (e.g. based on file extensions in `input:` or `output:`),
* all fields of the example rules in the `Snakefile`s and their entries are explained via comments (`input:`/`output:`/`params:` etc.),
* `stderr` and/or `stdout` are logged correctly (`log:`), depending on the wrapped tool,
* temporary files are either written to a unique hidden folder in the working directory, or (better) stored where the Python function `tempfile.gettempdir()` points to (see [here](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir); this also means that using any Python `tempfile` default behavior works),
* the `meta.yaml` contains a link to the documentation of the respective tool or command,
* `Snakefile`s pass the linting (`snakemake --lint`),
* `Snakefile`s are formatted with [snakefmt](https://github.com/snakemake/snakefmt),
* Python wrapper scripts are formatted with [black](https://black.readthedocs.io).
* Conda environments use a minimal amount of channels, in recommended ordering. E.g. for bioconda, use (conda-forge, bioconda, nodefaults, as conda-forge should have highest priority and defaults channels are usually not needed because most packages are in conda-forge nowadays).
