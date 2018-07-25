# Global-Register-Allocation
Global register allocation is done as a project for Compiler Construction course at the Faculty of Mathematics in Belgrade, Serbia.

## :floppy_disk: Requirements
- python3.6
- module matplotlib
- module networkx

## Usage
`$ python3.6 main.py [-h] [-v] path numOfRegisters`

- `path` - path to input .txt file with  three-address code and labeld line numbers
- `numOfRegisters` - available number of registers (number of colors - k)
- `v` [optional] - visual graph representation colored with numOfRegisters colors. Spilled variables are still in graph and colored white
- `h` [optional] - help

## Output
- in console:
    - Basic blocks
    - Initial graph (adjacency list)
    - Number of colors used
    - Graph coloring (dictionary)
    - List of spilled variables
    - Name of output file
- `outputCode.txt`:  three-address code with allocated registers

## :mortar_board: Authors
- David Dimic
- Zorana Gajic
