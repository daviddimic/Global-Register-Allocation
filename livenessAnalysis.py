#!/usr/bin/env python
# -*- coding: utf-8 -*-

import basicBlock as bb
import parser
import yacc

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
        if len(instr) == 1 and list(instr) not in graph:
            graph.append(list(instr))

        for i, node1 in enumerate(instr):
            for node2 in instr[i+1:]:
                t = [node1, node2]
                t_rev = [node2, node1]
                if t not in graph and t_rev not in graph:
                    graph.append(t)
    return graph

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    print(modelGraph(livenessAnalysis(basicBlocks)))

if __name__ == "__main__":
    main()
