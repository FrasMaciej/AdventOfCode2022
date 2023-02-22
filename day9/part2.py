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
t_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [
    0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

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

        # wybór kierunku ruchu przez HEAD
        if dir == 'L':
            t_pos[0][0] -= 1
        elif dir == 'R':
            t_pos[0][0] += 1
        elif dir == 'U':
            t_pos[0][1] += 1
        elif dir == 'D':
            t_pos[0][1] -= 1
        # sprawdzenie czy TAIL znajduje się we właściwej pozycji
        for k in range(0, len(t_pos) - 1):
            x_dif = t_pos[k][0] - t_pos[k+1][0]
            y_dif = t_pos[k][1] - t_pos[k+1][1]
            if (abs(x_dif) <= 1) and (abs(y_dif) <= 1):
                continue
            else:
                if y_dif == 0 and x_dif == -2:
                    t_pos[k+1][0] -= 1
                elif y_dif == 0 and x_dif == 2:
                    t_pos[k+1][0] += 1
                elif y_dif == -2 and x_dif == 0:
                    t_pos[k+1][1] -= 1
                elif y_dif == 2 and x_dif == 0:
                    t_pos[k+1][1] += 1
                elif (y_dif == 1 and x_dif == -2) or (y_dif == 2 and x_dif == -1) or (y_dif == 2 and x_dif == -2):
                    t_pos[k+1][0] -= 1
                    t_pos[k+1][1] += 1
                elif (y_dif == 2 and x_dif == 1) or (y_dif == 1 and x_dif == 2) or (y_dif == 2 and x_dif == 2):
                    t_pos[k+1][0] += 1
                    t_pos[k+1][1] += 1
                elif (y_dif == -1 and x_dif == -2) or (y_dif == -2 and x_dif == -1) or (y_dif == -2 and x_dif == -2):
                    t_pos[k+1][0] -= 1
                    t_pos[k+1][1] -= 1
                elif (y_dif == -2 and x_dif == 1) or (y_dif == -1 and x_dif == 2) or (y_dif == -2 and x_dif == 2):
                    t_pos[k+1][0] += 1
                    t_pos[k+1][1] -= 1
                # Sprawdzenie czy dany punkt został już odwiedzony, jeśli nie - dodajemy go do listy (dla ogona)
                if k == (len(t_pos) - 2):
                    for j in range(0, len(visitedNodes)):
                        if (visitedNodes[j][0] == t_pos[k+1][0]) and (visitedNodes[j][1] == t_pos[k+1][1]):
                            break
                        elif j == len(visitedNodes) - 1:
                            visitedNodes.append([t_pos[k+1][0], t_pos[k+1][1]])

output = open("output2.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + str(len(visitedNodes)) + '\n')
output.close()
