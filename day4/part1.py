import csv 
from datetime import datetime

fullyContainsCounter = 0
with open('input.txt') as file:
    for line in file:
        fileContent = csv.reader(file, delimiter='\n')
        fileContent = list(fileContent)
        for line in fileContent:
            content = str(line).replace('[\'', '').replace('\']', '')
            from0 = int(content.partition("-")[0])
            to0 = int(content.partition("-")[2].partition(",")[0])
            from1 = int(content.partition(",")[2].partition("-")[0])
            to1 = int(content.partition(",")[2].partition("-")[2])
            size0 = to0 - from0 + 1
            size1 = to1 - from1 + 1
            
            if size0 >= size1:
                if from0 <= from1 and to0 >= to1:
                    fullyContainsCounter += 1
            else:
                if from1 <= from0 and to1 >= to0:
                    fullyContainsCounter += 1


output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(fullyContainsCounter) + '\n')
output.close()