import networkx as nx

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
