#!/usr/bin/env python
# -*- coding: utf-8 -*-

import basicBlock as bb
import parser
import yacc

def livenessAnalysis(basicBlocks):
    bb.ReverseListOfBasicBlocks(basicBlocks)
    bb.PrintBasicBlocks(basicBlocks)

    for block in basicBlocks:
        listOfInstructions = block.__getInstructions__()
        use = set([])
        for instr in listOfInstructions:
            useI, killI = parseInstruction(instr)
            use = use.union(set(useI))
            use = use.difference(set(killI))
            print(use)

def parseInstruction(instruction):
    #remove number of instruction
    instruction = ' '.join(instruction.rsplit()[1:])
    yacc.parse(instruction)
    return parser.use, parser.kill

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    livenessAnalysis(basicBlocks)

if __name__ == "__main__":
    main()
