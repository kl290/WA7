def groesste_zahl():
    while True:
        zahlen = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ").strip()

        if not zahlen:
            print("Es wurden keine Zahlen eingegeben. Bitte versuche es erneut.")
            continue

        try:
            zahlen_liste = [int(z) for z in zahlen.split(",")]
            groesste = max(zahlen_liste)
            print(f"Die größte Zahl in der Liste ist: {groesste}")
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte nur Zahlen durch Kommas trennen.")


groesste_zahl()
