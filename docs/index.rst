
The Snakemake Wrappers repository
=================================

.. image:: https://img.shields.io/badge/snakemake-≥5.7.0-brightgreen.svg?style=flat-square
      :target: http://snakemake.readthedocs.io

.. image:: https://github.com/snakemake/snakemake-wrappers/workflows/Tests/badge.svg?branch=master
      :target: https://github.com/snakemake/snakemake-wrappers/actions?query=branch%3Amaster+workflow%3ATests

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


Here, Snakemake will automatically download and use the corresponding wrapper files from https://github.com/snakemake/snakemake-wrappers/tree/0.2.0/bio/samtools/sort.
Thereby, ``0.2.0`` can be replaced with the `version tag <https://github.com/snakemake/snakemake-wrappers/releases>`_ you want to use, or a `commit id <https://github.com/snakemake/snakemake-wrappers/commits/master>`_.
This ensures reproducibility since changes in the wrapper implementation will only be propagated to your workflow if you update that version tag.

Each wrapper defines required software packages and versions in an ``environment.yaml`` file.
In combination with the ``--use-conda`` flag of Snakemake, this will be deployed automatically.

Alternatively, for example for development, the wrapper directive can also point to full URLs, including the local ``file://``.
For this to work, you need to provide the (remote) path to the directory containing the ``wrapper.*`` and ``environment.yaml`` files.
For the above example, the explicit GitHub URL to specify would need to be the ``/raw/`` version of the directory:

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
            "https://github.com/snakemake/snakemake-wrappers/raw/0.2.0/bio/samtools/sort"


Maintainers
-----------

- Johannes Köster (`johanneskoester <https://github.com/johanneskoester>`_)
- Filipe G. Vieira (`fgvieira <https://github.com/fgvieira>`_)
- Thibault Dayris (`tdayris <https://github.com/tdayris>`_)
- Felix Mölder (`FelixMoelder <https://github.com/FelixMoelder>`_)
- David Laehnemann (`dlaehnemann <https://github.com/dlaehnemann>`_)


Contributing
------------

We invite anybody to contribute to the Snakemake Wrapper Repository.
If you want to contribute refer to the :ref:`contributing guide <contributing>`.


.. toctree::
   :maxdepth: 4
   :glob:
   :hidden:
   :caption: Wrappers and Meta-Wrappers
      
   wrappers
   meta-wrappers


.. toctree::
    :caption: Development
    :maxdepth: 2
    :hidden:

    contributing
    changelog
