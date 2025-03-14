from eingabe_zahl import eingabe_zahl


print("Dieser Rechner berechnet die Summe, Differenz, Multiplikation und Division von 2 Zahlen.")

Zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
Zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")

print(f"{Zahl1} + {Zahl2} = {Zahl1 + Zahl2}")
print(f"{Zahl1} - {Zahl2} = {Zahl1 - Zahl2}")
print(f"{Zahl1} * {Zahl2} = {Zahl1 * Zahl2}")

if Zahl2 != 0:
    print(f"{Zahl1} / {Zahl2} = {Zahl1 / Zahl2}")
else:
    print("Division durch 0 ist nicht erlaubt!")
