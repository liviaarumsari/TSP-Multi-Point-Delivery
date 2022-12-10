import numpy as np
from multiStopRoute import findMinRoute

# Location data
loc_data = np.array([[0, 0.85, 1.7, 3.8, 4.7, 3.3, 3.5, 4.8], 
            [1.2, 0, 1.2, 3.8, 5.3, 3.4, 4.0, 5.3], 
            [1.7, 1.7, 0, 4.9, 3.9, 4.4, 3.1, 4.9], 
            [1.9, 2.4, 2.6, 0, 4.8, 4.8, 2.9, 4.2],
            [4.7, 4.7, 3.5, 5.4, 0, 7.4, 1.4, 2.0],
            [3.5, 3.4, 4.8, 2.4, 7.0, 0, 5.2, 6.5],
            [3.8, 3.8, 2.9, 5.5, 1.9, 6.5, 0, 0.95],
            [3.8, 4.9, 4.1, 4.0, 2.6, 6.2, 0.75, 0]])
place_name = ["Institut Teknologi Bandung", "Unpad Dipatiukur", "Gedung Sate", "Ciwalk", "Alun-alun Bandung", "Universitas Katolik Parahyangan", "Stasiun Bandung", "Paskal 23 Hyper Square"]


menu = """
=============Welcome to Multi-stop Delivery Route Optimization=============

Here is the available location you can choose as your stop:
"""
print(menu)
for i in range(len(place_name)):
    print(str(i+1) + ". " + place_name[i])
print()

while True:
    startPoint = int(input("Choose your starting point: "))
    if (startPoint >= 1 and startPoint <= 8):
        stopList = np.array([startPoint-1])
        break
    else:
        print("Please input the number available!")

while True:
    stopSum = int(input("Choose how many stops you want to make: "))
    if(startPoint > 0 and startPoint < 8):
        break
    else:
        print("Please input 1 - 7 amount of stops!")

for i in range (1,stopSum+1):
    stopPoint = int(input("Stop " + str(i) + ": "))
    stopList = np.append(stopList, [stopPoint-1]) 

while True:
    isBack = input("Do you want to go back to your starting point after the last stop? (y/n) ")
    if (isBack.lower() == "y" or isBack.lower() == "n"):
        break
    else:
        ("Please input y or n!")

print(stopList)
filteredRow = loc_data[stopList]
filteredLoc = filteredRow[:,stopList]

if (isBack.lower() == "y"):
    sum, route = findMinRoute(filteredLoc, True)
else:
    sum, route = findMinRoute(filteredLoc, False)

print(f'The shortest route you could take from your starting point with a total distance of {sum} kilometers is: ')
print(place_name[startPoint-1], end="")
locFormat = " - {place}"
for i in range (len(route)):
    place = place_name[stopList[route[i]-1]]
    print(f' - {place}', end="")
