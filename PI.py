#Schreiben Sie ein Programm, das nach Eingabe des Radius in einer Funktion
#den Kreisumfang berechnet.
#Verwenden Sie dazu die Konstante pi aus dem math-Paket.
#
#Die Eingabe soll ein einer eigenen Funktion erfolgen, in der sichergestellt wird, dass es sich dabei
#  a) jedenfalls eine Zahl ist
#und
#  b) eine positive

import math
print(math.pi)


#oder

from math import pi
print(pi)

#oder

import math as m
print(m.pi)

import math

def eingabe():
    correct = False
    
    while correct == False:                #solange bis korrekte Eingabe
        #Tests, ob Eingabe korrekt
        rad1 = input("Eingabe Radius: ")
        try:
            rad = float(rad1)
            correct = True
            
        except ValueError:
            print("Keine gültige Zahl")
            
    return rad

radius = eingabe()

kreisumfang = 2*math.pi*radius
print("der Kreisumfang beträgt: ", kreisumfang)
