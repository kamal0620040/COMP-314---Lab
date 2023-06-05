import networkx as nx
import matplotlib.pyplot as plt

from reused import average_clustering_coefficient, diameter

# Inport the data
G = nx.read_edgelist('Data/mammalia-dolphin-social.edges')

# Compute the number of nodes and edges
num_nodes = len(G.nodes())
num_edges = len(G.edges())

# Compute the average degree
avg_degree = num_edges / num_nodes

# Compute the density
# Length of the shortest path between the most distanced nodes.
density = 2 * num_edges / (num_nodes * (num_nodes - 1)) if num_nodes > 1 else 0


# Compute the clustering coefficient
clustering_coefficient = average_clustering_coefficient(G)

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Average degree:", avg_degree)
print("Density:", density)
print("Diameter:", diameter(G))
print("Clustering coefficient:",clustering_coefficient)

# Draw the graph
plt.figure()
nx.draw(G, with_labels=True)
plt.show()