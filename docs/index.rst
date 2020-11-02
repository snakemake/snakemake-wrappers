
The Snakemake Wrappers repository
=================================

.. image:: https://img.shields.io/badge/snakemake-≥5.7.0-brightgreen.svg?style=flat-square
      :target: http://snakemake.readthedocs.io

.. image:: https://github.com/snakemake/snakemake-wrappers/workflows/CI/badge.svg?branch=master
      :target: https://github.com/snakemake/snakemake-wrappers/actions?query=branch%3Amaster+workflow%3ACI

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular tools
from `Snakemake <https://snakemake.readthedocs.io>`_ rules and workflows.

Usage
-----

The general strategy is to include a wrapper into your workflow via the `wrapper <http://snakemake.readthedocs.io/en/latest/snakefiles/modularization.html?highlight=wrapper#wrappers>`_ directive, e.g.

.. code-block:: python

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


Here, Snakemake will automatically download the corresponding wrapper from https://github.com/snakemake/snakemake-wrappers/tree/0.2.0/bio/samtools/sort. Thereby, 0.2.0 can be replaced with the `version tag <https://github.com/snakemake/snakemake-wrappers/releases>`_ you want to use, or a `commit id <https://github.com/snakemake/snakemake-wrappers/commits/master>`_. This ensures reproducibility since changes in the wrapper implementation won't be propagated automatically to your workflow. Alternatively, e.g., for development, the wrapper directive can also point to full URLs, including the local ``file://``.

Each wrapper defines required software packages and versions. In combination with the ``--use-conda`` flag of Snakemake, these will be deployed automatically.

Contribute 
----------

We invite anybody to contribute to the Snakemake Wrapper Repository.
If you want to contribute we suggest the following procedure:

#. Fork the repository: https://github.com/snakemake/snakemake-wrappers
#. Clone your fork locally.
#. Locally, create a new branch: ``git checkout -b my-new-snakemake-wrapper``
#. Commit your contributions to that branch and push them to your fork: ``git push -u origin my-new-snakemake-wrapper``
#. Create a pull request.

The pull request will be reviewed and included as fast as possible.
Contributions should follow the coding style of the already present examples, i.e.:

* provide a ``meta.yaml`` with name, description and author(s) of the wrapper
* provide an ``environment.yaml`` which lists all required software packages (the
  packages should be available for installation via the
  `default anaconda channels <https://anaconda.org/anaconda>`_ or via the
  `conda <https://conda.io/docs/>`_ channels
  `bioconda <https://bioconda.github.io/recipes.html>`_ or
  `conda-forge <https://conda-forge.org/feedstocks/>`_. 
  Other sustainable community maintained channels are possible as well.)
* provide a minimal test case in a subfolder called ``test``, with an example
  ``Snakefile`` that shows how to use the wrapper, some minimal testing data
  (also check existing wrappers for suitable data) and add an invocation of the
  test in ``test.py``
* follow the python `style guide <http://legacy.python.org/dev/peps/pep-0008>`_,
  using 4 spaces for indentation.

Testing locally
^^^^^^^^^^^^^^^

If you want to debug your contribution locally, before creating a pull request,
we recommend adding your test case to the start of the list in ``test.py``, so
that it runs first. Then, `install miniconda with the channels as described for
bioconda <https://bioconda.github.io/#using-bioconda>`_ and set up an
environment with the necessary dependencies and activate it::

  conda create -n test-snakemake-wrappers snakemake pytest conda
  conda activate test-snakemake-wrappers

Afterwards, from the main directory of the repo, you can run the tests with::

  pytest test.py -v

If you use a keyboard interrupt after your test has failed, you will get all
the relevant stdout and stderr messages printed.

If you also want to test the docs generation locally, create another environment
and activate it::

  conda create -n test-snakemake-wrapper-docs sphinx sphinx_rtd_theme pyyaml sphinx-copybutton
  conda activate test-snakemake-wrapper-docs

Then, enter the respective directory and build the docs::

  cd docs
  make html

If it runs through, you can open the main page at ``docs/_build/html/index.html``
in a web browser. If you want to start fresh, you can clean up the build
with ``make clean``.


.. toctree::
   :maxdepth: 3
   :glob:
   :hidden:
   :caption: Wrappers

   wrappers/*
   
.. toctree::
   :maxdepth: 3
   :glob:
   :hidden:
   :caption: Meta-Wrappers
      
   meta-wrappers/*
