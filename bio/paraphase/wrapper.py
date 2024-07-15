import glob
import sys
from snakemake.shell import shell
from tempfile import TemporaryDirectory
import shutil

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

try:
    with TemporaryDirectory() as tmpdirname:
        
        ### Run paraphase
        shell(
            f"""
            (paraphase --bam {snakemake.input.bam} \
            --reference {snakemake.input.fasta} \
            --out {tmpdirname} \
            {snakemake.params.genome} \
            {extra}) {log}
            """,
            tmpdirname=tmpdirname  # Pass tmpdirname to the shell environment
        )
        shell ("""
            touch {snakemake.output.vcf_header} {snakemake.output.merged_vcf} {snakemake.output.vcf_header} {snakemake.output.bam} {snakemake.output.bai}
            """
        )

        ### Create a new VCF header

        # Get the paths from Snakemake input and output objects
        input_faidx = snakemake.input.faidx
        output_vcf_header = snakemake.output.vcf_header

        # Open the .fai index file and read lines
        with open(input_faidx, 'r') as fai_file:
            lines = fai_file.readlines()
        fai_file.close()

        # Open the output file and write formatted header lines
        with open(output_vcf_header, 'w') as output:
            for line in lines:
                contig_id, length = line.split()[:2]  # Assuming the first two elements are ID and length
                output.write(f"##contig=<ID={contig_id},length={length}>\n")
        output.close()

        ### Concatenating, reheadering, and sorting the zipped and indexed VCF files, and copy the remapped reads
        vcf_res = glob.glob(f"{tmpdirname}/*_vcfs/*vcf")
        if vcf_res:
            for vcf in vcf_res:
                bgzip_cmd = f"bgzip -c {vcf} > {vcf}.gz"
                shell(bgzip_cmd)
                index_cmd = f"bcftools index {vcf}.gz"
                shell(index_cmd)
                print(f"Compressed and indexed: {vcf}.gz")

            params_variant_files = " ".join([f"{vcf}.gz" for vcf in vcf_res])
            shell(
                f"bcftools concat -a -Oz {params_variant_files} | "
                f"bcftools annotate --header-lines {snakemake.output.vcf_header} | "
                f"bcftools sort -Oz -o {snakemake.output.merged_vcf}"
            )
            print(f"Merged, reheadered, and sorted VCF file created: {snakemake.output.merged_vcf}")
            
            # Copy out bam and bai files
            bam_res = glob.glob(f"{tmpdirname}/*.bam")
            bai_res = glob.glob(f"{tmpdirname}/*.bai")
            #print("BAM RES: ", bam_res, bai_res)
            shell(
                f"""
                cp -pr {' '.join(bam_res)} {snakemake.output.bam};
                cp -pr {' '.join(bai_res)} {snakemake.output.bai}
                """
            )
        else:
            print("No output VCF or BAM files were produced by paraphase, I hope this is what you were expecting, human?")
            shell(f"touch {snakemake.output.merged_vcf}")

except Exception as e:
    print(f"Error running paraphase: {e}")
    sys.exit(1)


""" Slut """



