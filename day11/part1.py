import csv
from datetime import datetime


monkeys = []
with open('input.txt') as file:
    file.readline()
    fileContent = file.readlines()
    lineNum = 0
    for i in range(0, 8):
        # Id małpki
        monkeyId = fileContent[lineNum][7]
        # Startowe itemy małpki
        monkeyStartingItems = []
        j = 18
        while (j < len(fileContent[lineNum+1])):
            numStr = ''
            numberFound = False
            while ord(fileContent[lineNum+1][j]) >= 48 and ord(fileContent[lineNum+1][j]) <= 57:
                numStr += fileContent[lineNum+1][j]
                j += 1
                numInt = int(numStr)
                numberFound = True
            if numberFound:
                monkeyStartingItems.append(numInt)
            j += 1
        # Operacja małpki
        # Test małpki
        # If true testu
        # If false testu
        print(monkeyStartingItems)
        lineNum += 7

# Sekwencja zdarzeń
# 1. Inspekcja kolejnych przedmitów wszystkich posiadanych przedmiotów przez kolejną małpę
# 2. Podzielnie worry level przez 3 i zaokrąglenie do najbliższego integera
# 3. Wyrzucenie przedmiotu, który trafia na koniec listy małpy do której ma on trafić

# Jeżeli małpa nie posiada przedmiotów a jej tura rozpoczyna się to wtedy pomijamy turę i przechodzimy do nastepnej małpy

output = open("output.txt", "a")
output.write(str(datetime.now()) + ':\n')
output.write('Result: ' + '' + '\n')
output.close()
