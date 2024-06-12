# Changelog

### [3.12.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.12.0...v3.12.1) (2024-06-12)


### Performance Improvements

* Update Datavzrd wrapper ([#2989](https://www.github.com/snakemake/snakemake-wrappers/issues/2989)) ([9ef3b31](https://www.github.com/snakemake/snakemake-wrappers/commit/9ef3b31352370cc5882d9ed34de385e8fea0db8d))
* Update Datavzrd wrapper ([#2991](https://www.github.com/snakemake/snakemake-wrappers/issues/2991)) ([387369c](https://www.github.com/snakemake/snakemake-wrappers/commit/387369cbdb1231f605f9938d8a7f05ecf86a5213))

## [3.12.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.11.0...v3.12.0) (2024-06-07)


### Features

* Support lists in param.region, and fix typo ([#2978](https://www.github.com/snakemake/snakemake-wrappers/issues/2978)) ([1e9e511](https://www.github.com/snakemake/snakemake-wrappers/commit/1e9e511fdf14174c52ae7555fb78e416986503be))


### Performance Improvements

* autobump bio/entrez/efetch ([#2980](https://www.github.com/snakemake/snakemake-wrappers/issues/2980)) ([c3d76eb](https://www.github.com/snakemake/snakemake-wrappers/commit/c3d76ebee2f651ec41fee1035ce13fd52828a4ef))
* autobump bio/kallisto/quant ([#2247](https://www.github.com/snakemake/snakemake-wrappers/issues/2247)) ([11dd11e](https://www.github.com/snakemake/snakemake-wrappers/commit/11dd11e39800b92d1a999e070e38e8759306cce7))
* autobump bio/multiqc ([#2981](https://www.github.com/snakemake/snakemake-wrappers/issues/2981)) ([bf34418](https://www.github.com/snakemake/snakemake-wrappers/commit/bf344183cbef71dd8fe083644c503c5f384cc792))
* autobump bio/ngs-disambiguate ([#2982](https://www.github.com/snakemake/snakemake-wrappers/issues/2982)) ([8cdb584](https://www.github.com/snakemake/snakemake-wrappers/commit/8cdb5846b13fabe820aafea0b77aa9e1807f1e42))
* autobump bio/open-cravat/module ([#2983](https://www.github.com/snakemake/snakemake-wrappers/issues/2983)) ([7942f61](https://www.github.com/snakemake/snakemake-wrappers/commit/7942f61a82e1cbe8572f2652d21e7004a52a1336))
* autobump bio/open-cravat/run ([#2984](https://www.github.com/snakemake/snakemake-wrappers/issues/2984)) ([099d86a](https://www.github.com/snakemake/snakemake-wrappers/commit/099d86a7ddcd9887184071469eac2b3c9ddb43ec))
* autobump bio/spades/metaspades ([#2986](https://www.github.com/snakemake/snakemake-wrappers/issues/2986)) ([6286c02](https://www.github.com/snakemake/snakemake-wrappers/commit/6286c02a4d0dc89122508b172485a7393dfa75ad))

## [3.11.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.10.2...v3.11.0) (2024-05-31)


### Features

* add samtools markdup wrapper ([#2926](https://www.github.com/snakemake/snakemake-wrappers/issues/2926)) ([3c86bae](https://www.github.com/snakemake/snakemake-wrappers/commit/3c86baef4586b596c6c3375336828257e8bb815f))
* Add support for regions file and arbitrary FAI/GZI paths ([#2936](https://www.github.com/snakemake/snakemake-wrappers/issues/2936)) ([445b35f](https://www.github.com/snakemake/snakemake-wrappers/commit/445b35f314f035d8248ca84cb16b273b0e65847c))
* add wrapper to samtools collate ([#2929](https://www.github.com/snakemake/snakemake-wrappers/issues/2929)) ([0c7ae27](https://www.github.com/snakemake/snakemake-wrappers/commit/0c7ae27622e45167b9cc1aaf1be238b0d25429b9))
* All ngsderive subcommands ([#2732](https://www.github.com/snakemake/snakemake-wrappers/issues/2732)) ([847ab1d](https://www.github.com/snakemake/snakemake-wrappers/commit/847ab1d918c09908bcdb40fa3413b6dbc88d4803))
* auto infer run mode ([#2937](https://www.github.com/snakemake/snakemake-wrappers/issues/2937)) ([08bd3cd](https://www.github.com/snakemake/snakemake-wrappers/commit/08bd3cd79243c4c0636f88d229667e58595611bd))
* Goleft indexcov ([#2734](https://www.github.com/snakemake/snakemake-wrappers/issues/2734)) ([ebef6f8](https://www.github.com/snakemake/snakemake-wrappers/commit/ebef6f8259e89d9a06b2264a5d0a34da23d2e84e))


### Bug Fixes

* bamcoverage without effective genome size ([#2941](https://www.github.com/snakemake/snakemake-wrappers/issues/2941)) ([b6ad55f](https://www.github.com/snakemake/snakemake-wrappers/commit/b6ad55f4d2c702ecc904d6b40b4b35b2463c895a))
* issue [#366](https://www.github.com/snakemake/snakemake-wrappers/issues/366) and [#2649](https://www.github.com/snakemake/snakemake-wrappers/issues/2649) ([#2928](https://www.github.com/snakemake/snakemake-wrappers/issues/2928)) ([e10ab57](https://www.github.com/snakemake/snakemake-wrappers/commit/e10ab571a63b36ce1295e50b6f6b7e4742e0beae))
* remove NA string replacement, fixed upstream ([#2940](https://www.github.com/snakemake/snakemake-wrappers/issues/2940)) ([8f4d223](https://www.github.com/snakemake/snakemake-wrappers/commit/8f4d223ec6c1e1e2715708d0532399ede4ed2727))


### Performance Improvements

* autobump bio/bismark/bam2nuc ([#2943](https://www.github.com/snakemake/snakemake-wrappers/issues/2943)) ([9228479](https://www.github.com/snakemake/snakemake-wrappers/commit/9228479896c2410ae6a58849bf59e5f01bc5e712))
* autobump bio/bismark/bismark ([#2948](https://www.github.com/snakemake/snakemake-wrappers/issues/2948)) ([d9abb20](https://www.github.com/snakemake/snakemake-wrappers/commit/d9abb20e0e002d9ec16507d86211b0555a2546ba))
* autobump bio/bismark/bismark_genome_preparation ([#2945](https://www.github.com/snakemake/snakemake-wrappers/issues/2945)) ([899ae0d](https://www.github.com/snakemake/snakemake-wrappers/commit/899ae0d96d04fa56a7ba5989d9dea18be0d3ebc6))
* autobump bio/bismark/bismark_methylation_extractor ([#2944](https://www.github.com/snakemake/snakemake-wrappers/issues/2944)) ([1b232d2](https://www.github.com/snakemake/snakemake-wrappers/commit/1b232d24816a40f75568bec224eff4e164b3f953))
* autobump bio/bismark/bismark2bedGraph ([#2947](https://www.github.com/snakemake/snakemake-wrappers/issues/2947)) ([ab29098](https://www.github.com/snakemake/snakemake-wrappers/commit/ab29098757c3eef17884f198234ec456e19414f9))
* autobump bio/bismark/bismark2report ([#2951](https://www.github.com/snakemake/snakemake-wrappers/issues/2951)) ([13dd155](https://www.github.com/snakemake/snakemake-wrappers/commit/13dd155a20025b8aaaa80ce3747e6822562bb6b1))
* autobump bio/bismark/bismark2summary ([#2946](https://www.github.com/snakemake/snakemake-wrappers/issues/2946)) ([bfb3d30](https://www.github.com/snakemake/snakemake-wrappers/commit/bfb3d305daa519faee4ad4ea7dbd313941f4c128))
* autobump bio/bismark/deduplicate_bismark ([#2950](https://www.github.com/snakemake/snakemake-wrappers/issues/2950)) ([bcf3c06](https://www.github.com/snakemake/snakemake-wrappers/commit/bcf3c06887443dae9749254f0e8d34e30f880b7e))
* autobump bio/bowtie2/align ([#2949](https://www.github.com/snakemake/snakemake-wrappers/issues/2949)) ([6b0593f](https://www.github.com/snakemake/snakemake-wrappers/commit/6b0593facfcae0b9c92cb1f31423426752c0230d))
* autobump bio/bowtie2/build ([#2942](https://www.github.com/snakemake/snakemake-wrappers/issues/2942)) ([5b3ca20](https://www.github.com/snakemake/snakemake-wrappers/commit/5b3ca20635bd0e427a548e68cd8a40fdb0047f10))
* autobump bio/bwa-mem2/mem-samblaster ([#2962](https://www.github.com/snakemake/snakemake-wrappers/issues/2962)) ([ff613f3](https://www.github.com/snakemake/snakemake-wrappers/commit/ff613f37f857f23d19e4dc0cace22b02113a7e07))
* autobump bio/bwa/mem-samblaster ([#2961](https://www.github.com/snakemake/snakemake-wrappers/issues/2961)) ([83754dd](https://www.github.com/snakemake/snakemake-wrappers/commit/83754dd9f158ea978faa1ed33668a6dda648cdb7))
* autobump bio/fastq_screen ([#2952](https://www.github.com/snakemake/snakemake-wrappers/issues/2952)) ([e45fcac](https://www.github.com/snakemake/snakemake-wrappers/commit/e45fcac221ef45f345a516bff905a53c864e7355))
* autobump bio/freebayes ([#2963](https://www.github.com/snakemake/snakemake-wrappers/issues/2963)) ([7a0d553](https://www.github.com/snakemake/snakemake-wrappers/commit/7a0d553e09921cebc77b54d314c211b91099f7bd))
* autobump bio/gatk/applybqsr ([#2938](https://www.github.com/snakemake/snakemake-wrappers/issues/2938)) ([498c67f](https://www.github.com/snakemake/snakemake-wrappers/commit/498c67fb12691b0021a7b234dfc279957b46708c))
* autobump bio/gatk3/realignertargetcreator ([#2931](https://www.github.com/snakemake/snakemake-wrappers/issues/2931)) ([2d2835c](https://www.github.com/snakemake/snakemake-wrappers/commit/2d2835c51f974f7f45420f832b8084520d2d3ec0))
* autobump bio/gdc-api/bam-slicing ([#2954](https://www.github.com/snakemake/snakemake-wrappers/issues/2954)) ([32d25c1](https://www.github.com/snakemake/snakemake-wrappers/commit/32d25c1560b4c581694c49dc6d3a596e5ca581ab))
* autobump bio/goleft/indexcov ([#2930](https://www.github.com/snakemake/snakemake-wrappers/issues/2930)) ([5ccbdb0](https://www.github.com/snakemake/snakemake-wrappers/commit/5ccbdb078a835ad0c2fd3e9e63677103fe216eeb))
* autobump bio/gseapy/gsea ([#2953](https://www.github.com/snakemake/snakemake-wrappers/issues/2953)) ([dda3d16](https://www.github.com/snakemake/snakemake-wrappers/commit/dda3d16c9b49145bd58d287db1021c41d5a24710))
* autobump bio/hifiasm ([#2932](https://www.github.com/snakemake/snakemake-wrappers/issues/2932)) ([3722de7](https://www.github.com/snakemake/snakemake-wrappers/commit/3722de7000d0b74a3c56bfdb27aad6cf318562ee))
* autobump bio/multiqc ([#2955](https://www.github.com/snakemake/snakemake-wrappers/issues/2955)) ([91ad107](https://www.github.com/snakemake/snakemake-wrappers/commit/91ad1079fa03b07f8ebb9ebf21fe92d21c8a3c13))
* autobump bio/ngsderive ([#2964](https://www.github.com/snakemake/snakemake-wrappers/issues/2964)) ([df82b38](https://www.github.com/snakemake/snakemake-wrappers/commit/df82b381a49b7810087f73b7c83db4fff6d57b66))
* autobump bio/open-cravat/module ([#2966](https://www.github.com/snakemake/snakemake-wrappers/issues/2966)) ([f1ffa3e](https://www.github.com/snakemake/snakemake-wrappers/commit/f1ffa3eee366cba828314cc9a368ba69f17d98c2))
* autobump bio/open-cravat/run ([#2965](https://www.github.com/snakemake/snakemake-wrappers/issues/2965)) ([9b371ca](https://www.github.com/snakemake/snakemake-wrappers/commit/9b371ca6014a38cf23e78598638e4c709a5e82af))
* autobump bio/ptrimmer ([#2933](https://www.github.com/snakemake/snakemake-wrappers/issues/2933)) ([cd37e0b](https://www.github.com/snakemake/snakemake-wrappers/commit/cd37e0bb19e341ad40560828f3c052ef69529088))
* autobump bio/rasusa ([#2967](https://www.github.com/snakemake/snakemake-wrappers/issues/2967)) ([9f25643](https://www.github.com/snakemake/snakemake-wrappers/commit/9f2564323429bea84dfb0b01a5b9f53b37fa397c))
* autobump bio/rbt/csvreport ([#2956](https://www.github.com/snakemake/snakemake-wrappers/issues/2956)) ([b2a469d](https://www.github.com/snakemake/snakemake-wrappers/commit/b2a469dc907c8f3761399affd29ca53f012cc3ee))
* autobump bio/sambamba/flagstat ([#2973](https://www.github.com/snakemake/snakemake-wrappers/issues/2973)) ([4575792](https://www.github.com/snakemake/snakemake-wrappers/commit/4575792deb144dd80401d46bc2fb72175976305a))
* autobump bio/sambamba/index ([#2971](https://www.github.com/snakemake/snakemake-wrappers/issues/2971)) ([18359ac](https://www.github.com/snakemake/snakemake-wrappers/commit/18359ac437bb9f1065c703b3bf2da1d3da9548be))
* autobump bio/sambamba/markdup ([#2968](https://www.github.com/snakemake/snakemake-wrappers/issues/2968)) ([191542d](https://www.github.com/snakemake/snakemake-wrappers/commit/191542d475853f6f19495e136e105970928a9fd8))
* autobump bio/sambamba/merge ([#2975](https://www.github.com/snakemake/snakemake-wrappers/issues/2975)) ([adf9a28](https://www.github.com/snakemake/snakemake-wrappers/commit/adf9a28b64f87aec3fa8286f356f44b6bb77561e))
* autobump bio/sambamba/slice ([#2972](https://www.github.com/snakemake/snakemake-wrappers/issues/2972)) ([88ac3f6](https://www.github.com/snakemake/snakemake-wrappers/commit/88ac3f6dfae93606f74ae8c88b6f8b9e2d059a02))
* autobump bio/sambamba/sort ([#2976](https://www.github.com/snakemake/snakemake-wrappers/issues/2976)) ([990e841](https://www.github.com/snakemake/snakemake-wrappers/commit/990e8416b730267a65ba5a97b71537655bbfe6db))
* autobump bio/sambamba/view ([#2970](https://www.github.com/snakemake/snakemake-wrappers/issues/2970)) ([613e55d](https://www.github.com/snakemake/snakemake-wrappers/commit/613e55d915215348651e878fe37f6533e6d77363))
* autobump bio/seqkit ([#2969](https://www.github.com/snakemake/snakemake-wrappers/issues/2969)) ([e25b840](https://www.github.com/snakemake/snakemake-wrappers/commit/e25b8409af3cc9e591b5106f1ebb00289f628207))
* autobump bio/sra-tools/fasterq-dump ([#2974](https://www.github.com/snakemake/snakemake-wrappers/issues/2974)) ([d8b4b5f](https://www.github.com/snakemake/snakemake-wrappers/commit/d8b4b5fab114c66bf712ee271b00f831a5ed558d))
* autobump bio/unicycler ([#2957](https://www.github.com/snakemake/snakemake-wrappers/issues/2957)) ([185ce7e](https://www.github.com/snakemake/snakemake-wrappers/commit/185ce7e4bd6adbdf840effa665f62e358865c8b8))
* autobump bio/vep/annotate ([#2958](https://www.github.com/snakemake/snakemake-wrappers/issues/2958)) ([728658d](https://www.github.com/snakemake/snakemake-wrappers/commit/728658d5fae40ea784f7b8d3c567c4f7240ef7c7))
* autobump bio/vep/cache ([#2959](https://www.github.com/snakemake/snakemake-wrappers/issues/2959)) ([f4e5b66](https://www.github.com/snakemake/snakemake-wrappers/commit/f4e5b66f8765d09d51d4a640d2d775d781c3018f))
* autobump bio/whatshap/haplotag ([#2934](https://www.github.com/snakemake/snakemake-wrappers/issues/2934)) ([f0b638a](https://www.github.com/snakemake/snakemake-wrappers/commit/f0b638a55280c0727ccef5aab24e03b3d565f290))
* Update Datavzrd to 2.36.12 ([#2924](https://www.github.com/snakemake/snakemake-wrappers/issues/2924)) ([beb9d22](https://www.github.com/snakemake/snakemake-wrappers/commit/beb9d2231c5d59ba74f23f56bbfc5e004aa72331))
* Use samtools collate in fastq separate wrapper ([#2960](https://www.github.com/snakemake/snakemake-wrappers/issues/2960)) ([9c8cf81](https://www.github.com/snakemake/snakemake-wrappers/commit/9c8cf81c1894fc019ffbf0f906eb88e0960c3e7d))

### [3.10.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.10.1...v3.10.2) (2024-05-03)


### Performance Improvements

* autobump bio/gatk3/baserecalibrator ([#2919](https://www.github.com/snakemake/snakemake-wrappers/issues/2919)) ([aae9a13](https://www.github.com/snakemake/snakemake-wrappers/commit/aae9a137a117fb920a6b0817b8bf03016004abc8))
* autobump bio/mosdepth ([#2921](https://www.github.com/snakemake/snakemake-wrappers/issues/2921)) ([57c47b1](https://www.github.com/snakemake/snakemake-wrappers/commit/57c47b1b0f40a78f40f598f6475cb672e1d49192))
* autobump bio/ucsc/gtfToGenePred ([#2922](https://www.github.com/snakemake/snakemake-wrappers/issues/2922)) ([739ce2a](https://www.github.com/snakemake/snakemake-wrappers/commit/739ce2a4033f8c025f4db31eb3f8da2b4841b632))
* autobump bio/vsearch ([#2923](https://www.github.com/snakemake/snakemake-wrappers/issues/2923)) ([e3beaeb](https://www.github.com/snakemake/snakemake-wrappers/commit/e3beaeba734be08f3be28d80ebc00e34ca9a6b7d))

### [3.10.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.10.0...v3.10.1) (2024-05-02)


### Bug Fixes

* allow input access in config rendering for datavzrd ([#2917](https://www.github.com/snakemake/snakemake-wrappers/issues/2917)) ([167ed76](https://www.github.com/snakemake/snakemake-wrappers/commit/167ed764a5f5f5751bf84f91866994b74fbee56b))

## [3.10.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.9.0...v3.10.0) (2024-05-02)


### Features

* Add wrapper for filtering TTree in ROOT ([#2900](https://www.github.com/snakemake/snakemake-wrappers/issues/2900)) ([c294552](https://www.github.com/snakemake/snakemake-wrappers/commit/c294552aa6b19b2cbdda4c650af47f1b83733b32))
* enable YTE templating in datavzrd config file ([#2916](https://www.github.com/snakemake/snakemake-wrappers/issues/2916)) ([97262a5](https://www.github.com/snakemake/snakemake-wrappers/commit/97262a50efe2293b473f02b6761c4f95e0aa35a3))


### Performance Improvements

* autobump bio/cooltools/dots ([#2908](https://www.github.com/snakemake/snakemake-wrappers/issues/2908)) ([7f53f54](https://www.github.com/snakemake/snakemake-wrappers/commit/7f53f54a96802e6ef1a401bbb5b4c25bc9611491))
* autobump bio/cooltools/eigs_cis ([#2904](https://www.github.com/snakemake/snakemake-wrappers/issues/2904)) ([efe1887](https://www.github.com/snakemake/snakemake-wrappers/commit/efe18871eea04b55f8c921fb0ff19ef896c0dfb2))
* autobump bio/cooltools/eigs_trans ([#2903](https://www.github.com/snakemake/snakemake-wrappers/issues/2903)) ([843e331](https://www.github.com/snakemake/snakemake-wrappers/commit/843e331b929bcf72d7be161c457f8541a6cd66d2))
* autobump bio/cooltools/expected_cis ([#2902](https://www.github.com/snakemake/snakemake-wrappers/issues/2902)) ([c9ef619](https://www.github.com/snakemake/snakemake-wrappers/commit/c9ef619b858f59d4532e0df16fd9a6909019ea7c))
* autobump bio/cooltools/expected_trans ([#2909](https://www.github.com/snakemake/snakemake-wrappers/issues/2909)) ([91d92d1](https://www.github.com/snakemake/snakemake-wrappers/commit/91d92d1b9dc0016fecf1dbd03615de116e388cc1))
* autobump bio/cooltools/insulation ([#2906](https://www.github.com/snakemake/snakemake-wrappers/issues/2906)) ([f51323a](https://www.github.com/snakemake/snakemake-wrappers/commit/f51323afd11f6a3310862cee1542fb6776272f98))
* autobump bio/cooltools/pileup ([#2905](https://www.github.com/snakemake/snakemake-wrappers/issues/2905)) ([6aa0897](https://www.github.com/snakemake/snakemake-wrappers/commit/6aa089798d3e8e4b80ce96d8e1f3ccc349c20b46))
* autobump bio/cooltools/saddle ([#2907](https://www.github.com/snakemake/snakemake-wrappers/issues/2907)) ([925f413](https://www.github.com/snakemake/snakemake-wrappers/commit/925f413403ba2d970f003cd8d6ddfdbf29d6c624))
* autobump bio/gatk/applybqsrspark ([#2911](https://www.github.com/snakemake/snakemake-wrappers/issues/2911)) ([cbe905b](https://www.github.com/snakemake/snakemake-wrappers/commit/cbe905b271568c52bbaa687ee101d15b29ef4164))
* autobump bio/gatk3/indelrealigner ([#2910](https://www.github.com/snakemake/snakemake-wrappers/issues/2910)) ([40aa8f1](https://www.github.com/snakemake/snakemake-wrappers/commit/40aa8f1794a46b9285cf88d93451be88d83c67e6))
* autobump bio/mapdamage2 ([#2912](https://www.github.com/snakemake/snakemake-wrappers/issues/2912)) ([ea1bfbd](https://www.github.com/snakemake/snakemake-wrappers/commit/ea1bfbd33ba026022a7364903aaa42983b03f3ab))
* autobump bio/open-cravat/module ([#2913](https://www.github.com/snakemake/snakemake-wrappers/issues/2913)) ([593839d](https://www.github.com/snakemake/snakemake-wrappers/commit/593839d30d39f9c08721ac373d22721a8017b66a))
* autobump bio/open-cravat/run ([#2914](https://www.github.com/snakemake/snakemake-wrappers/issues/2914)) ([476823b](https://www.github.com/snakemake/snakemake-wrappers/commit/476823bfb83184116639be0a62bc47540255f6b3))
* Update Datavzrd to 2.36.10 ([#2915](https://www.github.com/snakemake/snakemake-wrappers/issues/2915)) ([c0a7ddf](https://www.github.com/snakemake/snakemake-wrappers/commit/c0a7ddff4bd0cc827e7c143e7e0dbf5f13f2e148))

## [3.9.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.8.0...v3.9.0) (2024-04-22)


### Features

* Add wrapper for defining columns in TTree in ROOT ([#2898](https://www.github.com/snakemake/snakemake-wrappers/issues/2898)) ([48730cd](https://www.github.com/snakemake/snakemake-wrappers/commit/48730cddcfb8035a927ee65912c0bda0f88f5ae5))
* Emu support ([#2792](https://www.github.com/snakemake/snakemake-wrappers/issues/2792)) ([149ef14](https://www.github.com/snakemake/snakemake-wrappers/commit/149ef14dca9d836d297c95cd4e010c360375f51d))


### Bug Fixes

* deeptools bamcoverage fix ([#2719](https://www.github.com/snakemake/snakemake-wrappers/issues/2719)) ([206425b](https://www.github.com/snakemake/snakemake-wrappers/commit/206425b0de89ce97fadd7f4a5af89f4c401470cb))
* empty emu combined output ([#2899](https://www.github.com/snakemake/snakemake-wrappers/issues/2899)) ([7b10806](https://www.github.com/snakemake/snakemake-wrappers/commit/7b10806933d735251039fc3e89193e82bb86d936))


### Performance Improvements

* autobump bio/bcftools/call ([#2828](https://www.github.com/snakemake/snakemake-wrappers/issues/2828)) ([cd25cc8](https://www.github.com/snakemake/snakemake-wrappers/commit/cd25cc85f238ebfcdcc01b7c550744e2ecee1e6c))
* autobump bio/bcftools/concat ([#2832](https://www.github.com/snakemake/snakemake-wrappers/issues/2832)) ([785cd77](https://www.github.com/snakemake/snakemake-wrappers/commit/785cd779e9fc4824b232919f33a76e231000713c))
* autobump bio/bcftools/filter ([#2821](https://www.github.com/snakemake/snakemake-wrappers/issues/2821)) ([c4c2315](https://www.github.com/snakemake/snakemake-wrappers/commit/c4c2315fd955fd101d6aee88807d4f5d23409629))
* autobump bio/bcftools/index ([#2829](https://www.github.com/snakemake/snakemake-wrappers/issues/2829)) ([3ea7efb](https://www.github.com/snakemake/snakemake-wrappers/commit/3ea7efbd36bf216a0a9f8af5ed325fe5587ceca3))
* autobump bio/bcftools/merge ([#2827](https://www.github.com/snakemake/snakemake-wrappers/issues/2827)) ([b1aee95](https://www.github.com/snakemake/snakemake-wrappers/commit/b1aee9585c4952b3f24ced6e216c1b9ec5765b82))
* autobump bio/bcftools/mpileup ([#2817](https://www.github.com/snakemake/snakemake-wrappers/issues/2817)) ([9b9c0ea](https://www.github.com/snakemake/snakemake-wrappers/commit/9b9c0ea91bc0ad00fa1d65b1737d3ed8f7ef44fd))
* autobump bio/bcftools/norm ([#2819](https://www.github.com/snakemake/snakemake-wrappers/issues/2819)) ([7126185](https://www.github.com/snakemake/snakemake-wrappers/commit/712618518f313737db725edf53bd19847478ad1a))
* autobump bio/bcftools/reheader ([#2822](https://www.github.com/snakemake/snakemake-wrappers/issues/2822)) ([a77fa02](https://www.github.com/snakemake/snakemake-wrappers/commit/a77fa020ea307926ccde2659d2146c6a9c413d8e))
* autobump bio/bcftools/sort ([#2825](https://www.github.com/snakemake/snakemake-wrappers/issues/2825)) ([7c9bb6d](https://www.github.com/snakemake/snakemake-wrappers/commit/7c9bb6d76a326ab8bfb91c38da4520cb4dfa79b0))
* autobump bio/bcftools/stats ([#2813](https://www.github.com/snakemake/snakemake-wrappers/issues/2813)) ([78e1ed6](https://www.github.com/snakemake/snakemake-wrappers/commit/78e1ed6cb3e9a5682eb05943c01afdc24769012d))
* autobump bio/bcftools/view ([#2837](https://www.github.com/snakemake/snakemake-wrappers/issues/2837)) ([ba4cb3b](https://www.github.com/snakemake/snakemake-wrappers/commit/ba4cb3b8f437916f6c49714c803e6ad9bb07604a))
* autobump bio/bellerophon ([#2834](https://www.github.com/snakemake/snakemake-wrappers/issues/2834)) ([f9c272e](https://www.github.com/snakemake/snakemake-wrappers/commit/f9c272eeb9c0760ef02985ec903a8422733fc8aa))
* autobump bio/benchmark/chm-eval-sample ([#2830](https://www.github.com/snakemake/snakemake-wrappers/issues/2830)) ([9911338](https://www.github.com/snakemake/snakemake-wrappers/commit/9911338baf4d0bcaf0db039195293675c4e0aaac))
* autobump bio/bgzip ([#2839](https://www.github.com/snakemake/snakemake-wrappers/issues/2839)) ([8b1d2d7](https://www.github.com/snakemake/snakemake-wrappers/commit/8b1d2d73c0b509ca71666974245c6b019028d168))
* autobump bio/bismark/bam2nuc ([#2815](https://www.github.com/snakemake/snakemake-wrappers/issues/2815)) ([1462242](https://www.github.com/snakemake/snakemake-wrappers/commit/146224245966bffff9211b808847102e5e481611))
* autobump bio/bismark/bismark ([#2812](https://www.github.com/snakemake/snakemake-wrappers/issues/2812)) ([62ee915](https://www.github.com/snakemake/snakemake-wrappers/commit/62ee9153a45f0ff18e3a6d5464a5ec3309202b0d))
* autobump bio/bismark/bismark_genome_preparation ([#2820](https://www.github.com/snakemake/snakemake-wrappers/issues/2820)) ([108387c](https://www.github.com/snakemake/snakemake-wrappers/commit/108387c294ad2019df29ff91efa1be80619c25b8))
* autobump bio/bismark/bismark_methylation_extractor ([#2814](https://www.github.com/snakemake/snakemake-wrappers/issues/2814)) ([47a2c50](https://www.github.com/snakemake/snakemake-wrappers/commit/47a2c507a7516082ef3d0eab6332d62255cf8980))
* autobump bio/bismark/bismark2bedGraph ([#2831](https://www.github.com/snakemake/snakemake-wrappers/issues/2831)) ([556aadd](https://www.github.com/snakemake/snakemake-wrappers/commit/556aaddc88dc4a0ab8cb5f6daf213e238d86d617))
* autobump bio/bismark/bismark2report ([#2808](https://www.github.com/snakemake/snakemake-wrappers/issues/2808)) ([b788b96](https://www.github.com/snakemake/snakemake-wrappers/commit/b788b963c4964ad862576362639107d3e269b54a))
* autobump bio/bismark/bismark2summary ([#2809](https://www.github.com/snakemake/snakemake-wrappers/issues/2809)) ([ff32047](https://www.github.com/snakemake/snakemake-wrappers/commit/ff320479233c211c11ae2c99a5f7ba583fc538d6))
* autobump bio/bismark/deduplicate_bismark ([#2841](https://www.github.com/snakemake/snakemake-wrappers/issues/2841)) ([d897740](https://www.github.com/snakemake/snakemake-wrappers/commit/d897740f94c32755233351e6d8880499baa450e9))
* autobump bio/bowtie2/align ([#2810](https://www.github.com/snakemake/snakemake-wrappers/issues/2810)) ([f9b273e](https://www.github.com/snakemake/snakemake-wrappers/commit/f9b273ec3d87d317a4c4ad15e6f9c253660c16af))
* autobump bio/bwa-mem2/mem ([#2824](https://www.github.com/snakemake/snakemake-wrappers/issues/2824)) ([a4451ea](https://www.github.com/snakemake/snakemake-wrappers/commit/a4451eae221446e7be759de3409e43ff1857acb3))
* autobump bio/bwa-meme/mem ([#2836](https://www.github.com/snakemake/snakemake-wrappers/issues/2836)) ([7f2a24b](https://www.github.com/snakemake/snakemake-wrappers/commit/7f2a24babbaf0dc6b894b3b412bac4587b8e9127))
* autobump bio/bwa-memx/index ([#2816](https://www.github.com/snakemake/snakemake-wrappers/issues/2816)) ([d218b2b](https://www.github.com/snakemake/snakemake-wrappers/commit/d218b2b4b8569869c4ad0f416e98c28f28f38b9c))
* autobump bio/bwa-memx/mem ([#2826](https://www.github.com/snakemake/snakemake-wrappers/issues/2826)) ([e7baf43](https://www.github.com/snakemake/snakemake-wrappers/commit/e7baf43d02a4e7c8606c2730d584a02508e07244))
* autobump bio/bwa/aln ([#2833](https://www.github.com/snakemake/snakemake-wrappers/issues/2833)) ([b41d0b4](https://www.github.com/snakemake/snakemake-wrappers/commit/b41d0b411e8a3eb5426afde949409d245549d80f))
* autobump bio/bwa/index ([#2838](https://www.github.com/snakemake/snakemake-wrappers/issues/2838)) ([946d5c3](https://www.github.com/snakemake/snakemake-wrappers/commit/946d5c3ebfe32d9c3cf15a6891c2a8f075a2e108))
* autobump bio/bwa/mem ([#2818](https://www.github.com/snakemake/snakemake-wrappers/issues/2818)) ([2d49db7](https://www.github.com/snakemake/snakemake-wrappers/commit/2d49db7de49030835c6a98c78a10e39557606515))
* autobump bio/bwa/mem-samblaster ([#2840](https://www.github.com/snakemake/snakemake-wrappers/issues/2840)) ([0fc7d78](https://www.github.com/snakemake/snakemake-wrappers/commit/0fc7d787ae8467112d8dbaf59ba1e1acf3fe0a1f))
* autobump bio/bwa/sampe ([#2811](https://www.github.com/snakemake/snakemake-wrappers/issues/2811)) ([a6367ba](https://www.github.com/snakemake/snakemake-wrappers/commit/a6367ba49220e1cd2a6b6e260613104d7a7427b2))
* autobump bio/bwa/samse ([#2823](https://www.github.com/snakemake/snakemake-wrappers/issues/2823)) ([6d2b199](https://www.github.com/snakemake/snakemake-wrappers/commit/6d2b19929db4b786afb18111ccb370932a09b226))
* autobump bio/bwa/samxe ([#2835](https://www.github.com/snakemake/snakemake-wrappers/issues/2835)) ([a375c11](https://www.github.com/snakemake/snakemake-wrappers/commit/a375c11180ab2c24c246cd88569e0ecaa067830b))
* autobump bio/cnvkit/antitarget ([#2848](https://www.github.com/snakemake/snakemake-wrappers/issues/2848)) ([91354dc](https://www.github.com/snakemake/snakemake-wrappers/commit/91354dcf037dae7dba3ca5ebb4db270e4c38525e))
* autobump bio/cnvkit/batch ([#2849](https://www.github.com/snakemake/snakemake-wrappers/issues/2849)) ([9fae85d](https://www.github.com/snakemake/snakemake-wrappers/commit/9fae85d27cad290e08c4bb186aed6bda0881ef71))
* autobump bio/cnvkit/call ([#2844](https://www.github.com/snakemake/snakemake-wrappers/issues/2844)) ([5437973](https://www.github.com/snakemake/snakemake-wrappers/commit/54379737d0474daaf982ed98eddad39aaae5446e))
* autobump bio/cnvkit/diagram ([#2846](https://www.github.com/snakemake/snakemake-wrappers/issues/2846)) ([bcfcbed](https://www.github.com/snakemake/snakemake-wrappers/commit/bcfcbed4cfb7134ad676bd0c704d17a75b6d201d))
* autobump bio/cnvkit/export ([#2843](https://www.github.com/snakemake/snakemake-wrappers/issues/2843)) ([c499d71](https://www.github.com/snakemake/snakemake-wrappers/commit/c499d719efb0947bd59134c1bc3f5eb8f76b8fed))
* autobump bio/cnvkit/target ([#2847](https://www.github.com/snakemake/snakemake-wrappers/issues/2847)) ([a41c0a0](https://www.github.com/snakemake/snakemake-wrappers/commit/a41c0a094c367343980265c6155a65fd833dbcf7))
* autobump bio/cutadapt/pe ([#2845](https://www.github.com/snakemake/snakemake-wrappers/issues/2845)) ([77a7990](https://www.github.com/snakemake/snakemake-wrappers/commit/77a79909f8e8e3dbc61e62fe9d6fab6998464219))
* autobump bio/cutadapt/se ([#2842](https://www.github.com/snakemake/snakemake-wrappers/issues/2842)) ([d258f5b](https://www.github.com/snakemake/snakemake-wrappers/commit/d258f5bdcb1ed8b8b3ae0550e864238394384225))
* autobump bio/deeptools/bamcoverage ([#2851](https://www.github.com/snakemake/snakemake-wrappers/issues/2851)) ([35d5649](https://www.github.com/snakemake/snakemake-wrappers/commit/35d5649d2a9bc18bcc321a8338a15c9406d31630))
* autobump bio/delly ([#2850](https://www.github.com/snakemake/snakemake-wrappers/issues/2850)) ([3fa1540](https://www.github.com/snakemake/snakemake-wrappers/commit/3fa154029b46cb4d8ad871a745edcb3e4c420881))
* autobump bio/emu/abundance ([#2853](https://www.github.com/snakemake/snakemake-wrappers/issues/2853)) ([fc3d8b6](https://www.github.com/snakemake/snakemake-wrappers/commit/fc3d8b62712c683938d1c5a7be2c804f78a04958))
* autobump bio/emu/collapse-taxonomy ([#2855](https://www.github.com/snakemake/snakemake-wrappers/issues/2855)) ([2ec61a4](https://www.github.com/snakemake/snakemake-wrappers/commit/2ec61a4f5d4a91d8e27d1125d7c9afa60caf8396))
* autobump bio/emu/combine-outputs ([#2854](https://www.github.com/snakemake/snakemake-wrappers/issues/2854)) ([ce414e9](https://www.github.com/snakemake/snakemake-wrappers/commit/ce414e9ea040fda1b5ceac1afa6f814538b1ff7f))
* autobump bio/encode_fastq_downloader ([#2852](https://www.github.com/snakemake/snakemake-wrappers/issues/2852)) ([b71c6d6](https://www.github.com/snakemake/snakemake-wrappers/commit/b71c6d6e380d8a0839a55c1d6c0ac02221bad4ba))
* autobump bio/freebayes ([#2856](https://www.github.com/snakemake/snakemake-wrappers/issues/2856)) ([6f33607](https://www.github.com/snakemake/snakemake-wrappers/commit/6f33607e04c7e80e2bf4dd693cb72900058f0c6a))
* autobump bio/gatk3/printreads ([#2857](https://www.github.com/snakemake/snakemake-wrappers/issues/2857)) ([e42c565](https://www.github.com/snakemake/snakemake-wrappers/commit/e42c565cfc0fe296ef0be29f0a0e192d36707c3a))
* autobump bio/hisat2/align ([#2858](https://www.github.com/snakemake/snakemake-wrappers/issues/2858)) ([b354fc1](https://www.github.com/snakemake/snakemake-wrappers/commit/b354fc1da877c92dd757e804fe07bb1996514ca4))
* autobump bio/hisat2/index ([#2860](https://www.github.com/snakemake/snakemake-wrappers/issues/2860)) ([5d6bdd1](https://www.github.com/snakemake/snakemake-wrappers/commit/5d6bdd137d0d0f4a3ba2ef27d3c2bd76a58e5f51))
* autobump bio/homer/makeTagDirectory ([#2859](https://www.github.com/snakemake/snakemake-wrappers/issues/2859)) ([b3b9dfd](https://www.github.com/snakemake/snakemake-wrappers/commit/b3b9dfdc8513a9523205c3d84bf71178b52d88d9))
* autobump bio/lofreq/call ([#2861](https://www.github.com/snakemake/snakemake-wrappers/issues/2861)) ([3f66fd1](https://www.github.com/snakemake/snakemake-wrappers/commit/3f66fd18ecb0099ed0f535f677c282ed4e10285a))
* autobump bio/lofreq/indelqual ([#2862](https://www.github.com/snakemake/snakemake-wrappers/issues/2862)) ([736bc9c](https://www.github.com/snakemake/snakemake-wrappers/commit/736bc9cd3af8465df355cbe80806788ea6cf641c))
* autobump bio/minimap2/aligner ([#2863](https://www.github.com/snakemake/snakemake-wrappers/issues/2863)) ([0fdbb99](https://www.github.com/snakemake/snakemake-wrappers/commit/0fdbb99f2588780f34a5c789cfcac8483830584d))
* autobump bio/paladin/align ([#2865](https://www.github.com/snakemake/snakemake-wrappers/issues/2865)) ([50b5c90](https://www.github.com/snakemake/snakemake-wrappers/commit/50b5c9024636f55c0a087853b12cadb6d2ea37d7))
* autobump bio/paladin/index ([#2867](https://www.github.com/snakemake/snakemake-wrappers/issues/2867)) ([9d31d8d](https://www.github.com/snakemake/snakemake-wrappers/commit/9d31d8d3ca7c5643d0b5dd6e407f092e75fdc47c))
* autobump bio/paladin/prepare ([#2866](https://www.github.com/snakemake/snakemake-wrappers/issues/2866)) ([e327ba7](https://www.github.com/snakemake/snakemake-wrappers/commit/e327ba7c3551dca0a2592d840974876d72fb6766))
* autobump bio/picard/markduplicates ([#2864](https://www.github.com/snakemake/snakemake-wrappers/issues/2864)) ([f5ddedc](https://www.github.com/snakemake/snakemake-wrappers/commit/f5ddedccc9a04ce610666ed4e099f07791996509))
* autobump bio/pretext/map ([#2868](https://www.github.com/snakemake/snakemake-wrappers/issues/2868)) ([68ba090](https://www.github.com/snakemake/snakemake-wrappers/commit/68ba0909728a349208b55ac9f818197a35d21995))
* autobump bio/rbt/collapse_reads_to_fragments-bam ([#2870](https://www.github.com/snakemake/snakemake-wrappers/issues/2870)) ([8b36d24](https://www.github.com/snakemake/snakemake-wrappers/commit/8b36d24b7bb6c5f228329dfca6b422b4ab58141b))
* autobump bio/reference/ensembl-variation ([#2869](https://www.github.com/snakemake/snakemake-wrappers/issues/2869)) ([c8df691](https://www.github.com/snakemake/snakemake-wrappers/commit/c8df691a9a210052101e0274cf6612b82292518e))
* autobump bio/samtools/calmd ([#2885](https://www.github.com/snakemake/snakemake-wrappers/issues/2885)) ([031bdfa](https://www.github.com/snakemake/snakemake-wrappers/commit/031bdfa9320abdb04d763b3a51e493bb7b2fdc50))
* autobump bio/samtools/depth ([#2875](https://www.github.com/snakemake/snakemake-wrappers/issues/2875)) ([16a53d6](https://www.github.com/snakemake/snakemake-wrappers/commit/16a53d6fe09439cc17d262b36218c35aabb2aa85))
* autobump bio/samtools/faidx ([#2874](https://www.github.com/snakemake/snakemake-wrappers/issues/2874)) ([6a1b758](https://www.github.com/snakemake/snakemake-wrappers/commit/6a1b758344904c1293215f0a568417ae3f213c34))
* autobump bio/samtools/fastx ([#2884](https://www.github.com/snakemake/snakemake-wrappers/issues/2884)) ([60b6495](https://www.github.com/snakemake/snakemake-wrappers/commit/60b6495e145fc098dab87495eeb1bc82513aedce))
* autobump bio/samtools/fixmate ([#2872](https://www.github.com/snakemake/snakemake-wrappers/issues/2872)) ([6a14082](https://www.github.com/snakemake/snakemake-wrappers/commit/6a14082b7335343f6b920eb148e380f6097ec401))
* autobump bio/samtools/flagstat ([#2880](https://www.github.com/snakemake/snakemake-wrappers/issues/2880)) ([b5b67be](https://www.github.com/snakemake/snakemake-wrappers/commit/b5b67be7ca6cac5433395e6a08d7c40cfd4d5501))
* autobump bio/samtools/idxstats ([#2876](https://www.github.com/snakemake/snakemake-wrappers/issues/2876)) ([1f5f13e](https://www.github.com/snakemake/snakemake-wrappers/commit/1f5f13e2cc31b3a8f548df38c2077ef5971cd19c))
* autobump bio/samtools/index ([#2890](https://www.github.com/snakemake/snakemake-wrappers/issues/2890)) ([f3f5be3](https://www.github.com/snakemake/snakemake-wrappers/commit/f3f5be30759d3a5e3a1fa4a464f423efb5b5a1c0))
* autobump bio/samtools/merge ([#2883](https://www.github.com/snakemake/snakemake-wrappers/issues/2883)) ([162ab43](https://www.github.com/snakemake/snakemake-wrappers/commit/162ab43c5b4eda63ea5d85c071e698156f3f22c4))
* autobump bio/samtools/mpileup ([#2877](https://www.github.com/snakemake/snakemake-wrappers/issues/2877)) ([376b565](https://www.github.com/snakemake/snakemake-wrappers/commit/376b5651e9829480e96c30d228cff2cfb6d71918))
* autobump bio/samtools/sort ([#2886](https://www.github.com/snakemake/snakemake-wrappers/issues/2886)) ([da3cc4c](https://www.github.com/snakemake/snakemake-wrappers/commit/da3cc4c8f259f7e2a59e0118840415f35fde4b20))
* autobump bio/samtools/stats ([#2888](https://www.github.com/snakemake/snakemake-wrappers/issues/2888)) ([5a11e6a](https://www.github.com/snakemake/snakemake-wrappers/commit/5a11e6a752a8fcdf03d4331ac773b399b98c265d))
* autobump bio/samtools/view ([#2878](https://www.github.com/snakemake/snakemake-wrappers/issues/2878)) ([d54caec](https://www.github.com/snakemake/snakemake-wrappers/commit/d54caecdb626b42c0e8c7e8eba7308a80fddf1a9))
* autobump bio/snpeff/annotate ([#2871](https://www.github.com/snakemake/snakemake-wrappers/issues/2871)) ([3732019](https://www.github.com/snakemake/snakemake-wrappers/commit/37320198fe14ccca7db2f90eee7b3f67051e0d52))
* autobump bio/snpeff/download ([#2889](https://www.github.com/snakemake/snakemake-wrappers/issues/2889)) ([6700901](https://www.github.com/snakemake/snakemake-wrappers/commit/6700901b9ce60732fbbf87b843b4145bf73fac36))
* autobump bio/snpsift/annotate ([#2879](https://www.github.com/snakemake/snakemake-wrappers/issues/2879)) ([8b5882d](https://www.github.com/snakemake/snakemake-wrappers/commit/8b5882d8e6ee00f54516de38ee62fbf3b65e22af))
* autobump bio/snpsift/dbnsfp ([#2881](https://www.github.com/snakemake/snakemake-wrappers/issues/2881)) ([af992da](https://www.github.com/snakemake/snakemake-wrappers/commit/af992daef072949309d833ea3edf995aa42a98fb))
* autobump bio/snpsift/genesets ([#2882](https://www.github.com/snakemake/snakemake-wrappers/issues/2882)) ([c58973e](https://www.github.com/snakemake/snakemake-wrappers/commit/c58973e90dc46fb3d92acb249d776c1b053164ed))
* autobump bio/snpsift/gwascat ([#2873](https://www.github.com/snakemake/snakemake-wrappers/issues/2873)) ([bd82454](https://www.github.com/snakemake/snakemake-wrappers/commit/bd82454a3ee003736478461a61f6aca48609909e))
* autobump bio/spades/metaspades ([#2887](https://www.github.com/snakemake/snakemake-wrappers/issues/2887)) ([a678d26](https://www.github.com/snakemake/snakemake-wrappers/commit/a678d26f4e40c1df1c8524bb63085b088b5b9274))
* autobump bio/tabix/index ([#2892](https://www.github.com/snakemake/snakemake-wrappers/issues/2892)) ([91122a4](https://www.github.com/snakemake/snakemake-wrappers/commit/91122a4fba60bd6658d30208207b392d190cf031))
* autobump bio/tabix/query ([#2891](https://www.github.com/snakemake/snakemake-wrappers/issues/2891)) ([67caa45](https://www.github.com/snakemake/snakemake-wrappers/commit/67caa4567fba4e2221a2209792929d05ad4f0a6d))
* autobump bio/umis/bamtag ([#2894](https://www.github.com/snakemake/snakemake-wrappers/issues/2894)) ([50d9fba](https://www.github.com/snakemake/snakemake-wrappers/commit/50d9fba291bba5e26b655b1e9c699ba793cce1b5))
* autobump bio/unicycler ([#2893](https://www.github.com/snakemake/snakemake-wrappers/issues/2893)) ([591095b](https://www.github.com/snakemake/snakemake-wrappers/commit/591095ba04afbfb3051a86d6d144d5a343da5920))
* autobump bio/vep/annotate ([#2896](https://www.github.com/snakemake/snakemake-wrappers/issues/2896)) ([85acb44](https://www.github.com/snakemake/snakemake-wrappers/commit/85acb44c4b787e554fab3aedd864f6db49a333e0))
* autobump bio/vep/cache ([#2897](https://www.github.com/snakemake/snakemake-wrappers/issues/2897)) ([529d832](https://www.github.com/snakemake/snakemake-wrappers/commit/529d832e8613bb5686fea9b3a5c25f83f4eb204d))
* autobump bio/vep/plugins ([#2895](https://www.github.com/snakemake/snakemake-wrappers/issues/2895)) ([e2045c6](https://www.github.com/snakemake/snakemake-wrappers/commit/e2045c6b91eaf5f50b31dcbac37f0e19668e2510))

## [3.8.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.7.0...v3.8.0) (2024-04-12)


### Features

* add fgbio sorting to bwa mem ([#2805](https://www.github.com/snakemake/snakemake-wrappers/issues/2805)) ([af98a55](https://www.github.com/snakemake/snakemake-wrappers/commit/af98a5591bc841b7fc829bcf71b9e4b2ebfe29d0))
* Add wrapper for ROOT hadd ([#2785](https://www.github.com/snakemake/snakemake-wrappers/issues/2785)) ([3e82e9c](https://www.github.com/snakemake/snakemake-wrappers/commit/3e82e9cd8a601d41381a870aee16cbdfb5072459))


### Bug Fixes

* bcftool stats bug ([#2806](https://www.github.com/snakemake/snakemake-wrappers/issues/2806)) ([e7ff82c](https://www.github.com/snakemake/snakemake-wrappers/commit/e7ff82cbe32d7ec8e296be3e21cb0653c3f1095d))


### Performance Improvements

* autobump bio/busco ([#2787](https://www.github.com/snakemake/snakemake-wrappers/issues/2787)) ([ebe243e](https://www.github.com/snakemake/snakemake-wrappers/commit/ebe243e751f40712bf3953a49c95d510b3680f14))
* autobump bio/deeptools/plotfingerprint ([#2776](https://www.github.com/snakemake/snakemake-wrappers/issues/2776)) ([214ea28](https://www.github.com/snakemake/snakemake-wrappers/commit/214ea28825991192f4f5f25b25f554eadfb15ec9))
* autobump bio/deeptools/plotheatmap ([#2788](https://www.github.com/snakemake/snakemake-wrappers/issues/2788)) ([81ee08b](https://www.github.com/snakemake/snakemake-wrappers/commit/81ee08b767737e66f4ef843fa7606d68d082e737))
* autobump bio/ega/fetch ([#2789](https://www.github.com/snakemake/snakemake-wrappers/issues/2789)) ([fd83ecb](https://www.github.com/snakemake/snakemake-wrappers/commit/fd83ecbeed2a36adc1170a41de59ed50202ee2e9))
* autobump bio/freebayes ([#1850](https://www.github.com/snakemake/snakemake-wrappers/issues/1850)) ([795e778](https://www.github.com/snakemake/snakemake-wrappers/commit/795e7781331c4e4bba56f055bc9c27d2b2167955))
* autobump bio/freebayes ([#2790](https://www.github.com/snakemake/snakemake-wrappers/issues/2790)) ([fe5de66](https://www.github.com/snakemake/snakemake-wrappers/commit/fe5de660110c8131d17ee27873a9c7f553133b36))
* autobump bio/gdc-api/bam-slicing ([#2778](https://www.github.com/snakemake/snakemake-wrappers/issues/2778)) ([9375ca8](https://www.github.com/snakemake/snakemake-wrappers/commit/9375ca8c718faf4b789633c5db768d247b59e93a))
* autobump bio/minimap2/aligner ([#2780](https://www.github.com/snakemake/snakemake-wrappers/issues/2780)) ([23fd5a3](https://www.github.com/snakemake/snakemake-wrappers/commit/23fd5a325964c7121ddeb218bad64630675e04db))
* autobump bio/minimap2/index ([#2779](https://www.github.com/snakemake/snakemake-wrappers/issues/2779)) ([8f5d611](https://www.github.com/snakemake/snakemake-wrappers/commit/8f5d61190bb7a711bba55e0c4591a8829e659964))
* autobump bio/plass ([#2791](https://www.github.com/snakemake/snakemake-wrappers/issues/2791)) ([11f34ca](https://www.github.com/snakemake/snakemake-wrappers/commit/11f34cad50399510051025aa157a4541ccb0b0f0))
* autobump bio/rseqc/read_gc ([#2781](https://www.github.com/snakemake/snakemake-wrappers/issues/2781)) ([842998d](https://www.github.com/snakemake/snakemake-wrappers/commit/842998dee3c213a4db315c472a98f5781734b394))
* autobump bio/seqkit ([#2795](https://www.github.com/snakemake/snakemake-wrappers/issues/2795)) ([1b2e7ba](https://www.github.com/snakemake/snakemake-wrappers/commit/1b2e7ba1b1163189cb617257a49f3e7492738f43))
* autobump bio/sourmash/compute ([#2794](https://www.github.com/snakemake/snakemake-wrappers/issues/2794)) ([8a37a3e](https://www.github.com/snakemake/snakemake-wrappers/commit/8a37a3e4fc29e3d63d8aa7d83cd9467382c4906d))
* autobump bio/tabix/query ([#2796](https://www.github.com/snakemake/snakemake-wrappers/issues/2796)) ([e21217e](https://www.github.com/snakemake/snakemake-wrappers/commit/e21217ebc139147e72424cd0a607907a3bf7f613))
* autobump bio/tmb/pytmb ([#2797](https://www.github.com/snakemake/snakemake-wrappers/issues/2797)) ([28ae8a8](https://www.github.com/snakemake/snakemake-wrappers/commit/28ae8a8d199235951617d164394e762b0453ebf9))
* autobump bio/ucsc/gtfToGenePred ([#2782](https://www.github.com/snakemake/snakemake-wrappers/issues/2782)) ([4e8c925](https://www.github.com/snakemake/snakemake-wrappers/commit/4e8c9252995e7ab3773c6dff6aee5e881bb2192f))
* autobump bio/unicycler ([#2316](https://www.github.com/snakemake/snakemake-wrappers/issues/2316)) ([0d1486b](https://www.github.com/snakemake/snakemake-wrappers/commit/0d1486b0b88b0f0077faf7533dc5d8b422e3af4d))
* autobump bio/vembrane/filter ([#2783](https://www.github.com/snakemake/snakemake-wrappers/issues/2783)) ([bb271ab](https://www.github.com/snakemake/snakemake-wrappers/commit/bb271abf6dbce49a9e86b5d299b2be8b0fca6df6))
* autobump bio/vembrane/table ([#2784](https://www.github.com/snakemake/snakemake-wrappers/issues/2784)) ([491d5b6](https://www.github.com/snakemake/snakemake-wrappers/commit/491d5b6273d8b341c1c9a898253ab196598a8b0a))
* autobump bio/vg/construct ([#2798](https://www.github.com/snakemake/snakemake-wrappers/issues/2798)) ([25300e4](https://www.github.com/snakemake/snakemake-wrappers/commit/25300e40f0b37ddc2e2c46534ef678b0a84d41c6))
* autobump bio/vg/ids ([#2804](https://www.github.com/snakemake/snakemake-wrappers/issues/2804)) ([4162ce1](https://www.github.com/snakemake/snakemake-wrappers/commit/4162ce1926b7bb2d5bdfa31315597f18125db791))
* autobump bio/vg/kmers ([#2802](https://www.github.com/snakemake/snakemake-wrappers/issues/2802)) ([9ddb88d](https://www.github.com/snakemake/snakemake-wrappers/commit/9ddb88d768a061b3dd9b3815c838fd5495b721b4))
* autobump bio/vg/merge ([#2800](https://www.github.com/snakemake/snakemake-wrappers/issues/2800)) ([5ba8325](https://www.github.com/snakemake/snakemake-wrappers/commit/5ba8325e54730a42096f29dc286de8fc615ed5ff))
* autobump bio/vg/prune ([#2801](https://www.github.com/snakemake/snakemake-wrappers/issues/2801)) ([2061beb](https://www.github.com/snakemake/snakemake-wrappers/commit/2061beb06a5bbf29ff5e095e1ac5803801a0fa22))
* autobump bio/vg/sim ([#2799](https://www.github.com/snakemake/snakemake-wrappers/issues/2799)) ([dfb0d6b](https://www.github.com/snakemake/snakemake-wrappers/commit/dfb0d6bf4f01bca68e221a08f08ed47fbaa739d4))
* autobump bio/vsearch ([#2803](https://www.github.com/snakemake/snakemake-wrappers/issues/2803)) ([7070607](https://www.github.com/snakemake/snakemake-wrappers/commit/7070607cb4e8bc233a55e20b62a2f019e63c9b00))

## [3.7.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.6.0...v3.7.0) (2024-03-27)


### Features

* pyTMB ([#2739](https://www.github.com/snakemake/snakemake-wrappers/issues/2739)) ([0ffbed9](https://www.github.com/snakemake/snakemake-wrappers/commit/0ffbed9fd49d575b94961eb9e34eb79a47b1fd6f))


### Bug Fixes

* path of .fai file in ensembl-variation wrapper ([#2773](https://www.github.com/snakemake/snakemake-wrappers/issues/2773)) ([af63b5b](https://www.github.com/snakemake/snakemake-wrappers/commit/af63b5b42ca974b2ad00d538d72c23763a7c7407))

## [3.6.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.5.3...v3.6.0) (2024-03-26)


### Features

* Taxonkit wrapper ([#2755](https://www.github.com/snakemake/snakemake-wrappers/issues/2755)) ([576ddb9](https://www.github.com/snakemake/snakemake-wrappers/commit/576ddb92927ad39c94a4e98d272455046b86d8dd))

### [3.5.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.5.2...v3.5.3) (2024-03-22)


### Performance Improvements

* autobump bio/busco ([#2760](https://www.github.com/snakemake/snakemake-wrappers/issues/2760)) ([96a5ee7](https://www.github.com/snakemake/snakemake-wrappers/commit/96a5ee7520a11cdcd12ba207d185e9c8b96d08bd))
* autobump bio/cutadapt/pe ([#2762](https://www.github.com/snakemake/snakemake-wrappers/issues/2762)) ([7326a2b](https://www.github.com/snakemake/snakemake-wrappers/commit/7326a2bf33c043d6aee7da32800379ee17dc597d))
* autobump bio/cutadapt/se ([#2761](https://www.github.com/snakemake/snakemake-wrappers/issues/2761)) ([2df0403](https://www.github.com/snakemake/snakemake-wrappers/commit/2df0403bab61cf8f1d2af89f69143f9b6bf026a2))
* autobump bio/mapdamage2 ([#2765](https://www.github.com/snakemake/snakemake-wrappers/issues/2765)) ([03e2812](https://www.github.com/snakemake/snakemake-wrappers/commit/03e2812979b5b76671bf1beb88c2d79e0b93442c))
* autobump bio/mosdepth ([#2764](https://www.github.com/snakemake/snakemake-wrappers/issues/2764)) ([b8b54ee](https://www.github.com/snakemake/snakemake-wrappers/commit/b8b54eed879416d52dd3b0c6875529559b79c075))
* autobump bio/rseqc/infer_experiment ([#2767](https://www.github.com/snakemake/snakemake-wrappers/issues/2767)) ([dfd6ce4](https://www.github.com/snakemake/snakemake-wrappers/commit/dfd6ce4c25ab9d03dcb130293554aeb1bc6f1351))
* autobump bio/rseqc/read_distribution ([#2766](https://www.github.com/snakemake/snakemake-wrappers/issues/2766)) ([7f32bdf](https://www.github.com/snakemake/snakemake-wrappers/commit/7f32bdfad7987613c74a9bbae03a4821eaf508f0))
* autobump bio/salmon/index ([#2769](https://www.github.com/snakemake/snakemake-wrappers/issues/2769)) ([f27e290](https://www.github.com/snakemake/snakemake-wrappers/commit/f27e290cb6f75dc35216ec8af1799a50f6ec2061))
* autobump bio/salmon/quant ([#2768](https://www.github.com/snakemake/snakemake-wrappers/issues/2768)) ([74e93c2](https://www.github.com/snakemake/snakemake-wrappers/commit/74e93c2393bc25d4ef2a1200878e719d1f9061fb))
* autobump bio/sourmash/compute ([#2770](https://www.github.com/snakemake/snakemake-wrappers/issues/2770)) ([19a8a84](https://www.github.com/snakemake/snakemake-wrappers/commit/19a8a84eb4d79f843e509ec563a353e1e1d82d14))
* autobump utils/csvtk ([#2763](https://www.github.com/snakemake/snakemake-wrappers/issues/2763)) ([d3fc9d3](https://www.github.com/snakemake/snakemake-wrappers/commit/d3fc9d32dff0c140129d4898784e9b3dbf921e33))
* Update Datavzrd to 2.36.9 ([#2758](https://www.github.com/snakemake/snakemake-wrappers/issues/2758)) ([efb4337](https://www.github.com/snakemake/snakemake-wrappers/commit/efb4337cc03ed1a1e1f118a526f484895c08c37f))

### [3.5.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.5.1...v3.5.2) (2024-03-18)


### Bug Fixes

* output file handling in ensembl-variation wrapper in combination with remote storage or absolute output file paths ([#2753](https://www.github.com/snakemake/snakemake-wrappers/issues/2753)) ([5bbb7b2](https://www.github.com/snakemake/snakemake-wrappers/commit/5bbb7b2751b8e1eb194e9729209becea00240917))

### [3.5.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.5.0...v3.5.1) (2024-03-15)


### Performance Improvements

* autobump bio/deeptools/alignmentsieve ([#2741](https://www.github.com/snakemake/snakemake-wrappers/issues/2741)) ([ce63735](https://www.github.com/snakemake/snakemake-wrappers/commit/ce63735a1f6e70e14a5217d7e5c5bcc71f62a188))
* autobump bio/deeptools/computematrix ([#2740](https://www.github.com/snakemake/snakemake-wrappers/issues/2740)) ([c3416a0](https://www.github.com/snakemake/snakemake-wrappers/commit/c3416a077b5912f8ba558fbdb239462655d15c68))
* autobump bio/deeptools/plotcoverage ([#2742](https://www.github.com/snakemake/snakemake-wrappers/issues/2742)) ([ec1b4e3](https://www.github.com/snakemake/snakemake-wrappers/commit/ec1b4e3cbeb41b9093e05dffb9349cf255ca1267))
* autobump bio/deeptools/plotprofile ([#2743](https://www.github.com/snakemake/snakemake-wrappers/issues/2743)) ([1773265](https://www.github.com/snakemake/snakemake-wrappers/commit/17732650991fca92c5ce951256633aea42e78f29))
* autobump bio/entrez/efetch ([#2745](https://www.github.com/snakemake/snakemake-wrappers/issues/2745)) ([43deba3](https://www.github.com/snakemake/snakemake-wrappers/commit/43deba38c7a435248a90520be123a07f7b5b52de))
* autobump bio/fgbio/setmateinformation ([#2746](https://www.github.com/snakemake/snakemake-wrappers/issues/2746)) ([6768125](https://www.github.com/snakemake/snakemake-wrappers/commit/67681250618c1d87473ca78189661a1c4ec4ae3f))
* autobump bio/gatk/genotypegvcfs ([#2747](https://www.github.com/snakemake/snakemake-wrappers/issues/2747)) ([37c7361](https://www.github.com/snakemake/snakemake-wrappers/commit/37c7361b9ba43b47cc8e9b48926eeb5eabf9990e))
* autobump bio/minimap2/aligner ([#2748](https://www.github.com/snakemake/snakemake-wrappers/issues/2748)) ([04eca33](https://www.github.com/snakemake/snakemake-wrappers/commit/04eca331209859bbf37ccb603432a4927664866b))
* autobump bio/minimap2/index ([#2749](https://www.github.com/snakemake/snakemake-wrappers/issues/2749)) ([60aac91](https://www.github.com/snakemake/snakemake-wrappers/commit/60aac91acb6a02940a9f7b2ea982ecc10194548a))
* autobump bio/rseqc/read_duplication ([#2750](https://www.github.com/snakemake/snakemake-wrappers/issues/2750)) ([78f15d1](https://www.github.com/snakemake/snakemake-wrappers/commit/78f15d197aa2085f9b3360379bfc3122bf284745))
* autobump bio/seqkit ([#2751](https://www.github.com/snakemake/snakemake-wrappers/issues/2751)) ([5a4705e](https://www.github.com/snakemake/snakemake-wrappers/commit/5a4705eeaba0d68ea52152c83ff788cb58cb70d9))
* autobump bio/ucsc/genePredToBed ([#2752](https://www.github.com/snakemake/snakemake-wrappers/issues/2752)) ([72ea812](https://www.github.com/snakemake/snakemake-wrappers/commit/72ea81202dd3981294d01710166aa009f424c9af))

## [3.5.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.4.1...v3.5.0) (2024-03-13)


### Features

* Genepred to bed ([#2726](https://www.github.com/snakemake/snakemake-wrappers/issues/2726)) ([3998574](https://www.github.com/snakemake/snakemake-wrappers/commit/3998574d4c3cc02706ef4056dbb387835755e0f6))
* MultiQC automatically detects configuration from input file(s) ([#2722](https://www.github.com/snakemake/snakemake-wrappers/issues/2722)) ([f61238d](https://www.github.com/snakemake/snakemake-wrappers/commit/f61238d350ba737aae0b2948857d7f50d5f124d7))
* Rseqc distribution ([#2737](https://www.github.com/snakemake/snakemake-wrappers/issues/2737)) ([c732ff0](https://www.github.com/snakemake/snakemake-wrappers/commit/c732ff0c1fc5e139659a65c5b4495c67a1476985))
* Rseqc infer experiment ([#2730](https://www.github.com/snakemake/snakemake-wrappers/issues/2730)) ([c597f2b](https://www.github.com/snakemake/snakemake-wrappers/commit/c597f2b50170ef0f3843624b38beb27f644022cc))
* Rseqc read duplication ([#2731](https://www.github.com/snakemake/snakemake-wrappers/issues/2731)) ([2d5f9e7](https://www.github.com/snakemake/snakemake-wrappers/commit/2d5f9e79b6620cd2bc4627c643b0db846e4d576d))
* Rseqc read gc ([#2729](https://www.github.com/snakemake/snakemake-wrappers/issues/2729)) ([739d809](https://www.github.com/snakemake/snakemake-wrappers/commit/739d809ad6d85a17bc5028a549d1e9e1b5262568))
* run Mutect2 multiple with input bam files  ([#2736](https://www.github.com/snakemake/snakemake-wrappers/issues/2736)) ([7b42689](https://www.github.com/snakemake/snakemake-wrappers/commit/7b426894a935eb071a842176e2449d481edf6d6c))


### Performance Improvements

* autobump bio/gseapy/gsea ([#2727](https://www.github.com/snakemake/snakemake-wrappers/issues/2727)) ([400db30](https://www.github.com/snakemake/snakemake-wrappers/commit/400db30891d291605d7bb9e039937a62aea23107))
* autobump bio/sra-tools/fasterq-dump ([#2728](https://www.github.com/snakemake/snakemake-wrappers/issues/2728)) ([92c9521](https://www.github.com/snakemake/snakemake-wrappers/commit/92c952124f885624e7725b672f8926cfb7386f76))
* Update Datavzrd ([#2735](https://www.github.com/snakemake/snakemake-wrappers/issues/2735)) ([41b562c](https://www.github.com/snakemake/snakemake-wrappers/commit/41b562cf1c387294e7637e46cce66dd2bcb6218e))
* Update Datavzrd to 2.36.4 ([#2720](https://www.github.com/snakemake/snakemake-wrappers/issues/2720)) ([7611d30](https://www.github.com/snakemake/snakemake-wrappers/commit/7611d30950b85360cb91ff2b58895ae788e05c68))
* Update Datavzrd to 2.36.5 ([#2733](https://www.github.com/snakemake/snakemake-wrappers/issues/2733)) ([2fad8a1](https://www.github.com/snakemake/snakemake-wrappers/commit/2fad8a1bdf205033b799ce0048aae5af6c2b57c1))
* Update Datavzrd to 2.36.8 ([#2738](https://www.github.com/snakemake/snakemake-wrappers/issues/2738)) ([8c86447](https://www.github.com/snakemake/snakemake-wrappers/commit/8c86447fde4419e377e7a2c544a330343bbf19ab))

### [3.4.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.4.0...v3.4.1) (2024-03-01)


### Performance Improvements

* autobump bio/gatk/applyvqsr ([#2705](https://www.github.com/snakemake/snakemake-wrappers/issues/2705)) ([8c90ec7](https://www.github.com/snakemake/snakemake-wrappers/commit/8c90ec7dc40e1324bfaf419859362b58254f2184))
* autobump bio/gatk/baserecalibrator ([#2704](https://www.github.com/snakemake/snakemake-wrappers/issues/2704)) ([0d6c664](https://www.github.com/snakemake/snakemake-wrappers/commit/0d6c664161dccc41e93fc2bf7d4aea424f54b2da))
* autobump bio/gatk/collectalleliccounts ([#2699](https://www.github.com/snakemake/snakemake-wrappers/issues/2699)) ([9018e05](https://www.github.com/snakemake/snakemake-wrappers/commit/9018e0565890db75129c9a66dfaba712ae449d81))
* autobump bio/gatk/haplotypecaller ([#2698](https://www.github.com/snakemake/snakemake-wrappers/issues/2698)) ([aa76a60](https://www.github.com/snakemake/snakemake-wrappers/commit/aa76a60ad436010bd578326454d5bb1652ddbbef))
* autobump bio/gatk/intervallisttobed ([#2700](https://www.github.com/snakemake/snakemake-wrappers/issues/2700)) ([3d35d2b](https://www.github.com/snakemake/snakemake-wrappers/commit/3d35d2b6dc1d8f8144fadfe2b46b8af239f23f21))
* autobump bio/gatk/printreadsspark ([#2703](https://www.github.com/snakemake/snakemake-wrappers/issues/2703)) ([a62781c](https://www.github.com/snakemake/snakemake-wrappers/commit/a62781c9ee05979fcb8c1790e06a75422ee7a12d))
* autobump bio/gatk/selectvariants ([#2707](https://www.github.com/snakemake/snakemake-wrappers/issues/2707)) ([9815aa5](https://www.github.com/snakemake/snakemake-wrappers/commit/9815aa571a3704c0edc5e16cbfc349720c48a57e))
* autobump bio/gatk/variantstotable ([#2697](https://www.github.com/snakemake/snakemake-wrappers/issues/2697)) ([0e6c7ef](https://www.github.com/snakemake/snakemake-wrappers/commit/0e6c7ef1248bc2a6a1324cf1dfc55a7e1015f9a3))
* autobump bio/gatk3/baserecalibrator ([#2702](https://www.github.com/snakemake/snakemake-wrappers/issues/2702)) ([90a833a](https://www.github.com/snakemake/snakemake-wrappers/commit/90a833a2997d10bf160ecede87dca2ea390140ad))
* autobump bio/gatk3/indelrealigner ([#2701](https://www.github.com/snakemake/snakemake-wrappers/issues/2701)) ([c13c656](https://www.github.com/snakemake/snakemake-wrappers/commit/c13c65623bd807769d66a55ca150ee1213eeb15d))
* autobump bio/gatk3/realignertargetcreator ([#2706](https://www.github.com/snakemake/snakemake-wrappers/issues/2706)) ([4f3e20b](https://www.github.com/snakemake/snakemake-wrappers/commit/4f3e20b137ae19ed95f8e06c2f8e859a47485487))
* autobump bio/multiqc ([#2708](https://www.github.com/snakemake/snakemake-wrappers/issues/2708)) ([4d60b0f](https://www.github.com/snakemake/snakemake-wrappers/commit/4d60b0fceee00697b088971cc264bc4ad2734855))
* autobump bio/open-cravat/module ([#2709](https://www.github.com/snakemake/snakemake-wrappers/issues/2709)) ([c8ec2ae](https://www.github.com/snakemake/snakemake-wrappers/commit/c8ec2ae4f4b2633ca60d3a083ec2ab46a1f64f62))
* autobump bio/open-cravat/run ([#2710](https://www.github.com/snakemake/snakemake-wrappers/issues/2710)) ([4268a26](https://www.github.com/snakemake/snakemake-wrappers/commit/4268a26087afc343cd6d5323c2e1eb1be89c78e7))
* autobump bio/picard/collectinsertsizemetrics ([#2711](https://www.github.com/snakemake/snakemake-wrappers/issues/2711)) ([a2b2d66](https://www.github.com/snakemake/snakemake-wrappers/commit/a2b2d66b284c4a5a3a471f00f1dc0402c9b8a17c))
* autobump bio/vg/construct ([#2715](https://www.github.com/snakemake/snakemake-wrappers/issues/2715)) ([7b1cde1](https://www.github.com/snakemake/snakemake-wrappers/commit/7b1cde1a0212e650a59147f0792a2df6dc363acd))
* autobump bio/vg/ids ([#2717](https://www.github.com/snakemake/snakemake-wrappers/issues/2717)) ([e7b495b](https://www.github.com/snakemake/snakemake-wrappers/commit/e7b495bb3018959db51c5d5c534113be4bc0c055))
* autobump bio/vg/kmers ([#2716](https://www.github.com/snakemake/snakemake-wrappers/issues/2716)) ([e5d6785](https://www.github.com/snakemake/snakemake-wrappers/commit/e5d67855029f10cb1831566ad8df9d028d131ee1))
* autobump bio/vg/merge ([#2713](https://www.github.com/snakemake/snakemake-wrappers/issues/2713)) ([2609163](https://www.github.com/snakemake/snakemake-wrappers/commit/2609163931f94e960c584f0282002075dd61e23f))
* autobump bio/vg/prune ([#2714](https://www.github.com/snakemake/snakemake-wrappers/issues/2714)) ([3abe763](https://www.github.com/snakemake/snakemake-wrappers/commit/3abe76370555309c2607d449c7f552f4465fd8ce))
* autobump bio/vg/sim ([#2712](https://www.github.com/snakemake/snakemake-wrappers/issues/2712)) ([79dfbef](https://www.github.com/snakemake/snakemake-wrappers/commit/79dfbef6b6d9b902facf8547488b5095b70e0735))
* Update datavzrd to 2.36.2 ([#2694](https://www.github.com/snakemake/snakemake-wrappers/issues/2694)) ([b1ea355](https://www.github.com/snakemake/snakemake-wrappers/commit/b1ea355d3bd25db056e4a96b794769754dc61e3b))
* Update Datavzrd to 2.36.3 ([#2696](https://www.github.com/snakemake/snakemake-wrappers/issues/2696)) ([baa8376](https://www.github.com/snakemake/snakemake-wrappers/commit/baa8376bb89ea08a04323df7eed2e63766547180))

## [3.4.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.7...v3.4.0) (2024-02-27)


### Features

* Add csvtk wrapper ([#2681](https://www.github.com/snakemake/snakemake-wrappers/issues/2681)) ([495053e](https://www.github.com/snakemake/snakemake-wrappers/commit/495053e85732d8c44ef1171447a35eac6fac77b4))
* MultiQC temp folder, specify outdir/filename, infer options, and bump version ([#2639](https://www.github.com/snakemake/snakemake-wrappers/issues/2639)) ([1edbead](https://www.github.com/snakemake/snakemake-wrappers/commit/1edbeadc1513bdd50ccf94309e14a73d4d0345d0))

### [3.3.7](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.6...v3.3.7) (2024-02-27)


### Bug Fixes

* account for memory overhead ([#2648](https://www.github.com/snakemake/snakemake-wrappers/issues/2648)) ([6a05aad](https://www.github.com/snakemake/snakemake-wrappers/commit/6a05aad6066b0f3aadb92e1f7f931c161222b150))


### Performance Improvements

* autobump bio/bbtools ([#2627](https://www.github.com/snakemake/snakemake-wrappers/issues/2627)) ([7f5b520](https://www.github.com/snakemake/snakemake-wrappers/commit/7f5b5209923401ec20fd1a08063821767300b40a))
* autobump bio/diamond/blastp ([#2630](https://www.github.com/snakemake/snakemake-wrappers/issues/2630)) ([3911776](https://www.github.com/snakemake/snakemake-wrappers/commit/39117768d8978f51fade713abf843d970f98c623))
* autobump bio/diamond/blastx ([#2629](https://www.github.com/snakemake/snakemake-wrappers/issues/2629)) ([faf5de8](https://www.github.com/snakemake/snakemake-wrappers/commit/faf5de8da5579e97620f668b6f6ac63dc57cc0b4))
* autobump bio/diamond/makedb ([#2628](https://www.github.com/snakemake/snakemake-wrappers/issues/2628)) ([7ddca67](https://www.github.com/snakemake/snakemake-wrappers/commit/7ddca679c07cc79598f4099ba0f17d3f10a4247f))
* autobump bio/encode_fastq_downloader ([#2682](https://www.github.com/snakemake/snakemake-wrappers/issues/2682)) ([eb4a093](https://www.github.com/snakemake/snakemake-wrappers/commit/eb4a0939a1c6de100d1c1689d8cbb32402c8d328))
* autobump bio/fgbio/collectduplexseqmetrics ([#2631](https://www.github.com/snakemake/snakemake-wrappers/issues/2631)) ([7a58ee9](https://www.github.com/snakemake/snakemake-wrappers/commit/7a58ee99d23d1f75024bf2e12cb82c3e99bdeefc))
* autobump bio/galah ([#2670](https://www.github.com/snakemake/snakemake-wrappers/issues/2670)) ([8972be1](https://www.github.com/snakemake/snakemake-wrappers/commit/8972be1d8625cd2a359088fb41bdec0945030a9e))
* autobump bio/gatk/applybqsr ([#2662](https://www.github.com/snakemake/snakemake-wrappers/issues/2662)) ([2d1ff8e](https://www.github.com/snakemake/snakemake-wrappers/commit/2d1ff8eeb36fd82f33e03149f2205cc795993f85))
* autobump bio/gatk/applybqsrspark ([#2669](https://www.github.com/snakemake/snakemake-wrappers/issues/2669)) ([46a8acd](https://www.github.com/snakemake/snakemake-wrappers/commit/46a8acdff97cef5ff1e064ccedac90ba05659bb6))
* autobump bio/gatk/baserecalibratorspark ([#2651](https://www.github.com/snakemake/snakemake-wrappers/issues/2651)) ([3b4f517](https://www.github.com/snakemake/snakemake-wrappers/commit/3b4f51740d2a5b371789385fbd0ffe307af100f5))
* autobump bio/gatk/calculatecontamination ([#2673](https://www.github.com/snakemake/snakemake-wrappers/issues/2673)) ([056c9a0](https://www.github.com/snakemake/snakemake-wrappers/commit/056c9a0cb2f9198a700c1972d0ab7879a7178cdf))
* autobump bio/gatk/callcopyratiosegments ([#2655](https://www.github.com/snakemake/snakemake-wrappers/issues/2655)) ([b1932ae](https://www.github.com/snakemake/snakemake-wrappers/commit/b1932ae110fd9e52b7a4c782ed72c98636a84fc0))
* autobump bio/gatk/cleansam ([#2660](https://www.github.com/snakemake/snakemake-wrappers/issues/2660)) ([3802099](https://www.github.com/snakemake/snakemake-wrappers/commit/3802099d38708052cef5284bb3ec93d64e362f58))
* autobump bio/gatk/collectreadcounts ([#2666](https://www.github.com/snakemake/snakemake-wrappers/issues/2666)) ([0aa2cce](https://www.github.com/snakemake/snakemake-wrappers/commit/0aa2ccee2a6b763dc4fe83da11ed9827276b34a5))
* autobump bio/gatk/combinegvcfs ([#2686](https://www.github.com/snakemake/snakemake-wrappers/issues/2686)) ([a903745](https://www.github.com/snakemake/snakemake-wrappers/commit/a903745748b38685cfa5c6381abdcfbfce80803e))
* autobump bio/gatk/denoisereadcounts ([#2685](https://www.github.com/snakemake/snakemake-wrappers/issues/2685)) ([1e8498b](https://www.github.com/snakemake/snakemake-wrappers/commit/1e8498b5c7771ea2f7c360abeb640e6caa665db4))
* autobump bio/gatk/depthofcoverage ([#2658](https://www.github.com/snakemake/snakemake-wrappers/issues/2658)) ([1f43492](https://www.github.com/snakemake/snakemake-wrappers/commit/1f434923e7d4c0cc2905b3f6f17e1735577e8631))
* autobump bio/gatk/estimatelibrarycomplexity ([#2650](https://www.github.com/snakemake/snakemake-wrappers/issues/2650)) ([e9395ff](https://www.github.com/snakemake/snakemake-wrappers/commit/e9395ff31acaa58506258905f62582f9db0a55c0))
* autobump bio/gatk/filtermutectcalls ([#2684](https://www.github.com/snakemake/snakemake-wrappers/issues/2684)) ([b239e62](https://www.github.com/snakemake/snakemake-wrappers/commit/b239e62c5d0d67b138d9af77d8318db9e62dd9af))
* autobump bio/gatk/genomicsdbimport ([#2665](https://www.github.com/snakemake/snakemake-wrappers/issues/2665)) ([a38b278](https://www.github.com/snakemake/snakemake-wrappers/commit/a38b278adbb28857b59d25c0acca53daf6e2478f))
* autobump bio/gatk/getpileupsummaries ([#2657](https://www.github.com/snakemake/snakemake-wrappers/issues/2657)) ([7523193](https://www.github.com/snakemake/snakemake-wrappers/commit/75231932739bd97c39814a4b819c119288b6bddb))
* autobump bio/gatk/learnreadorientationmodel ([#2653](https://www.github.com/snakemake/snakemake-wrappers/issues/2653)) ([773e78c](https://www.github.com/snakemake/snakemake-wrappers/commit/773e78c49e9c4f70291f2a98d99852fe347bc244))
* autobump bio/gatk/leftalignandtrimvariants ([#2656](https://www.github.com/snakemake/snakemake-wrappers/issues/2656)) ([183950c](https://www.github.com/snakemake/snakemake-wrappers/commit/183950c6424d223915bca50deba31d5c3423d385))
* autobump bio/gatk/markduplicatesspark ([#2659](https://www.github.com/snakemake/snakemake-wrappers/issues/2659)) ([706cda3](https://www.github.com/snakemake/snakemake-wrappers/commit/706cda3432a12b4a7379edc4f146b2d29919535a))
* autobump bio/gatk/modelsegments ([#2663](https://www.github.com/snakemake/snakemake-wrappers/issues/2663)) ([bc40698](https://www.github.com/snakemake/snakemake-wrappers/commit/bc40698b6a902012a6a1e197eccfd58ec40d7910))
* autobump bio/gatk/mutect ([#2661](https://www.github.com/snakemake/snakemake-wrappers/issues/2661)) ([0e1d98a](https://www.github.com/snakemake/snakemake-wrappers/commit/0e1d98a96fe448279f38e31b871acf2abf5ca47e))
* autobump bio/gatk/scatterintervalsbyns ([#2674](https://www.github.com/snakemake/snakemake-wrappers/issues/2674)) ([e49b027](https://www.github.com/snakemake/snakemake-wrappers/commit/e49b0273bce205a3597ac2709e599c1ce1f18317))
* autobump bio/gatk/splitintervals ([#2667](https://www.github.com/snakemake/snakemake-wrappers/issues/2667)) ([332eed5](https://www.github.com/snakemake/snakemake-wrappers/commit/332eed549c82ef34d150da68e6af5dfd534ae467))
* autobump bio/gatk/splitncigarreads ([#2672](https://www.github.com/snakemake/snakemake-wrappers/issues/2672)) ([dabbc1e](https://www.github.com/snakemake/snakemake-wrappers/commit/dabbc1eec0f5805664a83d08f603a0dcd91407da))
* autobump bio/gatk/variantannotator ([#2664](https://www.github.com/snakemake/snakemake-wrappers/issues/2664)) ([2142589](https://www.github.com/snakemake/snakemake-wrappers/commit/21425891baf75967a8d6c1bb373168ce4e4bec4d))
* autobump bio/gatk/varianteval ([#2654](https://www.github.com/snakemake/snakemake-wrappers/issues/2654)) ([9d4ffea](https://www.github.com/snakemake/snakemake-wrappers/commit/9d4ffea301af15a5829d4f04b649431139475bc8))
* autobump bio/gatk/variantfiltration ([#2668](https://www.github.com/snakemake/snakemake-wrappers/issues/2668)) ([5cf5407](https://www.github.com/snakemake/snakemake-wrappers/commit/5cf54078192852b3de6f853c0a5fff0176dfbae0))
* autobump bio/gatk/variantrecalibrator ([#2652](https://www.github.com/snakemake/snakemake-wrappers/issues/2652)) ([714ae91](https://www.github.com/snakemake/snakemake-wrappers/commit/714ae9130a7ae352443371cab90adc8817ee208c))
* autobump bio/gatk3/printreads ([#2683](https://www.github.com/snakemake/snakemake-wrappers/issues/2683)) ([c15b388](https://www.github.com/snakemake/snakemake-wrappers/commit/c15b3882c12d94a9b5a755dd851e94bbc65eca8f))
* autobump bio/gatk3/realignertargetcreator ([#2671](https://www.github.com/snakemake/snakemake-wrappers/issues/2671)) ([103425a](https://www.github.com/snakemake/snakemake-wrappers/commit/103425a18f9d4f194aa1794803faf5796e95fa54))
* autobump bio/igv-reports ([#2641](https://www.github.com/snakemake/snakemake-wrappers/issues/2641)) ([4bac92e](https://www.github.com/snakemake/snakemake-wrappers/commit/4bac92e374d7a5f977a67cfab0c92f1372e47be1))
* autobump bio/infernal/cmpress ([#2676](https://www.github.com/snakemake/snakemake-wrappers/issues/2676)) ([7e690c7](https://www.github.com/snakemake/snakemake-wrappers/commit/7e690c742c330d8ff195e920f9caf1643bbe1740))
* autobump bio/infernal/cmscan ([#2675](https://www.github.com/snakemake/snakemake-wrappers/issues/2675)) ([89eac39](https://www.github.com/snakemake/snakemake-wrappers/commit/89eac394bf1c2c183f21e734180398cc902b2455))
* autobump bio/jellyfish/count ([#2643](https://www.github.com/snakemake/snakemake-wrappers/issues/2643)) ([68d8bd6](https://www.github.com/snakemake/snakemake-wrappers/commit/68d8bd6d4c2900a872345a99bbb7c27fc3947fee))
* autobump bio/jellyfish/dump ([#2645](https://www.github.com/snakemake/snakemake-wrappers/issues/2645)) ([d3823f8](https://www.github.com/snakemake/snakemake-wrappers/commit/d3823f8b76565881aa3c451d9a781137538196e3))
* autobump bio/jellyfish/histo ([#2642](https://www.github.com/snakemake/snakemake-wrappers/issues/2642)) ([26c3123](https://www.github.com/snakemake/snakemake-wrappers/commit/26c3123627886f23160c55ac2555b186032cd2cf))
* autobump bio/jellyfish/merge ([#2644](https://www.github.com/snakemake/snakemake-wrappers/issues/2644)) ([2acb46b](https://www.github.com/snakemake/snakemake-wrappers/commit/2acb46b008bd2feaebda5c7d3952cf80e66fbc87))
* autobump bio/last/lastal ([#2632](https://www.github.com/snakemake/snakemake-wrappers/issues/2632)) ([0090d1a](https://www.github.com/snakemake/snakemake-wrappers/commit/0090d1a294c8b56738a9377ce420ebea27fab10c))
* autobump bio/last/lastal ([#2646](https://www.github.com/snakemake/snakemake-wrappers/issues/2646)) ([aecf702](https://www.github.com/snakemake/snakemake-wrappers/commit/aecf702f448f8bf449263d20d91518066af7ac69))
* autobump bio/last/lastal ([#2687](https://www.github.com/snakemake/snakemake-wrappers/issues/2687)) ([c252386](https://www.github.com/snakemake/snakemake-wrappers/commit/c25238635182b24f6e4c7fa09e0d8543fa5cb703))
* autobump bio/last/lastdb ([#2633](https://www.github.com/snakemake/snakemake-wrappers/issues/2633)) ([0adfac7](https://www.github.com/snakemake/snakemake-wrappers/commit/0adfac781ccf609b15bb4301a8597d52504d5049))
* autobump bio/last/lastdb ([#2647](https://www.github.com/snakemake/snakemake-wrappers/issues/2647)) ([9797636](https://www.github.com/snakemake/snakemake-wrappers/commit/979763663965ff14a19b8ae41dd744d6687c0dab))
* autobump bio/last/lastdb ([#2688](https://www.github.com/snakemake/snakemake-wrappers/issues/2688)) ([3dec479](https://www.github.com/snakemake/snakemake-wrappers/commit/3dec47921eee6532b0c94ba976c078dd61aae48d))
* autobump bio/multiqc ([#2677](https://www.github.com/snakemake/snakemake-wrappers/issues/2677)) ([197ef10](https://www.github.com/snakemake/snakemake-wrappers/commit/197ef1075a0c3676a0f3482c2b056e35cc8b7faa))
* autobump bio/seqkit ([#2635](https://www.github.com/snakemake/snakemake-wrappers/issues/2635)) ([8ed8105](https://www.github.com/snakemake/snakemake-wrappers/commit/8ed810512db5c7c76348993317320755d500ebe9))
* autobump bio/sourmash/compute ([#2678](https://www.github.com/snakemake/snakemake-wrappers/issues/2678)) ([1ba1a52](https://www.github.com/snakemake/snakemake-wrappers/commit/1ba1a52ebe2a3041178ba5ee93d6b1e0c8ce3d0c))
* autobump bio/spades/metaspades ([#2689](https://www.github.com/snakemake/snakemake-wrappers/issues/2689)) ([35e4c20](https://www.github.com/snakemake/snakemake-wrappers/commit/35e4c20760c9ae51fb46c2041178794d78965fe5))
* autobump bio/star/align ([#2634](https://www.github.com/snakemake/snakemake-wrappers/issues/2634)) ([0cb085a](https://www.github.com/snakemake/snakemake-wrappers/commit/0cb085a0fa6fd8466f0305350190464c8256850d))
* autobump bio/star/index ([#2636](https://www.github.com/snakemake/snakemake-wrappers/issues/2636)) ([e8df2fe](https://www.github.com/snakemake/snakemake-wrappers/commit/e8df2fe9cab9dc52575f771f170f0bdc0827aae0))
* autobump bio/ucsc/gtfToGenePred ([#2679](https://www.github.com/snakemake/snakemake-wrappers/issues/2679)) ([20682f2](https://www.github.com/snakemake/snakemake-wrappers/commit/20682f297038923eda28d5fb08388dbb555298ec))
* autobump bio/vep/cache ([#2690](https://www.github.com/snakemake/snakemake-wrappers/issues/2690)) ([0ea80f3](https://www.github.com/snakemake/snakemake-wrappers/commit/0ea80f342544af0552d99f6eb184eaab4314bc35))
* autobump bio/vep/plugins ([#2691](https://www.github.com/snakemake/snakemake-wrappers/issues/2691)) ([1b0108f](https://www.github.com/snakemake/snakemake-wrappers/commit/1b0108f96b23f50dae124c03b4b6b18e69163a4f))
* autobump bio/whatshap/haplotag ([#2637](https://www.github.com/snakemake/snakemake-wrappers/issues/2637)) ([5705ffc](https://www.github.com/snakemake/snakemake-wrappers/commit/5705ffc957a8d307c42920608d2a0f1e388a24ce))
* Update datavzrd to v2.36.1 ([#2692](https://www.github.com/snakemake/snakemake-wrappers/issues/2692)) ([cba4946](https://www.github.com/snakemake/snakemake-wrappers/commit/cba4946c8bef80ed3633f5b4a67a46ecee21a389))

### [3.3.6](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.5...v3.3.6) (2024-01-26)


### Performance Improvements

* autobump bio/bellerophon ([#2583](https://www.github.com/snakemake/snakemake-wrappers/issues/2583)) ([b0d51ea](https://www.github.com/snakemake/snakemake-wrappers/commit/b0d51ea04bca80802bd45044278084ea695cb367))
* autobump bio/benchmark/chm-eval-sample ([#2581](https://www.github.com/snakemake/snakemake-wrappers/issues/2581)) ([d6d37a2](https://www.github.com/snakemake/snakemake-wrappers/commit/d6d37a247d3dbd87b8a11a838ac882f5f9896fb9))
* autobump bio/bgzip ([#2584](https://www.github.com/snakemake/snakemake-wrappers/issues/2584)) ([f239106](https://www.github.com/snakemake/snakemake-wrappers/commit/f2391060f3a3cd79689202dcdd34fc5a5598ab1f))
* autobump bio/bismark/bam2nuc ([#2566](https://www.github.com/snakemake/snakemake-wrappers/issues/2566)) ([a892f71](https://www.github.com/snakemake/snakemake-wrappers/commit/a892f719e4030d98f7368e9de61fb48115f678a4))
* autobump bio/bismark/bismark ([#2582](https://www.github.com/snakemake/snakemake-wrappers/issues/2582)) ([5cb0282](https://www.github.com/snakemake/snakemake-wrappers/commit/5cb0282d07670f40e08bc5698d36e2d0bce1e170))
* autobump bio/bismark/bismark_genome_preparation ([#2567](https://www.github.com/snakemake/snakemake-wrappers/issues/2567)) ([73059b9](https://www.github.com/snakemake/snakemake-wrappers/commit/73059b979ec2c5f7fc636d63720b0a59ef0f8043))
* autobump bio/bismark/bismark_methylation_extractor ([#2576](https://www.github.com/snakemake/snakemake-wrappers/issues/2576)) ([c97b557](https://www.github.com/snakemake/snakemake-wrappers/commit/c97b5577aea193784c3c36f1847a1a7c6083592a))
* autobump bio/bismark/bismark2bedGraph ([#2575](https://www.github.com/snakemake/snakemake-wrappers/issues/2575)) ([4bbae6a](https://www.github.com/snakemake/snakemake-wrappers/commit/4bbae6a8c6e6a7f512915e83f158fb7fbdd19aa6))
* autobump bio/bismark/bismark2report ([#2572](https://www.github.com/snakemake/snakemake-wrappers/issues/2572)) ([b018012](https://www.github.com/snakemake/snakemake-wrappers/commit/b0180124926a0f315baa51f2414c0fd1489b81ac))
* autobump bio/bismark/bismark2summary ([#2574](https://www.github.com/snakemake/snakemake-wrappers/issues/2574)) ([ab1c8af](https://www.github.com/snakemake/snakemake-wrappers/commit/ab1c8aff530ac803237f1e11aed826e14cd37f6f))
* autobump bio/bismark/deduplicate_bismark ([#2571](https://www.github.com/snakemake/snakemake-wrappers/issues/2571)) ([a3d2e1a](https://www.github.com/snakemake/snakemake-wrappers/commit/a3d2e1a6312e7627c11ac9aa0da6f8056aa77606))
* autobump bio/bowtie2/align ([#2578](https://www.github.com/snakemake/snakemake-wrappers/issues/2578)) ([e9e6d1e](https://www.github.com/snakemake/snakemake-wrappers/commit/e9e6d1eafabca8c18ee88a8282d26caf589d2fe4))
* autobump bio/bwa-mem2/mem ([#2569](https://www.github.com/snakemake/snakemake-wrappers/issues/2569)) ([84ef50c](https://www.github.com/snakemake/snakemake-wrappers/commit/84ef50cf62414d2bc94546bdb17bc6ac04f85d01))
* autobump bio/bwa-meme/mem ([#2579](https://www.github.com/snakemake/snakemake-wrappers/issues/2579)) ([2bc7f68](https://www.github.com/snakemake/snakemake-wrappers/commit/2bc7f686f4cd58c15d33e93cf39e2db5aec0ae21))
* autobump bio/bwa-memx/mem ([#2577](https://www.github.com/snakemake/snakemake-wrappers/issues/2577)) ([c96c94b](https://www.github.com/snakemake/snakemake-wrappers/commit/c96c94be134d994631c4d92fa1b9552a03a73f42))
* autobump bio/bwa/mem ([#2573](https://www.github.com/snakemake/snakemake-wrappers/issues/2573)) ([191155a](https://www.github.com/snakemake/snakemake-wrappers/commit/191155ae70652ec7fbfb815fcdc60516993dec91))
* autobump bio/bwa/sampe ([#2580](https://www.github.com/snakemake/snakemake-wrappers/issues/2580)) ([0115a7c](https://www.github.com/snakemake/snakemake-wrappers/commit/0115a7cb3e4e57aabefacf4795234c967cc71919))
* autobump bio/bwa/samse ([#2568](https://www.github.com/snakemake/snakemake-wrappers/issues/2568)) ([9709ef4](https://www.github.com/snakemake/snakemake-wrappers/commit/9709ef479217fee45be1b07aa0894bbe91de1e17))
* autobump bio/bwa/samxe ([#2570](https://www.github.com/snakemake/snakemake-wrappers/issues/2570)) ([c1bf514](https://www.github.com/snakemake/snakemake-wrappers/commit/c1bf514964a395457ac6b04667c4085b912520b8))
* autobump bio/cnvkit/export ([#2585](https://www.github.com/snakemake/snakemake-wrappers/issues/2585)) ([e213c0f](https://www.github.com/snakemake/snakemake-wrappers/commit/e213c0f7d4e339483bc107af2c6e72ac353fbd48))
* autobump bio/fastq_screen ([#2586](https://www.github.com/snakemake/snakemake-wrappers/issues/2586)) ([bfc9e1d](https://www.github.com/snakemake/snakemake-wrappers/commit/bfc9e1d6550c9d598d31a2a3f25a5d6a2c5f2410))
* autobump bio/gatk/applybqsr ([#2587](https://www.github.com/snakemake/snakemake-wrappers/issues/2587)) ([d2ddd0b](https://www.github.com/snakemake/snakemake-wrappers/commit/d2ddd0b7043246c5fac5873ef486fb24def6af08))
* autobump bio/gatk/applybqsrspark ([#2588](https://www.github.com/snakemake/snakemake-wrappers/issues/2588)) ([b189fab](https://www.github.com/snakemake/snakemake-wrappers/commit/b189fabee088b6f109e730a6b069b24b4ecd8349))
* autobump bio/hisat2/align ([#2590](https://www.github.com/snakemake/snakemake-wrappers/issues/2590)) ([9701b79](https://www.github.com/snakemake/snakemake-wrappers/commit/9701b79649be325e70f9623724a15ce59c293975))
* autobump bio/hisat2/index ([#2589](https://www.github.com/snakemake/snakemake-wrappers/issues/2589)) ([bd7c9cf](https://www.github.com/snakemake/snakemake-wrappers/commit/bd7c9cfdf7a432cb3634838747fdf437eb2bb397))
* autobump bio/homer/makeTagDirectory ([#2591](https://www.github.com/snakemake/snakemake-wrappers/issues/2591)) ([228cc4e](https://www.github.com/snakemake/snakemake-wrappers/commit/228cc4e18d5269a0a345538ed685c4c82d460cf1))
* autobump bio/igv-reports ([#2592](https://www.github.com/snakemake/snakemake-wrappers/issues/2592)) ([b22c843](https://www.github.com/snakemake/snakemake-wrappers/commit/b22c84394fa11f3ec93ca870d1f978e520738513))
* autobump bio/last/lastal ([#2595](https://www.github.com/snakemake/snakemake-wrappers/issues/2595)) ([2148e09](https://www.github.com/snakemake/snakemake-wrappers/commit/2148e093c5f9cc2f01c0334f1e1dc641ee717e3b))
* autobump bio/last/lastdb ([#2594](https://www.github.com/snakemake/snakemake-wrappers/issues/2594)) ([e0d4413](https://www.github.com/snakemake/snakemake-wrappers/commit/e0d44139a751f6bcb90bb23d9d617b28f91d1bc5))
* autobump bio/lofreq/call ([#2596](https://www.github.com/snakemake/snakemake-wrappers/issues/2596)) ([533b0ab](https://www.github.com/snakemake/snakemake-wrappers/commit/533b0ab41ff18a43ed4d28e38ae7f44be380345b))
* autobump bio/lofreq/indelqual ([#2593](https://www.github.com/snakemake/snakemake-wrappers/issues/2593)) ([7741cda](https://www.github.com/snakemake/snakemake-wrappers/commit/7741cda31ad007688aceb4d88139c62f0bba7c89))
* autobump bio/minimap2/aligner ([#2597](https://www.github.com/snakemake/snakemake-wrappers/issues/2597)) ([832d386](https://www.github.com/snakemake/snakemake-wrappers/commit/832d38623c1a32a57f828186ecff6a7c82e8ac48))
* autobump bio/paladin/align ([#2599](https://www.github.com/snakemake/snakemake-wrappers/issues/2599)) ([0537271](https://www.github.com/snakemake/snakemake-wrappers/commit/0537271e0871a825a212872fec34480664113482))
* autobump bio/paladin/index ([#2601](https://www.github.com/snakemake/snakemake-wrappers/issues/2601)) ([b823df4](https://www.github.com/snakemake/snakemake-wrappers/commit/b823df4f90aef363bd4f063f27a86fa297491acb))
* autobump bio/paladin/prepare ([#2600](https://www.github.com/snakemake/snakemake-wrappers/issues/2600)) ([1b08512](https://www.github.com/snakemake/snakemake-wrappers/commit/1b085128d5e81ca152f18e5525ed257781068aa0))
* autobump bio/picard/markduplicates ([#2602](https://www.github.com/snakemake/snakemake-wrappers/issues/2602)) ([3186986](https://www.github.com/snakemake/snakemake-wrappers/commit/3186986a94d1b7c57b1d1b1d301416e928946c92))
* autobump bio/pretext/map ([#2598](https://www.github.com/snakemake/snakemake-wrappers/issues/2598)) ([29de6ab](https://www.github.com/snakemake/snakemake-wrappers/commit/29de6ab2b88d25edb95c9dd3d7c4d39ae61d94b3))
* autobump bio/samtools/calmd ([#2603](https://www.github.com/snakemake/snakemake-wrappers/issues/2603)) ([933e7c5](https://www.github.com/snakemake/snakemake-wrappers/commit/933e7c5b7a68ea702d9a8f86efe2160bd8935916))
* autobump bio/samtools/depth ([#2610](https://www.github.com/snakemake/snakemake-wrappers/issues/2610)) ([94d3b46](https://www.github.com/snakemake/snakemake-wrappers/commit/94d3b46f83db9228a7ad223c8715accefe65b1a6))
* autobump bio/samtools/faidx ([#2608](https://www.github.com/snakemake/snakemake-wrappers/issues/2608)) ([895739f](https://www.github.com/snakemake/snakemake-wrappers/commit/895739fa0921c99cd322d3f6314c36acf3bd9097))
* autobump bio/samtools/fastx ([#2612](https://www.github.com/snakemake/snakemake-wrappers/issues/2612)) ([bc81be6](https://www.github.com/snakemake/snakemake-wrappers/commit/bc81be65ba4c83cadff438a7299f6af22d2cb033))
* autobump bio/samtools/fixmate ([#2614](https://www.github.com/snakemake/snakemake-wrappers/issues/2614)) ([ecb6d9d](https://www.github.com/snakemake/snakemake-wrappers/commit/ecb6d9d3d890575b19d3ebca6b8728c13e52d953))
* autobump bio/samtools/flagstat ([#2615](https://www.github.com/snakemake/snakemake-wrappers/issues/2615)) ([3117a6a](https://www.github.com/snakemake/snakemake-wrappers/commit/3117a6ae0dc900929c8c1a64f9e72a44a1652f6e))
* autobump bio/samtools/idxstats ([#2604](https://www.github.com/snakemake/snakemake-wrappers/issues/2604)) ([bc779d3](https://www.github.com/snakemake/snakemake-wrappers/commit/bc779d344d4121c375785e7b09a6bbb4a04eaaba))
* autobump bio/samtools/index ([#2613](https://www.github.com/snakemake/snakemake-wrappers/issues/2613)) ([8fc34c5](https://www.github.com/snakemake/snakemake-wrappers/commit/8fc34c5ecc97ff72b20ac8b1d50e8d8b08460de5))
* autobump bio/samtools/merge ([#2607](https://www.github.com/snakemake/snakemake-wrappers/issues/2607)) ([6c94a03](https://www.github.com/snakemake/snakemake-wrappers/commit/6c94a0332e72fd0cc58cc477e4dc08155da1c775))
* autobump bio/samtools/mpileup ([#2605](https://www.github.com/snakemake/snakemake-wrappers/issues/2605)) ([6c2cbe5](https://www.github.com/snakemake/snakemake-wrappers/commit/6c2cbe5c498d85af70c6435b70cd08ff60d3d4e2))
* autobump bio/samtools/sort ([#2606](https://www.github.com/snakemake/snakemake-wrappers/issues/2606)) ([23c86ba](https://www.github.com/snakemake/snakemake-wrappers/commit/23c86bae49aefad6079c29eb8473bb26090e75f8))
* autobump bio/samtools/stats ([#2609](https://www.github.com/snakemake/snakemake-wrappers/issues/2609)) ([bdaa3c6](https://www.github.com/snakemake/snakemake-wrappers/commit/bdaa3c6e7a4e24e1d8b9b08611c4c9d31b68e480))
* autobump bio/samtools/view ([#2611](https://www.github.com/snakemake/snakemake-wrappers/issues/2611)) ([b18a52c](https://www.github.com/snakemake/snakemake-wrappers/commit/b18a52c7445d82e95101d10c72fa7bf5b480c111))
* autobump bio/tabix/index ([#2616](https://www.github.com/snakemake/snakemake-wrappers/issues/2616)) ([32bb492](https://www.github.com/snakemake/snakemake-wrappers/commit/32bb4929c686623dce1456007f68f2be1214d633))
* autobump bio/ucsc/bedGraphToBigWig ([#2618](https://www.github.com/snakemake/snakemake-wrappers/issues/2618)) ([a5a6056](https://www.github.com/snakemake/snakemake-wrappers/commit/a5a605691ddc2c87458d43f5a10cd5c8177ddae0))
* autobump bio/ucsc/twoBitInfo ([#2619](https://www.github.com/snakemake/snakemake-wrappers/issues/2619)) ([2b8b6ad](https://www.github.com/snakemake/snakemake-wrappers/commit/2b8b6ad705cf6ee2e457b5ca235b57bedc575dd7))
* autobump bio/umis/bamtag ([#2617](https://www.github.com/snakemake/snakemake-wrappers/issues/2617)) ([15bb341](https://www.github.com/snakemake/snakemake-wrappers/commit/15bb341dca1a625743d28110d16d462700b831cf))
* autobump bio/vg/construct ([#2625](https://www.github.com/snakemake/snakemake-wrappers/issues/2625)) ([a8e1d8b](https://www.github.com/snakemake/snakemake-wrappers/commit/a8e1d8bda4146f7f4705ba9cf9cb32ea4491016d))
* autobump bio/vg/ids ([#2620](https://www.github.com/snakemake/snakemake-wrappers/issues/2620)) ([ef17328](https://www.github.com/snakemake/snakemake-wrappers/commit/ef173288dbbc3a5fda67a529e0abac565af3fe42))
* autobump bio/vg/kmers ([#2624](https://www.github.com/snakemake/snakemake-wrappers/issues/2624)) ([0334cc3](https://www.github.com/snakemake/snakemake-wrappers/commit/0334cc3055ec8220244afe662003596d5483a4c6))
* autobump bio/vg/merge ([#2622](https://www.github.com/snakemake/snakemake-wrappers/issues/2622)) ([d224795](https://www.github.com/snakemake/snakemake-wrappers/commit/d224795638f1cdb80b5597ffe1bafa909dbeaddf))
* autobump bio/vg/prune ([#2621](https://www.github.com/snakemake/snakemake-wrappers/issues/2621)) ([d30b324](https://www.github.com/snakemake/snakemake-wrappers/commit/d30b324c362175a9b607ef3b78f05aa57747cbaf))
* autobump bio/vg/sim ([#2626](https://www.github.com/snakemake/snakemake-wrappers/issues/2626)) ([a2e60d6](https://www.github.com/snakemake/snakemake-wrappers/commit/a2e60d65cd6905319718d9a5f3df8287f4b7843c))
* autobump bio/vsearch ([#2623](https://www.github.com/snakemake/snakemake-wrappers/issues/2623)) ([f1e2f24](https://www.github.com/snakemake/snakemake-wrappers/commit/f1e2f24f067144e9cdeb05a5a7987108d63f0329))
* Update datavzrd to v2.35.4 ([#2564](https://www.github.com/snakemake/snakemake-wrappers/issues/2564)) ([d73914d](https://www.github.com/snakemake/snakemake-wrappers/commit/d73914d68ad0cadcffe0e850bea081a407d0412a))

### [3.3.5](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.4...v3.3.5) (2024-01-23)


### Performance Improvements

* Update datavzrd version to 2.35.3 ([#2562](https://www.github.com/snakemake/snakemake-wrappers/issues/2562)) ([766a490](https://www.github.com/snakemake/snakemake-wrappers/commit/766a490b25acd8d9c6baea8f13837d0b2859ed90))

### [3.3.4](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.3...v3.3.4) (2024-01-19)


### Bug Fixes

* plotting with no model in nonpareil ([#2536](https://www.github.com/snakemake/snakemake-wrappers/issues/2536)) ([1ac6350](https://www.github.com/snakemake/snakemake-wrappers/commit/1ac6350998c590c15ed672ea40b54a3025754bd1))
* test case for reference-ensembl-sequence wrapper ([#2522](https://www.github.com/snakemake/snakemake-wrappers/issues/2522)) ([46bac2e](https://www.github.com/snakemake/snakemake-wrappers/commit/46bac2e06d25da08e7dd5ae0a091e797c96089a7))


### Performance Improvements

* autobump bio/bismark/bam2nuc ([#2551](https://www.github.com/snakemake/snakemake-wrappers/issues/2551)) ([d15ce0b](https://www.github.com/snakemake/snakemake-wrappers/commit/d15ce0bedcbdc892ab2b48294d1d0c4bf7de0ef5))
* autobump bio/bismark/bismark ([#2553](https://www.github.com/snakemake/snakemake-wrappers/issues/2553)) ([8fe6734](https://www.github.com/snakemake/snakemake-wrappers/commit/8fe6734dc29191c5571e6279e3ce322bf8575c27))
* autobump bio/bismark/bismark_genome_preparation ([#2554](https://www.github.com/snakemake/snakemake-wrappers/issues/2554)) ([ab64460](https://www.github.com/snakemake/snakemake-wrappers/commit/ab64460a2aae4674d228dd567c8cefa2999f1dcc))
* autobump bio/bismark/bismark_methylation_extractor ([#2555](https://www.github.com/snakemake/snakemake-wrappers/issues/2555)) ([d468bbf](https://www.github.com/snakemake/snakemake-wrappers/commit/d468bbfad48a5f75c791497394cb0b7fd22e958d))
* autobump bio/bismark/bismark2bedGraph ([#2548](https://www.github.com/snakemake/snakemake-wrappers/issues/2548)) ([708070c](https://www.github.com/snakemake/snakemake-wrappers/commit/708070c77010f0251e7bdc05b002b70aab3ff0cc))
* autobump bio/bismark/bismark2report ([#2550](https://www.github.com/snakemake/snakemake-wrappers/issues/2550)) ([e78cdc4](https://www.github.com/snakemake/snakemake-wrappers/commit/e78cdc45aa506cc616bc280e7cd556bf706bdc2a))
* autobump bio/bismark/bismark2summary ([#2549](https://www.github.com/snakemake/snakemake-wrappers/issues/2549)) ([aeb56e8](https://www.github.com/snakemake/snakemake-wrappers/commit/aeb56e8225300e4ab959347bd1448b4960520459))
* autobump bio/bismark/deduplicate_bismark ([#2547](https://www.github.com/snakemake/snakemake-wrappers/issues/2547)) ([d8cbfba](https://www.github.com/snakemake/snakemake-wrappers/commit/d8cbfba5f91e8960fc5498c2108eba226f62e1ba))
* autobump bio/bowtie2/align ([#2552](https://www.github.com/snakemake/snakemake-wrappers/issues/2552)) ([85c799e](https://www.github.com/snakemake/snakemake-wrappers/commit/85c799e12fb9407fc6020000f65a4ed25b5b53a6))
* autobump bio/bowtie2/build ([#2557](https://www.github.com/snakemake/snakemake-wrappers/issues/2557)) ([3d51b99](https://www.github.com/snakemake/snakemake-wrappers/commit/3d51b9928cfd238ee771b3c378702df676211cc9))
* autobump bio/busco ([#2556](https://www.github.com/snakemake/snakemake-wrappers/issues/2556)) ([90a30bc](https://www.github.com/snakemake/snakemake-wrappers/commit/90a30bce90430c732ce1b7ceff8713ee073266c3))
* autobump bio/bustools/count ([#2524](https://www.github.com/snakemake/snakemake-wrappers/issues/2524)) ([456e00d](https://www.github.com/snakemake/snakemake-wrappers/commit/456e00d3550b3ddacad8041acb1108f5eece4343))
* autobump bio/bustools/sort ([#2526](https://www.github.com/snakemake/snakemake-wrappers/issues/2526)) ([0dc2402](https://www.github.com/snakemake/snakemake-wrappers/commit/0dc24023144fb444d1098ac2ddf90843d4d566c2))
* autobump bio/bustools/text ([#2525](https://www.github.com/snakemake/snakemake-wrappers/issues/2525)) ([c6a41f1](https://www.github.com/snakemake/snakemake-wrappers/commit/c6a41f1093373dc791883cba7949f416c7417456))
* autobump bio/dada2/add-species ([#2528](https://www.github.com/snakemake/snakemake-wrappers/issues/2528)) ([436567a](https://www.github.com/snakemake/snakemake-wrappers/commit/436567a3db7e884a7333c78c82317f6328a80e0d))
* autobump bio/dada2/assign-species ([#2527](https://www.github.com/snakemake/snakemake-wrappers/issues/2527)) ([7786476](https://www.github.com/snakemake/snakemake-wrappers/commit/7786476707198b315b28e1687c9e9e7ff37d32d3))
* autobump bio/dada2/collapse-nomismatch ([#2531](https://www.github.com/snakemake/snakemake-wrappers/issues/2531)) ([46a9bf0](https://www.github.com/snakemake/snakemake-wrappers/commit/46a9bf0a5ae9bcbbbcad1dee403f873e9fb9e889))
* autobump bio/dada2/filter-trim ([#2532](https://www.github.com/snakemake/snakemake-wrappers/issues/2532)) ([3b18635](https://www.github.com/snakemake/snakemake-wrappers/commit/3b186354c11e5fa7f0ceb24d84884c20760c1a97))
* autobump bio/dada2/learn-errors ([#2538](https://www.github.com/snakemake/snakemake-wrappers/issues/2538)) ([3c8d713](https://www.github.com/snakemake/snakemake-wrappers/commit/3c8d713213d78ea560cc9c314fac11ac32dd28c7))
* autobump bio/dada2/quality-profile ([#2530](https://www.github.com/snakemake/snakemake-wrappers/issues/2530)) ([40a65c7](https://www.github.com/snakemake/snakemake-wrappers/commit/40a65c7cb3ffddefa7bd6c48593d9d9ef617ddad))
* autobump bio/dada2/sample-inference ([#2529](https://www.github.com/snakemake/snakemake-wrappers/issues/2529)) ([b35731c](https://www.github.com/snakemake/snakemake-wrappers/commit/b35731c3ca9cf91e352274d041ccf701f93efa6e))
* autobump bio/delly ([#2558](https://www.github.com/snakemake/snakemake-wrappers/issues/2558)) ([70a1a17](https://www.github.com/snakemake/snakemake-wrappers/commit/70a1a17f57668eeb56765454b2577a67f6f95b45))
* autobump bio/deseq2/deseqdataset ([#2539](https://www.github.com/snakemake/snakemake-wrappers/issues/2539)) ([2353167](https://www.github.com/snakemake/snakemake-wrappers/commit/2353167d6383d3b272be1f50292d0170268e6acf))
* autobump bio/fgbio/annotatebamwithumis ([#2533](https://www.github.com/snakemake/snakemake-wrappers/issues/2533)) ([187aa85](https://www.github.com/snakemake/snakemake-wrappers/commit/187aa8537f93f018ec050fb992719db71a5fff9a))
* autobump bio/fgbio/callmolecularconsensusreads ([#2540](https://www.github.com/snakemake/snakemake-wrappers/issues/2540)) ([4d3c481](https://www.github.com/snakemake/snakemake-wrappers/commit/4d3c481e9b50a219d8bead43fae572c4b458da5f))
* autobump bio/fgbio/filterconsensusreads ([#2541](https://www.github.com/snakemake/snakemake-wrappers/issues/2541)) ([bd43470](https://www.github.com/snakemake/snakemake-wrappers/commit/bd434705c5c2c0cbf2fa84269aad748ccb5ec034))
* autobump bio/fgbio/groupreadsbyumi ([#2559](https://www.github.com/snakemake/snakemake-wrappers/issues/2559)) ([ff568c8](https://www.github.com/snakemake/snakemake-wrappers/commit/ff568c83910f9ada2b3bae9f278b502e1f093b90))
* autobump bio/gatk/applybqsrspark ([#2542](https://www.github.com/snakemake/snakemake-wrappers/issues/2542)) ([b2023c1](https://www.github.com/snakemake/snakemake-wrappers/commit/b2023c1924ec4fe9a685018b2c4810df0622f55c))
* autobump bio/gatk3/baserecalibrator ([#2543](https://www.github.com/snakemake/snakemake-wrappers/issues/2543)) ([c4e2a35](https://www.github.com/snakemake/snakemake-wrappers/commit/c4e2a3575ec05f22f446df0acc61056778746116))
* autobump bio/gatk3/indelrealigner ([#2534](https://www.github.com/snakemake/snakemake-wrappers/issues/2534)) ([9bd6dba](https://www.github.com/snakemake/snakemake-wrappers/commit/9bd6dbad38356eb035d0c33aaa4dee6e01e900eb))
* autobump bio/mashmap ([#2544](https://www.github.com/snakemake/snakemake-wrappers/issues/2544)) ([caee69d](https://www.github.com/snakemake/snakemake-wrappers/commit/caee69d44c395a315d35b36c4961a8e347b37088))
* autobump bio/rasusa ([#2535](https://www.github.com/snakemake/snakemake-wrappers/issues/2535)) ([caa3b3f](https://www.github.com/snakemake/snakemake-wrappers/commit/caa3b3ffaab9aa95cf9d7818c882e789255b9e9b))
* autobump bio/tximport ([#2545](https://www.github.com/snakemake/snakemake-wrappers/issues/2545)) ([fcb1f94](https://www.github.com/snakemake/snakemake-wrappers/commit/fcb1f9401c9ea66f7334ad91f45ea407dd474ace))
* autobump bio/vep/annotate ([#2561](https://www.github.com/snakemake/snakemake-wrappers/issues/2561)) ([9acd1ca](https://www.github.com/snakemake/snakemake-wrappers/commit/9acd1ca14c4eb929471367e399ed916c1e23fdcd))
* autobump bio/vep/cache ([#2560](https://www.github.com/snakemake/snakemake-wrappers/issues/2560)) ([1f8fe5f](https://www.github.com/snakemake/snakemake-wrappers/commit/1f8fe5fc9990bc9786e238accdd46f45d541c3dc))

### [3.3.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.2...v3.3.3) (2023-12-29)


### Performance Improvements

* autobump bio/dada2/assign-taxonomy ([#2512](https://www.github.com/snakemake/snakemake-wrappers/issues/2512)) ([a6c4b5d](https://www.github.com/snakemake/snakemake-wrappers/commit/a6c4b5dc516b7282136e1bc0164c5299a00e2ee0))
* autobump bio/dada2/dereplicate-fastq ([#2507](https://www.github.com/snakemake/snakemake-wrappers/issues/2507)) ([9a4a66a](https://www.github.com/snakemake/snakemake-wrappers/commit/9a4a66af7143489f5cf4aa547e8f21172efaf0fe))
* autobump bio/dada2/make-table ([#2509](https://www.github.com/snakemake/snakemake-wrappers/issues/2509)) ([3560de8](https://www.github.com/snakemake/snakemake-wrappers/commit/3560de8fde2ffd0d05ca96266106072a83b417c6))
* autobump bio/dada2/merge-pairs ([#2510](https://www.github.com/snakemake/snakemake-wrappers/issues/2510)) ([423f296](https://www.github.com/snakemake/snakemake-wrappers/commit/423f2963f695c9622559ef55c5e606bfca227f8d))
* autobump bio/dada2/remove-chimeras ([#2511](https://www.github.com/snakemake/snakemake-wrappers/issues/2511)) ([b672a0e](https://www.github.com/snakemake/snakemake-wrappers/commit/b672a0eca339373d5ec7157b0e440bffd81c4bc8))
* autobump bio/deseq2/deseqdataset ([#2513](https://www.github.com/snakemake/snakemake-wrappers/issues/2513)) ([408003b](https://www.github.com/snakemake/snakemake-wrappers/commit/408003b5c0db208289b94ee54bc17b3876e8bdc6))
* autobump bio/deseq2/wald ([#2508](https://www.github.com/snakemake/snakemake-wrappers/issues/2508)) ([3c2f4e5](https://www.github.com/snakemake/snakemake-wrappers/commit/3c2f4e5b4eb8d8086efbb2edaf45c92a70e37b16))
* autobump bio/ega/fetch ([#2497](https://www.github.com/snakemake/snakemake-wrappers/issues/2497)) ([2cfba15](https://www.github.com/snakemake/snakemake-wrappers/commit/2cfba1532869f530c419e8477e0a3927f8452baa))
* autobump bio/encode_fastq_downloader ([#2514](https://www.github.com/snakemake/snakemake-wrappers/issues/2514)) ([d66107e](https://www.github.com/snakemake/snakemake-wrappers/commit/d66107e6f66a271a49c1e8cee7661fa4a0d7e2a2))
* autobump bio/fgbio/callmolecularconsensusreads ([#2498](https://www.github.com/snakemake/snakemake-wrappers/issues/2498)) ([851f091](https://www.github.com/snakemake/snakemake-wrappers/commit/851f0915046076d6fa0896d7f49edc0ce4caf260))
* autobump bio/gatk3/printreads ([#2515](https://www.github.com/snakemake/snakemake-wrappers/issues/2515)) ([8ca1cee](https://www.github.com/snakemake/snakemake-wrappers/commit/8ca1cee1b89b02bb92b9548ab2251133b6619bb1))
* autobump bio/gseapy/gsea ([#2499](https://www.github.com/snakemake/snakemake-wrappers/issues/2499)) ([34ca621](https://www.github.com/snakemake/snakemake-wrappers/commit/34ca621bc87903f2a9b666c7220784803e90cabb))
* autobump bio/igv-reports ([#2516](https://www.github.com/snakemake/snakemake-wrappers/issues/2516)) ([7cb25c5](https://www.github.com/snakemake/snakemake-wrappers/commit/7cb25c58e4ecc5cb36961aa9cb1e75f996f96319))
* autobump bio/last/lastal ([#2500](https://www.github.com/snakemake/snakemake-wrappers/issues/2500)) ([421a62d](https://www.github.com/snakemake/snakemake-wrappers/commit/421a62d7973fe30f3fba332e729dbd2d52200593))
* autobump bio/last/lastal ([#2517](https://www.github.com/snakemake/snakemake-wrappers/issues/2517)) ([c6300a1](https://www.github.com/snakemake/snakemake-wrappers/commit/c6300a1a46377a8aa22a78144242f80267352285))
* autobump bio/last/lastdb ([#2501](https://www.github.com/snakemake/snakemake-wrappers/issues/2501)) ([bfc91b0](https://www.github.com/snakemake/snakemake-wrappers/commit/bfc91b046d1ec0811ff044a3441521f9cc9e626a))
* autobump bio/last/lastdb ([#2518](https://www.github.com/snakemake/snakemake-wrappers/issues/2518)) ([82aa2b2](https://www.github.com/snakemake/snakemake-wrappers/commit/82aa2b2e590fe4861a007184ca2760591a1e05f3))
* autobump bio/mashmap ([#2502](https://www.github.com/snakemake/snakemake-wrappers/issues/2502)) ([9153838](https://www.github.com/snakemake/snakemake-wrappers/commit/9153838c3e8f1a4ee5947f87e258105b4c5e55fa))
* autobump bio/minimap2/aligner ([#2504](https://www.github.com/snakemake/snakemake-wrappers/issues/2504)) ([f7968db](https://www.github.com/snakemake/snakemake-wrappers/commit/f7968db2c28b967bbc790d47b0d4194b71cdf93e))
* autobump bio/multiqc ([#2503](https://www.github.com/snakemake/snakemake-wrappers/issues/2503)) ([c9eda7f](https://www.github.com/snakemake/snakemake-wrappers/commit/c9eda7f2c12e994fc8220357f79027e6a2cfb9c9))
* autobump bio/sourmash/compute ([#2505](https://www.github.com/snakemake/snakemake-wrappers/issues/2505)) ([d776e51](https://www.github.com/snakemake/snakemake-wrappers/commit/d776e51d68368df350cf5d0dc08520eaa377b5b8))
* autobump bio/spades/metaspades ([#2519](https://www.github.com/snakemake/snakemake-wrappers/issues/2519)) ([6b88e9f](https://www.github.com/snakemake/snakemake-wrappers/commit/6b88e9f38fb85a56df057b0bb5b02c5577e766b5))
* autobump bio/sra-tools/fasterq-dump ([#2506](https://www.github.com/snakemake/snakemake-wrappers/issues/2506)) ([5132a1d](https://www.github.com/snakemake/snakemake-wrappers/commit/5132a1db113973b6c18437e01cac9aba5319f489))
* autobump bio/vep/cache ([#2520](https://www.github.com/snakemake/snakemake-wrappers/issues/2520)) ([79f83c7](https://www.github.com/snakemake/snakemake-wrappers/commit/79f83c75d6d4f60e549ea4463dbb0ae7e0beab8d))
* autobump bio/vep/plugins ([#2521](https://www.github.com/snakemake/snakemake-wrappers/issues/2521)) ([1adf343](https://www.github.com/snakemake/snakemake-wrappers/commit/1adf3436e616977accc50fa695ceb460ff67a939))
* autobump utils/datavzrd ([#2495](https://www.github.com/snakemake/snakemake-wrappers/issues/2495)) ([30fa79c](https://www.github.com/snakemake/snakemake-wrappers/commit/30fa79ccdd02f1cf1cc4272d8e739253cfd1de60))

### [3.3.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.1...v3.3.2) (2023-12-21)


### Bug Fixes

* fix title in ega/fetch metadata ([c8305af](https://www.github.com/snakemake/snakemake-wrappers/commit/c8305afe1afa7fcfa9dc13005d6f2b6bf5741a9a))
* for vsearch, fixed bug with bz2 output and added general log ([#1775](https://www.github.com/snakemake/snakemake-wrappers/issues/1775)) ([28e76d0](https://www.github.com/snakemake/snakemake-wrappers/commit/28e76d06362caf61ab033f2259a94fb65e788bd0))

### [3.3.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.3.0...v3.3.1) (2023-12-15)


### Miscellaneous Chores

* release 3.3.1 ([530381f](https://www.github.com/snakemake/snakemake-wrappers/commit/530381f1c23eed7fd8298f2116815e4b3891b892))

## [3.3.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.2.0...v3.3.0) (2023-12-15)


### Features

* add wrapper for fetching files from EGA ([#2488](https://www.github.com/snakemake/snakemake-wrappers/issues/2488)) ([3d29dcf](https://www.github.com/snakemake/snakemake-wrappers/commit/3d29dcf31a51e466796e48659402680cfd4d9290))


### Bug Fixes

* add error handling to entrez wrapper ([#2489](https://www.github.com/snakemake/snakemake-wrappers/issues/2489)) ([7d654d5](https://www.github.com/snakemake/snakemake-wrappers/commit/7d654d5a3553455400454c4f38c8a64762e54594))


### Performance Improvements

* autobump bio/bcftools/call ([#2431](https://www.github.com/snakemake/snakemake-wrappers/issues/2431)) ([3fb48df](https://www.github.com/snakemake/snakemake-wrappers/commit/3fb48df8a946a48194e0287d97906a09586275da))
* autobump bio/bcftools/concat ([#2413](https://www.github.com/snakemake/snakemake-wrappers/issues/2413)) ([5bf2d39](https://www.github.com/snakemake/snakemake-wrappers/commit/5bf2d39710d1a10139b7d9e5cd54b5e474b0e56c))
* autobump bio/bcftools/filter ([#2428](https://www.github.com/snakemake/snakemake-wrappers/issues/2428)) ([6819cb8](https://www.github.com/snakemake/snakemake-wrappers/commit/6819cb8b71e5d4be04018deb1418664454aee76f))
* autobump bio/bcftools/index ([#2418](https://www.github.com/snakemake/snakemake-wrappers/issues/2418)) ([53259a7](https://www.github.com/snakemake/snakemake-wrappers/commit/53259a700164f91540155c424b7d8b4778300da5))
* autobump bio/bcftools/merge ([#2432](https://www.github.com/snakemake/snakemake-wrappers/issues/2432)) ([778ea14](https://www.github.com/snakemake/snakemake-wrappers/commit/778ea14f174b4ecc809caacde9012e1cd10d22f4))
* autobump bio/bcftools/mpileup ([#2437](https://www.github.com/snakemake/snakemake-wrappers/issues/2437)) ([304d0b8](https://www.github.com/snakemake/snakemake-wrappers/commit/304d0b8605665eb31805c9d1e85c4b1ef77d0939))
* autobump bio/bcftools/norm ([#2442](https://www.github.com/snakemake/snakemake-wrappers/issues/2442)) ([17a025a](https://www.github.com/snakemake/snakemake-wrappers/commit/17a025ad934d6abe56fff43c310f9098b7f4bf00))
* autobump bio/bcftools/reheader ([#2427](https://www.github.com/snakemake/snakemake-wrappers/issues/2427)) ([d737204](https://www.github.com/snakemake/snakemake-wrappers/commit/d73720445433d3ff12f7c8e8ac2be736979d0736))
* autobump bio/bcftools/sort ([#2421](https://www.github.com/snakemake/snakemake-wrappers/issues/2421)) ([a6e4426](https://www.github.com/snakemake/snakemake-wrappers/commit/a6e44263b0cbf189c5f44ff9044c0775587801e3))
* autobump bio/bcftools/stats ([#2441](https://www.github.com/snakemake/snakemake-wrappers/issues/2441)) ([8c6f632](https://www.github.com/snakemake/snakemake-wrappers/commit/8c6f63282630326e051da8e15e8b0eca4761eb05))
* autobump bio/bcftools/view ([#2423](https://www.github.com/snakemake/snakemake-wrappers/issues/2423)) ([ba73c90](https://www.github.com/snakemake/snakemake-wrappers/commit/ba73c9018a294803101bd92c66bac63b2b42da10))
* autobump bio/bellerophon ([#2439](https://www.github.com/snakemake/snakemake-wrappers/issues/2439)) ([439488e](https://www.github.com/snakemake/snakemake-wrappers/commit/439488eac380b2d528240fcaee5457ff362780ba))
* autobump bio/benchmark/chm-eval-sample ([#2440](https://www.github.com/snakemake/snakemake-wrappers/issues/2440)) ([fd6981a](https://www.github.com/snakemake/snakemake-wrappers/commit/fd6981ae6f9734f0dd3ac62fd15370f844f81956))
* autobump bio/bgzip ([#2429](https://www.github.com/snakemake/snakemake-wrappers/issues/2429)) ([8f3b527](https://www.github.com/snakemake/snakemake-wrappers/commit/8f3b5278fcb985a9b68862fd321cbbf60af1af43))
* autobump bio/bismark/bam2nuc ([#2416](https://www.github.com/snakemake/snakemake-wrappers/issues/2416)) ([32f9515](https://www.github.com/snakemake/snakemake-wrappers/commit/32f9515e315b1a4e694e92eb57151ac8387649af))
* autobump bio/bismark/bismark ([#2443](https://www.github.com/snakemake/snakemake-wrappers/issues/2443)) ([2c156a9](https://www.github.com/snakemake/snakemake-wrappers/commit/2c156a9011d9694c08be5ab5368dcbf1748a7442))
* autobump bio/bismark/bismark_genome_preparation ([#2434](https://www.github.com/snakemake/snakemake-wrappers/issues/2434)) ([4a1b858](https://www.github.com/snakemake/snakemake-wrappers/commit/4a1b85846f4ee85bf0f6efb0c8f7746f0eed39de))
* autobump bio/bismark/bismark_methylation_extractor ([#2415](https://www.github.com/snakemake/snakemake-wrappers/issues/2415)) ([ae1848d](https://www.github.com/snakemake/snakemake-wrappers/commit/ae1848db14173cb06d8047688f3b3fdc8b2c0669))
* autobump bio/bismark/bismark2bedGraph ([#2435](https://www.github.com/snakemake/snakemake-wrappers/issues/2435)) ([ddbc964](https://www.github.com/snakemake/snakemake-wrappers/commit/ddbc964b016746be56e2682fa3be20ad895560b7))
* autobump bio/bismark/bismark2report ([#2422](https://www.github.com/snakemake/snakemake-wrappers/issues/2422)) ([b3b1f78](https://www.github.com/snakemake/snakemake-wrappers/commit/b3b1f78c0da8fc71a5b5748665b615fab2bf1c47))
* autobump bio/bismark/bismark2summary ([#2420](https://www.github.com/snakemake/snakemake-wrappers/issues/2420)) ([31a87bf](https://www.github.com/snakemake/snakemake-wrappers/commit/31a87bf24443051bde41283473b5eb3e803ea64f))
* autobump bio/bismark/deduplicate_bismark ([#2426](https://www.github.com/snakemake/snakemake-wrappers/issues/2426)) ([490e276](https://www.github.com/snakemake/snakemake-wrappers/commit/490e27668ee4ebf2e1d1c6e10a481d5f853a6c41))
* autobump bio/bowtie2/align ([#2414](https://www.github.com/snakemake/snakemake-wrappers/issues/2414)) ([8fe3716](https://www.github.com/snakemake/snakemake-wrappers/commit/8fe37169b72216ed862add0f992d72e5a9d2f53e))
* autobump bio/bwa-mem2/mem ([#2430](https://www.github.com/snakemake/snakemake-wrappers/issues/2430)) ([8ae7338](https://www.github.com/snakemake/snakemake-wrappers/commit/8ae7338165b7b7fad677486208c23b7caeefe73f))
* autobump bio/bwa-meme/mem ([#2433](https://www.github.com/snakemake/snakemake-wrappers/issues/2433)) ([2389bba](https://www.github.com/snakemake/snakemake-wrappers/commit/2389bba482f497e2b61b6be14ea2ab6d81772918))
* autobump bio/bwa-memx/mem ([#2424](https://www.github.com/snakemake/snakemake-wrappers/issues/2424)) ([ad72b7b](https://www.github.com/snakemake/snakemake-wrappers/commit/ad72b7b8048c53498df0951cf1deaf8e34c7f7cd))
* autobump bio/bwa/mem ([#2417](https://www.github.com/snakemake/snakemake-wrappers/issues/2417)) ([bb679e9](https://www.github.com/snakemake/snakemake-wrappers/commit/bb679e9a13a275e314fba628bfdd1703a87a4205))
* autobump bio/bwa/sampe ([#2438](https://www.github.com/snakemake/snakemake-wrappers/issues/2438)) ([ddefb15](https://www.github.com/snakemake/snakemake-wrappers/commit/ddefb155e42e6a7867abd88b8f0b1d0773c3a943))
* autobump bio/bwa/samse ([#2436](https://www.github.com/snakemake/snakemake-wrappers/issues/2436)) ([a845fa4](https://www.github.com/snakemake/snakemake-wrappers/commit/a845fa4b50966965a04b4c27895c740e4916ef45))
* autobump bio/bwa/samxe ([#2425](https://www.github.com/snakemake/snakemake-wrappers/issues/2425)) ([973ac6f](https://www.github.com/snakemake/snakemake-wrappers/commit/973ac6f531ac2a8735a3a344f548f5d3140054e1))
* autobump bio/cnvkit/export ([#2444](https://www.github.com/snakemake/snakemake-wrappers/issues/2444)) ([36a3d1e](https://www.github.com/snakemake/snakemake-wrappers/commit/36a3d1ef1782963483087a1cbdf7af3d49e360de))
* autobump bio/fgbio/annotatebamwithumis ([#2446](https://www.github.com/snakemake/snakemake-wrappers/issues/2446)) ([e896272](https://www.github.com/snakemake/snakemake-wrappers/commit/e89627231ac00d4a4f0a545bfc8dd3418611310f))
* autobump bio/fgbio/collectduplexseqmetrics ([#2448](https://www.github.com/snakemake/snakemake-wrappers/issues/2448)) ([2abdd7f](https://www.github.com/snakemake/snakemake-wrappers/commit/2abdd7f64d4e1ba0aa2429fe88e7e5d463a6c340))
* autobump bio/fgbio/filterconsensusreads ([#2447](https://www.github.com/snakemake/snakemake-wrappers/issues/2447)) ([96ad8bc](https://www.github.com/snakemake/snakemake-wrappers/commit/96ad8bc0343989e928ca1d19114735854e088c7d))
* autobump bio/fgbio/groupreadsbyumi ([#2445](https://www.github.com/snakemake/snakemake-wrappers/issues/2445)) ([d8bc1d7](https://www.github.com/snakemake/snakemake-wrappers/commit/d8bc1d73c6e165c0b5bf58ddae7611db55e39ff9))
* autobump bio/fgbio/setmateinformation ([#2449](https://www.github.com/snakemake/snakemake-wrappers/issues/2449)) ([866cedc](https://www.github.com/snakemake/snakemake-wrappers/commit/866cedca8690a14f198fc962db9c38ed89a1a27d))
* autobump bio/gatk/applybqsr ([#2450](https://www.github.com/snakemake/snakemake-wrappers/issues/2450)) ([63c744a](https://www.github.com/snakemake/snakemake-wrappers/commit/63c744a9791ed0b476637a89bff613b80216b2d5))
* autobump bio/hisat2/align ([#2452](https://www.github.com/snakemake/snakemake-wrappers/issues/2452)) ([3549c8e](https://www.github.com/snakemake/snakemake-wrappers/commit/3549c8e89904d762e3abcf9d2a09efb423cfba06))
* autobump bio/hisat2/index ([#2453](https://www.github.com/snakemake/snakemake-wrappers/issues/2453)) ([017190a](https://www.github.com/snakemake/snakemake-wrappers/commit/017190ad66419df64941a8928adc2cc8b2cd64d5))
* autobump bio/homer/makeTagDirectory ([#2451](https://www.github.com/snakemake/snakemake-wrappers/issues/2451)) ([22d8f8d](https://www.github.com/snakemake/snakemake-wrappers/commit/22d8f8dc5f5a803e60894e397dd6baa783266048))
* autobump bio/lofreq/call ([#2454](https://www.github.com/snakemake/snakemake-wrappers/issues/2454)) ([08bac48](https://www.github.com/snakemake/snakemake-wrappers/commit/08bac487ac8fdac031f1e36c2d33433aeaba1c30))
* autobump bio/lofreq/indelqual ([#2455](https://www.github.com/snakemake/snakemake-wrappers/issues/2455)) ([2637859](https://www.github.com/snakemake/snakemake-wrappers/commit/26378599f8b02a8c0d37cfe2557abda2dd12e4e0))
* autobump bio/mosdepth ([#2456](https://www.github.com/snakemake/snakemake-wrappers/issues/2456)) ([3caefb0](https://www.github.com/snakemake/snakemake-wrappers/commit/3caefb0fa0cb3953687c06458b900dccea1fe2da))
* autobump bio/paladin/align ([#2457](https://www.github.com/snakemake/snakemake-wrappers/issues/2457)) ([32fb56f](https://www.github.com/snakemake/snakemake-wrappers/commit/32fb56f4284d079a88c8f087be8f35349ccc9b3d))
* autobump bio/paladin/index ([#2461](https://www.github.com/snakemake/snakemake-wrappers/issues/2461)) ([e3bc12a](https://www.github.com/snakemake/snakemake-wrappers/commit/e3bc12a3d9a6e245efe8fa1af24198f06ded1696))
* autobump bio/paladin/prepare ([#2459](https://www.github.com/snakemake/snakemake-wrappers/issues/2459)) ([bb0f509](https://www.github.com/snakemake/snakemake-wrappers/commit/bb0f509113021d131c211165135f04713c334371))
* autobump bio/picard/markduplicates ([#2460](https://www.github.com/snakemake/snakemake-wrappers/issues/2460)) ([778f1fd](https://www.github.com/snakemake/snakemake-wrappers/commit/778f1fdf5e3479ac97fddb031b431047fd984729))
* autobump bio/pretext/map ([#2458](https://www.github.com/snakemake/snakemake-wrappers/issues/2458)) ([8535686](https://www.github.com/snakemake/snakemake-wrappers/commit/8535686db2eb1920a747dcaddcff4824aa34807f))
* autobump bio/reference/ensembl-variation ([#2462](https://www.github.com/snakemake/snakemake-wrappers/issues/2462)) ([26c321a](https://www.github.com/snakemake/snakemake-wrappers/commit/26c321a7e62e37eba26f3f75cb0833a8f7415cdf))
* autobump bio/samtools/calmd ([#2463](https://www.github.com/snakemake/snakemake-wrappers/issues/2463)) ([d1c7b4a](https://www.github.com/snakemake/snakemake-wrappers/commit/d1c7b4a8a48757443110d43e3982ddb0ec39eb0a))
* autobump bio/samtools/depth ([#2477](https://www.github.com/snakemake/snakemake-wrappers/issues/2477)) ([da2a62b](https://www.github.com/snakemake/snakemake-wrappers/commit/da2a62b805b096ec61c54aeef84ed0b67d1953ed))
* autobump bio/samtools/faidx ([#2470](https://www.github.com/snakemake/snakemake-wrappers/issues/2470)) ([7298ed1](https://www.github.com/snakemake/snakemake-wrappers/commit/7298ed1f515f915f17104354ed2f121c42b3150d))
* autobump bio/samtools/fastx ([#2474](https://www.github.com/snakemake/snakemake-wrappers/issues/2474)) ([ddbfa88](https://www.github.com/snakemake/snakemake-wrappers/commit/ddbfa884296d5f97ef7ab5cec7bf05bb00863ed6))
* autobump bio/samtools/fixmate ([#2481](https://www.github.com/snakemake/snakemake-wrappers/issues/2481)) ([71ecb0d](https://www.github.com/snakemake/snakemake-wrappers/commit/71ecb0dff6d027bee70232df03f71c4ebfc92fd3))
* autobump bio/samtools/flagstat ([#2471](https://www.github.com/snakemake/snakemake-wrappers/issues/2471)) ([93c93e3](https://www.github.com/snakemake/snakemake-wrappers/commit/93c93e31fdbb67dafa009f67577f0224878f3020))
* autobump bio/samtools/idxstats ([#2480](https://www.github.com/snakemake/snakemake-wrappers/issues/2480)) ([304c854](https://www.github.com/snakemake/snakemake-wrappers/commit/304c854a0a96caf417d50395a3635fc1e4db0cb3))
* autobump bio/samtools/index ([#2473](https://www.github.com/snakemake/snakemake-wrappers/issues/2473)) ([eed7721](https://www.github.com/snakemake/snakemake-wrappers/commit/eed772107289a59438d06bd51fdbae43bb08c6db))
* autobump bio/samtools/merge ([#2479](https://www.github.com/snakemake/snakemake-wrappers/issues/2479)) ([d6995ca](https://www.github.com/snakemake/snakemake-wrappers/commit/d6995ca4ba9987d96f5cc601b0a7dea09cc2f86a))
* autobump bio/samtools/mpileup ([#2475](https://www.github.com/snakemake/snakemake-wrappers/issues/2475)) ([c3707b0](https://www.github.com/snakemake/snakemake-wrappers/commit/c3707b04154b72196fc52c3872141c84dff9c9a9))
* autobump bio/samtools/sort ([#2468](https://www.github.com/snakemake/snakemake-wrappers/issues/2468)) ([f04208c](https://www.github.com/snakemake/snakemake-wrappers/commit/f04208c7ca7957755a17e6cc101821d69df80946))
* autobump bio/samtools/stats ([#2466](https://www.github.com/snakemake/snakemake-wrappers/issues/2466)) ([82c5af8](https://www.github.com/snakemake/snakemake-wrappers/commit/82c5af8b774d69ee625d5decb5974f617f4c5a03))
* autobump bio/samtools/view ([#2469](https://www.github.com/snakemake/snakemake-wrappers/issues/2469)) ([5ecc368](https://www.github.com/snakemake/snakemake-wrappers/commit/5ecc368c8f2fe29ecc8efbf8fff20eae0ec67d5f))
* autobump bio/snpeff/annotate ([#2472](https://www.github.com/snakemake/snakemake-wrappers/issues/2472)) ([41cbb4d](https://www.github.com/snakemake/snakemake-wrappers/commit/41cbb4d5ca2d765bfdcc70ba9cf2fa22259ed308))
* autobump bio/snpeff/download ([#2478](https://www.github.com/snakemake/snakemake-wrappers/issues/2478)) ([e8d0586](https://www.github.com/snakemake/snakemake-wrappers/commit/e8d0586f043152e85101fed0a0e2fcbf238aec74))
* autobump bio/snpsift/annotate ([#2464](https://www.github.com/snakemake/snakemake-wrappers/issues/2464)) ([7123087](https://www.github.com/snakemake/snakemake-wrappers/commit/712308755a24985f808679ba4ff116ba6d51ff5e))
* autobump bio/snpsift/dbnsfp ([#2467](https://www.github.com/snakemake/snakemake-wrappers/issues/2467)) ([4071e38](https://www.github.com/snakemake/snakemake-wrappers/commit/4071e38375713220e456d22be8d55fb0a07e01a2))
* autobump bio/snpsift/genesets ([#2476](https://www.github.com/snakemake/snakemake-wrappers/issues/2476)) ([8db87de](https://www.github.com/snakemake/snakemake-wrappers/commit/8db87defb87e7729e672bfda0b579cdab351b544))
* autobump bio/snpsift/gwascat ([#2465](https://www.github.com/snakemake/snakemake-wrappers/issues/2465)) ([74a030f](https://www.github.com/snakemake/snakemake-wrappers/commit/74a030fe1ca68f81136203722ee875a95802fb17))
* autobump bio/tabix/query ([#2483](https://www.github.com/snakemake/snakemake-wrappers/issues/2483)) ([1e15361](https://www.github.com/snakemake/snakemake-wrappers/commit/1e15361f6d9173d40a3de81379dc7c7ad386679c))
* autobump bio/tximport ([#2482](https://www.github.com/snakemake/snakemake-wrappers/issues/2482)) ([e97353f](https://www.github.com/snakemake/snakemake-wrappers/commit/e97353fac526b730b054a4b756fb59a6d0a6512a))
* autobump bio/umis/bamtag ([#2484](https://www.github.com/snakemake/snakemake-wrappers/issues/2484)) ([d0501aa](https://www.github.com/snakemake/snakemake-wrappers/commit/d0501aa052218dbca8b28124bff34c20f7db6d39))
* autobump bio/vembrane/filter ([#2486](https://www.github.com/snakemake/snakemake-wrappers/issues/2486)) ([b0b3cc9](https://www.github.com/snakemake/snakemake-wrappers/commit/b0b3cc9565e9723375a187c2536cabf4a30a87a2))
* autobump bio/vembrane/table ([#2485](https://www.github.com/snakemake/snakemake-wrappers/issues/2485)) ([a34fd66](https://www.github.com/snakemake/snakemake-wrappers/commit/a34fd66f3dcb6ae701ba756bcb8381ec83d7ecfa))
* autobump bio/vep/annotate ([#2487](https://www.github.com/snakemake/snakemake-wrappers/issues/2487)) ([530fe3f](https://www.github.com/snakemake/snakemake-wrappers/commit/530fe3f635634410ee57c2d2ffbe1e5737645a17))

## [3.2.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.1.0...v3.2.0) (2023-12-14)


### Features

* add entrez/efetch wrapper ([#2411](https://www.github.com/snakemake/snakemake-wrappers/issues/2411)) ([9f0ad09](https://www.github.com/snakemake/snakemake-wrappers/commit/9f0ad092e7dfe2a43a2d13d5f55225cea1dc6c1a))


### Bug Fixes

* Add json output to Nonpareil and extra plot options ([#2393](https://www.github.com/snakemake/snakemake-wrappers/issues/2393)) ([c43af99](https://www.github.com/snakemake/snakemake-wrappers/commit/c43af995f0d26892cd7331b03a1d2934ae371239))

## [3.1.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.0.4...v3.1.0) (2023-12-11)


### Features

* datavzrd to 2.33.2 ([#2408](https://www.github.com/snakemake/snakemake-wrappers/issues/2408)) ([8cd3c57](https://www.github.com/snakemake/snakemake-wrappers/commit/8cd3c573b886fdfa220043c47dc3d94f8b49e872))


### Performance Improvements

* autobump bio/cutadapt/pe ([#2395](https://www.github.com/snakemake/snakemake-wrappers/issues/2395)) ([1e23b52](https://www.github.com/snakemake/snakemake-wrappers/commit/1e23b52dd5c8b752d24675eb072d5cbe5eb5938b))
* autobump bio/cutadapt/se ([#2396](https://www.github.com/snakemake/snakemake-wrappers/issues/2396)) ([948d27e](https://www.github.com/snakemake/snakemake-wrappers/commit/948d27e0a3c689e1cc45c714b8b4fbc0574fcb50))
* autobump bio/enhancedvolcano ([#2398](https://www.github.com/snakemake/snakemake-wrappers/issues/2398)) ([8bf91e8](https://www.github.com/snakemake/snakemake-wrappers/commit/8bf91e8430d14cb85a6551de00362f71e641f57b))
* autobump bio/gdc-api/bam-slicing ([#2399](https://www.github.com/snakemake/snakemake-wrappers/issues/2399)) ([5826e30](https://www.github.com/snakemake/snakemake-wrappers/commit/5826e303bc5df2f0188922ac3512ac063769c9cb))
* autobump bio/last/lastal ([#2400](https://www.github.com/snakemake/snakemake-wrappers/issues/2400)) ([c705bda](https://www.github.com/snakemake/snakemake-wrappers/commit/c705bda526870282c95adc9dfe54f8462ffbb40f))
* autobump bio/last/lastdb ([#2401](https://www.github.com/snakemake/snakemake-wrappers/issues/2401)) ([5315ac4](https://www.github.com/snakemake/snakemake-wrappers/commit/5315ac42a5791bba09b8f1b050006858ed296880))
* autobump bio/vg/construct ([#2403](https://www.github.com/snakemake/snakemake-wrappers/issues/2403)) ([fb600b4](https://www.github.com/snakemake/snakemake-wrappers/commit/fb600b48111711c2464b91293127243f4f1d3f57))
* autobump bio/vg/ids ([#2406](https://www.github.com/snakemake/snakemake-wrappers/issues/2406)) ([a00c987](https://www.github.com/snakemake/snakemake-wrappers/commit/a00c987d8c72764f37fc9ce992f67fb08fa29c64))
* autobump bio/vg/kmers ([#2407](https://www.github.com/snakemake/snakemake-wrappers/issues/2407)) ([561ccaf](https://www.github.com/snakemake/snakemake-wrappers/commit/561ccafb6ba90cf7a3ae782076c90e5cd262a6a8))
* autobump bio/vg/merge ([#2404](https://www.github.com/snakemake/snakemake-wrappers/issues/2404)) ([49d66d3](https://www.github.com/snakemake/snakemake-wrappers/commit/49d66d36564773b4641a095b1cc9e94bc3b8fe2f))
* autobump bio/vg/prune ([#2402](https://www.github.com/snakemake/snakemake-wrappers/issues/2402)) ([51102d9](https://www.github.com/snakemake/snakemake-wrappers/commit/51102d9683fecb79981d57e67941081a41f22a4d))
* autobump bio/vg/sim ([#2405](https://www.github.com/snakemake/snakemake-wrappers/issues/2405)) ([5710671](https://www.github.com/snakemake/snakemake-wrappers/commit/571067139f010cdf0b4f2509fbc483b046bba0d2))

### [3.0.4](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.0.3...v3.0.4) (2023-12-07)


### Bug Fixes

* add support for multiple samples to bcftools mpileup ([#2391](https://www.github.com/snakemake/snakemake-wrappers/issues/2391)) ([1296a9c](https://www.github.com/snakemake/snakemake-wrappers/commit/1296a9ccd583b0fad159d6564530cc2f3f374055))

### [3.0.3](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.0.2...v3.0.3) (2023-12-05)


### Bug Fixes

* issue 2295 ([#2390](https://www.github.com/snakemake/snakemake-wrappers/issues/2390)) ([42906ac](https://www.github.com/snakemake/snakemake-wrappers/commit/42906aca1550a567a95966cf34f773911e2a9bb3))


### Performance Improvements

* autobump bio/last/lastal ([#2387](https://www.github.com/snakemake/snakemake-wrappers/issues/2387)) ([ff512fb](https://www.github.com/snakemake/snakemake-wrappers/commit/ff512fbd4fe7772a96b96f9ea177b1e8756b4782))
* autobump bio/last/lastdb ([#2388](https://www.github.com/snakemake/snakemake-wrappers/issues/2388)) ([0dea6a1](https://www.github.com/snakemake/snakemake-wrappers/commit/0dea6a14eebd955f641e265c7d14cfd495ecbc5e))

### [3.0.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.0.1...v3.0.2) (2023-11-29)


### Performance Improvements

* autobump bio/sra-tools/fasterq-dump ([#2385](https://www.github.com/snakemake/snakemake-wrappers/issues/2385)) ([2a92a50](https://www.github.com/snakemake/snakemake-wrappers/commit/2a92a5097e498add32fad68c2112870d34d61095))
* autobump bio/vsearch ([#2386](https://www.github.com/snakemake/snakemake-wrappers/issues/2386)) ([702f980](https://www.github.com/snakemake/snakemake-wrappers/commit/702f980bf4b65e8c12009f5414a57532a809db73))
* autobump utils/datavzrd ([#2383](https://www.github.com/snakemake/snakemake-wrappers/issues/2383)) ([0d64202](https://www.github.com/snakemake/snakemake-wrappers/commit/0d642022376b6e794c2a51b26a2f06b94a63e2c3))

### [3.0.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v3.0.0...v3.0.1) (2023-11-29)


### Performance Improvements

* autobump bio/qualimap/bamqc ([#2379](https://www.github.com/snakemake/snakemake-wrappers/issues/2379)) ([a3709f0](https://www.github.com/snakemake/snakemake-wrappers/commit/a3709f0ec08942a25ad85aab971ae2dd73591f96))
* autobump bio/qualimap/rnaseq ([#2378](https://www.github.com/snakemake/snakemake-wrappers/issues/2378)) ([61b6658](https://www.github.com/snakemake/snakemake-wrappers/commit/61b665892e0aebf58cd0a2cf4549cef64f2fcb5d))
* autobump bio/seqkit ([#2380](https://www.github.com/snakemake/snakemake-wrappers/issues/2380)) ([20c22b7](https://www.github.com/snakemake/snakemake-wrappers/commit/20c22b75e2af1d1d08ea6b74c236cd5685c3e904))

## [3.0.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.13.0...v3.0.0) (2023-11-23)


### ⚠ BREAKING CHANGES

* replace all bbtool wrappers with one bbtool wrapper for all subcommands (#1322)

### Features

* allow for specifying multiple chromosomes in ensembl reference dna sequence download wrapper ([#2376](https://www.github.com/snakemake/snakemake-wrappers/issues/2376)) ([c5590f0](https://www.github.com/snakemake/snakemake-wrappers/commit/c5590f03c9990b851181171e70217bb911ddac27))
* replace all bbtool wrappers with one bbtool wrapper for all subcommands ([#1322](https://www.github.com/snakemake/snakemake-wrappers/issues/1322)) ([6eb3c22](https://www.github.com/snakemake/snakemake-wrappers/commit/6eb3c227686c545b937d7cc5ef39b0b435f3e2b0))


### Bug Fixes

* Update MultiQC to 1.18 ([#2377](https://www.github.com/snakemake/snakemake-wrappers/issues/2377)) ([03bf2d9](https://www.github.com/snakemake/snakemake-wrappers/commit/03bf2d9e2d13968cb71a5e67d80a57b1502dc060))


### Performance Improvements

* autobump bio/bbtools ([#2325](https://www.github.com/snakemake/snakemake-wrappers/issues/2325)) ([bf09e80](https://www.github.com/snakemake/snakemake-wrappers/commit/bf09e801dba4e3cf2186ec80631e22df6adbf993))
* autobump bio/bedtools/bamtobed ([#2334](https://www.github.com/snakemake/snakemake-wrappers/issues/2334)) ([91b8054](https://www.github.com/snakemake/snakemake-wrappers/commit/91b8054fa408e2a96fed5ab24eea3f4f9f9a7f5c))
* autobump bio/bedtools/complement ([#2341](https://www.github.com/snakemake/snakemake-wrappers/issues/2341)) ([d0b9659](https://www.github.com/snakemake/snakemake-wrappers/commit/d0b96598864e0f5827eafb6a3f47aab8c2524995))
* autobump bio/bedtools/coveragebed ([#2342](https://www.github.com/snakemake/snakemake-wrappers/issues/2342)) ([8c25388](https://www.github.com/snakemake/snakemake-wrappers/commit/8c25388d851eaaae786f2ecdb3a684cf66037c1b))
* autobump bio/bedtools/genomecov ([#2336](https://www.github.com/snakemake/snakemake-wrappers/issues/2336)) ([2ba070e](https://www.github.com/snakemake/snakemake-wrappers/commit/2ba070edd0781b97227a2103bcd28670d0382141))
* autobump bio/bedtools/intersect ([#2338](https://www.github.com/snakemake/snakemake-wrappers/issues/2338)) ([b299438](https://www.github.com/snakemake/snakemake-wrappers/commit/b2994382ff94d11491ea991635fd25f74e9a56a4))
* autobump bio/bedtools/merge ([#2330](https://www.github.com/snakemake/snakemake-wrappers/issues/2330)) ([8c6ae83](https://www.github.com/snakemake/snakemake-wrappers/commit/8c6ae83bdd70b09dd3e434d13cc8b035ebe34089))
* autobump bio/bedtools/slop ([#2324](https://www.github.com/snakemake/snakemake-wrappers/issues/2324)) ([dfef51e](https://www.github.com/snakemake/snakemake-wrappers/commit/dfef51e5d5358a1fdfc87e7c560b31aab6e3a1aa))
* autobump bio/bedtools/sort ([#2328](https://www.github.com/snakemake/snakemake-wrappers/issues/2328)) ([fde082e](https://www.github.com/snakemake/snakemake-wrappers/commit/fde082e8c75bf674324499b52bd48340c0572f64))
* autobump bio/bedtools/split ([#2326](https://www.github.com/snakemake/snakemake-wrappers/issues/2326)) ([7663786](https://www.github.com/snakemake/snakemake-wrappers/commit/7663786a39a45ad0e6090324f400e94bb3e0bc68))
* autobump bio/blast/blastn ([#2335](https://www.github.com/snakemake/snakemake-wrappers/issues/2335)) ([518a30a](https://www.github.com/snakemake/snakemake-wrappers/commit/518a30ad707534046a2a1cfe861e861ece749683))
* autobump bio/blast/makeblastdb ([#2329](https://www.github.com/snakemake/snakemake-wrappers/issues/2329)) ([f24d810](https://www.github.com/snakemake/snakemake-wrappers/commit/f24d8106f4c2b6d1230535486967e82ae3f95dd5))
* autobump bio/bustools/count ([#2339](https://www.github.com/snakemake/snakemake-wrappers/issues/2339)) ([f8598f8](https://www.github.com/snakemake/snakemake-wrappers/commit/f8598f83cf8e4f7b5bd75f18bc036b4f9610de07))
* autobump bio/bwa-mem2/mem ([#2323](https://www.github.com/snakemake/snakemake-wrappers/issues/2323)) ([c751efd](https://www.github.com/snakemake/snakemake-wrappers/commit/c751efda5b93b155c1b42726dbe0f7fd4e10873c))
* autobump bio/bwa-meme/mem ([#2331](https://www.github.com/snakemake/snakemake-wrappers/issues/2331)) ([ae28cb4](https://www.github.com/snakemake/snakemake-wrappers/commit/ae28cb4db8473e147f033f447f186fead3a3f092))
* autobump bio/bwa-memx/mem ([#2337](https://www.github.com/snakemake/snakemake-wrappers/issues/2337)) ([1fe5ba7](https://www.github.com/snakemake/snakemake-wrappers/commit/1fe5ba7190b2f690a683a4c7f3397f039b8d71a2))
* autobump bio/bwa/mem ([#2333](https://www.github.com/snakemake/snakemake-wrappers/issues/2333)) ([e24ce7c](https://www.github.com/snakemake/snakemake-wrappers/commit/e24ce7c1affe9f779dd3bff9c72bfb46608fdbb9))
* autobump bio/bwa/sampe ([#2327](https://www.github.com/snakemake/snakemake-wrappers/issues/2327)) ([70a1ac3](https://www.github.com/snakemake/snakemake-wrappers/commit/70a1ac3efaeff35b3059e28d109ac8112b374669))
* autobump bio/bwa/samse ([#2332](https://www.github.com/snakemake/snakemake-wrappers/issues/2332)) ([61c0e6d](https://www.github.com/snakemake/snakemake-wrappers/commit/61c0e6d4fd93e13f956ef40720ab072519060d90))
* autobump bio/bwa/samxe ([#2340](https://www.github.com/snakemake/snakemake-wrappers/issues/2340)) ([d0865bc](https://www.github.com/snakemake/snakemake-wrappers/commit/d0865bc5a2f1e0a3358be2a678fd1545d95a75d8))
* autobump bio/cooltools/dots ([#2344](https://www.github.com/snakemake/snakemake-wrappers/issues/2344)) ([c55e268](https://www.github.com/snakemake/snakemake-wrappers/commit/c55e26814506ea5d6d33afd2689dfe005f2cf968))
* autobump bio/cooltools/eigs_cis ([#2348](https://www.github.com/snakemake/snakemake-wrappers/issues/2348)) ([1b7d26e](https://www.github.com/snakemake/snakemake-wrappers/commit/1b7d26e2775cdd6c785cf34a886e15bd82289aca))
* autobump bio/cooltools/eigs_trans ([#2346](https://www.github.com/snakemake/snakemake-wrappers/issues/2346)) ([f00f77b](https://www.github.com/snakemake/snakemake-wrappers/commit/f00f77b0a0d057f5576f1a375bc96b79a9e9f0c9))
* autobump bio/cooltools/expected_cis ([#2347](https://www.github.com/snakemake/snakemake-wrappers/issues/2347)) ([f4c8924](https://www.github.com/snakemake/snakemake-wrappers/commit/f4c8924b6b4f544a989e665d5e272d0f917ef700))
* autobump bio/cooltools/expected_trans ([#2350](https://www.github.com/snakemake/snakemake-wrappers/issues/2350)) ([7e3f763](https://www.github.com/snakemake/snakemake-wrappers/commit/7e3f7635a0a7e4832dbf4d45fcabb9497efb0e89))
* autobump bio/cooltools/insulation ([#2343](https://www.github.com/snakemake/snakemake-wrappers/issues/2343)) ([77e4ef5](https://www.github.com/snakemake/snakemake-wrappers/commit/77e4ef5d5a149bded23ebb28be3430e3c013eb76))
* autobump bio/cooltools/pileup ([#2345](https://www.github.com/snakemake/snakemake-wrappers/issues/2345)) ([6c6b0b1](https://www.github.com/snakemake/snakemake-wrappers/commit/6c6b0b1c6712d37909927f444debf13becb7841b))
* autobump bio/cooltools/saddle ([#2349](https://www.github.com/snakemake/snakemake-wrappers/issues/2349)) ([9f0f802](https://www.github.com/snakemake/snakemake-wrappers/commit/9f0f802f339667707bd8ed6013ca6e759ca9ce05))
* autobump bio/gseapy/gsea ([#2351](https://www.github.com/snakemake/snakemake-wrappers/issues/2351)) ([b3b3c94](https://www.github.com/snakemake/snakemake-wrappers/commit/b3b3c94d857cfcdfafdc9ef819ba8f2567f26afa))
* autobump bio/hmmer/hmmbuild ([#2355](https://www.github.com/snakemake/snakemake-wrappers/issues/2355)) ([2744f59](https://www.github.com/snakemake/snakemake-wrappers/commit/2744f59f5a9c13d5e80152f737d315535f4049ff))
* autobump bio/hmmer/hmmpress ([#2354](https://www.github.com/snakemake/snakemake-wrappers/issues/2354)) ([3f379bc](https://www.github.com/snakemake/snakemake-wrappers/commit/3f379bce4f20970983b319cd327bf5a31623ba8d))
* autobump bio/hmmer/hmmscan ([#2353](https://www.github.com/snakemake/snakemake-wrappers/issues/2353)) ([50c6425](https://www.github.com/snakemake/snakemake-wrappers/commit/50c642568ae259784c0fb50cf3440e3b84e0e6b5))
* autobump bio/hmmer/hmmsearch ([#2352](https://www.github.com/snakemake/snakemake-wrappers/issues/2352)) ([ed2bbcc](https://www.github.com/snakemake/snakemake-wrappers/commit/ed2bbccff232d5a16677ea60e6e70e241ed4bb61))
* autobump bio/last/lastal ([#2357](https://www.github.com/snakemake/snakemake-wrappers/issues/2357)) ([2589f18](https://www.github.com/snakemake/snakemake-wrappers/commit/2589f18971c2b377e0c8003c7f2ef7d412a277ae))
* autobump bio/last/lastdb ([#2356](https://www.github.com/snakemake/snakemake-wrappers/issues/2356)) ([4cee71f](https://www.github.com/snakemake/snakemake-wrappers/commit/4cee71f08cf1cf55c31ddb654f1349830412e708))
* autobump bio/picard/addorreplacereadgroups ([#2370](https://www.github.com/snakemake/snakemake-wrappers/issues/2370)) ([cf1cef0](https://www.github.com/snakemake/snakemake-wrappers/commit/cf1cef071e5b932c797078661bacf1eaf8ab12b2))
* autobump bio/picard/bedtointervallist ([#2360](https://www.github.com/snakemake/snakemake-wrappers/issues/2360)) ([b71d414](https://www.github.com/snakemake/snakemake-wrappers/commit/b71d414de9d5adea175fd773caead4c4e72a2dde))
* autobump bio/picard/collectalignmentsummarymetrics ([#2359](https://www.github.com/snakemake/snakemake-wrappers/issues/2359)) ([8873d75](https://www.github.com/snakemake/snakemake-wrappers/commit/8873d7552e8ef4acd58aa3d380e847768342aa59))
* autobump bio/picard/collectgcbiasmetrics ([#2366](https://www.github.com/snakemake/snakemake-wrappers/issues/2366)) ([f6d5248](https://www.github.com/snakemake/snakemake-wrappers/commit/f6d52486f7a511d705a383325ba07edd8821f99a))
* autobump bio/picard/collecthsmetrics ([#2369](https://www.github.com/snakemake/snakemake-wrappers/issues/2369)) ([f730d54](https://www.github.com/snakemake/snakemake-wrappers/commit/f730d54f21a56723237c33645f103645c9ea977e))
* autobump bio/picard/collectinsertsizemetrics ([#2373](https://www.github.com/snakemake/snakemake-wrappers/issues/2373)) ([a952ad4](https://www.github.com/snakemake/snakemake-wrappers/commit/a952ad4503ea74ecef60e0646c0fcbdc8aa8158f))
* autobump bio/picard/collectmultiplemetrics ([#2364](https://www.github.com/snakemake/snakemake-wrappers/issues/2364)) ([b21473a](https://www.github.com/snakemake/snakemake-wrappers/commit/b21473aff3482061b1e41b2b508f64e8072a77d7))
* autobump bio/picard/collectrnaseqmetrics ([#2361](https://www.github.com/snakemake/snakemake-wrappers/issues/2361)) ([2b36e3c](https://www.github.com/snakemake/snakemake-wrappers/commit/2b36e3c0dd38b1abd75e6a531c12913b4365b1b0))
* autobump bio/picard/collecttargetedpcrmetrics ([#2358](https://www.github.com/snakemake/snakemake-wrappers/issues/2358)) ([babe13e](https://www.github.com/snakemake/snakemake-wrappers/commit/babe13e9120377c7e6c3ea7f96c10fdb4e616571))
* autobump bio/picard/createsequencedictionary ([#2372](https://www.github.com/snakemake/snakemake-wrappers/issues/2372)) ([70630ac](https://www.github.com/snakemake/snakemake-wrappers/commit/70630ace2fba1b8a7e07e8dadeadb210dba5fbe6))
* autobump bio/picard/markduplicates ([#2365](https://www.github.com/snakemake/snakemake-wrappers/issues/2365)) ([66bea69](https://www.github.com/snakemake/snakemake-wrappers/commit/66bea6963e0cfe26908cd093acf011504869c4a3))
* autobump bio/picard/mergesamfiles ([#2362](https://www.github.com/snakemake/snakemake-wrappers/issues/2362)) ([b1e64e2](https://www.github.com/snakemake/snakemake-wrappers/commit/b1e64e2158f13381bd3c052e9641a1f6c65e9602))
* autobump bio/picard/mergevcfs ([#2363](https://www.github.com/snakemake/snakemake-wrappers/issues/2363)) ([2ca8f9e](https://www.github.com/snakemake/snakemake-wrappers/commit/2ca8f9eaa2255a7a9393e54ea88bae1c2d60ea06))
* autobump bio/picard/revertsam ([#2367](https://www.github.com/snakemake/snakemake-wrappers/issues/2367)) ([8a54527](https://www.github.com/snakemake/snakemake-wrappers/commit/8a54527a7b493d434c3d94e3376fab18673691b7))
* autobump bio/picard/samtofastq ([#2371](https://www.github.com/snakemake/snakemake-wrappers/issues/2371)) ([62ae9e5](https://www.github.com/snakemake/snakemake-wrappers/commit/62ae9e50d617a4529b767fce6d9f9b070d0dda45))
* autobump bio/picard/sortsam ([#2368](https://www.github.com/snakemake/snakemake-wrappers/issues/2368)) ([1a359a4](https://www.github.com/snakemake/snakemake-wrappers/commit/1a359a4bc88d38880bbf552698f95c6f1d605021))
* autobump bio/sortmerna ([#2374](https://www.github.com/snakemake/snakemake-wrappers/issues/2374)) ([e0920c9](https://www.github.com/snakemake/snakemake-wrappers/commit/e0920c9440f494167354f20583618d603b2c173e))
* autobump bio/vsearch ([#2375](https://www.github.com/snakemake/snakemake-wrappers/issues/2375)) ([c59fbc8](https://www.github.com/snakemake/snakemake-wrappers/commit/c59fbc8f52e16204ffb3b7c8b1c17479c4ebe391))

## [2.13.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.12.0...v2.13.0) (2023-11-13)


### Features

* sortmerna wrapper ([#2320](https://www.github.com/snakemake/snakemake-wrappers/issues/2320)) ([599165b](https://www.github.com/snakemake/snakemake-wrappers/commit/599165bb5dd817585b1abea320d22b530b1d68cc))

## [2.12.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.11.1...v2.12.0) (2023-11-10)


### Features

* update datavzrd wrapper to datavzrd `v2.31.0` ([#2318](https://www.github.com/snakemake/snakemake-wrappers/issues/2318)) ([a142594](https://www.github.com/snakemake/snakemake-wrappers/commit/a1425949e9a7717c14179481feed086a7187cb4f))

### [2.11.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.11.0...v2.11.1) (2023-11-10)


### Performance Improvements

* autobump utils/nextflow ([#2120](https://www.github.com/snakemake/snakemake-wrappers/issues/2120)) ([45ea105](https://www.github.com/snakemake/snakemake-wrappers/commit/45ea10591e835b4579031bea53399a2211ff76ec))

## [2.11.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.10.0...v2.11.0) (2023-11-10)


### Features

* Gatk short-variants-calling meta-wrapper ([#1778](https://www.github.com/snakemake/snakemake-wrappers/issues/1778)) ([4099e4b](https://www.github.com/snakemake/snakemake-wrappers/commit/4099e4bb17959efc5037d48c7557b5668e196acd))


### Performance Improvements

* autobump bio/gatk/applybqsr ([#2300](https://www.github.com/snakemake/snakemake-wrappers/issues/2300)) ([eb86cea](https://www.github.com/snakemake/snakemake-wrappers/commit/eb86cea6a11781b6461471e3b1deaffce06c42c6))
* autobump bio/gatk/callcopyratiosegments ([#2303](https://www.github.com/snakemake/snakemake-wrappers/issues/2303)) ([a079efa](https://www.github.com/snakemake/snakemake-wrappers/commit/a079efaeccbb45437b96afab79a732a44407b080))
* autobump bio/gatk/filtermutectcalls ([#2304](https://www.github.com/snakemake/snakemake-wrappers/issues/2304)) ([14cdc1f](https://www.github.com/snakemake/snakemake-wrappers/commit/14cdc1fd51517025114b88ee329c144fbb5bf86c))
* autobump bio/gatk/haplotypecaller ([#2307](https://www.github.com/snakemake/snakemake-wrappers/issues/2307)) ([ff59451](https://www.github.com/snakemake/snakemake-wrappers/commit/ff594514fb4baa264a38383baca3835f5afd6e33))
* autobump bio/gatk/leftalignandtrimvariants ([#2302](https://www.github.com/snakemake/snakemake-wrappers/issues/2302)) ([998385d](https://www.github.com/snakemake/snakemake-wrappers/commit/998385d95c5791d5759ad2a807862f4db4d158b0))
* autobump bio/gatk/printreadsspark ([#2308](https://www.github.com/snakemake/snakemake-wrappers/issues/2308)) ([2aa9b79](https://www.github.com/snakemake/snakemake-wrappers/commit/2aa9b79149cf81be0c19fe3217b43ddf44d6ffce))
* autobump bio/gatk/scatterintervalsbyns ([#2305](https://www.github.com/snakemake/snakemake-wrappers/issues/2305)) ([9ddace9](https://www.github.com/snakemake/snakemake-wrappers/commit/9ddace94c7341e488c69b6ca8024528ea6009839))
* autobump bio/gatk/variantannotator ([#2306](https://www.github.com/snakemake/snakemake-wrappers/issues/2306)) ([2d43be9](https://www.github.com/snakemake/snakemake-wrappers/commit/2d43be90f73466c5e9b611a3c71eca454efc1b38))
* autobump bio/gatk/varianteval ([#2301](https://www.github.com/snakemake/snakemake-wrappers/issues/2301)) ([a987c19](https://www.github.com/snakemake/snakemake-wrappers/commit/a987c19cb8027a98dd211620163fbe9afba45c2e))
* autobump bio/genomepy ([#2299](https://www.github.com/snakemake/snakemake-wrappers/issues/2299)) ([cfc3db3](https://www.github.com/snakemake/snakemake-wrappers/commit/cfc3db3deae107764d910c3b650d9b358080a68d))
* autobump bio/gridss/preprocess ([#2298](https://www.github.com/snakemake/snakemake-wrappers/issues/2298)) ([7cddab3](https://www.github.com/snakemake/snakemake-wrappers/commit/7cddab3f69e7c10dfb8453e6bccb429a287cfceb))
* autobump bio/hifiasm ([#2309](https://www.github.com/snakemake/snakemake-wrappers/issues/2309)) ([2d52e06](https://www.github.com/snakemake/snakemake-wrappers/commit/2d52e065539759eebf6a470bc802649096e2d971))
* autobump bio/kallisto/index ([#2246](https://www.github.com/snakemake/snakemake-wrappers/issues/2246)) ([29b1c32](https://www.github.com/snakemake/snakemake-wrappers/commit/29b1c32d24689084247611a09395e5b24109dc0c))
* autobump bio/last/lastal ([#2310](https://www.github.com/snakemake/snakemake-wrappers/issues/2310)) ([0c4ff31](https://www.github.com/snakemake/snakemake-wrappers/commit/0c4ff31c0737a387e6908b5b149023c35bbc925b))
* autobump bio/last/lastdb ([#2093](https://www.github.com/snakemake/snakemake-wrappers/issues/2093)) ([d055ba9](https://www.github.com/snakemake/snakemake-wrappers/commit/d055ba9ebc4e8863069a379dcc50ef25f41face2))
* autobump bio/pbmm2/align ([#2313](https://www.github.com/snakemake/snakemake-wrappers/issues/2313)) ([d977038](https://www.github.com/snakemake/snakemake-wrappers/commit/d977038730e2e64aa69d210a5c6473bd37f5983a))
* autobump bio/pbmm2/index ([#2312](https://www.github.com/snakemake/snakemake-wrappers/issues/2312)) ([8c714a6](https://www.github.com/snakemake/snakemake-wrappers/commit/8c714a635785f82ee26df1225844371785cd1c2f))
* autobump bio/pyroe/makesplicedintronic ([#2314](https://www.github.com/snakemake/snakemake-wrappers/issues/2314)) ([dcb1810](https://www.github.com/snakemake/snakemake-wrappers/commit/dcb1810b6b667e1c4e5442927ae3585d8c681b1d))
* autobump bio/pyroe/makeunspliceunspliced ([#2311](https://www.github.com/snakemake/snakemake-wrappers/issues/2311)) ([295df81](https://www.github.com/snakemake/snakemake-wrappers/commit/295df81e10435955afca1f81460c9f4b773dc823))
* autobump bio/seqkit ([#2315](https://www.github.com/snakemake/snakemake-wrappers/issues/2315)) ([5d8cd40](https://www.github.com/snakemake/snakemake-wrappers/commit/5d8cd40df228e60f218e27eb70c830ddf5f17c77))

## [2.10.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.9.1...v2.10.0) (2023-11-08)


### Features

* update datavzrd 2.29.0 ([#2288](https://www.github.com/snakemake/snakemake-wrappers/issues/2288)) ([02ca59a](https://www.github.com/snakemake/snakemake-wrappers/commit/02ca59af0b79d099c88bbd4407a3a7695e8a7848))
* update datavzrd 2.30.0 ([#2294](https://www.github.com/snakemake/snakemake-wrappers/issues/2294)) ([6c1750d](https://www.github.com/snakemake/snakemake-wrappers/commit/6c1750d9f915fc8c28a231ec575af7b9feafb65f))


### Bug Fixes

* bug when renaming samples ([#2293](https://www.github.com/snakemake/snakemake-wrappers/issues/2293)) ([8c217f8](https://www.github.com/snakemake/snakemake-wrappers/commit/8c217f8a86128deb7c5579ce35081e515434b6e9))
* fix datavzrd version pinning ([#2290](https://www.github.com/snakemake/snakemake-wrappers/issues/2290)) ([2f0cee7](https://www.github.com/snakemake/snakemake-wrappers/commit/2f0cee7fcaa3878e19534c05b2a4ac2c4d413c18))


### Performance Improvements

* autobump bio/bustools/sort ([#2234](https://www.github.com/snakemake/snakemake-wrappers/issues/2234)) ([3ce66d6](https://www.github.com/snakemake/snakemake-wrappers/commit/3ce66d627741904cb7903380900948f21d7902b6))
* autobump bio/bustools/text ([#2233](https://www.github.com/snakemake/snakemake-wrappers/issues/2233)) ([88185ac](https://www.github.com/snakemake/snakemake-wrappers/commit/88185acf6b74e1bc2280e54aaaab2a1e86ce2bed))
* autobump bio/deseq2/deseqdataset ([#2237](https://www.github.com/snakemake/snakemake-wrappers/issues/2237)) ([dfc5575](https://www.github.com/snakemake/snakemake-wrappers/commit/dfc5575b3364513c0530111043e2d961717b0c80))
* autobump bio/deseq2/wald ([#2236](https://www.github.com/snakemake/snakemake-wrappers/issues/2236)) ([8657895](https://www.github.com/snakemake/snakemake-wrappers/commit/8657895edeb9f2fc58a0837f5cccd94ef980d18f))
* autobump bio/fastp ([#2239](https://www.github.com/snakemake/snakemake-wrappers/issues/2239)) ([8b5947d](https://www.github.com/snakemake/snakemake-wrappers/commit/8b5947d8b6f24652eba036729d48a93957e6f08b))
* autobump bio/fastq_screen ([#2238](https://www.github.com/snakemake/snakemake-wrappers/issues/2238)) ([c75f5a2](https://www.github.com/snakemake/snakemake-wrappers/commit/c75f5a2faade1a5e6a89a9e05ab6688ce3a5951e))
* autobump bio/fastqc ([#2240](https://www.github.com/snakemake/snakemake-wrappers/issues/2240)) ([5b46013](https://www.github.com/snakemake/snakemake-wrappers/commit/5b46013824dda94c13e4a096e42eb34c4956f613))
* autobump bio/fgbio/annotatebamwithumis ([#2243](https://www.github.com/snakemake/snakemake-wrappers/issues/2243)) ([f7b8427](https://www.github.com/snakemake/snakemake-wrappers/commit/f7b842729e22695562df8601d172a02cd382ab00))
* autobump bio/fgbio/callmolecularconsensusreads ([#2244](https://www.github.com/snakemake/snakemake-wrappers/issues/2244)) ([0def80b](https://www.github.com/snakemake/snakemake-wrappers/commit/0def80b73c4f973d4c09de37ae3c5462e7e98209))
* autobump bio/fgbio/filterconsensusreads ([#2242](https://www.github.com/snakemake/snakemake-wrappers/issues/2242)) ([aed8b65](https://www.github.com/snakemake/snakemake-wrappers/commit/aed8b653dce7ea3f5813531ed8f88407309e4274))
* autobump bio/fgbio/groupreadsbyumi ([#2245](https://www.github.com/snakemake/snakemake-wrappers/issues/2245)) ([98ca646](https://www.github.com/snakemake/snakemake-wrappers/commit/98ca6462f82b24cfa9a1089b0f77f43454ccad68))
* autobump bio/filtlong ([#2241](https://www.github.com/snakemake/snakemake-wrappers/issues/2241)) ([2a5123f](https://www.github.com/snakemake/snakemake-wrappers/commit/2a5123f41cece081a3e03dd6c5a469552c8f585b))
* autobump bio/paladin/align ([#2270](https://www.github.com/snakemake/snakemake-wrappers/issues/2270)) ([e1d5293](https://www.github.com/snakemake/snakemake-wrappers/commit/e1d529342208c505a9aa25c09a288c9078ef9985))
* autobump bio/paladin/prepare ([#2277](https://www.github.com/snakemake/snakemake-wrappers/issues/2277)) ([5615116](https://www.github.com/snakemake/snakemake-wrappers/commit/5615116982038ef123b7eaeb63dd041a1df831bd))
* autobump bio/pbmm2/align ([#2269](https://www.github.com/snakemake/snakemake-wrappers/issues/2269)) ([6f2f6cf](https://www.github.com/snakemake/snakemake-wrappers/commit/6f2f6cf58aef9988fb2af0d2ee378a3c6c6d0234))
* autobump bio/pbmm2/index ([#2273](https://www.github.com/snakemake/snakemake-wrappers/issues/2273)) ([95eea96](https://www.github.com/snakemake/snakemake-wrappers/commit/95eea9646ddba88a5d38d945b75b6ef1d927e395))
* autobump bio/pear ([#2266](https://www.github.com/snakemake/snakemake-wrappers/issues/2266)) ([294be33](https://www.github.com/snakemake/snakemake-wrappers/commit/294be3391a8bb1704ebfab3e704df0749c4f286d))
* autobump bio/picard/addorreplacereadgroups ([#2259](https://www.github.com/snakemake/snakemake-wrappers/issues/2259)) ([bc422f3](https://www.github.com/snakemake/snakemake-wrappers/commit/bc422f3a7742faa648e421952d249e9452e1bed2))
* autobump bio/picard/bedtointervallist ([#2272](https://www.github.com/snakemake/snakemake-wrappers/issues/2272)) ([203b36a](https://www.github.com/snakemake/snakemake-wrappers/commit/203b36a4087ba4960f436d885961b71c6d4581d5))
* autobump bio/picard/collectalignmentsummarymetrics ([#2262](https://www.github.com/snakemake/snakemake-wrappers/issues/2262)) ([41e8dde](https://www.github.com/snakemake/snakemake-wrappers/commit/41e8dde0ecb9e4d7048cff9951d0806a31124c66))
* autobump bio/picard/collectgcbiasmetrics ([#2256](https://www.github.com/snakemake/snakemake-wrappers/issues/2256)) ([80b3cf6](https://www.github.com/snakemake/snakemake-wrappers/commit/80b3cf6b92cafc0e621a9829ff8ae9005d7f5d71))
* autobump bio/picard/collecthsmetrics ([#2257](https://www.github.com/snakemake/snakemake-wrappers/issues/2257)) ([ae663c2](https://www.github.com/snakemake/snakemake-wrappers/commit/ae663c2e72d5956625b8f107e78d3d3cc3ca0412))
* autobump bio/picard/collectinsertsizemetrics ([#2261](https://www.github.com/snakemake/snakemake-wrappers/issues/2261)) ([ef362b3](https://www.github.com/snakemake/snakemake-wrappers/commit/ef362b3cbcd7e8138c54e5ae57347d86bd1e1e6d))
* autobump bio/picard/collectmultiplemetrics ([#2248](https://www.github.com/snakemake/snakemake-wrappers/issues/2248)) ([f73efb6](https://www.github.com/snakemake/snakemake-wrappers/commit/f73efb6a6f30c51382a2837fb4d82769d2425286))
* autobump bio/picard/collectrnaseqmetrics ([#2250](https://www.github.com/snakemake/snakemake-wrappers/issues/2250)) ([c4f541b](https://www.github.com/snakemake/snakemake-wrappers/commit/c4f541b80a3a0cc2b85affc703aa02d6104f8add))
* autobump bio/picard/collecttargetedpcrmetrics ([#2263](https://www.github.com/snakemake/snakemake-wrappers/issues/2263)) ([2fb4af9](https://www.github.com/snakemake/snakemake-wrappers/commit/2fb4af954402e0ea66ae8b4494265c54f16fee21))
* autobump bio/picard/markduplicates ([#2276](https://www.github.com/snakemake/snakemake-wrappers/issues/2276)) ([93933d4](https://www.github.com/snakemake/snakemake-wrappers/commit/93933d408142d73093cdc87890faf1dc99de0452))
* autobump bio/picard/mergevcfs ([#2271](https://www.github.com/snakemake/snakemake-wrappers/issues/2271)) ([302d1ff](https://www.github.com/snakemake/snakemake-wrappers/commit/302d1ff942bdf57bb40fef322c018f1000b75585))
* autobump bio/picard/revertsam ([#2285](https://www.github.com/snakemake/snakemake-wrappers/issues/2285)) ([eee4daf](https://www.github.com/snakemake/snakemake-wrappers/commit/eee4daf752233ff0647b300fcb92499712ce0daf))
* autobump bio/picard/samtofastq ([#2280](https://www.github.com/snakemake/snakemake-wrappers/issues/2280)) ([803ddec](https://www.github.com/snakemake/snakemake-wrappers/commit/803ddec608bfd3414000f5285f6ebb9df588d3e8))
* autobump bio/picard/sortsam ([#2258](https://www.github.com/snakemake/snakemake-wrappers/issues/2258)) ([118b70d](https://www.github.com/snakemake/snakemake-wrappers/commit/118b70d5fa85cf257a2c29c71da4f9a0e4362fc9))
* autobump bio/pindel/call ([#2275](https://www.github.com/snakemake/snakemake-wrappers/issues/2275)) ([45c52d3](https://www.github.com/snakemake/snakemake-wrappers/commit/45c52d3b01b4e3f25d2682bfc2fdf67e8c7187df))
* autobump bio/pindel/pindel2vcf ([#2281](https://www.github.com/snakemake/snakemake-wrappers/issues/2281)) ([5ffe4bc](https://www.github.com/snakemake/snakemake-wrappers/commit/5ffe4bce3c7c7d07bce713b198f55402b2924bff))
* autobump bio/plass ([#2264](https://www.github.com/snakemake/snakemake-wrappers/issues/2264)) ([0d8ca7f](https://www.github.com/snakemake/snakemake-wrappers/commit/0d8ca7f058256c5e6aaba74030daa750639a056d))
* autobump bio/preseq/lc_extrap ([#2254](https://www.github.com/snakemake/snakemake-wrappers/issues/2254)) ([538e322](https://www.github.com/snakemake/snakemake-wrappers/commit/538e322bf3d3ad7f7c1a616d66b4b30c37113ead))
* autobump bio/pretext/graph ([#2251](https://www.github.com/snakemake/snakemake-wrappers/issues/2251)) ([f3c7296](https://www.github.com/snakemake/snakemake-wrappers/commit/f3c7296371f1dfd61753ea8b78f1d9c32413084f))
* autobump bio/pretext/map ([#2265](https://www.github.com/snakemake/snakemake-wrappers/issues/2265)) ([c6c35f8](https://www.github.com/snakemake/snakemake-wrappers/commit/c6c35f805cd933957f83700ac36540f15ca34a0a))
* autobump bio/pretext/snapshot ([#2282](https://www.github.com/snakemake/snakemake-wrappers/issues/2282)) ([a7358b9](https://www.github.com/snakemake/snakemake-wrappers/commit/a7358b9a2af8c34c9bd542b56aa4a49891d00ec2))
* autobump bio/prosolo/control-fdr ([#2268](https://www.github.com/snakemake/snakemake-wrappers/issues/2268)) ([c55a9ec](https://www.github.com/snakemake/snakemake-wrappers/commit/c55a9ecdbd2bfaa73525192ca8bd2ca8d62d6471))
* autobump bio/prosolo/single-cell-bulk ([#2253](https://www.github.com/snakemake/snakemake-wrappers/issues/2253)) ([03d4f9f](https://www.github.com/snakemake/snakemake-wrappers/commit/03d4f9f151edc5cdeee890510c37cd98bccc3b20))
* autobump bio/ptrimmer ([#2284](https://www.github.com/snakemake/snakemake-wrappers/issues/2284)) ([105ffd9](https://www.github.com/snakemake/snakemake-wrappers/commit/105ffd973ec63a61a6a78a185a899ee1d40cf682))
* autobump bio/purge_dups/calcuts ([#2249](https://www.github.com/snakemake/snakemake-wrappers/issues/2249)) ([72397c2](https://www.github.com/snakemake/snakemake-wrappers/commit/72397c20d4b8b1870c1588baf0aace517a03d1d6))
* autobump bio/purge_dups/get_seqs ([#2252](https://www.github.com/snakemake/snakemake-wrappers/issues/2252)) ([25a113c](https://www.github.com/snakemake/snakemake-wrappers/commit/25a113cec300a14f805b588ac27b19dd94c28c87))
* autobump bio/purge_dups/ngscstat ([#2267](https://www.github.com/snakemake/snakemake-wrappers/issues/2267)) ([f4e2068](https://www.github.com/snakemake/snakemake-wrappers/commit/f4e206860cec2518c14395278b509f6fab447b7b))
* autobump bio/purge_dups/pbcstat ([#2283](https://www.github.com/snakemake/snakemake-wrappers/issues/2283)) ([3893aa0](https://www.github.com/snakemake/snakemake-wrappers/commit/3893aa0a90fa15bbf3cfccf2b0cfcb8c8c6f0c8b))
* autobump bio/purge_dups/purge_dups ([#2278](https://www.github.com/snakemake/snakemake-wrappers/issues/2278)) ([a08e8f8](https://www.github.com/snakemake/snakemake-wrappers/commit/a08e8f83dbc62c06ceb5036c717f9d2b8e605f70))
* autobump bio/purge_dups/split_fa ([#2279](https://www.github.com/snakemake/snakemake-wrappers/issues/2279)) ([26dbb9e](https://www.github.com/snakemake/snakemake-wrappers/commit/26dbb9e5e5fa5f5454a470fb9000b254c4d77130))
* autobump bio/pyroe/idtoname ([#2274](https://www.github.com/snakemake/snakemake-wrappers/issues/2274)) ([76b9d89](https://www.github.com/snakemake/snakemake-wrappers/commit/76b9d8985f1a1d33b0815216404868e46b4c4d86))
* autobump bio/pyroe/makesplicedintronic ([#2255](https://www.github.com/snakemake/snakemake-wrappers/issues/2255)) ([436c1f8](https://www.github.com/snakemake/snakemake-wrappers/commit/436c1f8cd2a5a0674dbff22e24d02eb8aac1c855))
* autobump bio/pyroe/makeunspliceunspliced ([#2260](https://www.github.com/snakemake/snakemake-wrappers/issues/2260)) ([1da192d](https://www.github.com/snakemake/snakemake-wrappers/commit/1da192d80edc26fb03e8fa686cb40059ea535f35))
* autobump bio/ucsc/faToTwoBit ([#2286](https://www.github.com/snakemake/snakemake-wrappers/issues/2286)) ([93ba408](https://www.github.com/snakemake/snakemake-wrappers/commit/93ba4089edf02360c7ba1c195f76e4785e02a694))
* autobump bio/ucsc/twoBitToFa ([#2287](https://www.github.com/snakemake/snakemake-wrappers/issues/2287)) ([03447e8](https://www.github.com/snakemake/snakemake-wrappers/commit/03447e84d2184101967ad6bc75118a8cf1f28cf8))

### [2.9.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.9.0...v2.9.1) (2023-11-01)


### Performance Improvements

* autobump bio/adapterremoval ([#1914](https://www.github.com/snakemake/snakemake-wrappers/issues/1914)) ([ca25e3d](https://www.github.com/snakemake/snakemake-wrappers/commit/ca25e3d612d7a7b5a30e9dd968b68555582eb04d))
* autobump bio/arriba ([#1915](https://www.github.com/snakemake/snakemake-wrappers/issues/1915)) ([a4d53df](https://www.github.com/snakemake/snakemake-wrappers/commit/a4d53df430d818ba6d451d07998e14d857f9af03))
* autobump bio/art/profiler_illumina ([#1913](https://www.github.com/snakemake/snakemake-wrappers/issues/1913)) ([8beb04c](https://www.github.com/snakemake/snakemake-wrappers/commit/8beb04ccc52669db50e60f3f575b2c4a6fe2bf16))
* autobump bio/assembly-stats ([#1916](https://www.github.com/snakemake/snakemake-wrappers/issues/1916)) ([e7e4bb9](https://www.github.com/snakemake/snakemake-wrappers/commit/e7e4bb9a5baa120621765cfd230968620b0726b3))
* autobump bio/bamtools/filter ([#1935](https://www.github.com/snakemake/snakemake-wrappers/issues/1935)) ([92b7ce5](https://www.github.com/snakemake/snakemake-wrappers/commit/92b7ce5a20b98cb695444f2a5810f3e364d3da5c))
* autobump bio/bamtools/filter_json ([#1960](https://www.github.com/snakemake/snakemake-wrappers/issues/1960)) ([b4d740e](https://www.github.com/snakemake/snakemake-wrappers/commit/b4d740e699e42630aaae815738bfd7674e34abac))
* autobump bio/bamtools/split ([#1944](https://www.github.com/snakemake/snakemake-wrappers/issues/1944)) ([1860890](https://www.github.com/snakemake/snakemake-wrappers/commit/1860890dadfa61f63316d165943dca48248ffb69))
* autobump bio/bamtools/stats ([#1968](https://www.github.com/snakemake/snakemake-wrappers/issues/1968)) ([a221925](https://www.github.com/snakemake/snakemake-wrappers/commit/a22192501ae2fbae1a2d41963993fafed039e738))
* autobump bio/barrnap ([#1921](https://www.github.com/snakemake/snakemake-wrappers/issues/1921)) ([52a7360](https://www.github.com/snakemake/snakemake-wrappers/commit/52a7360ea76dda6aa991e7fb54b9f1e06badcd1d))
* autobump bio/bazam ([#1950](https://www.github.com/snakemake/snakemake-wrappers/issues/1950)) ([6daa3ad](https://www.github.com/snakemake/snakemake-wrappers/commit/6daa3ad5661e98df5830cbcd54a7fc0023efe8bc))
* autobump bio/bcftools/call ([#1954](https://www.github.com/snakemake/snakemake-wrappers/issues/1954)) ([4827897](https://www.github.com/snakemake/snakemake-wrappers/commit/48278971c6f19f372fcdace0da3a79a49e7c291a))
* autobump bio/bcftools/concat ([#1958](https://www.github.com/snakemake/snakemake-wrappers/issues/1958)) ([db356f5](https://www.github.com/snakemake/snakemake-wrappers/commit/db356f586b5a2d98d6a438e9e689b1de74451cd8))
* autobump bio/bcftools/filter ([#1947](https://www.github.com/snakemake/snakemake-wrappers/issues/1947)) ([43d2237](https://www.github.com/snakemake/snakemake-wrappers/commit/43d223741070e2bb03be6b8b1708f64566cdbb7c))
* autobump bio/bcftools/index ([#1937](https://www.github.com/snakemake/snakemake-wrappers/issues/1937)) ([6cd5422](https://www.github.com/snakemake/snakemake-wrappers/commit/6cd5422f6165b4fc270493f3b2d72e70fb813317))
* autobump bio/bcftools/merge ([#1930](https://www.github.com/snakemake/snakemake-wrappers/issues/1930)) ([aa26661](https://www.github.com/snakemake/snakemake-wrappers/commit/aa26661f9f53475fc51472c07d30d9c61d0864d2))
* autobump bio/bcftools/mpileup ([#1949](https://www.github.com/snakemake/snakemake-wrappers/issues/1949)) ([df4469e](https://www.github.com/snakemake/snakemake-wrappers/commit/df4469e92a8c933cba75f0797e51550acd2824f3))
* autobump bio/bcftools/norm ([#1975](https://www.github.com/snakemake/snakemake-wrappers/issues/1975)) ([769e84e](https://www.github.com/snakemake/snakemake-wrappers/commit/769e84e1382f55bb308c11cd4fd712f639088dd7))
* autobump bio/bcftools/reheader ([#1926](https://www.github.com/snakemake/snakemake-wrappers/issues/1926)) ([767f5f8](https://www.github.com/snakemake/snakemake-wrappers/commit/767f5f847c391782bce0eb218b7b6a4c1db6edfb))
* autobump bio/bcftools/sort ([#1962](https://www.github.com/snakemake/snakemake-wrappers/issues/1962)) ([d113d02](https://www.github.com/snakemake/snakemake-wrappers/commit/d113d02c2f25cf902ea711f90835501d5c834d36))
* autobump bio/bcftools/stats ([#1932](https://www.github.com/snakemake/snakemake-wrappers/issues/1932)) ([ac1725b](https://www.github.com/snakemake/snakemake-wrappers/commit/ac1725b682dc16798702d3ff4bd614bed4741fa0))
* autobump bio/bcftools/view ([#1936](https://www.github.com/snakemake/snakemake-wrappers/issues/1936)) ([34b12ac](https://www.github.com/snakemake/snakemake-wrappers/commit/34b12acea8b1ef68840bbbc18b479af10d4da6cd))
* autobump bio/bedtools/bamtobed ([#1956](https://www.github.com/snakemake/snakemake-wrappers/issues/1956)) ([0a50372](https://www.github.com/snakemake/snakemake-wrappers/commit/0a503722e3931fd0c72a2f5f3647f6bfd7bd8ffb))
* autobump bio/bedtools/complement ([#1925](https://www.github.com/snakemake/snakemake-wrappers/issues/1925)) ([2116c8b](https://www.github.com/snakemake/snakemake-wrappers/commit/2116c8b1f67b56a6d7c9b8984c5337e3afd5a921))
* autobump bio/bedtools/coveragebed ([#1970](https://www.github.com/snakemake/snakemake-wrappers/issues/1970)) ([3a04846](https://www.github.com/snakemake/snakemake-wrappers/commit/3a04846171c84ccaf4db19f603a18280f5fa9dfa))
* autobump bio/bedtools/genomecov ([#1938](https://www.github.com/snakemake/snakemake-wrappers/issues/1938)) ([92c9e9d](https://www.github.com/snakemake/snakemake-wrappers/commit/92c9e9d11f833ee001bbe26fd4b1569c97c92cbc))
* autobump bio/bedtools/intersect ([#1976](https://www.github.com/snakemake/snakemake-wrappers/issues/1976)) ([c90f102](https://www.github.com/snakemake/snakemake-wrappers/commit/c90f1026372c81196ef4364d9d5ce969cb34e8f9))
* autobump bio/bedtools/merge ([#1963](https://www.github.com/snakemake/snakemake-wrappers/issues/1963)) ([e5ac112](https://www.github.com/snakemake/snakemake-wrappers/commit/e5ac11205fba5999e45a38640ac1c0eaf83e3ed7))
* autobump bio/bedtools/slop ([#1955](https://www.github.com/snakemake/snakemake-wrappers/issues/1955)) ([569c089](https://www.github.com/snakemake/snakemake-wrappers/commit/569c089f6076f4f491960f4b5131f1a3381ec977))
* autobump bio/bedtools/sort ([#1971](https://www.github.com/snakemake/snakemake-wrappers/issues/1971)) ([5687f4f](https://www.github.com/snakemake/snakemake-wrappers/commit/5687f4fab86bbc89164ab816dc41772bf079622b))
* autobump bio/bedtools/split ([#1939](https://www.github.com/snakemake/snakemake-wrappers/issues/1939)) ([333dbcd](https://www.github.com/snakemake/snakemake-wrappers/commit/333dbcdd6dc9d3598af68123230bfc03717d8f6f))
* autobump bio/bellerophon ([#1969](https://www.github.com/snakemake/snakemake-wrappers/issues/1969)) ([cd4cc86](https://www.github.com/snakemake/snakemake-wrappers/commit/cd4cc866995fbf1208633eccdffd952cb7b52328))
* autobump bio/benchmark/chm-eval ([#1927](https://www.github.com/snakemake/snakemake-wrappers/issues/1927)) ([0cd3b22](https://www.github.com/snakemake/snakemake-wrappers/commit/0cd3b22c09a595aa0b9b8d13d9d478f2fbfcfec1))
* autobump bio/benchmark/chm-eval-kit ([#1922](https://www.github.com/snakemake/snakemake-wrappers/issues/1922)) ([b58dcf9](https://www.github.com/snakemake/snakemake-wrappers/commit/b58dcf9062fcf7ca6136f3155b154c84f00d49cd))
* autobump bio/benchmark/chm-eval-sample ([#1864](https://www.github.com/snakemake/snakemake-wrappers/issues/1864)) ([3e64b5f](https://www.github.com/snakemake/snakemake-wrappers/commit/3e64b5f737b8266f406fb4dc2bd7369501083485))
* autobump bio/bgzip ([#1966](https://www.github.com/snakemake/snakemake-wrappers/issues/1966)) ([ea9e8af](https://www.github.com/snakemake/snakemake-wrappers/commit/ea9e8af3be977f1bcfb771ce4a177d33143678cc))
* autobump bio/biobambam2/bamsormadup ([#1967](https://www.github.com/snakemake/snakemake-wrappers/issues/1967)) ([3e45960](https://www.github.com/snakemake/snakemake-wrappers/commit/3e4596017e04cf131b64914c23d3f7604a41ae89))
* autobump bio/bismark/bam2nuc ([#1964](https://www.github.com/snakemake/snakemake-wrappers/issues/1964)) ([5a9bbb1](https://www.github.com/snakemake/snakemake-wrappers/commit/5a9bbb185c6ab8f4d18fab1006b67e99f8539b13))
* autobump bio/bismark/bismark ([#1943](https://www.github.com/snakemake/snakemake-wrappers/issues/1943)) ([4c0f9e1](https://www.github.com/snakemake/snakemake-wrappers/commit/4c0f9e19e57a08e7f71f377f0fdfb89e06947f0a))
* autobump bio/bismark/bismark_genome_preparation ([#1957](https://www.github.com/snakemake/snakemake-wrappers/issues/1957)) ([1519191](https://www.github.com/snakemake/snakemake-wrappers/commit/1519191fb1c18e128fdf49fa008a29e4815ec6cd))
* autobump bio/bismark/bismark_methylation_extractor ([#1951](https://www.github.com/snakemake/snakemake-wrappers/issues/1951)) ([75b2628](https://www.github.com/snakemake/snakemake-wrappers/commit/75b262898d8d4b3ad449772be3f8092e36c16bdf))
* autobump bio/bismark/bismark2bedGraph ([#1940](https://www.github.com/snakemake/snakemake-wrappers/issues/1940)) ([4552c42](https://www.github.com/snakemake/snakemake-wrappers/commit/4552c429e1fec1d4f4d2dccce63667970d14d89d))
* autobump bio/bismark/bismark2report ([#1974](https://www.github.com/snakemake/snakemake-wrappers/issues/1974)) ([066760b](https://www.github.com/snakemake/snakemake-wrappers/commit/066760bdfb6c856a79d81f9da9a43ee63beaedf6))
* autobump bio/bismark/bismark2summary ([#1923](https://www.github.com/snakemake/snakemake-wrappers/issues/1923)) ([9c6ae90](https://www.github.com/snakemake/snakemake-wrappers/commit/9c6ae90ad6ccf9f892434929f7f373f256577ff5))
* autobump bio/bismark/deduplicate_bismark ([#1945](https://www.github.com/snakemake/snakemake-wrappers/issues/1945)) ([f0dd808](https://www.github.com/snakemake/snakemake-wrappers/commit/f0dd808cd22169557b40ba15178e195ec42fe10f))
* autobump bio/blast/blastn ([#1961](https://www.github.com/snakemake/snakemake-wrappers/issues/1961)) ([2515cb0](https://www.github.com/snakemake/snakemake-wrappers/commit/2515cb019655a2a8611e14446bbc54866949fc6a))
* autobump bio/blast/makeblastdb ([#1920](https://www.github.com/snakemake/snakemake-wrappers/issues/1920)) ([7450d51](https://www.github.com/snakemake/snakemake-wrappers/commit/7450d51c243dddc2ba5e09b5a6a475e0b8ed84f9))
* autobump bio/bowtie2/align ([#1942](https://www.github.com/snakemake/snakemake-wrappers/issues/1942)) ([184bf6d](https://www.github.com/snakemake/snakemake-wrappers/commit/184bf6d505c134e4421c03206c4de5103eb1a973))
* autobump bio/bowtie2/build ([#1931](https://www.github.com/snakemake/snakemake-wrappers/issues/1931)) ([78816da](https://www.github.com/snakemake/snakemake-wrappers/commit/78816daddcff71b647366c5294f485d245f4dec9))
* autobump bio/busco ([#1959](https://www.github.com/snakemake/snakemake-wrappers/issues/1959)) ([68b89c1](https://www.github.com/snakemake/snakemake-wrappers/commit/68b89c1b73c82dd2470df7d60be6de995835a7a8))
* autobump bio/bustools/count ([#1946](https://www.github.com/snakemake/snakemake-wrappers/issues/1946)) ([c3d8ce1](https://www.github.com/snakemake/snakemake-wrappers/commit/c3d8ce17bc51eebd8e00c7c138ad8542b708f2a6))
* autobump bio/bustools/sort ([#1952](https://www.github.com/snakemake/snakemake-wrappers/issues/1952)) ([6a2683a](https://www.github.com/snakemake/snakemake-wrappers/commit/6a2683abd023a6489e5ce309fb0b0ac34b667e61))
* autobump bio/bustools/text ([#1972](https://www.github.com/snakemake/snakemake-wrappers/issues/1972)) ([117f641](https://www.github.com/snakemake/snakemake-wrappers/commit/117f641f811cbb02fbae4dc2eadf452394d83a34))
* autobump bio/bwa-mem2/index ([#1918](https://www.github.com/snakemake/snakemake-wrappers/issues/1918)) ([20f6612](https://www.github.com/snakemake/snakemake-wrappers/commit/20f66120ea207051d8643fe2981c1a5b38c5152c))
* autobump bio/bwa-mem2/mem ([#1977](https://www.github.com/snakemake/snakemake-wrappers/issues/1977)) ([aae544a](https://www.github.com/snakemake/snakemake-wrappers/commit/aae544a051f09fcfc8a80959638bf5f32962486b))
* autobump bio/bwa-mem2/mem-samblaster ([#1928](https://www.github.com/snakemake/snakemake-wrappers/issues/1928)) ([38625be](https://www.github.com/snakemake/snakemake-wrappers/commit/38625be971c7a395f6ede55f1f84b2887e727ae1))
* autobump bio/bwa-meme/index ([#1917](https://www.github.com/snakemake/snakemake-wrappers/issues/1917)) ([ad4ac89](https://www.github.com/snakemake/snakemake-wrappers/commit/ad4ac89377ff29c9ed2743d1d9095d1c6dcb10af))
* autobump bio/bwa-meme/mem ([#1965](https://www.github.com/snakemake/snakemake-wrappers/issues/1965)) ([3e7aa09](https://www.github.com/snakemake/snakemake-wrappers/commit/3e7aa09441a879024c4a3cc27bba29d90ef8a0a8))
* autobump bio/bwa-memx/index ([#1933](https://www.github.com/snakemake/snakemake-wrappers/issues/1933)) ([baaf832](https://www.github.com/snakemake/snakemake-wrappers/commit/baaf8324a7c17a97cea63d6b3a5806ef7a63858e))
* autobump bio/bwa-memx/mem ([#1924](https://www.github.com/snakemake/snakemake-wrappers/issues/1924)) ([67aa9b7](https://www.github.com/snakemake/snakemake-wrappers/commit/67aa9b7a6982b29aa388d4d3164ae3e12ad9560a))
* autobump bio/bwa/aln ([#1929](https://www.github.com/snakemake/snakemake-wrappers/issues/1929)) ([ad52a2a](https://www.github.com/snakemake/snakemake-wrappers/commit/ad52a2a0cfa5679e291b16df43450f8ea4b556dd))
* autobump bio/bwa/index ([#1948](https://www.github.com/snakemake/snakemake-wrappers/issues/1948)) ([ad29c43](https://www.github.com/snakemake/snakemake-wrappers/commit/ad29c43daf8d0401fb77b8f329014721e0582bc4))
* autobump bio/bwa/mem ([#1953](https://www.github.com/snakemake/snakemake-wrappers/issues/1953)) ([9b8f65a](https://www.github.com/snakemake/snakemake-wrappers/commit/9b8f65a6bf8613b815765da7b41ce6a4b3fe9e14))
* autobump bio/bwa/mem-samblaster ([#1941](https://www.github.com/snakemake/snakemake-wrappers/issues/1941)) ([0c15ceb](https://www.github.com/snakemake/snakemake-wrappers/commit/0c15ceb8902eb5e60092cca052851b6d12a9d081))
* autobump bio/bwa/sampe ([#1934](https://www.github.com/snakemake/snakemake-wrappers/issues/1934)) ([57702a5](https://www.github.com/snakemake/snakemake-wrappers/commit/57702a5f84a2cfdfdfc8cbd09deff72745ee033b))
* autobump bio/bwa/samse ([#1973](https://www.github.com/snakemake/snakemake-wrappers/issues/1973)) ([0326445](https://www.github.com/snakemake/snakemake-wrappers/commit/0326445271ec0e731bf2d47c558c607478e441d9))
* autobump bio/bwa/samxe ([#1919](https://www.github.com/snakemake/snakemake-wrappers/issues/1919)) ([2928b60](https://www.github.com/snakemake/snakemake-wrappers/commit/2928b6085e57796c3502535986c33f7845069fca))
* autobump bio/clustalo ([#1984](https://www.github.com/snakemake/snakemake-wrappers/issues/1984)) ([7b07764](https://www.github.com/snakemake/snakemake-wrappers/commit/7b077640aa2bb2ae56499fd1699f976a0cc88b81))
* autobump bio/cnv_facets ([#1991](https://www.github.com/snakemake/snakemake-wrappers/issues/1991)) ([e37a14c](https://www.github.com/snakemake/snakemake-wrappers/commit/e37a14c5e6ad64a16bc3e41ffaed37d16467f0ba))
* autobump bio/cnvkit/antitarget ([#1992](https://www.github.com/snakemake/snakemake-wrappers/issues/1992)) ([c1b0e27](https://www.github.com/snakemake/snakemake-wrappers/commit/c1b0e2755543ffd934db6a21fb99aea28305afc2))
* autobump bio/cnvkit/batch ([#1994](https://www.github.com/snakemake/snakemake-wrappers/issues/1994)) ([cbabb15](https://www.github.com/snakemake/snakemake-wrappers/commit/cbabb15c10c4ce3fc361525d152d02186ceac163))
* autobump bio/cnvkit/call ([#1989](https://www.github.com/snakemake/snakemake-wrappers/issues/1989)) ([627ee34](https://www.github.com/snakemake/snakemake-wrappers/commit/627ee34e2301b2814121addbc7484e3737326883))
* autobump bio/cnvkit/diagram ([#1993](https://www.github.com/snakemake/snakemake-wrappers/issues/1993)) ([ae3cb53](https://www.github.com/snakemake/snakemake-wrappers/commit/ae3cb53f4c65b8c73c729c1cf7a67b36184db195))
* autobump bio/cnvkit/export ([#1983](https://www.github.com/snakemake/snakemake-wrappers/issues/1983)) ([5345405](https://www.github.com/snakemake/snakemake-wrappers/commit/534540582f2cad85b36ad18332e320e718a7e1de))
* autobump bio/cnvkit/target ([#1980](https://www.github.com/snakemake/snakemake-wrappers/issues/1980)) ([e504191](https://www.github.com/snakemake/snakemake-wrappers/commit/e50419194e8bd28297975fe35a934c16848b70a0))
* autobump bio/coolpuppy ([#1979](https://www.github.com/snakemake/snakemake-wrappers/issues/1979)) ([aba480d](https://www.github.com/snakemake/snakemake-wrappers/commit/aba480d23472508c698460b22ce7feca20a58002))
* autobump bio/cooltools/dots ([#1990](https://www.github.com/snakemake/snakemake-wrappers/issues/1990)) ([c03cb9f](https://www.github.com/snakemake/snakemake-wrappers/commit/c03cb9fe84a77cd35ecca0b7a9b45a8a026092de))
* autobump bio/cooltools/eigs_cis ([#1987](https://www.github.com/snakemake/snakemake-wrappers/issues/1987)) ([0055391](https://www.github.com/snakemake/snakemake-wrappers/commit/0055391973ca477bcd7b247a730ee6ebeec12fb1))
* autobump bio/cooltools/eigs_trans ([#1978](https://www.github.com/snakemake/snakemake-wrappers/issues/1978)) ([78083df](https://www.github.com/snakemake/snakemake-wrappers/commit/78083df3c30bb8e02b12965b1250a42b079ce168))
* autobump bio/cooltools/expected_cis ([#1909](https://www.github.com/snakemake/snakemake-wrappers/issues/1909)) ([2b970d5](https://www.github.com/snakemake/snakemake-wrappers/commit/2b970d5b3a62bae208a5185d524aebb0e69e2cc4))
* autobump bio/cooltools/expected_trans ([#1981](https://www.github.com/snakemake/snakemake-wrappers/issues/1981)) ([5c790a4](https://www.github.com/snakemake/snakemake-wrappers/commit/5c790a44bcb871429d03e62f419d82d39cc917c2))
* autobump bio/cooltools/insulation ([#1995](https://www.github.com/snakemake/snakemake-wrappers/issues/1995)) ([1155a97](https://www.github.com/snakemake/snakemake-wrappers/commit/1155a974865187232ff060ac1091f4c08c6d7498))
* autobump bio/cooltools/pileup ([#1986](https://www.github.com/snakemake/snakemake-wrappers/issues/1986)) ([d143516](https://www.github.com/snakemake/snakemake-wrappers/commit/d1435160100a912fd441d6f9c052c80e321c3405))
* autobump bio/cooltools/saddle ([#1985](https://www.github.com/snakemake/snakemake-wrappers/issues/1985)) ([4eba46c](https://www.github.com/snakemake/snakemake-wrappers/commit/4eba46c9cc27eab6f3cefcba50d874a0abfe582e))
* autobump bio/cutadapt/pe ([#1988](https://www.github.com/snakemake/snakemake-wrappers/issues/1988)) ([e8fb356](https://www.github.com/snakemake/snakemake-wrappers/commit/e8fb35674cf9a274a8058460c51fcf65dbd1f329))
* autobump bio/cutadapt/se ([#1982](https://www.github.com/snakemake/snakemake-wrappers/issues/1982)) ([1e1b57c](https://www.github.com/snakemake/snakemake-wrappers/commit/1e1b57cbae8609f65fd91b39f5ac5ac59fa3aa00))
* autobump bio/dada2/add-species ([#2010](https://www.github.com/snakemake/snakemake-wrappers/issues/2010)) ([104d101](https://www.github.com/snakemake/snakemake-wrappers/commit/104d1015221b39c2f2ad417448df155b8c66e7c3))
* autobump bio/dada2/assign-species ([#1998](https://www.github.com/snakemake/snakemake-wrappers/issues/1998)) ([f535959](https://www.github.com/snakemake/snakemake-wrappers/commit/f535959f27e7f48aa8e6cf34ee4b7f27d855cca7))
* autobump bio/dada2/assign-taxonomy ([#2013](https://www.github.com/snakemake/snakemake-wrappers/issues/2013)) ([f471539](https://www.github.com/snakemake/snakemake-wrappers/commit/f471539cf60238f4e95ee5aca3660eb19ad4bceb))
* autobump bio/dada2/collapse-nomismatch ([#1908](https://www.github.com/snakemake/snakemake-wrappers/issues/1908)) ([2453cdc](https://www.github.com/snakemake/snakemake-wrappers/commit/2453cdcdf223c6b44da06120c87b37113de96b63))
* autobump bio/dada2/dereplicate-fastq ([#2017](https://www.github.com/snakemake/snakemake-wrappers/issues/2017)) ([5fd2868](https://www.github.com/snakemake/snakemake-wrappers/commit/5fd2868d67edfb985f251e90146052683c59f6bd))
* autobump bio/dada2/filter-trim ([#2019](https://www.github.com/snakemake/snakemake-wrappers/issues/2019)) ([a907ef4](https://www.github.com/snakemake/snakemake-wrappers/commit/a907ef496a0885abad127ccf7fd939fed2d40b0c))
* autobump bio/dada2/learn-errors ([#1999](https://www.github.com/snakemake/snakemake-wrappers/issues/1999)) ([aae7fca](https://www.github.com/snakemake/snakemake-wrappers/commit/aae7fca671835a02af3dbbca39193c46bd967ec4))
* autobump bio/dada2/make-table ([#2006](https://www.github.com/snakemake/snakemake-wrappers/issues/2006)) ([b6644e2](https://www.github.com/snakemake/snakemake-wrappers/commit/b6644e2a8fa33fb40d3aeaadfa90112de68af78a))
* autobump bio/dada2/merge-pairs ([#2012](https://www.github.com/snakemake/snakemake-wrappers/issues/2012)) ([76127d2](https://www.github.com/snakemake/snakemake-wrappers/commit/76127d295adceed88a8134327920da840d2db53c))
* autobump bio/dada2/quality-profile ([#2004](https://www.github.com/snakemake/snakemake-wrappers/issues/2004)) ([55b3e07](https://www.github.com/snakemake/snakemake-wrappers/commit/55b3e074cd56d0c9098b2f65c1791a0fd32d13bf))
* autobump bio/dada2/remove-chimeras ([#2005](https://www.github.com/snakemake/snakemake-wrappers/issues/2005)) ([33ec8f8](https://www.github.com/snakemake/snakemake-wrappers/commit/33ec8f8e9d5822eb5ee5a5412708a9f62067b4d6))
* autobump bio/dada2/sample-inference ([#2018](https://www.github.com/snakemake/snakemake-wrappers/issues/2018)) ([651c9d1](https://www.github.com/snakemake/snakemake-wrappers/commit/651c9d19937c2b8a2b850d5aecd21f8b7f8ada14))
* autobump bio/deeptools/alignmentsieve ([#2007](https://www.github.com/snakemake/snakemake-wrappers/issues/2007)) ([3b681f7](https://www.github.com/snakemake/snakemake-wrappers/commit/3b681f76c68a1d8b8e66fda2235b068cf780e1b1))
* autobump bio/deeptools/bamcoverage ([#2011](https://www.github.com/snakemake/snakemake-wrappers/issues/2011)) ([94bfb0d](https://www.github.com/snakemake/snakemake-wrappers/commit/94bfb0daa255a5fb3177d458594f9c75ccb8c7f5))
* autobump bio/deeptools/computematrix ([#2003](https://www.github.com/snakemake/snakemake-wrappers/issues/2003)) ([441c5ad](https://www.github.com/snakemake/snakemake-wrappers/commit/441c5adb202af63ca4a52da87212b6a98bcd2607))
* autobump bio/deeptools/plotcoverage ([#2015](https://www.github.com/snakemake/snakemake-wrappers/issues/2015)) ([0a616d6](https://www.github.com/snakemake/snakemake-wrappers/commit/0a616d654b4dedbf82d4a2e18be6e5a288fc6b27))
* autobump bio/deeptools/plotfingerprint ([#2001](https://www.github.com/snakemake/snakemake-wrappers/issues/2001)) ([576d41a](https://www.github.com/snakemake/snakemake-wrappers/commit/576d41ae4aa4b28c7c571c8d39e3a5d794b89eb7))
* autobump bio/deeptools/plotheatmap ([#1997](https://www.github.com/snakemake/snakemake-wrappers/issues/1997)) ([8d22b5e](https://www.github.com/snakemake/snakemake-wrappers/commit/8d22b5e98e9e8843a06bee9526191874411eb112))
* autobump bio/deeptools/plotprofile ([#2020](https://www.github.com/snakemake/snakemake-wrappers/issues/2020)) ([60853d4](https://www.github.com/snakemake/snakemake-wrappers/commit/60853d4b7cb3061aea8b547260eeecb26993271f))
* autobump bio/delly ([#2016](https://www.github.com/snakemake/snakemake-wrappers/issues/2016)) ([0ad5c9a](https://www.github.com/snakemake/snakemake-wrappers/commit/0ad5c9a882ef8f00e9ada4ffb12979aebaa7c434))
* autobump bio/diamond/blastp ([#2008](https://www.github.com/snakemake/snakemake-wrappers/issues/2008)) ([623cba2](https://www.github.com/snakemake/snakemake-wrappers/commit/623cba28f02fe9b04f4913a7ae3581da6ee4149b))
* autobump bio/diamond/blastx ([#2000](https://www.github.com/snakemake/snakemake-wrappers/issues/2000)) ([7e4f284](https://www.github.com/snakemake/snakemake-wrappers/commit/7e4f284dbfea2f27dd413829b315415b505fe2c1))
* autobump bio/diamond/makedb ([#2002](https://www.github.com/snakemake/snakemake-wrappers/issues/2002)) ([5e1ef8c](https://www.github.com/snakemake/snakemake-wrappers/commit/5e1ef8c671d1c352bc251f2e405705d04a97ca00))
* autobump bio/dragmap/build ([#2014](https://www.github.com/snakemake/snakemake-wrappers/issues/2014)) ([c398736](https://www.github.com/snakemake/snakemake-wrappers/commit/c39873623f68aa3b89a0d7d1412e411082cdc24f))
* autobump bio/encode_fastq_downloader ([#2021](https://www.github.com/snakemake/snakemake-wrappers/issues/2021)) ([355a367](https://www.github.com/snakemake/snakemake-wrappers/commit/355a367de4cfd7fda2e7025a1bbfb172e32c21ab))
* autobump bio/enhancedvolcano ([#2023](https://www.github.com/snakemake/snakemake-wrappers/issues/2023)) ([4066191](https://www.github.com/snakemake/snakemake-wrappers/commit/4066191dd79ab9e8841114958c4d02afec212625))
* autobump bio/epic/peaks ([#2022](https://www.github.com/snakemake/snakemake-wrappers/issues/2022)) ([fa4e105](https://www.github.com/snakemake/snakemake-wrappers/commit/fa4e1055541955618b1596cb6a42a9822e29cd55))
* autobump bio/fasttree ([#2024](https://www.github.com/snakemake/snakemake-wrappers/issues/2024)) ([7ee6b83](https://www.github.com/snakemake/snakemake-wrappers/commit/7ee6b835b7680265b29772599ad1710761bf2000))
* autobump bio/fgbio/collectduplexseqmetrics ([#2025](https://www.github.com/snakemake/snakemake-wrappers/issues/2025)) ([1914548](https://www.github.com/snakemake/snakemake-wrappers/commit/1914548b4ca11a0e133b8507a3020cc582d3f707))
* autobump bio/fgbio/setmateinformation ([#1910](https://www.github.com/snakemake/snakemake-wrappers/issues/1910)) ([094090a](https://www.github.com/snakemake/snakemake-wrappers/commit/094090ab56394580bb17d15157c24208cce0b697))
* autobump bio/galah ([#2044](https://www.github.com/snakemake/snakemake-wrappers/issues/2044)) ([3de109a](https://www.github.com/snakemake/snakemake-wrappers/commit/3de109a3f15de36145c251896ca20eb31567a159))
* autobump bio/gatk/applybqsrspark ([#2029](https://www.github.com/snakemake/snakemake-wrappers/issues/2029)) ([bd111a6](https://www.github.com/snakemake/snakemake-wrappers/commit/bd111a64982dc14825cd97671b20f794de72aff9))
* autobump bio/gatk/applyvqsr ([#2047](https://www.github.com/snakemake/snakemake-wrappers/issues/2047)) ([2c38135](https://www.github.com/snakemake/snakemake-wrappers/commit/2c38135c9322208bb611b94935f02039f72176ee))
* autobump bio/gatk/baserecalibrator ([#2050](https://www.github.com/snakemake/snakemake-wrappers/issues/2050)) ([42e14b2](https://www.github.com/snakemake/snakemake-wrappers/commit/42e14b2af55912d1cee3b5db95686ee2557b47e4))
* autobump bio/gatk/baserecalibratorspark ([#2049](https://www.github.com/snakemake/snakemake-wrappers/issues/2049)) ([6076992](https://www.github.com/snakemake/snakemake-wrappers/commit/6076992b457043b6c4a5a761bf3572d36d05ad5c))
* autobump bio/gatk/calculatecontamination ([#2027](https://www.github.com/snakemake/snakemake-wrappers/issues/2027)) ([44204c2](https://www.github.com/snakemake/snakemake-wrappers/commit/44204c29f0943eae9d1f657a0f5796b927669c64))
* autobump bio/gatk/cleansam ([#2042](https://www.github.com/snakemake/snakemake-wrappers/issues/2042)) ([2675d3b](https://www.github.com/snakemake/snakemake-wrappers/commit/2675d3bd5111c49bbc3906838ff464af4bc0ab72))
* autobump bio/gatk/collectalleliccounts ([#2066](https://www.github.com/snakemake/snakemake-wrappers/issues/2066)) ([a7a7702](https://www.github.com/snakemake/snakemake-wrappers/commit/a7a770251dcc133c50ea08efd4d5bfc12effdd6c))
* autobump bio/gatk/collectreadcounts ([#2037](https://www.github.com/snakemake/snakemake-wrappers/issues/2037)) ([638c569](https://www.github.com/snakemake/snakemake-wrappers/commit/638c569eafc64ce5f6d23229900c64c6fed27cc6))
* autobump bio/gatk/combinegvcfs ([#2030](https://www.github.com/snakemake/snakemake-wrappers/issues/2030)) ([cfe403c](https://www.github.com/snakemake/snakemake-wrappers/commit/cfe403cbe1ed1abbc7791696ecd1c31efcb97e0f))
* autobump bio/gatk/denoisereadcounts ([#2038](https://www.github.com/snakemake/snakemake-wrappers/issues/2038)) ([a881b2f](https://www.github.com/snakemake/snakemake-wrappers/commit/a881b2fe68513615b3104f1e7cfa1478fbff39c6))
* autobump bio/gatk/depthofcoverage ([#2036](https://www.github.com/snakemake/snakemake-wrappers/issues/2036)) ([f9d6ec2](https://www.github.com/snakemake/snakemake-wrappers/commit/f9d6ec2d0c49336a2c2e559209aa523806fa3e99))
* autobump bio/gatk/estimatelibrarycomplexity ([#2063](https://www.github.com/snakemake/snakemake-wrappers/issues/2063)) ([3f08736](https://www.github.com/snakemake/snakemake-wrappers/commit/3f08736e9fc97ed7d7d54b9fd23b0270f21c3c51))
* autobump bio/gatk/genomicsdbimport ([#2041](https://www.github.com/snakemake/snakemake-wrappers/issues/2041)) ([ba2990a](https://www.github.com/snakemake/snakemake-wrappers/commit/ba2990aab827751e8fcf6f64f4e12f26fab2c9d1))
* autobump bio/gatk/genotypegvcfs ([#2065](https://www.github.com/snakemake/snakemake-wrappers/issues/2065)) ([679c506](https://www.github.com/snakemake/snakemake-wrappers/commit/679c506333a7321fbefe337051025efba618b2de))
* autobump bio/gatk/getpileupsummaries ([#2040](https://www.github.com/snakemake/snakemake-wrappers/issues/2040)) ([5a5d202](https://www.github.com/snakemake/snakemake-wrappers/commit/5a5d202bfe983109e4bb749fe718fd796293ec41))
* autobump bio/gatk/intervallisttobed ([#2043](https://www.github.com/snakemake/snakemake-wrappers/issues/2043)) ([54a5fbd](https://www.github.com/snakemake/snakemake-wrappers/commit/54a5fbdeed438ec155127967220a699d03c88c7e))
* autobump bio/gatk/learnreadorientationmodel ([#2060](https://www.github.com/snakemake/snakemake-wrappers/issues/2060)) ([99fbe2c](https://www.github.com/snakemake/snakemake-wrappers/commit/99fbe2c988357aad3169aab6425078b4cc94a412))
* autobump bio/gatk/markduplicatesspark ([#2035](https://www.github.com/snakemake/snakemake-wrappers/issues/2035)) ([50c5f8b](https://www.github.com/snakemake/snakemake-wrappers/commit/50c5f8b22a1bb98548d545040261a61b778d4e26))
* autobump bio/gatk/modelsegments ([#2057](https://www.github.com/snakemake/snakemake-wrappers/issues/2057)) ([6118bdc](https://www.github.com/snakemake/snakemake-wrappers/commit/6118bdc647a546e82f627daa6078374b279703a0))
* autobump bio/gatk/mutect ([#2051](https://www.github.com/snakemake/snakemake-wrappers/issues/2051)) ([3811e48](https://www.github.com/snakemake/snakemake-wrappers/commit/3811e482ab9b42e08b6b79998e5cae6e60339a74))
* autobump bio/gatk/selectvariants ([#2033](https://www.github.com/snakemake/snakemake-wrappers/issues/2033)) ([c67ec86](https://www.github.com/snakemake/snakemake-wrappers/commit/c67ec86c772576922801243f3b76f0886fbc0c8c))
* autobump bio/gatk/splitintervals ([#2045](https://www.github.com/snakemake/snakemake-wrappers/issues/2045)) ([917168c](https://www.github.com/snakemake/snakemake-wrappers/commit/917168c0addfe3ac187d44592447bfd8a6769cd1))
* autobump bio/gatk/splitncigarreads ([#2059](https://www.github.com/snakemake/snakemake-wrappers/issues/2059)) ([b286cc4](https://www.github.com/snakemake/snakemake-wrappers/commit/b286cc4c0183b2b88eacad1a83c4d94feb100d92))
* autobump bio/gatk/variantfiltration ([#2039](https://www.github.com/snakemake/snakemake-wrappers/issues/2039)) ([68512dc](https://www.github.com/snakemake/snakemake-wrappers/commit/68512dcbe7f1dbb571c05493f644641f69a585bf))
* autobump bio/gatk/variantrecalibrator ([#2061](https://www.github.com/snakemake/snakemake-wrappers/issues/2061)) ([8226d7e](https://www.github.com/snakemake/snakemake-wrappers/commit/8226d7e7be2a5f909a49311ecfefb55afda5087a))
* autobump bio/gatk/variantstotable ([#2028](https://www.github.com/snakemake/snakemake-wrappers/issues/2028)) ([36b616c](https://www.github.com/snakemake/snakemake-wrappers/commit/36b616c3aa252d13f4108b47731e1e38d408887f))
* autobump bio/gatk3/baserecalibrator ([#2054](https://www.github.com/snakemake/snakemake-wrappers/issues/2054)) ([693908f](https://www.github.com/snakemake/snakemake-wrappers/commit/693908f52fe2217fdcdcfa9e4464823833824b25))
* autobump bio/gatk3/indelrealigner ([#2046](https://www.github.com/snakemake/snakemake-wrappers/issues/2046)) ([982e7a2](https://www.github.com/snakemake/snakemake-wrappers/commit/982e7a23d871305b7fd443197865b83f00bd850f))
* autobump bio/gatk3/printreads ([#2052](https://www.github.com/snakemake/snakemake-wrappers/issues/2052)) ([e6e45a3](https://www.github.com/snakemake/snakemake-wrappers/commit/e6e45a3c85589bf8586618c7ba68805ab5e053c4))
* autobump bio/gatk3/realignertargetcreator ([#2026](https://www.github.com/snakemake/snakemake-wrappers/issues/2026)) ([f584dbc](https://www.github.com/snakemake/snakemake-wrappers/commit/f584dbcc14e0b4dae67f8e8baf1514d906ca707b))
* autobump bio/gdc-api/bam-slicing ([#2055](https://www.github.com/snakemake/snakemake-wrappers/issues/2055)) ([6a79095](https://www.github.com/snakemake/snakemake-wrappers/commit/6a790958e7a3670bba03e9b1a2cf2bc3f82ee1a5))
* autobump bio/genefuse ([#2032](https://www.github.com/snakemake/snakemake-wrappers/issues/2032)) ([9d696a9](https://www.github.com/snakemake/snakemake-wrappers/commit/9d696a99c7aca0d55cfff707e20dd827bc7afb9f))
* autobump bio/genomescope ([#2053](https://www.github.com/snakemake/snakemake-wrappers/issues/2053)) ([47912b0](https://www.github.com/snakemake/snakemake-wrappers/commit/47912b0f75765aa5e66f05920da8f2c410a504c5))
* autobump bio/gfatools ([#2048](https://www.github.com/snakemake/snakemake-wrappers/issues/2048)) ([bfb2a44](https://www.github.com/snakemake/snakemake-wrappers/commit/bfb2a44f7fcac9715062209e86b83febbc4c23de))
* autobump bio/gffread ([#2056](https://www.github.com/snakemake/snakemake-wrappers/issues/2056)) ([64450da](https://www.github.com/snakemake/snakemake-wrappers/commit/64450da3d099aa5901a8992481be48a9b15e0a69))
* autobump bio/gridss/assemble ([#2034](https://www.github.com/snakemake/snakemake-wrappers/issues/2034)) ([52e0b74](https://www.github.com/snakemake/snakemake-wrappers/commit/52e0b7471fa2cddc4a175d60517b925f74de0cc7))
* autobump bio/gridss/call ([#2062](https://www.github.com/snakemake/snakemake-wrappers/issues/2062)) ([46f2e00](https://www.github.com/snakemake/snakemake-wrappers/commit/46f2e00f340f819e0c803c4479c19d0a8e83e53d))
* autobump bio/gridss/setupreference ([#2064](https://www.github.com/snakemake/snakemake-wrappers/issues/2064)) ([15aa2c9](https://www.github.com/snakemake/snakemake-wrappers/commit/15aa2c907b46614625877ce1ca135dcae8cd399f))
* autobump bio/gseapy/gsea ([#2058](https://www.github.com/snakemake/snakemake-wrappers/issues/2058)) ([9eb8b6b](https://www.github.com/snakemake/snakemake-wrappers/commit/9eb8b6bdfc466c3e3c505170ed218b8dd9a4a14d))
* autobump bio/hap.py/hap.py ([#2076](https://www.github.com/snakemake/snakemake-wrappers/issues/2076)) ([3767f02](https://www.github.com/snakemake/snakemake-wrappers/commit/3767f026a65ede5a65c690c6ca375d917d28c081))
* autobump bio/hap.py/pre.py ([#2070](https://www.github.com/snakemake/snakemake-wrappers/issues/2070)) ([d896560](https://www.github.com/snakemake/snakemake-wrappers/commit/d896560129920c4a03c01a189ef42085a04c7db8))
* autobump bio/hifiasm ([#2077](https://www.github.com/snakemake/snakemake-wrappers/issues/2077)) ([c25e04c](https://www.github.com/snakemake/snakemake-wrappers/commit/c25e04cb7dcc332cf021298110868df124053c71))
* autobump bio/hisat2/align ([#2069](https://www.github.com/snakemake/snakemake-wrappers/issues/2069)) ([4f4351b](https://www.github.com/snakemake/snakemake-wrappers/commit/4f4351b6a231f3f75f8146839797f41e003fefd2))
* autobump bio/hisat2/index ([#2080](https://www.github.com/snakemake/snakemake-wrappers/issues/2080)) ([80d0564](https://www.github.com/snakemake/snakemake-wrappers/commit/80d05649f6bc119d476afe648c1bde440f77ab73))
* autobump bio/hmmer/hmmbuild ([#2078](https://www.github.com/snakemake/snakemake-wrappers/issues/2078)) ([f1ced02](https://www.github.com/snakemake/snakemake-wrappers/commit/f1ced02ccea71695099e496bf0af29d1f2078dcc))
* autobump bio/hmmer/hmmpress ([#2068](https://www.github.com/snakemake/snakemake-wrappers/issues/2068)) ([074976d](https://www.github.com/snakemake/snakemake-wrappers/commit/074976d0b7c7f6b8a8eb8ebba4a3c3d6172ef2f6))
* autobump bio/hmmer/hmmscan ([#2073](https://www.github.com/snakemake/snakemake-wrappers/issues/2073)) ([b14cb37](https://www.github.com/snakemake/snakemake-wrappers/commit/b14cb37fb59aa536b84a9185a298c5b627054805))
* autobump bio/hmmer/hmmsearch ([#2079](https://www.github.com/snakemake/snakemake-wrappers/issues/2079)) ([9ffc5cd](https://www.github.com/snakemake/snakemake-wrappers/commit/9ffc5cd582a95b7a2dff116658433f8e7fbb0c8d))
* autobump bio/homer/annotatePeaks ([#2074](https://www.github.com/snakemake/snakemake-wrappers/issues/2074)) ([b620702](https://www.github.com/snakemake/snakemake-wrappers/commit/b6207028ca4c6d71ded63c3f738f26da31018ed6))
* autobump bio/homer/findPeaks ([#2067](https://www.github.com/snakemake/snakemake-wrappers/issues/2067)) ([821e68b](https://www.github.com/snakemake/snakemake-wrappers/commit/821e68bb436b1436a5cefe0405a63ba5273b5f7c))
* autobump bio/homer/getDifferentialPeaks ([#2075](https://www.github.com/snakemake/snakemake-wrappers/issues/2075)) ([09a84a4](https://www.github.com/snakemake/snakemake-wrappers/commit/09a84a47f1b67a758ab4b7ada9742b2cfa5c69ee))
* autobump bio/homer/makeTagDirectory ([#2072](https://www.github.com/snakemake/snakemake-wrappers/issues/2072)) ([bbc0454](https://www.github.com/snakemake/snakemake-wrappers/commit/bbc04545cc77830feb2a0290d788378a32aab588))
* autobump bio/homer/mergePeaks ([#2071](https://www.github.com/snakemake/snakemake-wrappers/issues/2071)) ([c6eaf9b](https://www.github.com/snakemake/snakemake-wrappers/commit/c6eaf9bbdc6fd14d448893662c6fcc4d543cc00d))
* autobump bio/igv-reports ([#2084](https://www.github.com/snakemake/snakemake-wrappers/issues/2084)) ([6940483](https://www.github.com/snakemake/snakemake-wrappers/commit/694048334dd01ecba435438ed3a784a8afe4d032))
* autobump bio/immunedeconv ([#2083](https://www.github.com/snakemake/snakemake-wrappers/issues/2083)) ([025824d](https://www.github.com/snakemake/snakemake-wrappers/commit/025824df7da7e6aa5d621e01d0c187e73466eda7))
* autobump bio/infernal/cmpress ([#2081](https://www.github.com/snakemake/snakemake-wrappers/issues/2081)) ([da8bf6d](https://www.github.com/snakemake/snakemake-wrappers/commit/da8bf6d084ea7037413c28c6b751c385e70b0d8c))
* autobump bio/infernal/cmscan ([#2082](https://www.github.com/snakemake/snakemake-wrappers/issues/2082)) ([fbcb5c2](https://www.github.com/snakemake/snakemake-wrappers/commit/fbcb5c28670a6d1aaff0214e8e30a37baccdb432))
* autobump bio/jannovar ([#2089](https://www.github.com/snakemake/snakemake-wrappers/issues/2089)) ([20c6b98](https://www.github.com/snakemake/snakemake-wrappers/commit/20c6b98b182e9a5b2eb9e0b5e1fd7cf6843f34a0))
* autobump bio/jellyfish/count ([#2087](https://www.github.com/snakemake/snakemake-wrappers/issues/2087)) ([6f6c3c4](https://www.github.com/snakemake/snakemake-wrappers/commit/6f6c3c4b6294b101218a41c83b8a36d6105a7643))
* autobump bio/jellyfish/dump ([#2088](https://www.github.com/snakemake/snakemake-wrappers/issues/2088)) ([86f7d9a](https://www.github.com/snakemake/snakemake-wrappers/commit/86f7d9a4bd7c9fb7dd11c1c9ae38359e2e3f8076))
* autobump bio/jellyfish/histo ([#2085](https://www.github.com/snakemake/snakemake-wrappers/issues/2085)) ([8a7821f](https://www.github.com/snakemake/snakemake-wrappers/commit/8a7821f6c6466ca928eb26a76869ac46c058edc0))
* autobump bio/jellyfish/merge ([#2086](https://www.github.com/snakemake/snakemake-wrappers/issues/2086)) ([76708bc](https://www.github.com/snakemake/snakemake-wrappers/commit/76708bcb5117178f29e497641f787574ed070d94))
* autobump bio/kallisto/index ([#2090](https://www.github.com/snakemake/snakemake-wrappers/issues/2090)) ([696ada7](https://www.github.com/snakemake/snakemake-wrappers/commit/696ada70cfb7ae10f86c6bdc0be5692b0b633abc))
* autobump bio/kallisto/quant ([#2091](https://www.github.com/snakemake/snakemake-wrappers/issues/2091)) ([f2baa4a](https://www.github.com/snakemake/snakemake-wrappers/commit/f2baa4aa4a80d3d323d56b955d5fb07bf8943ef1))
* autobump bio/last/lastal ([#2095](https://www.github.com/snakemake/snakemake-wrappers/issues/2095)) ([30453d5](https://www.github.com/snakemake/snakemake-wrappers/commit/30453d55d5afd070637df0a67bd82ffe0fccb95b))
* autobump bio/liftoff ([#2094](https://www.github.com/snakemake/snakemake-wrappers/issues/2094)) ([d08add9](https://www.github.com/snakemake/snakemake-wrappers/commit/d08add9cf7cad79ea1b5995798ebefc0edb98d04))
* autobump bio/lofreq/call ([#2092](https://www.github.com/snakemake/snakemake-wrappers/issues/2092)) ([d4a55df](https://www.github.com/snakemake/snakemake-wrappers/commit/d4a55dfca7a318f480e09f7db3432b3b4a7e8809))
* autobump bio/lofreq/indelqual ([#2096](https://www.github.com/snakemake/snakemake-wrappers/issues/2096)) ([e0126f6](https://www.github.com/snakemake/snakemake-wrappers/commit/e0126f6b9b99b27cdaae41302e45eccc4e0d3080))
* autobump bio/macs2/callpeak ([#2098](https://www.github.com/snakemake/snakemake-wrappers/issues/2098)) ([c6d5037](https://www.github.com/snakemake/snakemake-wrappers/commit/c6d50374c4f8f8c1a6a502dbd38b751fa977f9d1))
* autobump bio/mapdamage2 ([#2113](https://www.github.com/snakemake/snakemake-wrappers/issues/2113)) ([33241fa](https://www.github.com/snakemake/snakemake-wrappers/commit/33241faabe4001c4940009de690b37c27be321d5))
* autobump bio/mashmap ([#2103](https://www.github.com/snakemake/snakemake-wrappers/issues/2103)) ([5a538aa](https://www.github.com/snakemake/snakemake-wrappers/commit/5a538aae10a7b42c609e264a37fa4f4cf5350d6b))
* autobump bio/merqury ([#2102](https://www.github.com/snakemake/snakemake-wrappers/issues/2102)) ([c005cd9](https://www.github.com/snakemake/snakemake-wrappers/commit/c005cd9b3c73c0eddff18a10a83bf0a7c8c0c20a))
* autobump bio/meryl/count ([#2099](https://www.github.com/snakemake/snakemake-wrappers/issues/2099)) ([016762d](https://www.github.com/snakemake/snakemake-wrappers/commit/016762d45caf23c9b4083bc9aa2eb59dcc5a87a4))
* autobump bio/meryl/sets ([#2107](https://www.github.com/snakemake/snakemake-wrappers/issues/2107)) ([273e654](https://www.github.com/snakemake/snakemake-wrappers/commit/273e654b32ab405e6c01924ed20e504e007f811e))
* autobump bio/meryl/stats ([#2097](https://www.github.com/snakemake/snakemake-wrappers/issues/2097)) ([5c487cd](https://www.github.com/snakemake/snakemake-wrappers/commit/5c487cd59efa22fc6ab0f7979dbd6f3037fb4443))
* autobump bio/methyldackel/extract ([#2115](https://www.github.com/snakemake/snakemake-wrappers/issues/2115)) ([df27e3c](https://www.github.com/snakemake/snakemake-wrappers/commit/df27e3c599740dc4fb18ab05b56efc305943fb9b))
* autobump bio/microphaser/build_reference ([#2100](https://www.github.com/snakemake/snakemake-wrappers/issues/2100)) ([7fa54a8](https://www.github.com/snakemake/snakemake-wrappers/commit/7fa54a835c063d38f1ca9bca4c6d16fbc9376eb6))
* autobump bio/microphaser/filter ([#2104](https://www.github.com/snakemake/snakemake-wrappers/issues/2104)) ([bc2cc17](https://www.github.com/snakemake/snakemake-wrappers/commit/bc2cc17bd480286efedea3bea6de84ed960ecb47))
* autobump bio/microphaser/normal ([#2110](https://www.github.com/snakemake/snakemake-wrappers/issues/2110)) ([b0bd51c](https://www.github.com/snakemake/snakemake-wrappers/commit/b0bd51cdde9ba8ad5943690c0b24ef2e4b16542d))
* autobump bio/microphaser/somatic ([#2108](https://www.github.com/snakemake/snakemake-wrappers/issues/2108)) ([93d075b](https://www.github.com/snakemake/snakemake-wrappers/commit/93d075b4e6650e181452a8aacfd6bd90a8ad90f2))
* autobump bio/minimap2/aligner ([#2112](https://www.github.com/snakemake/snakemake-wrappers/issues/2112)) ([3195652](https://www.github.com/snakemake/snakemake-wrappers/commit/31956524d21aaf34de05da6146aeef703d38eb51))
* autobump bio/minimap2/index ([#2106](https://www.github.com/snakemake/snakemake-wrappers/issues/2106)) ([6241e6c](https://www.github.com/snakemake/snakemake-wrappers/commit/6241e6cc82944f2724aef222fd24454a534204c2))
* autobump bio/mlst ([#2109](https://www.github.com/snakemake/snakemake-wrappers/issues/2109)) ([1d3b56a](https://www.github.com/snakemake/snakemake-wrappers/commit/1d3b56a561f782c96c87096f2f650904db846480))
* autobump bio/mosdepth ([#2101](https://www.github.com/snakemake/snakemake-wrappers/issues/2101)) ([c2463c6](https://www.github.com/snakemake/snakemake-wrappers/commit/c2463c651314eee5dc9cc80f546a31ce43ee0109))
* autobump bio/msisensor/msi ([#2111](https://www.github.com/snakemake/snakemake-wrappers/issues/2111)) ([3bcab04](https://www.github.com/snakemake/snakemake-wrappers/commit/3bcab0481645ba7411160dc595b05135e2114e22))
* autobump bio/msisensor/scan ([#2105](https://www.github.com/snakemake/snakemake-wrappers/issues/2105)) ([98e5658](https://www.github.com/snakemake/snakemake-wrappers/commit/98e56587db10513c4f152ef41c7c27cc49772431))
* autobump bio/muscle ([#2116](https://www.github.com/snakemake/snakemake-wrappers/issues/2116)) ([9fd8362](https://www.github.com/snakemake/snakemake-wrappers/commit/9fd8362c8feecda237c5e0de468edfbe343216a8))
* autobump bio/nanosim-h ([#2119](https://www.github.com/snakemake/snakemake-wrappers/issues/2119)) ([379ec37](https://www.github.com/snakemake/snakemake-wrappers/commit/379ec37567f7afd548bc71585e88ff959e146269))
* autobump bio/ngs-disambiguate ([#2121](https://www.github.com/snakemake/snakemake-wrappers/issues/2121)) ([3ca7956](https://www.github.com/snakemake/snakemake-wrappers/commit/3ca7956882cefe878b39943985abfc74b66dafc6))
* autobump bio/nonpareil/infer ([#2118](https://www.github.com/snakemake/snakemake-wrappers/issues/2118)) ([0d16598](https://www.github.com/snakemake/snakemake-wrappers/commit/0d165989e8eab2bb68c42daaaedba0d0c4d915f2))
* autobump bio/nonpareil/plot ([#2117](https://www.github.com/snakemake/snakemake-wrappers/issues/2117)) ([0055c5a](https://www.github.com/snakemake/snakemake-wrappers/commit/0055c5a35bbabdc58830a5d9f170954620a712ec))
* autobump bio/optitype ([#2122](https://www.github.com/snakemake/snakemake-wrappers/issues/2122)) ([151b0c7](https://www.github.com/snakemake/snakemake-wrappers/commit/151b0c7f18a50bd82cb90a9296c15b37dce5a7ed))
* autobump bio/paladin/index ([#2230](https://www.github.com/snakemake/snakemake-wrappers/issues/2230)) ([0434462](https://www.github.com/snakemake/snakemake-wrappers/commit/043446238a6005a7ce7642a02f7ffe1b1b0fbcd1))
* autobump bio/pandora/index ([#2123](https://www.github.com/snakemake/snakemake-wrappers/issues/2123)) ([a19a221](https://www.github.com/snakemake/snakemake-wrappers/commit/a19a221675698b72c3dd435cd4d9acb9a7b03b34))
* autobump bio/picard/collectinsertsizemetrics ([#2231](https://www.github.com/snakemake/snakemake-wrappers/issues/2231)) ([f90e3db](https://www.github.com/snakemake/snakemake-wrappers/commit/f90e3db1c358c5e46287c11f499bf8d7307bb6c4))
* autobump bio/picard/createsequencedictionary ([#1911](https://www.github.com/snakemake/snakemake-wrappers/issues/1911)) ([2122fc4](https://www.github.com/snakemake/snakemake-wrappers/commit/2122fc45a9c4669349e40ec6f0c1af5c2241d11b))
* autobump bio/picard/mergesamfiles ([#2124](https://www.github.com/snakemake/snakemake-wrappers/issues/2124)) ([84e1458](https://www.github.com/snakemake/snakemake-wrappers/commit/84e14588fc458aea85db52b9677e571f90411099))
* autobump bio/pyfastaq/replace_bases ([#2229](https://www.github.com/snakemake/snakemake-wrappers/issues/2229)) ([b6c1d0b](https://www.github.com/snakemake/snakemake-wrappers/commit/b6c1d0bf43f89624509ada11d4a1e00dc8a32878))
* autobump bio/qualimap/bamqc ([#2125](https://www.github.com/snakemake/snakemake-wrappers/issues/2125)) ([a798543](https://www.github.com/snakemake/snakemake-wrappers/commit/a79854303a01d44193d6da7bb431438790f10361))
* autobump bio/qualimap/rnaseq ([#2127](https://www.github.com/snakemake/snakemake-wrappers/issues/2127)) ([adc1965](https://www.github.com/snakemake/snakemake-wrappers/commit/adc19659e8d7308e5731d428be006a9d1e92b446))
* autobump bio/quast ([#2126](https://www.github.com/snakemake/snakemake-wrappers/issues/2126)) ([383dbe6](https://www.github.com/snakemake/snakemake-wrappers/commit/383dbe6fe0f5b3259a093ebb5aa3ea55f0e1115c))
* autobump bio/ragtag/correction ([#2128](https://www.github.com/snakemake/snakemake-wrappers/issues/2128)) ([2f3e9d4](https://www.github.com/snakemake/snakemake-wrappers/commit/2f3e9d43750db9d7653756a6d35845b9f8c34788))
* autobump bio/ragtag/merge ([#2131](https://www.github.com/snakemake/snakemake-wrappers/issues/2131)) ([b7fe507](https://www.github.com/snakemake/snakemake-wrappers/commit/b7fe507044672e21ab36dfce758e7b349e8a46af))
* autobump bio/ragtag/patch ([#2141](https://www.github.com/snakemake/snakemake-wrappers/issues/2141)) ([f8d917e](https://www.github.com/snakemake/snakemake-wrappers/commit/f8d917ed3d2cd11241ec3bf718c6928797ee5c92))
* autobump bio/ragtag/scaffold ([#2129](https://www.github.com/snakemake/snakemake-wrappers/issues/2129)) ([d640d76](https://www.github.com/snakemake/snakemake-wrappers/commit/d640d76bb649020060123c36ea7e628a184a83ce))
* autobump bio/rasusa ([#2134](https://www.github.com/snakemake/snakemake-wrappers/issues/2134)) ([3f55639](https://www.github.com/snakemake/snakemake-wrappers/commit/3f55639b09050075eb18c615084e0de1c8397ce3))
* autobump bio/razers3 ([#2135](https://www.github.com/snakemake/snakemake-wrappers/issues/2135)) ([19a75ec](https://www.github.com/snakemake/snakemake-wrappers/commit/19a75ecfc275a5a58bf53486dad34ccff212a390))
* autobump bio/rbt/collapse_reads_to_fragments-bam ([#2142](https://www.github.com/snakemake/snakemake-wrappers/issues/2142)) ([bb6bf0e](https://www.github.com/snakemake/snakemake-wrappers/commit/bb6bf0e7bfcb06c13a5d641cde83f77ecdd021e0))
* autobump bio/rbt/csvreport ([#2143](https://www.github.com/snakemake/snakemake-wrappers/issues/2143)) ([32cf0df](https://www.github.com/snakemake/snakemake-wrappers/commit/32cf0df6a3835c646d941f40e1562cfea2293acb))
* autobump bio/rebaler ([#2137](https://www.github.com/snakemake/snakemake-wrappers/issues/2137)) ([4267804](https://www.github.com/snakemake/snakemake-wrappers/commit/42678048440e7a6cc3a8a085814653a3edc5b9a8))
* autobump bio/reference/ensembl-annotation ([#2132](https://www.github.com/snakemake/snakemake-wrappers/issues/2132)) ([1528499](https://www.github.com/snakemake/snakemake-wrappers/commit/1528499c0134d16c7ca310cf183abfa321a6291e))
* autobump bio/reference/ensembl-sequence ([#2130](https://www.github.com/snakemake/snakemake-wrappers/issues/2130)) ([45077a5](https://www.github.com/snakemake/snakemake-wrappers/commit/45077a5248f9a4b5f38ea34933bdddf76483b20f))
* autobump bio/reference/ensembl-variation ([#2138](https://www.github.com/snakemake/snakemake-wrappers/issues/2138)) ([eedb3b6](https://www.github.com/snakemake/snakemake-wrappers/commit/eedb3b6beed094a16b6597cb0f361eb9f3758e0b))
* autobump bio/refgenie ([#2133](https://www.github.com/snakemake/snakemake-wrappers/issues/2133)) ([619f659](https://www.github.com/snakemake/snakemake-wrappers/commit/619f659fe1d8c10bf800a596774e7b90fcaa5543))
* autobump bio/rsem/calculate-expression ([#2136](https://www.github.com/snakemake/snakemake-wrappers/issues/2136)) ([f839456](https://www.github.com/snakemake/snakemake-wrappers/commit/f839456026d6de5c9e8dc1419ea2de20a42e222c))
* autobump bio/rsem/generate-data-matrix ([#2139](https://www.github.com/snakemake/snakemake-wrappers/issues/2139)) ([52950e0](https://www.github.com/snakemake/snakemake-wrappers/commit/52950e026fc8d9afd752ed43861a9b0a67141804))
* autobump bio/rsem/prepare-reference ([#2140](https://www.github.com/snakemake/snakemake-wrappers/issues/2140)) ([81171d1](https://www.github.com/snakemake/snakemake-wrappers/commit/81171d114b5fdaa71181ad5e3fd05d5e4c65868a))
* autobump bio/salmon/decoys ([#2144](https://www.github.com/snakemake/snakemake-wrappers/issues/2144)) ([30a4381](https://www.github.com/snakemake/snakemake-wrappers/commit/30a438177ed682637d97ede0fefb69ed5190fa16))
* autobump bio/salmon/index ([#2190](https://www.github.com/snakemake/snakemake-wrappers/issues/2190)) ([5aa45bd](https://www.github.com/snakemake/snakemake-wrappers/commit/5aa45bd2fc7c6cf06dc5ed14de1b7cffb7f34412))
* autobump bio/salmon/quant ([#2179](https://www.github.com/snakemake/snakemake-wrappers/issues/2179)) ([c5a264e](https://www.github.com/snakemake/snakemake-wrappers/commit/c5a264e801a117f7e6a478e57966a719b7c2a031))
* autobump bio/salsa2 ([#2161](https://www.github.com/snakemake/snakemake-wrappers/issues/2161)) ([22095dd](https://www.github.com/snakemake/snakemake-wrappers/commit/22095dd7efcb8523bf83c9b19bd93e46781b7ff7))
* autobump bio/sambamba/flagstat ([#2165](https://www.github.com/snakemake/snakemake-wrappers/issues/2165)) ([ecbd58c](https://www.github.com/snakemake/snakemake-wrappers/commit/ecbd58ca5a9cfc52bc31b785f64c51ea1980c1f5))
* autobump bio/sambamba/index ([#2183](https://www.github.com/snakemake/snakemake-wrappers/issues/2183)) ([6a30594](https://www.github.com/snakemake/snakemake-wrappers/commit/6a305944085f5064c13de43225e4985c1dcf54af))
* autobump bio/sambamba/markdup ([#2160](https://www.github.com/snakemake/snakemake-wrappers/issues/2160)) ([e2de05e](https://www.github.com/snakemake/snakemake-wrappers/commit/e2de05eaed08dcbbeecf5ddaa4dee301a2cb9eb0))
* autobump bio/sambamba/merge ([#2175](https://www.github.com/snakemake/snakemake-wrappers/issues/2175)) ([79dfdde](https://www.github.com/snakemake/snakemake-wrappers/commit/79dfddeed0f0c9c1aca779d414cbdda52b514f72))
* autobump bio/sambamba/slice ([#2156](https://www.github.com/snakemake/snakemake-wrappers/issues/2156)) ([7435e91](https://www.github.com/snakemake/snakemake-wrappers/commit/7435e91035c9d2cc95fc8880a351c3a361aba9dc))
* autobump bio/sambamba/sort ([#2192](https://www.github.com/snakemake/snakemake-wrappers/issues/2192)) ([93a8c09](https://www.github.com/snakemake/snakemake-wrappers/commit/93a8c09ebcd80f9f0c35cdcf5f0727afe627818f))
* autobump bio/sambamba/view ([#2180](https://www.github.com/snakemake/snakemake-wrappers/issues/2180)) ([47f09a8](https://www.github.com/snakemake/snakemake-wrappers/commit/47f09a843ba2b1f7c1df5f2c63c4976b11e38634))
* autobump bio/samtools/calmd ([#2174](https://www.github.com/snakemake/snakemake-wrappers/issues/2174)) ([b7c3c32](https://www.github.com/snakemake/snakemake-wrappers/commit/b7c3c323f9902e62f1be11defe2b06ce7e33ff3e))
* autobump bio/samtools/depth ([#2177](https://www.github.com/snakemake/snakemake-wrappers/issues/2177)) ([aa658d9](https://www.github.com/snakemake/snakemake-wrappers/commit/aa658d90e94ab67925be692b1614f7502813c30e))
* autobump bio/samtools/faidx ([#2147](https://www.github.com/snakemake/snakemake-wrappers/issues/2147)) ([d08dfcc](https://www.github.com/snakemake/snakemake-wrappers/commit/d08dfccdb16c50dbcfa5a4694782eb78316e138d))
* autobump bio/samtools/fastx ([#2158](https://www.github.com/snakemake/snakemake-wrappers/issues/2158)) ([90b64c9](https://www.github.com/snakemake/snakemake-wrappers/commit/90b64c911bcc3244812084bddd2205ca6cbf08e8))
* autobump bio/samtools/fixmate ([#2191](https://www.github.com/snakemake/snakemake-wrappers/issues/2191)) ([ac38e76](https://www.github.com/snakemake/snakemake-wrappers/commit/ac38e7684a58daebf02dd6d0e37b27d047db5fab))
* autobump bio/samtools/flagstat ([#2166](https://www.github.com/snakemake/snakemake-wrappers/issues/2166)) ([8b46d61](https://www.github.com/snakemake/snakemake-wrappers/commit/8b46d617f92b4099a0938c2352207d7870ccabde))
* autobump bio/samtools/idxstats ([#2171](https://www.github.com/snakemake/snakemake-wrappers/issues/2171)) ([443641c](https://www.github.com/snakemake/snakemake-wrappers/commit/443641cdb210fab46396052d13f1db0b66310e97))
* autobump bio/samtools/index ([#2187](https://www.github.com/snakemake/snakemake-wrappers/issues/2187)) ([6b61a5d](https://www.github.com/snakemake/snakemake-wrappers/commit/6b61a5d0d739c9a214ea17e9e7552bec4a44df51))
* autobump bio/samtools/merge ([#2151](https://www.github.com/snakemake/snakemake-wrappers/issues/2151)) ([551c6ce](https://www.github.com/snakemake/snakemake-wrappers/commit/551c6cedd5e58d4c91151be336343d3ca9e89baa))
* autobump bio/samtools/mpileup ([#2148](https://www.github.com/snakemake/snakemake-wrappers/issues/2148)) ([dfc18fa](https://www.github.com/snakemake/snakemake-wrappers/commit/dfc18fae98367ac0d41f0f0dd26228c27bb3078b))
* autobump bio/samtools/sort ([#2188](https://www.github.com/snakemake/snakemake-wrappers/issues/2188)) ([8cf6144](https://www.github.com/snakemake/snakemake-wrappers/commit/8cf61442bf298e75f93a7f8ad94ad713f301a0bb))
* autobump bio/samtools/stats ([#2146](https://www.github.com/snakemake/snakemake-wrappers/issues/2146)) ([79b20bb](https://www.github.com/snakemake/snakemake-wrappers/commit/79b20bb0abf24071725881af136e4f8312199f1b))
* autobump bio/samtools/view ([#2163](https://www.github.com/snakemake/snakemake-wrappers/issues/2163)) ([0b9f002](https://www.github.com/snakemake/snakemake-wrappers/commit/0b9f002cf38a221d8f7c17e5d36c270908d380ce))
* autobump bio/seqkit ([#2167](https://www.github.com/snakemake/snakemake-wrappers/issues/2167)) ([0546963](https://www.github.com/snakemake/snakemake-wrappers/commit/0546963114b5462e9b15ad2e05c95b981305d3fb))
* autobump bio/seqtk ([#2189](https://www.github.com/snakemake/snakemake-wrappers/issues/2189)) ([b0bd294](https://www.github.com/snakemake/snakemake-wrappers/commit/b0bd2945f773f22dbced360a1319936580c6e420))
* autobump bio/shovill ([#2145](https://www.github.com/snakemake/snakemake-wrappers/issues/2145)) ([e9d9f91](https://www.github.com/snakemake/snakemake-wrappers/commit/e9d9f91f889c19db99dae5ed947fcfdc8b0fefe3))
* autobump bio/sickle/pe ([#2150](https://www.github.com/snakemake/snakemake-wrappers/issues/2150)) ([4f734a8](https://www.github.com/snakemake/snakemake-wrappers/commit/4f734a83bc7190d70a04623f1dcb7ce91f0cc0c6))
* autobump bio/sickle/se ([#2178](https://www.github.com/snakemake/snakemake-wrappers/issues/2178)) ([fea107b](https://www.github.com/snakemake/snakemake-wrappers/commit/fea107b539b98df32465d5ca008c8e2349650f58))
* autobump bio/snp-mutator ([#2181](https://www.github.com/snakemake/snakemake-wrappers/issues/2181)) ([29a54d7](https://www.github.com/snakemake/snakemake-wrappers/commit/29a54d78dac129c6d6dc034c6792164d4f8312ea))
* autobump bio/snpeff/annotate ([#2162](https://www.github.com/snakemake/snakemake-wrappers/issues/2162)) ([b708f10](https://www.github.com/snakemake/snakemake-wrappers/commit/b708f10b3001f7fd8f79749c621d6d81e315f1c0))
* autobump bio/snpeff/download ([#2170](https://www.github.com/snakemake/snakemake-wrappers/issues/2170)) ([b7a2288](https://www.github.com/snakemake/snakemake-wrappers/commit/b7a2288c66196d9bf601c2d8530ea2f3cca6ec0b))
* autobump bio/snpsift/annotate ([#2149](https://www.github.com/snakemake/snakemake-wrappers/issues/2149)) ([3c9a5bd](https://www.github.com/snakemake/snakemake-wrappers/commit/3c9a5bd822a698c260dd55b600a8d586aa9ecbd4))
* autobump bio/snpsift/dbnsfp ([#2159](https://www.github.com/snakemake/snakemake-wrappers/issues/2159)) ([cc137a3](https://www.github.com/snakemake/snakemake-wrappers/commit/cc137a3acded2a1fef7e286a992f615327aeadb7))
* autobump bio/snpsift/genesets ([#2182](https://www.github.com/snakemake/snakemake-wrappers/issues/2182)) ([d802915](https://www.github.com/snakemake/snakemake-wrappers/commit/d802915ae613f10aec8e7915c950d548195fd536))
* autobump bio/snpsift/gwascat ([#2153](https://www.github.com/snakemake/snakemake-wrappers/issues/2153)) ([69b97be](https://www.github.com/snakemake/snakemake-wrappers/commit/69b97be21c10fae51cae1c1f4afdd00441284667))
* autobump bio/snpsift/varType ([#2173](https://www.github.com/snakemake/snakemake-wrappers/issues/2173)) ([98635fd](https://www.github.com/snakemake/snakemake-wrappers/commit/98635fd209a3c6a26bbbf36310073fb0ec7f4046))
* autobump bio/sourmash/compute ([#2157](https://www.github.com/snakemake/snakemake-wrappers/issues/2157)) ([b4cf7d6](https://www.github.com/snakemake/snakemake-wrappers/commit/b4cf7d6b3cc097531bf483e57042bada8e064cce))
* autobump bio/spades/metaspades ([#2186](https://www.github.com/snakemake/snakemake-wrappers/issues/2186)) ([2ea03ec](https://www.github.com/snakemake/snakemake-wrappers/commit/2ea03ec5fbddaffb3c309708766c935fc7841167))
* autobump bio/sra-tools/fasterq-dump ([#2169](https://www.github.com/snakemake/snakemake-wrappers/issues/2169)) ([c0a9f8a](https://www.github.com/snakemake/snakemake-wrappers/commit/c0a9f8a437774fdf26fdd7ece9e670df2e57602d))
* autobump bio/star/align ([#2172](https://www.github.com/snakemake/snakemake-wrappers/issues/2172)) ([244f7e4](https://www.github.com/snakemake/snakemake-wrappers/commit/244f7e4753fa6b0c969055bacbc7f8398c1fa02d))
* autobump bio/star/index ([#2154](https://www.github.com/snakemake/snakemake-wrappers/issues/2154)) ([04d580e](https://www.github.com/snakemake/snakemake-wrappers/commit/04d580e29eb23f62bdda88c6ca8443eadacd2686))
* autobump bio/strelka/germline ([#2184](https://www.github.com/snakemake/snakemake-wrappers/issues/2184)) ([68d5fda](https://www.github.com/snakemake/snakemake-wrappers/commit/68d5fda7032584c38b67639d0f428e32adc63fc7))
* autobump bio/strelka/somatic ([#2155](https://www.github.com/snakemake/snakemake-wrappers/issues/2155)) ([4609785](https://www.github.com/snakemake/snakemake-wrappers/commit/4609785f33b41ae195a6a31f8565066f8ddea5db))
* autobump bio/strling/call ([#2176](https://www.github.com/snakemake/snakemake-wrappers/issues/2176)) ([fe0a308](https://www.github.com/snakemake/snakemake-wrappers/commit/fe0a308e52518db091d85eef9ab28e488049a538))
* autobump bio/strling/extract ([#2168](https://www.github.com/snakemake/snakemake-wrappers/issues/2168)) ([67778b6](https://www.github.com/snakemake/snakemake-wrappers/commit/67778b60fe4634388151f62c20b64c6c7afb8cd9))
* autobump bio/strling/index ([#2152](https://www.github.com/snakemake/snakemake-wrappers/issues/2152)) ([37038ed](https://www.github.com/snakemake/snakemake-wrappers/commit/37038edde25dd1765b325452168281859897b292))
* autobump bio/strling/merge ([#2164](https://www.github.com/snakemake/snakemake-wrappers/issues/2164)) ([ec23c18](https://www.github.com/snakemake/snakemake-wrappers/commit/ec23c189c94e9b43074d29107b49cd925b7fde12))
* autobump bio/subread/featurecounts ([#2185](https://www.github.com/snakemake/snakemake-wrappers/issues/2185)) ([fcdd09e](https://www.github.com/snakemake/snakemake-wrappers/commit/fcdd09ed7f740b7f39ce47e473c0c5570730e417))
* autobump bio/tabix/index ([#2196](https://www.github.com/snakemake/snakemake-wrappers/issues/2196)) ([baf8370](https://www.github.com/snakemake/snakemake-wrappers/commit/baf8370c8152a7242c26a37404fc3527c8cf93f5))
* autobump bio/tabix/query ([#2195](https://www.github.com/snakemake/snakemake-wrappers/issues/2195)) ([0197350](https://www.github.com/snakemake/snakemake-wrappers/commit/0197350a7df612df2c1f475714a5b3c825ef5108))
* autobump bio/transdecoder/longorfs ([#2193](https://www.github.com/snakemake/snakemake-wrappers/issues/2193)) ([44405ff](https://www.github.com/snakemake/snakemake-wrappers/commit/44405fff881ff6074932a0633e0578997ba70019))
* autobump bio/transdecoder/predict ([#2194](https://www.github.com/snakemake/snakemake-wrappers/issues/2194)) ([c736c92](https://www.github.com/snakemake/snakemake-wrappers/commit/c736c927330e5aeb78abc99663af41193ae3b5c5))
* autobump bio/trim_galore/pe ([#2197](https://www.github.com/snakemake/snakemake-wrappers/issues/2197)) ([7b18aa9](https://www.github.com/snakemake/snakemake-wrappers/commit/7b18aa99c255f6d809f1001ca40ba0c68e9f7b06))
* autobump bio/trim_galore/se ([#2198](https://www.github.com/snakemake/snakemake-wrappers/issues/2198)) ([d0006df](https://www.github.com/snakemake/snakemake-wrappers/commit/d0006df1343fda77fefb9241d47623a6109a69b1))
* autobump bio/trinity ([#2199](https://www.github.com/snakemake/snakemake-wrappers/issues/2199)) ([4db0e23](https://www.github.com/snakemake/snakemake-wrappers/commit/4db0e23314310122ad76a49a60de9394df757b65))
* autobump bio/tximport ([#2200](https://www.github.com/snakemake/snakemake-wrappers/issues/2200)) ([59213ac](https://www.github.com/snakemake/snakemake-wrappers/commit/59213ac7b1a58e080c22f7a30191e2eda40c6ead))
* autobump bio/ucsc/bedGraphToBigWig ([#2207](https://www.github.com/snakemake/snakemake-wrappers/issues/2207)) ([d9802d5](https://www.github.com/snakemake/snakemake-wrappers/commit/d9802d53cfc16edf91e49aa0dd0a605a2e2209d8))
* autobump bio/ucsc/faToTwoBit ([#2206](https://www.github.com/snakemake/snakemake-wrappers/issues/2206)) ([6df0294](https://www.github.com/snakemake/snakemake-wrappers/commit/6df0294173f486009bed93865d0ae10602727e42))
* autobump bio/ucsc/gtfToGenePred ([#2203](https://www.github.com/snakemake/snakemake-wrappers/issues/2203)) ([caff71e](https://www.github.com/snakemake/snakemake-wrappers/commit/caff71e255236125376cdd05d8d1be6b938af89e))
* autobump bio/ucsc/twoBitInfo ([#2202](https://www.github.com/snakemake/snakemake-wrappers/issues/2202)) ([5b3026b](https://www.github.com/snakemake/snakemake-wrappers/commit/5b3026b0fa0358aff7fa89e9be87c82b10d3992b))
* autobump bio/ucsc/twoBitToFa ([#2201](https://www.github.com/snakemake/snakemake-wrappers/issues/2201)) ([feeb125](https://www.github.com/snakemake/snakemake-wrappers/commit/feeb125ce93926778558312499e57a92bcb1163c))
* autobump bio/umis/bamtag ([#2205](https://www.github.com/snakemake/snakemake-wrappers/issues/2205)) ([450649a](https://www.github.com/snakemake/snakemake-wrappers/commit/450649ab4df1627e2a6990d38f5180ed1f533547))
* autobump bio/unicycler ([#2204](https://www.github.com/snakemake/snakemake-wrappers/issues/2204)) ([c057410](https://www.github.com/snakemake/snakemake-wrappers/commit/c0574106c29ac70ed58f6b67b7e49a2da184f90f))
* autobump bio/vardict ([#2212](https://www.github.com/snakemake/snakemake-wrappers/issues/2212)) ([eb59fd5](https://www.github.com/snakemake/snakemake-wrappers/commit/eb59fd5344f8d1f63e5da253a7b8a9d2f2fe6696))
* autobump bio/varscan/mpileup2indel ([#2208](https://www.github.com/snakemake/snakemake-wrappers/issues/2208)) ([3c79afb](https://www.github.com/snakemake/snakemake-wrappers/commit/3c79afb2b4a8625addd697c79e6abc70adfe3f29))
* autobump bio/varscan/mpileup2snp ([#2214](https://www.github.com/snakemake/snakemake-wrappers/issues/2214)) ([89f1a73](https://www.github.com/snakemake/snakemake-wrappers/commit/89f1a73bc1dfceb30492aaafb80ff75efe12c02a))
* autobump bio/varscan/somatic ([#2223](https://www.github.com/snakemake/snakemake-wrappers/issues/2223)) ([3a423db](https://www.github.com/snakemake/snakemake-wrappers/commit/3a423dbcd4cc3dbe4d948c0b3b53b7d74e7d5e6d))
* autobump bio/vcftools/filter ([#2209](https://www.github.com/snakemake/snakemake-wrappers/issues/2209)) ([3bac802](https://www.github.com/snakemake/snakemake-wrappers/commit/3bac80246dbb1408680affc95468a7c691f59e0e))
* autobump bio/vembrane/filter ([#2218](https://www.github.com/snakemake/snakemake-wrappers/issues/2218)) ([01c8cf5](https://www.github.com/snakemake/snakemake-wrappers/commit/01c8cf5a1be64c45767e89e296d223b3e57d27de))
* autobump bio/vembrane/table ([#2220](https://www.github.com/snakemake/snakemake-wrappers/issues/2220)) ([94fd729](https://www.github.com/snakemake/snakemake-wrappers/commit/94fd7296a015708bb3e48a6c0448213c2d2270f2))
* autobump bio/vep/annotate ([#2217](https://www.github.com/snakemake/snakemake-wrappers/issues/2217)) ([7821c79](https://www.github.com/snakemake/snakemake-wrappers/commit/7821c79000294a920deee748a51a762ff75ac7d8))
* autobump bio/vep/cache ([#2210](https://www.github.com/snakemake/snakemake-wrappers/issues/2210)) ([12d3ebd](https://www.github.com/snakemake/snakemake-wrappers/commit/12d3ebde83a3750e423ea4b1a3ce4323dde0567d))
* autobump bio/vep/plugins ([#2213](https://www.github.com/snakemake/snakemake-wrappers/issues/2213)) ([a52a0e3](https://www.github.com/snakemake/snakemake-wrappers/commit/a52a0e36414543b30bc4262f895a6e2907e5ae12))
* autobump bio/verifybamid/verifybamid2 ([#2219](https://www.github.com/snakemake/snakemake-wrappers/issues/2219)) ([96fd2f4](https://www.github.com/snakemake/snakemake-wrappers/commit/96fd2f4f6f878e2f11bab437f00558cfc06da622))
* autobump bio/vg/construct ([#2216](https://www.github.com/snakemake/snakemake-wrappers/issues/2216)) ([263ce06](https://www.github.com/snakemake/snakemake-wrappers/commit/263ce06d6bccc53cfb90bf3ff45be31fc77c2878))
* autobump bio/vg/ids ([#2224](https://www.github.com/snakemake/snakemake-wrappers/issues/2224)) ([e870ebc](https://www.github.com/snakemake/snakemake-wrappers/commit/e870ebc99fef3f817f66b603bd8e6e564058a2d0))
* autobump bio/vg/kmers ([#2225](https://www.github.com/snakemake/snakemake-wrappers/issues/2225)) ([299fb69](https://www.github.com/snakemake/snakemake-wrappers/commit/299fb6995687b0191a7192938d3c6f6bf84bcda9))
* autobump bio/vg/merge ([#2215](https://www.github.com/snakemake/snakemake-wrappers/issues/2215)) ([bbbe6f8](https://www.github.com/snakemake/snakemake-wrappers/commit/bbbe6f84d16fcdca4ceb0d7c8b8d25ddc7e5049b))
* autobump bio/vg/prune ([#2211](https://www.github.com/snakemake/snakemake-wrappers/issues/2211)) ([eff9123](https://www.github.com/snakemake/snakemake-wrappers/commit/eff9123dbd23fd0968113a2ef5a49a0de8937488))
* autobump bio/vg/sim ([#2222](https://www.github.com/snakemake/snakemake-wrappers/issues/2222)) ([9a15f42](https://www.github.com/snakemake/snakemake-wrappers/commit/9a15f428ac3fc217ab0a8e1664a388febb122a17))
* autobump bio/vsearch ([#2221](https://www.github.com/snakemake/snakemake-wrappers/issues/2221)) ([e5da30c](https://www.github.com/snakemake/snakemake-wrappers/commit/e5da30c375a4be4a42c8c59ccc55c7edb199b820))
* autobump bio/wgsim ([#2226](https://www.github.com/snakemake/snakemake-wrappers/issues/2226)) ([6406049](https://www.github.com/snakemake/snakemake-wrappers/commit/64060498047b42a90407bd81789fb613d294c7e2))
* autobump bio/whatshap/haplotag ([#2227](https://www.github.com/snakemake/snakemake-wrappers/issues/2227)) ([00c9ff2](https://www.github.com/snakemake/snakemake-wrappers/commit/00c9ff2506f3e01822f767353451cff4338c29e1))
* autobump utils/cairosvg ([#1996](https://www.github.com/snakemake/snakemake-wrappers/issues/1996)) ([17a0166](https://www.github.com/snakemake/snakemake-wrappers/commit/17a0166a28510c262e903cd05301d52f3c6aad29))
* autobump utils/datavzrd ([#2009](https://www.github.com/snakemake/snakemake-wrappers/issues/2009)) ([bda71cb](https://www.github.com/snakemake/snakemake-wrappers/commit/bda71cb5735bde899dddbe0e7d1ccb5e6e87e700))
* autobump utils/xsv ([#2228](https://www.github.com/snakemake/snakemake-wrappers/issues/2228)) ([05af587](https://www.github.com/snakemake/snakemake-wrappers/commit/05af587b9079b0195d14d1c878dd1c9ec8eda4f3))

## [2.9.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.8.0...v2.9.0) (2023-10-30)


### Features

* CNV Facets ([#1773](https://www.github.com/snakemake/snakemake-wrappers/issues/1773)) ([74f5e4a](https://www.github.com/snakemake/snakemake-wrappers/commit/74f5e4a72ebb3abed014380314e63ca3db9f36f4))
* encode fastq downloader ([#1798](https://www.github.com/snakemake/snakemake-wrappers/issues/1798)) ([1cc3e00](https://www.github.com/snakemake/snakemake-wrappers/commit/1cc3e00c6bbb3761d1ffd07b26acd18a1caa746d))
* for bwa, auto infer block size, extra tests, code cleanup and add docs ([#1774](https://www.github.com/snakemake/snakemake-wrappers/issues/1774)) ([66940e3](https://www.github.com/snakemake/snakemake-wrappers/commit/66940e3c69e1a06a6e9b771d10e29b9eb03d9f24))
* Gseapy ([#1822](https://www.github.com/snakemake/snakemake-wrappers/issues/1822)) ([2a50eb0](https://www.github.com/snakemake/snakemake-wrappers/commit/2a50eb0b3567843f0082496f84999d1a9a08e2ab))
* unaligned bam input support for minimap2 alignment ([#1863](https://www.github.com/snakemake/snakemake-wrappers/issues/1863)) ([76280a5](https://www.github.com/snakemake/snakemake-wrappers/commit/76280a592677e81dc092c66351bc6eb7801da172))


### Bug Fixes

* for nonpareil, use pigz and pbzip2 and auto infer of -X ([#1776](https://www.github.com/snakemake/snakemake-wrappers/issues/1776)) ([45860bf](https://www.github.com/snakemake/snakemake-wrappers/commit/45860bfc1a1509311182f7057f4b7a6210be0423))
* moving to utils ([#1770](https://www.github.com/snakemake/snakemake-wrappers/issues/1770)) ([b5c0c01](https://www.github.com/snakemake/snakemake-wrappers/commit/b5c0c016b6a3c9c46672d5e5ee13bda934cbb970))


### Performance Improvements

* autopin bio/bwa/mem ([#1907](https://www.github.com/snakemake/snakemake-wrappers/issues/1907)) ([99e9f60](https://www.github.com/snakemake/snakemake-wrappers/commit/99e9f604eba4e77c4b3f69cad0e25114c72ff1fd))
* autopin bio/multiqc ([#1906](https://www.github.com/snakemake/snakemake-wrappers/issues/1906)) ([6c67666](https://www.github.com/snakemake/snakemake-wrappers/commit/6c676668b49210d8e99bec6948003421528ac5c4))

## [2.8.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.7.0...v2.8.0) (2023-10-26)


### Features

* methyldackel extract ([#1823](https://www.github.com/snakemake/snakemake-wrappers/issues/1823)) ([930d64e](https://www.github.com/snakemake/snakemake-wrappers/commit/930d64e7cfc07e52a0d872ace455a71bdabe7728))
* Unified seqtk wrapper ([#1777](https://www.github.com/snakemake/snakemake-wrappers/issues/1777)) ([0e7fff5](https://www.github.com/snakemake/snakemake-wrappers/commit/0e7fff5e839d6c14e07ab0b84f84bd622c1b5110))


### Bug Fixes

* add readthedocs config file v2 ([#1902](https://www.github.com/snakemake/snakemake-wrappers/issues/1902)) ([bb29891](https://www.github.com/snakemake/snakemake-wrappers/commit/bb29891d6c396ea44af35b3b9cbee30d2755188a))

## [2.7.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.6.1...v2.7.0) (2023-10-23)


### Features

* Cnvkit call wrapper ([#1879](https://www.github.com/snakemake/snakemake-wrappers/issues/1879)) ([db073db](https://www.github.com/snakemake/snakemake-wrappers/commit/db073dbfe00e19e71e198af2c809b8a71662a112))
* cnvkit diagram wrapper ([#1881](https://www.github.com/snakemake/snakemake-wrappers/issues/1881)) ([d3cfc11](https://www.github.com/snakemake/snakemake-wrappers/commit/d3cfc1176e877f324a38c125aa6d3a6f4ad7f556))
* Cnvkit target wrapper ([#1878](https://www.github.com/snakemake/snakemake-wrappers/issues/1878)) ([07f3b16](https://www.github.com/snakemake/snakemake-wrappers/commit/07f3b164d3f45512daff3c129bf5ce0e42608dae))
* whatshap haplotag ([#1862](https://www.github.com/snakemake/snakemake-wrappers/issues/1862)) ([d55ed6a](https://www.github.com/snakemake/snakemake-wrappers/commit/d55ed6a5913bb79d89766c217e7f4700ebe6fe48))
* wrapper for cnvkit batch ([#1877](https://www.github.com/snakemake/snakemake-wrappers/issues/1877)) ([40bfc5d](https://www.github.com/snakemake/snakemake-wrappers/commit/40bfc5d6b357b5be24fe4a51953dcaf7a44a7a1b))


### Bug Fixes

* Update environment.yaml of MultiQC ([#1873](https://www.github.com/snakemake/snakemake-wrappers/issues/1873)) ([bcd4a24](https://www.github.com/snakemake/snakemake-wrappers/commit/bcd4a24f99bf6e289db22ffcadd670f91677d8d2))


### Performance Improvements

* autobump bio/bcftools/call ([#1855](https://www.github.com/snakemake/snakemake-wrappers/issues/1855)) ([ef3ba47](https://www.github.com/snakemake/snakemake-wrappers/commit/ef3ba4738843404665dacd9a379c4b7dbe283119))
* autobump bio/bcftools/filter ([#1889](https://www.github.com/snakemake/snakemake-wrappers/issues/1889)) ([088aa72](https://www.github.com/snakemake/snakemake-wrappers/commit/088aa721e040c7b6e27c156e610f10c645378d7d))
* autobump bio/bcftools/merge ([#1887](https://www.github.com/snakemake/snakemake-wrappers/issues/1887)) ([43781d6](https://www.github.com/snakemake/snakemake-wrappers/commit/43781d6e7a2d2c356b216d8d9cb8474df829c085))
* autobump bio/bcftools/mpileup ([#1896](https://www.github.com/snakemake/snakemake-wrappers/issues/1896)) ([0dcb3cc](https://www.github.com/snakemake/snakemake-wrappers/commit/0dcb3cc3a51eab6ce0996e0ec6e33949662dd251))
* autobump bio/bcftools/norm ([#1884](https://www.github.com/snakemake/snakemake-wrappers/issues/1884)) ([30a9f95](https://www.github.com/snakemake/snakemake-wrappers/commit/30a9f95f98f18ff93b3411d374e08aa90cb15336))
* autobump bio/bcftools/reheader ([#1841](https://www.github.com/snakemake/snakemake-wrappers/issues/1841)) ([f450530](https://www.github.com/snakemake/snakemake-wrappers/commit/f450530b5fe38fc8fd6d964b22fb535c99c91ae5))
* autobump bio/bcftools/stats ([#1883](https://www.github.com/snakemake/snakemake-wrappers/issues/1883)) ([9ac746c](https://www.github.com/snakemake/snakemake-wrappers/commit/9ac746c3e73fcd4a484c16dda9a29ea945add33a))
* autobump bio/bcftools/view ([#1842](https://www.github.com/snakemake/snakemake-wrappers/issues/1842)) ([19e89ab](https://www.github.com/snakemake/snakemake-wrappers/commit/19e89abed1d3daae3f5875650d899fd4abc0df17))
* autobump bio/bismark/bam2nuc ([#1867](https://www.github.com/snakemake/snakemake-wrappers/issues/1867)) ([f29483a](https://www.github.com/snakemake/snakemake-wrappers/commit/f29483a63b6a81c99ec40ee3a250f221d2961a9d))
* autobump bio/bismark/bismark ([#1853](https://www.github.com/snakemake/snakemake-wrappers/issues/1853)) ([6babc2a](https://www.github.com/snakemake/snakemake-wrappers/commit/6babc2a3881cccae83efc90b550bc4d96994fbab))
* autobump bio/bismark/bismark2bedGraph ([#1894](https://www.github.com/snakemake/snakemake-wrappers/issues/1894)) ([6bd04db](https://www.github.com/snakemake/snakemake-wrappers/commit/6bd04dba4fbc94b1e671476c45c0668148551424))
* autobump bio/bismark/bismark2report ([#1871](https://www.github.com/snakemake/snakemake-wrappers/issues/1871)) ([c5003d5](https://www.github.com/snakemake/snakemake-wrappers/commit/c5003d5c711c3fd48e49d73957d3494b8554339e))
* autobump bio/bismark/bismark2summary ([#1882](https://www.github.com/snakemake/snakemake-wrappers/issues/1882)) ([3256aa1](https://www.github.com/snakemake/snakemake-wrappers/commit/3256aa1fe77ecf9773cc7531c9aca34aca142f17))
* autobump bio/bismark/deduplicate_bismark ([#1846](https://www.github.com/snakemake/snakemake-wrappers/issues/1846)) ([b18c5c7](https://www.github.com/snakemake/snakemake-wrappers/commit/b18c5c76149a3d2065273bc7bbf7779719e15a1d))
* autobump bio/bowtie2/build ([#1893](https://www.github.com/snakemake/snakemake-wrappers/issues/1893)) ([dc2f765](https://www.github.com/snakemake/snakemake-wrappers/commit/dc2f765252cac563fb16a84c3c4d6892ab0c5f9d))
* autobump bio/bwa-meme/mem ([#1861](https://www.github.com/snakemake/snakemake-wrappers/issues/1861)) ([31be794](https://www.github.com/snakemake/snakemake-wrappers/commit/31be794f7961dbb2eb627e9726ce80377de5f981))
* autobump bio/bwa/samxe ([#1895](https://www.github.com/snakemake/snakemake-wrappers/issues/1895)) ([929ddd6](https://www.github.com/snakemake/snakemake-wrappers/commit/929ddd60ac6c9ea77540b3d250a415221222555a))
* autobump bio/deeptools/computematrix ([#1848](https://www.github.com/snakemake/snakemake-wrappers/issues/1848)) ([0fdcd5a](https://www.github.com/snakemake/snakemake-wrappers/commit/0fdcd5a0809b6843cac2a2fbd2fe2b85c6514e39))
* autobump bio/gatk/applybqsr ([#1866](https://www.github.com/snakemake/snakemake-wrappers/issues/1866)) ([201dea6](https://www.github.com/snakemake/snakemake-wrappers/commit/201dea66f82fade2ece26538cbbf797277c974a7))
* autobump bio/gatk3/baserecalibrator ([#1847](https://www.github.com/snakemake/snakemake-wrappers/issues/1847)) ([80edec6](https://www.github.com/snakemake/snakemake-wrappers/commit/80edec6b4ee9b378c124653727185774f32b11bc))
* autobump bio/gatk3/indelrealigner ([#1890](https://www.github.com/snakemake/snakemake-wrappers/issues/1890)) ([7803fbe](https://www.github.com/snakemake/snakemake-wrappers/commit/7803fbebec46711a46e7748d2a51e161db0794e6))
* autobump bio/gatk3/printreads ([#1869](https://www.github.com/snakemake/snakemake-wrappers/issues/1869)) ([58fe71a](https://www.github.com/snakemake/snakemake-wrappers/commit/58fe71ab5e022df46ed7bb157352b202166b1086))
* autobump bio/lofreq/call ([#1860](https://www.github.com/snakemake/snakemake-wrappers/issues/1860)) ([ca5409d](https://www.github.com/snakemake/snakemake-wrappers/commit/ca5409d7b0e8d9abc82cc3fce57b8ae8b0f1d702))
* autobump bio/mashmap ([#1886](https://www.github.com/snakemake/snakemake-wrappers/issues/1886)) ([4d277b2](https://www.github.com/snakemake/snakemake-wrappers/commit/4d277b2dcf33bb359244137e44d3da9b222f878b))
* autobump bio/paladin/align ([#1897](https://www.github.com/snakemake/snakemake-wrappers/issues/1897)) ([7b5dc11](https://www.github.com/snakemake/snakemake-wrappers/commit/7b5dc11b916c734f484493459776555a0e561276))
* autobump bio/pandora/index ([#1868](https://www.github.com/snakemake/snakemake-wrappers/issues/1868)) ([bc7b88a](https://www.github.com/snakemake/snakemake-wrappers/commit/bc7b88a970972a56e7ba64060294bdd1f853171b))
* autobump bio/picard/collecthsmetrics ([#1865](https://www.github.com/snakemake/snakemake-wrappers/issues/1865)) ([6028b5d](https://www.github.com/snakemake/snakemake-wrappers/commit/6028b5d43a9422b3e9b23d950c9d574196e53c14))
* autobump bio/picard/collectrnaseqmetrics ([#1844](https://www.github.com/snakemake/snakemake-wrappers/issues/1844)) ([bd4ac2f](https://www.github.com/snakemake/snakemake-wrappers/commit/bd4ac2f0c14136c4c4b9fe44bf9f9b6721cbc318))
* autobump bio/pretext/map ([#1851](https://www.github.com/snakemake/snakemake-wrappers/issues/1851)) ([f4bb492](https://www.github.com/snakemake/snakemake-wrappers/commit/f4bb49242f87c5df15eb0d2071cbe3a8cb69f2be))
* autobump bio/salmon/quant ([#1888](https://www.github.com/snakemake/snakemake-wrappers/issues/1888)) ([af65c24](https://www.github.com/snakemake/snakemake-wrappers/commit/af65c24c53bfd53ff73147273d662ab714d6418e))
* autobump bio/samtools/calmd ([#1843](https://www.github.com/snakemake/snakemake-wrappers/issues/1843)) ([3c5bd68](https://www.github.com/snakemake/snakemake-wrappers/commit/3c5bd6885af82d589d64e863b45b2b8fc328f570))
* autobump bio/samtools/faidx ([#1891](https://www.github.com/snakemake/snakemake-wrappers/issues/1891)) ([2d4444e](https://www.github.com/snakemake/snakemake-wrappers/commit/2d4444e3e98320dbe42a2312de2b7b34a57b3ab4))
* autobump bio/samtools/index ([#1849](https://www.github.com/snakemake/snakemake-wrappers/issues/1849)) ([2dd024c](https://www.github.com/snakemake/snakemake-wrappers/commit/2dd024ca903d67ecb95b94821746ab5d90d0f1f3))
* autobump bio/snpeff/download ([#1892](https://www.github.com/snakemake/snakemake-wrappers/issues/1892)) ([920eb68](https://www.github.com/snakemake/snakemake-wrappers/commit/920eb68334dc17b21e246b85646a60b8174ab5d4))
* autobump bio/snpsift/dbnsfp ([#1852](https://www.github.com/snakemake/snakemake-wrappers/issues/1852)) ([f8453d6](https://www.github.com/snakemake/snakemake-wrappers/commit/f8453d6c40d7bb4c56f03b4fbbbadaf1b28a8097))
* autobump bio/snpsift/dbnsfp ([#1898](https://www.github.com/snakemake/snakemake-wrappers/issues/1898)) ([3b48591](https://www.github.com/snakemake/snakemake-wrappers/commit/3b48591460656f3a4799b2ec3d31cf6d1746c29d))
* autobump bio/snpsift/gwascat ([#1870](https://www.github.com/snakemake/snakemake-wrappers/issues/1870)) ([c55a0b5](https://www.github.com/snakemake/snakemake-wrappers/commit/c55a0b52ff99d6a093da64e6c2629042662452ec))
* autobump bio/snpsift/varType ([#1885](https://www.github.com/snakemake/snakemake-wrappers/issues/1885)) ([b456dc5](https://www.github.com/snakemake/snakemake-wrappers/commit/b456dc55ca48d43c5d9187fa0243a03681d654db))
* autobump bio/spades/metaspades ([#1859](https://www.github.com/snakemake/snakemake-wrappers/issues/1859)) ([ef24b5d](https://www.github.com/snakemake/snakemake-wrappers/commit/ef24b5da60de82893f461e9487cf2e477fb75228))
* autobump bio/tabix/query ([#1858](https://www.github.com/snakemake/snakemake-wrappers/issues/1858)) ([59a11ca](https://www.github.com/snakemake/snakemake-wrappers/commit/59a11caf111a7b7740ec862219f9abad49945110))
* autobump bio/umis/bamtag ([#1872](https://www.github.com/snakemake/snakemake-wrappers/issues/1872)) ([c44ef6b](https://www.github.com/snakemake/snakemake-wrappers/commit/c44ef6b6b7f54fe047e8a3c7c8c98b3a0327ebc4))
* autobump bio/vg/construct ([#1857](https://www.github.com/snakemake/snakemake-wrappers/issues/1857)) ([addcbdc](https://www.github.com/snakemake/snakemake-wrappers/commit/addcbdc120b5980b2d85530ef99c4bfa0030e1b6))
* autobump bio/vg/ids ([#1854](https://www.github.com/snakemake/snakemake-wrappers/issues/1854)) ([ea9934c](https://www.github.com/snakemake/snakemake-wrappers/commit/ea9934cfacbc7d9c8f1a97ff3e210e42d12bd931))
* autobump utils/datavzrd ([#1856](https://www.github.com/snakemake/snakemake-wrappers/issues/1856)) ([723fd8b](https://www.github.com/snakemake/snakemake-wrappers/commit/723fd8b28eb139227e4fdbec18eaa7435cb11502))

### [2.6.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.6.0...v2.6.1) (2023-10-04)


### Bug Fixes

* build docs on fork ([#1800](https://www.github.com/snakemake/snakemake-wrappers/issues/1800)) ([d859765](https://www.github.com/snakemake/snakemake-wrappers/commit/d85976505651052a00777fddcc0bf2178fbf0e4a))
* fix freebayes parallel ([#1807](https://www.github.com/snakemake/snakemake-wrappers/issues/1807)) ([2aa2f62](https://www.github.com/snakemake/snakemake-wrappers/commit/2aa2f62af06213d3060378b5600c10d5e79787fa))
* Fix MultiQC output file issues ([#1796](https://www.github.com/snakemake/snakemake-wrappers/issues/1796)) ([ecc45e8](https://www.github.com/snakemake/snakemake-wrappers/commit/ecc45e819f5e72b71ee777fa336da8c61a84758c))
* genomepy wrapper ([#1795](https://www.github.com/snakemake/snakemake-wrappers/issues/1795)) ([53231a0](https://www.github.com/snakemake/snakemake-wrappers/commit/53231a0ef6b9e8045081456e2a129fccfb744f18))
* gffread - properly generate fasta output ([#1797](https://www.github.com/snakemake/snakemake-wrappers/issues/1797)) ([89ea854](https://www.github.com/snakemake/snakemake-wrappers/commit/89ea854d1f2e26bed121650e3ae9f60a1ab84dec))


### Performance Improvements

* autobump bio/blast/makeblastdb ([#1786](https://www.github.com/snakemake/snakemake-wrappers/issues/1786)) ([a5db830](https://www.github.com/snakemake/snakemake-wrappers/commit/a5db830243346385601ab9c0851f221276df3342))
* autobump bio/bwa-mem2/mem ([#1826](https://www.github.com/snakemake/snakemake-wrappers/issues/1826)) ([37665c1](https://www.github.com/snakemake/snakemake-wrappers/commit/37665c12b4ba2760f0e078e781717ac9fa4efad8))
* autobump bio/bwa-memx/mem ([#1802](https://www.github.com/snakemake/snakemake-wrappers/issues/1802)) ([9ceb997](https://www.github.com/snakemake/snakemake-wrappers/commit/9ceb9974e99677accdfdbca32e17c496f880a901))
* autobump bio/bwa/samse ([#1831](https://www.github.com/snakemake/snakemake-wrappers/issues/1831)) ([8f93262](https://www.github.com/snakemake/snakemake-wrappers/commit/8f932627d344ded2331b396d6e585170bfaa4010))
* autobump bio/bwa/samxe ([#1833](https://www.github.com/snakemake/snakemake-wrappers/issues/1833)) ([95799fc](https://www.github.com/snakemake/snakemake-wrappers/commit/95799fc241a2cfb541464cba62f63056b350a0b7))
* autobump bio/deeptools/alignmentsieve ([#1790](https://www.github.com/snakemake/snakemake-wrappers/issues/1790)) ([cfa4cf7](https://www.github.com/snakemake/snakemake-wrappers/commit/cfa4cf7ca443a0d24858c804a55e563827e550b3))
* autobump bio/deeptools/alignmentsieve ([#1832](https://www.github.com/snakemake/snakemake-wrappers/issues/1832)) ([2623b3a](https://www.github.com/snakemake/snakemake-wrappers/commit/2623b3afce1baada662237259f4c3d6c2b3a5d33))
* autobump bio/deeptools/computematrix ([#1784](https://www.github.com/snakemake/snakemake-wrappers/issues/1784)) ([ccb2958](https://www.github.com/snakemake/snakemake-wrappers/commit/ccb2958e27d0ce3d5db13bbcf17581b3a6ccc0ae))
* autobump bio/deeptools/plotcoverage ([#1815](https://www.github.com/snakemake/snakemake-wrappers/issues/1815)) ([693e904](https://www.github.com/snakemake/snakemake-wrappers/commit/693e90453a938806b7b395a9db6c0f773f50f866))
* autobump bio/deeptools/plotprofile ([#1830](https://www.github.com/snakemake/snakemake-wrappers/issues/1830)) ([6f49c46](https://www.github.com/snakemake/snakemake-wrappers/commit/6f49c466ae3737afec0d3b4632625a9d4d62967d))
* autobump bio/deseq2/wald ([#1804](https://www.github.com/snakemake/snakemake-wrappers/issues/1804)) ([fbc6345](https://www.github.com/snakemake/snakemake-wrappers/commit/fbc6345cdaee3c1452aba52dfa007603b90a5d4f))
* autobump bio/gatk/combinegvcfs ([#1817](https://www.github.com/snakemake/snakemake-wrappers/issues/1817)) ([1cc8adc](https://www.github.com/snakemake/snakemake-wrappers/commit/1cc8adc07817b40746ec8ec58146e4f301ecf258))
* autobump bio/gatk3/baserecalibrator ([#1792](https://www.github.com/snakemake/snakemake-wrappers/issues/1792)) ([7b1b2c3](https://www.github.com/snakemake/snakemake-wrappers/commit/7b1b2c3c7eb05867b5cc770a28f65323b2cc18c4))
* autobump bio/gatk3/indelrealigner ([#1835](https://www.github.com/snakemake/snakemake-wrappers/issues/1835)) ([3d3d31c](https://www.github.com/snakemake/snakemake-wrappers/commit/3d3d31c9df0c9af9e1311cb691b7061c2f5a3fa9))
* autobump bio/gatk3/printreads ([#1839](https://www.github.com/snakemake/snakemake-wrappers/issues/1839)) ([c1d182a](https://www.github.com/snakemake/snakemake-wrappers/commit/c1d182a1dbbe3a70c9b7db2fae50e73224cba021))
* autobump bio/gatk3/realignertargetcreator ([#1814](https://www.github.com/snakemake/snakemake-wrappers/issues/1814)) ([0936b25](https://www.github.com/snakemake/snakemake-wrappers/commit/0936b25c211323af2cac819fc4d7982aad3bfa2c))
* autobump bio/gdc-api/bam-slicing ([#1806](https://www.github.com/snakemake/snakemake-wrappers/issues/1806)) ([f723338](https://www.github.com/snakemake/snakemake-wrappers/commit/f72333859b9f536990c22899ae2a720010a91d5d))
* autobump bio/igv-reports ([#1788](https://www.github.com/snakemake/snakemake-wrappers/issues/1788)) ([3ecdb17](https://www.github.com/snakemake/snakemake-wrappers/commit/3ecdb179679859e5ad8561f93c7476ef9430525c))
* autobump bio/meryl/count ([#1787](https://www.github.com/snakemake/snakemake-wrappers/issues/1787)) ([486d99b](https://www.github.com/snakemake/snakemake-wrappers/commit/486d99ba318e6a7b806077003f97f7b693e98a1d))
* autobump bio/multiqc ([#1811](https://www.github.com/snakemake/snakemake-wrappers/issues/1811)) ([221db0b](https://www.github.com/snakemake/snakemake-wrappers/commit/221db0b94a6a4f3658ce6a258bd868dc39ac79bd))
* autobump bio/pbmm2/align ([#1783](https://www.github.com/snakemake/snakemake-wrappers/issues/1783)) ([756a11d](https://www.github.com/snakemake/snakemake-wrappers/commit/756a11d317cdd332771925ae910c25eef39ea83e))
* autobump bio/pbmm2/index ([#1801](https://www.github.com/snakemake/snakemake-wrappers/issues/1801)) ([a91b214](https://www.github.com/snakemake/snakemake-wrappers/commit/a91b214b643452561bd3de81a6283c100471a427))
* autobump bio/picard/collectalignmentsummarymetrics ([#1803](https://www.github.com/snakemake/snakemake-wrappers/issues/1803)) ([3d727b4](https://www.github.com/snakemake/snakemake-wrappers/commit/3d727b4559cb8c2eb2a98d714b6a5f54d336b9c4))
* autobump bio/picard/collectmultiplemetrics ([#1791](https://www.github.com/snakemake/snakemake-wrappers/issues/1791)) ([a289b27](https://www.github.com/snakemake/snakemake-wrappers/commit/a289b276540d2da42920db86f9117090c8f39ddc))
* autobump bio/picard/collecttargetedpcrmetrics ([#1810](https://www.github.com/snakemake/snakemake-wrappers/issues/1810)) ([c64d4fd](https://www.github.com/snakemake/snakemake-wrappers/commit/c64d4fdf2c3da9ad31b40317678da3bb9937cfef))
* autobump bio/picard/createsequencedictionary ([#1812](https://www.github.com/snakemake/snakemake-wrappers/issues/1812)) ([3477e80](https://www.github.com/snakemake/snakemake-wrappers/commit/3477e80abdfa47c61f6c59c12530270fc81fd6ae))
* autobump bio/picard/markduplicates ([#1837](https://www.github.com/snakemake/snakemake-wrappers/issues/1837)) ([4e6af3d](https://www.github.com/snakemake/snakemake-wrappers/commit/4e6af3d7ce8c5d72698233d0515286759df7e8e4))
* autobump bio/picard/mergesamfiles ([#1818](https://www.github.com/snakemake/snakemake-wrappers/issues/1818)) ([0768970](https://www.github.com/snakemake/snakemake-wrappers/commit/07689707f145ad856a38dd47854b029421adf35c))
* autobump bio/picard/revertsam ([#1825](https://www.github.com/snakemake/snakemake-wrappers/issues/1825)) ([042589a](https://www.github.com/snakemake/snakemake-wrappers/commit/042589af84f216d12ad33ab7219efa7551c463d0))
* autobump bio/picard/samtofastq ([#1824](https://www.github.com/snakemake/snakemake-wrappers/issues/1824)) ([7a30dd8](https://www.github.com/snakemake/snakemake-wrappers/commit/7a30dd8191e4d0fb01a67dff22244ca9e0064bf3))
* autobump bio/picard/sortsam ([#1819](https://www.github.com/snakemake/snakemake-wrappers/issues/1819)) ([a7e1233](https://www.github.com/snakemake/snakemake-wrappers/commit/a7e1233d34f17c6dce50bc49b1a9b29dee1a7c0c))
* autobump bio/samtools/idxstats ([#1780](https://www.github.com/snakemake/snakemake-wrappers/issues/1780)) ([01985b9](https://www.github.com/snakemake/snakemake-wrappers/commit/01985b97b60be1ce4ca35958a5c4851ef98602dc))
* autobump bio/samtools/merge ([#1838](https://www.github.com/snakemake/snakemake-wrappers/issues/1838)) ([8a3c3c9](https://www.github.com/snakemake/snakemake-wrappers/commit/8a3c3c9276f41e3f4fc9085aa20fb164b06576a8))
* autobump bio/seqkit ([#1805](https://www.github.com/snakemake/snakemake-wrappers/issues/1805)) ([923c7ba](https://www.github.com/snakemake/snakemake-wrappers/commit/923c7bab7eb6dc4c8fb5825776c73c543e7a7207))
* autobump bio/spades/metaspades ([#1820](https://www.github.com/snakemake/snakemake-wrappers/issues/1820)) ([755343f](https://www.github.com/snakemake/snakemake-wrappers/commit/755343f58a0ec67f3d346b00a7ec8482fd461fa0))
* autobump bio/sra-tools/fasterq-dump ([#1793](https://www.github.com/snakemake/snakemake-wrappers/issues/1793)) ([873937e](https://www.github.com/snakemake/snakemake-wrappers/commit/873937e25308ede4a55fbf13698cb5e410aa8ad5))
* autobump bio/sra-tools/fasterq-dump ([#1813](https://www.github.com/snakemake/snakemake-wrappers/issues/1813)) ([ffdb0a4](https://www.github.com/snakemake/snakemake-wrappers/commit/ffdb0a4e64c4e5fbd8169ed6968416f5100dc285))
* autobump bio/star/align ([#1829](https://www.github.com/snakemake/snakemake-wrappers/issues/1829)) ([524917b](https://www.github.com/snakemake/snakemake-wrappers/commit/524917b4b8e0b02257cc02da5f128f2ef30ddd33))
* autobump bio/star/index ([#1836](https://www.github.com/snakemake/snakemake-wrappers/issues/1836)) ([0530063](https://www.github.com/snakemake/snakemake-wrappers/commit/05300632895eb4b1250de91a51e2c42b6da62adc))
* autobump bio/varscan/mpileup2indel ([#1821](https://www.github.com/snakemake/snakemake-wrappers/issues/1821)) ([cb2adbe](https://www.github.com/snakemake/snakemake-wrappers/commit/cb2adbe5cf4e0c73bd99f7454cdb2f64e66e1299))
* autobump bio/varscan/mpileup2snp ([#1827](https://www.github.com/snakemake/snakemake-wrappers/issues/1827)) ([40545ad](https://www.github.com/snakemake/snakemake-wrappers/commit/40545ad04b7bc37f36d97f562f19028b9d7e71ee))
* autobump bio/varscan/somatic ([#1834](https://www.github.com/snakemake/snakemake-wrappers/issues/1834)) ([a830aa7](https://www.github.com/snakemake/snakemake-wrappers/commit/a830aa7344c7edc8333d256c3fbf1ce2fb717e2a))
* autobump bio/vg/construct ([#1779](https://www.github.com/snakemake/snakemake-wrappers/issues/1779)) ([0a9bf2d](https://www.github.com/snakemake/snakemake-wrappers/commit/0a9bf2da9b053473069ac119db2a574790aa1112))
* autobump bio/vg/ids ([#1781](https://www.github.com/snakemake/snakemake-wrappers/issues/1781)) ([eb1e70e](https://www.github.com/snakemake/snakemake-wrappers/commit/eb1e70e7a0ce12c31be75d3ab682c9458164b9cd))
* autobump bio/vg/kmers ([#1828](https://www.github.com/snakemake/snakemake-wrappers/issues/1828)) ([5903848](https://www.github.com/snakemake/snakemake-wrappers/commit/5903848e1ac52f75c53fbd743f9847fe37a4be79))
* autobump bio/vg/merge ([#1816](https://www.github.com/snakemake/snakemake-wrappers/issues/1816)) ([6feb18f](https://www.github.com/snakemake/snakemake-wrappers/commit/6feb18fd1eb09b139c7c6018273afc9903d99fe2))
* autobump bio/vg/sim ([#1785](https://www.github.com/snakemake/snakemake-wrappers/issues/1785)) ([951ca2f](https://www.github.com/snakemake/snakemake-wrappers/commit/951ca2f81f2a03044af582fcc072f4dd7363c4a4))

## [2.6.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.5.0...v2.6.0) (2023-08-25)


### Features

* add galah wrapper ([#1754](https://www.github.com/snakemake/snakemake-wrappers/issues/1754)) ([083688a](https://www.github.com/snakemake/snakemake-wrappers/commit/083688a059439b1b886ac2db95fd53530d5bef11))
* Enhanced-volcano ([#1521](https://www.github.com/snakemake/snakemake-wrappers/issues/1521)) ([0bd316d](https://www.github.com/snakemake/snakemake-wrappers/commit/0bd316db902ed47d36250b4464f5d8710b295a61))
* Immunedeconv ([#1741](https://www.github.com/snakemake/snakemake-wrappers/issues/1741)) ([97b5bde](https://www.github.com/snakemake/snakemake-wrappers/commit/97b5bdec2bcff9b26de7e6889cba72521b845e99))


### Bug Fixes

* Bwa mem threads ([#1743](https://www.github.com/snakemake/snakemake-wrappers/issues/1743)) ([e35e312](https://www.github.com/snakemake/snakemake-wrappers/commit/e35e31219af8e7bf7b2f7174ddd7ade93abf7cad))


### Performance Improvements

* autobump bio/hifiasm ([#1768](https://www.github.com/snakemake/snakemake-wrappers/issues/1768)) ([5795e2c](https://www.github.com/snakemake/snakemake-wrappers/commit/5795e2c31d0d6742908223fb7ff86fb186dd09f5))
* autobump bio/sourmash/compute ([#1767](https://www.github.com/snakemake/snakemake-wrappers/issues/1767)) ([412f289](https://www.github.com/snakemake/snakemake-wrappers/commit/412f2892dc44c7218656b23dc6d83cb15e15eae0))
* autobump bio/vg/prune ([#1769](https://www.github.com/snakemake/snakemake-wrappers/issues/1769)) ([fe30289](https://www.github.com/snakemake/snakemake-wrappers/commit/fe302896b2550585c257ac0311ed9c5ee462a2dd))
* update datavzrd 2.23.8 ([#1764](https://www.github.com/snakemake/snakemake-wrappers/issues/1764)) ([2f76671](https://www.github.com/snakemake/snakemake-wrappers/commit/2f766717bbf35dfaf748c02757b4f5eef0ff96ba))

## [2.5.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.4.0...v2.5.0) (2023-08-24)


### Features

* bedtools split wrapper ([#1744](https://www.github.com/snakemake/snakemake-wrappers/issues/1744)) ([bad454d](https://www.github.com/snakemake/snakemake-wrappers/commit/bad454d662d15c8beac15ffa2307164d4d708d07))


### Bug Fixes

* ensembl-variation - remove index ([#1760](https://www.github.com/snakemake/snakemake-wrappers/issues/1760)) ([702a85b](https://www.github.com/snakemake/snakemake-wrappers/commit/702a85b7a2564fc9e94038825a12ed514192bc78))


### Performance Improvements

* bump datavzrd to 2.23.6 ([#1757](https://www.github.com/snakemake/snakemake-wrappers/issues/1757)) ([c500eb9](https://www.github.com/snakemake/snakemake-wrappers/commit/c500eb9682ef1230a1023211b1d96443cb341ab7))
* update datavzrd 2.23.7 ([#1763](https://www.github.com/snakemake/snakemake-wrappers/issues/1763)) ([b19813d](https://www.github.com/snakemake/snakemake-wrappers/commit/b19813d62a43db1d168087dccb62f85cd466a4cf))
* update picard markduplicates ([#1761](https://www.github.com/snakemake/snakemake-wrappers/issues/1761)) ([0c8aad0](https://www.github.com/snakemake/snakemake-wrappers/commit/0c8aad0a9e786850d49c49bb0baef21b5335883d))
* update snakemake wrapper utils ([#1762](https://www.github.com/snakemake/snakemake-wrappers/issues/1762)) ([371f337](https://www.github.com/snakemake/snakemake-wrappers/commit/371f3376d27efcacb679e0b2b645ba6ee33be24c))
* update vep annotate ([#1759](https://www.github.com/snakemake/snakemake-wrappers/issues/1759)) ([f7e372f](https://www.github.com/snakemake/snakemake-wrappers/commit/f7e372f4d1576306975ad611e5aeb1c335b6658a))

## [2.4.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.3.2...v2.4.0) (2023-08-21)


### Features

* Add support for threads to GATK genomicsdbimport ([#1742](https://www.github.com/snakemake/snakemake-wrappers/issues/1742)) ([b312e5c](https://www.github.com/snakemake/snakemake-wrappers/commit/b312e5c2fcd90ae709b5d799cdf378fb12a60301))
* add test for datavzrd ([#1755](https://www.github.com/snakemake/snakemake-wrappers/issues/1755)) ([996bdcf](https://www.github.com/snakemake/snakemake-wrappers/commit/996bdcf2a96535b967dfa483c363a5496f4b3906))


### Performance Improvements

* autobump bio/bcftools/stats ([#1751](https://www.github.com/snakemake/snakemake-wrappers/issues/1751)) ([56843f8](https://www.github.com/snakemake/snakemake-wrappers/commit/56843f87623f917a2820527d3b849a4e1263ca77))
* autobump bio/bismark/bismark2bedGraph ([#1747](https://www.github.com/snakemake/snakemake-wrappers/issues/1747)) ([d954019](https://www.github.com/snakemake/snakemake-wrappers/commit/d954019a308672778c3d969e809a076c667ba88d))
* autobump bio/busco ([#1739](https://www.github.com/snakemake/snakemake-wrappers/issues/1739)) ([d04d8d7](https://www.github.com/snakemake/snakemake-wrappers/commit/d04d8d73927354e8e43f222dc6d1d0de4dc1c4ce))
* autobump bio/delly ([#1735](https://www.github.com/snakemake/snakemake-wrappers/issues/1735)) ([479ac84](https://www.github.com/snakemake/snakemake-wrappers/commit/479ac84e866f61b0d905e7c9e7048f2bdb0ec772))
* autobump bio/fastqc ([#1750](https://www.github.com/snakemake/snakemake-wrappers/issues/1750)) ([8856ac6](https://www.github.com/snakemake/snakemake-wrappers/commit/8856ac647e5aea51f7aceab889cbc19fbf484311))
* autobump bio/gatk/estimatelibrarycomplexity ([#1736](https://www.github.com/snakemake/snakemake-wrappers/issues/1736)) ([b318de6](https://www.github.com/snakemake/snakemake-wrappers/commit/b318de6011e7dbab95465bb3d8961668f7ec8a39))
* autobump bio/gatk3/printreads ([#1731](https://www.github.com/snakemake/snakemake-wrappers/issues/1731)) ([b6fff95](https://www.github.com/snakemake/snakemake-wrappers/commit/b6fff95d6c25b3536d0999ed63b9e7aecc4bc586))
* autobump bio/mashmap ([#1737](https://www.github.com/snakemake/snakemake-wrappers/issues/1737)) ([ae721ec](https://www.github.com/snakemake/snakemake-wrappers/commit/ae721ec4f0bbede932b54cb53046307506a7c659))
* autobump bio/picard/bedtointervallist ([#1734](https://www.github.com/snakemake/snakemake-wrappers/issues/1734)) ([13e5cad](https://www.github.com/snakemake/snakemake-wrappers/commit/13e5cad53b86a84291b7420b37950cc111a7a7a2))
* autobump bio/qualimap/rnaseq ([#1746](https://www.github.com/snakemake/snakemake-wrappers/issues/1746)) ([36835c5](https://www.github.com/snakemake/snakemake-wrappers/commit/36835c5cf60d488efd646fc7ff039bf7a9c7e8a9))
* autobump bio/samtools/depth ([#1738](https://www.github.com/snakemake/snakemake-wrappers/issues/1738)) ([5d0f676](https://www.github.com/snakemake/snakemake-wrappers/commit/5d0f6761d8b2b11afeafe017d0566ae74fc0b0f9))
* autobump bio/snpsift/dbnsfp ([#1749](https://www.github.com/snakemake/snakemake-wrappers/issues/1749)) ([cdfa888](https://www.github.com/snakemake/snakemake-wrappers/commit/cdfa8887ed1e3a196d9e1c7f58477212afc8d653))
* autobump bio/sra-tools/fasterq-dump ([#1732](https://www.github.com/snakemake/snakemake-wrappers/issues/1732)) ([06e7b87](https://www.github.com/snakemake/snakemake-wrappers/commit/06e7b872c6de379a2c0452836b4f0c17e7f33fda))
* autobump bio/vg/kmers ([#1752](https://www.github.com/snakemake/snakemake-wrappers/issues/1752)) ([cf84881](https://www.github.com/snakemake/snakemake-wrappers/commit/cf84881a288fb254ce0326f0864fad04c790d869))
* autobump bio/vg/merge ([#1748](https://www.github.com/snakemake/snakemake-wrappers/issues/1748)) ([78f6716](https://www.github.com/snakemake/snakemake-wrappers/commit/78f671672ddeec3905d6a80751dc5d7cb7aa500f))
* autobump utils/cairosvg ([#1733](https://www.github.com/snakemake/snakemake-wrappers/issues/1733)) ([3a48cd7](https://www.github.com/snakemake/snakemake-wrappers/commit/3a48cd719e6798b0b4041b929d8e6b7a92f83f0c))
* bump datavzrd to 2.23.2 ([#1729](https://www.github.com/snakemake/snakemake-wrappers/issues/1729)) ([55a7066](https://www.github.com/snakemake/snakemake-wrappers/commit/55a70669a000900cfd23c9bd4092f92b3eda208b))
* bump datavzrd to 2.23.3 ([#1745](https://www.github.com/snakemake/snakemake-wrappers/issues/1745)) ([dff136b](https://www.github.com/snakemake/snakemake-wrappers/commit/dff136b2da7a26e2368a96428885b12ec20c8d3b))
* bump datavzrd to 2.23.4 ([#1753](https://www.github.com/snakemake/snakemake-wrappers/issues/1753)) ([1b729e1](https://www.github.com/snakemake/snakemake-wrappers/commit/1b729e1f3ab0ab87725e12b484d993aa5627ede0))

### [2.3.2](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.3.1...v2.3.2) (2023-08-07)


### Bug Fixes

* fgbio annotatebamwithumis allow multiple umi fastq files ([#1726](https://www.github.com/snakemake/snakemake-wrappers/issues/1726)) ([101744d](https://www.github.com/snakemake/snakemake-wrappers/commit/101744d37b9b062677e26453ee243ba42a6e48f9))

### [2.3.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.3.0...v2.3.1) (2023-08-04)


### Performance Improvements

* bump datavzrd to 2.23.1 ([#1723](https://www.github.com/snakemake/snakemake-wrappers/issues/1723)) ([b0d79d8](https://www.github.com/snakemake/snakemake-wrappers/commit/b0d79d88afec45f67c6dfccff46af91f898b9a5f))

## [2.3.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.2.1...v2.3.0) (2023-08-04)


### Features

* Bowtie2 meta ([#1586](https://www.github.com/snakemake/snakemake-wrappers/issues/1586)) ([d8edd7b](https://www.github.com/snakemake/snakemake-wrappers/commit/d8edd7bb2d282f097685d593abe1d2f83b3f1120))
* enable output of unmapped reads ([#1549](https://www.github.com/snakemake/snakemake-wrappers/issues/1549)) ([bff21bc](https://www.github.com/snakemake/snakemake-wrappers/commit/bff21bc8f644806a4f49ab68e1d8b70464460e02))
* Gatk calculate contamination ([#1547](https://www.github.com/snakemake/snakemake-wrappers/issues/1547)) ([4f73135](https://www.github.com/snakemake/snakemake-wrappers/commit/4f73135020da21e5e472acc42f7b229998788010))


### Bug Fixes

* freebayes wrapper ([#1715](https://www.github.com/snakemake/snakemake-wrappers/issues/1715)) ([8656035](https://www.github.com/snakemake/snakemake-wrappers/commit/865603539bba2e516acf50a7c38186810f1da051))


### Performance Improvements

* autobump bio/bazam ([#1555](https://www.github.com/snakemake/snakemake-wrappers/issues/1555)) ([9c5d121](https://www.github.com/snakemake/snakemake-wrappers/commit/9c5d121c561e00b3963e87d6f84020043fdaea2c))
* autobump bio/bcftools/call ([#1691](https://www.github.com/snakemake/snakemake-wrappers/issues/1691)) ([c6b88eb](https://www.github.com/snakemake/snakemake-wrappers/commit/c6b88ebc62f3153f636431acca6526a2ffe972da))
* autobump bio/bcftools/call ([#1710](https://www.github.com/snakemake/snakemake-wrappers/issues/1710)) ([7430a6f](https://www.github.com/snakemake/snakemake-wrappers/commit/7430a6f765e06d7684a265d89f44145bad1e7157))
* autobump bio/bcftools/concat ([#1531](https://www.github.com/snakemake/snakemake-wrappers/issues/1531)) ([d6edd85](https://www.github.com/snakemake/snakemake-wrappers/commit/d6edd85e222310bbdd28369f92186c7e33695d63))
* autobump bio/bcftools/concat ([#1603](https://www.github.com/snakemake/snakemake-wrappers/issues/1603)) ([5b72872](https://www.github.com/snakemake/snakemake-wrappers/commit/5b72872754d8eb177f064db70dc634bd640e6944))
* autobump bio/bcftools/concat ([#1630](https://www.github.com/snakemake/snakemake-wrappers/issues/1630)) ([cd70d77](https://www.github.com/snakemake/snakemake-wrappers/commit/cd70d7729504dcf7afea4557191e335f3efeeceb))
* autobump bio/bcftools/concat ([#1661](https://www.github.com/snakemake/snakemake-wrappers/issues/1661)) ([4455dcc](https://www.github.com/snakemake/snakemake-wrappers/commit/4455dcc8af9195e4b44ffdeb053c12b93a3ea858))
* autobump bio/bcftools/concat ([#1692](https://www.github.com/snakemake/snakemake-wrappers/issues/1692)) ([a7ece62](https://www.github.com/snakemake/snakemake-wrappers/commit/a7ece6239b043bf8583ac568427442d3021b68b4))
* autobump bio/bcftools/filter ([#1609](https://www.github.com/snakemake/snakemake-wrappers/issues/1609)) ([30d5d64](https://www.github.com/snakemake/snakemake-wrappers/commit/30d5d64904b956e2769b6e804e0972cfc0b4a60b))
* autobump bio/bcftools/filter ([#1637](https://www.github.com/snakemake/snakemake-wrappers/issues/1637)) ([772a77b](https://www.github.com/snakemake/snakemake-wrappers/commit/772a77baa7073666d2ddc09a377768acb3ca8d59))
* autobump bio/bcftools/filter ([#1676](https://www.github.com/snakemake/snakemake-wrappers/issues/1676)) ([1e69c25](https://www.github.com/snakemake/snakemake-wrappers/commit/1e69c25c5e7f27083bdd3c31569c3c5e57739071))
* autobump bio/bcftools/filter ([#1703](https://www.github.com/snakemake/snakemake-wrappers/issues/1703)) ([c5224a5](https://www.github.com/snakemake/snakemake-wrappers/commit/c5224a5b7adc3245dd48783550a9da505a2cf577))
* autobump bio/bcftools/index ([#1537](https://www.github.com/snakemake/snakemake-wrappers/issues/1537)) ([d403067](https://www.github.com/snakemake/snakemake-wrappers/commit/d4030670e039333b146989bff0437155e6e00944))
* autobump bio/bcftools/index ([#1602](https://www.github.com/snakemake/snakemake-wrappers/issues/1602)) ([45e0d82](https://www.github.com/snakemake/snakemake-wrappers/commit/45e0d827bdc05bcb2b508fa1be3252b747badfb1))
* autobump bio/bcftools/merge ([#1558](https://www.github.com/snakemake/snakemake-wrappers/issues/1558)) ([18ec70f](https://www.github.com/snakemake/snakemake-wrappers/commit/18ec70f9a8c7d47cdfd0b85aa52ba03879ffa5b9))
* autobump bio/bcftools/mpileup ([#1620](https://www.github.com/snakemake/snakemake-wrappers/issues/1620)) ([6bc5006](https://www.github.com/snakemake/snakemake-wrappers/commit/6bc50063bcb60d6cf0d84221c72d4cc5fae174f0))
* autobump bio/bcftools/mpileup ([#1683](https://www.github.com/snakemake/snakemake-wrappers/issues/1683)) ([dc033c5](https://www.github.com/snakemake/snakemake-wrappers/commit/dc033c50f08819c8a63090f5663fa1c829dced79))
* autobump bio/bcftools/norm ([#1680](https://www.github.com/snakemake/snakemake-wrappers/issues/1680)) ([0f32280](https://www.github.com/snakemake/snakemake-wrappers/commit/0f32280c4f6725564dee2bb784badca4bae39823))
* autobump bio/bcftools/norm ([#1706](https://www.github.com/snakemake/snakemake-wrappers/issues/1706)) ([6822f7a](https://www.github.com/snakemake/snakemake-wrappers/commit/6822f7a8e28edda64b3771c1f4d46687f64b8691))
* autobump bio/bcftools/reheader ([#1595](https://www.github.com/snakemake/snakemake-wrappers/issues/1595)) ([83455a3](https://www.github.com/snakemake/snakemake-wrappers/commit/83455a397f24bedbe811939cf012f1088fa758cd))
* autobump bio/bcftools/reheader ([#1638](https://www.github.com/snakemake/snakemake-wrappers/issues/1638)) ([6c63212](https://www.github.com/snakemake/snakemake-wrappers/commit/6c63212e503cbdfa43250616ee0359116709f017))
* autobump bio/bcftools/sort ([#1575](https://www.github.com/snakemake/snakemake-wrappers/issues/1575)) ([92b11ed](https://www.github.com/snakemake/snakemake-wrappers/commit/92b11ed004513e7118c0d2e0bd0f58cc65b251f7))
* autobump bio/bcftools/view ([#1618](https://www.github.com/snakemake/snakemake-wrappers/issues/1618)) ([e7c3390](https://www.github.com/snakemake/snakemake-wrappers/commit/e7c3390069dfcdf4da61199aa9d2d26569d94720))
* autobump bio/bcftools/view ([#1631](https://www.github.com/snakemake/snakemake-wrappers/issues/1631)) ([0756847](https://www.github.com/snakemake/snakemake-wrappers/commit/0756847ed1e837192d5310fbbca89305d4617295))
* autobump bio/bellerophon ([#1614](https://www.github.com/snakemake/snakemake-wrappers/issues/1614)) ([d9c9b0b](https://www.github.com/snakemake/snakemake-wrappers/commit/d9c9b0bda61505b66413b10590787d72ec39eab4))
* autobump bio/bellerophon ([#1646](https://www.github.com/snakemake/snakemake-wrappers/issues/1646)) ([5c47391](https://www.github.com/snakemake/snakemake-wrappers/commit/5c473918eb84a7b3bc6d4fbbb7d4587b12b0c38f))
* autobump bio/bgzip ([#1652](https://www.github.com/snakemake/snakemake-wrappers/issues/1652)) ([3cc38ac](https://www.github.com/snakemake/snakemake-wrappers/commit/3cc38acaa6374a4425d8cac3fc5b72c6c3126747))
* autobump bio/bismark/bismark2report ([#1714](https://www.github.com/snakemake/snakemake-wrappers/issues/1714)) ([6d95e56](https://www.github.com/snakemake/snakemake-wrappers/commit/6d95e56da2e2ed09133cb20ea2608f94d1483228))
* autobump bio/bismark/bismark2summary ([#1594](https://www.github.com/snakemake/snakemake-wrappers/issues/1594)) ([c7a0448](https://www.github.com/snakemake/snakemake-wrappers/commit/c7a044874f51c6231c8551b1e5b36d7302732385))
* autobump bio/bismark/bismark2summary ([#1679](https://www.github.com/snakemake/snakemake-wrappers/issues/1679)) ([135dabc](https://www.github.com/snakemake/snakemake-wrappers/commit/135dabc0f7b5f349cf43468be5899054e8f1d478))
* autobump bio/bismark/bismark2summary ([#1687](https://www.github.com/snakemake/snakemake-wrappers/issues/1687)) ([3cf315a](https://www.github.com/snakemake/snakemake-wrappers/commit/3cf315a96c213e92ef8ba6712b259d60840913d0))
* autobump bio/bowtie2/align ([#1634](https://www.github.com/snakemake/snakemake-wrappers/issues/1634)) ([477d1ab](https://www.github.com/snakemake/snakemake-wrappers/commit/477d1ab674e32642b0d46885964889230371193e))
* autobump bio/bustools/sort ([#1688](https://www.github.com/snakemake/snakemake-wrappers/issues/1688)) ([7d37969](https://www.github.com/snakemake/snakemake-wrappers/commit/7d3796958009213f62637e073b801974d82aab52))
* autobump bio/bustools/text ([#1523](https://www.github.com/snakemake/snakemake-wrappers/issues/1523)) ([08f0e0a](https://www.github.com/snakemake/snakemake-wrappers/commit/08f0e0a0b4033fff6aa1d30b0e0d315ae5f3086a))
* autobump bio/bwa-mem2/mem ([#1669](https://www.github.com/snakemake/snakemake-wrappers/issues/1669)) ([92ba532](https://www.github.com/snakemake/snakemake-wrappers/commit/92ba53269f589f156b8827d6188956fdad70c678))
* autobump bio/bwa/mem ([#1656](https://www.github.com/snakemake/snakemake-wrappers/issues/1656)) ([03224f2](https://www.github.com/snakemake/snakemake-wrappers/commit/03224f2c01a67f0df2efef4162b6f0b9c8b7aa41))
* autobump bio/dada2/add-species ([#1522](https://www.github.com/snakemake/snakemake-wrappers/issues/1522)) ([2f2ccc6](https://www.github.com/snakemake/snakemake-wrappers/commit/2f2ccc6b67dd1edd17eca576791f8be38bbaa675))
* autobump bio/dada2/assign-species ([#1563](https://www.github.com/snakemake/snakemake-wrappers/issues/1563)) ([adf781e](https://www.github.com/snakemake/snakemake-wrappers/commit/adf781e04c33988518b194aa322ac861ee0ebe06))
* autobump bio/dada2/assign-taxonomy ([#1551](https://www.github.com/snakemake/snakemake-wrappers/issues/1551)) ([31c3b9a](https://www.github.com/snakemake/snakemake-wrappers/commit/31c3b9a9e146de3a4337108f15702e8c175f457b))
* autobump bio/dada2/collapse-nomismatch ([#1554](https://www.github.com/snakemake/snakemake-wrappers/issues/1554)) ([db5b2ea](https://www.github.com/snakemake/snakemake-wrappers/commit/db5b2ea65ea7e811b54eb7e574a72d8cd257aa61))
* autobump bio/dada2/dereplicate-fastq ([#1671](https://www.github.com/snakemake/snakemake-wrappers/issues/1671)) ([2386b66](https://www.github.com/snakemake/snakemake-wrappers/commit/2386b66863189046d1df76bb5d16d9c8f9263110))
* autobump bio/dada2/filter-trim ([#1641](https://www.github.com/snakemake/snakemake-wrappers/issues/1641)) ([c58bcfb](https://www.github.com/snakemake/snakemake-wrappers/commit/c58bcfb860af2598f83d06d81156ea52eb15988c))
* autobump bio/dada2/learn-errors ([#1574](https://www.github.com/snakemake/snakemake-wrappers/issues/1574)) ([da832b1](https://www.github.com/snakemake/snakemake-wrappers/commit/da832b10177fd96b57b7475ee16c1fa39d86f5ba))
* autobump bio/dada2/make-table ([#1678](https://www.github.com/snakemake/snakemake-wrappers/issues/1678)) ([a235b2f](https://www.github.com/snakemake/snakemake-wrappers/commit/a235b2f33a35de1ce4e807a0cdb5d14d4afc1330))
* autobump bio/dada2/merge-pairs ([#1588](https://www.github.com/snakemake/snakemake-wrappers/issues/1588)) ([17d69a0](https://www.github.com/snakemake/snakemake-wrappers/commit/17d69a05c188d5072542db1876255f63dbb7368b))
* autobump bio/dada2/merge-pairs ([#1689](https://www.github.com/snakemake/snakemake-wrappers/issues/1689)) ([ef65a5f](https://www.github.com/snakemake/snakemake-wrappers/commit/ef65a5f39e403c2e2d8e1d61206d9854fcfa60c4))
* autobump bio/dada2/merge-pairs ([#1712](https://www.github.com/snakemake/snakemake-wrappers/issues/1712)) ([bc6d079](https://www.github.com/snakemake/snakemake-wrappers/commit/bc6d0798881a572d73876475ec989d7ddb4b532d))
* autobump bio/dada2/quality-profile ([#1534](https://www.github.com/snakemake/snakemake-wrappers/issues/1534)) ([05d12b3](https://www.github.com/snakemake/snakemake-wrappers/commit/05d12b309df632f6d45683b63843cd300333fde5))
* autobump bio/dada2/remove-chimeras ([#1541](https://www.github.com/snakemake/snakemake-wrappers/issues/1541)) ([7282994](https://www.github.com/snakemake/snakemake-wrappers/commit/7282994399a03f3f693b7efcc0935f2c2a71739c))
* autobump bio/dada2/sample-inference ([#1702](https://www.github.com/snakemake/snakemake-wrappers/issues/1702)) ([a82d8fc](https://www.github.com/snakemake/snakemake-wrappers/commit/a82d8fc9da618ae57572a2e8d5899c1ea767dde6))
* autobump bio/deeptools/alignmentsieve ([#1635](https://www.github.com/snakemake/snakemake-wrappers/issues/1635)) ([b01bb82](https://www.github.com/snakemake/snakemake-wrappers/commit/b01bb82378638f404a77959c9e2725c81480f0ec))
* autobump bio/deeptools/plotheatmap ([#1561](https://www.github.com/snakemake/snakemake-wrappers/issues/1561)) ([faf49e2](https://www.github.com/snakemake/snakemake-wrappers/commit/faf49e20a7e19592bde11835206b2427b9104c87))
* autobump bio/deseq2/deseqdataset ([#1633](https://www.github.com/snakemake/snakemake-wrappers/issues/1633)) ([176be53](https://www.github.com/snakemake/snakemake-wrappers/commit/176be53f11bde39e27bea97977eeedf72fdbd2fb))
* autobump bio/diamond/blastp ([#1570](https://www.github.com/snakemake/snakemake-wrappers/issues/1570)) ([3f61c8f](https://www.github.com/snakemake/snakemake-wrappers/commit/3f61c8fdb7c309ecc6655ff138467055313808e2))
* autobump bio/diamond/blastx ([#1670](https://www.github.com/snakemake/snakemake-wrappers/issues/1670)) ([0eaf267](https://www.github.com/snakemake/snakemake-wrappers/commit/0eaf267181dce43233e7708101593ee3805917c2))
* autobump bio/diamond/makedb ([#1711](https://www.github.com/snakemake/snakemake-wrappers/issues/1711)) ([e4bc2e4](https://www.github.com/snakemake/snakemake-wrappers/commit/e4bc2e4a2482a579e72821152d7964f8a57df99c))
* autobump bio/fastqc ([#1540](https://www.github.com/snakemake/snakemake-wrappers/issues/1540)) ([1e0d23e](https://www.github.com/snakemake/snakemake-wrappers/commit/1e0d23e8264738a256bc7059c73533befdc56e3f))
* autobump bio/fgbio/annotatebamwithumis ([#1572](https://www.github.com/snakemake/snakemake-wrappers/issues/1572)) ([47e4c62](https://www.github.com/snakemake/snakemake-wrappers/commit/47e4c6284b11f6aab4aae962a2d32df9a6c13b26))
* autobump bio/fgbio/collectduplexseqmetrics ([#1648](https://www.github.com/snakemake/snakemake-wrappers/issues/1648)) ([e8fd7f0](https://www.github.com/snakemake/snakemake-wrappers/commit/e8fd7f0cf0f21384738998af7ea3114ac3f5374f))
* autobump bio/gatk/applybqsr ([#1589](https://www.github.com/snakemake/snakemake-wrappers/issues/1589)) ([5ebf186](https://www.github.com/snakemake/snakemake-wrappers/commit/5ebf1868c5e30ed4b327e37bbff5cc4766abd49b))
* autobump bio/gatk/applybqsrspark ([#1578](https://www.github.com/snakemake/snakemake-wrappers/issues/1578)) ([007a4d1](https://www.github.com/snakemake/snakemake-wrappers/commit/007a4d11c21f5f3bb391b9d4288e549b3a7185ac))
* autobump bio/gatk/applyvqsr ([#1544](https://www.github.com/snakemake/snakemake-wrappers/issues/1544)) ([0c45d39](https://www.github.com/snakemake/snakemake-wrappers/commit/0c45d3911700546cd743c099a521cd011d0c28a2))
* autobump bio/gatk/baserecalibrator ([#1535](https://www.github.com/snakemake/snakemake-wrappers/issues/1535)) ([0d006e0](https://www.github.com/snakemake/snakemake-wrappers/commit/0d006e09645897807a24cd6af5963fc5155dc03a))
* autobump bio/gatk/baserecalibrator ([#1581](https://www.github.com/snakemake/snakemake-wrappers/issues/1581)) ([153b20b](https://www.github.com/snakemake/snakemake-wrappers/commit/153b20bcfdad658be7959f1b95b6bfb0aa03e3a9))
* autobump bio/gatk/baserecalibratorspark ([#1600](https://www.github.com/snakemake/snakemake-wrappers/issues/1600)) ([2d5a263](https://www.github.com/snakemake/snakemake-wrappers/commit/2d5a263bfec71b8d8ca07e7a558453c6f0ef11a3))
* autobump bio/gatk/baserecalibratorspark ([#1649](https://www.github.com/snakemake/snakemake-wrappers/issues/1649)) ([207026c](https://www.github.com/snakemake/snakemake-wrappers/commit/207026c9caa39af09e62f300811bf311a886e9a7))
* autobump bio/gatk/callcopyratiosegments ([#1527](https://www.github.com/snakemake/snakemake-wrappers/issues/1527)) ([5a4741a](https://www.github.com/snakemake/snakemake-wrappers/commit/5a4741acd39642095459cdbaec7b749fb8354ae8))
* autobump bio/gatk/callcopyratiosegments ([#1557](https://www.github.com/snakemake/snakemake-wrappers/issues/1557)) ([4c788df](https://www.github.com/snakemake/snakemake-wrappers/commit/4c788df8f68823bdff87d00a81df6b8541e49213))
* autobump bio/gatk/cleansam ([#1599](https://www.github.com/snakemake/snakemake-wrappers/issues/1599)) ([a58bbfe](https://www.github.com/snakemake/snakemake-wrappers/commit/a58bbfe6d15e005bad9cde29da3d780c1c90a601))
* autobump bio/gatk/cleansam ([#1659](https://www.github.com/snakemake/snakemake-wrappers/issues/1659)) ([299198f](https://www.github.com/snakemake/snakemake-wrappers/commit/299198fab4635546351653d0fbe5e5e39873f1c2))
* autobump bio/gatk/collectalleliccounts ([#1719](https://www.github.com/snakemake/snakemake-wrappers/issues/1719)) ([bf74f2f](https://www.github.com/snakemake/snakemake-wrappers/commit/bf74f2f922a2164c3cf6315c2fc2a9d4d505c3d9))
* autobump bio/gatk/collectreadcounts ([#1684](https://www.github.com/snakemake/snakemake-wrappers/issues/1684)) ([dae6459](https://www.github.com/snakemake/snakemake-wrappers/commit/dae64590862e492df1ba7e53cce41e9557688ee5))
* autobump bio/gatk/denoisereadcounts ([#1704](https://www.github.com/snakemake/snakemake-wrappers/issues/1704)) ([c398633](https://www.github.com/snakemake/snakemake-wrappers/commit/c39863369932331f70c5cc0175a0a903b41c6181))
* autobump bio/gatk/depthofcoverage ([#1601](https://www.github.com/snakemake/snakemake-wrappers/issues/1601)) ([45248d4](https://www.github.com/snakemake/snakemake-wrappers/commit/45248d45a0684f08a0697129b146f601822283b6))
* autobump bio/gatk/depthofcoverage ([#1667](https://www.github.com/snakemake/snakemake-wrappers/issues/1667)) ([7ffe876](https://www.github.com/snakemake/snakemake-wrappers/commit/7ffe876823b1b02e9c96821f60671d6b3a506d0c))
* autobump bio/gatk/filtermutectcalls ([#1668](https://www.github.com/snakemake/snakemake-wrappers/issues/1668)) ([8924792](https://www.github.com/snakemake/snakemake-wrappers/commit/89247926b6cd852161abe9765f3e66bb96c73a6d))
* autobump bio/gatk/filtermutectcalls ([#1713](https://www.github.com/snakemake/snakemake-wrappers/issues/1713)) ([30c7e9b](https://www.github.com/snakemake/snakemake-wrappers/commit/30c7e9bbcf3cea2188bca967c4a358f69cbfe8bf))
* autobump bio/gatk/genomicsdbimport ([#1722](https://www.github.com/snakemake/snakemake-wrappers/issues/1722)) ([eef7b43](https://www.github.com/snakemake/snakemake-wrappers/commit/eef7b43efdfbd0a92e7cc3ef423cd774ef0ab171))
* autobump bio/gatk/genotypegvcfs ([#1560](https://www.github.com/snakemake/snakemake-wrappers/issues/1560)) ([b64e056](https://www.github.com/snakemake/snakemake-wrappers/commit/b64e056c8eca0d12159bb73d225dc61eae3bef5d))
* autobump bio/gatk/haplotypecaller ([#1705](https://www.github.com/snakemake/snakemake-wrappers/issues/1705)) ([ec9815e](https://www.github.com/snakemake/snakemake-wrappers/commit/ec9815eaf4ecc8e0b4b85db2bd0940961b0548b6))
* autobump bio/gatk/intervallisttobed ([#1622](https://www.github.com/snakemake/snakemake-wrappers/issues/1622)) ([3d5215d](https://www.github.com/snakemake/snakemake-wrappers/commit/3d5215dd5d0da5a22c93f28374a5d36919ff97a6))
* autobump bio/gatk/intervallisttobed ([#1647](https://www.github.com/snakemake/snakemake-wrappers/issues/1647)) ([e4c13a2](https://www.github.com/snakemake/snakemake-wrappers/commit/e4c13a2cd9b9b8ecf9314e1bc6ee5b59875339c0))
* autobump bio/gatk/intervallisttobed ([#1663](https://www.github.com/snakemake/snakemake-wrappers/issues/1663)) ([9654834](https://www.github.com/snakemake/snakemake-wrappers/commit/9654834c9c5f9827e9a27687a3ce17034a2ce8b2))
* autobump bio/gatk/intervallisttobed ([#1693](https://www.github.com/snakemake/snakemake-wrappers/issues/1693)) ([8acf652](https://www.github.com/snakemake/snakemake-wrappers/commit/8acf6520e7ec204e0a4e663834632d8d1efc6a89))
* autobump bio/gatk/learnreadorientationmodel ([#1625](https://www.github.com/snakemake/snakemake-wrappers/issues/1625)) ([bd0fa42](https://www.github.com/snakemake/snakemake-wrappers/commit/bd0fa42705393cb1408a84ce4a060272d5428ce6))
* autobump bio/gatk/learnreadorientationmodel ([#1653](https://www.github.com/snakemake/snakemake-wrappers/issues/1653)) ([c2c64ea](https://www.github.com/snakemake/snakemake-wrappers/commit/c2c64ea596f00ccb67b27aa38c94c9a5376e172d))
* autobump bio/gatk/leftalignandtrimvariants ([#1639](https://www.github.com/snakemake/snakemake-wrappers/issues/1639)) ([c3f89ea](https://www.github.com/snakemake/snakemake-wrappers/commit/c3f89ea03d5bd6438d4af260c1c1c6f906a95926))
* autobump bio/gatk/leftalignandtrimvariants ([#1697](https://www.github.com/snakemake/snakemake-wrappers/issues/1697)) ([c4b738a](https://www.github.com/snakemake/snakemake-wrappers/commit/c4b738a40d21b0f14dd52b9e112ec88233b9f71b))
* autobump bio/gatk/markduplicatesspark ([#1467](https://www.github.com/snakemake/snakemake-wrappers/issues/1467)) ([1d383b7](https://www.github.com/snakemake/snakemake-wrappers/commit/1d383b71d42a13ba2df6a9404bb7d10ecbcc4b6b))
* autobump bio/gatk/modelsegments ([#1543](https://www.github.com/snakemake/snakemake-wrappers/issues/1543)) ([f26ea4a](https://www.github.com/snakemake/snakemake-wrappers/commit/f26ea4a8d1090467d3b5c2785cde878b2b58ba82))
* autobump bio/gatk/modelsegments ([#1611](https://www.github.com/snakemake/snakemake-wrappers/issues/1611)) ([77ff014](https://www.github.com/snakemake/snakemake-wrappers/commit/77ff01495e7dc8df19b11d6acbff6ae1e98ab474))
* autobump bio/gatk/mutect ([#1526](https://www.github.com/snakemake/snakemake-wrappers/issues/1526)) ([4789991](https://www.github.com/snakemake/snakemake-wrappers/commit/4789991a17450c2c36681ceeeb53d265fadf6b5f))
* autobump bio/gatk/mutect ([#1696](https://www.github.com/snakemake/snakemake-wrappers/issues/1696)) ([666ba69](https://www.github.com/snakemake/snakemake-wrappers/commit/666ba698538fab13afbb9b52a01e1abc8343f76a))
* autobump bio/gatk/printreadsspark ([#1699](https://www.github.com/snakemake/snakemake-wrappers/issues/1699)) ([1aee674](https://www.github.com/snakemake/snakemake-wrappers/commit/1aee674a645953d056548fd38dad966606b7d185))
* autobump bio/gatk/scatterintervalsbyns ([#1597](https://www.github.com/snakemake/snakemake-wrappers/issues/1597)) ([214c231](https://www.github.com/snakemake/snakemake-wrappers/commit/214c2316448fff942c7824f14cf754212d71c554))
* autobump bio/gatk/scatterintervalsbyns ([#1682](https://www.github.com/snakemake/snakemake-wrappers/issues/1682)) ([42e0238](https://www.github.com/snakemake/snakemake-wrappers/commit/42e0238a57d4acf8ec76eba77f8197ddc7e154db))
* autobump bio/gatk/selectvariants ([#1695](https://www.github.com/snakemake/snakemake-wrappers/issues/1695)) ([fb5b42d](https://www.github.com/snakemake/snakemake-wrappers/commit/fb5b42d01674337805b741a2e64c340204f09f19))
* autobump bio/gatk/splitintervals ([#1591](https://www.github.com/snakemake/snakemake-wrappers/issues/1591)) ([67ccba6](https://www.github.com/snakemake/snakemake-wrappers/commit/67ccba699188b4c02dd0bf2cb1f2557fcf5a544c))
* autobump bio/gatk/splitncigarreads ([#1536](https://www.github.com/snakemake/snakemake-wrappers/issues/1536)) ([68b02fe](https://www.github.com/snakemake/snakemake-wrappers/commit/68b02fe81e886721ac457895823491a4eaf21c9d))
* autobump bio/gatk/splitncigarreads ([#1562](https://www.github.com/snakemake/snakemake-wrappers/issues/1562)) ([c27f4a6](https://www.github.com/snakemake/snakemake-wrappers/commit/c27f4a6a224de88d1bb6855af5643c84e485385e))
* autobump bio/gatk/variantannotator ([#1582](https://www.github.com/snakemake/snakemake-wrappers/issues/1582)) ([2b41efe](https://www.github.com/snakemake/snakemake-wrappers/commit/2b41efeea999b2408cd58afb21eb9fa04cff7e42))
* autobump bio/gatk/varianteval ([#1545](https://www.github.com/snakemake/snakemake-wrappers/issues/1545)) ([1b70868](https://www.github.com/snakemake/snakemake-wrappers/commit/1b708687cbf5235cda3ba23c3ccaed1075394f88))
* autobump bio/gatk/varianteval ([#1619](https://www.github.com/snakemake/snakemake-wrappers/issues/1619)) ([78c57d1](https://www.github.com/snakemake/snakemake-wrappers/commit/78c57d16fccb06acb46c36707cae8beb43b8e68f))
* autobump bio/gatk/varianteval ([#1677](https://www.github.com/snakemake/snakemake-wrappers/issues/1677)) ([29eb05c](https://www.github.com/snakemake/snakemake-wrappers/commit/29eb05c8736207cd37ce620d9b43863e5f4ae3a2))
* autobump bio/gatk/variantfiltration ([#1577](https://www.github.com/snakemake/snakemake-wrappers/issues/1577)) ([0dabdf1](https://www.github.com/snakemake/snakemake-wrappers/commit/0dabdf194ead2950b1c2122cf304541f3da83e96))
* autobump bio/gatk/variantstotable ([#1539](https://www.github.com/snakemake/snakemake-wrappers/issues/1539)) ([00d5abd](https://www.github.com/snakemake/snakemake-wrappers/commit/00d5abd3d567688fb380da00358ad148f76b4f6b))
* autobump bio/gatk/variantstotable ([#1559](https://www.github.com/snakemake/snakemake-wrappers/issues/1559)) ([eba4873](https://www.github.com/snakemake/snakemake-wrappers/commit/eba48737c41efad2b63f77fa9f37c9ee3e308ed9))
* autobump bio/gatk3/baserecalibrator ([#1642](https://www.github.com/snakemake/snakemake-wrappers/issues/1642)) ([782593d](https://www.github.com/snakemake/snakemake-wrappers/commit/782593d339d4d51a59d52048e53d7af5929b23c7))
* autobump bio/gatk3/indelrealigner ([#1636](https://www.github.com/snakemake/snakemake-wrappers/issues/1636)) ([ab6be44](https://www.github.com/snakemake/snakemake-wrappers/commit/ab6be44365616650342ad7650075fc052bb2a609))
* autobump bio/gatk3/realignertargetcreator ([#1587](https://www.github.com/snakemake/snakemake-wrappers/issues/1587)) ([1e320ac](https://www.github.com/snakemake/snakemake-wrappers/commit/1e320acb33840a6e875b908bc4cd93d3910707f4))
* autobump bio/gatk3/realignertargetcreator ([#1650](https://www.github.com/snakemake/snakemake-wrappers/issues/1650)) ([66bfa88](https://www.github.com/snakemake/snakemake-wrappers/commit/66bfa88b02b68d6d853d934c6ff596be3d01f149))
* autobump bio/gdc-api/bam-slicing ([#1552](https://www.github.com/snakemake/snakemake-wrappers/issues/1552)) ([9760140](https://www.github.com/snakemake/snakemake-wrappers/commit/9760140b9a0c058c44c23ba95b3ef59d15e35473))
* autobump bio/gdc-api/bam-slicing ([#1627](https://www.github.com/snakemake/snakemake-wrappers/issues/1627)) ([14ff838](https://www.github.com/snakemake/snakemake-wrappers/commit/14ff8382dfbb04ffcff2e1a287317b45e93789b0))
* autobump bio/genomepy ([#1542](https://www.github.com/snakemake/snakemake-wrappers/issues/1542)) ([f615808](https://www.github.com/snakemake/snakemake-wrappers/commit/f6158084badc5b42a1eae0f71b66c45568e01cf3))
* autobump bio/hifiasm ([#1672](https://www.github.com/snakemake/snakemake-wrappers/issues/1672)) ([7ad6d77](https://www.github.com/snakemake/snakemake-wrappers/commit/7ad6d7797895488cc792c1ddfbaedabcf68e6b3f))
* autobump bio/hifiasm ([#1694](https://www.github.com/snakemake/snakemake-wrappers/issues/1694)) ([a99f0ef](https://www.github.com/snakemake/snakemake-wrappers/commit/a99f0ef10d75e69092973f6e152a4ab4fe2d2630))
* autobump bio/jannovar ([#1640](https://www.github.com/snakemake/snakemake-wrappers/issues/1640)) ([cf6d9d4](https://www.github.com/snakemake/snakemake-wrappers/commit/cf6d9d416bd170ee170a878ce3b33eaf64eacfc5))
* autobump bio/kallisto/index ([#1708](https://www.github.com/snakemake/snakemake-wrappers/issues/1708)) ([a84c0ab](https://www.github.com/snakemake/snakemake-wrappers/commit/a84c0ab498df5916c7017879394bb183e05ed450))
* autobump bio/kallisto/quant ([#1629](https://www.github.com/snakemake/snakemake-wrappers/issues/1629)) ([d076334](https://www.github.com/snakemake/snakemake-wrappers/commit/d076334515e77aa6efb7fa1f415fd7f8b9433a8c))
* autobump bio/last/lastal ([#1666](https://www.github.com/snakemake/snakemake-wrappers/issues/1666)) ([1aababe](https://www.github.com/snakemake/snakemake-wrappers/commit/1aababe757430337259293564e202190ad5eedd3))
* autobump bio/last/lastal ([#1709](https://www.github.com/snakemake/snakemake-wrappers/issues/1709)) ([fa7a100](https://www.github.com/snakemake/snakemake-wrappers/commit/fa7a10041c5276314a254d671a304f6c8851a0db))
* autobump bio/macs2/callpeak ([#1662](https://www.github.com/snakemake/snakemake-wrappers/issues/1662)) ([e175ce2](https://www.github.com/snakemake/snakemake-wrappers/commit/e175ce27e13b190e0bb27b37ab8f51cc06ed41d3))
* autobump bio/mashmap ([#1474](https://www.github.com/snakemake/snakemake-wrappers/issues/1474)) ([bf67fcd](https://www.github.com/snakemake/snakemake-wrappers/commit/bf67fcd92ae83269007e656664c7fa8be6b757f0))
* autobump bio/minimap2/aligner ([#1592](https://www.github.com/snakemake/snakemake-wrappers/issues/1592)) ([c2c611c](https://www.github.com/snakemake/snakemake-wrappers/commit/c2c611ca968f3bb03e69f4cfca40636c0a278a6c))
* autobump bio/mosdepth ([#1720](https://www.github.com/snakemake/snakemake-wrappers/issues/1720)) ([828f780](https://www.github.com/snakemake/snakemake-wrappers/commit/828f780d44b40f89de3ff278ff9d64fc6455eb1e))
* autobump bio/nonpareil/infer ([#1606](https://www.github.com/snakemake/snakemake-wrappers/issues/1606)) ([a19604d](https://www.github.com/snakemake/snakemake-wrappers/commit/a19604d729dc45c2d7b124512dc5219ef44ec261))
* autobump bio/nonpareil/infer ([#1681](https://www.github.com/snakemake/snakemake-wrappers/issues/1681)) ([e81c291](https://www.github.com/snakemake/snakemake-wrappers/commit/e81c291494d7eabc0e8384dc83831f614cca2439))
* autobump bio/nonpareil/infer ([#1701](https://www.github.com/snakemake/snakemake-wrappers/issues/1701)) ([0fa0b21](https://www.github.com/snakemake/snakemake-wrappers/commit/0fa0b2120ae4f7300eb94a2cbbf88c63fd970abf))
* autobump bio/open-cravat/module ([#1664](https://www.github.com/snakemake/snakemake-wrappers/issues/1664)) ([58047f7](https://www.github.com/snakemake/snakemake-wrappers/commit/58047f710ae8ea7e76e701c3f27f05b3b5c256d0))
* autobump bio/open-cravat/run ([#1596](https://www.github.com/snakemake/snakemake-wrappers/issues/1596)) ([acdb91e](https://www.github.com/snakemake/snakemake-wrappers/commit/acdb91ec328d5d8f27be985409fc769a1d0e45ad))
* autobump bio/pbmm2/align ([#1553](https://www.github.com/snakemake/snakemake-wrappers/issues/1553)) ([03be953](https://www.github.com/snakemake/snakemake-wrappers/commit/03be95318516cecd6b69424e245200bd8280acfb))
* autobump bio/picard/addorreplacereadgroups ([#1571](https://www.github.com/snakemake/snakemake-wrappers/issues/1571)) ([a68069e](https://www.github.com/snakemake/snakemake-wrappers/commit/a68069ed69bf618385e36f2eb4d1decc55b93115))
* autobump bio/picard/collectalignmentsummarymetrics ([#1716](https://www.github.com/snakemake/snakemake-wrappers/issues/1716)) ([f10e617](https://www.github.com/snakemake/snakemake-wrappers/commit/f10e617b8d5706a7913abb8ccb04e2d38531026d))
* autobump bio/picard/collectgcbiasmetrics ([#1660](https://www.github.com/snakemake/snakemake-wrappers/issues/1660)) ([aa83b56](https://www.github.com/snakemake/snakemake-wrappers/commit/aa83b567dc9f37254f00e802dea60551c2f9bac3))
* autobump bio/picard/collecthsmetrics ([#1565](https://www.github.com/snakemake/snakemake-wrappers/issues/1565)) ([58ebb45](https://www.github.com/snakemake/snakemake-wrappers/commit/58ebb45b750782fc968535475b96755b366c712d))
* autobump bio/picard/collectinsertsizemetrics ([#1616](https://www.github.com/snakemake/snakemake-wrappers/issues/1616)) ([83bbae5](https://www.github.com/snakemake/snakemake-wrappers/commit/83bbae58963ae7d7affa6864bbd0c3aa390f3274))
* autobump bio/picard/collectmultiplemetrics ([#1533](https://www.github.com/snakemake/snakemake-wrappers/issues/1533)) ([6163ba6](https://www.github.com/snakemake/snakemake-wrappers/commit/6163ba6c78980e85111a107e4a066659933557cf))
* autobump bio/picard/collectmultiplemetrics ([#1579](https://www.github.com/snakemake/snakemake-wrappers/issues/1579)) ([0009a9b](https://www.github.com/snakemake/snakemake-wrappers/commit/0009a9bddd279f9ad214ca59d93d8b39006fc850))
* autobump bio/picard/collectrnaseqmetrics ([#1567](https://www.github.com/snakemake/snakemake-wrappers/issues/1567)) ([8d6a569](https://www.github.com/snakemake/snakemake-wrappers/commit/8d6a5694ed861ab9edb00ee135767102174e8cd7))
* autobump bio/picard/collecttargetedpcrmetrics ([#1584](https://www.github.com/snakemake/snakemake-wrappers/issues/1584)) ([60c1626](https://www.github.com/snakemake/snakemake-wrappers/commit/60c1626eee96437f9b775f9de2cd5d15a9805923))
* autobump bio/picard/createsequencedictionary ([#1643](https://www.github.com/snakemake/snakemake-wrappers/issues/1643)) ([ddb979d](https://www.github.com/snakemake/snakemake-wrappers/commit/ddb979d72f7720ee554ad44d05d66957aad2b275))
* autobump bio/picard/mergesamfiles ([#1690](https://www.github.com/snakemake/snakemake-wrappers/issues/1690)) ([cf90f0d](https://www.github.com/snakemake/snakemake-wrappers/commit/cf90f0d07c802d7071724acfc4667fb80a7b28f8))
* autobump bio/picard/mergevcfs ([#1718](https://www.github.com/snakemake/snakemake-wrappers/issues/1718)) ([4681800](https://www.github.com/snakemake/snakemake-wrappers/commit/46818001763bea35a99e34d5d76cdb8a5c63995d))
* autobump bio/picard/revertsam ([#1580](https://www.github.com/snakemake/snakemake-wrappers/issues/1580)) ([8c9aa09](https://www.github.com/snakemake/snakemake-wrappers/commit/8c9aa090857328b1c53d41c29d817fd2e30fd3ba))
* autobump bio/picard/samtofastq ([#1569](https://www.github.com/snakemake/snakemake-wrappers/issues/1569)) ([9157dea](https://www.github.com/snakemake/snakemake-wrappers/commit/9157deaa1f89de327d4efbd797bf1173dbd9ec69))
* autobump bio/picard/sortsam ([#1530](https://www.github.com/snakemake/snakemake-wrappers/issues/1530)) ([075a64f](https://www.github.com/snakemake/snakemake-wrappers/commit/075a64fcccb9cc8ed9202fb081c96b35afd19c99))
* autobump bio/pretext/map ([#1721](https://www.github.com/snakemake/snakemake-wrappers/issues/1721)) ([b13f290](https://www.github.com/snakemake/snakemake-wrappers/commit/b13f290058329c7cbc5dbe2ca3f32271c802adb2))
* autobump bio/pyroe/makesplicedintronic ([#1564](https://www.github.com/snakemake/snakemake-wrappers/issues/1564)) ([de214c6](https://www.github.com/snakemake/snakemake-wrappers/commit/de214c69c156f60579bd7c8f20ef9b1b289572e8))
* autobump bio/pyroe/makeunspliceunspliced ([#1566](https://www.github.com/snakemake/snakemake-wrappers/issues/1566)) ([422e811](https://www.github.com/snakemake/snakemake-wrappers/commit/422e8112ca1cf98fbc30e01faf5300622862b7f3))
* autobump bio/qualimap/bamqc ([#1621](https://www.github.com/snakemake/snakemake-wrappers/issues/1621)) ([6806b8a](https://www.github.com/snakemake/snakemake-wrappers/commit/6806b8ae9f34315322bbfe50a5e9a81ac1718337))
* autobump bio/salmon/index ([#1532](https://www.github.com/snakemake/snakemake-wrappers/issues/1532)) ([dad1a25](https://www.github.com/snakemake/snakemake-wrappers/commit/dad1a25a858933902b0c7fba3fcbef51fd540723))
* autobump bio/samtools/calmd ([#1576](https://www.github.com/snakemake/snakemake-wrappers/issues/1576)) ([76c7661](https://www.github.com/snakemake/snakemake-wrappers/commit/76c76614bbd715396f19c38d32b38d8f489b4e84))
* autobump bio/samtools/faidx ([#1698](https://www.github.com/snakemake/snakemake-wrappers/issues/1698)) ([665c9c4](https://www.github.com/snakemake/snakemake-wrappers/commit/665c9c4dc375c4c1268703c865e99c047c061252))
* autobump bio/samtools/fastx ([#1644](https://www.github.com/snakemake/snakemake-wrappers/issues/1644)) ([26fef49](https://www.github.com/snakemake/snakemake-wrappers/commit/26fef493665b6cafd1a01cc61f062bee10a3c77d))
* autobump bio/samtools/fixmate ([#1686](https://www.github.com/snakemake/snakemake-wrappers/issues/1686)) ([3de2261](https://www.github.com/snakemake/snakemake-wrappers/commit/3de2261f9139a451b226f989e499f9b4062b8430))
* autobump bio/samtools/flagstat ([#1612](https://www.github.com/snakemake/snakemake-wrappers/issues/1612)) ([85c89a1](https://www.github.com/snakemake/snakemake-wrappers/commit/85c89a17b64010ed54035699cf2fef145ccd9699))
* autobump bio/samtools/sort ([#1528](https://www.github.com/snakemake/snakemake-wrappers/issues/1528)) ([11453ad](https://www.github.com/snakemake/snakemake-wrappers/commit/11453ad0b0dbd7b20efabaf5bb0050210ff3b95f))
* autobump bio/samtools/sort ([#1707](https://www.github.com/snakemake/snakemake-wrappers/issues/1707)) ([2a9efe5](https://www.github.com/snakemake/snakemake-wrappers/commit/2a9efe5956a6b5eecd9bdc6069f1e17e59e0a5f8))
* autobump bio/samtools/stats ([#1615](https://www.github.com/snakemake/snakemake-wrappers/issues/1615)) ([6b1bb79](https://www.github.com/snakemake/snakemake-wrappers/commit/6b1bb79c5c28c40ec2d62abc0543c0961ffa216d))
* autobump bio/samtools/stats ([#1628](https://www.github.com/snakemake/snakemake-wrappers/issues/1628)) ([6895834](https://www.github.com/snakemake/snakemake-wrappers/commit/689583407979460b92e3c2c581b7695a35ddab3d))
* autobump bio/samtools/stats ([#1674](https://www.github.com/snakemake/snakemake-wrappers/issues/1674)) ([7bd8a71](https://www.github.com/snakemake/snakemake-wrappers/commit/7bd8a718156c2c73ca4228324132ca3527a6ffab))
* autobump bio/samtools/view ([#1525](https://www.github.com/snakemake/snakemake-wrappers/issues/1525)) ([2755074](https://www.github.com/snakemake/snakemake-wrappers/commit/275507412b0d4a6769080a8b8e78e0f6a6776c22))
* autobump bio/samtools/view ([#1608](https://www.github.com/snakemake/snakemake-wrappers/issues/1608)) ([f582deb](https://www.github.com/snakemake/snakemake-wrappers/commit/f582deb36f56a10d2c1e6c2d789229a987493c01))
* autobump bio/seqkit ([#1610](https://www.github.com/snakemake/snakemake-wrappers/issues/1610)) ([cabdc5a](https://www.github.com/snakemake/snakemake-wrappers/commit/cabdc5a900ec70fbd6f0316e983d9905c354d306))
* autobump bio/seqkit ([#1673](https://www.github.com/snakemake/snakemake-wrappers/issues/1673)) ([13261f8](https://www.github.com/snakemake/snakemake-wrappers/commit/13261f8391c4834dd6dcc689839201eed9006d1a))
* autobump bio/seqtk/mergepe ([#1585](https://www.github.com/snakemake/snakemake-wrappers/issues/1585)) ([c671e66](https://www.github.com/snakemake/snakemake-wrappers/commit/c671e667ca0db03072aa562cff7bef1bfc9577f5))
* autobump bio/snpeff/annotate ([#1624](https://www.github.com/snakemake/snakemake-wrappers/issues/1624)) ([34a1005](https://www.github.com/snakemake/snakemake-wrappers/commit/34a1005b6e5f539428f0d4e409f5f98db4b9afce))
* autobump bio/snpeff/annotate ([#1685](https://www.github.com/snakemake/snakemake-wrappers/issues/1685)) ([a7b797d](https://www.github.com/snakemake/snakemake-wrappers/commit/a7b797d0860cd336de1805660279e6561217097b))
* autobump bio/snpeff/download ([#1626](https://www.github.com/snakemake/snakemake-wrappers/issues/1626)) ([9a649d3](https://www.github.com/snakemake/snakemake-wrappers/commit/9a649d3999b36de89f3ca4311a210f87af31790e))
* autobump bio/snpsift/annotate ([#1593](https://www.github.com/snakemake/snakemake-wrappers/issues/1593)) ([bc9c1a6](https://www.github.com/snakemake/snakemake-wrappers/commit/bc9c1a6bde205599beecadd67145a5f61b669e39))
* autobump bio/snpsift/annotate ([#1645](https://www.github.com/snakemake/snakemake-wrappers/issues/1645)) ([be76f44](https://www.github.com/snakemake/snakemake-wrappers/commit/be76f44e1cd80653468744511671bce1fd902774))
* autobump bio/snpsift/annotate ([#1675](https://www.github.com/snakemake/snakemake-wrappers/issues/1675)) ([baee34b](https://www.github.com/snakemake/snakemake-wrappers/commit/baee34b54edc532bf4201a7879ed0e6be5e31733))
* autobump bio/snpsift/gwascat ([#1613](https://www.github.com/snakemake/snakemake-wrappers/issues/1613)) ([1764ca5](https://www.github.com/snakemake/snakemake-wrappers/commit/1764ca5869b8e1625b12e5879a011f0731e10f55))
* autobump bio/snpsift/gwascat ([#1657](https://www.github.com/snakemake/snakemake-wrappers/issues/1657)) ([8cc8988](https://www.github.com/snakemake/snakemake-wrappers/commit/8cc8988f04b9817658328e0dbe675ce48d3e7d7e))
* autobump bio/snpsift/varType ([#1583](https://www.github.com/snakemake/snakemake-wrappers/issues/1583)) ([ad5d062](https://www.github.com/snakemake/snakemake-wrappers/commit/ad5d062fdc333fbe88c0108d9d77bb5327d7b421))
* autobump bio/sra-tools/fasterq-dump ([#1655](https://www.github.com/snakemake/snakemake-wrappers/issues/1655)) ([ceb9ed8](https://www.github.com/snakemake/snakemake-wrappers/commit/ceb9ed8f9eba541b7b6c8464dbd7a1323c0c495c))
* autobump bio/tabix/index ([#1658](https://www.github.com/snakemake/snakemake-wrappers/issues/1658)) ([3bcd66d](https://www.github.com/snakemake/snakemake-wrappers/commit/3bcd66d900b786f3dcdbdaf40880b96e08df58c7))
* autobump bio/transdecoder/longorfs ([#1617](https://www.github.com/snakemake/snakemake-wrappers/issues/1617)) ([39bb6fc](https://www.github.com/snakemake/snakemake-wrappers/commit/39bb6fc9359d003760b0b92f83df5f911272462b))
* autobump bio/transdecoder/predict ([#1568](https://www.github.com/snakemake/snakemake-wrappers/issues/1568)) ([1d19059](https://www.github.com/snakemake/snakemake-wrappers/commit/1d190599e05ef242eba2a415d42720a959b9b46c))
* autobump bio/tximport ([#1632](https://www.github.com/snakemake/snakemake-wrappers/issues/1632)) ([bbbb631](https://www.github.com/snakemake/snakemake-wrappers/commit/bbbb63132b172359877c3b292444320bdc977eed))
* autobump bio/varscan/mpileup2indel ([#1556](https://www.github.com/snakemake/snakemake-wrappers/issues/1556)) ([5d4f281](https://www.github.com/snakemake/snakemake-wrappers/commit/5d4f2810968c4d59caf657233c9a2a2648713ffd))
* autobump bio/varscan/mpileup2snp ([#1665](https://www.github.com/snakemake/snakemake-wrappers/issues/1665)) ([4171043](https://www.github.com/snakemake/snakemake-wrappers/commit/41710437367100bec97330c3cce0f5211c0f34e2))
* autobump bio/varscan/somatic ([#1598](https://www.github.com/snakemake/snakemake-wrappers/issues/1598)) ([0a86cbc](https://www.github.com/snakemake/snakemake-wrappers/commit/0a86cbc2bb20b86c9c8138ecf6df2a0addca5ea3))
* autobump bio/vembrane/filter ([#1623](https://www.github.com/snakemake/snakemake-wrappers/issues/1623)) ([47e6d58](https://www.github.com/snakemake/snakemake-wrappers/commit/47e6d5864002b7ab3162b2687b5b1da66187b0e6))
* autobump bio/vembrane/table ([#1605](https://www.github.com/snakemake/snakemake-wrappers/issues/1605)) ([9c616da](https://www.github.com/snakemake/snakemake-wrappers/commit/9c616daa55ee34376e9ad19873ff47e23588c4c1))
* autobump bio/vep/cache ([#1604](https://www.github.com/snakemake/snakemake-wrappers/issues/1604)) ([1681978](https://www.github.com/snakemake/snakemake-wrappers/commit/16819786ffbd6c7d7a54bddaa3fadb481c4d018e))
* autobump bio/vg/construct ([#1529](https://www.github.com/snakemake/snakemake-wrappers/issues/1529)) ([6206f18](https://www.github.com/snakemake/snakemake-wrappers/commit/6206f18136d322026075e3796cad486852c62a92))
* autobump bio/vg/sim ([#1573](https://www.github.com/snakemake/snakemake-wrappers/issues/1573)) ([7c2b587](https://www.github.com/snakemake/snakemake-wrappers/commit/7c2b587409dbaf75ae29984b8059e4e3d2402ba0))
* autobump bio/vsearch ([#1590](https://www.github.com/snakemake/snakemake-wrappers/issues/1590)) ([ed2e49b](https://www.github.com/snakemake/snakemake-wrappers/commit/ed2e49b6aed0a0a1f5d5a6613b66aea067e0ef94))
* autobump bio/vsearch ([#1700](https://www.github.com/snakemake/snakemake-wrappers/issues/1700)) ([92f42fc](https://www.github.com/snakemake/snakemake-wrappers/commit/92f42fcfe28e06ecfab070c8539d096fb2aff3a0))
* autobump utils/datavzrd ([#1538](https://www.github.com/snakemake/snakemake-wrappers/issues/1538)) ([10a6b0b](https://www.github.com/snakemake/snakemake-wrappers/commit/10a6b0b47943544ebfa291e759390ffa933a7624))
* autobump utils/datavzrd ([#1717](https://www.github.com/snakemake/snakemake-wrappers/issues/1717)) ([3ab8832](https://www.github.com/snakemake/snakemake-wrappers/commit/3ab88327c5581bb9809bf7a918011db53ce0d159))
* set version for coolpuppy and update versions for some cooltools wrappers ([#1546](https://www.github.com/snakemake/snakemake-wrappers/issues/1546)) ([41ef6d0](https://www.github.com/snakemake/snakemake-wrappers/commit/41ef6d0573daad70e4edd1601dcca29a9ceba801))

### [2.2.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.2.0...v2.2.1) (2023-07-07)


### Performance Improvements

* autobump bio/bcftools/call ([#1508](https://www.github.com/snakemake/snakemake-wrappers/issues/1508)) ([4732e05](https://www.github.com/snakemake/snakemake-wrappers/commit/4732e051fc177b2285232798ed63eb01b5734fe0))
* autobump bio/bismark/bismark_genome_preparation ([#1512](https://www.github.com/snakemake/snakemake-wrappers/issues/1512)) ([531493a](https://www.github.com/snakemake/snakemake-wrappers/commit/531493acb3ede05ef26f6f230fd454593d08afd8))
* autobump bio/bustools/count ([#1516](https://www.github.com/snakemake/snakemake-wrappers/issues/1516)) ([4f3925a](https://www.github.com/snakemake/snakemake-wrappers/commit/4f3925ab7fe5913bd4f25e6f267146dc31a58e9b))
* autobump bio/delly ([#1505](https://www.github.com/snakemake/snakemake-wrappers/issues/1505)) ([6b12ad1](https://www.github.com/snakemake/snakemake-wrappers/commit/6b12ad1c38f7b7c105c26ff9434ccbbeb469970e))
* autobump bio/deseq2/wald ([#1510](https://www.github.com/snakemake/snakemake-wrappers/issues/1510)) ([3ab5304](https://www.github.com/snakemake/snakemake-wrappers/commit/3ab53047b504a266a3ded1aa95508c688a1e1d94))
* autobump bio/gatk/getpileupsummaries ([#1506](https://www.github.com/snakemake/snakemake-wrappers/issues/1506)) ([ed84924](https://www.github.com/snakemake/snakemake-wrappers/commit/ed849241aa03a125e8828b999414373cb4501b6c))
* autobump bio/gatk/haplotypecaller ([#1504](https://www.github.com/snakemake/snakemake-wrappers/issues/1504)) ([b45b7fd](https://www.github.com/snakemake/snakemake-wrappers/commit/b45b7fd6f5694cd0d158d3086ed17402f8f28523))
* autobump bio/gatk/selectvariants ([#1501](https://www.github.com/snakemake/snakemake-wrappers/issues/1501)) ([8557991](https://www.github.com/snakemake/snakemake-wrappers/commit/855799137c2dd4453154f2ba9fa3bface51c92d6))
* autobump bio/picard/collectinsertsizemetrics ([#1517](https://www.github.com/snakemake/snakemake-wrappers/issues/1517)) ([b9749bb](https://www.github.com/snakemake/snakemake-wrappers/commit/b9749bb97a66254b518be660f22d12887a0a7d80))
* autobump bio/picard/markduplicates ([#1511](https://www.github.com/snakemake/snakemake-wrappers/issues/1511)) ([6e4f778](https://www.github.com/snakemake/snakemake-wrappers/commit/6e4f7786dfc925e4fcc82c3bf60d81e17bf027db))
* autobump bio/salmon/quant ([#1513](https://www.github.com/snakemake/snakemake-wrappers/issues/1513)) ([a2c9c37](https://www.github.com/snakemake/snakemake-wrappers/commit/a2c9c37a5b0472a94d2824666da2c85e0f383c6a))
* autobump bio/snpeff/annotate ([#1507](https://www.github.com/snakemake/snakemake-wrappers/issues/1507)) ([b0acd16](https://www.github.com/snakemake/snakemake-wrappers/commit/b0acd16c82a5e0f5ed7d495646814e4764728939))
* autobump bio/snpsift/genesets ([#1514](https://www.github.com/snakemake/snakemake-wrappers/issues/1514)) ([41edbc7](https://www.github.com/snakemake/snakemake-wrappers/commit/41edbc79d7753f4049d1b9b4f29183827633a1c0))
* autobump bio/subread/featurecounts ([#1509](https://www.github.com/snakemake/snakemake-wrappers/issues/1509)) ([83256f1](https://www.github.com/snakemake/snakemake-wrappers/commit/83256f16b0b325fc794664f764bbe835b2b11348))
* autobump bio/trinity ([#1503](https://www.github.com/snakemake/snakemake-wrappers/issues/1503)) ([84c1bef](https://www.github.com/snakemake/snakemake-wrappers/commit/84c1bef8d7dd509562a419ea0ef9508fe868e03c))
* autobump bio/tximport ([#1520](https://www.github.com/snakemake/snakemake-wrappers/issues/1520)) ([26e8842](https://www.github.com/snakemake/snakemake-wrappers/commit/26e88422d3cb4d4d9a7f7d7913eb24b154fcd61f))
* autobump bio/vg/merge ([#1515](https://www.github.com/snakemake/snakemake-wrappers/issues/1515)) ([a85a6c9](https://www.github.com/snakemake/snakemake-wrappers/commit/a85a6c9da4f94df790c669367619b6e5e461dfc4))
* autobump bio/vg/prune ([#1519](https://www.github.com/snakemake/snakemake-wrappers/issues/1519)) ([93099d3](https://www.github.com/snakemake/snakemake-wrappers/commit/93099d322011e91260c3650c145c9e84bc7d755d))

## [2.2.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.1.1...v2.2.0) (2023-07-06)


### Features

* Deseq2 wald ([#1428](https://www.github.com/snakemake/snakemake-wrappers/issues/1428)) ([e0d2831](https://www.github.com/snakemake/snakemake-wrappers/commit/e0d28313726251e918ee92816a8c5102cf1712b8))
* Pyroe id-to-name ([#1499](https://www.github.com/snakemake/snakemake-wrappers/issues/1499)) ([6e1d31d](https://www.github.com/snakemake/snakemake-wrappers/commit/6e1d31d2162e6125268d1a9e11909cbac65d6098))

### [2.1.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.1.0...v2.1.1) (2023-06-30)


### Bug Fixes

* bug with -O being used for gap opening penalty and samtools output directory ([#1450](https://www.github.com/snakemake/snakemake-wrappers/issues/1450)) ([c3f227f](https://www.github.com/snakemake/snakemake-wrappers/commit/c3f227ff64ee0d694587b50340424447ee847746))


### Performance Improvements

* autobump bio/bcftools/mpileup ([#1483](https://www.github.com/snakemake/snakemake-wrappers/issues/1483)) ([438c39b](https://www.github.com/snakemake/snakemake-wrappers/commit/438c39bd15816b068193664bb37ec8dfd1e21b00))
* autobump bio/bcftools/view ([#1469](https://www.github.com/snakemake/snakemake-wrappers/issues/1469)) ([1025cee](https://www.github.com/snakemake/snakemake-wrappers/commit/1025cee51c5fdb005610781f394e36f77d3a4fad))
* autobump bio/bedtools/coveragebed ([#1487](https://www.github.com/snakemake/snakemake-wrappers/issues/1487)) ([b9b6123](https://www.github.com/snakemake/snakemake-wrappers/commit/b9b612307055dfc9ee3cf8a6aa6cf51419a1a9de))
* autobump bio/bismark/bam2nuc ([#1491](https://www.github.com/snakemake/snakemake-wrappers/issues/1491)) ([b7fe91a](https://www.github.com/snakemake/snakemake-wrappers/commit/b7fe91a39563ad2839d835128a126ff4b7a16833))
* autobump bio/diamond/makedb ([#1495](https://www.github.com/snakemake/snakemake-wrappers/issues/1495)) ([5885a0e](https://www.github.com/snakemake/snakemake-wrappers/commit/5885a0e6d00b1005d2ecef4679cfac0119404f10))
* autobump bio/freebayes ([#1478](https://www.github.com/snakemake/snakemake-wrappers/issues/1478)) ([dd4c02b](https://www.github.com/snakemake/snakemake-wrappers/commit/dd4c02b81c920e69826c3a86e7ef9f9074b2e76f))
* autobump bio/gatk/applybqsr ([#1470](https://www.github.com/snakemake/snakemake-wrappers/issues/1470)) ([7aca9d9](https://www.github.com/snakemake/snakemake-wrappers/commit/7aca9d992096602f4bdf6ec252aa2376c0bfc990))
* autobump bio/gatk/estimatelibrarycomplexity ([#1484](https://www.github.com/snakemake/snakemake-wrappers/issues/1484)) ([b06df5f](https://www.github.com/snakemake/snakemake-wrappers/commit/b06df5fd5096097902ef26ffe07520a6728d6850))
* autobump bio/gatk/genomicsdbimport ([#1492](https://www.github.com/snakemake/snakemake-wrappers/issues/1492)) ([826e722](https://www.github.com/snakemake/snakemake-wrappers/commit/826e722ee20720483b6a2a894482cde9268dfd18))
* autobump bio/gatk/intervallisttobed ([#1473](https://www.github.com/snakemake/snakemake-wrappers/issues/1473)) ([214dd6b](https://www.github.com/snakemake/snakemake-wrappers/commit/214dd6bb41ae07d985d603f7f04e53139ac0ee50))
* autobump bio/gatk/learnreadorientationmodel ([#1494](https://www.github.com/snakemake/snakemake-wrappers/issues/1494)) ([e2623fd](https://www.github.com/snakemake/snakemake-wrappers/commit/e2623fd5111df37291918ca6768279ae98f0b694))
* autobump bio/gatk/splitintervals ([#1481](https://www.github.com/snakemake/snakemake-wrappers/issues/1481)) ([444dda4](https://www.github.com/snakemake/snakemake-wrappers/commit/444dda46364af8f2ed6baa42b6f0586b51b4808f))
* autobump bio/gatk/variantannotator ([#1489](https://www.github.com/snakemake/snakemake-wrappers/issues/1489)) ([03b3fb5](https://www.github.com/snakemake/snakemake-wrappers/commit/03b3fb581e4bb062ce2128215a898c692650343f))
* autobump bio/gatk/variantrecalibrator ([#1496](https://www.github.com/snakemake/snakemake-wrappers/issues/1496)) ([3748dec](https://www.github.com/snakemake/snakemake-wrappers/commit/3748dec7b916254d8777c16c37114b8d0a618476))
* autobump bio/minimap2/aligner ([#1477](https://www.github.com/snakemake/snakemake-wrappers/issues/1477)) ([75c6265](https://www.github.com/snakemake/snakemake-wrappers/commit/75c6265df3f888acd849a1617164b51c42cd3a0d))
* autobump bio/picard/collectalignmentsummarymetrics ([#1475](https://www.github.com/snakemake/snakemake-wrappers/issues/1475)) ([06e9c4b](https://www.github.com/snakemake/snakemake-wrappers/commit/06e9c4be45b3c6596e9c0fdde2eacb6eb2a83bdb))
* autobump bio/picard/mergevcfs ([#1465](https://www.github.com/snakemake/snakemake-wrappers/issues/1465)) ([dbbc182](https://www.github.com/snakemake/snakemake-wrappers/commit/dbbc182bab3b3496a1cbbbf11816382a93fcc5f2))
* autobump bio/pretext/map ([#1493](https://www.github.com/snakemake/snakemake-wrappers/issues/1493)) ([7fcae7f](https://www.github.com/snakemake/snakemake-wrappers/commit/7fcae7f60fbbdc7073af5e31b1bd1dbc2dacf96b))
* autobump bio/qualimap/bamqc ([#1471](https://www.github.com/snakemake/snakemake-wrappers/issues/1471)) ([4fe5fdc](https://www.github.com/snakemake/snakemake-wrappers/commit/4fe5fdcb0a4aaa0229c52d50188402030ed656c3))
* autobump bio/samtools/depth ([#1486](https://www.github.com/snakemake/snakemake-wrappers/issues/1486)) ([6d23daf](https://www.github.com/snakemake/snakemake-wrappers/commit/6d23daf52b1746f64ffb4f01f66202cd38bdb12f))
* autobump bio/samtools/stats ([#1468](https://www.github.com/snakemake/snakemake-wrappers/issues/1468)) ([adc059b](https://www.github.com/snakemake/snakemake-wrappers/commit/adc059b4758b1374eb445d0652194b68a8826a14))
* autobump bio/snpsift/annotate ([#1480](https://www.github.com/snakemake/snakemake-wrappers/issues/1480)) ([a60f667](https://www.github.com/snakemake/snakemake-wrappers/commit/a60f66793d05dd707b8834041cb69a0c325fe49b))
* autobump bio/snpsift/dbnsfp ([#1490](https://www.github.com/snakemake/snakemake-wrappers/issues/1490)) ([8e8af31](https://www.github.com/snakemake/snakemake-wrappers/commit/8e8af3118fc6e8f6eeb00bd3412e780f775d36e1))
* autobump bio/varscan/mpileup2indel ([#1472](https://www.github.com/snakemake/snakemake-wrappers/issues/1472)) ([c0a7c47](https://www.github.com/snakemake/snakemake-wrappers/commit/c0a7c475e70e978cbe46e67afa3b70bc16019dfb))
* autobump bio/varscan/mpileup2snp ([#1476](https://www.github.com/snakemake/snakemake-wrappers/issues/1476)) ([a439e5f](https://www.github.com/snakemake/snakemake-wrappers/commit/a439e5f8b8a5362c28751079beb544964a0af7a4))
* autobump bio/varscan/somatic ([#1482](https://www.github.com/snakemake/snakemake-wrappers/issues/1482)) ([18671ad](https://www.github.com/snakemake/snakemake-wrappers/commit/18671adc6821aad751a67845b0e453456bea6475))
* autobump bio/vg/kmers ([#1479](https://www.github.com/snakemake/snakemake-wrappers/issues/1479)) ([aa00d14](https://www.github.com/snakemake/snakemake-wrappers/commit/aa00d1488989e64ce215672c86bbc94d169f6f33))
* autobump bio/xsv ([#1485](https://www.github.com/snakemake/snakemake-wrappers/issues/1485)) ([a0baa27](https://www.github.com/snakemake/snakemake-wrappers/commit/a0baa27897c3e11d439a5bbb3dd138029d869afe))
* update datavzrd ([#1497](https://www.github.com/snakemake/snakemake-wrappers/issues/1497)) ([143a9c8](https://www.github.com/snakemake/snakemake-wrappers/commit/143a9c8caadb5f4391b351dfc0786c896c751c3f))

## [2.1.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v2.0.0...v2.1.0) (2023-06-29)


### Features

* barrnap-wrapper ([#1448](https://www.github.com/snakemake/snakemake-wrappers/issues/1448)) ([34e4e2c](https://www.github.com/snakemake/snakemake-wrappers/commit/34e4e2c21049dc3370c141e19205399eca95a2c1))
* Xsv (complete subcomand suite) ([#1430](https://www.github.com/snakemake/snakemake-wrappers/issues/1430)) ([da81a5a](https://www.github.com/snakemake/snakemake-wrappers/commit/da81a5aef4260fca9cfc6e53817a0633d416a622))


### Bug Fixes

* add threads to trim_galore ([#1452](https://www.github.com/snakemake/snakemake-wrappers/issues/1452)) ([96a3958](https://www.github.com/snakemake/snakemake-wrappers/commit/96a39582e6cd9bf7c292b322bc14c3c0322382c3))
* inconsistent output filenames trim-galore ([#1451](https://www.github.com/snakemake/snakemake-wrappers/issues/1451)) ([b915e37](https://www.github.com/snakemake/snakemake-wrappers/commit/b915e37b6a7d6e20a84369225d49a613c55e029c))
* Nonpareil tweaks ([#1449](https://www.github.com/snakemake/snakemake-wrappers/issues/1449)) ([b32b341](https://www.github.com/snakemake/snakemake-wrappers/commit/b32b3412389f4de0a6dbd28908155788528ef8d5))


### Performance Improvements

* autobump bio/bedtools/bamtobed ([#1462](https://www.github.com/snakemake/snakemake-wrappers/issues/1462)) ([fafb668](https://www.github.com/snakemake/snakemake-wrappers/commit/fafb668d1af349bffeebad81f15947164a20970e))
* autobump bio/benchmark/chm-eval-sample ([#1438](https://www.github.com/snakemake/snakemake-wrappers/issues/1438)) ([3e62178](https://www.github.com/snakemake/snakemake-wrappers/commit/3e62178c9bffa8be375f35d3e50d3f3c298933f5))
* autobump bio/bismark/bismark ([#1445](https://www.github.com/snakemake/snakemake-wrappers/issues/1445)) ([2110b31](https://www.github.com/snakemake/snakemake-wrappers/commit/2110b31ef4a8fa72e58a12e5f1a05ec79b87fe7d))
* autobump bio/bismark/deduplicate_bismark ([#1460](https://www.github.com/snakemake/snakemake-wrappers/issues/1460)) ([e19ac1c](https://www.github.com/snakemake/snakemake-wrappers/commit/e19ac1c78ccda4d5eb1d3557eb37cd56faba46fb))
* autobump bio/blast/makeblastdb ([#1439](https://www.github.com/snakemake/snakemake-wrappers/issues/1439)) ([477dc3f](https://www.github.com/snakemake/snakemake-wrappers/commit/477dc3fe8a95f24ed5abe491a7494d703ae49047))
* autobump bio/cutadapt/se ([#1436](https://www.github.com/snakemake/snakemake-wrappers/issues/1436)) ([f0b1c63](https://www.github.com/snakemake/snakemake-wrappers/commit/f0b1c631591b902d0b4db8cd8fc6ef7ef001be1e))
* autobump bio/deeptools/plotcoverage ([#1443](https://www.github.com/snakemake/snakemake-wrappers/issues/1443)) ([369bf8c](https://www.github.com/snakemake/snakemake-wrappers/commit/369bf8ceb6b367844076a33599e5b981d03cb709))
* autobump bio/deeptools/plotprofile ([#1461](https://www.github.com/snakemake/snakemake-wrappers/issues/1461)) ([7d378c1](https://www.github.com/snakemake/snakemake-wrappers/commit/7d378c132b40e4dde670eb83873bad29bb59bd71))
* autobump bio/deseq2/deseqdataset ([#1447](https://www.github.com/snakemake/snakemake-wrappers/issues/1447)) ([969113f](https://www.github.com/snakemake/snakemake-wrappers/commit/969113f54b53ed156dcca00c12c60797ad1dc9cc))
* autobump bio/fastp ([#1456](https://www.github.com/snakemake/snakemake-wrappers/issues/1456)) ([deea9b6](https://www.github.com/snakemake/snakemake-wrappers/commit/deea9b6006c34a119916139bcb03d1db9ef3a3b1))
* autobump bio/gatk/variantstotable ([#1459](https://www.github.com/snakemake/snakemake-wrappers/issues/1459)) ([d942d2b](https://www.github.com/snakemake/snakemake-wrappers/commit/d942d2b189faf0e2550be0ab880101767bbf4112))
* autobump bio/gatk3/indelrealigner ([#1437](https://www.github.com/snakemake/snakemake-wrappers/issues/1437)) ([11b52bf](https://www.github.com/snakemake/snakemake-wrappers/commit/11b52bf54687f61621870448601523c283ce9e5f))
* autobump bio/hap.py/hap.py ([#1435](https://www.github.com/snakemake/snakemake-wrappers/issues/1435)) ([2669467](https://www.github.com/snakemake/snakemake-wrappers/commit/26694676366160152467e8b6ed169d5564aa17c2))
* autobump bio/minimap2/index ([#1433](https://www.github.com/snakemake/snakemake-wrappers/issues/1433)) ([77c690d](https://www.github.com/snakemake/snakemake-wrappers/commit/77c690da1a97e9321637d4b190894f666309cbf7))
* autobump bio/pbmm2/index ([#1442](https://www.github.com/snakemake/snakemake-wrappers/issues/1442)) ([cbbe8b8](https://www.github.com/snakemake/snakemake-wrappers/commit/cbbe8b86a3dc1311b6a8aa8531ce77ddb9b3f139))
* autobump bio/pyroe/makesplicedintronic ([#1382](https://www.github.com/snakemake/snakemake-wrappers/issues/1382)) ([2509e69](https://www.github.com/snakemake/snakemake-wrappers/commit/2509e694edd840cafb5bc8f273205e07b3a95889))
* autobump bio/spades/metaspades ([#1463](https://www.github.com/snakemake/snakemake-wrappers/issues/1463)) ([064acf8](https://www.github.com/snakemake/snakemake-wrappers/commit/064acf80006fdbf0160a345eb2b31429d7a6a303))
* autobump bio/ucsc/bedGraphToBigWig ([#1441](https://www.github.com/snakemake/snakemake-wrappers/issues/1441)) ([a587628](https://www.github.com/snakemake/snakemake-wrappers/commit/a587628ee55735ea7ef5c8edc7fd560295688cb5))
* autobump bio/ucsc/twoBitInfo ([#1458](https://www.github.com/snakemake/snakemake-wrappers/issues/1458)) ([ba6cba8](https://www.github.com/snakemake/snakemake-wrappers/commit/ba6cba80fb9c57ca034c2832567e744f17277520))
* autobump bio/unicycler ([#1446](https://www.github.com/snakemake/snakemake-wrappers/issues/1446)) ([2edc574](https://www.github.com/snakemake/snakemake-wrappers/commit/2edc574dfcef371da9335917891d43ffa7f3ecf4))
* autobump bio/vembrane/filter ([#1444](https://www.github.com/snakemake/snakemake-wrappers/issues/1444)) ([59a0c94](https://www.github.com/snakemake/snakemake-wrappers/commit/59a0c94226aca46b2e0c39ec7f06d26159ee11d1))
* autobump bio/vembrane/table ([#1457](https://www.github.com/snakemake/snakemake-wrappers/issues/1457)) ([058f164](https://www.github.com/snakemake/snakemake-wrappers/commit/058f1645c05587b93c4abfa0fd199f691be0f5cf))
* autobump bio/vep/plugins ([#1440](https://www.github.com/snakemake/snakemake-wrappers/issues/1440)) ([37ad96d](https://www.github.com/snakemake/snakemake-wrappers/commit/37ad96dbc3ad7d92cdd421d885570cc6704c4580))
* autobump bio/vg/ids ([#1454](https://www.github.com/snakemake/snakemake-wrappers/issues/1454)) ([bfc78d2](https://www.github.com/snakemake/snakemake-wrappers/commit/bfc78d2a1236d6cf3db61efbebe36b95cf8e1440))
* autobump utils/cairosvg ([#1455](https://www.github.com/snakemake/snakemake-wrappers/issues/1455)) ([326e20b](https://www.github.com/snakemake/snakemake-wrappers/commit/326e20b9f90e13ad4cbd6c867a32cd7d902b0b33))

## [2.0.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.32.1...v2.0.0) (2023-06-13)


### ⚠ BREAKING CHANGES

* replace individual seqkit wrappers with a single wrapper for all seqkit commands (#1426)

### Features

* remove existing run directory option for strelka ([#1297](https://www.github.com/snakemake/snakemake-wrappers/issues/1297)) ([6f384dd](https://www.github.com/snakemake/snakemake-wrappers/commit/6f384ddc857293ec799526b75d355f5015191f70))
* replace individual seqkit wrappers with a single wrapper for all seqkit commands ([#1426](https://www.github.com/snakemake/snakemake-wrappers/issues/1426)) ([c7a4d96](https://www.github.com/snakemake/snakemake-wrappers/commit/c7a4d960044888825f2b9475d4df7b8f09cec0a0))


### Performance Improvements

* update datavzrd to 2.21.0 ([#1424](https://www.github.com/snakemake/snakemake-wrappers/issues/1424)) ([c7d757a](https://www.github.com/snakemake/snakemake-wrappers/commit/c7d757a31b86a367c3e104590ec86ce343e8127f))

### [1.32.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.32.0...v1.32.1) (2023-06-09)


### Performance Improvements

* autobump bio/bedtools/slop ([#1419](https://www.github.com/snakemake/snakemake-wrappers/issues/1419)) ([68c27c9](https://www.github.com/snakemake/snakemake-wrappers/commit/68c27c929c251ad6e0658deb834d6f7788867653))
* autobump bio/bismark/bismark_methylation_extractor ([#1418](https://www.github.com/snakemake/snakemake-wrappers/issues/1418)) ([fa75c52](https://www.github.com/snakemake/snakemake-wrappers/commit/fa75c5286a50a22bea4bd8cc576ba012827503b7))
* autobump bio/blast/blastn ([#1416](https://www.github.com/snakemake/snakemake-wrappers/issues/1416)) ([9a73c52](https://www.github.com/snakemake/snakemake-wrappers/commit/9a73c520e065521fe4657c078d9d5047273f01ff))
* autobump bio/freebayes ([#1420](https://www.github.com/snakemake/snakemake-wrappers/issues/1420)) ([3d8a9ef](https://www.github.com/snakemake/snakemake-wrappers/commit/3d8a9ef0d1673236359e688d888a58cdcc114d55))
* autobump bio/gatk/cleansam ([#1421](https://www.github.com/snakemake/snakemake-wrappers/issues/1421)) ([bcbbcee](https://www.github.com/snakemake/snakemake-wrappers/commit/bcbbceeed5ae5c6af4fb949af80b93ba67887fb6))
* autobump bio/hap.py/pre.py ([#1414](https://www.github.com/snakemake/snakemake-wrappers/issues/1414)) ([307bd02](https://www.github.com/snakemake/snakemake-wrappers/commit/307bd0224758738eb654871eb4c6198eb4f28568))
* autobump bio/open-cravat/run ([#1413](https://www.github.com/snakemake/snakemake-wrappers/issues/1413)) ([58c1065](https://www.github.com/snakemake/snakemake-wrappers/commit/58c1065f513a036f0b6a7c1b1d8a211f121c9f67))
* autobump bio/seqtk/seq ([#1423](https://www.github.com/snakemake/snakemake-wrappers/issues/1423)) ([cc1a6bf](https://www.github.com/snakemake/snakemake-wrappers/commit/cc1a6bff91c1c5d58365d1a228bd3cf54ec61019))
* autobump bio/tximport ([#1422](https://www.github.com/snakemake/snakemake-wrappers/issues/1422)) ([7557c08](https://www.github.com/snakemake/snakemake-wrappers/commit/7557c0881321047591135c716a2e7491012cf6a6))
* autobump bio/vg/kmers ([#1417](https://www.github.com/snakemake/snakemake-wrappers/issues/1417)) ([0d849eb](https://www.github.com/snakemake/snakemake-wrappers/commit/0d849ebd22c73e3e77f776d55a5b161b59468d5a))

## [1.32.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.31.1...v1.32.0) (2023-06-07)


### Features

* add ragtag wrapper ([#1397](https://www.github.com/snakemake/snakemake-wrappers/issues/1397)) ([6a967c5](https://www.github.com/snakemake/snakemake-wrappers/commit/6a967c540801b30240c63ca12332bac8dbf0fe2c))
* add wrapper to plot nonpareil results ([#1398](https://www.github.com/snakemake/snakemake-wrappers/issues/1398)) ([1b31bd5](https://www.github.com/snakemake/snakemake-wrappers/commit/1b31bd5fcf5b24d5b7603579c0d024aee64551ab))


### Bug Fixes

* bug with SE reads ([#1395](https://www.github.com/snakemake/snakemake-wrappers/issues/1395)) ([f44c6a0](https://www.github.com/snakemake/snakemake-wrappers/commit/f44c6a0875794f13eb03983a876d00a5226ce02b))
* fastqc doesn't know how to process multiple files.  ([#1327](https://www.github.com/snakemake/snakemake-wrappers/issues/1327)) ([b5b9878](https://www.github.com/snakemake/snakemake-wrappers/commit/b5b9878a91bbbdc4ccb604d5b5864a12c34ba02d))
* indexed bam files can now be put as input ([#1378](https://www.github.com/snakemake/snakemake-wrappers/issues/1378)) ([7c53b89](https://www.github.com/snakemake/snakemake-wrappers/commit/7c53b89cd6b70b4675f4ee82fd55982f4cfa51b1))


### Performance Improvements

* autobump bio/bcftools/filter ([#1383](https://www.github.com/snakemake/snakemake-wrappers/issues/1383)) ([dab7630](https://www.github.com/snakemake/snakemake-wrappers/commit/dab7630075ae834c61918dc4ee5cb302022bc8ed))
* autobump bio/bcftools/view ([#1394](https://www.github.com/snakemake/snakemake-wrappers/issues/1394)) ([8a8d877](https://www.github.com/snakemake/snakemake-wrappers/commit/8a8d877c51dce3c2a966f1ff884728d0333a49fd))
* autobump bio/bedtools/complement ([#1392](https://www.github.com/snakemake/snakemake-wrappers/issues/1392)) ([7284ac2](https://www.github.com/snakemake/snakemake-wrappers/commit/7284ac2b1c38678db067c5c04fce590fdd9a85c9))
* autobump bio/bedtools/intersect ([#1403](https://www.github.com/snakemake/snakemake-wrappers/issues/1403)) ([6a839c1](https://www.github.com/snakemake/snakemake-wrappers/commit/6a839c182d0d0c1f9dc54b5b560491ccf01b21ce))
* autobump bio/bustools/sort ([#1411](https://www.github.com/snakemake/snakemake-wrappers/issues/1411)) ([54e2956](https://www.github.com/snakemake/snakemake-wrappers/commit/54e295607ac93101983916429de3bb3a9a1279fe))
* autobump bio/bwa-mem2/mem ([#1389](https://www.github.com/snakemake/snakemake-wrappers/issues/1389)) ([9a5828c](https://www.github.com/snakemake/snakemake-wrappers/commit/9a5828cae18fe542e41b42796e9da03d50fbd8a6))
* autobump bio/bwa/samse ([#1405](https://www.github.com/snakemake/snakemake-wrappers/issues/1405)) ([476f722](https://www.github.com/snakemake/snakemake-wrappers/commit/476f722e80a56405f93aa74480be74c558f83940))
* autobump bio/cutadapt/pe ([#1401](https://www.github.com/snakemake/snakemake-wrappers/issues/1401)) ([38dfed4](https://www.github.com/snakemake/snakemake-wrappers/commit/38dfed4b9f5bd1504dd40bad2432b3ebf8096ce0))
* autobump bio/deeptools/bamcoverage ([#1409](https://www.github.com/snakemake/snakemake-wrappers/issues/1409)) ([426852b](https://www.github.com/snakemake/snakemake-wrappers/commit/426852bfe9f60bd1c2d000f64af4c838d677f783))
* autobump bio/deeptools/computematrix ([#1373](https://www.github.com/snakemake/snakemake-wrappers/issues/1373)) ([6f3e9b5](https://www.github.com/snakemake/snakemake-wrappers/commit/6f3e9b5eedd5019ea36e840e7cc7101dbdc77639))
* autobump bio/deseq2/deseqdataset ([#1369](https://www.github.com/snakemake/snakemake-wrappers/issues/1369)) ([8ca67e8](https://www.github.com/snakemake/snakemake-wrappers/commit/8ca67e82ebb92e18dce5baf153f72b3e77bad7c6))
* autobump bio/fastq_screen ([#1375](https://www.github.com/snakemake/snakemake-wrappers/issues/1375)) ([abb82c4](https://www.github.com/snakemake/snakemake-wrappers/commit/abb82c4a98be3c71e17de50670d19579f63901ec))
* autobump bio/gatk/learnreadorientationmodel ([#1407](https://www.github.com/snakemake/snakemake-wrappers/issues/1407)) ([614f343](https://www.github.com/snakemake/snakemake-wrappers/commit/614f34377df8d7557959d15a50ff6238896bff64))
* autobump bio/gatk/scatterintervalsbyns ([#1387](https://www.github.com/snakemake/snakemake-wrappers/issues/1387)) ([61944c3](https://www.github.com/snakemake/snakemake-wrappers/commit/61944c37e94c2ef80228f3310ef7e64fe3ab0f5e))
* autobump bio/gatk/selectvariants ([#1376](https://www.github.com/snakemake/snakemake-wrappers/issues/1376)) ([e2962a1](https://www.github.com/snakemake/snakemake-wrappers/commit/e2962a14ccff2e339f5d137c729b1d5607b9e666))
* autobump bio/gatk/variantrecalibrator ([#1374](https://www.github.com/snakemake/snakemake-wrappers/issues/1374)) ([341ccaa](https://www.github.com/snakemake/snakemake-wrappers/commit/341ccaac9e9343774c57477e8d6fede514b7c8eb))
* autobump bio/gatk3/indelrealigner ([#1371](https://www.github.com/snakemake/snakemake-wrappers/issues/1371)) ([6ef06a1](https://www.github.com/snakemake/snakemake-wrappers/commit/6ef06a1e8fa5cad5a69906061d3827c656e6843b))
* autobump bio/hisat2/index ([#1370](https://www.github.com/snakemake/snakemake-wrappers/issues/1370)) ([b5e37ab](https://www.github.com/snakemake/snakemake-wrappers/commit/b5e37ab3ed8bd70ed969a444274a183fa9ff36f8))
* autobump bio/last/lastdb ([#1400](https://www.github.com/snakemake/snakemake-wrappers/issues/1400)) ([db60b46](https://www.github.com/snakemake/snakemake-wrappers/commit/db60b46ce39e9721770901a0b46084bc68823340))
* autobump bio/open-cravat/module ([#1399](https://www.github.com/snakemake/snakemake-wrappers/issues/1399)) ([fc2b86a](https://www.github.com/snakemake/snakemake-wrappers/commit/fc2b86a92430d32b2d8f5f8aa1ee1a697959c1de))
* autobump bio/paladin/index ([#1379](https://www.github.com/snakemake/snakemake-wrappers/issues/1379)) ([598d8e7](https://www.github.com/snakemake/snakemake-wrappers/commit/598d8e717261c02d663d99a0c81d44c8b9cfaac8))
* autobump bio/picard/bedtointervallist ([#1408](https://www.github.com/snakemake/snakemake-wrappers/issues/1408)) ([b0f6786](https://www.github.com/snakemake/snakemake-wrappers/commit/b0f6786e60c03cd82eede73456853375a63877cf))
* autobump bio/picard/revertsam ([#1384](https://www.github.com/snakemake/snakemake-wrappers/issues/1384)) ([007cbd1](https://www.github.com/snakemake/snakemake-wrappers/commit/007cbd17a36ada11943908d6c02dc4b8fc74a226))
* autobump bio/pyroe/makeunspliceunspliced ([#1406](https://www.github.com/snakemake/snakemake-wrappers/issues/1406)) ([61d8377](https://www.github.com/snakemake/snakemake-wrappers/commit/61d83774a3c86e5624e61ea4594c325fddf8bdd3))
* autobump bio/samtools/sort ([#1410](https://www.github.com/snakemake/snakemake-wrappers/issues/1410)) ([935a677](https://www.github.com/snakemake/snakemake-wrappers/commit/935a6770d422287330ed1977a44b4be245437026))
* autobump bio/snpsift/annotate ([#1390](https://www.github.com/snakemake/snakemake-wrappers/issues/1390)) ([f59bb6b](https://www.github.com/snakemake/snakemake-wrappers/commit/f59bb6ba01e13333fc8693b9e55773814d37a0dc))
* autobump bio/spades/metaspades ([#1385](https://www.github.com/snakemake/snakemake-wrappers/issues/1385)) ([df5c0d1](https://www.github.com/snakemake/snakemake-wrappers/commit/df5c0d18ce6a38a3db6206083414ee69fceeeecf))
* autobump bio/sra-tools/fasterq-dump ([#1380](https://www.github.com/snakemake/snakemake-wrappers/issues/1380)) ([8b007a5](https://www.github.com/snakemake/snakemake-wrappers/commit/8b007a51a066cbba0f0a390a08fa8e5c60d8464c))
* autobump bio/strling/merge ([#1404](https://www.github.com/snakemake/snakemake-wrappers/issues/1404)) ([f62427b](https://www.github.com/snakemake/snakemake-wrappers/commit/f62427b3abec766d7d13ad6d7f93c9c27456d363))
* autobump bio/ucsc/faToTwoBit ([#1388](https://www.github.com/snakemake/snakemake-wrappers/issues/1388)) ([8356b4f](https://www.github.com/snakemake/snakemake-wrappers/commit/8356b4fe00cad3529484a821bc7582b6f5a88a51))
* autobump bio/ucsc/gtfToGenePred ([#1391](https://www.github.com/snakemake/snakemake-wrappers/issues/1391)) ([32aa42f](https://www.github.com/snakemake/snakemake-wrappers/commit/32aa42f187351108aa7f6d2ca060c2446c16f9e6))
* autobump bio/ucsc/twoBitToFa ([#1393](https://www.github.com/snakemake/snakemake-wrappers/issues/1393)) ([ae1453a](https://www.github.com/snakemake/snakemake-wrappers/commit/ae1453a323d11c7a4d5eee81031180f0db690e47))
* autobump bio/vep/annotate ([#1386](https://www.github.com/snakemake/snakemake-wrappers/issues/1386)) ([3365493](https://www.github.com/snakemake/snakemake-wrappers/commit/3365493f7e2a93c55b700b9446ee5e73ab7c90cd))
* autobump bio/vg/construct ([#1381](https://www.github.com/snakemake/snakemake-wrappers/issues/1381)) ([0785aac](https://www.github.com/snakemake/snakemake-wrappers/commit/0785aaca7e5ce77faadf3cfe49b23d6af551bf57))
* autobump bio/vg/ids ([#1354](https://www.github.com/snakemake/snakemake-wrappers/issues/1354)) ([3743f2e](https://www.github.com/snakemake/snakemake-wrappers/commit/3743f2ec07af726542ed605f40377ad73c25b957))
* autobump bio/vg/prune ([#1377](https://www.github.com/snakemake/snakemake-wrappers/issues/1377)) ([7dc7890](https://www.github.com/snakemake/snakemake-wrappers/commit/7dc7890769257d161731b2004401db4b6760bae6))
* autobump bio/vg/sim ([#1402](https://www.github.com/snakemake/snakemake-wrappers/issues/1402)) ([3bf4bf7](https://www.github.com/snakemake/snakemake-wrappers/commit/3bf4bf754598d7efbff776d4a90cf3114c4e2383))

### [1.31.1](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.31.0...v1.31.1) (2023-05-17)


### Bug Fixes

* fix snpsift annotate output compression (bcf and vcf.gz) ([#1367](https://www.github.com/snakemake/snakemake-wrappers/issues/1367)) ([7b46592](https://www.github.com/snakemake/snakemake-wrappers/commit/7b46592aae016d1dbbf96b92dde26e7765bccb70))

## [1.31.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.30.0...v1.31.0) (2023-05-16)


### Features

* add nonpareil wrapper ([#1294](https://www.github.com/snakemake/snakemake-wrappers/issues/1294)) ([53318ed](https://www.github.com/snakemake/snakemake-wrappers/commit/53318edadc897c57d72375ba426dbdf9b456fe92))


### Bug Fixes

* removed unnecessary dependencies ([#1366](https://www.github.com/snakemake/snakemake-wrappers/issues/1366)) ([4262cea](https://www.github.com/snakemake/snakemake-wrappers/commit/4262cea3fad8b28d07b542461a941a89a6cde380))

## [1.30.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.29.0...v1.30.0) (2023-05-12)


### Features

* add memory inference to samtools sort ([#1208](https://www.github.com/snakemake/snakemake-wrappers/issues/1208)) ([d70a806](https://www.github.com/snakemake/snakemake-wrappers/commit/d70a80650c640ab37e21690bd9c90dc581d2ec4e))
* deeptools bamcoverage ([#1237](https://www.github.com/snakemake/snakemake-wrappers/issues/1237)) ([ee2413b](https://www.github.com/snakemake/snakemake-wrappers/commit/ee2413b7f4e5576692330821f3cdd8829d731144))
* deeptools plotcoverage ([#1241](https://www.github.com/snakemake/snakemake-wrappers/issues/1241)) ([d08e4c6](https://www.github.com/snakemake/snakemake-wrappers/commit/d08e4c6908347ff979ff512f6523368ed9fc0df2))
* DeseqDataSet from multiple input ([#1326](https://www.github.com/snakemake/snakemake-wrappers/issues/1326)) ([25d8a07](https://www.github.com/snakemake/snakemake-wrappers/commit/25d8a076bc6830bfcf58d7a5999b68a790879f9a))
* Gffread ([#1291](https://www.github.com/snakemake/snakemake-wrappers/issues/1291)) ([d613ddf](https://www.github.com/snakemake/snakemake-wrappers/commit/d613ddffa7f78f5697e836e71ce2e51f232c1884))
* Salmon-Tximport meta-wrapper ([#1270](https://www.github.com/snakemake/snakemake-wrappers/issues/1270)) ([1e31da2](https://www.github.com/snakemake/snakemake-wrappers/commit/1e31da29769eebefdff470ae24598eb479547bca))


### Bug Fixes

* auto memory calculation ([#1210](https://www.github.com/snakemake/snakemake-wrappers/issues/1210)) ([b08081f](https://www.github.com/snakemake/snakemake-wrappers/commit/b08081fc066b10040fcd94a8f9fd1b70099a6f54))
* ensembl annotation GRCh37 gft release ([#1296](https://www.github.com/snakemake/snakemake-wrappers/issues/1296)) ([d5be001](https://www.github.com/snakemake/snakemake-wrappers/commit/d5be001cfdd5cd85fdbd19abe15de43310f9bfed))
* fixed bug when formatting string in GATK denoisereadcounts ([#1343](https://www.github.com/snakemake/snakemake-wrappers/issues/1343)) ([8cc5d91](https://www.github.com/snakemake/snakemake-wrappers/commit/8cc5d91f0b459ef18d461367a449c9bf5c901571))


### Performance Improvements

* autobump bio/bcftools/call ([#1349](https://www.github.com/snakemake/snakemake-wrappers/issues/1349)) ([064d4a4](https://www.github.com/snakemake/snakemake-wrappers/commit/064d4a469e8a3be063c7ac2b4916127c1f4b9abf))
* autobump bio/bcftools/reheader ([#1362](https://www.github.com/snakemake/snakemake-wrappers/issues/1362)) ([bc4bb1d](https://www.github.com/snakemake/snakemake-wrappers/commit/bc4bb1deb95a5cab588c34b55e03496a5242dcf3))
* autobump bio/bcftools/stats ([#1361](https://www.github.com/snakemake/snakemake-wrappers/issues/1361)) ([444b198](https://www.github.com/snakemake/snakemake-wrappers/commit/444b198e0a97483ce66011a0cb022166d6d45ed2))
* autobump bio/bedtools/genomecov ([#1351](https://www.github.com/snakemake/snakemake-wrappers/issues/1351)) ([f39d37d](https://www.github.com/snakemake/snakemake-wrappers/commit/f39d37dd38dc6a1e672b901278cf8774a132f4c2))
* autobump bio/bedtools/merge ([#1348](https://www.github.com/snakemake/snakemake-wrappers/issues/1348)) ([46ba353](https://www.github.com/snakemake/snakemake-wrappers/commit/46ba35317bd292816fbc833ca43b2bc50485a0a9))
* autobump bio/bedtools/sort ([#1357](https://www.github.com/snakemake/snakemake-wrappers/issues/1357)) ([e17cb5a](https://www.github.com/snakemake/snakemake-wrappers/commit/e17cb5a405d0d770749969cd89a0bcc58179f292))
* autobump bio/bismark/bam2nuc ([#1341](https://www.github.com/snakemake/snakemake-wrappers/issues/1341)) ([ce2b39e](https://www.github.com/snakemake/snakemake-wrappers/commit/ce2b39e65752a5088088c65d67abe3fa4d01a0dc))
* autobump bio/bismark/bismark2report ([#1334](https://www.github.com/snakemake/snakemake-wrappers/issues/1334)) ([d497124](https://www.github.com/snakemake/snakemake-wrappers/commit/d497124a689d436169dd360e674bd7af7bfc7fa9))
* autobump bio/bowtie2/align ([#1356](https://www.github.com/snakemake/snakemake-wrappers/issues/1356)) ([0e6cc68](https://www.github.com/snakemake/snakemake-wrappers/commit/0e6cc68ed2499215903a1adb1e83c883f6d73277))
* autobump bio/busco ([#1359](https://www.github.com/snakemake/snakemake-wrappers/issues/1359)) ([41f1185](https://www.github.com/snakemake/snakemake-wrappers/commit/41f1185ee23cd2810022510a2d89f4ea39212a44))
* autobump bio/bwa/samxe ([#1335](https://www.github.com/snakemake/snakemake-wrappers/issues/1335)) ([8042216](https://www.github.com/snakemake/snakemake-wrappers/commit/80422161ea03b1d8a1f513f7562b7cbe6667a952))
* autobump bio/deeptools/plotfingerprint ([#1345](https://www.github.com/snakemake/snakemake-wrappers/issues/1345)) ([39f88b7](https://www.github.com/snakemake/snakemake-wrappers/commit/39f88b73d148b02436d7476642ca24b02201e6d6))
* autobump bio/gatk/applybqsr ([#1339](https://www.github.com/snakemake/snakemake-wrappers/issues/1339)) ([ec62a41](https://www.github.com/snakemake/snakemake-wrappers/commit/ec62a41f3ece28922bc9a35edec5c44997006320))
* autobump bio/gatk/splitncigarreads ([#1350](https://www.github.com/snakemake/snakemake-wrappers/issues/1350)) ([7a7eb1e](https://www.github.com/snakemake/snakemake-wrappers/commit/7a7eb1e46b65843a295055c6cd74fe49ee68466c))
* autobump bio/gatk/variantfiltration ([#1340](https://www.github.com/snakemake/snakemake-wrappers/issues/1340)) ([d108c9c](https://www.github.com/snakemake/snakemake-wrappers/commit/d108c9c0adc28b8b7bac14b418f1f79df91a90a5))
* autobump bio/manta ([#1342](https://www.github.com/snakemake/snakemake-wrappers/issues/1342)) ([a23858a](https://www.github.com/snakemake/snakemake-wrappers/commit/a23858aa5e6980e559ee8cb02f0a54208af9eef5))
* autobump bio/minimap2/aligner ([#1329](https://www.github.com/snakemake/snakemake-wrappers/issues/1329)) ([45c53eb](https://www.github.com/snakemake/snakemake-wrappers/commit/45c53eba9041a28745c2d678638827b0b2537667))
* autobump bio/open-cravat/run ([#1330](https://www.github.com/snakemake/snakemake-wrappers/issues/1330)) ([fc82508](https://www.github.com/snakemake/snakemake-wrappers/commit/fc82508898e6de6c5f673f1a3044bda7fe02d656))
* autobump bio/picard/addorreplacereadgroups ([#1333](https://www.github.com/snakemake/snakemake-wrappers/issues/1333)) ([d273596](https://www.github.com/snakemake/snakemake-wrappers/commit/d27359682dbe2a4c411971e09c72079a9d803dfb))
* autobump bio/picard/collectinsertsizemetrics ([#1352](https://www.github.com/snakemake/snakemake-wrappers/issues/1352)) ([ae1e2bd](https://www.github.com/snakemake/snakemake-wrappers/commit/ae1e2bd62f7a6683c495abc70cd9dd1773b683f4))
* autobump bio/rasusa ([#1353](https://www.github.com/snakemake/snakemake-wrappers/issues/1353)) ([3c41241](https://www.github.com/snakemake/snakemake-wrappers/commit/3c4124152e9b49bd02f944707e47517d6e7826dc))
* autobump bio/samtools/fastx ([#1347](https://www.github.com/snakemake/snakemake-wrappers/issues/1347)) ([d6e6329](https://www.github.com/snakemake/snakemake-wrappers/commit/d6e63291192027c7c4c994d8d5e2dee6f727b5cb))
* autobump bio/seqkit/fx2tab ([#1338](https://www.github.com/snakemake/snakemake-wrappers/issues/1338)) ([53922ca](https://www.github.com/snakemake/snakemake-wrappers/commit/53922ca8c2a7ad2da5c17a39fb98e724dff56df5))
* autobump bio/snpeff/annotate ([#1363](https://www.github.com/snakemake/snakemake-wrappers/issues/1363)) ([9ba0b3d](https://www.github.com/snakemake/snakemake-wrappers/commit/9ba0b3ddd02f784df8eddd203a5619362c88f36f))
* autobump bio/snpeff/download ([#1358](https://www.github.com/snakemake/snakemake-wrappers/issues/1358)) ([2c5a385](https://www.github.com/snakemake/snakemake-wrappers/commit/2c5a385ad1d499d183a6075d1c274d7beab14621))
* autobump bio/sourmash/compute ([#1360](https://www.github.com/snakemake/snakemake-wrappers/issues/1360)) ([1ec19c2](https://www.github.com/snakemake/snakemake-wrappers/commit/1ec19c22df58905271b50399b8b1d83e94801fe3))
* autobump bio/sra-tools/fasterq-dump ([#1355](https://www.github.com/snakemake/snakemake-wrappers/issues/1355)) ([d1118bd](https://www.github.com/snakemake/snakemake-wrappers/commit/d1118bd4f59c1315b99539c8b2d99bb1ac86326c))
* autobump bio/tabix/index ([#1336](https://www.github.com/snakemake/snakemake-wrappers/issues/1336)) ([dfab9c6](https://www.github.com/snakemake/snakemake-wrappers/commit/dfab9c6aa5e50596d7348553d8414c534130f5f8))
* autobump bio/vembrane/table ([#1337](https://www.github.com/snakemake/snakemake-wrappers/issues/1337)) ([953c0dc](https://www.github.com/snakemake/snakemake-wrappers/commit/953c0dcdedc8ebbaff96e139c93d5c2aef3ad87f))
* autobump bio/vep/plugins ([#1346](https://www.github.com/snakemake/snakemake-wrappers/issues/1346)) ([887ba11](https://www.github.com/snakemake/snakemake-wrappers/commit/887ba11f0be215ddf0110d6ba31de4a0eb93056c))
* autobump bio/vg/sim ([#1332](https://www.github.com/snakemake/snakemake-wrappers/issues/1332)) ([91574fd](https://www.github.com/snakemake/snakemake-wrappers/commit/91574fd8795d55ff9e60b35f884c4f2cd7956b54))

## [1.29.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.28.0...v1.29.0) (2023-05-04)


### Features

* Add seqkit subseq ([#1318](https://www.github.com/snakemake/snakemake-wrappers/issues/1318)) ([262d9bb](https://www.github.com/snakemake/snakemake-wrappers/commit/262d9bb50cf8d03edca00916bc29fe5f1009209a))
* Deeptools Alignement seive ([#1320](https://www.github.com/snakemake/snakemake-wrappers/issues/1320)) ([b7cb7ab](https://www.github.com/snakemake/snakemake-wrappers/commit/b7cb7ab5b70c1eec3b89d02f0bc94a2294e6a9aa))
* fix threads and new IO options in Bowtie2 ([#1324](https://www.github.com/snakemake/snakemake-wrappers/issues/1324)) ([a9c7117](https://www.github.com/snakemake/snakemake-wrappers/commit/a9c711718533f18429db50fb052549c49aa6fcf7))
* gatk CallCopyRatioSegments ([#1323](https://www.github.com/snakemake/snakemake-wrappers/issues/1323)) ([528c91a](https://www.github.com/snakemake/snakemake-wrappers/commit/528c91a5b87ffe0d34964b01478a9b5d520ed80f))
* gatk collectalleliccount wrapper ([#1316](https://www.github.com/snakemake/snakemake-wrappers/issues/1316)) ([158c328](https://www.github.com/snakemake/snakemake-wrappers/commit/158c328d1b846fb45c90c946edbcf2a7a0da15de))
* gatk collectreadcount wrapper ([#1315](https://www.github.com/snakemake/snakemake-wrappers/issues/1315)) ([ee55de4](https://www.github.com/snakemake/snakemake-wrappers/commit/ee55de4cc2a850775ef94d5394f9a220844d8a7b))
* gatk DenoisedReadCounts wrapper ([#1319](https://www.github.com/snakemake/snakemake-wrappers/issues/1319)) ([0288ace](https://www.github.com/snakemake/snakemake-wrappers/commit/0288ace7e61fbf2adf79514eefa2ff8f3566041e))
* gatk modelsegments wrapper ([#1321](https://www.github.com/snakemake/snakemake-wrappers/issues/1321)) ([dfecc26](https://www.github.com/snakemake/snakemake-wrappers/commit/dfecc26de3c649c4661ac26203d846a54f7dd0b0))
* Pyroe make-spliced+unspliced ([#1290](https://www.github.com/snakemake/snakemake-wrappers/issues/1290)) ([96a2cbb](https://www.github.com/snakemake/snakemake-wrappers/commit/96a2cbbf667fb45676087c2002fa875a76982e6b))


### Bug Fixes

* Lofreq indelqual ([#1325](https://www.github.com/snakemake/snakemake-wrappers/issues/1325)) ([dabecf0](https://www.github.com/snakemake/snakemake-wrappers/commit/dabecf065975b7e53102221a63ec11b2c812cdee))


### Performance Improvements

* Updated version of datavzrd to 2.19.1 ([#1328](https://www.github.com/snakemake/snakemake-wrappers/issues/1328)) ([fd89645](https://www.github.com/snakemake/snakemake-wrappers/commit/fd89645aa28773f872a3b2f54192d66129852d83))

## [1.28.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.27.0...v1.28.0) (2023-04-28)


### Features

* Pyroe make-spliced+intronic ([#1288](https://www.github.com/snakemake/snakemake-wrappers/issues/1288)) ([352d6f3](https://www.github.com/snakemake/snakemake-wrappers/commit/352d6f38218fba384e2ab93076966245a7494bc0))


### Performance Improvements

* autobump bio/bbtools/loglog ([#1304](https://www.github.com/snakemake/snakemake-wrappers/issues/1304)) ([9316253](https://www.github.com/snakemake/snakemake-wrappers/commit/93162531beede4dd06096630c4c1199022792ea5))
* autobump bio/bismark/bismark ([#1303](https://www.github.com/snakemake/snakemake-wrappers/issues/1303)) ([fa68ba8](https://www.github.com/snakemake/snakemake-wrappers/commit/fa68ba87f07eb5eb8499c16cc3a6f9888ced7bf0))
* autobump bio/fgbio/annotatebamwithumis ([#1312](https://www.github.com/snakemake/snakemake-wrappers/issues/1312)) ([13cb583](https://www.github.com/snakemake/snakemake-wrappers/commit/13cb583b4245d88127e13b6248fac76eddada186))
* autobump bio/gatk/intervallisttobed ([#1305](https://www.github.com/snakemake/snakemake-wrappers/issues/1305)) ([d895b8f](https://www.github.com/snakemake/snakemake-wrappers/commit/d895b8fa7a73083175f51f1c4a46505d42eab22e))
* autobump bio/minimap2/index ([#1308](https://www.github.com/snakemake/snakemake-wrappers/issues/1308)) ([a578d2f](https://www.github.com/snakemake/snakemake-wrappers/commit/a578d2f4bb66cfd0a862e0ea6dfa5e099aace832))
* autobump bio/paladin/prepare ([#1299](https://www.github.com/snakemake/snakemake-wrappers/issues/1299)) ([1e27b4c](https://www.github.com/snakemake/snakemake-wrappers/commit/1e27b4cef31a985dace89b17cb04d8395a211e0e))
* autobump bio/picard/mergevcfs ([#1307](https://www.github.com/snakemake/snakemake-wrappers/issues/1307)) ([7a8a8aa](https://www.github.com/snakemake/snakemake-wrappers/commit/7a8a8aa893fcd0b5be78c3576e7e25335e010492))
* autobump bio/qualimap/rnaseq ([#1306](https://www.github.com/snakemake/snakemake-wrappers/issues/1306)) ([0ba2d3e](https://www.github.com/snakemake/snakemake-wrappers/commit/0ba2d3ec80362179223149bf06d97e3f0b35bc84))
* autobump bio/samtools/merge ([#1300](https://www.github.com/snakemake/snakemake-wrappers/issues/1300)) ([69332cd](https://www.github.com/snakemake/snakemake-wrappers/commit/69332cd327df12de1935f9c5e1e993f5c33900f4))
* autobump bio/samtools/mpileup ([#1310](https://www.github.com/snakemake/snakemake-wrappers/issues/1310)) ([f72ccf0](https://www.github.com/snakemake/snakemake-wrappers/commit/f72ccf0b3ef51a8ceeda5474367902781103edc1))
* autobump bio/seqkit/grep ([#1301](https://www.github.com/snakemake/snakemake-wrappers/issues/1301)) ([dfa1f4d](https://www.github.com/snakemake/snakemake-wrappers/commit/dfa1f4d2ddbe03295c8c4eb9e888e15995333b4c))
* autobump bio/snpsift/dbnsfp ([#1309](https://www.github.com/snakemake/snakemake-wrappers/issues/1309)) ([007437e](https://www.github.com/snakemake/snakemake-wrappers/commit/007437e877d48a091e3da77c1abbb152f0987e37))
* autobump bio/vembrane/filter ([#1311](https://www.github.com/snakemake/snakemake-wrappers/issues/1311)) ([15dc129](https://www.github.com/snakemake/snakemake-wrappers/commit/15dc12911e108fca225ff1a049b7dcb0115385dd))
* update datavzrd to 2.18.5 ([#1313](https://www.github.com/snakemake/snakemake-wrappers/issues/1313)) ([0089e88](https://www.github.com/snakemake/snakemake-wrappers/commit/0089e8825eb6b962be66da9a0964bd658b9b96fc))

## [1.27.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.26.0...v1.27.0) (2023-04-26)


### Features

* Update datavzrd to 2.18.4 and add extra params ([#1292](https://www.github.com/snakemake/snakemake-wrappers/issues/1292)) ([fa11c1c](https://www.github.com/snakemake/snakemake-wrappers/commit/fa11c1cc37361f879d47ae9dbcf5d7e410003cb1))

## [1.26.0](https://www.github.com/snakemake/snakemake-wrappers/compare/v1.25.0...v1.26.0) (2023-04-21)


### Features

* added vsearch wrapper ([#1149](https://www.github.com/snakemake/snakemake-wrappers/issues/1149)) ([79342b7](https://www.github.com/snakemake/snakemake-wrappers/commit/79342b73df13b135e09dd61da5d185f84c20f6a1))
* also define overhang on params.extra ([#1173](https://www.github.com/snakemake/snakemake-wrappers/issues/1173)) ([7e63821](https://www.github.com/snakemake/snakemake-wrappers/commit/7e6382183ea02e086360dba5946a8725a3cdc98d))
* automate inference of index name ([#1169](https://www.github.com/snakemake/snakemake-wrappers/issues/1169)) ([0d2c92a](https://www.github.com/snakemake/snakemake-wrappers/commit/0d2c92a5be480dd60cdb1c422282b9812aa01e2f))
* Enhance deeptools compute matrix ([#1236](https://www.github.com/snakemake/snakemake-wrappers/issues/1236)) ([a44bef5](https://www.github.com/snakemake/snakemake-wrappers/commit/a44bef54526ea07da64305147aa8cfa9f74497a9))
* Lofreq indelqual wrapper ([#1166](https://www.github.com/snakemake/snakemake-wrappers/issues/1166)) ([e2215f2](https://www.github.com/snakemake/snakemake-wrappers/commit/e2215f2e3cc18ed0ee165a440c3bb1752babab59))
* update datavzrd 2.18.1 ([#1171](https://www.github.com/snakemake/snakemake-wrappers/issues/1171)) ([00b9b1c](https://www.github.com/snakemake/snakemake-wrappers/commit/00b9b1cfac184303f70716749977e0343a09e8d0))


### Bug Fixes

* allow for arbitrary filename prefixes in the optitype wrapper ([#500](https://www.github.com/snakemake/snakemake-wrappers/issues/500)) ([0bf7175](https://www.github.com/snakemake/snakemake-wrappers/commit/0bf71755787c9c207f578d74007948ec7f89dfa8))


### Performance Improvements

* autobump bio/bazam ([#1187](https://www.github.com/snakemake/snakemake-wrappers/issues/1187)) ([df7d90e](https://www.github.com/snakemake/snakemake-wrappers/commit/df7d90e18cb33d3bd57c8720ab00971a26ee952a))
* autobump bio/bbtools/bbduk ([#1269](https://www.github.com/snakemake/snakemake-wrappers/issues/1269)) ([86c7a0a](https://www.github.com/snakemake/snakemake-wrappers/commit/86c7a0ac481bbb643a1d5460cc6668e134dc74e4))
* autobump bio/bcftools/call ([#1181](https://www.github.com/snakemake/snakemake-wrappers/issues/1181)) ([7fbc611](https://www.github.com/snakemake/snakemake-wrappers/commit/7fbc61182b3f9163c946306ec01ffd3575988970))
* autobump bio/bcftools/concat ([#1183](https://www.github.com/snakemake/snakemake-wrappers/issues/1183)) ([93d7103](https://www.github.com/snakemake/snakemake-wrappers/commit/93d71037234a1162036225065ac2ec329f1d1c34))
* autobump bio/bcftools/index ([#1279](https://www.github.com/snakemake/snakemake-wrappers/issues/1279)) ([3affe33](https://www.github.com/snakemake/snakemake-wrappers/commit/3affe33f6ed69becd7317b015e40ac2b4d7ac125))
* autobump bio/bcftools/merge ([#1266](https://www.github.com/snakemake/snakemake-wrappers/issues/1266)) ([b0a2c88](https://www.github.com/snakemake/snakemake-wrappers/commit/b0a2c88ac6239b55ac6638d35f80946c839220cd))
* autobump bio/bcftools/norm ([#1192](https://www.github.com/snakemake/snakemake-wrappers/issues/1192)) ([9e06c59](https://www.github.com/snakemake/snakemake-wrappers/commit/9e06c59da15866ea0f6c4793e053cb5169815fcd))
* autobump bio/bcftools/norm ([#1212](https://www.github.com/snakemake/snakemake-wrappers/issues/1212)) ([3667c6b](https://www.github.com/snakemake/snakemake-wrappers/commit/3667c6b1d3f824f4153212c18b9abbcca19a31e7))
* autobump bio/bcftools/sort ([#1257](https://www.github.com/snakemake/snakemake-wrappers/issues/1257)) ([dd478d2](https://www.github.com/snakemake/snakemake-wrappers/commit/dd478d216b6865a8828728a51354ad09ab286967))
* autobump bio/bcftools/stats ([#1197](https://www.github.com/snakemake/snakemake-wrappers/issues/1197)) ([c844da5](https://www.github.com/snakemake/snakemake-wrappers/commit/c844da5a713c588f3aaacd0d17494312c0901b43))
* autobump bio/bellerophon ([#1199](https://www.github.com/snakemake/snakemake-wrappers/issues/1199)) ([a2fe593](https://www.github.com/snakemake/snakemake-wrappers/commit/a2fe593f4e4f98dd3a135617129c817669f83b71))
* autobump bio/bellerophon ([#1286](https://www.github.com/snakemake/snakemake-wrappers/issues/1286)) ([2a21d19](https://www.github.com/snakemake/snakemake-wrappers/commit/2a21d1948ce87e13f781309e73ed42dadf297d15))
* autobump bio/bismark/bismark_genome_preparation ([#1276](https://www.github.com/snakemake/snakemake-wrappers/issues/1276)) ([5074972](https://www.github.com/snakemake/snakemake-wrappers/commit/507497256b9bf5b4d296ca105696e6bd4532b118))
* autobump bio/bismark/bismark_methylation_extractor ([#1220](https://www.github.com/snakemake/snakemake-wrappers/issues/1220)) ([05964de](https://www.github.com/snakemake/snakemake-wrappers/commit/05964de5e1e9c738654bd18c8f07cecf2626711b))
* autobump bio/bismark/bismark2bedGraph ([#1258](https://www.github.com/snakemake/snakemake-wrappers/issues/1258)) ([3eb60c2](https://www.github.com/snakemake/snakemake-wrappers/commit/3eb60c226ed74464e3b31b16c22cc5d99cf465e5))
* autobump bio/bismark/bismark2summary ([#1235](https://www.github.com/snakemake/snakemake-wrappers/issues/1235)) ([74a9de2](https://www.github.com/snakemake/snakemake-wrappers/commit/74a9de2c0896bc4ced38561bfa978bd99bd01e02))
* autobump bio/bowtie2/align ([#1206](https://www.github.com/snakemake/snakemake-wrappers/issues/1206)) ([d3544b0](https://www.github.com/snakemake/snakemake-wrappers/commit/d3544b024545620f4f17ca390d1466cebf5bca21))
* autobump bio/busco ([#1255](https://www.github.com/snakemake/snakemake-wrappers/issues/1255)) ([402aaaa](https://www.github.com/snakemake/snakemake-wrappers/commit/402aaaaf2cbbc47314db353905292a6e572ceb61))
* autobump bio/bwa-mem2/mem ([#1202](https://www.github.com/snakemake/snakemake-wrappers/issues/1202)) ([90e1d60](https://www.github.com/snakemake/snakemake-wrappers/commit/90e1d60c7f9f9c518814196f2e9d94b9a7fb6496))
* autobump bio/bwa-meme/index ([#1180](https://www.github.com/snakemake/snakemake-wrappers/issues/1180)) ([1f0378c](https://www.github.com/snakemake/snakemake-wrappers/commit/1f0378cdb6ed256362cf753fdba82d6f71677307))
* autobump bio/bwa-meme/mem ([#1163](https://www.github.com/snakemake/snakemake-wrappers/issues/1163)) ([5236667](https://www.github.com/snakemake/snakemake-wrappers/commit/52366674dbfaac0796041db97397e10b216bdf1a))
* autobump bio/bwa-meme/mem ([#1231](https://www.github.com/snakemake/snakemake-wrappers/issues/1231)) ([1ad2b8d](https://www.github.com/snakemake/snakemake-wrappers/commit/1ad2b8deb38664ebd2c92d67ce77fc095b6a4a18))
* autobump bio/bwa-memx/index ([#1207](https://www.github.com/snakemake/snakemake-wrappers/issues/1207)) ([59be498](https://www.github.com/snakemake/snakemake-wrappers/commit/59be498ccf3c3eb267c27db84ddbb4ad78157d29))
* autobump bio/bwa-memx/mem ([#1268](https://www.github.com/snakemake/snakemake-wrappers/issues/1268)) ([a2fe8b9](https://www.github.com/snakemake/snakemake-wrappers/commit/a2fe8b975f3ac9e61cdcea172e506292b6a69a97))
* autobump bio/bwa/sampe ([#1225](https://www.github.com/snakemake/snakemake-wrappers/issues/1225)) ([d759781](https://www.github.com/snakemake/snakemake-wrappers/commit/d759781ec230084724d3dad2005aee196c135889))
* autobump bio/cutadapt/pe ([#1219](https://www.github.com/snakemake/snakemake-wrappers/issues/1219)) ([44f346e](https://www.github.com/snakemake/snakemake-wrappers/commit/44f346e2094a5d1c69d4bad14c98dfe3fb641b57))
* autobump bio/cutadapt/se ([#1253](https://www.github.com/snakemake/snakemake-wrappers/issues/1253)) ([95c8278](https://www.github.com/snakemake/snakemake-wrappers/commit/95c8278409f14990147d501a019cbe875ad4b28b))
* autobump bio/delly ([#1267](https://www.github.com/snakemake/snakemake-wrappers/issues/1267)) ([75a0d1a](https://www.github.com/snakemake/snakemake-wrappers/commit/75a0d1a0a2b03622f76f814258719c396691e5c7))
* autobump bio/diamond/blastp ([#1161](https://www.github.com/snakemake/snakemake-wrappers/issues/1161)) ([1f89877](https://www.github.com/snakemake/snakemake-wrappers/commit/1f898770af5b3c41135ede213508885bb214ab5f))
* autobump bio/diamond/blastx ([#1221](https://www.github.com/snakemake/snakemake-wrappers/issues/1221)) ([480fc20](https://www.github.com/snakemake/snakemake-wrappers/commit/480fc206378e088a1c7a46e71523a63bb7fe048a))
* autobump bio/diamond/makedb ([#1223](https://www.github.com/snakemake/snakemake-wrappers/issues/1223)) ([49d1484](https://www.github.com/snakemake/snakemake-wrappers/commit/49d14842fa6be1be1ed439b1107b3b4a952f6e45))
* autobump bio/fgbio/collectduplexseqmetrics ([#1201](https://www.github.com/snakemake/snakemake-wrappers/issues/1201)) ([04e4ec7](https://www.github.com/snakemake/snakemake-wrappers/commit/04e4ec73d53f15993ad55563c9477fb2885ff0f8))
* autobump bio/gatk/applybqsrspark ([#1194](https://www.github.com/snakemake/snakemake-wrappers/issues/1194)) ([65f53d8](https://www.github.com/snakemake/snakemake-wrappers/commit/65f53d89cee7a2b7903891fd33b40a33fd328c2f))
* autobump bio/gatk/applybqsrspark ([#1250](https://www.github.com/snakemake/snakemake-wrappers/issues/1250)) ([56efdd1](https://www.github.com/snakemake/snakemake-wrappers/commit/56efdd137d91a8bcbeebcfdb1591a5f7ccba2c32))
* autobump bio/gatk/applyvqsr ([#1274](https://www.github.com/snakemake/snakemake-wrappers/issues/1274)) ([8b8d890](https://www.github.com/snakemake/snakemake-wrappers/commit/8b8d89097eeccf042c848eab72ef2f3d964d2714))
* autobump bio/gatk/baserecalibrator ([#1249](https://www.github.com/snakemake/snakemake-wrappers/issues/1249)) ([788ed8f](https://www.github.com/snakemake/snakemake-wrappers/commit/788ed8f9d5c9fbdceece90cf2f53ca02dfa0bc14))
* autobump bio/gatk/baserecalibratorspark ([#1185](https://www.github.com/snakemake/snakemake-wrappers/issues/1185)) ([f5a5f47](https://www.github.com/snakemake/snakemake-wrappers/commit/f5a5f47382b2a7d9fce892d5564b8ef73dae9b0e))
* autobump bio/gatk/combinegvcfs ([#1261](https://www.github.com/snakemake/snakemake-wrappers/issues/1261)) ([bd3066a](https://www.github.com/snakemake/snakemake-wrappers/commit/bd3066a4b8444e00ed6fefa6d6aab8483d73f5fe))
* autobump bio/gatk/estimatelibrarycomplexity ([#1252](https://www.github.com/snakemake/snakemake-wrappers/issues/1252)) ([12f5440](https://www.github.com/snakemake/snakemake-wrappers/commit/12f54404f391cdd250471bde20442e131ce62e5b))
* autobump bio/gatk/filtermutectcalls ([#1155](https://www.github.com/snakemake/snakemake-wrappers/issues/1155)) ([0071533](https://www.github.com/snakemake/snakemake-wrappers/commit/00715334b70c8b0e2ae1e52b47351320fe8157af))
* autobump bio/gatk/filtermutectcalls ([#1195](https://www.github.com/snakemake/snakemake-wrappers/issues/1195)) ([7f05ddf](https://www.github.com/snakemake/snakemake-wrappers/commit/7f05ddf98bf36db83fb4846188f0b512cd08b68f))
* autobump bio/gatk/genomicsdbimport ([#1215](https://www.github.com/snakemake/snakemake-wrappers/issues/1215)) ([300dbe8](https://www.github.com/snakemake/snakemake-wrappers/commit/300dbe83c2ed9e573318a8b30fd22293541695ab))
* autobump bio/gatk/genotypegvcfs ([#1179](https://www.github.com/snakemake/snakemake-wrappers/issues/1179)) ([85758b7](https://www.github.com/snakemake/snakemake-wrappers/commit/85758b7f4d36fb40b9e9826200cba5cf5e95b29b))
* autobump bio/gatk/getpileupsummaries ([#1277](https://www.github.com/snakemake/snakemake-wrappers/issues/1277)) ([2239049](https://www.github.com/snakemake/snakemake-wrappers/commit/2239049edb6f3324cec7d43f9ecd50cdea30e6d4))
* autobump bio/gatk/haplotypecaller ([#1256](https://www.github.com/snakemake/snakemake-wrappers/issues/1256)) ([5caa178](https://www.github.com/snakemake/snakemake-wrappers/commit/5caa178fbcbc1dca8444f6a238c868d096b3785a))
* autobump bio/gatk/learnreadorientationmodel ([#1158](https://www.github.com/snakemake/snakemake-wrappers/issues/1158)) ([97cd747](https://www.github.com/snakemake/snakemake-wrappers/commit/97cd7470196fa28fa229361b81cc10466f87b495))
* autobump bio/gatk/leftalignandtrimvariants ([#1205](https://www.github.com/snakemake/snakemake-wrappers/issues/1205)) ([377f253](https://www.github.com/snakemake/snakemake-wrappers/commit/377f2533992ff68f563faed1a37059aeadf041bb))
* autobump bio/gatk/markduplicatesspark ([#1224](https://www.github.com/snakemake/snakemake-wrappers/issues/1224)) ([0893b4e](https://www.github.com/snakemake/snakemake-wrappers/commit/0893b4ec8d1cfecfc2a80c77e6170bbe2bbc981e))
* autobump bio/gatk/mutect ([#1262](https://www.github.com/snakemake/snakemake-wrappers/issues/1262)) ([a01e719](https://www.github.com/snakemake/snakemake-wrappers/commit/a01e7190abb6f08f8fbcd54d886d36b752171165))
* autobump bio/gatk/splitintervals ([#1188](https://www.github.com/snakemake/snakemake-wrappers/issues/1188)) ([2d610dd](https://www.github.com/snakemake/snakemake-wrappers/commit/2d610dd129d1b179ff550932416a0dcec6991cb9))
* autobump bio/gatk/variantannotator ([#1160](https://www.github.com/snakemake/snakemake-wrappers/issues/1160)) ([f7001e2](https://www.github.com/snakemake/snakemake-wrappers/commit/f7001e2c2a6ce9e3fef0fe700bb1a37c56d86c22))
* autobump bio/gatk/variantannotator ([#1282](https://www.github.com/snakemake/snakemake-wrappers/issues/1282)) ([a158262](https://www.github.com/snakemake/snakemake-wrappers/commit/a1582620d1c628988075455fb9e9d1b6f76ea09e))
* autobump bio/gatk3/baserecalibrator ([#1273](https://www.github.com/snakemake/snakemake-wrappers/issues/1273)) ([63e7ae2](https://www.github.com/snakemake/snakemake-wrappers/commit/63e7ae2258533c1bb7676d24e6eb163dcafb1801))
* autobump bio/gatk3/printreads ([#1174](https://www.github.com/snakemake/snakemake-wrappers/issues/1174)) ([22f8e69](https://www.github.com/snakemake/snakemake-wrappers/commit/22f8e696259744d09af4d07053bbe1124f5ca0e5))
* autobump bio/gatk3/printreads ([#1217](https://www.github.com/snakemake/snakemake-wrappers/issues/1217)) ([5d05b88](https://www.github.com/snakemake/snakemake-wrappers/commit/5d05b8828266a4a33dbeb80900faf6f2df971c7d))
* autobump bio/gdc-api/bam-slicing ([#1159](https://www.github.com/snakemake/snakemake-wrappers/issues/1159)) ([96a1a42](https://www.github.com/snakemake/snakemake-wrappers/commit/96a1a42b672bdf9fca9a8e8ef5d140cc02d93753))
* autobump bio/hisat2/align ([#1281](https://www.github.com/snakemake/snakemake-wrappers/issues/1281)) ([a9edff7](https://www.github.com/snakemake/snakemake-wrappers/commit/a9edff748a9eead75e1e43ae5601e7a8c814d221))
* autobump bio/homer/makeTagDirectory ([#1246](https://www.github.com/snakemake/snakemake-wrappers/issues/1246)) ([44847e2](https://www.github.com/snakemake/snakemake-wrappers/commit/44847e2ef5f63c51f03a2370a0d6768dc49fed46))
* autobump bio/last/lastal ([#1165](https://www.github.com/snakemake/snakemake-wrappers/issues/1165)) ([ca0d13f](https://www.github.com/snakemake/snakemake-wrappers/commit/ca0d13fad8396327826d41d394861809305c87d5))
* autobump bio/last/lastdb ([#1254](https://www.github.com/snakemake/snakemake-wrappers/issues/1254)) ([2f11b1e](https://www.github.com/snakemake/snakemake-wrappers/commit/2f11b1e181be6435687bf28ac00c4183ea2868d9))
* autobump bio/lofreq/call ([#1156](https://www.github.com/snakemake/snakemake-wrappers/issues/1156)) ([c750bbf](https://www.github.com/snakemake/snakemake-wrappers/commit/c750bbf2b0fd45abd3d0ba8b926a6cf404b38c0d))
* autobump bio/lofreq/call ([#1275](https://www.github.com/snakemake/snakemake-wrappers/issues/1275)) ([e2c4dc2](https://www.github.com/snakemake/snakemake-wrappers/commit/e2c4dc2e8d79f65af02860f5c762bc2a6a3372ab))
* autobump bio/lofreq/indelqual ([#1283](https://www.github.com/snakemake/snakemake-wrappers/issues/1283)) ([9730460](https://www.github.com/snakemake/snakemake-wrappers/commit/9730460bd457d8b0a8163d49b592d446fe412ae6))
* autobump bio/mashmap ([#1244](https://www.github.com/snakemake/snakemake-wrappers/issues/1244)) ([fad0092](https://www.github.com/snakemake/snakemake-wrappers/commit/fad0092b61dba723b7d653894950121553f5b126))
* autobump bio/microphaser/filter ([#1164](https://www.github.com/snakemake/snakemake-wrappers/issues/1164)) ([8932d38](https://www.github.com/snakemake/snakemake-wrappers/commit/8932d3882426094d0de56fc32c8e9b81a72c37e5))
* autobump bio/minimap2/aligner ([#1177](https://www.github.com/snakemake/snakemake-wrappers/issues/1177)) ([07f4e02](https://www.github.com/snakemake/snakemake-wrappers/commit/07f4e0238bd7c9207aa6c56744dcfe9c5090f7b5))
* autobump bio/open-cravat/module ([#1232](https://www.github.com/snakemake/snakemake-wrappers/issues/1232)) ([be62998](https://www.github.com/snakemake/snakemake-wrappers/commit/be629987465b94a9f616c3754af8349d33dd875a))
* autobump bio/paladin/align ([#1234](https://www.github.com/snakemake/snakemake-wrappers/issues/1234)) ([df3c213](https://www.github.com/snakemake/snakemake-wrappers/commit/df3c213a390bd4a9fdebb809ecf31debef74b8f7))
* autobump bio/picard/collectalignmentsummarymetrics ([#1175](https://www.github.com/snakemake/snakemake-wrappers/issues/1175)) ([856224a](https://www.github.com/snakemake/snakemake-wrappers/commit/856224a4db42aa3ea9937c39745a1c7dfab7ff20))
* autobump bio/picard/collectgcbiasmetrics ([#1247](https://www.github.com/snakemake/snakemake-wrappers/issues/1247)) ([202ab81](https://www.github.com/snakemake/snakemake-wrappers/commit/202ab81a08990a4d9c2b6915130430928c3414e0))
* autobump bio/picard/collecthsmetrics ([#1198](https://www.github.com/snakemake/snakemake-wrappers/issues/1198)) ([874fc3f](https://www.github.com/snakemake/snakemake-wrappers/commit/874fc3f6ab40df13dcc3be0a8f68510c2da555f2))
* autobump bio/picard/collectinsertsizemetrics ([#1190](https://www.github.com/snakemake/snakemake-wrappers/issues/1190)) ([543540a](https://www.github.com/snakemake/snakemake-wrappers/commit/543540aca4afc447f8e22eae8ec01a7a4f143839))
* autobump bio/picard/collectmultiplemetrics ([#1284](https://www.github.com/snakemake/snakemake-wrappers/issues/1284)) ([1e90009](https://www.github.com/snakemake/snakemake-wrappers/commit/1e900096bac6e3e85b4c795ffd0021116106e11a))
* autobump bio/picard/collecttargetedpcrmetrics ([#1203](https://www.github.com/snakemake/snakemake-wrappers/issues/1203)) ([7e55cfc](https://www.github.com/snakemake/snakemake-wrappers/commit/7e55cfc9f208bc95ea50fae9e5d52ccb6cd43998))
* autobump bio/picard/markduplicates ([#1233](https://www.github.com/snakemake/snakemake-wrappers/issues/1233)) ([1708e12](https://www.github.com/snakemake/snakemake-wrappers/commit/1708e127dbd80e5f96bc8224bbcbad7b14daa111))
* autobump bio/picard/mergesamfiles ([#1176](https://www.github.com/snakemake/snakemake-wrappers/issues/1176)) ([554f501](https://www.github.com/snakemake/snakemake-wrappers/commit/554f501f1c04cf90335b39e38d9919af1aa62d20))
* autobump bio/picard/samtofastq ([#1218](https://www.github.com/snakemake/snakemake-wrappers/issues/1218)) ([da9e010](https://www.github.com/snakemake/snakemake-wrappers/commit/da9e0101e9e9be9aa124dc454c43e5196746523e))
* autobump bio/picard/sortsam ([#1248](https://www.github.com/snakemake/snakemake-wrappers/issues/1248)) ([4cf9fdd](https://www.github.com/snakemake/snakemake-wrappers/commit/4cf9fdd2a49cc733f9917ff4c7f2257c770f9bd1))
* autobump bio/pretext/map ([#1227](https://www.github.com/snakemake/snakemake-wrappers/issues/1227)) ([fafa6ee](https://www.github.com/snakemake/snakemake-wrappers/commit/fafa6eeff201564f274ade75a3c1d31b21b575df))
* autobump bio/qualimap/bamqc ([#1251](https://www.github.com/snakemake/snakemake-wrappers/issues/1251)) ([4dc2495](https://www.github.com/snakemake/snakemake-wrappers/commit/4dc249559d4f59e9aec43c2b3757ca0a8fc61adb))
* autobump bio/rbt/csvreport ([#1243](https://www.github.com/snakemake/snakemake-wrappers/issues/1243)) ([25acb2f](https://www.github.com/snakemake/snakemake-wrappers/commit/25acb2f0c99dda2d36da474706dce1f18796022c))
* autobump bio/reference/ensembl-variation ([#1265](https://www.github.com/snakemake/snakemake-wrappers/issues/1265)) ([ede45c7](https://www.github.com/snakemake/snakemake-wrappers/commit/ede45c783b659b54758b4eee9570c8bd76d0a8da))
* autobump bio/samtools/faidx ([#1182](https://www.github.com/snakemake/snakemake-wrappers/issues/1182)) ([c223f0c](https://www.github.com/snakemake/snakemake-wrappers/commit/c223f0c429a41bdf3d10652c5a2286fc6034d4eb))
* autobump bio/samtools/faidx ([#1287](https://www.github.com/snakemake/snakemake-wrappers/issues/1287)) ([511d539](https://www.github.com/snakemake/snakemake-wrappers/commit/511d539680280ec2217e010809d158fa5fca67f9))
* autobump bio/samtools/fixmate ([#1264](https://www.github.com/snakemake/snakemake-wrappers/issues/1264)) ([f42a717](https://www.github.com/snakemake/snakemake-wrappers/commit/f42a717fa58bb3a1b9b442caa4d32b8778830568))
* autobump bio/samtools/flagstat ([#1184](https://www.github.com/snakemake/snakemake-wrappers/issues/1184)) ([4f5349c](https://www.github.com/snakemake/snakemake-wrappers/commit/4f5349cf64c1129ddb81b79cb29e9993f34af193))
* autobump bio/samtools/flagstat ([#1280](https://www.github.com/snakemake/snakemake-wrappers/issues/1280)) ([5fbbbbf](https://www.github.com/snakemake/snakemake-wrappers/commit/5fbbbbff43b98f2f4b9a5908704af9e39c52fd9b))
* autobump bio/samtools/idxstats ([#1193](https://www.github.com/snakemake/snakemake-wrappers/issues/1193)) ([f930f9e](https://www.github.com/snakemake/snakemake-wrappers/commit/f930f9e15ae64f07415fa6a0ba808b7e3ba12765))
* autobump bio/samtools/idxstats ([#1259](https://www.github.com/snakemake/snakemake-wrappers/issues/1259)) ([c6b3b40](https://www.github.com/snakemake/snakemake-wrappers/commit/c6b3b4088f4dea4645e1c95203cacaa400eacd4c))
* autobump bio/samtools/index ([#1214](https://www.github.com/snakemake/snakemake-wrappers/issues/1214)) ([a1ca2a1](https://www.github.com/snakemake/snakemake-wrappers/commit/a1ca2a110b8de164a14aaa9d9964e8681ba95d6b))
* autobump bio/samtools/stats ([#1222](https://www.github.com/snakemake/snakemake-wrappers/issues/1222)) ([0eb7652](https://www.github.com/snakemake/snakemake-wrappers/commit/0eb76529d289920319bd5368294a2c51fbc8834e))
* autobump bio/seqkit/rmdup ([#1162](https://www.github.com/snakemake/snakemake-wrappers/issues/1162)) ([88f74d4](https://www.github.com/snakemake/snakemake-wrappers/commit/88f74d4bc502b3299b40eb127f8eefa7e0554fcf))
* autobump bio/seqkit/stats ([#1213](https://www.github.com/snakemake/snakemake-wrappers/issues/1213)) ([523b69b](https://www.github.com/snakemake/snakemake-wrappers/commit/523b69b193b3e9d5b56964785626f4b07949f7b9))
* autobump bio/snpeff/annotate ([#1189](https://www.github.com/snakemake/snakemake-wrappers/issues/1189)) ([d873ee8](https://www.github.com/snakemake/snakemake-wrappers/commit/d873ee83265f6f34903a6e8d69f574422cb4f6da))
* autobump bio/snpsift/annotate ([#1204](https://www.github.com/snakemake/snakemake-wrappers/issues/1204)) ([8c069ff](https://www.github.com/snakemake/snakemake-wrappers/commit/8c069ff88aadba45c394f55a558a2b70cd3d4735))
* autobump bio/snpsift/genesets ([#1245](https://www.github.com/snakemake/snakemake-wrappers/issues/1245)) ([a2649a7](https://www.github.com/snakemake/snakemake-wrappers/commit/a2649a7e563758599af1834c2871ac19b8c0aa3f))
* autobump bio/snpsift/gwascat ([#1191](https://www.github.com/snakemake/snakemake-wrappers/issues/1191)) ([0c3c051](https://www.github.com/snakemake/snakemake-wrappers/commit/0c3c0519db9a75c78750a26b407bd9d0ebb88741))
* autobump bio/snpsift/gwascat ([#1211](https://www.github.com/snakemake/snakemake-wrappers/issues/1211)) ([53d82b9](https://www.github.com/snakemake/snakemake-wrappers/commit/53d82b92e41bf2eab92bd2eb6c92d10f94e4a09a))
* autobump bio/snpsift/varType ([#1196](https://www.github.com/snakemake/snakemake-wrappers/issues/1196)) ([75bd430](https://www.github.com/snakemake/snakemake-wrappers/commit/75bd430edf46275f075a6b344642dece836532fe))
* autobump bio/snpsift/varType ([#1196](https://www.github.com/snakemake/snakemake-wrappers/issues/1196)) ([eaee058](https://www.github.com/snakemake/snakemake-wrappers/commit/eaee0581606c601eda849d0cbfe255839ae91d46))
* autobump bio/strling/call ([#1216](https://www.github.com/snakemake/snakemake-wrappers/issues/1216)) ([fa539be](https://www.github.com/snakemake/snakemake-wrappers/commit/fa539be3e05ac73058c7dc450719363117014d28))
* autobump bio/strling/extract ([#1272](https://www.github.com/snakemake/snakemake-wrappers/issues/1272)) ([128d8b9](https://www.github.com/snakemake/snakemake-wrappers/commit/128d8b9fcc04b980822a730e7f2c4626e30993b7))
* autobump bio/strling/index ([#1228](https://www.github.com/snakemake/snakemake-wrappers/issues/1228)) ([6cc0059](https://www.github.com/snakemake/snakemake-wrappers/commit/6cc00599fa9dd88d8559501f08fdd691a1b6668c))
* autobump bio/tximport ([#1278](https://www.github.com/snakemake/snakemake-wrappers/issues/1278)) ([f309cb9](https://www.github.com/snakemake/snakemake-wrappers/commit/f309cb98b6bc4fa762d3ba2043612c6e54c5d51f))
* autobump bio/umis/bamtag ([#1260](https://www.github.com/snakemake/snakemake-wrappers/issues/1260)) ([1334743](https://www.github.com/snakemake/snakemake-wrappers/commit/1334743834a811551f799d7e18038a5a546b9dbb))
* autobump bio/varscan/mpileup2indel ([#1186](https://www.github.com/snakemake/snakemake-wrappers/issues/1186)) ([72816c8](https://www.github.com/snakemake/snakemake-wrappers/commit/72816c80df421f1dad58f63559e1671c4b00a5af))
* autobump bio/varscan/mpileup2snp ([#1230](https://www.github.com/snakemake/snakemake-wrappers/issues/1230)) ([0266507](https://www.github.com/snakemake/snakemake-wrappers/commit/0266507d87ed97c4a67bef33cf39362fe32ec174))
* autobump bio/varscan/somatic ([#1178](https://www.github.com/snakemake/snakemake-wrappers/issues/1178)) ([1882608](https://www.github.com/snakemake/snakemake-wrappers/commit/18826087b21fb1f5279cfa8eea349fda58bcd50a))
* autobump bio/vembrane/filter ([#1229](https://www.github.com/snakemake/snakemake-wrappers/issues/1229)) ([1a30d43](https://www.github.com/snakemake/snakemake-wrappers/commit/1a30d43738fccdf0b9bfdc3477adbd4cbb3a8c38))
* autobump bio/vep/plugins ([#1200](https://www.github.com/snakemake/snakemake-wrappers/issues/1200)) ([a7909be](https://www.github.com/snakemake/snakemake-wrappers/commit/a7909be8b31e68c2f933d77b0befaf8bfe005d80))
* autobump bio/vg/construct ([#1226](https://www.github.com/snakemake/snakemake-wrappers/issues/1226)) ([4b2745f](https://www.github.com/snakemake/snakemake-wrappers/commit/4b2745f6ed8d987b355db06af29c62ffa0ad54f4))
* autobump bio/vg/ids ([#1285](https://www.github.com/snakemake/snakemake-wrappers/issues/1285)) ([8ffb3ea](https://www.github.com/snakemake/snakemake-wrappers/commit/8ffb3ea8ba79ce933ec7cf7445065dd4b26e15d1))
* autobump bio/vg/prune ([#1263](https://www.github.com/snakemake/snakemake-wrappers/issues/1263)) ([8a36dec](https://www.github.com/snakemake/snakemake-wrappers/commit/8a36deccdf7750b41625f152843d02e5ef0bd257))
* bump Salmon to v1.10.1 ([#1168](https://www.github.com/snakemake/snakemake-wrappers/issues/1168)) ([a718777](https://www.github.com/snakemake/snakemake-wrappers/commit/a718777f285f175c5f6c67170b6d6440d504184b))

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
