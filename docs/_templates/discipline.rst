.. _`{{name}}`:

{% macro category_section(name, description) -%}
{{ name|title }}
{{ '=' * name|length }}

A collection of wrappers to quickly use popular {{ description }} tools and libraries in `Snakemake <https://snakemake.readthedocs.io>`_ workflows.

The menu on the left (expand by clicking (+) if necessary), lists all available {{ description }} wrappers.

.. toctree::
    :glob:
    :hidden:
    :maxdepth: 2
    :caption: {{ name|title }} Modules
    
    {{ name|lower }}/*
{% endmacro %}

{{ category_section(name, description) }}