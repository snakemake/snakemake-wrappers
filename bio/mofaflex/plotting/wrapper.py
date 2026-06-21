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
    results_dir_exists: bool = False

    if training_curve is not None:
        if not results_dir_exists:
            training_curve.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        t_curve: pn.ggplot = mfl.pl.training_curve(model)
        t_curve.save(training_curve)

    if factor_correlation is not None:
        if not results_dir_exists:
            factor_correlation.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        factor_corr: pn.ggplot = mfl.pl.factor_correlation(model)
        factor_corr.save(factor_correlation)

    if variance_explained is not None:
        if not results_dir_exists:
            variance_explained.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        var_expl: pn.ggplot = mfl.pl.variance_explained(model)
        var_expl.save(variance_explained)

    if top_weights is not None:
        if not results_dir_exists:
            top_weights.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        top_w: pn.ggplot = mfl.pl.top_weights(model, figsize=(10, 10))
        top_w.save(top_weights)

    if weights is not None:
        if not results_dir_exists:
            weights.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        w: pn.ggplot = mfl.pl.weights(model, factors=(1, 2), figsize=(10, 10))
        w.save(weights)

    if factors_scatter is not None:
        if not results_dir_exists:
            factors_scatter.parent.mkdir(exist_ok=True)
            results_dir_exists = True
        f_scatter: pn.ggplot = mfl.pl.factors_scatter(
            model, factors_scatter_x, factors_scatter_y, alpha=0.5
        )
        f_scatter.save(factors_scatter)


if __name__ == "__main__":
    model_path: Path = Path(snakemake.input[0])

    model: mfl.MOFAFLEX = mfl.MOFAFLEX.load(model_path)

    n_factors: int = snakemake.params.get("n_factors", 15)
    likelihoods: Literal["Normal", "NegativeBinomial", "Binomial"] = (
        snakemake.params.get("likelihoods", "Normal")
    )
    batch_size: int = snakemake.params.get("batch_size", 1000)
    seed: int = snakemake.params.get("seed", 42)

    training_curve: Path = Path(snakemake.output.get("training_curve"))
    factor_correlation: Path = Path(snakemake.output.get("factor_correlation"))
    variance_explained: Path = Path(snakemake.output.get("variance_explained"))
    top_weights: Path = Path(snakemake.output.get("top_weights"))
    weights: Path = Path(snakemake.output.get("weights"))
    factors_scatter: Path = Path(snakemake.output.get("factors_scatter"))

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
