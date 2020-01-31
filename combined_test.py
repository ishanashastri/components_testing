# Ishana Shastri 
# IBM 010920
# Compare the efficiency of the NetworkX and iGraph Python libraries for graph algorithms

import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import igraph as ig
from graph_tool.all import *


def nComponents(G): 
    t0 = time.clock()
    tables  = nx.connected_components(G)
    largest = max(tables)
    t1 = time.clock()
    return (tables, largest, t1-t0)

def iComponents(G): 
    t0 = time.clock()
    tables  = ig.Graph().components(G, mode=WEAK)
    largest = max(tables)
    t1 = time.clock()
    return (tables, largest, t1-t0)

def gComponents(G):
    t0 = time.clock()
    tables  = label_components(G)
    #largest = max(tables)
    t1 = time.clock()
    return (tables, t1-t0)

if __name__ == "__main__":
    ntimes = []
    itimes = []
    gtimes = []
    nodes = list(range(100, 5000, 100))

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
        
        nG = nx.from_numpy_matrix(np.matrix(adj))
        iG = ig.Graph.Adjacency(adj.tolist())
        gG = Graph()
        gG.add_edge_list(edges)

        [ntables, nlargest, nt] = nComponents(nG)
        ntimes.append(nt)
    
        [itables, ilargest, it] = iComponents(iG)
        itimes.append(it)

        [gtables, gt] = gComponents(gG)
        gtimes.append(gt)


    fig = plt.figure()
    plt.plot(nodes, ntimes, '-r', label="networkx")
    plt.plot(nodes, itimes, '-b', label='igraph')
    plt.plot(nodes, gtimes, '-g', label="graphtool")
    plt.title('Connected Components Efficiency Test')
    plt.xlabel('# of Nodes')
    plt.ylabel('CPU Time (s)')
    plt.legend(loc="upper left")
    plt.savefig('components_testing/combined_test_3_cpu.png')
    plt.show()