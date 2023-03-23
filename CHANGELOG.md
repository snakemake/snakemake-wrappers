# Changelog

## [1.25.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.24.0...v1.25.0) (2023-03-23)


### Features

* added several Seqkit wrappers ([#1128](https://www.github.com/snakemake/snakemake-wrappers/issues/1128)) ([9c4e667](https://www.github.com/snakemake/snakemake-wrappers/commit/9c4e66705de7f0db6c4cedae8b06359bacc9169a))
* added wrapper for loglog ([#1154](https://www.github.com/snakemake/snakemake-wrappers/issues/1154)) ([08917f9](https://www.github.com/snakemake/snakemake-wrappers/commit/08917f991e60b19cac03b9b9cec82fdaf10891b9))
* added wrapper for tadpole ([#1152](https://www.github.com/snakemake/snakemake-wrappers/issues/1152)) ([cb1372b](https://www.github.com/snakemake/snakemake-wrappers/commit/cb1372ba61ea3f92050b974e0dfa61e42b496806))
* Merqury ([#540](https://www.github.com/snakemake/snakemake-wrappers/issues/540)) ([f7914c4](https://www.github.com/snakemake/snakemake-wrappers/commit/f7914c4025fcbcea124765732b4241cfe233f379))
* Mutect2 additional parameters ([#516](https://www.github.com/snakemake/snakemake-wrappers/issues/516)) ([f2b70ca](https://www.github.com/snakemake/snakemake-wrappers/commit/f2b70ca7371d2bb7c031930d047d1e18f9f0610f))


### Bug Fixes

* use new java memory overhead utils ([#1150](https://www.github.com/snakemake/snakemake-wrappers/issues/1150)) ([d15d5f5](https://www.github.com/snakemake/snakemake-wrappers/commit/d15d5f5dda23a60aa6c570c9b5da4d5a855cadf5))


### Performance Improvements

* autobump bio/bcftools/filter ([#646](https://www.github.com/snakemake/snakemake-wrappers/issues/646)) ([b7b98fd](https://www.github.com/snakemake/snakemake-wrappers/commit/b7b98fd9cd9ae819e116aa81c6d082585a77b41d))
* autobump bio/bismark/deduplicate_bismark ([#1141](https://www.github.com/snakemake/snakemake-wrappers/issues/1141)) ([45cd1a6](https://www.github.com/snakemake/snakemake-wrappers/commit/45cd1a635a00d48dbbfbf591059364e0d6d09864))
* autobump bio/cooltools/dots ([#702](https://www.github.com/snakemake/snakemake-wrappers/issues/702)) ([7ac6569](https://www.github.com/snakemake/snakemake-wrappers/commit/7ac656961dff08341e3d448932dda37c19f7d65d))
* autobump bio/fgbio/collectduplexseqmetrics ([#1100](https://www.github.com/snakemake/snakemake-wrappers/issues/1100)) ([ae2a295](https://www.github.com/snakemake/snakemake-wrappers/commit/ae2a295303b987e9e1fb303a689bec6d0cbb4aa1))
* autobump bio/gatk/markduplicatesspark ([#1142](https://www.github.com/snakemake/snakemake-wrappers/issues/1142)) ([190dd18](https://www.github.com/snakemake/snakemake-wrappers/commit/190dd18d6a29cdb1fefdfe98f7d25a5d9c4d00d1))
* autobump bio/gridss/preprocess ([#800](https://www.github.com/snakemake/snakemake-wrappers/issues/800)) ([71463ad](https://www.github.com/snakemake/snakemake-wrappers/commit/71463adf79b2a12f3360e1f80f8452f3803c9315))
* autobump bio/gridss/setupreference ([#848](https://www.github.com/snakemake/snakemake-wrappers/issues/848)) ([c2f9766](https://www.github.com/snakemake/snakemake-wrappers/commit/c2f976626319fde811e4a4043f9307f7fb7e6758))
* autobump bio/hisat2/align ([#1079](https://www.github.com/snakemake/snakemake-wrappers/issues/1079)) ([dea181a](https://www.github.com/snakemake/snakemake-wrappers/commit/dea181a03196c4a6f8612651478ee07bbee16467))
* autobump bio/liftoff ([#953](https://www.github.com/snakemake/snakemake-wrappers/issues/953)) ([0928808](https://www.github.com/snakemake/snakemake-wrappers/commit/0928808b812b2f4c24c3b747e4eee42cab534453))
* autobump bio/lofreq/call ([#1120](https://www.github.com/snakemake/snakemake-wrappers/issues/1120)) ([a327d86](https://www.github.com/snakemake/snakemake-wrappers/commit/a327d860f3db5154007e3c527b584c5eadc9050f))
* autobump bio/muscle ([#612](https://www.github.com/snakemake/snakemake-wrappers/issues/612)) ([659d106](https://www.github.com/snakemake/snakemake-wrappers/commit/659d10646b41c01b009a55b1f15503a7965bce6a))
* autobump bio/snpeff/annotate ([#1038](https://www.github.com/snakemake/snakemake-wrappers/issues/1038)) ([5628ccd](https://www.github.com/snakemake/snakemake-wrappers/commit/5628ccdc4156f17ffa1b2a84bb255e81036b86ea))
* autobump bio/subread/featurecounts ([#1044](https://www.github.com/snakemake/snakemake-wrappers/issues/1044)) ([b7d7ed4](https://www.github.com/snakemake/snakemake-wrappers/commit/b7d7ed4d6b7c58a774a8dd9c04d8a5880d3fc991))
* autobump bio/trinity ([#634](https://www.github.com/snakemake/snakemake-wrappers/issues/634)) ([d084304](https://www.github.com/snakemake/snakemake-wrappers/commit/d084304a9afff1c460465d4db6bfa4898fa26e8e))
* autobump bio/vep/cache ([#1132](https://www.github.com/snakemake/snakemake-wrappers/issues/1132)) ([d8c3faa](https://www.github.com/snakemake/snakemake-wrappers/commit/d8c3faac3f30b001534d104bf26f916c04787d71))

## [1.24.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.5...v1.24.0) (2023-03-17)


### Features

* allowed strelka germline using multiple bam ([#1092](https://www.github.com/snakemake/snakemake-wrappers/issues/1092)) ([422e849](https://www.github.com/snakemake/snakemake-wrappers/commit/422e849ec1311ada235048c4ebc7d40ffdb4f3fc))
* BWA-MEME Version 1.0.6 update ([#1123](https://www.github.com/snakemake/snakemake-wrappers/issues/1123)) ([7422b0b](https://www.github.com/snakemake/snakemake-wrappers/commit/7422b0b7dfcebab2a09006073b354e37f93bddec))
* update arriba to 2.4.0 ([#1148](https://www.github.com/snakemake/snakemake-wrappers/issues/1148)) ([eda64d8](https://www.github.com/snakemake/snakemake-wrappers/commit/eda64d8f37b22cdc0cfdf59a87b3b46f643aee5b))


### Bug Fixes

* Add tests to Sickle and fixed typo ([#1126](https://www.github.com/snakemake/snakemake-wrappers/issues/1126)) ([02518ff](https://www.github.com/snakemake/snakemake-wrappers/commit/02518ff9c5243dd0ceb4668bf1c25d4d7f6bebe9))


### Performance Improvements

* autobump bio/bgzip ([#1140](https://www.github.com/snakemake/snakemake-wrappers/issues/1140)) ([f0e1aa4](https://www.github.com/snakemake/snakemake-wrappers/commit/f0e1aa427bd7bc8ff23b6b09faa80288c905e502))
* autobump bio/bismark/bam2nuc ([#1099](https://www.github.com/snakemake/snakemake-wrappers/issues/1099)) ([fd24a3d](https://www.github.com/snakemake/snakemake-wrappers/commit/fd24a3d9b3b438ed35fbf314c112c10d9692e10f))
* autobump bio/bismark/bismark2summary ([#1105](https://www.github.com/snakemake/snakemake-wrappers/issues/1105)) ([e8ec077](https://www.github.com/snakemake/snakemake-wrappers/commit/e8ec077efa43855012f19a1a355d4eb6c7c5c8db))
* autobump bio/bustools/text ([#1107](https://www.github.com/snakemake/snakemake-wrappers/issues/1107)) ([c280d8b](https://www.github.com/snakemake/snakemake-wrappers/commit/c280d8baaf7878f2f2636cbf5f0a9aee9828ec5e))
* autobump bio/bwa-mem2/mem ([#1130](https://www.github.com/snakemake/snakemake-wrappers/issues/1130)) ([25a44a5](https://www.github.com/snakemake/snakemake-wrappers/commit/25a44a5f8c5f1b8947d477d99b01c2a664f3354c))
* autobump bio/bwa-memx/mem ([#1108](https://www.github.com/snakemake/snakemake-wrappers/issues/1108)) ([75964c1](https://www.github.com/snakemake/snakemake-wrappers/commit/75964c1741bcbc76c8e40aeb431b08a91a46554c))
* autobump bio/bwa-memx/mem ([#1145](https://www.github.com/snakemake/snakemake-wrappers/issues/1145)) ([2bf0fee](https://www.github.com/snakemake/snakemake-wrappers/commit/2bf0feeb1ab12070ecf35dbedeeb19a0d6f09e4e))
* autobump bio/bwa/samse ([#1119](https://www.github.com/snakemake/snakemake-wrappers/issues/1119)) ([c591284](https://www.github.com/snakemake/snakemake-wrappers/commit/c591284e40d856aa73f0d9382e729bc924c44443))
* autobump bio/cooltools/expected_cis ([#1098](https://www.github.com/snakemake/snakemake-wrappers/issues/1098)) ([a642717](https://www.github.com/snakemake/snakemake-wrappers/commit/a642717900174d3e95173924941622901a0042e0))
* autobump bio/cooltools/saddle ([#1138](https://www.github.com/snakemake/snakemake-wrappers/issues/1138)) ([0108e6d](https://www.github.com/snakemake/snakemake-wrappers/commit/0108e6d65d11475fa8eadb25d70592c92b414ed1))
* autobump bio/cutadapt/pe ([#1006](https://www.github.com/snakemake/snakemake-wrappers/issues/1006)) ([ab85e5d](https://www.github.com/snakemake/snakemake-wrappers/commit/ab85e5dbba4962a8668e7646438d7e604ff7ff81))
* autobump bio/diamond/blastp ([#1114](https://www.github.com/snakemake/snakemake-wrappers/issues/1114)) ([0aeb9b2](https://www.github.com/snakemake/snakemake-wrappers/commit/0aeb9b2fc1f4c92ff20636e094ae602682acd666))
* autobump bio/diamond/blastx ([#1122](https://www.github.com/snakemake/snakemake-wrappers/issues/1122)) ([1638662](https://www.github.com/snakemake/snakemake-wrappers/commit/1638662ac5d4534843a1f6c4727efd2506167faf))
* autobump bio/diamond/makedb ([#1111](https://www.github.com/snakemake/snakemake-wrappers/issues/1111)) ([b17ff0a](https://www.github.com/snakemake/snakemake-wrappers/commit/b17ff0a678bd78b55823b33c55356b785620b146))
* autobump bio/fastqc ([#1147](https://www.github.com/snakemake/snakemake-wrappers/issues/1147)) ([e0efb68](https://www.github.com/snakemake/snakemake-wrappers/commit/e0efb687dc20fe38cba6d78ada4233c06c934954))
* autobump bio/fgbio/callmolecularconsensusreads ([#1101](https://www.github.com/snakemake/snakemake-wrappers/issues/1101)) ([2a0a77d](https://www.github.com/snakemake/snakemake-wrappers/commit/2a0a77d4ab0f4cab5c2634d10a821da422c3b373))
* autobump bio/genomepy ([#1137](https://www.github.com/snakemake/snakemake-wrappers/issues/1137)) ([ab85927](https://www.github.com/snakemake/snakemake-wrappers/commit/ab85927603ccec3b55c52cf0ee8b27bdf4be1959))
* autobump bio/kallisto/index ([#1005](https://www.github.com/snakemake/snakemake-wrappers/issues/1005)) ([17613e6](https://www.github.com/snakemake/snakemake-wrappers/commit/17613e6d881c7cd62cd785ba89bab78efaf26937))
* autobump bio/last/lastal ([#1143](https://www.github.com/snakemake/snakemake-wrappers/issues/1143)) ([c0443b1](https://www.github.com/snakemake/snakemake-wrappers/commit/c0443b1770913cdd7268cacb69e0abd3f7773500))
* autobump bio/last/lastdb ([#1110](https://www.github.com/snakemake/snakemake-wrappers/issues/1110)) ([905a6e6](https://www.github.com/snakemake/snakemake-wrappers/commit/905a6e6cbb49345464318d34abe5d217fe20dddb))
* autobump bio/last/lastdb ([#1121](https://www.github.com/snakemake/snakemake-wrappers/issues/1121)) ([394942a](https://www.github.com/snakemake/snakemake-wrappers/commit/394942ad9a48461f882fa2c430c98cfcc0cb962a))
* autobump bio/mlst ([#1117](https://www.github.com/snakemake/snakemake-wrappers/issues/1117)) ([c97bae1](https://www.github.com/snakemake/snakemake-wrappers/commit/c97bae18068a67fc0af706e285e2950c419c5456))
* autobump bio/multiqc ([#1104](https://www.github.com/snakemake/snakemake-wrappers/issues/1104)) ([2a4894e](https://www.github.com/snakemake/snakemake-wrappers/commit/2a4894e906a84b03fdf9ad1f8fb4f8ccabdf0e66))
* autobump bio/picard/addorreplacereadgroups ([#1115](https://www.github.com/snakemake/snakemake-wrappers/issues/1115)) ([7748621](https://www.github.com/snakemake/snakemake-wrappers/commit/77486216285f74c2171c0276fe4141aee9b63be1))
* autobump bio/picard/collectalignmentsummarymetrics ([#1131](https://www.github.com/snakemake/snakemake-wrappers/issues/1131)) ([a9af1d2](https://www.github.com/snakemake/snakemake-wrappers/commit/a9af1d26de80bc12eabfcb337e4ad082609a3c6f))
* autobump bio/picard/collectgcbiasmetrics ([#1096](https://www.github.com/snakemake/snakemake-wrappers/issues/1096)) ([c6896b8](https://www.github.com/snakemake/snakemake-wrappers/commit/c6896b80098282f1bada24c6496c74bb44e0ee15))
* autobump bio/picard/collectinsertsizemetrics ([#1097](https://www.github.com/snakemake/snakemake-wrappers/issues/1097)) ([cb3f91d](https://www.github.com/snakemake/snakemake-wrappers/commit/cb3f91de62979df73c627a677c5e1fd05413d74b))
* autobump bio/picard/collectrnaseqmetrics ([#1103](https://www.github.com/snakemake/snakemake-wrappers/issues/1103)) ([6f53085](https://www.github.com/snakemake/snakemake-wrappers/commit/6f53085bae1722e9e9fcc12b842efa77a04f5671))
* autobump bio/picard/collecttargetedpcrmetrics ([#1102](https://www.github.com/snakemake/snakemake-wrappers/issues/1102)) ([b8615ed](https://www.github.com/snakemake/snakemake-wrappers/commit/b8615ed8f04e45ba0edf11d841ac5c390f2542ab))
* autobump bio/picard/markduplicateswithmatecigar ([#1135](https://www.github.com/snakemake/snakemake-wrappers/issues/1135)) ([2f6a0de](https://www.github.com/snakemake/snakemake-wrappers/commit/2f6a0ded591f4070c28b9cff19328b36a95472d6))
* autobump bio/picard/mergesamfiles ([#1109](https://www.github.com/snakemake/snakemake-wrappers/issues/1109)) ([155484c](https://www.github.com/snakemake/snakemake-wrappers/commit/155484c7ab6d093aaba47d72d1f07dfc21fc312d))
* autobump bio/picard/mergevcfs ([#1095](https://www.github.com/snakemake/snakemake-wrappers/issues/1095)) ([7abf5cc](https://www.github.com/snakemake/snakemake-wrappers/commit/7abf5cce0f797071a2c2bc7984bb650dee1c60ed))
* autobump bio/picard/samtofastq ([#1146](https://www.github.com/snakemake/snakemake-wrappers/issues/1146)) ([a670bc5](https://www.github.com/snakemake/snakemake-wrappers/commit/a670bc5f383bd0026b5e4483f05f770382317db8))
* autobump bio/reference/ensembl-variation ([#1144](https://www.github.com/snakemake/snakemake-wrappers/issues/1144)) ([0a9cdfc](https://www.github.com/snakemake/snakemake-wrappers/commit/0a9cdfc0344a2f1d69a53373603a8de1b4b3da37))
* autobump bio/salmon/index ([#1139](https://www.github.com/snakemake/snakemake-wrappers/issues/1139)) ([fdd9619](https://www.github.com/snakemake/snakemake-wrappers/commit/fdd9619e90aa1bb16d97b545ab3c4ee2c8733c45))
* autobump bio/sambamba/sort ([#1106](https://www.github.com/snakemake/snakemake-wrappers/issues/1106)) ([3f06b9f](https://www.github.com/snakemake/snakemake-wrappers/commit/3f06b9f9590b98fe49544b279ce0194dbb1ee389))
* autobump bio/tabix/query ([#1134](https://www.github.com/snakemake/snakemake-wrappers/issues/1134)) ([c3249e0](https://www.github.com/snakemake/snakemake-wrappers/commit/c3249e0b7146ec7913dd9f80a1daaca93978ff21))
* autobump bio/trim_galore/pe ([#1136](https://www.github.com/snakemake/snakemake-wrappers/issues/1136)) ([b10b38f](https://www.github.com/snakemake/snakemake-wrappers/commit/b10b38f98c2f1d9850060e7aa7fdb68db7158bff))
* autobump bio/ucsc/gtfToGenePred ([#1093](https://www.github.com/snakemake/snakemake-wrappers/issues/1093)) ([d145388](https://www.github.com/snakemake/snakemake-wrappers/commit/d1453880491a8f51223d9c3ec185f420d20c04ab))
* autobump bio/ucsc/twoBitInfo ([#1112](https://www.github.com/snakemake/snakemake-wrappers/issues/1112)) ([407f8b3](https://www.github.com/snakemake/snakemake-wrappers/commit/407f8b36ef7d6e154dcf49ce4a428dcdf9c83cf0))
* autobump bio/umis/bamtag ([#1133](https://www.github.com/snakemake/snakemake-wrappers/issues/1133)) ([d58e25c](https://www.github.com/snakemake/snakemake-wrappers/commit/d58e25c77dd67d63a82d65e75aad2607d3d0bc97))
* autobump bio/vep/annotate ([#1116](https://www.github.com/snakemake/snakemake-wrappers/issues/1116)) ([20b9a8d](https://www.github.com/snakemake/snakemake-wrappers/commit/20b9a8de066b73e1500185d2a66166ee8dd69461))
* autobump bio/vg/construct ([#1118](https://www.github.com/snakemake/snakemake-wrappers/issues/1118)) ([622e244](https://www.github.com/snakemake/snakemake-wrappers/commit/622e244c8569874c0acb30e9e9d3ca0e2bd7a86c))

### [1.23.5](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.4...v1.23.5) (2023-02-24)


### Bug Fixes

* fixed bug in obtaining paired_end parameter for RSEM calculate-expression ([#1075](https://www.github.com/snakemake/snakemake-wrappers/issues/1075)) ([8bf224b](https://www.github.com/snakemake/snakemake-wrappers/commit/8bf224b79504a1a632756a104949ce6edaad360a))


### Performance Improvements

* autobump bio/dada2/dereplicate-fastq ([#1084](https://www.github.com/snakemake/snakemake-wrappers/issues/1084)) ([437f6a8](https://www.github.com/snakemake/snakemake-wrappers/commit/437f6a83a34ad3450047bd87efdab23499d3aa9c))
* autobump bio/diamond/blastp ([#1083](https://www.github.com/snakemake/snakemake-wrappers/issues/1083)) ([7a33605](https://www.github.com/snakemake/snakemake-wrappers/commit/7a33605b9f4fc23aef1880dd31d5c9455148e46f))
* autobump bio/fgbio/filterconsensusreads ([#1088](https://www.github.com/snakemake/snakemake-wrappers/issues/1088)) ([39c3c37](https://www.github.com/snakemake/snakemake-wrappers/commit/39c3c3729875469e073a00e3a8c5cfd433209a21))
* autobump bio/fgbio/setmateinformation ([#1089](https://www.github.com/snakemake/snakemake-wrappers/issues/1089)) ([c50c845](https://www.github.com/snakemake/snakemake-wrappers/commit/c50c845c5d5e0eea30a41f788ffab610d7fc6966))
* autobump bio/jellyfish/dump ([#1077](https://www.github.com/snakemake/snakemake-wrappers/issues/1077)) ([260ba99](https://www.github.com/snakemake/snakemake-wrappers/commit/260ba99d2e86a9bcc36afe0447803e4625d78b3c))
* autobump bio/last/lastal ([#1087](https://www.github.com/snakemake/snakemake-wrappers/issues/1087)) ([03401fa](https://www.github.com/snakemake/snakemake-wrappers/commit/03401fa1f0a10f7a90f53060ef3140b2405a0b3c))
* autobump bio/last/lastdb ([#1091](https://www.github.com/snakemake/snakemake-wrappers/issues/1091)) ([8bf8271](https://www.github.com/snakemake/snakemake-wrappers/commit/8bf8271a469960325f4982486f6c888fc4309ff2))
* autobump bio/pbmm2/align ([#1086](https://www.github.com/snakemake/snakemake-wrappers/issues/1086)) ([3cc3e23](https://www.github.com/snakemake/snakemake-wrappers/commit/3cc3e239ef414045d1b78ef64315c5ad306e8ad5))
* autobump bio/picard/collectrnaseqmetrics ([#1082](https://www.github.com/snakemake/snakemake-wrappers/issues/1082)) ([812a58a](https://www.github.com/snakemake/snakemake-wrappers/commit/812a58a46259488b9a34047fba6394fba5efaa16))
* autobump bio/picard/collecttargetedpcrmetrics ([#1003](https://www.github.com/snakemake/snakemake-wrappers/issues/1003)) ([43682ed](https://www.github.com/snakemake/snakemake-wrappers/commit/43682ed68205f418027d9df58ada9d5eb8a7fc27))
* autobump bio/picard/sortsam ([#1081](https://www.github.com/snakemake/snakemake-wrappers/issues/1081)) ([176f729](https://www.github.com/snakemake/snakemake-wrappers/commit/176f729b3cdf0ea72d65ef1b0e32c5a466bf5848))
* autobump bio/star/index ([#1090](https://www.github.com/snakemake/snakemake-wrappers/issues/1090)) ([9e654cb](https://www.github.com/snakemake/snakemake-wrappers/commit/9e654cb6af57b8c3b7b42b2a4511a474c538dbdf))
* autobump bio/transdecoder/longorfs ([#1080](https://www.github.com/snakemake/snakemake-wrappers/issues/1080)) ([d8c37ce](https://www.github.com/snakemake/snakemake-wrappers/commit/d8c37cecf5c33cfffd99087b27349e8745f74fe0))
* autobump bio/transdecoder/predict ([#1085](https://www.github.com/snakemake/snakemake-wrappers/issues/1085)) ([2ef8d50](https://www.github.com/snakemake/snakemake-wrappers/commit/2ef8d50ebcb3c1de4031adeddcba05e2a608a5c6))
* autobump bio/unicycler ([#1078](https://www.github.com/snakemake/snakemake-wrappers/issues/1078)) ([3c1770c](https://www.github.com/snakemake/snakemake-wrappers/commit/3c1770c1558e50c5d5bd61e4ecdab1edde41f145))

### [1.23.4](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.3...v1.23.4) (2023-02-17)


### Performance Improvements

* autobump bio/bismark/bismark2bedGraph ([#1073](https://www.github.com/snakemake/snakemake-wrappers/issues/1073)) ([2766554](https://www.github.com/snakemake/snakemake-wrappers/commit/276655494c4ae297e48ca6ae9098c65c4883de1d))
* autobump bio/bismark/bismark2report ([#1063](https://www.github.com/snakemake/snakemake-wrappers/issues/1063)) ([599ae52](https://www.github.com/snakemake/snakemake-wrappers/commit/599ae5256b5d840411398387a5b822a39fa8dd20))
* autobump bio/bustools/count ([#1067](https://www.github.com/snakemake/snakemake-wrappers/issues/1067)) ([19154c6](https://www.github.com/snakemake/snakemake-wrappers/commit/19154c6ae442cdac5a956b70c4a1309069cb5125))
* autobump bio/cooltools/eigs_cis ([#1007](https://www.github.com/snakemake/snakemake-wrappers/issues/1007)) ([2742fb7](https://www.github.com/snakemake/snakemake-wrappers/commit/2742fb7228b2f9bf8985b4e77efb9c352a93ca73))
* autobump bio/cooltools/pileup ([#1058](https://www.github.com/snakemake/snakemake-wrappers/issues/1058)) ([127917f](https://www.github.com/snakemake/snakemake-wrappers/commit/127917ff333992d802d4637a6d7dd14ecb159f86))
* autobump bio/dada2/filter-trim ([#1065](https://www.github.com/snakemake/snakemake-wrappers/issues/1065)) ([677627f](https://www.github.com/snakemake/snakemake-wrappers/commit/677627f070871ae7f9f18b8fa3921e3c02be3c9d))
* autobump bio/fastq_screen ([#1060](https://www.github.com/snakemake/snakemake-wrappers/issues/1060)) ([14dc0ab](https://www.github.com/snakemake/snakemake-wrappers/commit/14dc0abd243002f1eba38163ccd6f10b1666a5c7))
* autobump bio/fgbio/annotatebamwithumis ([#1064](https://www.github.com/snakemake/snakemake-wrappers/issues/1064)) ([9ed4c70](https://www.github.com/snakemake/snakemake-wrappers/commit/9ed4c70bc3c816b063ee8eb651c35ca62f516bdd))
* autobump bio/fgbio/groupreadsbyumi ([#1070](https://www.github.com/snakemake/snakemake-wrappers/issues/1070)) ([b93045c](https://www.github.com/snakemake/snakemake-wrappers/commit/b93045c0300c7617be17c893b41189166c43524c))
* autobump bio/freebayes ([#1055](https://www.github.com/snakemake/snakemake-wrappers/issues/1055)) ([7b21acc](https://www.github.com/snakemake/snakemake-wrappers/commit/7b21acc9064e745b41e9e5c6ae7bd465ae776518))
* autobump bio/gdc-api/bam-slicing ([#1004](https://www.github.com/snakemake/snakemake-wrappers/issues/1004)) ([eae8d4d](https://www.github.com/snakemake/snakemake-wrappers/commit/eae8d4dad0672849c95c70f40c52370b413f1e55))
* autobump bio/hifiasm ([#1069](https://www.github.com/snakemake/snakemake-wrappers/issues/1069)) ([da38102](https://www.github.com/snakemake/snakemake-wrappers/commit/da3810250d383b828cb9e7f318d4d560bb17ef76))
* autobump bio/microphaser/normal ([#1051](https://www.github.com/snakemake/snakemake-wrappers/issues/1051)) ([70cbcc5](https://www.github.com/snakemake/snakemake-wrappers/commit/70cbcc54d88d570d7df24f4b608b8af21e7eb2d4))
* autobump bio/picard/collecthsmetrics ([#1057](https://www.github.com/snakemake/snakemake-wrappers/issues/1057)) ([dd3b642](https://www.github.com/snakemake/snakemake-wrappers/commit/dd3b642f199fff0f18f24b78f15a935813e696c9))
* autobump bio/picard/collectmultiplemetrics ([#1054](https://www.github.com/snakemake/snakemake-wrappers/issues/1054)) ([c1c1d02](https://www.github.com/snakemake/snakemake-wrappers/commit/c1c1d026e3a9b071d1493cba14f891f991670919))
* autobump bio/picard/revertsam ([#1061](https://www.github.com/snakemake/snakemake-wrappers/issues/1061)) ([6b7abe4](https://www.github.com/snakemake/snakemake-wrappers/commit/6b7abe4da2bf1d0f5589efebdc036343b4e8d125))
* autobump bio/picard/samtofastq ([#1066](https://www.github.com/snakemake/snakemake-wrappers/issues/1066)) ([3b269b1](https://www.github.com/snakemake/snakemake-wrappers/commit/3b269b117bd2d2a029b53800778bbf1c7b267daf))
* autobump bio/sambamba/flagstat ([#1068](https://www.github.com/snakemake/snakemake-wrappers/issues/1068)) ([8f038a0](https://www.github.com/snakemake/snakemake-wrappers/commit/8f038a0ba39409e0e4bff58656fa27e5472b490b))
* autobump bio/sambamba/view ([#1056](https://www.github.com/snakemake/snakemake-wrappers/issues/1056)) ([13ebb41](https://www.github.com/snakemake/snakemake-wrappers/commit/13ebb41ef2e0bd9c92d2a62b4624cc151ea2244c))
* autobump bio/sourmash/compute ([#1059](https://www.github.com/snakemake/snakemake-wrappers/issues/1059)) ([58d1b56](https://www.github.com/snakemake/snakemake-wrappers/commit/58d1b5642cd9a0455b549d650a1c83b214432d22))
* autobump bio/star/align ([#1009](https://www.github.com/snakemake/snakemake-wrappers/issues/1009)) ([61b9c99](https://www.github.com/snakemake/snakemake-wrappers/commit/61b9c99fadd3681025580851eb701628c0f5ecb7))
* autobump bio/umis/bamtag ([#1053](https://www.github.com/snakemake/snakemake-wrappers/issues/1053)) ([1056357](https://www.github.com/snakemake/snakemake-wrappers/commit/10563578ffdb684ff990746fe450bec9ac5e5634))
* autobump bio/vg/ids ([#1052](https://www.github.com/snakemake/snakemake-wrappers/issues/1052)) ([f0c864c](https://www.github.com/snakemake/snakemake-wrappers/commit/f0c864c0779b637b2224c08e92721b4e7ee9b0a1))
* autobump bio/vg/kmers ([#1062](https://www.github.com/snakemake/snakemake-wrappers/issues/1062)) ([3c65ce9](https://www.github.com/snakemake/snakemake-wrappers/commit/3c65ce9ce56a5f31d8380f372d3273199a6882b3))
* autobump bio/vg/prune ([#1050](https://www.github.com/snakemake/snakemake-wrappers/issues/1050)) ([9c0b28d](https://www.github.com/snakemake/snakemake-wrappers/commit/9c0b28d8392c87bcb8aa93324e2ac63e96da5c89))
* autobump utils/cairosvg ([#1072](https://www.github.com/snakemake/snakemake-wrappers/issues/1072)) ([b978339](https://www.github.com/snakemake/snakemake-wrappers/commit/b9783399a43b50a2f0086f01c88db5e36f771bef))
* autobump utils/datavzrd ([#1071](https://www.github.com/snakemake/snakemake-wrappers/issues/1071)) ([341cd67](https://www.github.com/snakemake/snakemake-wrappers/commit/341cd67211c5740b1cf7b8b16d80f0a8c7918387))

### [1.23.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.2...v1.23.3) (2023-02-12)


### Performance Improvements

* update datavzrd wrapper to 2.16.2 ([a3784ec](https://www.github.com/snakemake/snakemake-wrappers/commit/a3784ec03589503bd1c58a3f0dbd8719925bf41b))

### [1.23.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.1...v1.23.2) (2023-02-10)


### Performance Improvements

* autobump bio/bismark/bismark ([#1046](https://www.github.com/snakemake/snakemake-wrappers/issues/1046)) ([4c692f6](https://www.github.com/snakemake/snakemake-wrappers/commit/4c692f6316a6b257df7c26b69d4739e01c5886c4))
* autobump bio/bustools/sort ([#1039](https://www.github.com/snakemake/snakemake-wrappers/issues/1039)) ([915ff3d](https://www.github.com/snakemake/snakemake-wrappers/commit/915ff3d96ce6702daac5132948b62ba63adac307))
* autobump bio/bwa-mem2/mem-samblaster ([#1035](https://www.github.com/snakemake/snakemake-wrappers/issues/1035)) ([68d0b8e](https://www.github.com/snakemake/snakemake-wrappers/commit/68d0b8e63e69079ae86cca78c4379821257b645e))
* autobump bio/cooltools/insulation ([#1032](https://www.github.com/snakemake/snakemake-wrappers/issues/1032)) ([3ccb3c1](https://www.github.com/snakemake/snakemake-wrappers/commit/3ccb3c1a03600d4e71c7d14b8570c17c93f177e8))
* autobump bio/dada2/add-species ([#1031](https://www.github.com/snakemake/snakemake-wrappers/issues/1031)) ([1e84d85](https://www.github.com/snakemake/snakemake-wrappers/commit/1e84d85c3f38f86a6956a9f0bc833288e9e3301c))
* autobump bio/dada2/assign-species ([#1040](https://www.github.com/snakemake/snakemake-wrappers/issues/1040)) ([939fb25](https://www.github.com/snakemake/snakemake-wrappers/commit/939fb2538e59064bc733e772ef1c4efbd9f4bcc8))
* autobump bio/dada2/sample-inference ([#1043](https://www.github.com/snakemake/snakemake-wrappers/issues/1043)) ([8d40576](https://www.github.com/snakemake/snakemake-wrappers/commit/8d40576408d2cddec2a79a723ec078c6ae8fa740))
* autobump bio/igv-reports ([#1029](https://www.github.com/snakemake/snakemake-wrappers/issues/1029)) ([a9765ed](https://www.github.com/snakemake/snakemake-wrappers/commit/a9765edc4e6e5867aab9afde84177405d8e6f0ef))
* autobump bio/last/lastal ([#1041](https://www.github.com/snakemake/snakemake-wrappers/issues/1041)) ([1854b53](https://www.github.com/snakemake/snakemake-wrappers/commit/1854b5352df38080adf6355f2270c3aa6747c1b7))
* autobump bio/mapdamage2 ([#1045](https://www.github.com/snakemake/snakemake-wrappers/issues/1045)) ([dae7008](https://www.github.com/snakemake/snakemake-wrappers/commit/dae70088efce7f40a3581bc7abeb0e93449e4fa6))
* autobump bio/minimap2/aligner ([#1033](https://www.github.com/snakemake/snakemake-wrappers/issues/1033)) ([c1bbdd8](https://www.github.com/snakemake/snakemake-wrappers/commit/c1bbdd8804acb80e65de718ae3dc589ede5d9375))
* autobump bio/paladin/index ([#1036](https://www.github.com/snakemake/snakemake-wrappers/issues/1036)) ([0ce4cee](https://www.github.com/snakemake/snakemake-wrappers/commit/0ce4cee58e720f69faaa73ea30b9b407b72b48ae))
* autobump bio/picard/markduplicateswithmatecigar ([#1042](https://www.github.com/snakemake/snakemake-wrappers/issues/1042)) ([19a404b](https://www.github.com/snakemake/snakemake-wrappers/commit/19a404b0cb304de290790414666ca67b2109345d))
* autobump bio/sra-tools/fasterq-dump ([#1047](https://www.github.com/snakemake/snakemake-wrappers/issues/1047)) ([c74a7c3](https://www.github.com/snakemake/snakemake-wrappers/commit/c74a7c3cd4a5dc289294e023d4d49669803982fa))
* autobump bio/trim_galore/se ([#1034](https://www.github.com/snakemake/snakemake-wrappers/issues/1034)) ([daeb43d](https://www.github.com/snakemake/snakemake-wrappers/commit/daeb43dd375f56f83d0a5b06bedf4dbec80be9d8))
* autobump bio/vg/ids ([#1037](https://www.github.com/snakemake/snakemake-wrappers/issues/1037)) ([d89576e](https://www.github.com/snakemake/snakemake-wrappers/commit/d89576ef745b57387b07b5c2b2d826e8023a1a8b))

### [1.23.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.23.0...v1.23.1) (2023-02-07)


### Performance Improvements

* update to datavzrd 2.16.0 ([4a988ce](https://www.github.com/snakemake/snakemake-wrappers/commit/4a988ce0aa503a3ff8f01f147dad533888c183e0))

## [1.23.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.22.0...v1.23.0) (2023-02-06)


### Features

* Add GATK LeftAlignAndTrimVariants ([#993](https://www.github.com/snakemake/snakemake-wrappers/issues/993)) ([4ec0c91](https://www.github.com/snakemake/snakemake-wrappers/commit/4ec0c91f37e037479c40551463449d96830a548e))


### Performance Improvements

* autobump bio/bismark/bismark_methylation_extractor ([#1024](https://www.github.com/snakemake/snakemake-wrappers/issues/1024)) ([e6f7f0a](https://www.github.com/snakemake/snakemake-wrappers/commit/e6f7f0a5143d9fd88904921a5249ccd10b0a13de))
* autobump bio/bowtie2/build ([#1025](https://www.github.com/snakemake/snakemake-wrappers/issues/1025)) ([f242c1c](https://www.github.com/snakemake/snakemake-wrappers/commit/f242c1c15461eab86738a6687cc73dddb40e9677))
* autobump bio/bwa/mem-samblaster ([#1015](https://www.github.com/snakemake/snakemake-wrappers/issues/1015)) ([2ff4af3](https://www.github.com/snakemake/snakemake-wrappers/commit/2ff4af3c7e732762c8a1209d1319d279e1718cda))
* autobump bio/cooltools/eigs_trans ([#1026](https://www.github.com/snakemake/snakemake-wrappers/issues/1026)) ([01eb73c](https://www.github.com/snakemake/snakemake-wrappers/commit/01eb73cf7f33c11bc58610ad82900fa3ae600698))
* autobump bio/cooltools/expected_trans ([#995](https://www.github.com/snakemake/snakemake-wrappers/issues/995)) ([080b51d](https://www.github.com/snakemake/snakemake-wrappers/commit/080b51d818424d102cda2cdbe6b66052cad8b4d6))
* autobump bio/cutadapt/se ([#1010](https://www.github.com/snakemake/snakemake-wrappers/issues/1010)) ([8cf09dc](https://www.github.com/snakemake/snakemake-wrappers/commit/8cf09dccfe7e789e6bd2300e94da3f44d315f715))
* autobump bio/dada2/quality-profile ([#1022](https://www.github.com/snakemake/snakemake-wrappers/issues/1022)) ([f077b94](https://www.github.com/snakemake/snakemake-wrappers/commit/f077b9402ff375b3a9387efd2afa02987e1c7716))
* autobump bio/deeptools/plotprofile ([#1018](https://www.github.com/snakemake/snakemake-wrappers/issues/1018)) ([d9d2a69](https://www.github.com/snakemake/snakemake-wrappers/commit/d9d2a690ba1a91f0f52e1997876ed7752f3896d1))
* autobump bio/delly ([#1000](https://www.github.com/snakemake/snakemake-wrappers/issues/1000)) ([f499f25](https://www.github.com/snakemake/snakemake-wrappers/commit/f499f25acd085b02687a699e4f1f77bd5f6ea1f5))
* autobump bio/dragmap/build ([#1002](https://www.github.com/snakemake/snakemake-wrappers/issues/1002)) ([f0e0334](https://www.github.com/snakemake/snakemake-wrappers/commit/f0e033454a33d456702f2841ecbc7bd23c889666))
* autobump bio/gatk/varianteval ([#997](https://www.github.com/snakemake/snakemake-wrappers/issues/997)) ([1690ac6](https://www.github.com/snakemake/snakemake-wrappers/commit/1690ac6914251b160dd9f549b09972c0aa93fa1b))
* autobump bio/gatk3/baserecalibrator ([#1016](https://www.github.com/snakemake/snakemake-wrappers/issues/1016)) ([3e2bef3](https://www.github.com/snakemake/snakemake-wrappers/commit/3e2bef360699ac223ef579a7e9afffc71519c3c8))
* autobump bio/gridss/assemble ([#998](https://www.github.com/snakemake/snakemake-wrappers/issues/998)) ([fa9002e](https://www.github.com/snakemake/snakemake-wrappers/commit/fa9002e010e1ffede3e111ecae0ae983f5ee8068))
* autobump bio/hmmer/hmmbuild ([#1021](https://www.github.com/snakemake/snakemake-wrappers/issues/1021)) ([492a0c5](https://www.github.com/snakemake/snakemake-wrappers/commit/492a0c5ed5e468c063f76a4ffa8bfb42fd73fd26))
* autobump bio/microphaser/somatic ([#1012](https://www.github.com/snakemake/snakemake-wrappers/issues/1012)) ([95854e8](https://www.github.com/snakemake/snakemake-wrappers/commit/95854e827ae99f8f6f3cda777fab1ce77c93ae0d))
* autobump bio/paladin/align ([#1027](https://www.github.com/snakemake/snakemake-wrappers/issues/1027)) ([7ebca79](https://www.github.com/snakemake/snakemake-wrappers/commit/7ebca795f284ee7ddb64aeb06d16c9657fa39ab8))
* autobump bio/pbmm2/index ([#1011](https://www.github.com/snakemake/snakemake-wrappers/issues/1011)) ([d170c59](https://www.github.com/snakemake/snakemake-wrappers/commit/d170c59524d9376a7ce9fa82f9c323398106f488))
* autobump bio/picard/addorreplacereadgroups ([#1008](https://www.github.com/snakemake/snakemake-wrappers/issues/1008)) ([094c52e](https://www.github.com/snakemake/snakemake-wrappers/commit/094c52e1fe2523382714cfc04ecd9fbaab0a3adb))
* autobump bio/picard/bedtointervallist ([#1019](https://www.github.com/snakemake/snakemake-wrappers/issues/1019)) ([284c3ba](https://www.github.com/snakemake/snakemake-wrappers/commit/284c3ba54782b9a02db2e501318fccbcf404dab6))
* autobump bio/picard/mergesamfiles ([#1014](https://www.github.com/snakemake/snakemake-wrappers/issues/1014)) ([ea653db](https://www.github.com/snakemake/snakemake-wrappers/commit/ea653db97e36d011f750b991a9364e67ddb910c2))
* autobump bio/pyfastaq/replace_bases ([#1020](https://www.github.com/snakemake/snakemake-wrappers/issues/1020)) ([46f165f](https://www.github.com/snakemake/snakemake-wrappers/commit/46f165f9e51a4f3eb59f0b6e3862f9b9b55dff2e))
* autobump bio/sambamba/slice ([#996](https://www.github.com/snakemake/snakemake-wrappers/issues/996)) ([a3daa64](https://www.github.com/snakemake/snakemake-wrappers/commit/a3daa644e5b4c768df52a2cc71fb4c950e3f9d98))
* autobump bio/snpsift/gwascat ([#1023](https://www.github.com/snakemake/snakemake-wrappers/issues/1023)) ([c797edb](https://www.github.com/snakemake/snakemake-wrappers/commit/c797edb3b5eace9b23ce19edba9ac947fc48ac6d))
* autobump bio/tximport ([#1017](https://www.github.com/snakemake/snakemake-wrappers/issues/1017)) ([b4005d1](https://www.github.com/snakemake/snakemake-wrappers/commit/b4005d196518e1d9889d05c2eff560d297bf8026))
* autobump bio/ucsc/gtfToGenePred ([#999](https://www.github.com/snakemake/snakemake-wrappers/issues/999)) ([aeb6bd0](https://www.github.com/snakemake/snakemake-wrappers/commit/aeb6bd0a2168f5ca5c9370853e29b9140cbed7e4))
* autobump bio/vg/merge ([#1001](https://www.github.com/snakemake/snakemake-wrappers/issues/1001)) ([158c387](https://www.github.com/snakemake/snakemake-wrappers/commit/158c387372c578127f537f831d7d49532185a4dd))
* autobump bio/vg/sim ([#1013](https://www.github.com/snakemake/snakemake-wrappers/issues/1013)) ([94ecd75](https://www.github.com/snakemake/snakemake-wrappers/commit/94ecd75817ffe1256b093585ba9d9eff14ca90fd))

## [1.22.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.6...v1.22.0) (2023-02-01)


### Features

* Add GATK VariantsToTable ([#989](https://www.github.com/snakemake/snakemake-wrappers/issues/989)) ([e3654ce](https://www.github.com/snakemake/snakemake-wrappers/commit/e3654ced09ad53eecc2b7abe8eee8c59fc6e44aa))


### Bug Fixes

* do not download fasta file in VEP cache wrapper ([#992](https://www.github.com/snakemake/snakemake-wrappers/issues/992)) ([612933e](https://www.github.com/snakemake/snakemake-wrappers/commit/612933e4cb945355d0e6fa752f80a6564ee8d3f6))


### Performance Improvements

* Sambamba version update 0.8.2->1.0 ([#988](https://www.github.com/snakemake/snakemake-wrappers/issues/988)) ([6525373](https://www.github.com/snakemake/snakemake-wrappers/commit/6525373d909155025d5d7a494bc27739f88944d6))

### [1.21.6](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.5...v1.21.6) (2023-01-30)


### Bug Fixes

* properly handle proxy setting in vep cache wrapper ([#986](https://www.github.com/snakemake/snakemake-wrappers/issues/986)) ([3a5379b](https://www.github.com/snakemake/snakemake-wrappers/commit/3a5379bf8b672e7374b7f0bab3ed966c5bfe211a))

### [1.21.5](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.4...v1.21.5) (2023-01-30)


### Performance Improvements

* autobump bio/sambamba/merge ([#982](https://www.github.com/snakemake/snakemake-wrappers/issues/982)) ([701abe0](https://www.github.com/snakemake/snakemake-wrappers/commit/701abe0819f23ab63a672aa7d5d02397e2591aa7))
* update datavzrd to version 2.14.1 ([#985](https://www.github.com/snakemake/snakemake-wrappers/issues/985)) ([07fc839](https://www.github.com/snakemake/snakemake-wrappers/commit/07fc8391b967fc287803b04b2716c94a1f74eb46))

### [1.21.4](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.3...v1.21.4) (2023-01-20)


### Bug Fixes

* channel definitions for cooltools (and update version to 0.5.2), genefuse, genomescope, qualimap and meryl ([#980](https://www.github.com/snakemake/snakemake-wrappers/issues/980)) ([26271ac](https://www.github.com/snakemake/snakemake-wrappers/commit/26271acfb27c02d51d2a8cc0922b4780998e6b53))
* RSEM-calculate-expression wrapper with FASTQ-files as input + Integration of test case ([#970](https://www.github.com/snakemake/snakemake-wrappers/issues/970)) ([ea9c897](https://www.github.com/snakemake/snakemake-wrappers/commit/ea9c8978259c87156f4e48711eed0172a8966209))

### [1.21.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.2...v1.21.3) (2023-01-20)


### Bug Fixes

* consensus meta wrapper ([#977](https://www.github.com/snakemake/snakemake-wrappers/issues/977)) ([a320aa5](https://www.github.com/snakemake/snakemake-wrappers/commit/a320aa5fdef6dd6215b5cfee8232713dcdf19de3))
* snakemake and mamba deployment ([#978](https://www.github.com/snakemake/snakemake-wrappers/issues/978)) ([4c64b96](https://www.github.com/snakemake/snakemake-wrappers/commit/4c64b9647eddbb52d80e9377ca16357cf00136c0))

### [1.21.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.1...v1.21.2) (2023-01-10)


### Bug Fixes

* make 'params: extra=' optional for rbt collapse_reads_to_fragments-bam wrapper ([#968](https://www.github.com/snakemake/snakemake-wrappers/issues/968)) ([03463da](https://www.github.com/snakemake/snakemake-wrappers/commit/03463da5ea60046d7c9a1a33459d3296c3ddb98c))


### Performance Improvements

* update datavzrd wrapper to 2.12.0 ([#973](https://www.github.com/snakemake/snakemake-wrappers/issues/973)) ([8523e73](https://www.github.com/snakemake/snakemake-wrappers/commit/8523e737ca0a5d7ae28a8a98b0988d6ea9e7f67b))

### [1.21.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.21.0...v1.21.1) (2022-12-21)


### Performance Improvements

* update datavzrd wrapper to 2.11.1 ([12b3076](https://www.github.com/snakemake/snakemake-wrappers/commit/12b30766e1fbecefeae5ad99dce8856a8f28f006))

## [1.21.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.20.0...v1.21.0) (2022-12-12)


### Features

* tmpdir in Sambamba wrappers ([#960](https://www.github.com/snakemake/snakemake-wrappers/issues/960)) ([a8333a3](https://www.github.com/snakemake/snakemake-wrappers/commit/a8333a3e44d3eac30453860f1793678d01167e40))
* update arriba and star_arriba meta-wrapper ([#963](https://www.github.com/snakemake/snakemake-wrappers/issues/963)) ([f75d997](https://www.github.com/snakemake/snakemake-wrappers/commit/f75d997ca582e20165adbb34e55ce2224136081d))


### Bug Fixes

* updated parsing of bcftools opts ([#959](https://www.github.com/snakemake/snakemake-wrappers/issues/959)) ([0af69c9](https://www.github.com/snakemake/snakemake-wrappers/commit/0af69c9f5ea2e016ea70ebe8a44747dc6fbd3e30))


### Performance Improvements

* autobump bio/bwa-memx/index ([#955](https://www.github.com/snakemake/snakemake-wrappers/issues/955)) ([f51c0d6](https://www.github.com/snakemake/snakemake-wrappers/commit/f51c0d6e1cc6dfe714a0ef875bd68c0401dcc21a))
* autobump bio/cooltools/pileup ([#948](https://www.github.com/snakemake/snakemake-wrappers/issues/948)) ([bf28d88](https://www.github.com/snakemake/snakemake-wrappers/commit/bf28d88b33aff888d9b3dc339b8a740a7e2017c8))
* autobump bio/dada2/assign-taxonomy ([#946](https://www.github.com/snakemake/snakemake-wrappers/issues/946)) ([ed9ebfb](https://www.github.com/snakemake/snakemake-wrappers/commit/ed9ebfb588af703fe550cf71945ee5b684efa0d8))
* autobump bio/diamond/makedb ([#944](https://www.github.com/snakemake/snakemake-wrappers/issues/944)) ([a95b5db](https://www.github.com/snakemake/snakemake-wrappers/commit/a95b5db5d7c722804b9e4ecb3fa375a76e4f3191))
* autobump bio/gatk/genotypegvcfs ([#951](https://www.github.com/snakemake/snakemake-wrappers/issues/951)) ([5fb96d8](https://www.github.com/snakemake/snakemake-wrappers/commit/5fb96d8e8e43b3350ba2833f291c09d3e7ea1ff0))
* autobump bio/gatk/selectvariants ([#947](https://www.github.com/snakemake/snakemake-wrappers/issues/947)) ([5f697b8](https://www.github.com/snakemake/snakemake-wrappers/commit/5f697b80cf3acee5367efd2fddc58aa7828abba9))
* autobump bio/homer/annotatePeaks ([#952](https://www.github.com/snakemake/snakemake-wrappers/issues/952)) ([8f1270d](https://www.github.com/snakemake/snakemake-wrappers/commit/8f1270de93dd613e1d3f4042ed5c2c3c099b87b5))
* autobump bio/homer/mergePeaks ([#957](https://www.github.com/snakemake/snakemake-wrappers/issues/957)) ([0330a43](https://www.github.com/snakemake/snakemake-wrappers/commit/0330a434160a5a015c19fb76a9c67665ace630ff))
* autobump bio/jellyfish/count ([#950](https://www.github.com/snakemake/snakemake-wrappers/issues/950)) ([0a6f68d](https://www.github.com/snakemake/snakemake-wrappers/commit/0a6f68db8723f2c3f8a794d33badef8e4e32a773))
* autobump bio/last/lastal ([#942](https://www.github.com/snakemake/snakemake-wrappers/issues/942)) ([8e5ef69](https://www.github.com/snakemake/snakemake-wrappers/commit/8e5ef69bc49fc2b911b7b9da6ba8f97c6149590b))
* autobump bio/microphaser/build_reference ([#943](https://www.github.com/snakemake/snakemake-wrappers/issues/943)) ([1e7ece5](https://www.github.com/snakemake/snakemake-wrappers/commit/1e7ece5157bab0a83608a14cbdf45bced50322f0))
* autobump bio/picard/collecttargetedpcrmetrics ([#949](https://www.github.com/snakemake/snakemake-wrappers/issues/949)) ([5239da9](https://www.github.com/snakemake/snakemake-wrappers/commit/5239da9b112d0ad5af6e0f79275b162d9a2b3f57))
* autobump bio/transdecoder/longorfs ([#956](https://www.github.com/snakemake/snakemake-wrappers/issues/956)) ([54c2b74](https://www.github.com/snakemake/snakemake-wrappers/commit/54c2b74e6913cef43fa81a0fd86e997d12c37cde))
* autobump bio/tximport ([#954](https://www.github.com/snakemake/snakemake-wrappers/issues/954)) ([4942f36](https://www.github.com/snakemake/snakemake-wrappers/commit/4942f365b97cabeb7478113aece432d2439ac9ce))
* autobump bio/varscan/somatic ([#958](https://www.github.com/snakemake/snakemake-wrappers/issues/958)) ([28df43c](https://www.github.com/snakemake/snakemake-wrappers/commit/28df43c261751477a9cc888c30794709795e9dcb))

## [1.20.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.19.2...v1.20.0) (2022-12-01)


### Features

* Add threads to cooltools insulation ([#919](https://www.github.com/snakemake/snakemake-wrappers/issues/919)) ([fdf035e](https://www.github.com/snakemake/snakemake-wrappers/commit/fdf035ea037d7ce3c2883d49d76fd186e350bbac))
* GATK SplitIntervals wrapper ([#836](https://www.github.com/snakemake/snakemake-wrappers/issues/836)) ([986fa3a](https://www.github.com/snakemake/snakemake-wrappers/commit/986fa3a4f330cf0ff27869718a17aa86668ca141))
* samtools view allow region specification ([#940](https://www.github.com/snakemake/snakemake-wrappers/issues/940)) ([c1fdb5e](https://www.github.com/snakemake/snakemake-wrappers/commit/c1fdb5eab1496b5e95a4a8ede82670cf2f6d2cef))


### Bug Fixes

* Correct referencing of Snakemake input variables (release: 1.19.2) ([#937](https://www.github.com/snakemake/snakemake-wrappers/issues/937)) ([b828ac3](https://www.github.com/snakemake/snakemake-wrappers/commit/b828ac3c6eaf5c8382e3746635817cebcefe449f))


### Performance Improvements

* autobump bio/bowtie2/build ([#932](https://www.github.com/snakemake/snakemake-wrappers/issues/932)) ([26bcc0b](https://www.github.com/snakemake/snakemake-wrappers/commit/26bcc0b2ec6b553fc6c0720d9075c4def2de2ef5))
* autobump bio/dada2/learn-errors ([#929](https://www.github.com/snakemake/snakemake-wrappers/issues/929)) ([32e9f5c](https://www.github.com/snakemake/snakemake-wrappers/commit/32e9f5c15442f78978b319205ed2b517a14e3f3a))
* autobump bio/gatk/baserecalibratorspark ([#935](https://www.github.com/snakemake/snakemake-wrappers/issues/935)) ([ff15e44](https://www.github.com/snakemake/snakemake-wrappers/commit/ff15e44badd984d4dd6598bafa41d93959c8afb0))
* autobump bio/gatk/cleansam ([#792](https://www.github.com/snakemake/snakemake-wrappers/issues/792)) ([6055e79](https://www.github.com/snakemake/snakemake-wrappers/commit/6055e791c104c896f18d3671f3593ad83340d6e7))
* autobump bio/gatk/estimatelibrarycomplexity ([#926](https://www.github.com/snakemake/snakemake-wrappers/issues/926)) ([c366755](https://www.github.com/snakemake/snakemake-wrappers/commit/c3667553c4354932bb7efdbfca0587f7b205b42e))
* autobump bio/infernal/cmscan ([#924](https://www.github.com/snakemake/snakemake-wrappers/issues/924)) ([36634d9](https://www.github.com/snakemake/snakemake-wrappers/commit/36634d91f686e03385e5af5de1c7fe1cbf1c0ea5))
* autobump bio/microphaser/somatic ([#925](https://www.github.com/snakemake/snakemake-wrappers/issues/925)) ([cb44ee0](https://www.github.com/snakemake/snakemake-wrappers/commit/cb44ee09dafa8bb51a449a42d325a8523a8c27fc))
* autobump bio/picard/collectinsertsizemetrics ([#934](https://www.github.com/snakemake/snakemake-wrappers/issues/934)) ([fd8fecd](https://www.github.com/snakemake/snakemake-wrappers/commit/fd8fecdcd9db0994686219f45307b62b27bb5a85))
* autobump bio/picard/collectrnaseqmetrics ([#920](https://www.github.com/snakemake/snakemake-wrappers/issues/920)) ([40eccd5](https://www.github.com/snakemake/snakemake-wrappers/commit/40eccd5ae9e5ac0814a448b6ccb3917f4c35b28d))
* autobump bio/pretext/graph ([#930](https://www.github.com/snakemake/snakemake-wrappers/issues/930)) ([2a1fb56](https://www.github.com/snakemake/snakemake-wrappers/commit/2a1fb569f7e9e0b5afe515ffb24cfe82f11f64ae))
* autobump bio/purge_dups/get_seqs ([#922](https://www.github.com/snakemake/snakemake-wrappers/issues/922)) ([ad5fba2](https://www.github.com/snakemake/snakemake-wrappers/commit/ad5fba20ed453cd0c8ce7222481f2cf425e4d460))
* autobump bio/samtools/sort ([#921](https://www.github.com/snakemake/snakemake-wrappers/issues/921)) ([4dde2ae](https://www.github.com/snakemake/snakemake-wrappers/commit/4dde2ae49115171502f1f0a162b24bfa8eebb5db))
* autobump bio/samtools/view ([#936](https://www.github.com/snakemake/snakemake-wrappers/issues/936)) ([24254fd](https://www.github.com/snakemake/snakemake-wrappers/commit/24254fdf65866b09a52feeb307943c633d875959))
* autobump bio/vembrane/filter ([#927](https://www.github.com/snakemake/snakemake-wrappers/issues/927)) ([510b06a](https://www.github.com/snakemake/snakemake-wrappers/commit/510b06af5e32befd649da3f9340b716665c9b6e0))
* autobump bio/vep/annotate ([#928](https://www.github.com/snakemake/snakemake-wrappers/issues/928)) ([bb30b19](https://www.github.com/snakemake/snakemake-wrappers/commit/bb30b19d1df00ac89f124a3a8ee93530ed2285c5))
* autobump bio/vg/kmers ([#931](https://www.github.com/snakemake/snakemake-wrappers/issues/931)) ([067b6a8](https://www.github.com/snakemake/snakemake-wrappers/commit/067b6a8735ff09cbfeacdd1478f034b3e24433e5))
* autobump bio/vg/merge ([#933](https://www.github.com/snakemake/snakemake-wrappers/issues/933)) ([5ac344d](https://www.github.com/snakemake/snakemake-wrappers/commit/5ac344d929e147fc9c450792b2438a83bbd3b633))
* update to latest datavzrd ([d08bc08](https://www.github.com/snakemake/snakemake-wrappers/commit/d08bc08197e925c9b3e96d53bed453153cc9576f))

### [1.19.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.19.1...v1.19.2) (2022-11-18)


### Bug Fixes

* Removed unnecessary openjdk references ([#835](https://www.github.com/snakemake/snakemake-wrappers/issues/835)) ([0353285](https://www.github.com/snakemake/snakemake-wrappers/commit/035328563254b7c5e1dc9ac0be8faedee066855e))


### Performance Improvements

* autobump bio/bismark/bismark ([#907](https://www.github.com/snakemake/snakemake-wrappers/issues/907)) ([2c8dc87](https://www.github.com/snakemake/snakemake-wrappers/commit/2c8dc8769e5eac41d19a7b35fee7b41eadffca91))
* autobump bio/bwa-meme/mem ([#897](https://www.github.com/snakemake/snakemake-wrappers/issues/897)) ([d377cce](https://www.github.com/snakemake/snakemake-wrappers/commit/d377cce4b70659d4b65bd083b5bb36f0cf212a8b))
* autobump bio/bwa-memx/mem ([#909](https://www.github.com/snakemake/snakemake-wrappers/issues/909)) ([31974b1](https://www.github.com/snakemake/snakemake-wrappers/commit/31974b1a9dc8e60551c1a5f6e8e894602b067cf5))
* autobump bio/deeptools/computematrix ([#895](https://www.github.com/snakemake/snakemake-wrappers/issues/895)) ([b0b1943](https://www.github.com/snakemake/snakemake-wrappers/commit/b0b1943bf1a6958972ec86829a7d6a32975c6d3e))
* autobump bio/deeptools/plotfingerprint ([#887](https://www.github.com/snakemake/snakemake-wrappers/issues/887)) ([5157780](https://www.github.com/snakemake/snakemake-wrappers/commit/5157780b3e9baf0268ec75b13e3db4058fe9eac8))
* autobump bio/fastq_screen ([#916](https://www.github.com/snakemake/snakemake-wrappers/issues/916)) ([6c62488](https://www.github.com/snakemake/snakemake-wrappers/commit/6c62488020b061dad87219e8b8d5034a58550e71))
* autobump bio/fgbio/groupreadsbyumi ([#908](https://www.github.com/snakemake/snakemake-wrappers/issues/908)) ([caa4b85](https://www.github.com/snakemake/snakemake-wrappers/commit/caa4b854eebae9eb5faf0f09aac286a1b2a54595))
* autobump bio/gatk/depthofcoverage ([#905](https://www.github.com/snakemake/snakemake-wrappers/issues/905)) ([8043b30](https://www.github.com/snakemake/snakemake-wrappers/commit/8043b30f7efdc41859c406c618b24c8842abcf08))
* autobump bio/gatk/mutect ([#892](https://www.github.com/snakemake/snakemake-wrappers/issues/892)) ([6fcabfa](https://www.github.com/snakemake/snakemake-wrappers/commit/6fcabfa8990343810a6dd12c0ce0f0f9d4c70b5b))
* autobump bio/gatk/variantfiltration ([#911](https://www.github.com/snakemake/snakemake-wrappers/issues/911)) ([b9cc5d4](https://www.github.com/snakemake/snakemake-wrappers/commit/b9cc5d47d1b6a558b639116fe8880aa3a1b659b2))
* autobump bio/homer/getDifferentialPeaks ([#894](https://www.github.com/snakemake/snakemake-wrappers/issues/894)) ([fba57fa](https://www.github.com/snakemake/snakemake-wrappers/commit/fba57fa7b7dcfba2fcb32ae45994e3eb2b2fec64))
* autobump bio/homer/makeTagDirectory ([#899](https://www.github.com/snakemake/snakemake-wrappers/issues/899)) ([762aa81](https://www.github.com/snakemake/snakemake-wrappers/commit/762aa81c64bce22ec907aa18ce40a2c1b42c7132))
* autobump bio/last/lastdb ([#889](https://www.github.com/snakemake/snakemake-wrappers/issues/889)) ([f3ffc52](https://www.github.com/snakemake/snakemake-wrappers/commit/f3ffc52334d5c2f3d10e3d00eb887608e07f635b))
* autobump bio/meryl/count ([#896](https://www.github.com/snakemake/snakemake-wrappers/issues/896)) ([c1dea53](https://www.github.com/snakemake/snakemake-wrappers/commit/c1dea53900835ac2c308025f0618cd59d89d33c9))
* autobump bio/paladin/prepare ([#900](https://www.github.com/snakemake/snakemake-wrappers/issues/900)) ([f06905d](https://www.github.com/snakemake/snakemake-wrappers/commit/f06905daaa57e566218b6e76be67e5be06515ff3))
* autobump bio/pbmm2/index ([#893](https://www.github.com/snakemake/snakemake-wrappers/issues/893)) ([7b84d5b](https://www.github.com/snakemake/snakemake-wrappers/commit/7b84d5b5d1dc88ca8dfd45f026ec3ef8ecc9d2c3))
* autobump bio/picard/mergesamfiles ([#906](https://www.github.com/snakemake/snakemake-wrappers/issues/906)) ([c89123b](https://www.github.com/snakemake/snakemake-wrappers/commit/c89123b486fe9a6f91cb76d5b3ea1bf357c2e32e))
* autobump bio/pindel/pindel2vcf ([#904](https://www.github.com/snakemake/snakemake-wrappers/issues/904)) ([7582c86](https://www.github.com/snakemake/snakemake-wrappers/commit/7582c86cb920b540a0a21f17fd68e27133c98c7b))
* autobump bio/qualimap/bamqc ([#912](https://www.github.com/snakemake/snakemake-wrappers/issues/912)) ([d73c713](https://www.github.com/snakemake/snakemake-wrappers/commit/d73c7136937e3188a30c62c05b602886c75dad4b))
* autobump bio/qualimap/rnaseq ([#914](https://www.github.com/snakemake/snakemake-wrappers/issues/914)) ([43ec0e7](https://www.github.com/snakemake/snakemake-wrappers/commit/43ec0e7ca5685f15a1d640d9c6f6bc927e770da7))
* autobump bio/rsem/calculate-expression ([#915](https://www.github.com/snakemake/snakemake-wrappers/issues/915)) ([4a02028](https://www.github.com/snakemake/snakemake-wrappers/commit/4a020286194c579e63e229dde0f4427e398054be))
* autobump bio/salmon/index ([#917](https://www.github.com/snakemake/snakemake-wrappers/issues/917)) ([9a7dd71](https://www.github.com/snakemake/snakemake-wrappers/commit/9a7dd71bf29c9c8810b388ae8cb93a54e6b84db7))
* autobump bio/salmon/quant ([#901](https://www.github.com/snakemake/snakemake-wrappers/issues/901)) ([1abf483](https://www.github.com/snakemake/snakemake-wrappers/commit/1abf4835642646844227335d61883f791ed4c969))
* autobump bio/sambamba/index ([#903](https://www.github.com/snakemake/snakemake-wrappers/issues/903)) ([e15388c](https://www.github.com/snakemake/snakemake-wrappers/commit/e15388c85668dee3b9a916ecf9c8e437764ffd3d))
* autobump bio/sambamba/slice ([#890](https://www.github.com/snakemake/snakemake-wrappers/issues/890)) ([7d90b49](https://www.github.com/snakemake/snakemake-wrappers/commit/7d90b492656e1a9ff22a3f3b028bb23f822af693))
* autobump bio/seqtk/mergepe ([#910](https://www.github.com/snakemake/snakemake-wrappers/issues/910)) ([374d337](https://www.github.com/snakemake/snakemake-wrappers/commit/374d337b784ebb82a33c07cbeacdd7c953a5c06a))
* autobump bio/snpsift/annotate ([#898](https://www.github.com/snakemake/snakemake-wrappers/issues/898)) ([6aabee4](https://www.github.com/snakemake/snakemake-wrappers/commit/6aabee4cc1bca83c1435d1eae6d75de28003a84f))
* autobump bio/snpsift/varType ([#902](https://www.github.com/snakemake/snakemake-wrappers/issues/902)) ([c200777](https://www.github.com/snakemake/snakemake-wrappers/commit/c20077773d39573920e67c2e3ff5fec57343f9c7))
* autobump bio/vep/plugins ([#913](https://www.github.com/snakemake/snakemake-wrappers/issues/913)) ([298ab04](https://www.github.com/snakemake/snakemake-wrappers/commit/298ab04eb8cfa659917c0386b5df1c369fbcb695))
* autobump bio/vg/kmers ([#888](https://www.github.com/snakemake/snakemake-wrappers/issues/888)) ([5570e67](https://www.github.com/snakemake/snakemake-wrappers/commit/5570e675fd639d1d28366b93832d562c6d9ec4e5))
* autobump bio/vg/sim ([#886](https://www.github.com/snakemake/snakemake-wrappers/issues/886)) ([83c3189](https://www.github.com/snakemake/snakemake-wrappers/commit/83c3189322e414831ec37ce1ade2dfd0f5cf3bba))
* autobump utils/datavzrd ([#891](https://www.github.com/snakemake/snakemake-wrappers/issues/891)) ([4a4e4ce](https://www.github.com/snakemake/snakemake-wrappers/commit/4a4e4ce81b2f51e91cc3fcab763d2f105645ae58))

### [1.19.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.19.0...v1.19.1) (2022-11-11)


### Performance Improvements

* autobump bio/bismark/bismark_genome_preparation ([#819](https://www.github.com/snakemake/snakemake-wrappers/issues/819)) ([1da1afc](https://www.github.com/snakemake/snakemake-wrappers/commit/1da1afc6c616b0376f5bd61269fd584d932e7527))
* autobump bio/bismark/bismark2report ([#812](https://www.github.com/snakemake/snakemake-wrappers/issues/812)) ([8ce5b1a](https://www.github.com/snakemake/snakemake-wrappers/commit/8ce5b1a4d2de950261237a1aafd8572eef778ef4))
* autobump bio/bismark/deduplicate_bismark ([#816](https://www.github.com/snakemake/snakemake-wrappers/issues/816)) ([7f539c4](https://www.github.com/snakemake/snakemake-wrappers/commit/7f539c4ac6f743fbe9e584b9e78efa35388ac82c))
* autobump bio/bowtie2/align ([#798](https://www.github.com/snakemake/snakemake-wrappers/issues/798)) ([6fa3cc7](https://www.github.com/snakemake/snakemake-wrappers/commit/6fa3cc7cad4a1c38b9e7107a55505586909a0904))
* autobump bio/bwa-meme/index ([#862](https://www.github.com/snakemake/snakemake-wrappers/issues/862)) ([68f9c48](https://www.github.com/snakemake/snakemake-wrappers/commit/68f9c480bdef3a053c09fa2eafa46e710e91762a))
* autobump bio/bwa-memx/index ([#780](https://www.github.com/snakemake/snakemake-wrappers/issues/780)) ([9937924](https://www.github.com/snakemake/snakemake-wrappers/commit/99379244427145af11182debb3017a8a8c6764e5))
* autobump bio/cooltools/eigs_cis ([#853](https://www.github.com/snakemake/snakemake-wrappers/issues/853)) ([3973951](https://www.github.com/snakemake/snakemake-wrappers/commit/3973951806c9cf0fd89c9149b4d77723aebeb977))
* autobump bio/cooltools/eigs_trans ([#777](https://www.github.com/snakemake/snakemake-wrappers/issues/777)) ([348c67d](https://www.github.com/snakemake/snakemake-wrappers/commit/348c67dfef15f52063e0d8004ab7f9540effbb96))
* autobump bio/dada2/collapse-nomismatch ([#852](https://www.github.com/snakemake/snakemake-wrappers/issues/852)) ([2ab7b64](https://www.github.com/snakemake/snakemake-wrappers/commit/2ab7b647ac3a6c6f6455715bd596822926fe7cfe))
* autobump bio/dada2/dereplicate-fastq ([#808](https://www.github.com/snakemake/snakemake-wrappers/issues/808)) ([c0692ff](https://www.github.com/snakemake/snakemake-wrappers/commit/c0692ff1eb37e3ee7a456d4b1d064d3a648e86e4))
* autobump bio/dada2/make-table ([#796](https://www.github.com/snakemake/snakemake-wrappers/issues/796)) ([a42557f](https://www.github.com/snakemake/snakemake-wrappers/commit/a42557f1696125bbd16cc51c3538d30bf6151c62))
* autobump bio/dada2/merge-pairs ([#847](https://www.github.com/snakemake/snakemake-wrappers/issues/847)) ([67a8ee6](https://www.github.com/snakemake/snakemake-wrappers/commit/67a8ee600836c2376b6d1ebf3705b0864127b2dd))
* autobump bio/dada2/remove-chimeras ([#776](https://www.github.com/snakemake/snakemake-wrappers/issues/776)) ([2da85cc](https://www.github.com/snakemake/snakemake-wrappers/commit/2da85cc4d8ed68f16eb2adcc79a819448444bb5c))
* autobump bio/deeptools/plotheatmap ([#864](https://www.github.com/snakemake/snakemake-wrappers/issues/864)) ([1eea5f0](https://www.github.com/snakemake/snakemake-wrappers/commit/1eea5f04c7136842812379c34fd1871260e6a79e))
* autobump bio/diamond/blastx ([#875](https://www.github.com/snakemake/snakemake-wrappers/issues/875)) ([a503669](https://www.github.com/snakemake/snakemake-wrappers/commit/a503669257059cdcce4e5fa4ce17be6e1e0f6bd0))
* autobump bio/epic/peaks ([#781](https://www.github.com/snakemake/snakemake-wrappers/issues/781)) ([400c8ce](https://www.github.com/snakemake/snakemake-wrappers/commit/400c8ceeb223913cac333da6bef9cf156593cc0a))
* autobump bio/fgbio/callmolecularconsensusreads ([#826](https://www.github.com/snakemake/snakemake-wrappers/issues/826)) ([194056e](https://www.github.com/snakemake/snakemake-wrappers/commit/194056e9b19e5a50ff7439bc844f0c0f5678de29))
* autobump bio/fgbio/filterconsensusreads ([#801](https://www.github.com/snakemake/snakemake-wrappers/issues/801)) ([491eed9](https://www.github.com/snakemake/snakemake-wrappers/commit/491eed92cbfff12c9433774819717e87247eeca7))
* autobump bio/gatk/applybqsr ([#803](https://www.github.com/snakemake/snakemake-wrappers/issues/803)) ([d27cc85](https://www.github.com/snakemake/snakemake-wrappers/commit/d27cc85bb85b57e5759d8f9fde73129d8ead96a8))
* autobump bio/gatk/applyvqsr ([#858](https://www.github.com/snakemake/snakemake-wrappers/issues/858)) ([202ab9f](https://www.github.com/snakemake/snakemake-wrappers/commit/202ab9f4b950849ed8ae51b28facc9f162ab13dc))
* autobump bio/gatk/baserecalibrator ([#820](https://www.github.com/snakemake/snakemake-wrappers/issues/820)) ([20e258c](https://www.github.com/snakemake/snakemake-wrappers/commit/20e258c4c6418cbafc20a901e4529e8c87ec26bf))
* autobump bio/gatk/combinegvcfs ([#811](https://www.github.com/snakemake/snakemake-wrappers/issues/811)) ([6b27084](https://www.github.com/snakemake/snakemake-wrappers/commit/6b2708449daa7d3ab9f5873cec1ee52853a9fcaf))
* autobump bio/gatk/filtermutectcalls ([#845](https://www.github.com/snakemake/snakemake-wrappers/issues/845)) ([15de736](https://www.github.com/snakemake/snakemake-wrappers/commit/15de736111357384912b03e55e4b55e99a9e2e75))
* autobump bio/gatk/getpileupsummaries ([#866](https://www.github.com/snakemake/snakemake-wrappers/issues/866)) ([ae118d0](https://www.github.com/snakemake/snakemake-wrappers/commit/ae118d029ae2311370bf5520f307d106810e21b7))
* autobump bio/gatk/learnreadorientationmodel ([#854](https://www.github.com/snakemake/snakemake-wrappers/issues/854)) ([82d03d5](https://www.github.com/snakemake/snakemake-wrappers/commit/82d03d56b410afe96a8017dae92ad6a5d2bffe8f))
* autobump bio/gatk/splitncigarreads ([#790](https://www.github.com/snakemake/snakemake-wrappers/issues/790)) ([a7a890b](https://www.github.com/snakemake/snakemake-wrappers/commit/a7a890bc2fa0d253ad427b3bd5237aa4b4221f26))
* autobump bio/gatk3/indelrealigner ([#827](https://www.github.com/snakemake/snakemake-wrappers/issues/827)) ([a0793af](https://www.github.com/snakemake/snakemake-wrappers/commit/a0793aff88f8ae11bd33a8645e70d68c632718cd))
* autobump bio/gatk3/printreads ([#806](https://www.github.com/snakemake/snakemake-wrappers/issues/806)) ([998852c](https://www.github.com/snakemake/snakemake-wrappers/commit/998852c4f4d0254c409d72fe353e95f02ae6c5b1))
* autobump bio/gatk3/realignertargetcreator ([#865](https://www.github.com/snakemake/snakemake-wrappers/issues/865)) ([b76bd75](https://www.github.com/snakemake/snakemake-wrappers/commit/b76bd7537bcd5c132158857945b6e7dff421a9dd))
* autobump bio/gridss/call ([#846](https://www.github.com/snakemake/snakemake-wrappers/issues/846)) ([01b3056](https://www.github.com/snakemake/snakemake-wrappers/commit/01b30560fe2c4cd3ec65cf7a7fc04ac7340eaf18))
* autobump bio/hisat2/index ([#815](https://www.github.com/snakemake/snakemake-wrappers/issues/815)) ([3c13af5](https://www.github.com/snakemake/snakemake-wrappers/commit/3c13af55cc5a7afe40d52313268a90be73bc2f89))
* autobump bio/hmmer/hmmpress ([#779](https://www.github.com/snakemake/snakemake-wrappers/issues/779)) ([d08c5fd](https://www.github.com/snakemake/snakemake-wrappers/commit/d08c5fd2fd7ca2cd551e9366bde2f4d42ebf726a))
* autobump bio/jellyfish/histo ([#818](https://www.github.com/snakemake/snakemake-wrappers/issues/818)) ([0dd35bc](https://www.github.com/snakemake/snakemake-wrappers/commit/0dd35bc7697a5a0babaccc4df4786bb36b94feb0))
* autobump bio/jellyfish/merge ([#861](https://www.github.com/snakemake/snakemake-wrappers/issues/861)) ([278a80e](https://www.github.com/snakemake/snakemake-wrappers/commit/278a80e363641341991a259df67ded624da228b5))
* autobump bio/kallisto/quant ([#821](https://www.github.com/snakemake/snakemake-wrappers/issues/821)) ([af4128c](https://www.github.com/snakemake/snakemake-wrappers/commit/af4128ccfbdcccd5cedf52a7abfdab5b8c7fb77d))
* autobump bio/lofreq/call ([#872](https://www.github.com/snakemake/snakemake-wrappers/issues/872)) ([000eb6e](https://www.github.com/snakemake/snakemake-wrappers/commit/000eb6e5e119d5d52fd39320c80cb7f963740f36))
* autobump bio/macs2/callpeak ([#810](https://www.github.com/snakemake/snakemake-wrappers/issues/810)) ([9fe846b](https://www.github.com/snakemake/snakemake-wrappers/commit/9fe846b2748fad337b93ae308a45ae72759520fb))
* autobump bio/meryl/sets ([#783](https://www.github.com/snakemake/snakemake-wrappers/issues/783)) ([f8bec12](https://www.github.com/snakemake/snakemake-wrappers/commit/f8bec126c49e72cd04c913d9bd2b71f69da459a3))
* autobump bio/meryl/stats ([#785](https://www.github.com/snakemake/snakemake-wrappers/issues/785)) ([bfae5c5](https://www.github.com/snakemake/snakemake-wrappers/commit/bfae5c552536a538921c9015c5ff8c5f27ff9ae3))
* autobump bio/microphaser/build_reference ([#823](https://www.github.com/snakemake/snakemake-wrappers/issues/823)) ([7a79754](https://www.github.com/snakemake/snakemake-wrappers/commit/7a79754a8ca6d1837bdf01337bcd5aa1cd118938))
* autobump bio/msisensor/msi ([#850](https://www.github.com/snakemake/snakemake-wrappers/issues/850)) ([7d605a0](https://www.github.com/snakemake/snakemake-wrappers/commit/7d605a0a91f36b82ce106a40643c2af700babbc1))
* autobump bio/msisensor/scan ([#842](https://www.github.com/snakemake/snakemake-wrappers/issues/842)) ([1db9fe6](https://www.github.com/snakemake/snakemake-wrappers/commit/1db9fe6662b818fcd9dd7cf4367004c82b90408a))
* autobump bio/open-cravat/module ([#782](https://www.github.com/snakemake/snakemake-wrappers/issues/782)) ([996fe01](https://www.github.com/snakemake/snakemake-wrappers/commit/996fe0152632c98a279f58897e0979110efd6336))
* autobump bio/open-cravat/run ([#807](https://www.github.com/snakemake/snakemake-wrappers/issues/807)) ([70c6500](https://www.github.com/snakemake/snakemake-wrappers/commit/70c65004cd77eba2c05267c68c367e7351f128b7))
* autobump bio/pandora/index ([#805](https://www.github.com/snakemake/snakemake-wrappers/issues/805)) ([8c9ea62](https://www.github.com/snakemake/snakemake-wrappers/commit/8c9ea624e2c2690413a8f241766f32dc389adb2f))
* autobump bio/picard/collecthsmetrics ([#788](https://www.github.com/snakemake/snakemake-wrappers/issues/788)) ([0220a41](https://www.github.com/snakemake/snakemake-wrappers/commit/0220a4174c459dad5c9c9175f92d42849ac1de82))
* autobump bio/picard/revertsam ([#874](https://www.github.com/snakemake/snakemake-wrappers/issues/874)) ([c811ef5](https://www.github.com/snakemake/snakemake-wrappers/commit/c811ef5fe714a078963b5fbd518c4ed4cca79966))
* autobump bio/picard/sortsam ([#822](https://www.github.com/snakemake/snakemake-wrappers/issues/822)) ([30f468d](https://www.github.com/snakemake/snakemake-wrappers/commit/30f468d2fef33fdf9b4bda5f1ed41553a89b5cd4))
* autobump bio/preseq/lc_extrap ([#840](https://www.github.com/snakemake/snakemake-wrappers/issues/840)) ([d0ec0bb](https://www.github.com/snakemake/snakemake-wrappers/commit/d0ec0bbfd28920050862778cae6a2cdc0bad8581))
* autobump bio/pretext/map ([#841](https://www.github.com/snakemake/snakemake-wrappers/issues/841)) ([0a0193c](https://www.github.com/snakemake/snakemake-wrappers/commit/0a0193ccf59f1393100125feca9678fd9b976ad2))
* autobump bio/pretext/snapshot ([#843](https://www.github.com/snakemake/snakemake-wrappers/issues/843)) ([4d3a224](https://www.github.com/snakemake/snakemake-wrappers/commit/4d3a2247d2f90ac640de4b634f0743e3efbc609b))
* autobump bio/prosolo/single-cell-bulk ([#870](https://www.github.com/snakemake/snakemake-wrappers/issues/870)) ([da52ad6](https://www.github.com/snakemake/snakemake-wrappers/commit/da52ad6d014a4bc5a6ea1f77bcbdfcc3282687ca))
* autobump bio/purge_dups/calcuts ([#793](https://www.github.com/snakemake/snakemake-wrappers/issues/793)) ([95f421c](https://www.github.com/snakemake/snakemake-wrappers/commit/95f421c00987f12581a178bb60ba9d9209e296c8))
* autobump bio/purge_dups/ngscstat ([#791](https://www.github.com/snakemake/snakemake-wrappers/issues/791)) ([a7d6ef9](https://www.github.com/snakemake/snakemake-wrappers/commit/a7d6ef986ef98a7e86adfc629617d840d02b722d))
* autobump bio/purge_dups/pbcstat ([#787](https://www.github.com/snakemake/snakemake-wrappers/issues/787)) ([3775e6a](https://www.github.com/snakemake/snakemake-wrappers/commit/3775e6a9b9b22889bf9db8bae0bb03478ff9d718))
* autobump bio/rbt/collapse_reads_to_fragments-bam ([#794](https://www.github.com/snakemake/snakemake-wrappers/issues/794)) ([2eb9983](https://www.github.com/snakemake/snakemake-wrappers/commit/2eb998301b1a9b4ceb0b41ad050ad5cbec6728eb))
* autobump bio/rbt/csvreport ([#838](https://www.github.com/snakemake/snakemake-wrappers/issues/838)) ([eea403e](https://www.github.com/snakemake/snakemake-wrappers/commit/eea403e36648e6d13d14c0ccf0e1ba4a3f6f30a7))
* autobump bio/rsem/generate-data-matrix ([#828](https://www.github.com/snakemake/snakemake-wrappers/issues/828)) ([e16d591](https://www.github.com/snakemake/snakemake-wrappers/commit/e16d591cef368c22aee51d4e1964f39aeef8b1e6))
* autobump bio/sambamba/markdup ([#814](https://www.github.com/snakemake/snakemake-wrappers/issues/814)) ([0cd1c99](https://www.github.com/snakemake/snakemake-wrappers/commit/0cd1c993ce538ffc854b2a3b080dcc463811223c))
* autobump bio/sambamba/merge ([#839](https://www.github.com/snakemake/snakemake-wrappers/issues/839)) ([b81e778](https://www.github.com/snakemake/snakemake-wrappers/commit/b81e77835cee48a5d7ef5ec083f3d0aec9e9ad29))
* autobump bio/sambamba/sort ([#784](https://www.github.com/snakemake/snakemake-wrappers/issues/784)) ([6252efd](https://www.github.com/snakemake/snakemake-wrappers/commit/6252efdcf60ea7567c33a9b87ad30d9bc66bb206))
* autobump bio/samtools/faidx ([#859](https://www.github.com/snakemake/snakemake-wrappers/issues/859)) ([cbdae53](https://www.github.com/snakemake/snakemake-wrappers/commit/cbdae53cc73d96de1ef6e966a31b8deeef4c005c))
* autobump bio/samtools/fastx ([#855](https://www.github.com/snakemake/snakemake-wrappers/issues/855)) ([509c570](https://www.github.com/snakemake/snakemake-wrappers/commit/509c5708df7bc8d6c63a7c8b6904c9f36b82710c))
* autobump bio/samtools/fixmate ([#774](https://www.github.com/snakemake/snakemake-wrappers/issues/774)) ([bb28da9](https://www.github.com/snakemake/snakemake-wrappers/commit/bb28da9ea03ded3081afa3b09a77f06363a3347d))
* autobump bio/samtools/merge ([#844](https://www.github.com/snakemake/snakemake-wrappers/issues/844)) ([5905d2e](https://www.github.com/snakemake/snakemake-wrappers/commit/5905d2e2ff9952e5e32f610e93843a73efea7931))
* autobump bio/samtools/mpileup ([#829](https://www.github.com/snakemake/snakemake-wrappers/issues/829)) ([d5120cb](https://www.github.com/snakemake/snakemake-wrappers/commit/d5120cbe1fc9ffc22cc6dd6dd0a102bc201b06f0))
* autobump bio/samtools/stats ([#797](https://www.github.com/snakemake/snakemake-wrappers/issues/797)) ([524db3e](https://www.github.com/snakemake/snakemake-wrappers/commit/524db3ef71aaf966a61781c5fb4106be229c2fc7))
* autobump bio/sickle/se ([#786](https://www.github.com/snakemake/snakemake-wrappers/issues/786)) ([ef4a4ad](https://www.github.com/snakemake/snakemake-wrappers/commit/ef4a4ad3beacab30b78cc4c440e7186bdab3a6bc))
* autobump bio/snpeff/download ([#851](https://www.github.com/snakemake/snakemake-wrappers/issues/851)) ([3bc7aa5](https://www.github.com/snakemake/snakemake-wrappers/commit/3bc7aa5a18fc5f7a28b284bcae65204586e38488))
* autobump bio/snpsift/dbnsfp ([#856](https://www.github.com/snakemake/snakemake-wrappers/issues/856)) ([67ed70a](https://www.github.com/snakemake/snakemake-wrappers/commit/67ed70a33518b8f7453cb243bc19c0976f31525b))
* autobump bio/snpsift/genesets ([#799](https://www.github.com/snakemake/snakemake-wrappers/issues/799)) ([251fd82](https://www.github.com/snakemake/snakemake-wrappers/commit/251fd822694d089237411cd2d3d95163a27450bd))
* autobump bio/sourmash/compute ([#795](https://www.github.com/snakemake/snakemake-wrappers/issues/795)) ([e063ce8](https://www.github.com/snakemake/snakemake-wrappers/commit/e063ce88ceb4a37ed4cb90a58ef7dc3a9f4775e3))
* autobump bio/spades/metaspades ([#860](https://www.github.com/snakemake/snakemake-wrappers/issues/860)) ([983754f](https://www.github.com/snakemake/snakemake-wrappers/commit/983754f7386aecbc2f0dd2921a47f7034e41ae80))
* autobump bio/sra-tools/fasterq-dump ([#873](https://www.github.com/snakemake/snakemake-wrappers/issues/873)) ([5914529](https://www.github.com/snakemake/snakemake-wrappers/commit/59145293bb2e52ca438289d1881b75dd8ea649cf))
* autobump bio/strelka/somatic ([#813](https://www.github.com/snakemake/snakemake-wrappers/issues/813)) ([d52a2ad](https://www.github.com/snakemake/snakemake-wrappers/commit/d52a2ad6aee1b1ef74ddb6805f6d8535c27e3e0e))
* autobump bio/strling/call ([#789](https://www.github.com/snakemake/snakemake-wrappers/issues/789)) ([9fa5f86](https://www.github.com/snakemake/snakemake-wrappers/commit/9fa5f8615769e7ce4d8f1ab7b36bea1978bf834a))
* autobump bio/strling/extract ([#876](https://www.github.com/snakemake/snakemake-wrappers/issues/876)) ([45152e6](https://www.github.com/snakemake/snakemake-wrappers/commit/45152e6a31d733cdb358d09f39df97227bec45e6))
* autobump bio/strling/index ([#809](https://www.github.com/snakemake/snakemake-wrappers/issues/809)) ([9472934](https://www.github.com/snakemake/snakemake-wrappers/commit/9472934c6b1dfdb2a752b80ae5019cf812f492b6))
* autobump bio/strling/merge ([#824](https://www.github.com/snakemake/snakemake-wrappers/issues/824)) ([82cc5a7](https://www.github.com/snakemake/snakemake-wrappers/commit/82cc5a75d4ace1c58fb0245cc77a7d57cb02af0d))
* autobump bio/tabix/index ([#863](https://www.github.com/snakemake/snakemake-wrappers/issues/863)) ([9de5e3c](https://www.github.com/snakemake/snakemake-wrappers/commit/9de5e3c3b88774bbecb7dc33f8002501e1a7a61c))
* autobump bio/tabix/query ([#868](https://www.github.com/snakemake/snakemake-wrappers/issues/868)) ([088f3db](https://www.github.com/snakemake/snakemake-wrappers/commit/088f3db257b55cbc15ce9aedc6c892547917a0cf))
* autobump bio/ucsc/bedGraphToBigWig ([#825](https://www.github.com/snakemake/snakemake-wrappers/issues/825)) ([c72f046](https://www.github.com/snakemake/snakemake-wrappers/commit/c72f046e5579ca1975afc13de5dd21c38eb7da4f))
* autobump bio/ucsc/gtfToGenePred ([#802](https://www.github.com/snakemake/snakemake-wrappers/issues/802)) ([b306b81](https://www.github.com/snakemake/snakemake-wrappers/commit/b306b8141e3ca984b57c8ba445c96a3a216907b7))
* autobump bio/varscan/mpileup2snp ([#849](https://www.github.com/snakemake/snakemake-wrappers/issues/849)) ([300738b](https://www.github.com/snakemake/snakemake-wrappers/commit/300738b4abf4ac547202a3e01826403b2ee998be))
* autobump bio/vcftools/filter ([#804](https://www.github.com/snakemake/snakemake-wrappers/issues/804)) ([a18db0a](https://www.github.com/snakemake/snakemake-wrappers/commit/a18db0a1b953ad1b844f29403e873c50a985ddd7))
* autobump bio/vep/annotate ([#857](https://www.github.com/snakemake/snakemake-wrappers/issues/857)) ([84bd8bd](https://www.github.com/snakemake/snakemake-wrappers/commit/84bd8bd9ac30e68250eaafbc79455ef1f4b2cd46))
* autobump bio/vep/cache ([#741](https://www.github.com/snakemake/snakemake-wrappers/issues/741)) ([ef12aed](https://www.github.com/snakemake/snakemake-wrappers/commit/ef12aed70413f4bdace81923cf1ab650b24f27ed))
* autobump bio/vg/ids ([#871](https://www.github.com/snakemake/snakemake-wrappers/issues/871)) ([10a1c0d](https://www.github.com/snakemake/snakemake-wrappers/commit/10a1c0de13ef61b9896a4be1134f36538f6602f1))
* autobump bio/vg/merge ([#867](https://www.github.com/snakemake/snakemake-wrappers/issues/867)) ([064ca8c](https://www.github.com/snakemake/snakemake-wrappers/commit/064ca8c086e6ddc6e821b941da621d4dcac6846c))
* autobump bio/vg/prune ([#817](https://www.github.com/snakemake/snakemake-wrappers/issues/817)) ([104775a](https://www.github.com/snakemake/snakemake-wrappers/commit/104775ab5b03628d2cb6a6ea42b76df24476de5c))

## [1.19.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.18.3...v1.19.0) (2022-11-08)


### Features

* add wrapper for coolpuppy ([#554](https://www.github.com/snakemake/snakemake-wrappers/issues/554)) ([60f1fc1](https://www.github.com/snakemake/snakemake-wrappers/commit/60f1fc1a895fff794569fefa51312199a7e0bfd2))


### Bug Fixes

* fixed GATK3 conda channel priorities and code reformat ([#534](https://www.github.com/snakemake/snakemake-wrappers/issues/534)) ([43e5a16](https://www.github.com/snakemake/snakemake-wrappers/commit/43e5a16c1bb88ea09999278d12eaee89c8d4e424))


### Performance Improvements

* autobump bio/bismark/deduplicate_bismark ([#672](https://www.github.com/snakemake/snakemake-wrappers/issues/672)) ([c4ee12f](https://www.github.com/snakemake/snakemake-wrappers/commit/c4ee12f83c544833aa4f807b60e691516c030bf3))
* autobump bio/gatk/variantrecalibrator ([#773](https://www.github.com/snakemake/snakemake-wrappers/issues/773)) ([8de1652](https://www.github.com/snakemake/snakemake-wrappers/commit/8de1652264379da3e83e4cc0b6fb01d40699de69))
* autobump bio/hmmer/hmmscan ([#830](https://www.github.com/snakemake/snakemake-wrappers/issues/830)) ([727b385](https://www.github.com/snakemake/snakemake-wrappers/commit/727b385701a695a0a352275a0e3dcd1d19707056))
* autobump bio/picard/bedtointervallist ([#833](https://www.github.com/snakemake/snakemake-wrappers/issues/833)) ([f1faa62](https://www.github.com/snakemake/snakemake-wrappers/commit/f1faa6244fde6ff28f26169aaae0f04c17723910))
* autobump bio/picard/collectalignmentsummarymetrics ([#831](https://www.github.com/snakemake/snakemake-wrappers/issues/831)) ([c264c15](https://www.github.com/snakemake/snakemake-wrappers/commit/c264c15a32439c40029938ed2dce285e4e2bf9e3))
* autobump bio/picard/collectinsertsizemetrics ([#834](https://www.github.com/snakemake/snakemake-wrappers/issues/834)) ([8381cd8](https://www.github.com/snakemake/snakemake-wrappers/commit/8381cd8ab874d09a3d9295c846a2c8c7cb3c93bd))
* autobump bio/seqtk/seq ([#832](https://www.github.com/snakemake/snakemake-wrappers/issues/832)) ([754c4df](https://www.github.com/snakemake/snakemake-wrappers/commit/754c4dfda12338f04610377a70a87ca1b51f3939))
* update datavzrd wrapper to version 2.7.2 ([12e47fd](https://www.github.com/snakemake/snakemake-wrappers/commit/12e47fdc05b2c603e9970a7a2ed9fe70e226249e))

### [1.18.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.18.2...v1.18.3) (2022-10-30)


### Performance Improvements

* autobump bio/bwa-memx/mem ([#729](https://www.github.com/snakemake/snakemake-wrappers/issues/729)) ([eb4ceba](https://www.github.com/snakemake/snakemake-wrappers/commit/eb4ceba3cd8acbb9de5e4c5cd370535198e0b179))
* autobump bio/cooltools/expected_cis ([#754](https://www.github.com/snakemake/snakemake-wrappers/issues/754)) ([3507020](https://www.github.com/snakemake/snakemake-wrappers/commit/3507020a68e317cf1c77895b68cf67dbadebb73a))
* autobump bio/cooltools/expected_trans ([#728](https://www.github.com/snakemake/snakemake-wrappers/issues/728)) ([b2b6598](https://www.github.com/snakemake/snakemake-wrappers/commit/b2b659868965dc5160fdd1a963f53221c412bd07))
* autobump bio/cooltools/pileup ([#710](https://www.github.com/snakemake/snakemake-wrappers/issues/710)) ([8f675a7](https://www.github.com/snakemake/snakemake-wrappers/commit/8f675a7643717dfd349363900149dfe285683750))
* autobump bio/cooltools/saddle ([#719](https://www.github.com/snakemake/snakemake-wrappers/issues/719)) ([77b7765](https://www.github.com/snakemake/snakemake-wrappers/commit/77b776582001b46c219ec05134012c33265b245f))
* autobump bio/dada2/filter-trim ([#722](https://www.github.com/snakemake/snakemake-wrappers/issues/722)) ([2784d7d](https://www.github.com/snakemake/snakemake-wrappers/commit/2784d7d5d780f6c508b7aaa4a72409d119f2bcb0))
* autobump bio/dada2/learn-errors ([#727](https://www.github.com/snakemake/snakemake-wrappers/issues/727)) ([2df75ab](https://www.github.com/snakemake/snakemake-wrappers/commit/2df75abcdc05ef2ce1ca460bd1f4208ee47921db))
* autobump bio/dada2/quality-profile ([#753](https://www.github.com/snakemake/snakemake-wrappers/issues/753)) ([2d541c7](https://www.github.com/snakemake/snakemake-wrappers/commit/2d541c778f49f13927ba48dee53116faf6ef7f81))
* autobump bio/diamond/blastp ([#756](https://www.github.com/snakemake/snakemake-wrappers/issues/756)) ([a4d1a2c](https://www.github.com/snakemake/snakemake-wrappers/commit/a4d1a2c1a92ff714ea04ab9eda60cb302010b7bb))
* autobump bio/fgbio/annotatebamwithumis ([#740](https://www.github.com/snakemake/snakemake-wrappers/issues/740)) ([2405be7](https://www.github.com/snakemake/snakemake-wrappers/commit/2405be71f9d49555009de8d01d4c3ba1fc359067))
* autobump bio/fgbio/setmateinformation ([#751](https://www.github.com/snakemake/snakemake-wrappers/issues/751)) ([3f335df](https://www.github.com/snakemake/snakemake-wrappers/commit/3f335dfe8fca37b6cf0abd1f1ce19f65abe03729))
* autobump bio/gatk/applybqsrspark ([#757](https://www.github.com/snakemake/snakemake-wrappers/issues/757)) ([5afaf86](https://www.github.com/snakemake/snakemake-wrappers/commit/5afaf86c895cebab5a685ff1418c1ff971539de5))
* autobump bio/gatk/estimatelibrarycomplexity ([#717](https://www.github.com/snakemake/snakemake-wrappers/issues/717)) ([1ec8a34](https://www.github.com/snakemake/snakemake-wrappers/commit/1ec8a348e61045d48a37c36d897ef8179c85ffb2))
* autobump bio/gatk/intervallisttobed ([#721](https://www.github.com/snakemake/snakemake-wrappers/issues/721)) ([d7a2d2a](https://www.github.com/snakemake/snakemake-wrappers/commit/d7a2d2aa8f7fa6f11c7b36836c6ce1cf72db059d))
* autobump bio/gatk/printreadsspark ([#749](https://www.github.com/snakemake/snakemake-wrappers/issues/749)) ([42f55d3](https://www.github.com/snakemake/snakemake-wrappers/commit/42f55d3a3dff5e5ee474003bb0e57166e7235301))
* autobump bio/gatk/scatterintervalsbyns ([#712](https://www.github.com/snakemake/snakemake-wrappers/issues/712)) ([fd1d5a3](https://www.github.com/snakemake/snakemake-wrappers/commit/fd1d5a3a347cf3c21f6f766d8c06804245d783f9))
* autobump bio/gatk3/printreads ([#737](https://www.github.com/snakemake/snakemake-wrappers/issues/737)) ([6a595c3](https://www.github.com/snakemake/snakemake-wrappers/commit/6a595c358f298eafbb81be7c5fb0f7b5596a1ec1))
* autobump bio/gdc-api/bam-slicing ([#747](https://www.github.com/snakemake/snakemake-wrappers/issues/747)) ([b7c4734](https://www.github.com/snakemake/snakemake-wrappers/commit/b7c4734cd71dcb6778d3ea61929eb5086a67366a))
* autobump bio/gdc-client/download ([#720](https://www.github.com/snakemake/snakemake-wrappers/issues/720)) ([7245dab](https://www.github.com/snakemake/snakemake-wrappers/commit/7245daba9cd510a0769e787aa5e9b422651d01bd))
* autobump bio/hmmer/hmmsearch ([#752](https://www.github.com/snakemake/snakemake-wrappers/issues/752)) ([57b7f73](https://www.github.com/snakemake/snakemake-wrappers/commit/57b7f73b6cba0ce2d58b99e3dfe4f4b8c0edb6f5))
* autobump bio/homer/findPeaks ([#746](https://www.github.com/snakemake/snakemake-wrappers/issues/746)) ([396d6ba](https://www.github.com/snakemake/snakemake-wrappers/commit/396d6ba520dff1b4d70078d55ae36e7b39b42248))
* autobump bio/igv-reports ([#603](https://www.github.com/snakemake/snakemake-wrappers/issues/603)) ([b2c306a](https://www.github.com/snakemake/snakemake-wrappers/commit/b2c306ace7cb7aba786f9b814f51112680ec807b))
* autobump bio/infernal/cmpress ([#750](https://www.github.com/snakemake/snakemake-wrappers/issues/750)) ([4c9dbc0](https://www.github.com/snakemake/snakemake-wrappers/commit/4c9dbc01857c0f002137af7664c6d350a04df5af))
* autobump bio/liftoff ([#605](https://www.github.com/snakemake/snakemake-wrappers/issues/605)) ([a963375](https://www.github.com/snakemake/snakemake-wrappers/commit/a963375e965cc5d59e62bb2ed60fc2238bd95340))
* autobump bio/manta ([#606](https://www.github.com/snakemake/snakemake-wrappers/issues/606)) ([186bad3](https://www.github.com/snakemake/snakemake-wrappers/commit/186bad3bbb4853350d626e04fd372409c9bf8c0c))
* autobump bio/mapdamage2 ([#607](https://www.github.com/snakemake/snakemake-wrappers/issues/607)) ([8c20ad2](https://www.github.com/snakemake/snakemake-wrappers/commit/8c20ad2487099a987ea807e05da5a655025fe6b6))
* autobump bio/microphaser/normal ([#755](https://www.github.com/snakemake/snakemake-wrappers/issues/755)) ([a1d3025](https://www.github.com/snakemake/snakemake-wrappers/commit/a1d30255716a120e56f26397da805ebaa9c31059))
* autobump bio/picard/collectgcbiasmetrics ([#725](https://www.github.com/snakemake/snakemake-wrappers/issues/725)) ([35af564](https://www.github.com/snakemake/snakemake-wrappers/commit/35af564edcaf3a44fc8166ecbbf07a0eedd09230))
* autobump bio/picard/createsequencedictionary ([#714](https://www.github.com/snakemake/snakemake-wrappers/issues/714)) ([d12cf4f](https://www.github.com/snakemake/snakemake-wrappers/commit/d12cf4f15aba3a922f8d2a7606dffebcbb7ec3dc))
* autobump bio/picard/markduplicates ([#733](https://www.github.com/snakemake/snakemake-wrappers/issues/733)) ([4fabb76](https://www.github.com/snakemake/snakemake-wrappers/commit/4fabb76931008598785a5442520681b40ae70b3a))
* autobump bio/picard/markduplicateswithmatecigar ([#744](https://www.github.com/snakemake/snakemake-wrappers/issues/744)) ([0981aab](https://www.github.com/snakemake/snakemake-wrappers/commit/0981aab5ed8766364259fc61cd5da94a7e6ab187))
* autobump bio/prosolo/control-fdr ([#723](https://www.github.com/snakemake/snakemake-wrappers/issues/723)) ([b71e470](https://www.github.com/snakemake/snakemake-wrappers/commit/b71e47082a464072b8e59601c977be3a5e14dc72))
* autobump bio/purge_dups/purge_dups ([#748](https://www.github.com/snakemake/snakemake-wrappers/issues/748)) ([e277e97](https://www.github.com/snakemake/snakemake-wrappers/commit/e277e9706884049dbcab0d82afb0ae89c10cdc32))
* autobump bio/purge_dups/split_fa ([#726](https://www.github.com/snakemake/snakemake-wrappers/issues/726)) ([5cd0255](https://www.github.com/snakemake/snakemake-wrappers/commit/5cd025523b669bdc357b3c21dd1384a4241a7f8d))
* autobump bio/sambamba/flagstat ([#711](https://www.github.com/snakemake/snakemake-wrappers/issues/711)) ([4c1322d](https://www.github.com/snakemake/snakemake-wrappers/commit/4c1322d580ab0b8e5f4f6c713d97036dcd9ec9c7))
* autobump bio/samtools/depth ([#715](https://www.github.com/snakemake/snakemake-wrappers/issues/715)) ([e2973ae](https://www.github.com/snakemake/snakemake-wrappers/commit/e2973aef7d1d1746a268b2928535f4e64bf36000))
* autobump bio/samtools/idxstats ([#738](https://www.github.com/snakemake/snakemake-wrappers/issues/738)) ([3da64d0](https://www.github.com/snakemake/snakemake-wrappers/commit/3da64d0cbcd98ee45966ffdf9c7cffc06102e745))
* autobump bio/samtools/index ([#743](https://www.github.com/snakemake/snakemake-wrappers/issues/743)) ([a4aa08f](https://www.github.com/snakemake/snakemake-wrappers/commit/a4aa08f9089853d8cc6af96a6976f953d001c709))
* autobump bio/strelka/germline ([#716](https://www.github.com/snakemake/snakemake-wrappers/issues/716)) ([10d123f](https://www.github.com/snakemake/snakemake-wrappers/commit/10d123f764bda21b0575e02e956a7c6a97c5df00))
* autobump bio/subread/featurecounts ([#724](https://www.github.com/snakemake/snakemake-wrappers/issues/724)) ([3984c2b](https://www.github.com/snakemake/snakemake-wrappers/commit/3984c2bae5fde719faee2fcbe70412895ad6e901))
* autobump bio/transdecoder/predict ([#742](https://www.github.com/snakemake/snakemake-wrappers/issues/742)) ([61c3552](https://www.github.com/snakemake/snakemake-wrappers/commit/61c3552ea30ad548d26c42a817ad014207c5cb25))
* autobump bio/ucsc/faToTwoBit ([#718](https://www.github.com/snakemake/snakemake-wrappers/issues/718)) ([234a306](https://www.github.com/snakemake/snakemake-wrappers/commit/234a306abae8e6a82c6aa0ea2c949921aec649bd))
* autobump bio/ucsc/twoBitToFa ([#745](https://www.github.com/snakemake/snakemake-wrappers/issues/745)) ([bea275e](https://www.github.com/snakemake/snakemake-wrappers/commit/bea275e21c796609a7e4fc58c082faaa89e1ae1d))
* autobump bio/varscan/mpileup2indel ([#759](https://www.github.com/snakemake/snakemake-wrappers/issues/759)) ([96d3944](https://www.github.com/snakemake/snakemake-wrappers/commit/96d3944d5506c720ff6bf852736b3969d54f3697))

### [1.18.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.18.1...v1.18.2) (2022-10-29)


### Bug Fixes

* bwa-meme and bwa-memx documentation ([#765](https://www.github.com/snakemake/snakemake-wrappers/issues/765)) ([43fc0b7](https://www.github.com/snakemake/snakemake-wrappers/commit/43fc0b7e9614d6e828d00e540434c0b41da00e5d))

### [1.18.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.18.0...v1.18.1) (2022-10-28)


### Performance Improvements

* autobump bio/gatk/haplotypecaller ([#758](https://www.github.com/snakemake/snakemake-wrappers/issues/758)) ([ec87a20](https://www.github.com/snakemake/snakemake-wrappers/commit/ec87a20931f56fd2f909f699b1da0349c1188f38))
* autobump bio/mashmap ([#608](https://www.github.com/snakemake/snakemake-wrappers/issues/608)) ([7168282](https://www.github.com/snakemake/snakemake-wrappers/commit/71682820ea5a93e610f49874448d8da0804d25cc))
* autobump bio/microphaser/filter ([#734](https://www.github.com/snakemake/snakemake-wrappers/issues/734)) ([3e1f7d3](https://www.github.com/snakemake/snakemake-wrappers/commit/3e1f7d309d9822aa1e956a91e1720c1d47b81b6a))
* autobump bio/pbmm2/align ([#761](https://www.github.com/snakemake/snakemake-wrappers/issues/761)) ([14dd875](https://www.github.com/snakemake/snakemake-wrappers/commit/14dd875c84b4066f59dbef3009e589c508773af5))
* autobump bio/picard/mergevcfs ([#760](https://www.github.com/snakemake/snakemake-wrappers/issues/760)) ([286d041](https://www.github.com/snakemake/snakemake-wrappers/commit/286d04135db5785223298cc9b233add512cd1448))
* autobump bio/rsem/prepare-reference ([#732](https://www.github.com/snakemake/snakemake-wrappers/issues/732)) ([2a146ac](https://www.github.com/snakemake/snakemake-wrappers/commit/2a146ace99ee175ab1e62a548791e28deb36ee85))
* autobump bio/samtools/calmd ([#735](https://www.github.com/snakemake/snakemake-wrappers/issues/735)) ([df4c61e](https://www.github.com/snakemake/snakemake-wrappers/commit/df4c61e3c1e492eaaa25afc5baaa1487803f5e5e))
* autobump bio/samtools/flagstat ([#736](https://www.github.com/snakemake/snakemake-wrappers/issues/736)) ([a189006](https://www.github.com/snakemake/snakemake-wrappers/commit/a189006a8645399f3379d7d823ec5bd37f102894))
* autobump bio/sickle/pe ([#731](https://www.github.com/snakemake/snakemake-wrappers/issues/731)) ([866bfb5](https://www.github.com/snakemake/snakemake-wrappers/commit/866bfb52e7d62d8b5f921c1f1f6948c6eeff5cf8))
* autobump bio/verifybamid/verifybamid2 ([#730](https://www.github.com/snakemake/snakemake-wrappers/issues/730)) ([8e0f3d7](https://www.github.com/snakemake/snakemake-wrappers/commit/8e0f3d7e7188d6607f2d8b5f0fed731730f4d682))

## [1.18.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.5...v1.18.0) (2022-10-28)


### Features

* bwa memx ([#691](https://www.github.com/snakemake/snakemake-wrappers/issues/691)) ([f281336](https://www.github.com/snakemake/snakemake-wrappers/commit/f2813368441d1e650e9cc6b972938ee0b79b5b13))


### Performance Improvements

* autobump bio/art/profiler_illumina ([#640](https://www.github.com/snakemake/snakemake-wrappers/issues/640)) ([9c91417](https://www.github.com/snakemake/snakemake-wrappers/commit/9c91417b1ae9bd66cf66d6b621d7dc1eff4cb8e8))
* autobump bio/bamtools/filter ([#641](https://www.github.com/snakemake/snakemake-wrappers/issues/641)) ([ad679b8](https://www.github.com/snakemake/snakemake-wrappers/commit/ad679b87ece51c1b4bcb6fe36f0d36b4d7e4eafb))
* autobump bio/bamtools/filter_json ([#642](https://www.github.com/snakemake/snakemake-wrappers/issues/642)) ([41ac02f](https://www.github.com/snakemake/snakemake-wrappers/commit/41ac02f3d12fcc6e047cba8784e41efad6ae4c04))
* autobump bio/bamtools/split ([#643](https://www.github.com/snakemake/snakemake-wrappers/issues/643)) ([ca4cd00](https://www.github.com/snakemake/snakemake-wrappers/commit/ca4cd0019266b2bd14efb6de55692197f8c841f7))
* autobump bio/bamtools/stats ([#644](https://www.github.com/snakemake/snakemake-wrappers/issues/644)) ([7967763](https://www.github.com/snakemake/snakemake-wrappers/commit/79677639fd9b551ecaf06930324f424cf3a63d56))
* autobump bio/bazam ([#600](https://www.github.com/snakemake/snakemake-wrappers/issues/600)) ([1dc1cde](https://www.github.com/snakemake/snakemake-wrappers/commit/1dc1cdede8b273411ff9efe7072ecd393956d33c))
* autobump bio/bbtools/bbduk ([#645](https://www.github.com/snakemake/snakemake-wrappers/issues/645)) ([40c20a9](https://www.github.com/snakemake/snakemake-wrappers/commit/40c20a9b3f9669bb753c9fd25ce6982878af3fbe))
* autobump bio/bcftools/mpileup ([#648](https://www.github.com/snakemake/snakemake-wrappers/issues/648)) ([547922e](https://www.github.com/snakemake/snakemake-wrappers/commit/547922eda6c4319b3f47173dfbcf87620ee5243c))
* autobump bio/bcftools/norm ([#649](https://www.github.com/snakemake/snakemake-wrappers/issues/649)) ([46c6686](https://www.github.com/snakemake/snakemake-wrappers/commit/46c66861486232fd709665c0e23d95d5e896b87a))
* autobump bio/bcftools/reheader ([#650](https://www.github.com/snakemake/snakemake-wrappers/issues/650)) ([e1f3303](https://www.github.com/snakemake/snakemake-wrappers/commit/e1f330325ef3a8b95f6287e65bf954252c85014c))
* autobump bio/bcftools/sort ([#651](https://www.github.com/snakemake/snakemake-wrappers/issues/651)) ([897bdab](https://www.github.com/snakemake/snakemake-wrappers/commit/897bdab983ba503b8fb714299d0de026431c3d11))
* autobump bio/bcftools/stats ([#652](https://www.github.com/snakemake/snakemake-wrappers/issues/652)) ([6aa4a38](https://www.github.com/snakemake/snakemake-wrappers/commit/6aa4a3816eff1f7d475b430beeca669f7bc5dd2e))
* autobump bio/bcftools/view ([#653](https://www.github.com/snakemake/snakemake-wrappers/issues/653)) ([7e67f97](https://www.github.com/snakemake/snakemake-wrappers/commit/7e67f9773951af8d0ade7c3dd7f345fbccc3a5e5))
* autobump bio/bedtools/bamtobed ([#654](https://www.github.com/snakemake/snakemake-wrappers/issues/654)) ([a84d5d4](https://www.github.com/snakemake/snakemake-wrappers/commit/a84d5d4346bb01f8ab6b69c5f860faf743078f67))
* autobump bio/bedtools/complement ([#655](https://www.github.com/snakemake/snakemake-wrappers/issues/655)) ([8c69237](https://www.github.com/snakemake/snakemake-wrappers/commit/8c6923727d8f81b0c6ca208a91753aa0ba560c48))
* autobump bio/bedtools/coveragebed ([#656](https://www.github.com/snakemake/snakemake-wrappers/issues/656)) ([12e7f9f](https://www.github.com/snakemake/snakemake-wrappers/commit/12e7f9fa545f41374c8201f00e2f572d53f211e2))
* autobump bio/bedtools/genomecov ([#657](https://www.github.com/snakemake/snakemake-wrappers/issues/657)) ([db7b0df](https://www.github.com/snakemake/snakemake-wrappers/commit/db7b0dfd8153ad273e90e2594571c1ec46fbec6f))
* autobump bio/bedtools/intersect ([#658](https://www.github.com/snakemake/snakemake-wrappers/issues/658)) ([5be4783](https://www.github.com/snakemake/snakemake-wrappers/commit/5be47839cfc02c7502f061570421748d46106a84))
* autobump bio/bedtools/merge ([#659](https://www.github.com/snakemake/snakemake-wrappers/issues/659)) ([23e0c2f](https://www.github.com/snakemake/snakemake-wrappers/commit/23e0c2f117ed341fc40bdc9cc3f19d00ccf3aba5))
* autobump bio/bedtools/slop ([#660](https://www.github.com/snakemake/snakemake-wrappers/issues/660)) ([1dc9593](https://www.github.com/snakemake/snakemake-wrappers/commit/1dc9593aa77ee1b9eab13053d8597cc38eea4f3e))
* autobump bio/bedtools/sort ([#661](https://www.github.com/snakemake/snakemake-wrappers/issues/661)) ([c19f269](https://www.github.com/snakemake/snakemake-wrappers/commit/c19f2694fd5bc3abfb28c354bef492b805ae10c5))
* autobump bio/benchmark/chm-eval ([#663](https://www.github.com/snakemake/snakemake-wrappers/issues/663)) ([a192bfc](https://www.github.com/snakemake/snakemake-wrappers/commit/a192bfceb691cd62cbbb3217278bf77d2d62aa1d))
* autobump bio/benchmark/chm-eval-sample ([#662](https://www.github.com/snakemake/snakemake-wrappers/issues/662)) ([4c21a14](https://www.github.com/snakemake/snakemake-wrappers/commit/4c21a147e67b882767a03be99c69abba063bd8ec))
* autobump bio/biobambam2/bamsormadup ([#664](https://www.github.com/snakemake/snakemake-wrappers/issues/664)) ([32fa98c](https://www.github.com/snakemake/snakemake-wrappers/commit/32fa98c81967eeabde2ec39c4e77357bcdc5908e))
* autobump bio/bismark/bam2nuc ([#665](https://www.github.com/snakemake/snakemake-wrappers/issues/665)) ([5b29dc2](https://www.github.com/snakemake/snakemake-wrappers/commit/5b29dc264fad580b329eb830ee1565f1a5321e6f))
* autobump bio/bismark/bismark_genome_preparation ([#670](https://www.github.com/snakemake/snakemake-wrappers/issues/670)) ([4099d65](https://www.github.com/snakemake/snakemake-wrappers/commit/4099d656c977092d0c13946875c392735d7fe6d5))
* autobump bio/bismark/bismark_methylation_extractor ([#671](https://www.github.com/snakemake/snakemake-wrappers/issues/671)) ([48993a9](https://www.github.com/snakemake/snakemake-wrappers/commit/48993a9bb55e2af732155df9ae72654cd00d63ff))
* autobump bio/bismark/bismark2report ([#668](https://www.github.com/snakemake/snakemake-wrappers/issues/668)) ([fc9277f](https://www.github.com/snakemake/snakemake-wrappers/commit/fc9277f51ee3fd534e4cfe350e94ea897fb1575c))
* autobump bio/blast/blastn ([#673](https://www.github.com/snakemake/snakemake-wrappers/issues/673)) ([c9cbd1a](https://www.github.com/snakemake/snakemake-wrappers/commit/c9cbd1aaa55def0ede392b24ad70d76fd0ba39ea))
* autobump bio/blast/makeblastdb ([#674](https://www.github.com/snakemake/snakemake-wrappers/issues/674)) ([0e76eab](https://www.github.com/snakemake/snakemake-wrappers/commit/0e76eabb377c90a7d126a72a9a92252eb2784b24))
* autobump bio/bowtie2/align ([#675](https://www.github.com/snakemake/snakemake-wrappers/issues/675)) ([ba0ea38](https://www.github.com/snakemake/snakemake-wrappers/commit/ba0ea38a27015b4a35336e1bc3ee3abf54ebb1dc))
* autobump bio/bowtie2/build ([#676](https://www.github.com/snakemake/snakemake-wrappers/issues/676)) ([3c4915f](https://www.github.com/snakemake/snakemake-wrappers/commit/3c4915f8349948f8da87126ba17a2c2bf334b283))
* autobump bio/bustools/count ([#677](https://www.github.com/snakemake/snakemake-wrappers/issues/677)) ([d60a41e](https://www.github.com/snakemake/snakemake-wrappers/commit/d60a41ea2726b90a8743bacfe41356a1f04e403f))
* autobump bio/bustools/sort ([#678](https://www.github.com/snakemake/snakemake-wrappers/issues/678)) ([9380cc6](https://www.github.com/snakemake/snakemake-wrappers/commit/9380cc69f81ef943fe1210ec2c6c44eebaf0a194))
* autobump bio/bustools/text ([#679](https://www.github.com/snakemake/snakemake-wrappers/issues/679)) ([e423131](https://www.github.com/snakemake/snakemake-wrappers/commit/e4231317e8c8a907d0a423610dd09a9cdf6f3dcd))
* autobump bio/bwa-mem2/mem-samblaster ([#681](https://www.github.com/snakemake/snakemake-wrappers/issues/681)) ([8871969](https://www.github.com/snakemake/snakemake-wrappers/commit/8871969adb3ebd003468b6c87a925cb69d082cad))
* autobump bio/dada2/add-species ([#703](https://www.github.com/snakemake/snakemake-wrappers/issues/703)) ([3296efd](https://www.github.com/snakemake/snakemake-wrappers/commit/3296efd54e266510c57158f6ee0e51379c0c79b0))
* autobump bio/dada2/assign-taxonomy ([#705](https://www.github.com/snakemake/snakemake-wrappers/issues/705)) ([cf0b49e](https://www.github.com/snakemake/snakemake-wrappers/commit/cf0b49ea11380e482e91f8ed4df6aefd0d59b8b6))
* autobump bio/dada2/collapse-nomismatch ([#706](https://www.github.com/snakemake/snakemake-wrappers/issues/706)) ([e314e90](https://www.github.com/snakemake/snakemake-wrappers/commit/e314e90b3e0b19613e04574bf0ec11765c261357))
* autobump bio/gatk/variantannotator ([#762](https://www.github.com/snakemake/snakemake-wrappers/issues/762)) ([4b11881](https://www.github.com/snakemake/snakemake-wrappers/commit/4b118817248b15f3d80d247182ebaf2c305f1ae4))
* autobump bio/hap.py/hap.py ([#713](https://www.github.com/snakemake/snakemake-wrappers/issues/713)) ([a901d87](https://www.github.com/snakemake/snakemake-wrappers/commit/a901d87fdf06ece3a10d074a95bf6dc02d01045c))
* autobump bio/hifiasm ([#602](https://www.github.com/snakemake/snakemake-wrappers/issues/602)) ([24cc310](https://www.github.com/snakemake/snakemake-wrappers/commit/24cc3108a3e10761b9e5ee31f329b382824073c0))
* autobump bio/jannovar ([#604](https://www.github.com/snakemake/snakemake-wrappers/issues/604)) ([dece141](https://www.github.com/snakemake/snakemake-wrappers/commit/dece141bd1a816fbb773e5dd9ab0bea427e5522c))
* autobump bio/mlst ([#609](https://www.github.com/snakemake/snakemake-wrappers/issues/609)) ([a949c78](https://www.github.com/snakemake/snakemake-wrappers/commit/a949c78e18741149540c4e2838367615cce3f635))
* autobump bio/mosdepth ([#610](https://www.github.com/snakemake/snakemake-wrappers/issues/610)) ([1a25a6f](https://www.github.com/snakemake/snakemake-wrappers/commit/1a25a6f5e41242cbc6c6101b4c73cf91fad3568e))
* autobump bio/multiqc ([#611](https://www.github.com/snakemake/snakemake-wrappers/issues/611)) ([7fabb68](https://www.github.com/snakemake/snakemake-wrappers/commit/7fabb6893bbfbb29da877bffeb56071986c130ee))
* autobump bio/nanosim-h ([#613](https://www.github.com/snakemake/snakemake-wrappers/issues/613)) ([b046dd6](https://www.github.com/snakemake/snakemake-wrappers/commit/b046dd6a0e94163cf7dc0f49e952a12c79c02ed0))
* autobump bio/ngs-disambiguate ([#614](https://www.github.com/snakemake/snakemake-wrappers/issues/614)) ([1ff4b77](https://www.github.com/snakemake/snakemake-wrappers/commit/1ff4b77fe51479d3fa3d6f6b17f085160e358d68))
* autobump bio/optitype ([#615](https://www.github.com/snakemake/snakemake-wrappers/issues/615)) ([6c3d720](https://www.github.com/snakemake/snakemake-wrappers/commit/6c3d720644f2d2fee97a4515ac4fa8e3bd6d36c2))
* autobump bio/pear ([#616](https://www.github.com/snakemake/snakemake-wrappers/issues/616)) ([c64a0f1](https://www.github.com/snakemake/snakemake-wrappers/commit/c64a0f13c5d5c2d185b4cf13d6aa353ed60c2bca))
* autobump bio/plass ([#617](https://www.github.com/snakemake/snakemake-wrappers/issues/617)) ([19ffcc6](https://www.github.com/snakemake/snakemake-wrappers/commit/19ffcc6de2ecc2634df8382d0273e142aec9b35a))
* autobump bio/ptrimmer ([#625](https://www.github.com/snakemake/snakemake-wrappers/issues/625)) ([93869a9](https://www.github.com/snakemake/snakemake-wrappers/commit/93869a9a75ca835f13915effa655e50a2d872456))
* autobump bio/quast ([#626](https://www.github.com/snakemake/snakemake-wrappers/issues/626)) ([4a948d3](https://www.github.com/snakemake/snakemake-wrappers/commit/4a948d386fc63d467aba32eb1decdfeb051ae644))
* autobump bio/rasusa ([#627](https://www.github.com/snakemake/snakemake-wrappers/issues/627)) ([ae7393e](https://www.github.com/snakemake/snakemake-wrappers/commit/ae7393ea7e5cde715ec325c7964ef0c8424ebd20))
* autobump bio/razers3 ([#628](https://www.github.com/snakemake/snakemake-wrappers/issues/628)) ([71c4c16](https://www.github.com/snakemake/snakemake-wrappers/commit/71c4c1631401ad8d971dee50cb83d99af6e1ebb0))
* autobump bio/rebaler ([#629](https://www.github.com/snakemake/snakemake-wrappers/issues/629)) ([7822769](https://www.github.com/snakemake/snakemake-wrappers/commit/7822769fd9fd435891090671c438dd2566740dab))
* autobump bio/refgenie ([#630](https://www.github.com/snakemake/snakemake-wrappers/issues/630)) ([caf7da7](https://www.github.com/snakemake/snakemake-wrappers/commit/caf7da7e52512e8d75b19e55e02286088caa65a1))
* autobump bio/shovill ([#632](https://www.github.com/snakemake/snakemake-wrappers/issues/632)) ([62bac99](https://www.github.com/snakemake/snakemake-wrappers/commit/62bac990ae79964832c1c8e7c77dbfd1bc79fa9a))
* autobump bio/snp-mutator ([#633](https://www.github.com/snakemake/snakemake-wrappers/issues/633)) ([444237a](https://www.github.com/snakemake/snakemake-wrappers/commit/444237a13b82d67b65f30fb04413bef2b69716de))
* autobump bio/star/index ([#739](https://www.github.com/snakemake/snakemake-wrappers/issues/739)) ([a2723ec](https://www.github.com/snakemake/snakemake-wrappers/commit/a2723ec97afacd9ec25e85b8644f24c4c9b487f0))
* autobump bio/tximport ([#635](https://www.github.com/snakemake/snakemake-wrappers/issues/635)) ([4dede59](https://www.github.com/snakemake/snakemake-wrappers/commit/4dede59c36b616fd90f034ef11cd7c6d1adf9ba3))
* autobump bio/unicycler ([#636](https://www.github.com/snakemake/snakemake-wrappers/issues/636)) ([8d8c8d7](https://www.github.com/snakemake/snakemake-wrappers/commit/8d8c8d75a0373b0938da03c7fd240635efa52ddd))
* autobump bio/vardict ([#637](https://www.github.com/snakemake/snakemake-wrappers/issues/637)) ([1494755](https://www.github.com/snakemake/snakemake-wrappers/commit/149475514941146857f7730ab9498c86002a72e4))
* autobump bio/vembrane/table ([#763](https://www.github.com/snakemake/snakemake-wrappers/issues/763)) ([a5eded7](https://www.github.com/snakemake/snakemake-wrappers/commit/a5eded7b354776ed65d50cdcd1795c4c7f54766d))
* autobump bio/wgsim ([#638](https://www.github.com/snakemake/snakemake-wrappers/issues/638)) ([77dd163](https://www.github.com/snakemake/snakemake-wrappers/commit/77dd163cdd4ab78648b361ee364198e505edcaf8))
* autobump utils/cairosvg ([#639](https://www.github.com/snakemake/snakemake-wrappers/issues/639)) ([cbb1239](https://www.github.com/snakemake/snakemake-wrappers/commit/cbb1239e34b5dc37e0424cb6ce44180dcd25206d))

### [1.17.5](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.4...v1.17.5) (2022-10-27)


### Performance Improvements

* autobump bio/bcftools/merge ([#647](https://www.github.com/snakemake/snakemake-wrappers/issues/647)) ([56e4237](https://www.github.com/snakemake/snakemake-wrappers/commit/56e4237b87b4ac5ef666bfdd0a3912c38905d65c))
* autobump bio/bismark/bismark ([#666](https://www.github.com/snakemake/snakemake-wrappers/issues/666)) ([94f83e8](https://www.github.com/snakemake/snakemake-wrappers/commit/94f83e82550f963c58b3598fd9d2833b2f355b32))
* autobump bio/bismark/bismark2bedGraph ([#667](https://www.github.com/snakemake/snakemake-wrappers/issues/667)) ([bccafa5](https://www.github.com/snakemake/snakemake-wrappers/commit/bccafa56106d95fa7a92846678da910fe22189a7))
* autobump bio/bismark/bismark2summary ([#669](https://www.github.com/snakemake/snakemake-wrappers/issues/669)) ([1343842](https://www.github.com/snakemake/snakemake-wrappers/commit/134384236432de3171ff37236060b69b0612b32a))
* autobump bio/bwa-mem2/index ([#680](https://www.github.com/snakemake/snakemake-wrappers/issues/680)) ([9644bd9](https://www.github.com/snakemake/snakemake-wrappers/commit/9644bd9b0bc9d885f2d48f69395c5281934ba13e))
* autobump bio/bwa-mem2/mem ([#682](https://www.github.com/snakemake/snakemake-wrappers/issues/682)) ([50f2ba7](https://www.github.com/snakemake/snakemake-wrappers/commit/50f2ba7aa0ca089ab679ca4f37d118552913269a))
* autobump bio/bwa-meme/index ([#683](https://www.github.com/snakemake/snakemake-wrappers/issues/683)) ([39041dd](https://www.github.com/snakemake/snakemake-wrappers/commit/39041dd149618463ed9dbb4b98d6e32c2c47a014))
* autobump bio/bwa-meme/mem ([#684](https://www.github.com/snakemake/snakemake-wrappers/issues/684)) ([595b2d8](https://www.github.com/snakemake/snakemake-wrappers/commit/595b2d8cc3ffb3c5e2c1acc2522f7df1b23b7037))
* autobump bio/bwa/aln ([#685](https://www.github.com/snakemake/snakemake-wrappers/issues/685)) ([8867513](https://www.github.com/snakemake/snakemake-wrappers/commit/8867513de7bee6df1f4f8028ee6cef393d7d5590))
* autobump bio/bwa/index ([#686](https://www.github.com/snakemake/snakemake-wrappers/issues/686)) ([940b7a4](https://www.github.com/snakemake/snakemake-wrappers/commit/940b7a4d78a246b7d13263ce1e4aa98dd9c2769d))
* autobump bio/bwa/mem ([#688](https://www.github.com/snakemake/snakemake-wrappers/issues/688)) ([b087056](https://www.github.com/snakemake/snakemake-wrappers/commit/b087056083a8f45143aaecda7283d27f1b626678))
* autobump bio/bwa/mem-samblaster ([#687](https://www.github.com/snakemake/snakemake-wrappers/issues/687)) ([b8ecfd0](https://www.github.com/snakemake/snakemake-wrappers/commit/b8ecfd01433d8892fbe454752c870b15469d2a39))
* autobump bio/bwa/sampe ([#689](https://www.github.com/snakemake/snakemake-wrappers/issues/689)) ([007c6dd](https://www.github.com/snakemake/snakemake-wrappers/commit/007c6dd9e99c1fbeadd138d024860708045d1c25))
* autobump bio/bwa/samse ([#690](https://www.github.com/snakemake/snakemake-wrappers/issues/690)) ([23c4d2a](https://www.github.com/snakemake/snakemake-wrappers/commit/23c4d2a0144a6981a2c77c7a6b2374d0b66c7a42))
* autobump bio/bwa/samxe ([#701](https://www.github.com/snakemake/snakemake-wrappers/issues/701)) ([fe75619](https://www.github.com/snakemake/snakemake-wrappers/commit/fe756197a3919408fbf4fcb8f7a3920576989bbe))
* autobump bio/dada2/assign-species ([#704](https://www.github.com/snakemake/snakemake-wrappers/issues/704)) ([c196baa](https://www.github.com/snakemake/snakemake-wrappers/commit/c196baa17b65decacf301c600af6cc51d221ffb0))

### [1.17.4](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.3...v1.17.4) (2022-10-25)


### Performance Improvements

* update datavzrd wrapper to 2.6.1 ([4fb483d](https://www.github.com/snakemake/snakemake-wrappers/commit/4fb483dce834d8e7844127778be716a1e7831c58))

### [1.17.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.2...v1.17.3) (2022-10-24)


### Performance Improvements

* update datavzrd wrapper to 2.5.2 ([533c542](https://www.github.com/snakemake/snakemake-wrappers/commit/533c5429faadf6323f4c97ecd43fe844623d9f73))

### [1.17.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.1...v1.17.2) (2022-10-19)


### Bug Fixes

* allow for optional pindel bed files ([#598](https://www.github.com/snakemake/snakemake-wrappers/issues/598)) ([123fd98](https://www.github.com/snakemake/snakemake-wrappers/commit/123fd98bcac86013bbbd59f9eaaa35a94c144ea7))

### [1.17.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.17.0...v1.17.1) (2022-10-18)


### Performance Improvements

* update datavzrd wrapper to version 2.5.1 ([#618](https://www.github.com/snakemake/snakemake-wrappers/issues/618)) ([6fff732](https://www.github.com/snakemake/snakemake-wrappers/commit/6fff73282a72de4692208a5be4d8a62f0bc82cbb))

## [1.17.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.16.0...v1.17.0) (2022-10-13)


### Features

* move pindel region bed files to input ([#594](https://www.github.com/snakemake/snakemake-wrappers/issues/594)) ([8f52877](https://www.github.com/snakemake/snakemake-wrappers/commit/8f52877aeb5d6510e34ebe846a4fbe2d0e9a2458))

## [1.16.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.15.2...v1.16.0) (2022-10-13)


### Features

* bazam wrapper ([#580](https://www.github.com/snakemake/snakemake-wrappers/issues/580)) ([17e58e6](https://www.github.com/snakemake/snakemake-wrappers/commit/17e58e6f254ce429b3b76b841df29b573949e278))


### Bug Fixes

* set RG tag ([#593](https://www.github.com/snakemake/snakemake-wrappers/issues/593)) ([506a083](https://www.github.com/snakemake/snakemake-wrappers/commit/506a08391b56d4b53edda2c6555b9b9d404d4f94))


### Performance Improvements

* autobump bio/deepvariant ([#583](https://www.github.com/snakemake/snakemake-wrappers/issues/583)) ([9b7c4fe](https://www.github.com/snakemake/snakemake-wrappers/commit/9b7c4feec69d05fc7d6286dcdfdc65802cb93317))

### [1.15.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.15.1...v1.15.2) (2022-10-12)


### Performance Improvements

* update bio/adapterremoval/environment.yaml. ([#573](https://www.github.com/snakemake/snakemake-wrappers/issues/573)) ([8cb0391](https://www.github.com/snakemake/snakemake-wrappers/commit/8cb03915ba46d0a7bf186b54882aa23c4b78f7ed))
* update bio/assembly-stats/environment.yaml. ([#575](https://www.github.com/snakemake/snakemake-wrappers/issues/575)) ([2c12db0](https://www.github.com/snakemake/snakemake-wrappers/commit/2c12db04b2afae3e5ac1c56ee36baff66a8aff0e))
* update bio/bellerophon/environment.yaml. ([#576](https://www.github.com/snakemake/snakemake-wrappers/issues/576)) ([fd06157](https://www.github.com/snakemake/snakemake-wrappers/commit/fd06157a4daec8fb6146bccb8925b00d025231e5))
* update bio/bgzip/environment.yaml. ([#577](https://www.github.com/snakemake/snakemake-wrappers/issues/577)) ([36720ca](https://www.github.com/snakemake/snakemake-wrappers/commit/36720ca9a0d2c6093c7b8ebe26e0b78b5e90227b))
* update bio/busco/environment.yaml. ([#581](https://www.github.com/snakemake/snakemake-wrappers/issues/581)) ([9825a5f](https://www.github.com/snakemake/snakemake-wrappers/commit/9825a5f882228f6a663408c21e9647ae31c00e53))
* update bio/clustalo/environment.yaml. ([#582](https://www.github.com/snakemake/snakemake-wrappers/issues/582)) ([dc322c8](https://www.github.com/snakemake/snakemake-wrappers/commit/dc322c898466341a292b06354301f83f51c005cc))
* update bio/delly/environment.yaml. ([#584](https://www.github.com/snakemake/snakemake-wrappers/issues/584)) ([0eb8ebc](https://www.github.com/snakemake/snakemake-wrappers/commit/0eb8ebc51a1f312836c4a3a7d3d2cfc16a4853c8))
* update bio/fastp/environment.yaml. ([#585](https://www.github.com/snakemake/snakemake-wrappers/issues/585)) ([a573035](https://www.github.com/snakemake/snakemake-wrappers/commit/a573035813ba39d6bf47eb3bb9c5c68aecf074e0))
* update bio/fastq_screen/environment.yaml. ([#586](https://www.github.com/snakemake/snakemake-wrappers/issues/586)) ([73a3d45](https://www.github.com/snakemake/snakemake-wrappers/commit/73a3d450ae1d7eff884eae89195758039aadd9c4))
* update bio/fastqc/environment.yaml. ([#587](https://www.github.com/snakemake/snakemake-wrappers/issues/587)) ([9a0b30e](https://www.github.com/snakemake/snakemake-wrappers/commit/9a0b30e8131560d705c35d9a2eb68b986c743812))
* update bio/fasttree/environment.yaml. ([#588](https://www.github.com/snakemake/snakemake-wrappers/issues/588)) ([b9b8a4e](https://www.github.com/snakemake/snakemake-wrappers/commit/b9b8a4e6ada4e3e2fcf6e266d7430ab51ab978eb))
* update bio/filtlong/environment.yaml. ([#589](https://www.github.com/snakemake/snakemake-wrappers/issues/589)) ([3394085](https://www.github.com/snakemake/snakemake-wrappers/commit/33940856b332699f73410b5b49d6b387b817bd1b))
* update bio/freebayes/environment.yaml. ([#590](https://www.github.com/snakemake/snakemake-wrappers/issues/590)) ([17c9581](https://www.github.com/snakemake/snakemake-wrappers/commit/17c95816b6158eb7c2db56bc1b7c257357359441))
* update bio/genefuse/environment.yaml. ([#591](https://www.github.com/snakemake/snakemake-wrappers/issues/591)) ([63c620d](https://www.github.com/snakemake/snakemake-wrappers/commit/63c620d40435fc9306d0c5e63e06c79287e537c8))
* update bio/genomepy/environment.yaml. ([#592](https://www.github.com/snakemake/snakemake-wrappers/issues/592)) ([4cfb29b](https://www.github.com/snakemake/snakemake-wrappers/commit/4cfb29b97770555af53b16523b14b033d0a1f2fb))

### [1.15.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.15.0...v1.15.1) (2022-10-11)


### Performance Improvements

* autobump bio/bcftools/index/environment.yaml ([#570](https://www.github.com/snakemake/snakemake-wrappers/issues/570)) ([bc77e03](https://www.github.com/snakemake/snakemake-wrappers/commit/bc77e037a0a086c1fede8cd54481426001460a13))
* update bio/bcftools/call/environment.yaml. ([#567](https://www.github.com/snakemake/snakemake-wrappers/issues/567)) ([5c4356a](https://www.github.com/snakemake/snakemake-wrappers/commit/5c4356af4a2bcb288f4fe71169f97151df524d52))
* update bio/bcftools/concat/environment.yaml. ([#568](https://www.github.com/snakemake/snakemake-wrappers/issues/568)) ([70685f1](https://www.github.com/snakemake/snakemake-wrappers/commit/70685f12db06ffe17f09aff7ecd258bcff27284a))
* update utils/datavzrd/environment.yaml. ([#566](https://www.github.com/snakemake/snakemake-wrappers/issues/566)) ([a6f4ff8](https://www.github.com/snakemake/snakemake-wrappers/commit/a6f4ff88e1cf9949737de779b0cc8a56d749e374))

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
