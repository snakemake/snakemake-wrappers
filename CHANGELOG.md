# Changelog

## [1.15.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.14.1...v1.15.0) (2022-10-11)


### Features

* add cram support to applybsqr ([#563](https://www.github.com/snakemake/snakemake-wrappers/issues/563)) ([41bb50b](https://www.github.com/snakemake/snakemake-wrappers/commit/41bb50b065b4712c712ca86be50142c20fd31dc9))
* bwa-meme picard option ([#558](https://www.github.com/snakemake/snakemake-wrappers/issues/558)) ([76174cf](https://www.github.com/snakemake/snakemake-wrappers/commit/76174cf1c82e2b300505159b476560bf87d0fb29))


### Bug Fixes

* improve bcftools norm example rule ([#561](https://www.github.com/snakemake/snakemake-wrappers/issues/561)) ([ad41354](https://www.github.com/snakemake/snakemake-wrappers/commit/ad41354b3308e2c2926d9ca7b6fa258dfb555815))

### [1.14.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.14.0...v1.14.1) (2022-09-27)


### Bug Fixes

* fix regression in bcftools concat wrapper that made it use only the first input file. The bug was introduced in wrapper version v1.8.0. ([#559](https://www.github.com/snakemake/snakemake-wrappers/issues/559)) ([80960db](https://www.github.com/snakemake/snakemake-wrappers/commit/80960db8f36edff2a5f0c9df4c93f767a1f74af3))

## [1.14.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.13.0...v1.14.0) (2022-09-19)


### Features

* Add wrapper for GATK DepthOfCoverage ([#494](https://www.github.com/snakemake/snakemake-wrappers/issues/494)) ([636060a](https://www.github.com/snakemake/snakemake-wrappers/commit/636060ac7538c5c0bc2c045e19aecd67f089f0ba))

## [1.13.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.12.2...v1.13.0) (2022-09-17)


### Features

* Add wrapper for bwa-meme ([#555](https://www.github.com/snakemake/snakemake-wrappers/issues/555)) ([92579c4](https://www.github.com/snakemake/snakemake-wrappers/commit/92579c400fc88999774b762254fac75b13a9fdb1))


### Performance Improvements

* bwa mem2 version update and use wrapper utils ([#553](https://www.github.com/snakemake/snakemake-wrappers/issues/553)) ([356ee4d](https://www.github.com/snakemake/snakemake-wrappers/commit/356ee4d0f4fdf35a270185ad671eb88d288be7ad))

### [1.12.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.12.1...v1.12.2) (2022-09-02)


### Performance Improvements

* update to datavzrd wrapper to datavzrd 2.0 ([#551](https://www.github.com/snakemake/snakemake-wrappers/issues/551)) ([a0bb674](https://www.github.com/snakemake/snakemake-wrappers/commit/a0bb6748031307a63e919cd7f923dd4ef61c40a9))

### [1.12.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.12.0...v1.12.1) (2022-09-01)


### Bug Fixes

* remove debug code from vep wrapper ([c58334b](https://www.github.com/snakemake/snakemake-wrappers/commit/c58334b5e0bb23713e363fcaf04988103ffcce98))
* tabix wrapper names ([bf7627e](https://www.github.com/snakemake/snakemake-wrappers/commit/bf7627eb8ab6ccc93edc182496a9bf1e664213dd))

## [1.12.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.11.0...v1.12.0) (2022-08-30)


### Features

* genefuse wrapper ([#493](https://www.github.com/snakemake/snakemake-wrappers/issues/493)) ([9bcf282](https://www.github.com/snakemake/snakemake-wrappers/commit/9bcf282a25fb1f27ffebc8114ed1b15e3ee412c0))


### Bug Fixes

* upgrade vep wrappers to latest version, fixing issues with strict channel priorities. ([#547](https://www.github.com/snakemake/snakemake-wrappers/issues/547)) ([c3b46e5](https://www.github.com/snakemake/snakemake-wrappers/commit/c3b46e5b71429e08c5e6066a3437b543c0c6b35e))

## [1.11.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.10.0...v1.11.0) (2022-08-29)


### Features

* Wrapper and meta-wrapper for rbt consensus reads ([#544](https://www.github.com/snakemake/snakemake-wrappers/issues/544)) ([6736211](https://www.github.com/snakemake/snakemake-wrappers/commit/6736211fdc5f7f6ea530ba847ff19391c33cb91c))

## [1.10.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.9.0...v1.10.0) (2022-08-21)


### Features

* Delly automated conversion of output file ([#468](https://www.github.com/snakemake/snakemake-wrappers/issues/468)) ([67c11a3](https://www.github.com/snakemake/snakemake-wrappers/commit/67c11a33842e199d34d8ed1639696d7213019dbc))
* support branches (e.g. plants) in ensembl wrappers for sequence, annotation, and variation download ([#546](https://www.github.com/snakemake/snakemake-wrappers/issues/546)) ([94d7f8e](https://www.github.com/snakemake/snakemake-wrappers/commit/94d7f8eeded9e755d86484c6d2b33f7468e6e298))

## [1.9.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.8.0...v1.9.0) (2022-08-18)


### Features

* add datavzrd wrapper ([#535](https://www.github.com/snakemake/snakemake-wrappers/issues/535)) ([8c05064](https://www.github.com/snakemake/snakemake-wrappers/commit/8c050644d3d2c876a4a428c28fb7c4fc17f8a18e))
* BWA mem2 index - remove prefix parameter and determine prefix from output ([#515](https://www.github.com/snakemake/snakemake-wrappers/issues/515)) ([ab8d4ad](https://www.github.com/snakemake/snakemake-wrappers/commit/ab8d4adba91f05fec04d9c6b946b77bba78c03e7))


### Performance Improvements

* update bcftools norm versions ([#543](https://www.github.com/snakemake/snakemake-wrappers/issues/543)) ([5313db6](https://www.github.com/snakemake/snakemake-wrappers/commit/5313db611d498c9f8b9e4063d5d7a95b9da769cb))

## [1.8.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.7.2...v1.8.0) (2022-08-16)


### Features

* add "qualimap bamqc" wrapper ([#533](https://www.github.com/snakemake/snakemake-wrappers/issues/533)) ([3af38c8](https://www.github.com/snakemake/snakemake-wrappers/commit/3af38c88a8413d2bcc5dba3649d0e7cf82379a2c))
* added bamtobed wrapper ([#531](https://www.github.com/snakemake/snakemake-wrappers/issues/531)) ([0486745](https://www.github.com/snakemake/snakemake-wrappers/commit/048674518b6108b93708be0ce30521d59c62b149))
* added Bellerophon wrapper ([#529](https://www.github.com/snakemake/snakemake-wrappers/issues/529)) ([888f651](https://www.github.com/snakemake/snakemake-wrappers/commit/888f651627fd68b479eeeabb00b21182702fb285))
* added gfatools wrapper ([#512](https://www.github.com/snakemake/snakemake-wrappers/issues/512)) ([2c6b897](https://www.github.com/snakemake/snakemake-wrappers/commit/2c6b897fa04b8df256af99ae59ee09376cbab2da))
* added purge_dups wrapper ([#528](https://www.github.com/snakemake/snakemake-wrappers/issues/528)) ([17d87e2](https://www.github.com/snakemake/snakemake-wrappers/commit/17d87e29c426266f45b973d6940b781f452332b4))
* added Salsa2 wrapper ([#532](https://www.github.com/snakemake/snakemake-wrappers/issues/532)) ([8cb4137](https://www.github.com/snakemake/snakemake-wrappers/commit/8cb41378aba9b8fcc3d88a9881af0a5b4bdee832))
* added wrapper-utils, and tempdirs ([#467](https://www.github.com/snakemake/snakemake-wrappers/issues/467)) ([48c49a9](https://www.github.com/snakemake/snakemake-wrappers/commit/48c49a97d20653b2ed3fecfee6c7bbbc3cf45127))
* added wrappers for pretext map, snapshot and graph ([#530](https://www.github.com/snakemake/snakemake-wrappers/issues/530)) ([2eb3fdd](https://www.github.com/snakemake/snakemake-wrappers/commit/2eb3fdd267cfa2d59a9bb8f70c9afd6149bc8c98))
* BUSCO auto lineage mode, tempdir, updated version ([#526](https://www.github.com/snakemake/snakemake-wrappers/issues/526)) ([67cf8e1](https://www.github.com/snakemake/snakemake-wrappers/commit/67cf8e13c1ea6dda362c45e934122a25e2c470f6))
* Bustools count ([#511](https://www.github.com/snakemake/snakemake-wrappers/issues/511)) ([bb050e4](https://www.github.com/snakemake/snakemake-wrappers/commit/bb050e4683185cb6ff5bcc9091f99cf058f82f53))
* Bustools sort ([#513](https://www.github.com/snakemake/snakemake-wrappers/issues/513)) ([1415748](https://www.github.com/snakemake/snakemake-wrappers/commit/1415748aebb18649b1c6a83d04ea0115563e0494))
* Bustools text ([#509](https://www.github.com/snakemake/snakemake-wrappers/issues/509)) ([00f60b7](https://www.github.com/snakemake/snakemake-wrappers/commit/00f60b7f0d730c5fe1870d854422314f03af8c0a))
* cooltools wrappers ([#519](https://www.github.com/snakemake/snakemake-wrappers/issues/519)) ([d28de15](https://www.github.com/snakemake/snakemake-wrappers/commit/d28de15c1f8575ff4934e5cf98a0a03c5fa771ed))
* fixed minimap2 bioconda strict channels, updated version, and added test ([#527](https://www.github.com/snakemake/snakemake-wrappers/issues/527)) ([8f95ddb](https://www.github.com/snakemake/snakemake-wrappers/commit/8f95ddb3e1a55c2edd1a70cfd42b1fc526bd6171))
* GATK FilterMutectCall enhancement ([#521](https://www.github.com/snakemake/snakemake-wrappers/issues/521)) ([eea67d4](https://www.github.com/snakemake/snakemake-wrappers/commit/eea67d404c72da087af4c3b0b9d82c8174dd73fb))
* GATK Getpileupsummaries ([#517](https://www.github.com/snakemake/snakemake-wrappers/issues/517)) ([4281982](https://www.github.com/snakemake/snakemake-wrappers/commit/42819826781470566bd6e0c097c525020e10c407))
* gatk Learnreadorientationmodel ([#523](https://www.github.com/snakemake/snakemake-wrappers/issues/523)) ([cd68aa5](https://www.github.com/snakemake/snakemake-wrappers/commit/cd68aa57e7d988a488bd0599fd6ec102effe81c5))
* hifiasm wrapper ([#510](https://www.github.com/snakemake/snakemake-wrappers/issues/510)) ([5360346](https://www.github.com/snakemake/snakemake-wrappers/commit/53603466e1ed00a098a6289bfbf7460a601a261a))
* Meryl wrapper ([#506](https://www.github.com/snakemake/snakemake-wrappers/issues/506)) ([f5ddac1](https://www.github.com/snakemake/snakemake-wrappers/commit/f5ddac16ae28549d4bb44a1e18cc8c7a6d423799))
* output aln is saved from stdout, to reduce I/O ([#502](https://www.github.com/snakemake/snakemake-wrappers/issues/502)) ([6695486](https://www.github.com/snakemake/snakemake-wrappers/commit/6695486bbc2ba67bc0f9ecb05086d8065df85ec9))
* Quast wrapper ([#525](https://www.github.com/snakemake/snakemake-wrappers/issues/525)) ([754dfc1](https://www.github.com/snakemake/snakemake-wrappers/commit/754dfc1019a7eb52642e3f3e91c3df9da8df3495))


### Bug Fixes

* create tabix index sub-wrapper ([#501](https://www.github.com/snakemake/snakemake-wrappers/issues/501)) ([6c47164](https://www.github.com/snakemake/snakemake-wrappers/commit/6c471647c090a60757d111b781fd88e9e010715a))


### Performance Improvements

* updated cutadapt version, formatted files, and improved docs. ([#505](https://www.github.com/snakemake/snakemake-wrappers/issues/505)) ([3a20eb7](https://www.github.com/snakemake/snakemake-wrappers/commit/3a20eb75dc8ac7449b1a58948bb3e1327c2754a8))

### [1.7.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.7.1...v1.7.2) (2022-08-15)


### Bug Fixes

* give conda-forge highest priority to ensure proper semantic under strict channel priorities ([#508](https://www.github.com/snakemake/snakemake-wrappers/issues/508)) ([6976c9a](https://www.github.com/snakemake/snakemake-wrappers/commit/6976c9abe83341694219689c73063edde55e6424))

### [1.7.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.7.0...v1.7.1) (2022-07-19)


### Bug Fixes

* better error handling for ensembl sequence download ([#524](https://www.github.com/snakemake/snakemake-wrappers/issues/524)) ([c289800](https://www.github.com/snakemake/snakemake-wrappers/commit/c28980096fcedef29b67c2e4bb383ff590e46503))
* give conda-forge highest priority to ensure proper semantic under strict channel priorities ([ce78f79](https://www.github.com/snakemake/snakemake-wrappers/commit/ce78f79fb3fd5740e414b93f9f62cee72f7dcf38))
* issue when picard does not create output files ([#496](https://www.github.com/snakemake/snakemake-wrappers/issues/496)) ([aceab7e](https://www.github.com/snakemake/snakemake-wrappers/commit/aceab7efe9039afe4178fc3a346937cb5ea9806b))
* remove misleading kmer size parameter for kallisto index ([#518](https://www.github.com/snakemake/snakemake-wrappers/issues/518)) ([309b376](https://www.github.com/snakemake/snakemake-wrappers/commit/309b376bff59e545b6ba7c114bc1262a48128b3b))
* use strict channel priorities ([#503](https://www.github.com/snakemake/snakemake-wrappers/issues/503)) ([6419dbf](https://www.github.com/snakemake/snakemake-wrappers/commit/6419dbf67772319c8b848eb06478abf07d5f3c28))

## [1.7.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.6.0...v1.7.0) (2022-06-14)


### Features

* Salmon decoy-aware gentrome ([#490](https://www.github.com/snakemake/snakemake-wrappers/issues/490)) ([5bb3eab](https://www.github.com/snakemake/snakemake-wrappers/commit/5bb3eab04e0b2dcfac624207c3810d036f22339b))

## [1.6.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.5.0...v1.6.0) (2022-05-23)


### Features

* make it possible to set input as files or dirs to multiqc ([#488](https://www.github.com/snakemake/snakemake-wrappers/issues/488)) ([32fd0e0](https://www.github.com/snakemake/snakemake-wrappers/commit/32fd0e0818379ada75f5a6854d6b4000cf3d44b5))
* Mashmap ([#485](https://www.github.com/snakemake/snakemake-wrappers/issues/485)) ([c05006d](https://www.github.com/snakemake/snakemake-wrappers/commit/c05006d9fb624efcbd23bfe37f7d288568290a25))
* Salmon update ([#482](https://www.github.com/snakemake/snakemake-wrappers/issues/482)) ([3684276](https://www.github.com/snakemake/snakemake-wrappers/commit/36842760dddc71e321c93cb11d4c39840cdd2a84))

## [1.5.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.4.0...v1.5.0) (2022-05-13)


### Features

* samtools stat bed params ([#418](https://www.github.com/snakemake/snakemake-wrappers/issues/418)) ([28fa3a8](https://www.github.com/snakemake/snakemake-wrappers/commit/28fa3a806f1e2d75d1a3325b5ca8d84b87b5db48))
* support cram output in picardtools markduplicates ([#486](https://www.github.com/snakemake/snakemake-wrappers/issues/486)) ([218fd39](https://www.github.com/snakemake/snakemake-wrappers/commit/218fd396ea51f22fb3a059cf5eac2edebd3b5eb6))

## [1.4.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.3.2...v1.4.0) (2022-05-05)


### Features

* added ref as an optional input file ([#473](https://www.github.com/snakemake/snakemake-wrappers/issues/473)) ([dd8c066](https://www.github.com/snakemake/snakemake-wrappers/commit/dd8c0662a39850b62b5758f7ecf291a5337c86b8))
* Added specific param for strandness ([#474](https://www.github.com/snakemake/snakemake-wrappers/issues/474)) ([12b7978](https://www.github.com/snakemake/snakemake-wrappers/commit/12b7978884650f748fd414e94cfa597baa52aa10))
* added support for gzip output files in ensembl annotation download wrapper ([#475](https://www.github.com/snakemake/snakemake-wrappers/issues/475)) ([42696c2](https://www.github.com/snakemake/snakemake-wrappers/commit/42696c2c6dd270c32467b6ee49997978131d92d3))
* convert gtf to gene pred output ([#477](https://www.github.com/snakemake/snakemake-wrappers/issues/477)) ([4672e5b](https://www.github.com/snakemake/snakemake-wrappers/commit/4672e5b9dacd9cde34614b6df1254308944262c6))
* DragMap wrapper ([#472](https://www.github.com/snakemake/snakemake-wrappers/issues/472)) ([6f54512](https://www.github.com/snakemake/snakemake-wrappers/commit/6f54512814244c2c4962dd1b0b77ce92eab894fa))
* make it possible to set output type, vcf or gvcf. ([#476](https://www.github.com/snakemake/snakemake-wrappers/issues/476)) ([e62744d](https://www.github.com/snakemake/snakemake-wrappers/commit/e62744de125df3cd1958712f3dc00e428c815c2b))


### Bug Fixes

* fixed issue when several output files are specified with gatk splitncigarreads wrapper ([#471](https://www.github.com/snakemake/snakemake-wrappers/issues/471)) ([353bf0a](https://www.github.com/snakemake/snakemake-wrappers/commit/353bf0af238603ea11f9554c6454280bf36630b6))
* restrict bwa wrappers' picard installation to picard-slim (e.g. removes r-base dependency) ([#484](https://www.github.com/snakemake/snakemake-wrappers/issues/484)) ([bd3cdbc](https://www.github.com/snakemake/snakemake-wrappers/commit/bd3cdbc0343585703e7af6d36f2433c5cb64a96b))

### [1.3.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.3.1...v1.3.2) (2022-03-28)


### Bug Fixes

* fixed some known bugs, added docs, and reformat ([#469](https://www.github.com/snakemake/snakemake-wrappers/issues/469)) ([58247e3](https://www.github.com/snakemake/snakemake-wrappers/commit/58247e3694222ede9a450540bae82557feeb5ea6))

### [1.3.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.3.0...v1.3.1) (2022-03-17)


### Bug Fixes

* Nextflow profile ([#456](https://www.github.com/snakemake/snakemake-wrappers/issues/456)) ([bd9af55](https://www.github.com/snakemake/snakemake-wrappers/commit/bd9af55375d6b31b6edeaeac5504209e31914919))

## [1.3.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.2.1...v1.3.0) (2022-03-16)


### Features

* added GATK variantAnnotator wrapper ([#462](https://www.github.com/snakemake/snakemake-wrappers/issues/462)) ([3ace5fa](https://www.github.com/snakemake/snakemake-wrappers/commit/3ace5faa11aa412864784e4d541c264f8b7a4deb))

### [1.2.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.2.0...v1.2.1) (2022-03-11)


### Bug Fixes

* bcftools filter cannot run with mem options and this will prevent mem-max to be set. ([#464](https://www.github.com/snakemake/snakemake-wrappers/issues/464)) ([d7a0de4](https://www.github.com/snakemake/snakemake-wrappers/commit/d7a0de4a2b0cd36d9b141f9e9b717f98a4979ea6))
* issue 339 ([#461](https://www.github.com/snakemake/snakemake-wrappers/issues/461)) ([6734675](https://www.github.com/snakemake/snakemake-wrappers/commit/6734675cfbc7f5c4df246dca9063f84bb4346ace))
* update multiqc version to 1.12 ([#460](https://www.github.com/snakemake/snakemake-wrappers/issues/460)) ([330359d](https://www.github.com/snakemake/snakemake-wrappers/commit/330359d40a98f8efedc6e55fbd963d02a1e14fad))

## [1.2.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.1.0...v1.2.0) (2022-02-21)


### Features

* added samtools wrapper utils ([#454](https://www.github.com/snakemake/snakemake-wrappers/issues/454)) ([23c28bf](https://www.github.com/snakemake/snakemake-wrappers/commit/23c28bf0ca2cf00109e604989386fd9d372f1718))
* added STAR temp dir ([#453](https://www.github.com/snakemake/snakemake-wrappers/issues/453)) ([86a6c11](https://www.github.com/snakemake/snakemake-wrappers/commit/86a6c1109e7469972fe0aed50bab33a3b2ba6e0a))
* added temp dir to featurecounts ([#455](https://www.github.com/snakemake/snakemake-wrappers/issues/455)) ([d93866e](https://www.github.com/snakemake/snakemake-wrappers/commit/d93866e0b2abbe81f0cd544698f554b1a67faff9))
* added tmpdir to all GATK wrappers, plus some doc changes ([#449](https://www.github.com/snakemake/snakemake-wrappers/issues/449)) ([c17266b](https://www.github.com/snakemake/snakemake-wrappers/commit/c17266b95f58b15e3b9ded712bf203e398f0f2ea))
* explicitly specify bwa index in bwa samxe ([#448](https://www.github.com/snakemake/snakemake-wrappers/issues/448)) ([ef5b36a](https://www.github.com/snakemake/snakemake-wrappers/commit/ef5b36a31a2301d9833e661fd612dee49675cab7))

## [1.1.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.0.0...v1.1.0) (2022-02-07)


### Features

* automatically set temp dir tempfile ([#446](https://www.github.com/snakemake/snakemake-wrappers/issues/446)) ([5b0d26a](https://www.github.com/snakemake/snakemake-wrappers/commit/5b0d26afcb41eda7a0fbd883b82246352a33e7a7))
* updated delly wrapper to version 0.9.1.


### Bug Fixes

* added missing dependencies and improved docs ([#450](https://www.github.com/snakemake/snakemake-wrappers/issues/450)) ([e99f2a1](https://www.github.com/snakemake/snakemake-wrappers/commit/e99f2a1aab0db4f08503340bb863c18a6b15596f))

## [1.0.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v0.87.0...v1.0.0) (2022-01-26)


### ⚠ BREAKING CHANGES

* added tempdir, updated version and metadata to all picard wrappers (#443)

### Features

* added tempdir, updated version and metadata to all picard wrappers ([#443](https://www.github.com/snakemake/snakemake-wrappers/issues/443)) ([55e672a](https://www.github.com/snakemake/snakemake-wrappers/commit/55e672a893d135d439a972c12a0811ec860ffb78))

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
