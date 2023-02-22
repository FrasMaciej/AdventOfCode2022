import csv
from datetime import datetime
import queue

with open('input.txt') as file:
    file.readline()
    fileContent = file.read().split()

sum = 0

xreg = 1
cycleNumber = 0
ordersQueue = queue.Queue()
pendingCycles = 2
pixel = 0

for i in range(0, len(fileContent)):
    if fileContent[i] == 'addx':
        ordersQueue.put(fileContent[i+1])
        i += 1

    cycleNumber += 1

    if cycleNumber == 20 or (((20 + cycleNumber) % 40) == 0):
        sum += (xreg * cycleNumber)

    if not ordersQueue.qsize() == 0:
        pendingCycles -= 1
        if pendingCycles == 0:
            val = int(ordersQueue.get())
            xreg += val
            pendingCycles = 2

while ordersQueue.qsize() != 0:
    cycleNumber += 1
    if cycleNumber == 20 or (((20 + cycleNumber) % 40) == 0):
        sum += (xreg * cycleNumber)

    pendingCycles -= 1
    if pendingCycles == 0:
        val = ordersQueue.get()
        xreg += int(val)
        pendingCycles = 2


output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(sum) + '\n')
output.close()
