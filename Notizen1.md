# Tag 1

## Auf GitHub hochladen
    git add -A
    git commit -m "Initial commit"
    git push origin main

## Übungen Tag 1

# Code

    hoehe = 5

    for i in range(1, hoehe + 1):
        print("X" * i)

    X
    XX
    XXX
    XXXX
    XXXXX

    hoehe = 5

    for i in range(1, hoehe + 1):
        print(" " * (hoehe - i) + "X" * i)

        X
       XX
      XXX
     XXXX
    XXXXX


    hoehe = 5

    for i in range(hoehe):
        print(" " * (hoehe - i - 1) + "X" * (2 * i + 1))

        X
       XXX
      XXXXX
     XXXXXXX
    XXXXXXXXX

    import string

    for zeile in range(8, 0, -1):
        for spalte in string.ascii_lowercase[:8]:
            print(spalte + str(zeile), end=" ")
        print()

    a8 b8 c8 d8 e8 f8 g8 h8
    a7 b7 c7 d7 e7 f7 g7 h7
    a6 b6 c6 d6 e6 f6 g6 h6
    a5 b5 c5 d5 e5 f5 g5 h5
    a4 b4 c4 d4 e4 f4 g4 h4
    a3 b3 c3 d3 e3 f3 g3 h3
    a2 b2 c2 d2 e2 f2 g2 h2
    a1 b1 c1 d1 e1 f1 g1 h1


    zahlen = [1, 2, 3, 4, 5, 6]

    summe = 0

    for zahl in zahlen:
        summe += zahl
    print(summe)

    21




# Tag 2

## Übungen Tag 2









# Beispiele


    Normaler Text. **Fett**, *kursiv*, ~~durchgestrichen~~.

    - Aufzählungspunkt
    - noch einer
    - eingerückt (zwei Leerzeichen Einzug)

    1. Nummerierte Liste
    2. zweiter Punkt
    
    - [ ] Aufgabe noch offen
    - [x] Aufgabe erledigt
    
    > Blockzitat - gut für wichtige Hinweise oder Definitionen
        
        `inline code` - für Variablennamen, Befehle, Dateipfade

    # Codeblock: vier Leerzeichen Einzug
    punkte = [1, 2, 3]
    
    [Linktext](https://example.com)
    
    | Spalte 1 | Spalte 2 | 
    | :---     | :---     |
    | Wert A   | Wert B   |