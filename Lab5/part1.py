import networkx as nx
import matplotlib.pyplot as plt

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

# Compute the diameter
def diameter(G):
    """
    Calculates the diameter of a graph.
    """
    nodes = G.nodes
    nodes=list(nodes)
    maxPathFromNode=[]
    for i in range(0, len(nodes)):
        pathFromNode=[]
        for j in range(0, len(nodes)):
            if i==j:
                continue
            distance = nx.shortest_path_length(G, source=nodes[i], target=nodes[j])
            pathFromNode.append(distance)
        maxPathFromNode.append(max(pathFromNode))

    return max(maxPathFromNode)


# Clustering Coefficient
def clustering_coefficient(G, node):
    """
    Calculates the clustering coefficient of a node in a graph.
    """

    neighbors = G.neighbors(node)
    k = len(list(neighbors))
    if k <= 1:
        return 0

    edges = len([(u, v) for u, v in G.edges(node) if u != v])
    return 2 * edges / k * (k - 1)


def average_clustering_coefficient(G):
    """
    Calculates the average clustering coefficient of a graph.
    """

    ccs = [clustering_coefficient(G, node) for node in G.nodes()]
    return sum(ccs) / len(ccs)

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