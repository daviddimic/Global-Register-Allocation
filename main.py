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
    print("Initial graph: ")
    print(g)

    #number of colors for graph coloring
    k = 5
    #optional: set color for some vertexes
    #coloring = {'5': 0}
    if args.visual:
        colored_graph = g.visual_graph_coloring(k)
        print(colored_graph)
    else:
        colored_graph = g.graph_coloring(k)
        print(colored_graph)


if __name__ == "__main__":
    main()
