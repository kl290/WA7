def woerter_zaehlen():
    eingabe = input("Bitte einen Text eingeben: ")
    woerter = eingabe.split()

    anzahl_zahlen = sum(1 for wort in eingabe.split() if wort.isdigit())
    haeufigkeit = {}

    for wort in woerter:
        wort = wort.strip(".,!?;:()\"")
        if wort:
            wort = wort.lower()
            haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1


    print(f"Der Text enthält {len(woerter)} Wörter, und {anzahl_zahlen} Zahlen insgesamt.")
    print("Häufigkeit der Wörter:", haeufigkeit)

woerter_zaehlen()
