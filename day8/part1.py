import csv 
from datetime import datetime

fileContent = []
with open('input.txt') as file:
    file.readline()
    fileContent = file.readlines()

visibleTrees = 0
# [y][x] !!!
for y in range(0, len(fileContent[0]) ):
    for x in range(0, len(fileContent) -1 ):
        if y == 0 or y == (len(fileContent[0]) - 1) or x == 0 or x == (len(fileContent) - 2):
            visibleTrees += 1
        else:
            isVisible = False

            for i in range (x - 1, -1, -1):
                if fileContent[y][x] > fileContent[y][i]:
                    if i == 0:
                        isVisible = True
                        visibleTrees += 1
                        break
                    continue
                else:
                    break
            if isVisible:
                continue
            
            for i in range (x + 1, len(fileContent) - 1):
                if fileContent[y][x] > fileContent[y][i]:
                    if i == (len(fileContent) - 2):
                        isVisible = True
                        visibleTrees += 1
                        break
                    continue
                else:
                    break
            if isVisible:
                continue

            for i in range (y + 1, len(fileContent[0]) - 1):
                if fileContent[y][x] > fileContent[y][i]:
                    if i == (len(fileContent) - 1):
                        isVisible = True
                        visibleTrees += 1
                        break
                    continue
                else:
                    break
            if isVisible:
                continue

            for i in range (y - 1, -1, -1):
                if fileContent[y][x] > fileContent[y][i]:
                    if i == (len(fileContent) - 1):
                        isVisible = True
                        visibleTrees += 1
                        break
                    continue
                else:
                    break
            if isVisible:
                continue

output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(visibleTrees) + '\n')
output.close()