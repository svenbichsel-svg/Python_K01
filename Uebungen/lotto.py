import random

def lottoziehung(): 
    ziehung = set()
    while len(ziehung) < 6:
        ziehung.add(random.randint(1, 42))
    return ziehung

def benutzereingabe():
    while True:
        try:
            eingabe = input("Gib 6 Zahlen ein (1-42): ")
            zahlen = set(int(z) for z in eingabe.split())
            if len(zahlen) != 6:
                print("Bitte genau 6 verschiedene Zahlen eingeben.")
            elif not all(1 <= z <= 42 for z in zahlen):
                print("Alle Zahlen müssen zwischen 1 und 42 sein.")
            else:
                return zahlen
        except ValueError:
            print("Bitte nur Zahlen eingeben.")

tipp = benutzereingabe()
print(f"\nDeine Tipps: {sorted(tipp)}")

versuche = 0
while True:
    versuche += 1
    if lottoziehung() == tipp:
        break

print(f"Anzahl Ziehungen bis 6 Richtige: {versuche:,}")