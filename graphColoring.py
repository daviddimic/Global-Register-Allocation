#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, graph):
        self.graph = graph


    def __str__(self):
        s = ""
        for (v1, v2) in self.graph:
            s += v1 + ": " + v2  + os.linesep
        return s


    def remove_vertex(self, vertex):
        """
        remove vertex from graph
        """
        for_remove = []
        for v in self.graph:
            if v[0] == vertex or v[1] == vertex:
                for_remove.append(v)

        for v in for_remove:
            self.graph.remove(v)


    def degree(self, vertex):
        """
        degree of vertex in graph
        if vertex is not in graph returns None
        """
        deg = 0
        for v in self.graph:
            if v[0] == vertex or v[1] == vertex:
                deg += 1

        return deg if deg else None


    def smaller_degree(self, k):
        """
        list of vertexes with degree smaller than k
        """
        list_smaller_degree = []
        for v in self.graph:
            if v[0] not in list_smaller_degree and self.degree(v[0]) < k:
                list_smaller_degree.append(v[0])
            if v[1] not in list_smaller_degree and self.degree(v[1]) < k:
                list_smaller_degree.append(v[1])

        return list_smaller_degree


    def empty(self):
        return True if len(self.graph) == 0 else False


    def min_color(self, coloring, k, adjacents):
        """
        get first available color from k colors
        """
        all_possible_colors = list(range(k, -1, -1))
        #from all colors remove color od adjecents
        for adj in adjacents:
            if coloring[adj] in all_possible_colors:
                all_possible_colors.remove(coloring[adj])
        return all_possible_colors.pop()


    def vertex_adjacents(self, vertex):
        """
        adjacents list of vertex
        """
        adjacents = []
        for v in self.graph:
            if vertex == v[0]:
                adjacents.append(v[1])
            elif vertex == v[1]:
                adjacents.append(v[0])

        return adjacents


    def graph_coloring(self, k, coloring = {}):
        """
        Coloring graph with <= k colors
        and returns map {node: color}
        if that coloring it's not possible returns None
        """

        #ako je neki cvor vec obojen - dodamo ga u listu obojenih
        colored = []
        for (vertex, color) in coloring.items():
            colored.append((vertex, self.vertex_adjacents(vertex)))

        smaller_vertexes = self.smaller_degree(k)
        stack = []

        while len(smaller_vertexes) > 0:
            vertex = smaller_vertexes[-1]
            stack.append((vertex, self.vertex_adjacents(vertex)))
            self.remove_vertex(vertex)
            smaller_vertexes = self.smaller_degree(k)
        last = stack[-1]
        stack.append((last[1][0], []))

        #uzimanje u obzir susedsva sa vec obojenim cvorovima
        for (v, adjacents) in colored:
            for adj in adjacents:
                [*map(lambda q: q[1].append(v), filter(lambda t: t[0] == adj , stack))]

        if not self.empty():
            return None

        while len(stack) > 0:
            (v, adj) = stack.pop()
            if v not in coloring.keys():
                coloring[v] = self.min_color(coloring, k, adj)

        return coloring


    def visual_graph_coloring(self, k, coloring = {}):
        """
        Visualize colored graph with k colors
        """
        G_print = nx.Graph()
        G_print.add_edges_from(self.graph)


        print("Graph coloring with %d colors" % k)
        colored_graph = self.graph_coloring(k, coloring)
        if colored_graph == None:
            sys.exit("Graph can't be colored with " + str(k)  + " colors!")
        print("Number of colors used: ", used_colors(colored_graph))

        #list_of_colors = ['blue', 'yellow', 'green', 'orange', 'pink', 'magenta', 'aqua', 'red', 'purple', 'gray']
        list_of_colors = [float(x/k) for x in range(k)]

        #can be colored with less than k colors
        new_colors = []
        s_colored_graph = sorted(colored_graph.items())
        for (vertex, vertex_color) in s_colored_graph:
            new_colors.append(list_of_colors[vertex_color])

        #draw
        pos = nx.spring_layout(G_print)
        nx.draw_networkx_nodes(G_print, pos, cmap = plt.get_cmap('jet'),
                               nodelist = sorted(G_print.nodes()),
                               node_color = new_colors,
                               node_size = 400)
        nx.draw_networkx_labels(G_print, pos)

        black_edges = G_print.edges()
        nx.draw_networkx_edges(G_print, pos, edgelist = black_edges)
        plt.show()

        return coloring


def used_colors(colored_graph):
    """
    number of used colors from k colors
    """
    colors = []
    num_of_colors = 0
    for (vertex, color) in colored_graph.items():
        if color not in colors:
            colors.append(color)
            num_of_colors += 1
    return num_of_colors

