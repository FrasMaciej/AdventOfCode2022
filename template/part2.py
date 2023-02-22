import csv 
from datetime import datetime

with open('input.txt') as file:
    file.readline()
    fileContent = file.readline()

output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + '' + '\n')
output.close()