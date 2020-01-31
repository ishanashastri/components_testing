""" 
Ishana Shastri IBM 010820

TODO:
    - visualize graph and components to see what it's actually doing
    - print adjacency matrix for reference
    - make sure tic toc isn't cumulative
    - replot and don't touch computer 
    - try with biconnected components 
    - try with other probabilities for the ER Graph
"""

from igraph import *
from pytictoc import TicToc
import matplotlib.pyplot as plt

def components(nodes): #randomize graph and calculate connected components given number of nodes
    G = Graph.Erdos_Renyi(nodes, p=0.3)
    t = TicToc()

    #create an adjacency matrix.
    #An = (sparse(1:nodes,assig,np.ones(1,nodes),nodes,nodes))

    tables  = G.components(mode=WEAK)
    largest = max(tables)
    t.tic()
    adj = G.get_adjacency()

    t.toc()

    return (tables, largest, adj, t.tocvalue())

if __name__ == "__main__":
    times = []
    nodes = list(range(100, 5000, 100))
    for n in nodes:
        [tables, largest, adj, t] = components(n)
        times.append(t)
    plt.plot(nodes, times)
    plt.title('IGraph Test')
    plt.xlabel('# of Nodes')
    plt.ylabel('Time (s)')
    plt.savefig('components_testing/igraph_test_mat.png')
    plt.show()



