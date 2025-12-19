import polars as pl

FILENAME = "microbiome.tsv"
OUTPATH = "microbiome.parquet"

df = pl.read_csv(FILENAME, separator="\t")

df.write_parquet(OUTPATH)
print("Success.")

df2 = pl.read_parquet(OUTPATH)

print(df.equals(df2))
