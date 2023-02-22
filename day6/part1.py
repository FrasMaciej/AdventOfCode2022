import csv
from datetime import datetime


def findSolution():
    with open('input.txt') as file:
        file.readline()
        fileContent = file.readline()
        for i in range(0, len(fileContent) - 3):
            chars = [fileContent[i], fileContent[i+1],
                     fileContent[i+2], fileContent[i+3]]
            solution = isUnique(chars, i)
            if solution:
                return solution


def isUnique(chars, i):
    for j in range(1, len(chars)):
        for k in range(0, j):
            if chars[j] == chars[k]:    # Nastąpiło powtórzenie
                return False
            elif k == 2:                # Znaleziono rozwiązanie
                solution = i + 4        # +4 -> +1 bo indeksy, +3 bo i to pierwszy znak ciągu
                return solution


solution = findSolution()
print(solution)
output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(solution) + '\n')
output.close()
