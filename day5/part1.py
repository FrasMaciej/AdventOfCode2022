from datetime import datetime

with open('input.txt') as file:
    file.readline()
    fileContent = file.readlines()
    stacks = [[] for i in range(9)]
    for i in range(7, -1, -1):
        for j in range(0, 9):
            if fileContent[i][1 + j*4] != ' ':  # Indeksy: 1 ... 1 + i*4
                stacks[j].append(fileContent[i][1 + j*4])

for i in range(10, len(fileContent)):
    howMany = 0
    fromWhich = 0
    toWhich = 0
    # 2 przypadki w zależności czy how many jest -jedno czy -dwu cyfrowe
    if fileContent[i][6] != ' ':
        howMany = int(fileContent[i][5] + fileContent[i][6])
        fromWhich = int(fileContent[i][13])
        toWhich = int(fileContent[i][18])
    else:
        howMany = int(fileContent[i][5])
        fromWhich = int(fileContent[i][12])
        toWhich = int(fileContent[i][17])

    for j in range(0, howMany):
        # ściąganie i odkładanie elementów na zasadzie stosu
        char = stacks[fromWhich - 1].pop()
        stacks[toWhich - 1].append(char)

print(stacks)
output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: \n')
output.write(str(stacks) + '\n')
output.close()
