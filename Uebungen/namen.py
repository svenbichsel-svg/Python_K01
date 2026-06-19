datei = r"C:\Users\svenb\OneDrive\Desktop\K01\Python_K01\Uebungen\personen.txt"
with open(datei, "r") as lesezugriff:
    inhalt = lesezugriff.readlines()
print(inhalt)

nachnamen = []
for zeile in inhalt:
    teile = zeile.strip().split(" ")
    nachnamen.append(teile[1])

    
nachnamen.sort()

print("Nachnamen alphabetisch sortiert:")
for name in nachnamen:
    print(name)

ausgabe_datei = r"C:\Users\svenb\OneDrive\Desktop\K01\Python_K01\Uebungen\alphabetisch_nachnamen.txt"
 
nachnamen.sort()
 
with open(ausgabe_datei, "w") as schreibzugriff:
    for name in nachnamen:
        schreibzugriff.write(name + "\n")
 
 