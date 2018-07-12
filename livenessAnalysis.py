#!/usr/bin/env python
# -*- coding: utf-8 -*-

import basicBlock as bb
import parser
import yacc
from functools import reduce


def livenessAnalysis(basicBlocks):
    livenessList = []

    bb.ReverseListOfBasicBlocks(basicBlocks)
    bb.PrintBasicBlocks(basicBlocks)

    use = set([])
    # REPEAT UNTIL NEMA PROMENA U IN B
    for block in basicBlocks: # i nije exitBB

        listOfInstructions = block.__getInstructions__()
        #outB = # UNIJA SVIH INOVA SLEDBENIKA

        for instr in listOfInstructions:
            useI, killI = parseInstruction(instr)
            use = use.union(set(useI))
            use = use.difference(set(killI))
            print(use) #TODO remove
            livenessList.append(list(use))

        block.setInBB(use)

    return livenessList


def parseInstruction(instruction):
    #remove number of instruction
    instruction = ' '.join(instruction.rsplit()[1:])
    yacc.parse(instruction)
    return parser.use, parser.kill


def modelGraph(livenessList):
    """
    model adjacency list (for graph coloring) from liveness list
    """
    graph = []

    for instr in livenessList:
        if len(instr) == 1 and [instr[0], instr[0]] not in graph:
            #don't add [a] if [a, _] or [_, a] already exists in graph
            used_nodes = reduce(lambda a,b: a + b, graph) if graph != [] else []
            if instr[0] not in used_nodes:
                graph.append([instr[0], instr[0]])

        for i, node1 in enumerate(instr):
            for node2 in instr[i+1:]:
                t = [node1, node2]
                t_rev = [node2, node1]

                #if exist [a]
                #remove [a] and later add [a, _] or [_, a]
                if [node1, node1] in graph:
                    graph.remove([node1, node1])
                if [node2, node2] in graph:
                    graph.remove([node2, node2])

                #add [a, b] if [a, b] or [b, a] don't exist in graph
                if t not in graph and t_rev not in graph:
                    graph.append(t)

    return graph


def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    print(modelGraph(livenessAnalysis(basicBlocks)))


if __name__ == "__main__":
    main()
