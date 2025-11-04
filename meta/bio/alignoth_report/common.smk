import pandas as pd

def get_alignoth_tables(wildcards, results_dir):
    count = count_variants(wildcards)
    return [f"{results_dir}/alignoth/{{sample}}/{i}/" for i in range(count)]


def count_variants(wildcards):
    return sum(1 for _ in open(checkpoints.vembrane_table.get(sample=wildcards.sample).output[0], "r")) - 1
