#Schreiben Sie ein Programm, das auf 2 mögliche Versionen, die in der Liste aufgefürten Personen begrüßt
#Z.B. "Hallo, Peter!"
#
#Version 1 : for-SChleife im Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
#
#Version 2 : for-Schleife und Ausgabe der Begrüßung in einem Unterprogramm

namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo ", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm")

def begruessung2(namenliste):
    for ein_name in namenliste:
        print("Hallo ", ein_name)
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm")   

print("Version 1")
for name in namen:
    begruessung(name)
    
print("Version 2")
begruessung2(namen)
  
