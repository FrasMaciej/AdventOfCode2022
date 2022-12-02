import csv
from datetime import datetime

sums = []

with open('input.txt') as file:
    value = 0
    for line in file:
        if not line.strip():
            sums.append(value)
            value = 0
        else:
            value += int(line)

sums.sort(reverse=True)
maxValue = sums[0]
topThreeSum = sums[0] + sums[1] + sums[2]

output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Max: ' + str(maxValue) + '\n')
output.write('Top3 sum: ' + str(topThreeSum) + '\n')
output.close()
