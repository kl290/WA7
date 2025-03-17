if __name__ == "__main__":
    satz = input("Bitte einen Satz eingeben: ").strip()
    wort_liste = satz.split()
    woerter_anzahl = len(wort_liste)
    print(f"Der Satz enthält {woerter_anzahl} Wörter.")
