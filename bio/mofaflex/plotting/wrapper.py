__author__ = "Simon Sack"
__copyright__ = "Copyright 2026, Simon Sack"
__license__ = "MIT"

from typing import Literal
from collections.abc import Sequence
import mofaflex as mfl
import plotnine as pn


def plot(
    model: mfl.MOFAFLEX,
    training_curve: str | None,
    factor_correlation: str | None,
    variance_explained: str | None,
    top_weights: str | None,
    weights: str | None,
    factors_scatter: str | None,
    factors_scatter_x: int | str,
    factors_scatter_y: int | str,
    weight_factors: int | str | Sequence[int] | Sequence[str] | None,
):
    if training_curve:
        mfl.pl.training_curve(model).save(training_curve)

    if factor_correlation:
        mfl.pl.factor_correlation(model).save(factor_correlation)

    if variance_explained:
        mfl.pl.variance_explained(model).save(variance_explained)

    if top_weights:
        mfl.pl.top_weights(model, figsize=(10, 10)).save(top_weights)

    if weights:
        mfl.pl.weights(model, factors=weight_factors, figsize=(10, 10)).save(weights)

    if factors_scatter:
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

    training_curve = snakemake.output.get("training_curve")
    factor_correlation = snakemake.output.get("factor_correlation")
    variance_explained = snakemake.output.get("variance_explained")
    top_weights = snakemake.output.get("top_weights")
    weights = snakemake.output.get("weights")
    factors_scatter = snakemake.output.get("factors_scatter")

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
