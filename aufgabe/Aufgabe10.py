from eingabe_zahl import eingabe_zahl

if __name__ == "__main__":
    print("Taschenrechner!")
    print("Berechnungen: +, -, *, /")


def addition(zahl1, zahl2):
    return zahl1 + zahl2


def subtraktion(zahl1, zahl2):
    return zahl1 - zahl2


def multiplikation(zahl1, zahl2):
    return zahl1 * zahl2


def division(zahl1, zahl2):
    if zahl2 == 0:
        return "Division durch Null ist nicht erlaubt."
    return zahl1 / zahl2


def taschenrechner():
    operationen = {
        "+": addition,
        "-": subtraktion,
        "*": multiplikation,
        "/": division
    }

    while True:
        operation = input("Wähle die Grundrechenart (+, -, *, /): ")

        if operation not in operationen:
            print("Ungültige Auswahl. Bitte versuche es erneut.")
            continue

        zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
        zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")

        ergebnis = operationen[operation](zahl1, zahl2)

        print(f"Das Ergebnis ist: {ergebnis}")
        break


taschenrechner()
