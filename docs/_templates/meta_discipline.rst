.. _`{{name}}`:

{% macro meta_wrapper_section(name, description) -%}
{{ name }} 
============

Curated and tested combinations of {{ description|lower }} wrappers that fulfil common tasks with popular {{ description }} tools, in a best-practice way.
For using them, simply copy-paste the offered snippets into your `Snakemake <https://snakemake.github.io>`_ workflow.

The menu on the left (expand by clicking (+) if necessary), lists all available {{ description }} meta-wrappers.

.. toctree::
   :maxdepth: 3
   :glob:
   :hidden:
   :caption: {{ name|title }} Meta-Wrappers
      
   {{ name|lower }}/*
{% endmacro %}

{{ meta_wrapper_section(name, description) }}