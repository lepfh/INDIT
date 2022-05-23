#Ändern Sie das Wörterbuch.Beispiel aus LAB 2 wie folgt:

#1) Verwendung eines oder mehrerer Assoziativ.Arrays (dictionary)
#2) Funktion, um übersezte Begriffe auszulesen
#3) Funktion, um den Wörterbuch neue Begirffe hinzufügen

woerterbuch = {"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"}

print("Wählen Sie ihre benötigte Funktion aus") #Ausgabe: Wählen Sie ihre benötigte Funktion aus
print("Wähle [A] zum übersetzen") #Ausgabe: Wähle A zum übersetzten
print("Wähle [B] um ein neues Wort hinzuzufügen") #Ausgabe: Wähle B um ein neues Wort hinzuzufügen
    

    
correct = False
    
while correct == False:       
    eingabe = input("Geben Sie ihre ausgewählte Funktion ein: ") #A oder B muss eingegeben um eine Funktion zu wählen
    
    if eingabe == "A": #Bei der Eingabe A:
        
        word=input("Giben Sie das zu übersetzente Wort ein: ") #Man wird aufgerufen um den gesuchten deutschen Begriff einzugeben
        
        if word in woerterbuch: #Wenn das eingegebene Wort im Wörterbuch enthalten ist:
            print("Übersetzung: ",woerterbuch[word]) #wird die englische Übersetzung angezeigt
            
        else: #anderenfalls
            print('Nicht gefunden!') #wird "nicht gefunden!" ausgegeben
            
    elif eingabe == "B": #Bei der Eingabe B:
        woerterbuch[input('englischer Begriff:')] = [input('deutscher Begriff:')] #wird im Wörterbuch der zuerst eingegebene Begriff als
        #deutsche Übersetzung und danach die zweite Eingabe als dazupassender englischer Begriff gespeichert
        
        
    else: #falls nicht
        print("Nicht möglich!") #wird "nicht möglich!" ausgegeben


