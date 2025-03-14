print("Multiplikationstabelle ( kleines 1-mal-1 )")

from .eingabe_zahl import eingabe_zahl

zahl = eingabe_zahl("Bitte gib eine Zahl ein: ")

for i in range(1, 11):
    print(f"{zahl} * {i} = {zahl * i}")
