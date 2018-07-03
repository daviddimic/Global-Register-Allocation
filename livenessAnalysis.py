import basicBlock as bb

def livenessAnalysis(basicBlocks):
    bb.ReverseListOfBasicBlocks(basicBlocks)
    bb.PrintBasicBlocks(basicBlocks)

def main():
    fileName = 'testBasicBlocks/bbtest2.txt'
    basicBlocks = bb.CreateListOfBasicBlocksFromFile(fileName)
    livenessAnalysis(basicBlocks)

if __name__=="__main__":
    main()
