def eingabe():
    satz = input("Bitte einen Satz eingeben: ").strip()

    return satz.split()


def woerter_zaehlen():
    wort_liste = eingabe()

    woerter_anzahl = len(wort_liste)

    print(f"Der Satz enthält {woerter_anzahl} Wörter.")


woerter_zaehlen()