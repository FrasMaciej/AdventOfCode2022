import csv 
from datetime import datetime

overlapsCounter = 0
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
            
            if (from1 <= to0 and to1 >= from0) or (from0 <= to1 and to0 >= from1):
                overlapsCounter += 1


output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(overlapsCounter) + '\n')
output.close()