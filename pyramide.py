hoehe = 5

for i in range(1, hoehe + 1):
     print("X" * i)


hoehe = 5

    for i in range(1, hoehe + 1):
        print(" " * (hoehe - i) + "X" * i)


hoehe = 5

for i in range(hoehe):
    print(" " * (hoehe - i - 1) + "X" * (2 * i + 1))
