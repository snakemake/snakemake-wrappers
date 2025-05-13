<!-- Ensure that the PR title follows conventional commit style (<type>: <description>)-->
<!-- Possible types are here: https://github.com/commitizen/conventional-commit-types/blob/master/index.json -->

<!-- Add a description of your PR here-->

### QC
<!-- Make sure that you can tick the boxes below. -->

* [ ] I confirm that I have followed the [documentation for contributing to `snakemake-wrappers`](https://snakemake-wrappers.readthedocs.io/en/stable/contributing.html).

While the contributions guidelines are more extensive, please particularly ensure that:
* [ ] `test.py` was updated to call any added or updated example rules in a `Snakefile`
* [ ] `input:` and `output:` file paths in the rules can be chosen arbitrarily
* [ ] wherever possible, command line arguments are inferred and set automatically (e.g. based on file extensions in `input:` or `output:`)
* [ ] temporary files are either written to a unique hidden folder in the working directory, or (better) stored where the Python function `tempfile.gettempdir()` points to 
* [ ] the `meta.yaml` contains a link to the documentation of the respective tool or command under `url:`
* [ ] conda environments use a minimal amount of channels and packages, in recommended ordering
