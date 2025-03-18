if __name__ == "__main__":
    eingabe = input("Bitte einen Text eingeben: ")

    woerter = eingabe.split()
    haeufigkeit = {}

    for wort in woerter:
        wort = wort.strip(".,!?;:()\"")
        if wort.isalpha():
            wort = wort.lower()
            haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1

            print(f"Der Text enthält {len(woerter)} Wörter.")
            print("Häufigkeit der Wörter:", haeufigkeit)
