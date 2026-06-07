"""Generate README figures."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / "pca-anomaly"))
sys.path.insert(0, str(ROOT / "regression"))

from log_anomaly import detect_anomalies  # noqa: E402
from kpi_regression import kpi_regression  # noqa: E402

# Binomial PMF (6419x exercise12 params)
n, p = 63, 0.00203
x = np.arange(0, 6)
pmf = binom.pmf(x, n, p)
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(x, pmf, color="#0ea5e9", edgecolor="white")
ax.axvline(1, color="#ef4444", ls="--", label="Alert threshold (α=1%)")
ax.set_xlabel("Incident count per window")
ax.set_ylabel("P(X=k)")
ax.set_title(f"Binomial({n}, {p:.5f}) — rare event model (SOC)")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "binomial_pmf.png", dpi=150)
plt.close()

# PCA anomaly
rng = np.random.default_rng(42)
normal = rng.normal(0, 1, (200, 50))
anomalies = rng.normal(5, 2, (10, 50))
features = np.vstack([normal, anomalies])
result = detect_anomalies(features, n_components=5, contamination=0.08)
proj = result["projected"]
fig, ax = plt.subplots(figsize=(7, 5))
colors = np.where(result["is_anomaly"], "#ef4444", "#3b82f6")
ax.scatter(proj[:, 0], proj[:, 1], c=colors, alpha=0.7, s=30, edgecolors="white", linewidths=0.3)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA projection — blue=normal, red=anomaly")
fig.tight_layout()
fig.savefig(OUT / "pca_anomaly.png", dpi=150)
plt.close()

# Regression
rng = np.random.default_rng(0)
mttr = rng.uniform(5, 60, 100)
downtime = 2.0 * mttr + rng.normal(0, 10, 100)
reg = kpi_regression(mttr, downtime)
x_line = np.linspace(mttr.min(), mttr.max(), 100)
y_line = reg["intercept"] + reg["slope"] * x_line
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(mttr, downtime, alpha=0.6, color="#6366f1", s=25)
ax.plot(x_line, y_line, color="#ef4444", lw=2, label=f"ŷ = {reg['intercept']:.1f} + {reg['slope']:.2f}·MTTR")
ax.set_xlabel("MTTR (min)")
ax.set_ylabel("Downtime (min)")
ax.set_title(f"KPI regression — R²={reg['r_squared']:.3f}, r={reg['correlation']['pearson_r']:.3f}")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "kpi_regression.png", dpi=150)
plt.close()

print(f"Saved 3 figures to {OUT}")
