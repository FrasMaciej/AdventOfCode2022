import csv 
from datetime import datetime

result = 0

with open('input.txt') as file:
    for line in file:
        fileContent = csv.reader(file, delimiter=' ')
        fileContent = list(fileContent)
    for line in fileContent:
        opponent = line[0]
        me = line[1]

        if opponent == 'A': 
            opponent = 'X'
        elif opponent  == 'B':
            opponent = 'Y'
        elif opponent  == 'C':
            opponent = 'Z'
        
        if me == 'X':
            result += 0
            if opponent == 'X':
                result += 3
            if opponent == 'Y':
                result += 1
            if opponent == 'Z':
                result += 2
        if me == 'Y':
            result += 3
            if opponent == 'X':
                result += 1
            if opponent == 'Y':
                result += 2
            if opponent == 'Z':
                result += 3
        if me == 'Z':
            result += 6
            if opponent == 'X':
                result += 2
            if opponent == 'Y':
                result += 3
            if opponent == 'Z':
                result += 1

output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(result) + '\n')
output.close()