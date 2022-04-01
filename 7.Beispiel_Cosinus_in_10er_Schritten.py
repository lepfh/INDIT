#Programm, das in 10° - Schritten zwischen 0° und 180° den jew. Cosinus-Wert berechnet und ausgibt

import math

Grad = 0

while Grad <= 180:
    floatErgebnis = Grad*math.pi / 180
    cosinus = math.cos(floatErgebnis)
    print("Winkel: ", Grad, "-> cosinus: ", cosinus)
    Grad += 10
    
    
