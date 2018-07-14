#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import graphColoring as gc
import livenessAnalysis as la

def main():

    #parsing arguments of command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visual', action = "store_true")
    parser.add_argument('path', help = "path to input json file")
    args = parser.parse_args()

    #open input code, do liveness analysis and get adjacents list for graph
    graph = la.modelGraph(la.livenessAnalysis(args.path))

    g = gc.Graph(graph)
    print("Initial graph:")
    print(g)

    #number of colors for graph coloring
    k = 2
    #optional: set color for some vertexes
    #coloring = {'a': 0, 'f':0}
    if args.visual:
        colored_graph, spilled_vertexes = gc.visual_graph_coloring(g, k)
        print("Number of colors used: ", gc.used_colors(colored_graph))
        print("Graph coloring:\n", colored_graph)
        print("Spilled:\n", spilled_vertexes)
    else:
        print(g.spill(k))



if __name__ == "__main__":
    main()
