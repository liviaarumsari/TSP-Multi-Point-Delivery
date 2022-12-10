import numpy as np
from multiStopRoute import findMinRoute

menu = """
=============Welcome to Multi-stop Delivery Route Optimization=============

Here is the available location you can choose as your stop:
1. Institut Teknologi Bandung
2. Unpad Dipatiukur
3. Gedung Sate
4. Ciwalk
5. Alun-alun Bandung
6. Universitas Katolik Parahyangan
7. Stasiun Bandung
8. Paskal 23 Hyper Square

"""
print(menu)

startPoint = input("Choose your starting point: ")
stopSum = input("Choose how many stops you want to make: ")
stopList = []

for i in range (1,stopSum+1):
    stopPoint = input("Stop " + str(i) + ": ")
    np.append(stopList, stopPoint - 1)
