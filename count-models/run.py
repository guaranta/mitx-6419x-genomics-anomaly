"""Demo: binomial incident count model."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from incident_counts import alert_threshold, incident_pmf

if __name__ == "__main__":
    # 6419x exercise12 params adapted to SOC context
    n, p = 63, 0.00203
    result = incident_pmf(n, p)
    print(f"Binomial({n}, {p})")
    print(f"  E[X] = {result['mean']:.4f}, Var = {result['variance']:.4f}")
    print(f"  Alert threshold (α=1%): {alert_threshold(n, p)} events")
