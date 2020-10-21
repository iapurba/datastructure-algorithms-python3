#!/usr/bin/env python3

class Graph:
    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}


    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.num_of_nodes += 1
        return self


    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)
        return self

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')
my_graph.add_vertex('F')
my_graph.add_vertex('G')
my_graph.add_vertex('H')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'G')
my_graph.add_edge('B', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')
my_graph.add_edge('C', 'E')
my_graph.add_edge('C', 'F')
my_graph.add_edge('D', 'E')
my_graph.add_edge('E', 'F')
my_graph.add_edge('E', 'H')
my_graph.add_edge('F', 'G')
my_graph.add_edge('G', 'H')

print(my_graph.__dict__)
