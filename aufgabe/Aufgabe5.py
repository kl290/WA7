from .eingabe_zahl import eingabe_zahl

punkte = eingabe_zahl("Geben Sie eine Punktezahl zwischen 0 und 100 ein: ")

n = "Die Note lautet:"

if punkte >= 90:
    print(f"{n} Sehr gut")
elif punkte >= 80:
    print(f"{n} Gut")
elif punkte >= 70:
    print(f"{n} Befriedigend")
elif punkte >= 60:
    print(f"{n} Ausreichend")
else:
    print(f"{n} Nicht bestanden")
