.. Snakemake Wrappers documentation master file, created by
   sphinx-quickstart on Wed Dec 14 09:55:46 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Snakemake Wrappers's documentation!
==============================================

{% for tool in tools %}
.. toctree::
   :maxdepth: 0
   :glob:
   :hidden:
   :caption: {{ tool }}
   
   wrappers/{{ tool }}/*
{% endfor %}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
