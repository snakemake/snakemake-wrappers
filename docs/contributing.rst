.. _contributing:

Contributing
============

We invite anybody to contribute to the Snakemake Wrapper Repository.
If you want to contribute we suggest the following procedure:

#. Fork the repository: https://github.com/snakemake/snakemake-wrappers
#. Clone your fork locally.
#. Locally, create a new branch: ``git checkout -b my-new-snakemake-wrapper``
#. Commit your contributions to that branch and push them to your fork: ``git push -u origin my-new-snakemake-wrapper``
#. Create a pull request.

The pull request will be reviewed and included as fast as possible.
If your pull request does not get a review quickly, you can `@mention <https://github.blog/2011-03-23-mention-somebody-they-re-notified/>` previous contributors to a particular wrapper (``git blame``) or regular contributors that you think might be able to give a review.
Contributions should follow the coding style of the already present examples, i.e.:

* provide a ``meta.yaml`` that describes the wrapper (see the `meta.yaml documentation below <meta>`_)
* provide an ``environment.yaml`` which lists all required software packages and follows
  `the respective best practices <https://stackoverflow.com/a/64594513/2352071>`_. The
  packages should be available for installation via the
  `default anaconda channels <https://anaconda.org/anaconda>`_ or via the
  `conda`_ channels
  `bioconda <https://bioconda.github.io/recipes.html>`_ or
  `conda-forge <https://conda-forge.org/feedstocks/>`_.
  Other sustainable community maintained channels are possible as well.
* add a ``wrapper.py`` or ``wrapper.R`` file that can deal with arbitrary ``input:`` and ``output:`` paths.
* provide a minimal test case in a subfolder called ``test``, with an example
  ``Snakefile`` that shows how to use the wrapper (rule names should be descriptive and written in `snake_case <https://en.wikipedia.org/wiki/Snake_case>`_), some minimal testing data
  (also check existing wrappers for suitable data) and add an invocation of the
  test in ``test.py``
* ensure consistent `formatting`_ of Python files and `linting`_ of Snakefiles.

.. _meta:

``meta.yaml`` file
-------------------

The following fields are available to use in the wrapper ``meta.yaml`` file. All, except
those marked optional, should be provided.

* **name**: The name of the wrapper.
* **description**: a description of what the wrapper does.
* **url**: URL to the wrapper tool webpage.
* **authors**: A `sequence`_ of names of the people who have contributed to the wrapper.
* **input**: A `mapping`_ or `sequence`_ of required inputs for the wrapper.
* **output**: A `mapping`_ or `sequence`_ of output(s) from the wrapper.
* **params** (optional): A `mapping`_ of parameters that can be used in the wrapper's ``params`` directive. If no parameters are used for the wrapper, this field can be omitted.
* **notes** (optional): Anything of note that does not fit into the scope of the other fields.

You can add a newline to the rendered text in these fields with the addition of ``|nl|``

Example
^^^^^^^

.. code-block:: yaml

    name: seqtk mergepe
    description: Interleave two paired-end FASTA/Q files
    url: https://github.com/lh3/seqtk
    authors:
      - Michael Hall
    input:
      - paired fastq files - can be compressed.
    output:
      - >
        a single, interleaved FASTA/Q file. By default, the output will be compressed,
        use the param ``compress_lvl`` to change this.
    params:
      compress_lvl: >
        Regulate the speed of compression using the specified digit,
        where 1 indicates the fastest compression method (less compression)
        and 9 indicates the slowest compression method (best compression).
        0 is no compression. 11 gives a few percent better compression at a severe cost
        in execution time, using the zopfli algorithm. The default is 6.
    notes: Multiple threads can be used during compression of the output file with ``pigz``.



.. _sequence: https://yaml.org/spec/1.2/spec.html#id2759963
.. _mapping: https://yaml.org/spec/1.2/spec.html#id2759963

.. _formatting:

Formatting
----------

Please ensure Python files such as ``test.py`` and ``wrapper.py`` are formatted with
|black|_. Additionally, please format your test ``Snakefile`` with |snakefmt|_.

.. |black| replace:: ``black``
.. _black: https://github.com/psf/black
.. |snakefmt| replace:: ``snakefmt``
.. _snakefmt: https://github.com/snakemake/snakefmt

.. _linting:

Linting
-------

Please `lint`_ your test ``Snakefile`` with::

    snakemake -s <path/to/wrapper/test/Snakefile> --lint

.. _lint: https://snakemake.readthedocs.io/en/stable/snakefiles/writing_snakefiles.html#best-practices

Testing locally
---------------

If you want to debug your contribution locally (before creating a pull request), you
can install all dependencies with |mamba|_ (or |conda|_). `Install miniconda with the
channels as described for bioconda <https://bioconda.github.io/#using-bioconda>`_ and
set up an environment with the necessary dependencies and activate it::

  mamba create -n test-snakemake-wrappers snakemake pytest conda snakefmt black
  conda activate test-snakemake-wrappers

Afterwards, from the main directory of the repo, you can run the test(s) for your
contribution by `specifying an expression <https://docs.pytest.org/en/stable/usage.html#specifying-tests-selecting-tests>`_
that matches the name(s) of your test(s) via the ``-k`` option of ``pytest``::

  pytest test.py -v -k your_test


If you also want to test the docs generation locally, create another environment
and activate it::

  mamba create -n test-snakemake-wrapper-docs sphinx sphinx_rtd_theme pyyaml sphinx-copybutton
  conda activate test-snakemake-wrapper-docs

Then, enter the respective directory and build the docs::

  cd docs
  make html

If it runs through, you can open the main page at ``docs/_build/html/index.html``
in a web browser. If you want to start fresh, you can clean up the build
with ``make clean``.


.. |mamba| replace:: ``mamba``
.. _mamba: https://github.com/mamba-org/mamba
.. |conda| replace:: ``conda``
.. _conda: https://conda.io
