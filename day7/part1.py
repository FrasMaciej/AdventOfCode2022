import csv 
from datetime import datetime

sizeSum = 0
with open('input.txt') as file:
    file.readline()
    fileContent = file.readlines()
    
    iteration = 0
    linesToCheck = []

    for lines in fileContent:
        depth = -1
        size = 0

        if lines[0 : 4] == '$ cd' and lines[5 : 7] != '..':
            lineFound = True
            linesToCheck = fileContent [iteration : len(fileContent)]
        else:
            lineFound = False

        if lineFound:
            for line in linesToCheck:
                if line[0 : 7] == '$ cd ..':
                    depth -= 1
                elif line[0 : 4] == '$ cd' and line[5 : 7] != '..':
                    depth += 1
                
                if depth < 0:
                    break

                if ord(line[0]) >= 49 and ord(line[0]) <= 57:
                    i = 0
                    fileSizeStr = ''
                    while ord(line[i]) >= 48 and ord(line[i]) <= 57:
                        fileSizeStr = fileSizeStr + line[i]
                        i += 1
                    size += int(fileSizeStr)
            if size <= 100000:
              sizeSum += size
        iteration+=1


output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(sizeSum) + '\n')
output.close()