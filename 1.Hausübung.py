# Hausübung 1
# Aufgabenstellung:
#  Programm schreiebn das Pi anhand der Leibniz-Reihe berechnet
#  Anzahl der Terme sollen frei eingegeben werde

#Die Werte die in der While-Schleife verwendet werden zu beginn definieren (0 setzen)
intTerm = 0
floatPi = 0            
summe = 0


strVariable = input("Geben Sie die Anzahl der zu berechneten Terme ein: ") #Eine (Gleitkomma)zahl wird eingegeben
intVariable = int(strVariable) #Bei der eingegebenen Zahl wird die Kommastelle abgeschnitten


while intTerm <= intVariable: #While-Schleife beginnt / solange intTerm kleiner gleich intVariable ist
    
    floatPi = (((-1)**intTerm)/(2*intTerm+1)) #In der Formel wird die Zahl eingesetzt das ergibt eine Gleitkommazahl
    summe += floatPi #Summe ist alles floatPi zusammengezählt
    intTerm += 1 #Formel beginnt mit 1 und jedes mal wird 1 dazugezählt bis die Zahl gleich groß wie die eingegebene Zahl ist
    
    
print("Das Ergebniss beträgt: ", summe*4) #Summe wird mit 4 multipliziert und angezeitg