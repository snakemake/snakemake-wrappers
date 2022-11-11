# Changelog

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
