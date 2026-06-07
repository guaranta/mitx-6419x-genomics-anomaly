"""PCA + clustering for high-dimensional log anomaly detection."""

from __future__ import annotations

import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def detect_anomalies(
    features: np.ndarray,
    n_components: int = 10,
    n_clusters: int = 3,
    contamination: float = 0.05,
    seed: int = 42,
) -> dict:
    """
    PCA → k-means → flag points far from assigned centroid.
    Genomics-inspired pipeline applied to log feature matrices.
    """
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    pca = PCA(n_components=min(n_components, scaled.shape[1]))
    projected = pca.fit_transform(scaled)

    km = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    labels = km.fit_predict(projected)
    dists = np.linalg.norm(projected - km.cluster_centers_[labels], axis=1)
    threshold = np.percentile(dists, 100 * (1 - contamination))
    is_anomaly = dists > threshold

    return {
        "projected": projected,
        "labels": labels,
        "distances": dists,
        "is_anomaly": is_anomaly,
        "n_anomalies": int(is_anomaly.sum()),
        "explained_variance_ratio": pca.explained_variance_ratio_.tolist(),
    }
