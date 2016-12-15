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
