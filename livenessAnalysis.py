import basicBlock as bb

def livenessAnalysis(basicBlocks):
    bb.ReverseListOfBasicBlocks(basicBlocks)
    bb.PrintBasicBlocks(basicBlocks)

    # for block in basicBlocks:
    #     listOfInstructions = block.__getInstructions__()
    #     for instr in listOfInstructions:
    #         parseInstruction(instr)

def parseInstruction(instruction):
    use = []
    #
    # instruction = instruction.rsplit()
    # instruction = instruction[1:]

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    livenessAnalysis(basicBlocks)

if __name__=="__main__":
    main()
