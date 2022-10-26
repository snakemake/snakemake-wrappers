.. _`{{id}}`:

{{ name|upper }}
{{ name | length * '=' }}

{% if blacklisted %}
.. image:: https://img.shields.io/badge/blacklisted-{{ blacklisted|urlencode }}-red
{% endif %}

.. image:: https://img.shields.io/github/issues-pr/snakemake/snakemake-wrappers/{{ wrapper_path }}?label=version%20update%20pull%20requests
   :target: https://github.com/snakemake/snakemake-wrappers/pulls?q=is%3Apr+is%3Aopen+label%3A{{ wrapper_path }}

{{ description }}

{% if url %}
**URL**: {{ url }}
{% endif %}

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

{% if pkgs|length %}
Software dependencies
---------------------

{% for pkg in pkgs %}
* ``{{ pkg |replace(' ','')}}``
{% endfor %}
{% endif %}

{% if input and output %}
Input/Output
------------
{# Parse the input and output section of .yaml #}
{% for iotitle, io in ({"Input":input,"Output": output}).items() %}
**{{ iotitle }}:**

 {% for foo in io %}
  {% if foo is mapping %}
   {% for key, value in foo.items() %}
* ``{{ key }}``: {{ value }}
   {% endfor %}
  {% else %}
* {{ foo }}
  {% endif %}
 {% endfor %}

{% endfor %}
{% endif %}

{% if params %}

Params
------

{# Parse the params section of .yaml #}
{% for key in params %}
  {% if key is mapping %}
   {% for k, value in key.items() %}
* ``{{ k }}``: {{ value }}
   {% endfor %}
  {% else %}
* ``{{ key }}``: {{ params[key] }}
  {% endif %}

{% endfor %}

{% endif %}


Authors
-------

{% for author in authors %}
* {{ author }}
{% endfor %}


Code
----

.. code-block:: {{ wrapper_lang }}

{{ wrapper }}

.. |nl| raw:: html

   <br>
