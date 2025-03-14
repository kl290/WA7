eingabe = input("Bitte geben Sie ein Wort ein: ")


def ist_palindrom(s):
    return s == s[::-1]


eingabe = eingabe.lower().replace(" ", "")

if not eingabe:
    print("Die leere Eingabe wird nicht als Palindrom gewertet.")

else:
    if ist_palindrom(eingabe):
        print(f'"{eingabe}" ist ein Palindrom.')
    else:
        print(f'"{eingabe}" ist kein Palindrom.')
