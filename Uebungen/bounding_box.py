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