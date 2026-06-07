"""Demo: KPI regression."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from kpi_regression import kpi_regression

if __name__ == "__main__":
    np.random.seed(0)
    mttr = np.random.uniform(5, 60, 100)  # minutes
    downtime = 2.0 * mttr + np.random.normal(0, 10, 100)
    result = kpi_regression(mttr, downtime)
    print(f"MTTR → Downtime: slope={result['slope']:.3f}, R²={result['r_squared']:.3f}")
    print(f"Pearson r={result['correlation']['pearson_r']:.3f}, p={result['correlation']['p_value']:.4f}")
