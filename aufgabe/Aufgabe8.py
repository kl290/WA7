print("Durchschnittsberechner")


def eingabe_zahlen():
    while True:
        eingabe = input("Bitte gib die Zahlen ein, getrennt durch Leerzeichen: ").strip()

        if not eingabe:
            print("Es wurden keine Zahlen eingegeben. Bitte versuche es erneut.")
            continue

        try:
            return list(map(float, eingabe.split()))
        except ValueError:
            print("Bitte gib gültige Zahlen ein.")



zahlen = eingabe_zahlen()

durchschnitt = sum(zahlen) / len(zahlen)
print(f"Der Durchschnitt der eingegebenen Zahlen ist: {durchschnitt}")