import csv 
from datetime import datetime

pointsSum = 0
i = 0
items = {}
with open('input.txt') as file:
    for line in file:
        fileContent = csv.reader(file, delimiter='\n')
        fileContent = list(fileContent)
        for line in fileContent:
            content = str(line).replace('[\'', '').replace('\']', '')
            print(line)

            if i == 0:
                for char in content:
                    if char not in items:
                        items[char] = 1
            else:
                for char in content:
                    if (char in items) and (items[char] == i):
                        items[char] = items[char] + 1

            i+=1
            if i == 3:
                for d in items:
                    if items[d] == 3:
                        if ord(d) >= 97 and ord(d) <= 122:
                            pointsSum += ord(d) - 96
                        elif ord(d) >= 65 and ord(d) <=90:
                             pointsSum += ord(d) - 38
                        break
                print(items)
                items.clear()
                i = 0


output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(pointsSum) + '\n')
output.close()