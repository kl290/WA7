def eingabe_zahl(prompt, min_val = None, max_val = None, return_type = float):
    while True:
        eingabe = input(prompt)

        try:
            zahl = return_type(eingabe)

            if min_val is not None and zahl < min_val:
                print(f"Die Zahl muss mindestens {min_val} sein!")
                continue

            if max_val is not None and zahl > max_val:
                print(f"Die Zahl darf höchstens {max_val} sein!")
                continue

            return zahl

        except (ValueError, TypeError):
            print(f"Ungültige Eingabe '{eingabe}'. Bitte eine gültige Zahl eingeben!")

