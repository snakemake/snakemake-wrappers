
The Snakemake Wrappers repository
=================================

.. image:: https://img.shields.io/badge/snakemake-≥4.5.0-brightgreen.svg?style=flat-square
      :target: http://snakemake.bitbucket.io

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular tools
from `Snakemake <https://snakemake.bitbucket.io>`_ rules and workflows.

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


Here, Snakemake will automatically download the corresponding wrapper from https://bitbucket.org/snakemake/snakemake-wrappers/src/0.2.0/bio/samtools/sort/wrapper.py. Thereby, 0.2.0 can be replaced with the version tag you want to use, or a commit id (see `here <https://bitbucket.org/snakemake/snakemake-wrappers/commits/>`_). This ensures reproducibility since changes in the wrapper implementation won't be propagated automatically to your workflow. Alternatively, e.g., for development, the wrapper directive can also point to full URLs, including the local ``file://``.

Each wrapper defines required software packages and versions. In combination with the ``--use-conda`` flag of Snakemake, these will be deployed automatically.

Contribute
----------

We invite anybody to contribute to the Snakemake Wrapper Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* provide a meta.yaml with name, description and author of the wrapper,
* provide an environment.yaml which lists all required software packages (the packages shall be available via https://anaconda.org),
* provide an example Snakefile that shows how to use the wrapper,
* follow the python `style guide <http://legacy.python.org/dev/peps/pep-0008>`_,
* use 4 spaces for indentation.


.. toctree::
   :maxdepth: 3
   :glob:
   :hidden:
   :caption: Wrappers

   wrappers/*
