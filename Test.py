
try:
    r = float(input("Bitte gib den Radius des Kreises ein: "))
except ValueError as e:
    print("Fehler: {e} aufetreten.")
    
print ("Dein Ergebnis: ", {r})