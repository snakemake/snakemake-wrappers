.. _`{{name}}`:

{{ name|upper }}
{{ name | length * '=' }}

{{ description }}


Example
-------

This meta-wrapper can be used by integrating the following into your workflow:

.. code-block:: python

{{ snakefile }}

Note that input, output and log file paths can be chosen freely, as long as the dependencies between the rules remain as listed here.
For additional parameters in each individual wrapper, please refer to their corresponding documentation (see links below).

When running with

.. code-block:: bash

    snakemake --use-conda

the software dependencies will be automatically deployed into an isolated environment before execution.
{% if usedwrappers|length %}


Used wrappers
---------------------

The following individual wrappers are used in this meta-wrapper:

{% for uw in usedwrappers %}
* :ref:`{{ uw }}`
{% endfor %}

Please refer to each wrapper in above list for additional configuration parameters and information about the executed code.

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

