import basicBlock as bb
import parser
import yacc as yacc

def livenessAnalysis(basicBlocks):
    bb.ReverseListOfBasicBlocks(basicBlocks)
    bb.PrintBasicBlocks(basicBlocks)

    # for block in basicBlocks:
    #     listOfInstructions = block.__getInstructions__()
    #     for instr in listOfInstructions:
    #         parseInstruction(instr)
    instructionList = basicBlocks[0].__getInstructions__()
    parseInstruction(instructionList[0])
    #for l in instructionList:
    #    parseInstruction(l)

def parseInstruction(instruction):
    instruction = ' '.join(instruction.rsplit()[1:]) # remove number of instruction
    yacc.parse('ifFalse v >2 goto 4')
    print(parser.use)

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    livenessAnalysis(basicBlocks)

if __name__=="__main__":
    main()
