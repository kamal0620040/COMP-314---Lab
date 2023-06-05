import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict
import collections


from reused import average_clustering_coefficient, diameter

networks = [
    nx.read_edgelist('Data/rt_justinbieber.edges', delimiter=',', nodetype=int, data=(('timestamp', int),)),
    nx.read_edgelist('Data/rt_onedirection.edges',delimiter=',', nodetype=int, data=(('timestamp', int),)),
    nx.read_edgelist('Data/rt_saudi.edges',delimiter=',', nodetype=int, data=(('timestamp', int),)),
    nx.read_edgelist('Data/rt_alwefaq.edges',delimiter=',', nodetype=int, data=(('timestamp', int),)),
    nx.read_edgelist('Data/rt_libya.edges',delimiter=',', nodetype=int, data=(('timestamp', int),)),
]

# Compute the network properties
for network in networks:
    num_nodes = len(network.nodes())
    num_edges = len(network.edges())
    avg_degree = num_edges / num_nodes
    density = 2 * num_edges / (num_nodes * (num_nodes - 1)) if num_nodes > 1 else 0
    # diameter = nx.diameter(network)
    clustering_coefficient = average_clustering_coefficient(network)

    print("Number of nodes:", num_nodes)
    print("Number of edges:", num_edges)
    print("Average degree:", avg_degree)
    print("Density:", density)
    # print("Diameter:", diameter)
    print("Clustering coefficient:", clustering_coefficient)
    # print(calculate_degree_distribution(network))



for network in networks:
    degree_sequence = sorted([d for n, d in network.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="r")
    plt.title("Degree Distribution")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.show()
