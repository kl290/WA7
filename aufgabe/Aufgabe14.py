def woerter_zaehlen():
    eingabe = input("Bitte einen Satz eingeben: ")

    woerter = eingabe.split()
    anzahl_woerter = len(woerter)
    anzahl_zeichen = len(eingabe)
    anzahl_buchstaben = sum(c.isalpha() for c in eingabe)
    anzahl_ziffern = sum(c.isdigit() for c in eingabe)
    anzahl_whitespaces = sum(c.isspace() for c in eingabe)
    anzahl_sonderzeichen = anzahl_zeichen - (anzahl_buchstaben + anzahl_ziffern + anzahl_whitespaces)

    print("\nStatistik:")
    print(f"Der Satz enthält {anzahl_woerter} Wörter.")
    print(f"Der Satz enthält {anzahl_zeichen} Zeichen.")
    print(f"Der Satz enthält {anzahl_buchstaben} Buchstaben.")
    print(f"Der Satz enthält {anzahl_ziffern} Ziffern.")
    print(f"Der Satz enthält {anzahl_whitespaces} Whitespaces.")
    print(f"Der Satz enthält {anzahl_sonderzeichen} Sonderzeichen.")


woerter_zaehlen()
