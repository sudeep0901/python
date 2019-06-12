import abc
from queue import Queue
from tkinter import *

import matplotlib.pyplot as plt
import networkx as nx  # nx can be seemed as an alias of networkx module

from graph import *
import time


def breadth_first(graph, start=0):

    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue
        # print("visit: ", vertex)
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)


g = AdjacencyMatrixGraph(9)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

breadth_first(g, 2)
time.sleep(10)

G = nx.from_numpy_matrix(g.matrix)
nx.draw_networkx(G, with_labels=True)
plt.show()


def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1
    # print("Visit: ", current)
    connected_nodes =graph.get_adjacent_vertices(current)
    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


visited = np.zeros(g.numVertices)
depth_first(g, visited)

paths = []

source = 0
dest   = 8

visited = np.zeros(g.numVertices)

def find_print_all_path(g, source,dest, visited, paths):
    # Mark the current node as visited and store in path 

    visited[source] = 1
    paths.append(source)
    if (source == dest):
        print(paths)
    else:
        for adj_vertex in g.get_adjacent_vertices(source):
            # print("Vertext....:" , adj_vertex)
            if visited[adj_vertex] == 0:
                # visited[adj_vertex] = 1
                # print("visited: ", adj_vertex)
                find_print_all_path(g, adj_vertex, dest, visited,  paths)

    # Remove current vertex from path[] and mark it as unvisited 
    paths.pop() 
    visited[source]= 0

def print_all_path(g,source,dest):
    print("source vertex is :-----------", source)
    print("destination vertex is :-----------", dest)

    visited = np.zeros(g.numVertices)
    paths = []
    find_print_all_path(g, source, dest, visited, paths)

# print_all_path(g,0,8)


def find_paths(g , source, dest ,paths):
    visited[source] = 1
    if(visited[source] !=0):
        visited[source] =1

    paths.append(source)
    if (source == dest):
        print(paths)
    for adj_vertex in g.get_adjacent_vertices(source):
        # print(adj_vertex)
        time.sleep(2)
        if (visited[adj_vertex] == 0):
            print("new vertex:",adj_vertex)
            find_paths(g, adj_vertex, dest, paths)
    
    paths.pop()
    visited[source] = 0


find_paths(g , source, dest, paths)

directedgraph = AdjacencyMatrixGraph(9,True)

directedgraph.add_edge(0, 1)
directedgraph.add_edge(0, 2)
directedgraph.add_edge(1, 3)
directedgraph.add_edge(0, 8)
directedgraph.add_edge(3, 5)

directedgraph.add_edge(2, 3)
directedgraph.add_edge(4, 8)
directedgraph.add_edge(6, 4)
directedgraph.add_edge(6, 7)
directedgraph.add_edge(7, 8)
directedgraph.add_edge(8, 0)



G = nx.from_numpy_matrix(directedgraph.matrix)
nx.draw_networkx(G , with_labels=True)
plt.show()
find_paths(directedgraph , source, dest, paths)
