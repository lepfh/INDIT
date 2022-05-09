#Aufgabe: Wörterbuch DE -> EN

# Kurzes Programm, das nach Eingabe des deutschen Begriffs die englische Übersetzung ausgibt,
# bzw. falls der Begriff nich im Wörterbuch zu finden ist, eine entsprechende Meldung

#Kommentieren Sie Ihren Code

woerterbuch = {"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"} #Das Wörterbuch mit den deutschen und den dazugehörigen englischen Begriff


strObst = input("Geben Sie den deutschen Begriff ein: ")

max = len(woerterbuch) #nicht mehr als 6 Wörter

index = 0

if strObst not in woerterbuch: #wenn die Eingabe nicht im Wörterbuch enthalten ist, dann:
    print("Falsche Eingabe") #zeige: "Falsche Eingabe" an
    
else: #ansonsten:
    print("englische Übersetzung: ", woerterbuch[strObst]) #zeige "englische Übersetzung" plus der englischen Übersetzung, die im Wörterbuch steht
