from .eingabe_zahl import eingabe_zahl

Zahl = eingabe_zahl("Bitte geben Sie eine Zahl ein (Wenn Kommazahl, dann getrennt durch . (2.5): ")

if Zahl == 0:
    print("Die eingegebene Zahl ist 0!")
elif Zahl > 0:
    print("Die eingegebene Zahl ist positiv!")
else:
    print("Die eingegebene Zahl ist negativ!")
