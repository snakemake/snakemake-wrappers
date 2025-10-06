.. _`{{name}}`:

{{ name|upper }}
{{ name | length * '=' }}

{{ description }}

{% set module_name = name|lower|replace('-', '_') %}


Usage
-----

Via module
~~~~~~~~~~

This usage is recommended with Snakemake ``>=7.9``.
You can include this meta-wrapper in your workflow via the `Snakemake module system <https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#meta-wrappers>`__:

.. code-block:: python

    module {{ module_name }}:
        meta_wrapper: "{{ uri }}"
        pathvars:
            {% for var, desc in pathvars.items() -%}
            {{ var }}="...", # {{ desc }}
            {%- endfor %}

    use rule * from {{ module_name }} as {{ module_name }}_*

Upon using the rules, you can additionally modify input, output, log, and params as needed (see the definition of each rule below and the `modules documentation <https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#modules>`__).
For additional parameters in each individual wrapper, please refer to their corresponding documentation (see links below).

Via copy-paste
~~~~~~~~~~~~~~

Alternatively, you can directly copy-paste and modify the full meta-wrapper code below into your workflow.

Execution
~~~~~~~~~


When running with

.. code-block:: bash

    snakemake --sdm conda

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

Code
----

.. code-block:: python

{{ snakefile }}