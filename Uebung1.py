# Dieser Funktion mach eine Schleife, die die Wochentage ausgibt


week = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
#print(week)

for w in range(0,7):
    print(week[w])
print("Ende der Woche")

# Eine Schleife, die die Zahlen von 0 bis 10 ausgibt und sagt, ob sie gerade oder ungerade sind
for zahlen in range(11):
    if zahlen % 2 == 0:
        print(zahlen, "ist gerade")
    else:
        print(zahlen, "ist ungerade")

# Pause 
zahl = 1
while zahl <= 10:
    print(zahl)
    if zahl == 5:
        print("Abbruchkriterium erfuellt")
        break
    zahl += 1
print("Schleife fertig")