import random

from eingabe_zahl import eingabe_zahl

if __name__ == "__main__":
    min_val = 1
    max_val = 100

    zufallszahl = random.randint(min_val, max_val)
    print(f"Ich habe eine Zahl zwischen {min_val} und {max_val} gewählt. Versuche, sie zu erraten!")

    geraten = False
    while not geraten:
        rateversuch = eingabe_zahl(f"Gib deine Schätzung ein ({min_val}-{max_val}): ")

        if rateversuch < zufallszahl:
            print("Zu niedrig!")
        elif rateversuch > zufallszahl:
            print("Zu hoch!")
        else:
            print("Glückwunsch! Du hast die richtige Zahl erraten.")
            geraten = True
