#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import graphColoring as gc
import livenessAnalysis as la


def spilledVarsWriteToFile(inPath, outPath, spilled_vertexes, coloring):
    #open input file
    inFile = open(inPath, 'r')

    instructions = inFile.readlines()
    new_instructions = []
    for instr in instructions:

        varFromMemory = []
        varToMemory = []

        for spilled in spilled_vertexes:
            var_def = ""
            use = ""
            if instr.find(':=') != -1:
                #left and right od ':='
                var_def = instr.split(':=')[0]
                #if there is [a], a shoud be 'use', not 'def'
                if var_def.find('[') != -1:
                    use = (var_def.split('[')[1]).split(']')[0]
                    var_def = ""
                var_use =  instr.split(':=')[1] + use
            else:
                var_use = instr

            if var_def.find(spilled) != -1:
                    varToMemory.append(spilled)
            if var_use.find(spilled) != -1:
                    varFromMemory.append(spilled)


        #definition of variable spilled
        for spilled in varFromMemory:
            new_instructions.append("x: {} := M[{}_loc]\n".format(spilled, spilled))

        new_instructions.append(instr)

        #use variable spilled
        for spilled in varToMemory:
            new_instructions.append("x: M[{}_loc] := {}\n".format(spilled, spilled))

    inFile.close()

    #replace all variables that is not spilled with their allocated register
    instructions = []
    for instr in new_instructions:
        for k, v in coloring.items():
            instr = instr.replace(' ' + k, ' r' + str(v))
        instructions.append(instr)

    changeInstrNumerationAndWrite(instructions, outPath)


def changeInstrNumerationAndWrite(instructions, outPath):
    #open output file and write new instructions
    outFile = open(outPath, 'w')

    #change numeration
    for num, instr in enumerate(instructions):
        new_instr = instr

        #change goto number
        if instr.find('goto') != -1:
            gotoNum = int(instr.split(' ')[-1])
            new_goto = numOfInsertedInstr(gotoNum, instructions) + gotoNum
            new_instr = instr.rsplit(' ', 1)[0] + ' ' + str(new_goto) + '\n'

        #remove instruction number
        instr = new_instr.split(':', 1)[1].lstrip()
        #new number apply
        instr = str(num+1) + ": " + instr
        outFile.write(instr)

    outFile.close()


def numOfInsertedInstr(currentInstrNum, instructions):
    num = 0
    for instr in instructions:
        i = instr.split(':', 1)[0].strip()
        if i == 'x':
            num += 1
        elif int(i) >= currentInstrNum:
            return num
    return num



def main():
    #parsing arguments of command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visual', action = "store_true")
    parser.add_argument('path', help = "path to input json file")
    parser.add_argument('numOfRegisters', type = int, help = "number of registers")
    args = parser.parse_args()

    #open input code, do liveness analysis and get adjacents list for graph
    graph = la.modelGraph(la.livenessAnalysis(args.path))

    outPath = "outputCode.txt"

    g = gc.Graph(graph)
    print("Initial graph:")
    print(g)

    #number of colors for graph coloring
    k = int(args.numOfRegisters)
    #optional: set color for some vertexes
    #coloring = {'a': 0, 'f':0}
    if args.visual:
        colored_graph, spilled_vertexes = gc.visual_graph_coloring(g, k)
    else:
        colored_graph, spilled_vertexes = g.spill(k)

    print("Number of colors used: ", gc.used_colors(colored_graph))
    print("Graph coloring: ", colored_graph)
    print("Spilled: ", spilled_vertexes)
    spilledVarsWriteToFile(args.path, outPath, spilled_vertexes, colored_graph)
    print("OUTPUT FILE: ", outPath)

if __name__ == "__main__":
    main()
