import csv
from datetime import datetime


def findSolution():
    with open('input.txt') as file:
        file.readline()
        fileContent = file.readline()
        for i in range(0, len(fileContent) - 13):
            chars = []
            for j in range(0, 14):
                chars.append(fileContent[i+j])
            solution = isUnique(chars, i)
            if solution:
                return solution


def isUnique(chars, i):
    for j in range(1, len(chars)):
        for k in range(0, j):
            if chars[j] == chars[k]:
                return False
            elif k == len(chars)-2:
                solution = i + 14
                return solution


solution = findSolution()
print(solution)
output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(solution) + '\n')
output.close()
