#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, json
import argparse
import graphColoring as gc

def main():

    #parsing arguments of command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visual', action = "store_true")
    parser.add_argument('path', help = "path to input json file")
    args = parser.parse_args()

    #open input graph
    try:
        with open(args.path, "r") as f:
            graph = json.load(f)
    except IOError as e:
        sys.exit(e)

    g = gc.Graph(graph)
    print("Initial graph:")
    print(g)

    #number of colors for graph coloring
    k = 4
    #optional: set color for some vertexes
    #coloring = {'a': 1, 'f':2}
    if args.visual:
        colored_graph = g.visual_graph_coloring(k)
        if colored_graph == None:
            print("Graph can't be colored with ", k, " colors!")
        else:
            print("Number of colors used: ", gc.used_colors(colored_graph))
            print(colored_graph)
    else:
        coloring = {}
        colored_graph = g.graph_coloring(k, coloring)
        if colored_graph == None:
            print("Graph can't be colored with ", k, " colors!")
            print(coloring)

            #vertex_for_spill
            #remove vertex
            #color again
            for (spill, color) in coloring.items():
                if color == None:
                    print(spill)
                    g.remove_vertex(spill)
                    colored_graph = g.graph_coloring(k)
                    print(g)
                    print(colored_graph)
        else:
            print(colored_graph)


if __name__ == "__main__":
    main()
