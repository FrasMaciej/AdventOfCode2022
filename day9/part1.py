import csv
from datetime import datetime

with open('input.txt') as file:
    file.readline()
    fileContent = file.readlines()
    # Usuniecie znaków noej linii
    fileContent = [line[:-1] for line in fileContent]


def readSteps(line):
    dir = line[0]
    stepsStr = ''
    for i in range(2, len(line)):
        stepsStr += line[i]
    return int(stepsStr)


# Input: [x,y] number of steps may be bigger than 9!
h_posx = 0
h_posy = 0
t_posx = 0
t_posy = 0

# visitedNodes[[1,2],[3,3]]
# visitedNodes[0][0] - wartość X z pierwszej zapisanej pozycji z listy
# visitedNodes[0][1] - wartość Y z pierwszej zapisanej pozycji z listy
# visitedNodes[1][0] - wartość X z drugiej zapisanej pozycji z listy
# visitedNodes[1][1] - wartość Y z drugiej zapisanej pozycji z listy
visitedNodes = [[0, 0]]

for line in fileContent:
    dir = line[0]
    steps = readSteps(line)

    for i in range(0, steps):

        # print('H: ' + str(h_posx) + ',' + str(h_posy))
        # print('T: ' + str(t_posx) + ',' + str(t_posy))

        # wybór kierunku ruchu przez HEAD
        if dir == 'L':
            h_posx -= 1
        elif dir == 'R':
            h_posx += 1
        elif dir == 'U':
            h_posy += 1
        elif dir == 'D':
            h_posy -= 1

        # sprawdzenie czy TAIL znajduje się we właściwej pozycji
        x_dif = h_posx - t_posx
        y_dif = h_posy - t_posy
        if (abs(x_dif) <= 1) and (abs(y_dif) <= 1):
            continue
        else:
            if y_dif == 0 and x_dif == -2:
                t_posx -= 1
            elif y_dif == 0 and x_dif == 2:
                t_posx += 1
            elif y_dif == -2 and x_dif == 0:
                t_posy -= 1
            elif y_dif == 2 and x_dif == 0:
                t_posy += 1
            elif (y_dif == 1 and x_dif == -2) or (y_dif == 2 and x_dif == -1):
                t_posx -= 1
                t_posy += 1
            elif (y_dif == 2 and x_dif == 1) or (y_dif == 1 and x_dif == 2):
                t_posx += 1
                t_posy += 1
            elif (y_dif == -1 and x_dif == -2) or (y_dif == -2 and x_dif == -1):
                t_posx -= 1
                t_posy -= 1
            elif (y_dif == -2 and x_dif == 1) or (y_dif == -1 and x_dif == 2):
                t_posx += 1
                t_posy -= 1

            # Sprawdzenie czy dany punkt został już odwiedzony, jeśli nie - dodajemy go do listy
            for j in range(0, len(visitedNodes)):
                if (visitedNodes[j][0] == t_posx) and (visitedNodes[j][1] == t_posy):
                    break
                elif j == len(visitedNodes) - 1:
                    visitedNodes.append([t_posx, t_posy])

print(str(len(visitedNodes)))
output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(len(visitedNodes)) + '\n')
output.close()
