while 1:
    strWetter = input("Geben Sie das Wetter ein: ")
    
    if strWetter.upper() == "SONNIG" or strWetter.upper() == "SONNE":
        print("Gartenparty")
    elif strWetter.upper() == "REGNERISCH" or strWetter.upper() == "REGEN":
        print("Kellerparty")
    else:
        print("falsche Eingabe")
