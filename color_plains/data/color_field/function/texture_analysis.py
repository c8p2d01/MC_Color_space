import variables as var
import numpy as np
from PIL import Image

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def load_png_pixel_data(path):
    image = Image.open(path).convert('RGB')
    return np.array(image)

def rgb_to_3d_points(pixel_array, normalize=True, scale=1.0):
    if pixel_array.ndim != 3 or pixel_array.shape[2] != 3:
        raise ValueError('Expected RGB pixel array with shape (H, W, 3)')
    points = pixel_array.reshape((-1, 3)).astype(np.float64)
    if normalize:
        points /= 255.0
    points *= scale
    return points

#
# Currently using KMeans to determine positions
#

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
    if k is None:
        k = estimate_k(points)
    k = min(k, unique_point_count)

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
        return midpoints
    
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

def find_positions(texture_list):
    midpoints = []
    points = []
    for texture in texture_list:
        try:
            pixs = load_png_pixel_data(var.texture_folder + "block/" + texture)
            pts = rgb_to_3d_points(pixs, normalize=True, scale=1.0)
            points.append(pts)
          #  break # if break here then this is effectively only checking the first texture
        except Exception as e:
            print(f"eeee{e}\t>{texture}<")
    if points:
        combined_points = np.concatenate(points, axis=0)
        filtered_points, labels, k = cluster_points(
            combined_points,
            min_cluster_size=25
        )
        unique_labels = np.unique(labels)
        midpoints = compute_cluster_means(filtered_points, labels)
        return (merge_close_midpoints(midpoints))
    return ([])

if __name__ == "__main__":
    pass
