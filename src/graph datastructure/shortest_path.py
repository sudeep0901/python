# build distance table

from queue import Queue
from graph import *
from tkinter import *

import matplotlib.pyplot as plt
import networkx as nx  # nx can be seemed as an alias of networkx module

def build_distance_table(graph, source):
    
    distance_table = {} # vertex and tuple (distance and last preceding node)

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)

    while not  queue.empty():
        current_vertex =  queue.get()
        current_distance =  distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbour][0] is None:
                distance_table[neighbour] = (1+current_distance, current_vertex)

                if len(graph.get_adjacent_vertices(neighbour)) > 0:
                    queue.put(neighbour)

    return distance_table

def shortes_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)
    # print(distance_table)
    path = [destination]

    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex =  distance_table[previous_vertex][1]


    if previous_vertex is None:
        print("there is no path between %d and %d" %(source,destination))
    else:
        path = [source] + path
        print("Shorted path:", path)


g = AdjacencyMatrixGraph(8, directed=False)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(5, 4)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(0, 7)



# G = nx.from_numpy_matrix(g.matrix)
# nx.draw_networkx(G, with_labels=True)
# plt.show()

shortes_path(g, 0, 5)
shortes_path(g, 0, 6)
shortes_path(g, 7, 4)
