""" 
Ishana Shastri IBM 010820

TODO:
    - visualize graph and components to see what it's actually doing
    - print adjacency matrix for reference
    - try with biconnected components 
    - try with other probabilities for the ER Graph
"""

import networkx as nx 
from pytictoc import TicToc
import matplotlib.pyplot as plt

def components(nodes): #randomize graph and calculate connected components given number of nodes
    G = nx.erdos_renyi_graph(nodes, 0.3)
    t = TicToc()

    #t.tic()
    #create an adjacency matrix.
    #An = (sparse(1:nodes,assig,np.ones(1,nodes),nodes,nodes))

    tables  = nx.connected_components(G)
    largest = max(tables)
    t.tic()
    adj = G.adjacency()

    t.toc()

    return (tables, largest, adj, t.tocvalue())

if __name__ == "__main__":
    times = []
    nodes = list(range(100, 5000, 100))
    for n in nodes:
        [tables, largest, adj, t] = components(n)
        times.append(t)
    fig = plt.figure()
    plt.plot(nodes, times)
    plt.title('NetworkX Test')
    plt.xlabel('# of Nodes')
    plt.ylabel('Time (s)')
    plt.savefig('components_testing/networkx_test_mat.png')

