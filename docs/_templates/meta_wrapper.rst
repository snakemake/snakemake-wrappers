.. _`{{name}}`:

{{ name|upper }}
{{ name | length * '=' }}

{{ description }}


Example
-------

This meta-wrapper can be used in the following way:

.. code-block:: python

{{ snakefile }}

Note that input, output and log file paths can be chosen freely.
When running with

.. code-block:: bash

    snakemake --use-conda

the software dependencies will be automatically deployed into an isolated environment before execution.
{% if usedwrappers|length %}


Used wrappers
---------------------

{% for uw in usedwrappers %}
* :ref:`{{ uw }}`
{% endfor %}
{% endif %}


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

