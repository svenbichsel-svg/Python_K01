import math

while True:
    try:
        R = float(input("Bitte Radius eingeben: "))

        if R > 0:
            break
        else:
            print("Der Radius muss positiv sein.")

    except ValueError:
        print("Bitte eine Zahl eingeben.")

D = 2 * R
U = 2 * math.pi * R
A = math.pi * R ** 2

print("Durchmesser:", D)
print("Umfang:", U)
print("Fläche:", A)