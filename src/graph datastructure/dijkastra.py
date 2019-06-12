# build distance table
from queue import Queue
from graph import *
from tkinter import *
import sys

# sys.path.append("D:\github\python\src\graph datastructure\dijkastra\priority_queue.py")
# print(sys.path)
import  priority_dict  

import matplotlib.pyplot as plt
import networkx as nx  # nx can be seemed as an alias of networkx module

def build_distance_table(graph, source):
    
    distance_table = {} # vertex and tuple (distance and last preceding node)

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    distance_table[source] = (0, source)

    priority_queue = priority_dict.priority_dict()
    priority_queue[source]  = 0

    while len(priority_queue.keys()) > 0:
        current_vertex =  priority_queue.pop_smallest()
        current_distance =  distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbour][0] is None:
                distance = (g.get_edge_weight(current_vertex,neighbour) +current_distance)

                neighbour_distance = distance_table[neighbour][0]

                if neighbour_distance is None or neighbour_distance > distance > 0:
                    distance_table[neighbour] = (distance, current_vertex)
                    priority_queue[neighbour] = distance

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

g.add_edge(0, 1,1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 5)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(0, 7, 8)



# G = nx.from_numpy_matrix(g.matrix)
# nx.draw_networkx(G, with_labels=True)
# plt.show()

shortes_path(g, 0, 6)
shortes_path(g, 4, 7)
shortes_path(g, 7, 0)
