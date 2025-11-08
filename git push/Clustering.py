import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = np.array([
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0],
    [8.0, 2.0],
    [10.0, 2.0],
    [9.0, 3.0]
])

# Given centroids
centroids = np.array([
    [1.0, 1.0],  # centroid 1
    [8.0, 9.0]   # centroid 2
])

# Function to compute Euclidean distance and assign clusters
def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = np.linalg.norm(point - centroids, axis=1)
        cluster = np.argmin(distances)  # Index of closest centroid
        clusters.append(cluster)
    return np.array(clusters)  # <-- Moved outside the loop

# Assign clusters
clusters = assign_clusters(data, centroids)

# Visualize result
colors = ['r', 'b']
for i in range(len(centroids)):
    plt.scatter(data[clusters == i][:, 0], data[clusters == i][:, 1], c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[i][0], centroids[i][1], c='black', marker='x', s=200)
plt.title("Clustering with Given Centroids")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
