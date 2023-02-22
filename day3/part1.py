import csv 
from datetime import datetime

pointsSum = 0

with open('input.txt') as file:
    for line in file:
        fileContent = csv.reader(file, delimiter='\n')
        fileContent = list(fileContent)
        for line in fileContent:
            print(line)
            content = str(line).replace('[\'', '').replace('\']', '')
            length = len(content)
            i = 1
            items = []
            resultFound = False
            for char in content:
                if i <= (length/2): 
                    if char not in items:
                        items.append(char)
                else:
                    for item in items:
                        if ord(item) == ord(char):
                            resultFound = True
                            break
                if(resultFound):
                    # a ... z (1 ... 26), A ... Z (27, 52)
                    if ord(char) >= 97 and ord(char) <= 122:
                        pointsSum += ord(char) - 96
                    elif ord(char) >= 65 and ord(char) <=90:
                        pointsSum += ord(char) - 38
                    break
                i+=1

output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(pointsSum) + '\n')
output.close()