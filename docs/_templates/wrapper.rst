.. _`{{id}}`:

{{ name|upper }}
{{ name | length * '=' }}

{{ description }}

**URL**: {{ url }}

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

.. code-block:: {{ wrapper_lang }}

{{ wrapper }}

.. |nl| raw:: html

   <br>
