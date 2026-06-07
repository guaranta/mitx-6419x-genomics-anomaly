"""Binomial count model for security incidents — inspired by 6419x exercise12."""

from __future__ import annotations

import numpy as np
from scipy.stats import binom


def incident_pmf(n_observations: int, p_event: float, max_count: int | None = None) -> dict:
    """
    PMF for count of rare events across n_observations.
    Based on 6419x exercise12 parameters (n=63, p=0.00203).
    """
    if max_count is None:
        lo = int(binom.ppf(0.01, n_observations, p_event))
        hi = int(binom.ppf(0.99, n_observations, p_event))
    else:
        lo, hi = 0, max_count

    x = np.arange(lo, hi + 1)
    pmf = binom.pmf(x, n_observations, p_event)
    mean, var = binom.stats(n_observations, p_event)[:2]
    return {
        "x": x,
        "pmf": pmf,
        "mean": float(mean),
        "variance": float(var),
        "n": n_observations,
        "p": p_event,
    }


def alert_threshold(n: int, p: float, alpha: float = 0.01) -> int:
    """Critical value: minimum count to trigger alert at significance alpha."""
    return int(binom.ppf(1 - alpha, n, p))
