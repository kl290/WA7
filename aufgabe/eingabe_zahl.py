def eingabe_zahl(prompt, min_val = None, max_val = None, return_type = float):
    eingabe = input(prompt)

    try:
        zahl = return_type(eingabe)

        if min_val is not None and zahl < min_val:
            print(f"Die Zahl muss mindestens {min_val} sein!")
            return None

        if max_val is not None and zahl > max_val:
            print(f"Die Zahl darf höchstens {max_val} sein!")
            return None

        return zahl

    except (ValueError, TypeError):
        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben!")
        return None

