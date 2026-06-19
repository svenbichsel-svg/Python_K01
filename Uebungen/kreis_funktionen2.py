import math


def calc_diameter(r):
    return r * 2


def circumference(r):
    return r * 2 * math.pi


def calc_area(r):
    return r**2 * math.pi


def check_radius_input():
    """Fetches radius from user input and checks, if it is a valid float.

    Returns:
        A float value of the radius from the user input.
    """
    while True:
        r = input("Bitte Radius als Zahl eingeben: ")
        try:
            # Versuchen, Benutzereingabe in eine Flieskommazahl 'float' umzuwandeln...
            r = float(r)
            # ...wenn das klappt, while-Schleife abbrechen, wenn der Radius >=0 ist.
            if r < 0:
                raise Exception(
                    "Radius darf nicht negativ sein"
                )  # too broad exception, aber passt für Demo-Zwecke
            break
        except ValueError:
            # ...sonst den User um erneute Eingabe bitten
            print("Bitte eine Zahl eingeben")
        except Exception:  # too broad, aber passt für Demo-Zwecke
            print("Bitte eine positive Zahl eingeben")
    return r


# Läuft nur, wenn die Datei direkt gestartet wird und nicht beim Import in eine andere Datei
if __name__ == "__main__":
    radius = check_radius_input()
    print("Durchmesser:", calc_diameter(radius))
    print("Umfang: " + str(circumference(radius)))
    print(f"Fläche: {calc_area(radius)}")