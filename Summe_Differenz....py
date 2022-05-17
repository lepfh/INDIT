def summe(sumand1, sumand2): #Funktion -> def Funktionsnamen(Parameter1, Parameter, ...)
    zwischensumme = sumand1 + sumand2
    return zwischensumme

wert1 = summe(23, 24)
print("wert1: ", wert1)

wert2 = summe(1, 3)
print("summe: ", wert2)

wert3 = summe(wert1, wert2)
print("summe: ", wert3)

#Schreiben Sie ein kurzes Python-Programm, das Sie nach der Eingabe von 2 Zahlen fragt
#und danach die Summe, die Differenz, das Produkt und den Quotienten der beiden Zahlen
#ausgibt.
#Schreiben Sie jeweils eine Funktion zur Berechnung von Summe, Differenz, Produkt und
#Quotient
#Verhindern Sie dass mathematisch unmögliche Berechnungen gestartet werden

import math

Wert1 = int(input("Geben Sie eine Zahlen ein: "))
Wert2 = int(input("Geben Sie einen weiteren Zahlenwert ein: "))


def fsumme(Wert1, Wert2):
    Addition = Wert1 + Wert2
    return Addition

def differenz(Wert1, Wert2):
    Minus = Wert1 - Wert2
    return Minus

def produkt(Wert1, Wert2):
    Ergebnis = Wert1 * Wert2
    return Ergebnis

def quodient(Wert1, Wert2):
    if Wert2 == 0:
        print("Mathematisch unmöglich")
        return
    Ergebnis2 = Wert1 / Wert2
    return Ergebnis2


output1 = fsumme(Wert1, Wert2)
output2 = differenz(Wert1, Wert2)
output3 = produkt(Wert1, Wert2)
output4 = quodient(Wert1, Wert2)

print("Summe: ", output1)
print("Differenz: ", output2)
print("Produkt: ", output3)
print("Quodient: ", output4)