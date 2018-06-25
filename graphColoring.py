#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

class Graph:
    def __init__(self, graph):
        self.graph = graph


    def __str__(self):
        return str(self.graph)


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
        all_possible_colors = list(range(k-1, -1, -1))
        #from all colors remove color of adjecents
        for adj in adjacents:
            if coloring[adj] in all_possible_colors:
                all_possible_colors.remove(coloring[adj])

        if len(all_possible_colors) == 0:
            return None

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
        and returns coloring map {node: color}
        if node can't be colored color is None and returns None
        optional argument is coloring: manualy set color for some vertexes
        """

        g = deepcopy(self)

        #if vertex is already colored
        colored = []
        for (vertex, color) in coloring.items():
            colored.append((vertex, g.vertex_adjacents(vertex)))

        #SIMPLIFY
        smaller_vertexes = g.smaller_degree(k)
        stack = []
        while len(smaller_vertexes) > 0:
            vertex = smaller_vertexes[-1]
            stack.append((vertex, g.vertex_adjacents(vertex)))
            g.remove_vertex(vertex)
            smaller_vertexes = g.smaller_degree(k)

        #Optimistic step: maybe vertex could be colored later
        while not g.empty():
            smaller_vertexes = g.smaller_degree(float('inf'))
            vertex = smaller_vertexes[-1]
            stack.append((vertex, g.vertex_adjacents(vertex)))
            g.remove_vertex(vertex)

        #last vertex
        if len(stack) > 0:
            last = stack[-1]
            stack.append((last[1][0], []))

        #append colored vertexes in adjacents
        for (v, adjacents) in colored:
            for adj in adjacents:
                [*map(lambda q: q[1].append(v), filter(lambda t: t[0] == adj, stack))]


        #SELECT
        while len(stack) > 0:
            (v, adj) = stack.pop()
            if v not in coloring.keys():
                coloring[v] = g.min_color(coloring, k, adj)

        if None in coloring.values():
            return None

        return coloring



    def visual_graph_coloring(self, k, coloring = {}):
        """
        Visualize colored graph with k colors
        """
        G_print = nx.Graph()
        G_print.add_edges_from(self.graph)

        colored = self.graph_coloring(k, coloring)
        if colored == None or coloring == {}:
            return None

        list_of_colors = [float(x/k) for x in range(k)]

        #can be colored with less than k colors
        new_colors = []
        s_colored_graph = sorted(coloring.items())
        for (vertex, vertex_color) in s_colored_graph:
            new_colors.append(list_of_colors[vertex_color])

        #draw
        pos = nx.spring_layout(G_print)
        nx.draw_networkx_nodes(G_print, pos, cmap = plt.get_cmap('jet'),
                               nodelist = sorted(G_print.nodes()),
                               node_color = new_colors,
                               node_size = 500)
        nx.draw_networkx_labels(G_print, pos)

        black_edges = G_print.edges()
        nx.draw_networkx_edges(G_print, pos, edgelist = black_edges)
        plt.show()

        return coloring



    def spill(self, k, coloring = {}):
        """
        coloring graph with k colors
        if graph can't be colored with k colors spill
        """
        start_coloring = coloring.copy()

        g = deepcopy(self)

        colored_graph = g.graph_coloring(k, coloring)

        while colored_graph == None:
            spill_list = for_spill(coloring)
            g.remove_vertex(spill_list.pop())
            #TODO izmeniti polazni kod
            coloring = start_coloring.copy()
            colored_graph = g.graph_coloring(k, coloring)

        return colored_graph



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



def for_spill(coloring):
    """
    list of vertexes for spill
    if colored_graph can't be colored with k colors
    (colored_graph is None)
    """
    spill_list = []
    for (spill, color) in coloring.items():
        if color == None:
            spill_list.append(spill)
    return spill_list
