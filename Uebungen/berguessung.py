def begruessung():
    if name.lower().startswith("a"):
        print("Hallo, dein Name ist ganz vorn im Alphabet!")
    else:
        print(f"Hallo {name}, Du bist im Alphabet leider weiter hinten.!")
        
        
def namenseingabe():
    while True:
        try:
            user_name = str(input("Gib deinen Namen ein: "))
            if len(user_name) < 2:
                raise Exception("Name muss mindestens 2 Zeichen lang sein.")
            if any(c.isdigit() for c in user_name):
                raise Exception("Ungültige Eingabe, bitte versuche es erneut.")
            else:
                return user_name
        except ValueError:
            print("Ungültige Eingabe, bitte versuche es erneut.")
        except Exception as e:
            print(e)

    return name

name: Unknown = namenseingabe()
begruessung(name)