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
            result +=1
        elif me == 'Y':
            result +=2
        elif me == 'Z':
            result +=3

        if opponent == me:
            result += 3
        elif opponent == 'X' and me == 'Y':
            result+=6
        elif opponent == 'X' and me == 'Z':
            result+=0
        elif opponent == 'Y' and me == 'X':
            result+=0
        elif opponent == 'Y' and me == 'Z':
            result+=6
        elif opponent == 'Z' and me == 'X':
            result+=6
        elif opponent == 'Z' and me == 'Y':
            result+=0

output = open("output1.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(result) + '\n')
output.close()