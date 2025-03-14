def eingabe():
    zahlen = input("Bitte eine Liste von Zahlen eingeben (durch Kommas getrennt): ").strip()
    return [int(z) for z in zahlen.split(",")]


def groesste_zahl():
    zahlen = eingabe()
    groesste = max(zahlen)
    print(f"Die größte Zahl in der Liste ist: {groesste}")


groesste_zahl()
