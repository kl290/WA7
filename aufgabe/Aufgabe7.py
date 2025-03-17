from eingabe_zahl import eingabe_zahl

if __name__ == "__main__":
    print("Multiplikationstabelle ( kleines 1-mal-1 )")

zahl = eingabe_zahl("Bitte gib eine Zahl ein: ")

for i in range(1, 11):
    print(f"{zahl} * {i} = {zahl * i}")
