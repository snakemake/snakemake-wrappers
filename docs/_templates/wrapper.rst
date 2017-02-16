.. _`{{name}}`:

{{ name|upper }}
==========

{{ description }}


Software dependencies
---------------------

{% for pkg in pkgs %}
* {{ pkg }}
{% endfor %}


Example
-------

This wrapper can be used in the following way:

.. code-block:: python

{{ snakefile }}

Note that input, output and log file paths can be chosen freely.
When running with

.. code-block:: bash

    snakemake --use-conda

the software dependencies will be automatically deployed into an isolated environment before execution.

{% if notes %}

Notes
-----

{{ notes }}
{% endif %}

Authors
-------

{% for author in authors %}
* {{ author }}
{% endfor %}
