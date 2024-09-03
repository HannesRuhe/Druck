# Variabel definieren

# Umrechnungsfaktoren:3
umrechnungsfaktor14 = 14.5037738   # Bar <> PSI
umrechnungsfaktor6894 = 6894.75729 # PSI <> Pascal
umrechnungsfaktor100000 = 100000   # Pascal <> Bar

# while-Schleife
eingabeJaNein = 1
while eingabeJaNein == 1:

# Auswahl Startvariable
    wahl = input("gib eine Auswahl zwischen Bar, PSI oder Pascal an: ").upper()
    
# Umrechnung von Bar in PSI und Pascal    
    if wahl == "BAR":
        inputBar = float(input("Gib den Wert in Bar an: "))
        outputPSI = inputBar * umrechnungsfaktor14
        print(inputBar,"Bar sind",outputPSI,"PSI")
        outputPascal = inputBar * umrechnungsfaktor100000
        print(inputBar,"Bar sind",outputPascal,"Pascal")

# Umrechnung von PSI in Pascal und Bar
    elif wahl == "PSI":
        inputPSI = float(input("Gib den Wert in PSI an: "))
        outputPascal = inputPSI * umrechnungsfaktor6894
        print(inputPSI,"PSI sind",outputPascal,"Pascal")
        outputBar = inputPSI / umrechnungsfaktor14
        print(inputPSI,"PSI sind",outputBar,"Bar")
    
# Umrechnung von Pascal in Bar und PSI
    elif wahl == "PASCAL":
        inputPascal = float(input("Gib den Wert in Pascal an: "))
        outputBar = inputPascal / umrechnungsfaktor100000
        print(inputPascal,"Pascal sind",outputBar,"Bar")
        outputPSI = inputPascal / umrechnungsfaktor6894
        print(inputPascal,"Pascal sind",outputPSI,"PSI")


# Sprung zum Anfang (while-Schleife)
    neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ").upper()
    if neueEingabe == "JA":
        eingabeJaNein = 1
    elif neueEingabe == "NEIN":
        eingabeJaNein = 0