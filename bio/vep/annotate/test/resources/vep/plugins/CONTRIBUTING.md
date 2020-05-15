# Contribution Guide

We welcome contributions from outside the Ensembl team and our full contribution guidelines are available [here](https://github.com/Ensembl/ensembl/blob/master/CONTRIBUTING.md).

Please submit new plugins and updates as pull requests against the MASTER branch unless otherwise discussed.

## Plugin Development

To make development of plugins easier, we suggest you use the [Bio::EnsEMBL::Variation::Utils::BaseVepPlugin](https://github.com/Ensembl/ensembl-variation/blob/master/modules/Bio/EnsEMBL/Variation/Utils/BaseVepPlugin.pm) module as your base class, as this provides default implementations of all the necessary methods which can be overridden as required.
The documentation in this module provides details of all required methods and a simple example of a plugin implementation. 
Also see [Bio::EnsEMBL::Variation::Utils::BaseVepTabixPlugin](https://github.com/Ensembl/ensembl-variation/blob/master/modules/Bio/EnsEMBL/Variation/Utils/BaseVepTabixPlugin.pm) for reading tabix-indexed files.

Ensembl VEP provides multiple output formats; it is worth testing plugins with each format for ease of parsing.

Fuller guidance on creating and using plugins for Ensembl VEP is given [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html).

## Documentation

* Please add NAME and DESCRIPTION sections to the POD header - these are used to automatically create documentation pages.
* The documentation should include enough information for others to use the plugin, including:
  * full instructions on how to download and format any required data
  * full instructions on how to download and install required software
* Also acknowledge any data/tool provider with any text they specify on their website, including the project URL and latest publication where possible. 

## Licence
Please add a licence and your contact details. Ensembl code is licensed under the Apache 2.0 License and our expectation is that contributed code is made available under the same License. Any copyright assertion to other organisations should be declared in the modifying file and in the root LICENSE section.


