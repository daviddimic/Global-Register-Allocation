#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BasicBlock:
    """
    startBB and endBB represent the instructions with which basic block starts/ends
    inBB represents variables used in basic block
    """
    def __init__(self, startBB, endBB, instructions, inBB):
        self.startBB = startBB
        self.endBB = endBB
        self.instructions = instructions
        self.inBB = inBB

    def __str__(self):
        str = ""
        header = "---------\n"
        str += header
        for instr in self.instructions:
            str += instr + "\n"
        str += header
        return str

    def __reverse__(self):
        self.instructions = self.instructions[::-1]

    def __getInstructions__(self):
        return self.instructions

def getPairs(instructions):
    """
    Method: getPairs
    Return: a list of toupples (start, end) with indexes of begining and end of each basic block
    """
    leaders = getLeaders(instructions)
    n = len(instructions)

    leadersLen = len(leaders)
    pairStartEnd = []

    # we create a pair for each leader
    for i in range(0, leadersLen):
        startBB = int(leaders[i].rsplit(' ')[0].rsplit(':')[0])
        if(i+1 != leadersLen):
            endBB = int(leaders[i+1].rsplit(' ')[0].rsplit(':')[0])
        else:
            endBB = n
        pairStartEnd.append((startBB, endBB))
    return pairStartEnd

def getLeaders(instructions):
    """
    Method: getLeaders
    Return: a list of leader instructions in 3 address code
    Leader instructions:
      - First instruction is always a leader instruction
      - Instruction on which we jump with goto is a leader instruction
      - First instruction after instruction that contains goto is a leader instruction
    """
    leaders = [instructions[0]]
    n = len(instructions)

    for i in range(0, n):
        if(instructions[i].__contains__("goto")):
            if((i+1)!=n):
                leaders.append(instructions[i+1])

            instructions[i].rstrip(' ')
            # returns a list of strings splited by space
            num = instructions[i].rsplit(' ')
            # minus one because of the indexing
            leaders.append(instructions[int(num[-1])-1])
            # print("Goto " + str(int(num[-1]))) line on which we jump with goto

    leaders.sort(key = lambda l: int(l.rsplit(' ')[0].rsplit(':')[0]))
    return leaders

def getLeadersFromFile(fileName):
    instructions = getInstructionsFromFile(fileName)
    return getLeaders(instructions)

def getInstructionsFromFile(fileName):
    with open(fileName, 'r') as f:
        instructions = [line.rstrip('\n') for line in f]
        return instructions

def CreateListOfBasicBlocks(pairs, instructions):
    basicBlocks = []
    n = len(instructions)

    for pair in pairs:
        if(n != pair[1]):
             # so the last block catches the last instruction
            basicBlocks.append(BasicBlock(pair[0], pair[1], instructions[pair[0]-1:pair[1]-1], set([])))
            # in indexing the instructions first is minus one because of indexing a list starts from zero
            # the second minus one so we don't catch the last instruction of lock which belongs to next block
            #print(instructions[pair[0]-1:pair[1]-1])
        else:
            basicBlocks.append(BasicBlock(pair[0], pair[1], instructions[pair[0]-1:pair[1]], set([])))
            #print(instructions[pair[0]-1:pair[1]])
    return basicBlocks

def CreateListOfBasicBlocksFromFile(fileName):
    instructions = getInstructionsFromFile(fileName)
    pairs = getPairs(instructions)
    return CreateListOfBasicBlocks(pairs, instructions)

def ReverseListOfBasicBlocks(basicBlocks):
    for b in basicBlocks:
        b.__reverse__()
    basicBlocks.reverse()

def PrintPairs(pairs):
    print("Pairs of start end indexes of basic block: ")
    print("---------------------")
    for i in pairs:
        print(i)
    print ("---------------------")

def PrintLeaderInstructions(leaders):
    print ("Leader instructions: ")
    print ("---------------------")
    for leader in leaders:
        print(leader)
    print ("---------------------")

def PrintBasicBlocks(basicBlocks):
    print ("Basic Blocks: ")
    for bb in basicBlocks:
        print(bb)

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = CreateListOfBasicBlocksFromFile(fileName)
    PrintBasicBlocks(basicBlocks)

if __name__ == "__main__":
    main()
