import variables as var
import numpy as np
from PIL import Image

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def rgba_list_to_3d_points(rgba_list, normalize=True, scale=1.0):
    """
    Konvertiert eine flache RGBA-Liste oder eine 2D-Liste von RGBA-Werten
    in 3D-Koordinaten (RGB) und filtert unsichtbare Pixel heraus.
    """
    rgba_array = np.array(rgba_list, dtype=np.float64)
    
    # Falls die Liste flach ist (1D), formatiere sie zu (N, 4) um
    if rgba_array.ndim == 1:
        if rgba_array.size % 4 != 0:
            raise ValueError('Die flache RGBA-Liste muss eine Länge aufweisen, die durch 4 teilbar ist.')
        rgba_array = rgba_array.reshape((-1, 4))
    
    if rgba_array.ndim != 2 or rgba_array.shape[1] != 4:
        raise ValueError('Erwartet ein Array mit dem Shape (N, 4) oder eine flache RGBA-Liste.')
    
    # Filtert komplett transparente Pixel heraus (Alpha > 0)
    mask = rgba_array[:, 3] > 0
    visible_rgba = rgba_array[mask]
    
    # Nutze nur die RGB-Kanäle als 3D-Punkte
    points = visible_rgba[:, :3]
    
    if normalize:
        points /= 255.0
    points *= scale
    
    return points

def estimate_k(points, k_min=2, k_max=12):
    unique_point_count = len(np.unique(points, axis=0))
    k_max = min(k_max, unique_point_count)

    if k_max < k_min:
        return k_max

    best_k = k_min
    best_score = -1

    for k in range(k_min, k_max + 1):
        model = KMeans(n_clusters=k, n_init='auto', random_state=42)
        labels = model.fit_predict(points)

        if len(np.unique(labels)) < 2:
            continue

        score = silhouette_score(points, labels)

        if score > best_score:
            best_score = score
            best_k = k

    return best_k

def cluster_points(points, min_cluster_size=10, k=None):
    unique_point_count = len(np.unique(points, axis=0))
    if unique_point_count == 0:
        return np.array([]), np.array([]), 0
        
    if k is None:
        k = estimate_k(points)
    k = min(k, unique_point_count)

    if k < 1:
        return np.array([]), np.array([]), 0

    model = KMeans(n_clusters=k, n_init='auto', random_state=42)
    labels = model.fit_predict(points)

    unique_labels, counts = np.unique(labels, return_counts=True)
    valid_clusters = unique_labels[counts >= min_cluster_size]

    mask = np.isin(labels, valid_clusters)
    filtered_points = points[mask]
    filtered_labels = labels[mask]

    return filtered_points, filtered_labels, k

def compute_cluster_means(points, labels):
    unique_labels = np.unique(labels)
    means = []

    for label in unique_labels:
        cluster_points = points[labels == label]
        mean_point = cluster_points.mean(axis=0)
        means.append(mean_point)

    return np.array(means)

def merge_close_midpoints(midpoints, threshold=0.1):
    if len(midpoints) <= 1:
        return np.array(midpoints).tolist()
    
    merged = []
    used = set()
    
    for i, mp1 in enumerate(midpoints):
        if i in used:
            continue
        current_cluster = [mp1]
        for j, mp2 in enumerate(midpoints):
            if i != j and j not in used:
                dist = np.linalg.norm(np.array(mp1) - np.array(mp2))
                if dist < threshold:
                    current_cluster.append(mp2)
                    used.add(j)
        
        merged.append(np.mean(current_cluster, axis=0).tolist())
        used.add(i)
        
    return merged

def find_positions(rgba_list, name):
    """
    Hauptfunktion: Akzeptiert die neue flache RGBA-Liste, wandelt sie in 3D-Punkte um,
    clustert diese und gibt die gemittelten Farbmittelpunkte zurück.
    """
    # 1. Konvertiere die RGBA-Liste in 3D-Punkte (RGB)
    points = rgba_list_to_3d_points(rgba_list, normalize=True, scale=1.0)
    
    min = len(points) / 7

    if points.shape[0] == 0:
        print(f'no visibles found in {name}')
        return []

    # 2. Clustere die Punkte anhand ihrer Farbwerte
    filtered_points, labels, k = cluster_points(
        points,
        min_cluster_size=min
    )
    
    if filtered_points.shape[0] == 0:
        print(f'no clusters bigeer than {min} in {name}')
        return []
        
    # 3. Berechne die Durchschnittsfarben der Cluster
    midpoints = compute_cluster_means(filtered_points, labels)
    
    # 4. Verschmelze nahe beieinanderliegende Farbmittelpunkte
    return merge_close_midpoints(midpoints, threshold=0.1)


if __name__ == "__main__":
    pass
