#! /usr/bin/python
from __future__ import print_function
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)

    for line in range(len(tableData)):
        for word in range(len(tableData[line])):
            if colWidths[line] <= len(tableData[line][word]):
                colWidths[line] = len(tableData[line][word])

    for col in range(len(tableData[0])-1):
        for row in range(len(tableData)):
            print(tableData[row][col].rjust(colWidths[row]+1),end = '')
        print()
printTable()
