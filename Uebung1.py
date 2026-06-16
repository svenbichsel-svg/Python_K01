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



# Diese Funktion zählt die Punkte in einer Box und gibt aus, ob sie in der Box sind oder nicht. 
punkte = [
    {'name': 'A', 'ost': 2600100, 'nord': 1200200},
    {'name': 'B', 'ost': 2601500, 'nord': 1201000},
    {'name': 'C', 'ost': 2599800, 'nord': 1199500},
    {'name': 'D', 'ost': 2600800, 'nord': 1200600},
    {'name': 'E', 'ost': 2602000, 'nord': 1198000},
]

bbox = {'ost_min': 2600000, 'ost_max': 2601000,
        'nord_min': 1200000, 'nord_max': 1201000}

Anzahl_I=0
Anzahl_A=0  
        
for punkt in punkte:
    if (bbox['ost_min'] <= punkt['ost'] <= bbox['ost_max'] and
        bbox['nord_min'] <= punkt['nord'] <= bbox['nord_max']):
        print(punkt['name'], "ist in der Box")
        Anzahl_I += 1
    else:
        print(punkt['name'], "ist nicht in der Box")
        Anzahl_A += 1
        
print("Anzahl Punkte in der Box:", Anzahl_I)
print("Anzahl Punkte ausserhalb der Box:", Anzahl_A)



# Diese Funktion fragt den Benutzer nach seinem Namen und Alter und gibt eine Begrüssung aus.
user_name = input("Bitte gib deinen Namen ein:")
print("Hallo", user_name, "guten Tag")
user_alter = input("Was ist dein Alter, " + user_name + "? ")
print("Du bist", user_alter, "Jahre alt.")