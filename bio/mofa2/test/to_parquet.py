import polars as pl

FILENAME = "data.tsv"
OUTPATH = "data.parquet"

df = pl.read_csv(FILENAME, separator="\t")
df2 = pl.read_parquet(OUTPATH)

print(df.equals(df2))

# df.write_parquet(OUTPATH)
# print("Success.")
