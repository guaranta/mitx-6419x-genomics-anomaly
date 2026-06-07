"""Correlation and regression for operational KPIs."""

from __future__ import annotations

import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression


def correlation_report(x: np.ndarray, y: np.ndarray) -> dict:
    """Pearson correlation with p-value."""
    r, p = stats.pearsonr(x, y)
    return {"pearson_r": float(r), "p_value": float(p)}


def kpi_regression(x: np.ndarray, y: np.ndarray) -> dict:
    """Simple OLS: y = β₀ + β₁x."""
    x_2d = x.reshape(-1, 1)
    model = LinearRegression().fit(x_2d, y)
    y_pred = model.predict(x_2d)
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return {
        "intercept": float(model.intercept_),
        "slope": float(model.coef_[0]),
        "r_squared": float(r2),
        "correlation": correlation_report(x, y),
    }
