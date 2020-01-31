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

from graph_tool.all import *
import time
import numpy as np
import matplotlib.pyplot as plt

def components(G): #randomize graph and calculate connected components given number of nodes
    #G = Graph.random_graph(nodes, random=True, directed=True, self_loops=True, model="erdos")
    t0 = time.process_time()
    #create an adjacency matrix.
    #An = (sparse(1:nodes,assig,np.ones(1,nodes),nodes,nodes))

    tables = label_components(G)
    largest = max(tables)

    t1 = time.process_time()

    return (tables, largest, t1-t0)

if __name__ == "__main__":
    gtimes = []
    nodes = list(range(100, 1000, 100))
    
    for n in nodes: 
        pointers = np.random.choice(n, n, replace=False) #generate random graph as a vector of pointers corresponding to edges
        edges = []

        for i in range(0,len(pointers)): #relabel pointers to begin from 1
            pointers[i]+=1
        for p in range(0, len(pointers)):
            edges.append((p+1, pointers[p]))
        adj = np.zeros((n,n)) #create n x n sparse matrix 
        for i in range(0, len(adj)): #add ones to create adjacency matrix
            #print((edges[i][0], edges[i][1]))
            adj[edges[i][0]-1,edges[i][1]-1]=1

        adj = np.maximum(adj, adj.transpose()) #make symmetric (undirected)        
  
        gG = Graph()
        gG.add_edge_list(edges)
        
        [gtables, glargest, gt] = components(gG)
        gtimes.append(gt) 

    fig = plt.figure()
    plt.plot(nodes, gtimes)
    plt.title('Graph-Tool Test')
    plt.xlabel('# of Nodes')
    plt.ylabel('CPU Time (s)')
    plt.savefig('components_testing/graphtool_test.png')

