from ftplib import FTP

with FTP("ftp.ncbi.nlm.nih.gov") as ftp, open(snakemake.output[0], "wb") as out:
    ftp.login()
    ftp.storbinary(
        "STOR snp/organisms/{params.organism}/VCF/All_{params.release}.vcf.gz".format(
            params=snakemake.params
        ),
        out,
    )
