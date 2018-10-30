from snakemake.remote import HTTP

https = HTTP.RemoteProvider(allow_redirects=True)


rule haplotype_caller:
    input:
        vcf=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/phase1.projectConsensus.chr20.1M-10M.raw.snps.vcf"),
        ref=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/human_g1k_v37.20.21.fasta"),
        aux=[https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/human_g1k_v37.20.21.dict"),
             https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/human_g1k_v37.20.21.fasta.fai"),
             https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/ALL.wgs.indels_mills_devine_hg19_leftAligned_collapsed_double_hit.sites.20.1M-10M.vcf.idx"),
             https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/Omni25_sites_1525_samples.b37.20.1M-10M.vcf.idx"),
             https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/combined.phase1.chr20.raw.indels.filtered.sites.1M-10M.vcf.idx"),
             https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/dbsnp_132_b37.leftAligned.20.1M-10M.vcf.idx")],
        mills=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/ALL.wgs.indels_mills_devine_hg19_leftAligned_collapsed_double_hit.sites.20.1M-10M.vcf"),
        omni=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/Omni25_sites_1525_samples.b37.20.1M-10M.vcf"),
        g1k=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/combined.phase1.chr20.raw.indels.filtered.sites.1M-10M.vcf"),
        dbsnp=https.remote("github.com/broadinstitute/gatk/raw/4.0.5.2/src/test/resources/large/VQSR/dbsnp_132_b37.leftAligned.20.1M-10M.vcf")
    output:
        vcf="calls/all.recal.vcf",
        tranches="calls/all.tranches"
    log:
        "logs/gatk/variantrecalibrator.log"
    params:
        mode="SNP",  # set mode, must be either SNP, INDEL or BOTH
        resources={"mills": {"known": False, "training": True, "truth": True, "prior": 15.0},
                   "omni":   {"known": False, "training": True, "truth": False, "prior": 12.0},
                   "g1k":   {"known": False, "training": True, "truth": False, "prior": 10.0},
                   "dbsnp":  {"known": True, "training": False, "truth": False, "prior": 2.0}},
        annotation=["SB"],
        extra="--max-gaussians 4",  # optional
    wrapper:
        "master/bio/gatk/variantrecalibrator"
