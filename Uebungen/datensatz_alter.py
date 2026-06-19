import time
import locale
locale.setlocale(locale.LC_ALL,"de_CH")

while True:
    eingabe = input("Aufnahmedatum (TT.MM.JJJJ): ")
    try:
        aufnahme = time.strptime(eingabe, "%d.%m.%Y")
        break
    except ValueError:
        print("Ungültiges Datum.")

tage = (time.time() - time.mktime(aufnahme)) / 86400
print(f"Datensatz ist {tage:.0f} Tage alt.")

if tage > 365:
    print("Achtung! Datensatz ist älter als 1 Jahr, bitte aktualisieren.")
    
