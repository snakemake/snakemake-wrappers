__author__ = "Simon Sack"
__copyright__ = "Copyright 2026, Simon Sack"
__license__ = "MIT"

from typing import Literal
from collections.abc import Sequence
import mofaflex as mfl
from pathlib import Path
import plotnine as pn


def plot(
    model: mfl.MOFAFLEX,
    training_curve: Path | None,
    factor_correlation: Path | None,
    variance_explained: Path | None,
    top_weights: Path | None,
    weights: Path | None,
    factors_scatter: Path | None,
    factors_scatter_x: int | str,
    factors_scatter_y: int | str,
    weight_factors: int | str | Sequence[int] | Sequence[str] | None,
):
    if training_curve is not None:
        mfl.pl.training_curve(model).save(training_curve)

    if factor_correlation is not None:
        mfl.pl.factor_correlation(model).save(factor_correlation)

    if variance_explained is not None:
        mfl.pl.variance_explained(model).save(variance_explained)

    if top_weights is not None:
        mfl.pl.top_weights(model, figsize=(10, 10)).save(top_weights)

    if weights is not None:
        mfl.pl.weights(model, factors=weight_factors, figsize=(10, 10)).save(weights)

    if factors_scatter is not None:
        mfl.pl.factors_scatter(
            model, factors_scatter_x, factors_scatter_y, alpha=0.5
        ).save(factors_scatter)


if __name__ == "__main__":
    model: mfl.MOFAFLEX = mfl.MOFAFLEX.load(snakemake.input[0])

    n_factors: int = snakemake.params.get("n_factors", 15)
    likelihoods: Literal["Normal", "NegativeBinomial", "Binomial"] = (
        snakemake.params.get("likelihoods", "Normal")
    )
    batch_size: int = snakemake.params.get("batch_size", 1000)
    seed: int = snakemake.params.get("seed", 42)

    training_curve_raw = snakemake.output.get("training_curve")
    factor_correlation_raw = snakemake.output.get("factor_correlation")
    variance_explained_raw = snakemake.output.get("variance_explained")
    top_weights_raw = snakemake.output.get("top_weights")
    weights_raw = snakemake.output.get("weights")
    factors_scatter_raw = snakemake.output.get("factors_scatter")

    training_curve: Path | None = (
        Path(training_curve_raw) if training_curve_raw is not None else None
    )
    factor_correlation: Path | None = (
        Path(factor_correlation_raw) if factor_correlation_raw is not None else None
    )
    variance_explained: Path | None = (
        Path(variance_explained_raw) if variance_explained_raw is not None else None
    )
    top_weights: Path | None = (
        Path(top_weights_raw) if top_weights_raw is not None else None
    )
    weights: Path | None = Path(weights_raw) if weights_raw is not None else None
    factors_scatter: Path | None = (
        Path(factors_scatter_raw) if factors_scatter_raw is not None else None
    )

    factors_scatter_x: int | str = snakemake.params.get("factors_scatter_x", 1)
    factors_scatter_y: int | str = snakemake.params.get("factors_scatter_y", 2)
    weight_factors: int | str | Sequence[int] | Sequence[str] | None = (
        snakemake.params.get("weight_factors")
    )

    plot(
        model,
        training_curve,
        factor_correlation,
        variance_explained,
        top_weights,
        weights,
        factors_scatter,
        factors_scatter_x,
        factors_scatter_y,
        weight_factors,
    )
