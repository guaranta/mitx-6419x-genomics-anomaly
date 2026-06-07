"""Demo: PCA anomaly detection on synthetic log features."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from log_anomaly import detect_anomalies

if __name__ == "__main__":
    np.random.seed(42)
    normal = np.random.normal(0, 1, (200, 50))
    anomalies = np.random.normal(5, 2, (10, 50))
    features = np.vstack([normal, anomalies])

    result = detect_anomalies(features, n_components=5, contamination=0.08)
    print(f"Samples: {len(features)}, anomalies flagged: {result['n_anomalies']}")
    print(f"Explained variance (top 5): {result['explained_variance_ratio'][:3]}")
