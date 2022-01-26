# Changelog

## [0.87.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v0.86.0...v0.87.0) (2022-01-26)


### Features

* added wrapper for bcftools stats ([#201](https://www.github.com/snakemake/snakemake-wrappers/issues/201)) ([2caecb9](https://www.github.com/snakemake/snakemake-wrappers/commit/2caecb9aabd532fa1dc0cdb4b713208614c74ef2))
* added wrapper for bgzip ([#195](https://www.github.com/snakemake/snakemake-wrappers/issues/195)) ([6d837f2](https://www.github.com/snakemake/snakemake-wrappers/commit/6d837f2096749fce45eda44cfe2daab1d057449d))
* added wrapper for seqtk seq subcommand ([#202](https://www.github.com/snakemake/snakemake-wrappers/issues/202)) ([599f370](https://www.github.com/snakemake/snakemake-wrappers/commit/599f37078dbe669106a867845da0caddfa259908))
* added wrapper for using tabix to query an indexed file ([#203](https://www.github.com/snakemake/snakemake-wrappers/issues/203)) ([2bb9131](https://www.github.com/snakemake/snakemake-wrappers/commit/2bb91310af377fc19fc8c9df1e6ee7b4bf8c6836))
* explicitly specify bwa index in bwa wrappers ([#232](https://www.github.com/snakemake/snakemake-wrappers/issues/232)) ([0e323b1](https://www.github.com/snakemake/snakemake-wrappers/commit/0e323b1ee64b4db65c36466460efba8faac85731))
* Implemented handling of memory constraints in fasterq-dump wrapper ([#432](https://www.github.com/snakemake/snakemake-wrappers/issues/432)) ([7febbb0](https://www.github.com/snakemake/snakemake-wrappers/commit/7febbb0903daf82dae125f54fe9cac5577c8393b))
* parse mem for samtools sort ([#442](https://www.github.com/snakemake/snakemake-wrappers/issues/442)) ([37c2d08](https://www.github.com/snakemake/snakemake-wrappers/commit/37c2d08895efe1a596b2f9e1b76ab4150d39f2cf))
* wrapper for Manta SV caller ([#415](https://www.github.com/snakemake/snakemake-wrappers/issues/415)) ([6b4d6a1](https://www.github.com/snakemake/snakemake-wrappers/commit/6b4d6a1282efd651bfdd097d4b780247f5474c35))

## [0.86.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v0.85.1...v0.86.0) (2022-01-18)


### Features

* add fasttree wrapper ([#405](https://www.github.com/snakemake/snakemake-wrappers/issues/405)) ([ad99f9e](https://www.github.com/snakemake/snakemake-wrappers/commit/ad99f9ef63a4e80b51860f71287d4396b055a9da))
* add MUSCLE wrapper ([#404](https://www.github.com/snakemake/snakemake-wrappers/issues/404)) ([564ada7](https://www.github.com/snakemake/snakemake-wrappers/commit/564ada7de5a4beb124ee5be16b80f0d5a53d51e0))
* added shards temp folder ([#441](https://www.github.com/snakemake/snakemake-wrappers/issues/441)) ([dda1546](https://www.github.com/snakemake/snakemake-wrappers/commit/dda1546a924e8646e11c5020246622d64b2b5ffa))
* update multiqc wrapper to v1.11 ([#422](https://www.github.com/snakemake/snakemake-wrappers/issues/422)) ([0fa22a3](https://www.github.com/snakemake/snakemake-wrappers/commit/0fa22a3b8a4c8355fd103b85eb1fecfb1e0c4bc0))
* updated versions and fixes for samtools wrappers. ([#431](https://www.github.com/snakemake/snakemake-wrappers/issues/431)) ([cbba82d](https://www.github.com/snakemake/snakemake-wrappers/commit/cbba82daf9ce90888924e91f2aa4524ca0bf7ca4))
* added wrapper for verifybamid2 ([#401](https://github.com/snakemake/snakemake-wrappers/pull/401))


### Bug Fixes

* log file handling and other small improvements for bcftools wrappers ([#429](https://www.github.com/snakemake/snakemake-wrappers/issues/429)) ([961edb8](https://www.github.com/snakemake/snakemake-wrappers/commit/961edb8cfe7b224b2ddb6344caf5293a0938d003))
* proper tempfile handling for STAR and improved documentation ([#430](https://www.github.com/snakemake/snakemake-wrappers/issues/430)) ([922cf87](https://www.github.com/snakemake/snakemake-wrappers/commit/922cf87856e61f6cbf408d2c31c83723dfe67f5b))
* correctly handle extra parameters in vardict wrapper ([#437](https://github.com/snakemake/snakemake-wrappers/pull/437))

### [0.85.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v0.85.0...v0.85.1) (2022-01-14)


### Bug Fixes

* fix bug in pindel2vcf wrapper ([#433](https://www.github.com/snakemake/snakemake-wrappers/issues/433)) ([f94b225](https://www.github.com/snakemake/snakemake-wrappers/commit/f94b2251914f585c44fe562bc67d815e2431bcf8))
