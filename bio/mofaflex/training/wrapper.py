__author__ = "Simon Sack"
__copyright__ = "Copyright 2026, Simon Sack"
__license__ = "MIT"

from io import BufferedWriter
from typing import Literal
import mudata as md
import mofaflex as mfl
from pathlib import Path
import pickle as p


def train_model(
    mdata: md.MuData | md.AnnData,
    out_path: Path,
    n_factors: int = 15,
    likelihoods: Literal["Normal", "NegativeBinomial", "Binomial"] = "Normal",
    batch_size: int = 1000,
    seed: int = 42,
) -> mfl.MOFAFLEX:
    model = mfl.MOFAFLEX(
        mdata,
        mfl.ModelOptions(n_factors=n_factors, likelihoods=likelihoods),
        mfl.TrainingOptions(batch_size=batch_size, seed=seed, save_path=out_path),
        mfl.DataOptions(plot_data_overview=False),
    )
    return model


# def store_model(model: mfl.MOFAFLEX, file: BufferedWriter):
#     p.dump(model, file)


if __name__ == "__main__":
    mdata_path: Path = Path(snakemake.input[0])
    out_path: Path = Path(snakemake.output[0])

    mdata: md.MuData | md.AnnData = md.MuData()

    if mdata_path.suffix == ".h5mu":
        mdata = md.read_h5mu(mdata_path)
    elif mdata_path.suffix == ".h5ad":
        mdata = md.read_h5ad(mdata_path)
    else:
        raise Exception("Illegal file format. Must be h5mu or h5ad.")

    n_factors: int = snakemake.params.get("n_factors", 15)
    likelihoods: Literal["Normal", "NegativeBinomial", "Binomial"] = (
        snakemake.params.get("likelihoods", "Normal")
    )
    batch_size: int = snakemake.params.get("batch_size", 1000)
    seed: int = snakemake.params.get("seed", 42)

    model: mfl.MOFAFLEX = train_model(
        mdata=mdata,
        out_path=out_path,
        n_factors=n_factors,
        likelihoods=likelihoods,
        batch_size=batch_size,
        seed=seed,
    )

    # with open(out_path, "wb") as file:
    #     store_model(model, file)
